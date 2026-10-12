#!/usr/bin/env python3
"""Exact vertex-sector obstruction + larger-patch recheck for surviving pairs.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-two-class-sector.py TYPES.json PAIRS6.json PATCH7.json OUT.json

Vertex-sector test (parameter independent, exact in units of 36 degrees):
at an interior patch vertex v, list the rhomb corners around v in angular
order with the number of decoration segments each rhomb's decoration sends
into that corner.  Consecutive segments at v bound a sector of one tile;
the sector contains every segment-free corner between them entirely, plus
two strictly positive partial angles.  If some sector has segment-free
corners summing to >= 180 degrees while v carries at least one segment,
that tile has an interior angle > 180 at v for EVERY parameter choice, so
the pair is dead.
"""
import sys, json, importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('pa', os.path.join(here, 'ammann-two-class-pairs.py'))
pa = importlib.util.module_from_spec(spec); spec.loader.exec_module(pa)

UNITS = {'thin': [1, 4, 1, 4], 'thick': [2, 3, 2, 3]}   # corner angles / 36 deg

def seg_count(t):
    c = [0, 0, 0, 0]
    for a, b in t['edges']:
        for x in (a, b):
            if x in '0123':
                c[int(x)] += 1
    return c

def direction(vec):
    for k in range(10):
        if pa.mulwk((1, 0, 0, 0), k) == vec:
            return k
    raise ValueError(vec)

def sector_test(tthin, tthick, verts, rh):
    segs = {'thin': seg_count(tthin), 'thick': seg_count(tthick)}
    corners = {}
    for ri, (kind, gv, a) in enumerate(rh):
        for i in range(4):
            d = direction(pa.sub(verts[gv[(i + 1) % 4]], verts[gv[i]]))
            corners.setdefault(gv[i], []).append((d, UNITS[kind][i], segs[kind][i]))
    worst = None
    for v, cs in corners.items():
        if sum(u for d, u, s in cs) != 10:
            continue                       # boundary vertex of the patch
        cs.sort()
        # check contiguity
        for j in range(len(cs)):
            assert (cs[j][0] + cs[j][1]) % 10 == cs[(j + 1) % len(cs)][0] % 10
        total = sum(s for d, u, s in cs)
        if total == 0:
            continue
        # rotate to start right after a corner carrying segments
        j0 = [j for j in range(len(cs)) if cs[j][2] > 0][0]
        seq = cs[j0 + 1:] + cs[:j0 + 1]
        run = 0
        for d, u, s in seq:
            if s == 0:
                run += u
            else:
                if run >= 5:
                    return {'dead': True, 'vertex': v, 'free_full_corner_units': run}
                run = 0
        if total == 1:
            return {'dead': True, 'vertex': v, 'reason': 'single segment at vertex (slit)'}
    return {'dead': False}

def main(types_path, pairs_path, patch7_path, out_path):
    T = json.load(open(types_path))
    alive = json.load(open(pairs_path))['alive']
    T7, verts, rh, eo = pa.load(types_path, patch7_path)
    out = []
    for r in alive:
        i, j = r['thin'], r['thick']
        st = sector_test(T[i], T[j], verts, rh)
        r7 = pa.analyze(T[i], T[j], verts, rh, eo)
        same = None
        if r7['dead'] is None:
            same = sorted((c['corners']) for c in r7['classes']) == sorted(c['corners'] for c in r['classes']) \
                and r7['nclasses'] == r['nclasses']
        rec = {'thin': i, 'thick': j, 'thin_edges': T[i]['edges'], 'thick_edges': T[j]['edges'],
               'n6_classes': r['nclasses'], 'sector_test': st,
               'n7_dead': r7['dead'], 'n7_classes': r7.get('nclasses'),
               'n7_tiles': r7.get('tiles'), 'class_list_stable_n6_n7': same,
               'n7_class_corners_counts': [(c['corners'], c['count']) for c in r7.get('classes', [])]}
        print(rec, flush=True)
        out.append(rec)
    json.dump(out, open(out_path, 'w'), indent=1)

if __name__ == '__main__':
    main(*sys.argv[1:5])
