"""Independent exact checks for discovery certificates.

Coordinates (x,y) mean Euclidean (x, sqrt(3)*y).  This module does not
import catalogue geometry or the search engine.  A periodic certificate is
proved by congruence, exact area, and disjoint interiors for ALL lattice
translates, including translates beyond an arbitrary 3-by-3 neighbourhood.
It verifies positive evidence; it does not certify completeness or UNSAT.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import ceil, floor
from pathlib import Path


class VerificationError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def area2(poly):
    return abs(sum(cross(p, q) for p, q in zip(poly, poly[1:]+poly[:1])))


def points(raw):
    require(isinstance(raw, (list, tuple)), "polygon must be a sequence")
    require(all(len(p) == 2 and all(type(v) is int for v in p) for p in raw),
            "coordinates must be exact integers")
    return tuple(tuple(p) for p in raw)


def hull(raw):
    pts = sorted(set(raw))
    if len(pts) < 3:
        return tuple(pts)
    chains = []
    for seq in (pts, pts[::-1]):
        chain = []
        for p in seq:
            while len(chain) >= 2 and cross(sub(chain[-1],chain[-2]),sub(p,chain[-1])) <= 0:
                chain.pop()
            chain.append(p)
        chains.append(chain[:-1])
    return tuple(chains[0]+chains[1])


def convex_polygon(raw):
    poly = points(raw)
    require(len(poly) >= 3 and len(set(poly)) == len(poly), "degenerate/repeated polygon vertices")
    # Reject crossings and backtracking even if the vertex set has a convex hull.
    turns = [cross(sub(poly[(i+1)%len(poly)],p),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)]))
             for i,p in enumerate(poly)]
    require(all(t >= 0 for t in turns) or all(t <= 0 for t in turns), "polygon is not convex in boundary order")
    require(area2(poly) == area2(hull(poly)) > 0, "polygon does not traverse its convex hull once")
    require(all(cross(sub(q,p),sub(r,p)) >= 0 for p,q in zip(hull(poly), hull(poly)[1:]+hull(poly)[:1]) for r in poly),
            "invalid polygon")
    return hull(poly)


def cell_polygon(cell):
    require(len(cell) == 4 and all(type(v) is int for v in cell), "invalid cell ID")
    i,j,o,k = cell
    require(o in (0,1) and k in (0,1,2), "invalid cell orientation/corner")
    a = (12*i+6*j,6*j)
    u,v = (a[0]+12,a[1]),(a[0]+6,a[1]+6)
    face = (a,u,v) if o == 0 else (u,(a[0]+18,a[1]+6),v)
    before, corner, after = face[(k-1)%3],face[k],face[(k+1)%3]
    mid = lambda p,q: ((p[0]+q[0])//2,(p[1]+q[1])//2)
    center = (sum(p[0] for p in face)//3,sum(p[1] for p in face)//3)
    return corner,mid(corner,after),center,mid(before,corner)


def inside(poly, p):
    return all(cross(sub(q,a),sub(p,a)) >= 0 for a,q in zip(poly,poly[1:]+poly[:1]))


def verify_cells_polygon(raw_cells, raw_polygon):
    cells = [tuple(c) for c in raw_cells]
    require(len(cells) == len(set(cells)) > 0, "duplicate or empty cells")
    poly = convex_polygon(raw_polygon)
    for cell in cells:
        cpoly = cell_polygon(cell)
        require(area2(cpoly) == 24, "invalid kite area")
        require(all(inside(poly,p) for p in cpoly), "cell is outside polygon")
    # Grid cells have disjoint interiors; containment + equal areas proves equality.
    require(area2(poly) == 24*len(cells), "polygon differs from union of its cells")
    return poly


def squared_distance(p,q):
    d = sub(p,q)
    return d[0]*d[0]+3*d[1]*d[1]


def congruent(a,b):
    """All Euclidean isometries, without imposing grid rotations/phases."""
    a,b = convex_polygon(a),convex_polygon(b)
    if len(a) != len(b):
        return False
    n = len(a)
    for direction in (1,-1):
        for offset in range(n):
            if all(squared_distance(a[i],a[j]) == squared_distance(b[(offset+direction*i)%n],b[(offset+direction*j)%n])
                   for i in range(n) for j in range(i)):
                return True
    return False


def interiors_overlap(a,b):
    """Strict separating-axis test, invariant under our affine coordinates."""
    for poly in (a,b):
        for p,q in zip(poly,poly[1:]+poly[:1]):
            edge = sub(q,p)
            ap = [cross(edge,v) for v in a]
            bp = [cross(edge,v) for v in b]
            if max(ap) <= min(bp) or max(bp) <= min(ap):
                return False
    return True


def shift(poly,vector):
    return tuple((p[0]+vector[0],p[1]+vector[1]) for p in poly)


def _checked_placements(cert):
    types = {}
    for tile in cert['prototiles']:
        require(tile['id'] not in types, "duplicate prototile ID")
        types[tile['id']] = verify_cells_polygon(tile['cells'],tile['polygon'])
    require(types, "no prototiles")
    polygons = []
    for item in cert['placements']:
        require(item['tile'] in types, "unknown placement tile")
        poly = verify_cells_polygon(item['cells'],item['polygon'])
        require(congruent(poly,types[item['tile']]), "placement is not congruent to prototile")
        polygons.append(poly)
    require(polygons, "no placements")
    return polygons


def verify_periodic(cert):
    polys = _checked_placements(cert)
    u,v = points(cert['period_vectors'])
    det = cross(u,v)
    require(det != 0, "period vectors are dependent")
    if 'domain_hnf' in cert:
        a,b,c = cert['domain_hnf']
        require(all(type(x) is int for x in (a,b,c)) and a > 0 and c > 0 and 0 <= b < a,
                "invalid HNF domain")
        require((u,v) == ((12*a,0),(12*b+6*c,6*c)), "period vectors disagree with HNF")
    require(sum(area2(p) for p in polys) == 2*abs(det), "period area is not covered exactly once")
    bounds = []
    for poly in polys:
        alpha = [Fraction(cross(p,v),det) for p in poly]
        beta = [Fraction(cross(u,p),det) for p in poly]
        bounds.append((min(alpha),max(alpha),min(beta),max(beta)))
    checks = 0
    for i,a in enumerate(polys):
        ai,ax,aj,ay = bounds[i]
        for j in range(i,len(polys)):
            bi,bx,bj,by = bounds[j]
            for m in range(ceil(ai-bx),floor(ax-bi)+1):
                for n in range(ceil(aj-by),floor(ay-bj)+1):
                    if i == j and m == n == 0:
                        continue
                    translation = (m*u[0]+n*v[0],m*u[1]+n*v[1])
                    require(not interiors_overlap(a,shift(polys[j],translation)),
                            f"periodic overlap: placements {i},{j}, lattice shift {m},{n}")
                    checks += 1
    if 'domain_hnf' in cert:
        a,b,c = cert['domain_hnf']
        residues = []
        for item in cert['placements']:
            item_residues = []
            for i,j,o,k in item['cells']:
                quotient,j = divmod(j,c)
                item_residues.append(((i-quotient*b)%a,j,o,k))
            if 'wrapped_cells' in item:
                require(sorted(tuple(cell) for cell in item['wrapped_cells']) == sorted(item_residues),
                        'stored wrapped cells disagree with actual reduction')
            residues.extend(item_residues)
        expected = {(i,j,o,k) for i in range(a) for j in range(c)
                    for o in range(2) for k in range(3)}
        require(len(residues) == len(set(residues)) and set(residues) == expected,
                "wrapped cells do not cover the fundamental domain exactly once")
    # The periodic union is closed. Equal area and no overlaps leave no open gap.
    return {'valid':True,'kind':'periodic','placements':len(polys),
            'area2':2*abs(det),'translated_overlap_checks':checks}


def verify_patch(cert):
    polys = _checked_placements(cert)
    occupied = set()
    for i,(item,poly) in enumerate(zip(cert['placements'],polys)):
        cells = {tuple(c) for c in item['cells']}
        require(not occupied.intersection(cells), "patch repeats a cell")
        occupied.update(cells)
        require(all(not interiors_overlap(poly,p) for p in polys[:i]), "patch polygons overlap")
    targets = {tuple(c) for c in cert['target_cells']}
    for cell in targets:
        cell_polygon(cell)
    require(targets <= occupied, "patch fails target-cell coverage")
    if 'seed_index' in cert:
        require(type(cert['seed_index']) is int and 0 <= cert['seed_index'] < len(polys), "invalid seed index")
    return {'valid':True,'kind':'patch','placements':len(polys),'target_cells':len(targets),
            'scope':'target coverage only; no claim of extendibility or complete coronas'}


def digest(value):
    raw = json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def congruence_signature(poly):
    poly = convex_polygon(poly)
    n = len(poly)
    words = []
    for direction in (1,-1):
        for offset in range(n):
            ordered = [poly[(offset+direction*i)%n] for i in range(n)]
            words.append(tuple(squared_distance(p,q) for p in ordered for q in ordered))
    return (n,)+min(words)


def verify_screen(data):
    """Check the retained all-positive funnel, binding every witness to its tile.

    Catalogue completeness is a separate mathematical/enumeration claim and
    must be replayed; this function checks every supplied catalogue record.
    The intentionally narrow envelope rejects theorem omissions and negative
    screens rather than treating them as machine-verified conclusions.
    """
    require(data['schema'] == 'arisearch.discovery.screen.v1', "unknown screen schema")
    require(digest({k:v for k,v in data.items() if k not in ('result_sha256','execution')}) == data['result_sha256'],
            "result hash mismatch")
    require(digest(data['catalogue']) == data['catalogue_sha256'], "catalogue hash mismatch")
    provenance = data['provenance']
    require(provenance['use_theorems'] is False, "only all-witness screens are verified here")
    require(set(provenance['source_sha256']) == {'kite_grid.py','screen.py','render.py'}, "incomplete source hashes")
    for name,expected in provenance['source_sha256'].items():
        actual = hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest()
        require(actual == expected, f"source hash mismatch: {name}")
    require(provenance['catalogue_input'] is None, "external catalogue completeness is not covered")
    require(type(provenance['max_cells']) is int and provenance['max_cells'] > 0, "invalid catalogue size bound")
    catalogue = {}
    signatures = set()
    for tile in data['catalogue']:
        require(tile['id'] not in catalogue, "duplicate catalogue ID")
        poly = verify_cells_polygon(tile['cells'],tile['polygon'])
        signature = congruence_signature(poly)
        require(tuple(tile['signature']) == signature, "catalogue congruence signature mismatch")
        require(signature not in signatures, "duplicate congruent catalogue polygons")
        signatures.add(signature)
        require(tile['area_cells'] == len(tile['cells']) <= provenance['max_cells'], "catalogue area bound mismatch")
        require(tile['side_count'] == len(poly), "catalogue side count mismatch")
        lengths = [squared_distance(p,q) for p,q in zip(poly,poly[1:]+poly[:1])]
        require(tile['edge_squared_lengths'] == lengths, "catalogue edge lengths mismatch")
        angle_data = []
        for i,p in enumerate(poly):
            before,after = sub(poly[i-1],p),sub(poly[(i+1)%len(poly)],p)
            angle_data.append({'dot':before[0]*after[0]+3*before[1]*after[1],
                               'norm_product_squared':squared_distance(poly[i-1],p)*squared_distance(poly[(i+1)%len(poly)],p)})
        require(tile['angle_cos_data'] == angle_data, "catalogue angle data mismatch")
        require(tile['embeddings'], "catalogue has no mesh embeddings")
        for cells in tile['embeddings']:
            embedding_poly = hull(p for c in cells for p in cell_polygon(c))
            verify_cells_polygon(cells,embedding_poly)
            require(congruent(poly,embedding_poly), "catalogue embedding has a different shape")
        catalogue[tile['id']] = tile
    require(catalogue, "empty catalogue")
    budgets = data['budgets']
    require(type(budgets['max_index']) is int and budgets['max_index'] > 0, "invalid period bound")
    require(budgets['workers'] == 1 and budgets['solve_seconds'] > 0 and budgets['deterministic_time'] > 0,
            "invalid solver budget")
    domains = [(a,b,index//a) for index in range(1,budgets['max_index']+1)
               for a in range(1,index+1) if index%a == 0 for b in range(a)]
    seen = set()
    checked = []
    for row in data['singletons']:
        tile_id = row['tile']
        require(tile_id in catalogue and tile_id not in seen, "invalid or duplicate singleton reference")
        seen.add(tile_id)
        require(row['status'] == 'PERIODIC_WITNESS', "retained screen is not all-positive")
        witness = row['witness']
        require(digest(witness) == row['witness_sha256'], "witness hash mismatch")
        require(len(witness['prototiles']) == 1 and witness['prototiles'][0]['id'] == tile_id,
                "singleton witness refers to different prototiles")
        proto = witness['prototiles'][0]
        tile = catalogue[tile_id]
        require({tuple(c) for c in proto['cells']} == {tuple(c) for c in tile['cells']}
                and convex_polygon(proto['polygon']) == convex_polygon(tile['polygon']),
                "witness prototile differs from catalogue definition")
        attempts = row['attempts']
        require(0 < len(attempts) <= len(domains), "invalid attempts list")
        require([tuple(a['hnf']) for a in attempts] == domains[:len(attempts)], "period attempts are not the bounded HNF prefix")
        require(all(a['status'] in ('INFEASIBLE','UNKNOWN','MODEL_INVALID') for a in attempts[:-1]),
                "search continued past a successful witness")
        require(attempts[-1]['status'] in ('OPTIMAL','FEASIBLE')
                and attempts[-1]['hnf'] == witness['domain_hnf'], "witness disagrees with successful attempt")
        checked.append({'tile':tile_id,**verify_periodic(witness)})
    require(seen == set(catalogue), "singleton records omit catalogue tiles")
    require(data['pairs'] == [], "all-positive singleton funnel must have no eligible pairs")
    expected = {'catalogue':len(catalogue),'monohedral_theorem':0,'monohedral_periodic':len(catalogue),
                'unresolved_singletons':0,'remaining_unordered_pairs':0,'periodic_pairs':0,'unresolved_pairs':0}
    require(data['funnel'] == expected, "funnel disagrees with verified witnesses")
    return {'valid':True,'kind':'screen','catalogue_records':len(catalogue),'funnel':expected,
            'witnesses':checked,'scope':'all supplied records verified; catalogue completeness requires generator proof and replay'}


def verify_certificate(cert):
    if cert.get('schema') == 'arisearch.discovery.screen.v1':
        return verify_screen(cert)
    if 'period_vectors' in cert:
        return verify_periodic(cert)
    return verify_patch(cert)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    result = [verify_certificate(c) for c in data] if isinstance(data,list) else verify_certificate(data)
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
