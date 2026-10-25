"""Solver-free exact validation of developed native honeycomb certificates.

Stored (x,y) means physical (x,sqrt(3)*y). A finite certificate proves a
geometric native disk, not its extension to the whole plane. Native radii
count dual-graph steps; no maximal Euclidean-corona claim is inferred.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
from fractions import Fraction
import json
import hashlib
from itertools import combinations, product
from math import ceil, floor, gcd
from functools import reduce
from pathlib import Path

from .verify import (VerificationError, area2, convex_polygon, cross, hull,
                     digest, interiors_overlap, points, require, shift, sub)

DIRECTIONS = ((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
STEPS = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))


def canonical_word(word):
    word = tuple(word)
    return min(seq[i:]+seq[:i] for seq in (word,word[::-1]) for i in range(6))


def word_polygon(word):
    require(len(word) == 6 and all(type(v) is int and v > 0 for v in word),
            'side word must contain six positive exact integers')
    result = []
    p = (0,0)
    for length,direction in zip(word,DIRECTIONS):
        result.append(p)
        p = p[0]+length*direction[0],p[1]+length*direction[1]
    require(p == (0,0), 'side word does not close')
    poly = tuple(result)
    require(len(convex_polygon(poly)) == 6, 'word does not form a strict convex hexagon')
    return poly


def face_distance(a,b=(0,0)):
    i,j = a[0]-b[0],a[1]-b[1]
    return max(abs(i),abs(j),abs(i+j))


def disk_faces(radius,seed=(0,0)):
    return {(seed[0]+i,seed[1]+j) for i in range(-radius,radius+1)
            for j in range(-radius,radius+1) if max(abs(i),abs(j),abs(i+j)) <= radius}


def _on_segment(p,a,b):
    return cross(sub(b,a),sub(p,a)) == 0 and all(min(a[k],b[k]) <= p[k] <= max(a[k],b[k]) for k in (0,1))


def segments_meet(a,b,c,d):
    ab_c,ab_d = cross(sub(b,a),sub(c,a)),cross(sub(b,a),sub(d,a))
    cd_a,cd_b = cross(sub(d,c),sub(a,c)),cross(sub(d,c),sub(b,c))
    if ab_c*ab_d < 0 and cd_a*cd_b < 0:
        return True
    return any((value == 0 and _on_segment(p,u,v)) for value,p,u,v in
               ((ab_c,c,a,b),(ab_d,d,a,b),(cd_a,a,c,d),(cd_b,b,c,d)))


def _boxes_disjoint(a,b):
    return any(max(p[k] for p in a) < min(p[k] for p in b)
               or max(p[k] for p in b) < min(p[k] for p in a) for k in (0,1))


def polygons_touch(a,b):
    if _boxes_disjoint(a,b):
        return False
    return any(segments_meet(p,q,r,s) for p,q in zip(a,a[1:]+a[:1])
               for r,s in zip(b,b[1:]+b[:1]))


def _checked_records(cert):
    types = {}
    for item in cert['prototiles']:
        require(item['id'] not in types, 'duplicate prototile ID')
        word = tuple(item['word'])
        expected = word_polygon(word)
        require(points(item['polygon']) == expected, 'prototile polygon disagrees with side word')
        types[item['id']] = canonical_word(word)
    require(types, 'no prototiles')
    records = {}
    for item in cert['placements']:
        require(item['tile'] in types, 'unknown placement species')
        face = tuple(item['face'])
        origin = tuple(item['origin'])
        require(len(face) == len(origin) == 2 and all(type(v) is int for v in face+origin),
                'face and origin must be exact integer pairs')
        require(face not in records, 'duplicate face assignment')
        word = tuple(item['word'])
        local = word_polygon(word)
        require(canonical_word(word) == types[item['tile']], 'placement side word is not congruent to species')
        poly = shift(local,origin)
        require(points(item['polygon']) == poly, 'placement polygon disagrees with origin and side word')
        if 'state_id' in item:
            canonical = types[item['tile']]
            orbit = sorted({seq[k:]+seq[:k] for seq in (canonical,canonical[::-1]) for k in range(6)})
            require(item['state_id'] == f"{item['tile']}:o{orbit.index(word):02d}", 'state ID disagrees with directed/reflected word')
        records[face] = {'word':word,'local':local,'origin':origin,'polygon':poly,'tile':item['tile']}
    require(records, 'empty face assignment')
    if 'species_present' in cert:
        require(cert['species_present'] == sorted({item['tile'] for item in records.values()}), 'species-present summary mismatch')
    return records


def _edge_displacement(here,there,k):
    require(here['word'][k] == there['word'][(k+3)%6], 'matched sides have unequal lengths')
    # Reversed identification of full side endpoints. Equivalent to
    # here[k+1]-there[k+3], but checked independently at both endpoints.
    displacement = sub(here['local'][k],there['local'][(k+4)%6])
    require(displacement == sub(here['local'][(k+1)%6],there['local'][(k+3)%6]),
            'matched side endpoints disagree')
    return displacement


def develop_patch(records,seed):
    """Develop without trusting any certificate origin; check every cycle."""
    developed = {seed:records[seed]['origin']}
    queue = deque([seed])
    edge_count = 0
    while queue:
        face = queue.popleft()
        here = records[face]
        for k,step in enumerate(STEPS):
            neighbor = (face[0]+step[0],face[1]+step[1])
            if neighbor not in records:
                continue
            delta = _edge_displacement(here,records[neighbor],k)
            origin = (developed[face][0]+delta[0],developed[face][1]+delta[1])
            if neighbor in developed:
                require(developed[neighbor] == origin, 'nonzero development holonomy around a native cycle')
            else:
                developed[neighbor] = origin
                queue.append(neighbor)
            edge_count += 1
    require(len(developed) == len(records), 'native assignment is disconnected')
    require(all(developed[f] == item['origin'] for f,item in records.items()), 'stored origins disagree with independent development')
    return edge_count//2


def verify_patch(cert):
    records = _checked_records(cert)
    seed = tuple(cert['seed_face'])
    radius = cert['symbolic_radius']
    require(type(radius) is int and radius >= 0, 'invalid symbolic radius')
    require(set(records) == disk_faces(radius,seed), 'faces do not equal the asserted native disk')
    require(len(records) == 1+3*radius*(radius+1), 'native disk cardinality mismatch')
    if cert.get('seed_tile') is not None:
        require(records[seed]['tile'] == cert['seed_tile'], 'seed species mismatch')
    edges = develop_patch(records,seed)
    faces = sorted(records)
    for i,face in enumerate(faces):
        for other in faces[:i]:
            a,b = records[face]['polygon'],records[other]['polygon']
            if _boxes_disjoint(a,b):
                continue
            require(not interiors_overlap(a,b), f'developed patch overlaps: {face}, {other}')
            require(face_distance(face,other) == 1 or not polygons_touch(a,b),
                    f'nonnative boundary contact: {face}, {other}')
    return {'valid':True,'kind':'boundary_patch','placements':len(records),
            'native_radius':radius,'native_edges':edges,'layer_counts':[1]+[6*r for r in range(1,radius+1)],
            'scope':'developed native graph ball only; no infinite extension or maximal Euclidean-corona claim'}


def _wrap_face(face,hnf):
    a,b,c = hnf
    n,j = divmod(face[1],c)
    m,i = divmod(face[0]-n*b,a)
    return (i,j),m,n


def verify_periodic(cert):
    records = _checked_records(cert)
    hnf = tuple(cert['domain_hnf'])
    require(len(hnf) == 3 and all(type(x) is int for x in hnf), 'invalid HNF')
    a,b,c = hnf
    require(a > 0 and c > 0 and 0 <= b < a, 'invalid HNF')
    require(set(records) == {(i,j) for i in range(a) for j in range(c)}, 'periodic face representatives do not cover HNF domain')
    vectors = points(cert['period_vectors'])
    require(len(vectors) == 2, 'need two period vectors')
    u,v = vectors
    det = cross(u,v)
    require(det != 0, 'dependent geometric periods')
    seam_checks = 0
    for face,here in records.items():
        for k,step in enumerate(STEPS):
            neighbor,m,n = _wrap_face((face[0]+step[0],face[1]+step[1]),hnf)
            there = records[neighbor]
            delta = _edge_displacement(here,there,k)
            desired = (here['origin'][0]+delta[0],here['origin'][1]+delta[1])
            actual = (there['origin'][0]+m*u[0]+n*v[0],there['origin'][1]+m*u[1]+n*v[1])
            require(actual == desired, 'periodic edge holonomy or period-vector inconsistency')
            seam_checks += 1
    require(sum(area2(item['polygon']) for item in records.values()) == 2*abs(det), 'period area differs from polygon area')
    faces = sorted(records)
    bounds = {}
    for face in faces:
        poly = records[face]['polygon']
        xx = [Fraction(cross(p,v),det) for p in poly]
        yy = [Fraction(cross(u,p),det) for p in poly]
        bounds[face] = min(xx),max(xx),min(yy),max(yy)
    checks = 0
    for i,face in enumerate(faces):
        ai,ax,aj,ay = bounds[face]
        poly = records[face]['polygon']
        for other in faces[i:]:
            bi,bx,bj,by = bounds[other]
            for m in range(ceil(ai-bx),floor(ax-bi)+1):
                for n in range(ceil(aj-by),floor(ay-bj)+1):
                    if face == other and m == n == 0:
                        continue
                    translated = shift(records[other]['polygon'],(m*u[0]+n*v[0],m*u[1]+n*v[1]))
                    require(not interiors_overlap(poly,translated), 'translated periodic polygons overlap')
                    native_other = (other[0]+m*a+n*b,other[1]+n*c)
                    require(face_distance(face,native_other) == 1 or not polygons_touch(poly,translated),
                            'nonnative contact in periodic development')
                    checks += 1
    # Closed periodic union, equal domain area, disjoint interiors: full coverage.
    return {'valid':True,'kind':'boundary_periodic','placements':len(records),
            'area2':2*abs(det),'seam_checks':seam_checks,'translated_contact_checks':checks}


def independent_library(max_length):
    """Six independent bounded loops, intentionally separate from generator."""
    require(type(max_length) is int and 1 <= max_length <= 6, 'verifier library cap is M6')
    found = set()
    for word in product(range(1,max_length+1),repeat=6):
        x = 2*word[0]+word[1]-word[2]-2*word[3]-word[4]+word[5]
        y = word[1]+word[2]-word[4]-word[5]
        if x == y == 0:
            found.add(canonical_word(word))
    return found


def _bound_witness(summary,identifiers,catalogue):
    witness = summary['witness']
    require(digest(witness) == summary['witness_sha256'], 'boundary witness hash mismatch')
    protos = witness['prototiles']
    require(len(protos) == len(identifiers) and {p['id'] for p in protos} == set(identifiers),
            'witness prototile IDs differ from screened species')
    for proto in protos:
        tile = catalogue[proto['id']]
        require(tuple(proto['word']) == tuple(tile['word']) and points(proto['polygon']) == points(tile['polygon']),
                'witness prototile differs from library definition')
    return verify_certificate(witness)


def verify_batch(data,*,check_sources=True):
    """Verify full library/pair coverage and all retained positive certificates.

    UNSAT/UNKNOWN and SAT summaries without retained coordinates remain solver
    reports. This checker neither calls nor trusts the CSP solver for positives.
    """
    require(data['schema'] == 'arisearch.discovery.boundary.v1', 'unknown boundary batch schema')
    require(digest({k:v for k,v in data.items() if k not in ('result_sha256','execution')}) == data['result_sha256'],
            'boundary result hash mismatch')
    require(digest(data['catalogue']) == data['catalogue_sha256'], 'boundary catalogue hash mismatch')
    provenance = data['provenance']
    if check_sources:
        expected_files = {'boundary_words.py','boundary_screen.py','boundary_render.py'}
        require(set(provenance['source_sha256']) == expected_files, 'incomplete boundary source hashes')
        for name,expected in provenance['source_sha256'].items():
            require(hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() == expected,
                    f'boundary source hash mismatch: {name}')
    expected_words = independent_library(provenance['max_length'])
    catalogue,actual_words = {},set()
    for tile in data['catalogue']:
        word = tuple(tile['word'])
        require(canonical_word(word) == word, 'noncanonical library word')
        require(word not in actual_words and tile['id'] not in catalogue, 'duplicate library shape or ID')
        require(tile['id'] == 'bw120-'+'-'.join(map(str,word)), 'library ID disagrees with word')
        poly = word_polygon(word)
        require(points(tile['polygon']) == poly, 'library polygon disagrees with word')
        require(tile['centrally_symmetric'] is (word[:3] == word[3:]), 'incorrect central symmetry flag')
        require(tile['closure_parameter'] == word[0]-word[3], 'closure metadata mismatch')
        require(tile['side_count'] == 6 and tile['angles_degrees'] == [120]*6, 'angle metadata mismatch')
        require(tile['edge_squared_lengths'] == [4*x*x for x in word], 'edge metric metadata mismatch')
        require(tile['double_area_coefficient_sqrt3'] == area2(poly), 'area metadata mismatch')
        require(tile['corner_length_pairs'] == [[word[i-1],word[i]] for i in range(6)], 'corner metadata mismatch')
        require(tile['angle_cos_data'] == [{'dot':-2*word[i-1]*word[i], 'norm_product_squared':16*word[i-1]**2*word[i]**2} for i in range(6)], 'angle metric metadata mismatch')
        orbit = sorted({seq[k:]+seq[:k] for seq in (word,word[::-1]) for k in range(6)})
        require([tuple(w) for w in tile['orientation_words']] == orbit, 'reflection/rotation state catalogue mismatch')
        actual_words.add(word)
        catalogue[tile['id']] = tile
    require(actual_words == expected_words, 'full bounded library coverage mismatch')
    metadata = data['metadata']
    central_count = sum(t['centrally_symmetric'] for t in catalogue.values())
    require((metadata['tile_count'],metadata['central_count'],metadata['noncentral_count']) ==
            (len(catalogue),central_count,len(catalogue)-central_count), 'library count metadata mismatch')
    histogram = Counter(len(set(w)) for w in actual_words)
    require({int(k):v for k,v in metadata['distinct_length_count_histogram'].items()} == dict(histogram), 'length histogram mismatch')
    similarity = {canonical_word(tuple(x//reduce(gcd,w) for x in w)) for w in actual_words}
    require(metadata['integer_similarity_family_count'] == len(similarity) and metadata['common_physical_length_scale'] == 2,
            'similarity/scale metadata mismatch')
    conventions = data['conventions']
    require(tuple(map(tuple,conventions['face_steps'])) == STEPS
            and tuple(map(tuple,conventions['edge_vectors_per_native_length'])) == DIRECTIONS, 'native coordinate conventions mismatch')
    central = {identifier for identifier,t in catalogue.items() if t['centrally_symmetric']}
    noncentral = set(catalogue)-central
    omissions = data['central_omissions']
    require(len(omissions) == len(central) and {r['tile'] for r in omissions} == central
            and all(r['status'] == 'MONOHEDRAL_THEOREM' for r in omissions), 'central omission coverage mismatch')
    budgets = data['budgets']
    require(budgets['workers'] == 1 and budgets['periodic_requires_both_species'] is False, 'unsupported species/worker policy')
    require(type(budgets['max_index']) is int and budgets['max_index'] > 0, 'invalid HNF bound')
    require(all(type(budgets[k]) is int and budgets[k] > 0 for k in ('node_budget','propagation_budget')), 'invalid deterministic budget')
    radii = budgets['radii']
    require(radii and len(set(radii)) == len(radii) and all(type(r) is int and r > 0 for r in radii), 'invalid disk radii')
    domains = [(a,b,index//a) for index in range(1,budgets['max_index']+1)
               for a in range(1,index+1) if index%a == 0 for b in range(a)]
    checked = Counter()
    def finite_summary(record):
        require(record['status'] in ('SAT','UNSAT','UNKNOWN'), 'invalid finite solver status')
        for field,budget in (('nodes','node_budget'),('propagations','propagation_budget')):
            require(type(record[field]) is int and 0 <= record[field] <= budgets[budget], 'solver counter exceeds deterministic budget')
        if record['status'] == 'UNKNOWN':
            require(record.get('budget_reason') in ('node_budget','propagation_budget','outer_cpu_budget'), 'unexplained UNKNOWN')
    def periodic(summary,identifiers):
        attempts = summary['attempts']
        require(0 < len(attempts) <= len(domains), 'invalid periodic attempt count')
        require([tuple(a['domain_hnf']) for a in attempts] == domains[:len(attempts)], 'periodic attempts differ from HNF prefix')
        for attempt in attempts:
            finite_summary(attempt)
        if summary['status'] == 'PERIODIC_WITNESS':
            require(attempts[-1]['status'] == 'SAT' and all(a['status'] != 'SAT' for a in attempts[:-1]), 'periodic positive status mismatch')
            require(tuple(summary['witness']['domain_hnf']) == domains[len(attempts)-1], 'witness uses a different tested HNF')
            require(summary['witness']['kind'] == 'boundary_periodic', 'wrong periodic witness kind')
            _bound_witness(summary,identifiers,catalogue)
            checked['periodic'] += 1
        else:
            outer_stop = summary.get('budget_reason') == 'outer_cpu_budget'
            require((len(attempts) == len(domains) or outer_stop) and all(a['status'] != 'SAT' for a in attempts), 'negative periodic summary stopped early')
            if outer_stop:
                require(attempts[-1].get('budget_reason') == 'outer_cpu_budget', 'unexplained truncated period search')
            expected = 'UNKNOWN' if any(a['status'] == 'UNKNOWN' for a in attempts) else 'NO_PERIODIC_WITNESS_IN_TESTED_DOMAINS'
            require(summary['status'] == expected and 'witness' not in summary, 'periodic nonpositive summary mismatch')
    mono,seen_singletons = set(),set()
    for row in data['singletons']:
        identifier = row['tile']
        require(identifier in noncentral and identifier not in seen_singletons, 'duplicate/invalid singleton reference')
        seen_singletons.add(identifier)
        if row['status'] == 'NOT_RUN_OUTER_BUDGET':
            continue
        periodic(row,[identifier])
        if row['status'] == 'PERIODIC_WITNESS':
            mono.add(identifier)
    require(seen_singletons == noncentral, 'singleton coverage mismatch')
    selection = data.get('selection',{'pair_filter':None,'expected_pair_count':len(noncentral)*(len(noncentral)-1)//2})
    pair_filter = selection['pair_filter']
    if pair_filter is None:
        expected_pairs = {frozenset(pair) for pair in combinations(noncentral,2)}
    else:
        require(len(pair_filter) == len(set(pair_filter)) == 2 and set(pair_filter) <= noncentral, 'invalid focused pair selection')
        expected_pairs = {frozenset(pair_filter)}
    require(selection['expected_pair_count'] == len(expected_pairs), 'declared pair selection count mismatch')
    seen_pairs = set()
    statuses = Counter()
    for row in data['pairs']:
        identifiers = row['tiles']
        pair = frozenset(identifiers)
        require(len(identifiers) == len(pair) == 2 and pair in expected_pairs and pair not in seen_pairs, 'duplicate/invalid pair reference')
        seen_pairs.add(pair)
        status = row['status']
        statuses[status] += 1
        if status == 'OMITTED_MONOHEDRAL_MEMBER':
            require(set(row['positive_members']) == pair & mono and pair & mono, 'unsupported singleton omission')
            continue
        require(not pair & mono, 'positive singleton pair was unnecessarily screened')
        if status == 'NOT_RUN_OUTER_BUDGET':
            continue
        require(status in ('LOCAL_OBSTRUCTION','FINITE_EXTENSION_FAILURE','PERIODIC_WITNESS','UNKNOWN','SURVIVES_BOUNDED_SCREENS'), 'unknown pair status')
        local,growth = row['local'],row['growth']
        require(0 < len(local) <= 2 and [r['seed_tile'] for r in local] == identifiers[:len(local)], 'local seed coverage mismatch')
        for record in local+growth:
            if 'nodes' in record and 'propagations' in record:
                finite_summary(record)
            else:
                require(record in growth and any(all(record[k] == r[k] for k in ('seed_tile','symbolic_radius','status')) for r in local),
                        'counterless growth record has no corresponding local summary')
            require(record['seed_tile'] in pair and record['symbolic_radius'] in radii, 'disk summary has wrong seed/radius')
            if record in local:
                require(record['symbolic_radius'] == min(radii), 'local summary uses wrong radius')
            if 'witness' in record:
                require(record['status'] == 'SAT' and record['witness']['kind'] == 'boundary_patch', 'invalid disk positive status')
                witness = record['witness']
                require(witness['seed_tile'] == record['seed_tile'] and witness['symbolic_radius'] == record['symbolic_radius'], 'disk witness summary mismatch')
                _bound_witness(record,identifiers,catalogue)
                checked['patch'] += 1
        # Retain one strongest SAT disk for each attempted seed, even when
        # later growth is impossible; old SAT summaries may omit coordinates.
        if status != 'PERIODIC_WITNESS':
            last_sat = {r['seed_tile']:i for i,r in enumerate(growth) if r['status'] == 'SAT'}
            require(all(('witness' in r) == (r['status'] == 'SAT' and last_sat[r['seed_tile']] == i)
                        for i,r in enumerate(growth)), 'strongest SAT disk witness missing or duplicated')
        outer_stop = row.get('budget_reason') == 'outer_cpu_budget'
        if outer_stop:
            require(status == 'UNKNOWN', 'outer budget stop must remain UNKNOWN')
            if 'attempts' in row.get('periodic',{}):
                periodic(row['periodic'],identifiers)
            continue
        initial = [(r['seed_tile'],min(radii)) for r in local if r['status'] == 'SAT']
        schedule = initial+[(seed,radius) for radius in sorted(set(radii)-{min(radii)}) for seed in identifiers]
        actual = [(r['seed_tile'],r['symbolic_radius']) for r in growth]
        if status == 'LOCAL_OBSTRUCTION':
            require(actual == initial, 'local obstruction retained unexpected growth stages')
            require(any(r['status'] == 'UNSAT' for r in local) and row.get('periodic',{}).get('status','DEFERRED_LOCAL_OBSTRUCTION') == 'DEFERRED_LOCAL_OBSTRUCTION', 'local obstruction summary mismatch')
            continue
        require(len(local) == 2 and all(r['status'] != 'UNSAT' for r in local), 'periodic stage lacks local seed screens')
        periodic(row['periodic'],identifiers)
        if status == 'PERIODIC_WITNESS':
            require(row['periodic']['status'] == status and growth == [], 'pair periodic funnel mismatch')
        elif status == 'FINITE_EXTENSION_FAILURE':
            require(actual == schedule[:len(actual)] and len(actual) > len(initial) and all(r['status'] != 'UNSAT' for r in growth[:-1]), 'finite growth schedule mismatch')
            require(row['periodic']['status'] != 'PERIODIC_WITNESS' and growth[-1]['status'] == 'UNSAT', 'finite-extension summary mismatch')
        else:
            require(actual == schedule, 'survivor omitted an asserted growth radius or seed')
            require(row['periodic']['status'] != 'PERIODIC_WITNESS' and all(r['status'] != 'UNSAT' for r in local+growth), 'survivor funnel mismatch')
            expected = 'UNKNOWN' if row['periodic']['status'] == 'UNKNOWN' or any(r['status'] == 'UNKNOWN' for r in local+growth) else 'SURVIVES_BOUNDED_SCREENS'
            require(status == expected, 'survivor status mismatch')
    require(seen_pairs == expected_pairs, 'full unordered pair coverage mismatch')
    def budget_stopped(value):
        if isinstance(value,dict):
            return value.get('budget_reason') == 'outer_cpu_budget' or value.get('status') == 'NOT_RUN_OUTER_BUDGET' or any(budget_stopped(v) for v in value.values())
        if isinstance(value,(list,tuple)):
            return any(budget_stopped(v) for v in value)
        return False
    require(data['batch_complete'] is (not budget_stopped([data['singletons'],data['pairs']])), 'batch completion flag mismatch')
    expected_funnel = {'library':len(catalogue),'central_theorem_omissions':len(central),
                       'noncentral_singletons':len(noncentral),'positive_singleton_periodic':len(mono),
                       'unordered_pairs':len(expected_pairs),'pair_status_counts':dict(sorted((k,v) for k,v in statuses.items() if v))}
    require(data['funnel'] == expected_funnel, 'boundary funnel mismatch')
    return {'valid':True,'kind':'boundary_batch','library':len(catalogue),'central':len(central),
            'noncentral':len(noncentral),'pairs':len(expected_pairs),'verified_witnesses':dict(checked),
            'funnel':expected_funnel,'scope':'all retained positive geometry verified; negative solver labels require fresh replay; finite library only'}


def verify_certificate(cert):
    if cert.get('schema') == 'arisearch.discovery.boundary.v1':
        return verify_batch(cert)
    if cert['kind'] == 'boundary_periodic':
        return verify_periodic(cert)
    require(cert['kind'] == 'boundary_patch', 'unknown boundary certificate kind')
    return verify_patch(cert)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    args = parser.parse_args()
    cert = json.loads(args.certificate.read_text())
    result = [verify_certificate(c) for c in cert] if isinstance(cert,list) else verify_certificate(cert)
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
