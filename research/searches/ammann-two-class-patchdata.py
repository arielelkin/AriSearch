#!/usr/bin/env python3
"""Export an exact Penrose rhomb patch in Ammann frames as integer data.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-two-class-patchdata.py N OUT.json

Uses the Robinson deflation and the (thin 'B', thick 'B') frame selection of
ammann-two-class-reconstruct.py (the unique option reproducing Ammann's three
tiles).  The patch is rescaled to unit rhomb side, so every vertex lies in
Z[w] and is stored as an integer 4-vector in the basis 1, w, w^2, w^3.
Each rhomb is stored as (kind, [4 global vertex ids in frame order], a) with
frame map z -> v0 + w^a z  (thin frame A,B,C,D; thick frame E,F,G,H).
"""
import sys, json, importlib.util, os
from sage.all import ZZ

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rec', os.path.join(here, 'ammann-two-class-reconstruct.py'))
rec = importlib.util.module_from_spec(spec); spec.loader.exec_module(rec)
K, w = rec.K, rec.w

def main(n, out):
    tris = rec.sun()
    for _ in range(n):
        tris = rec.subdivide(tris)
    rh = rec.rhombs(tris)
    scale = rec.phi**n
    vid = {}; verts = []
    def gid(p):
        q = p * scale
        if q not in vid:
            vid[q] = len(verts)
            v = [ZZ(c) for c in q.vector()]   # must be integral
            verts.append([int(c) for c in v])
        return vid[q]
    out_rh = []
    for r in rh:
        kind, cyc, decpts, segs = rec.place(r, 'B', 'B', 0, 0)
        u = (cyc[1] - cyc[0]) * scale
        a = [k for k in range(10) if w**k == u]
        assert len(a) == 1
        out_rh.append(['thin' if kind == 'thin' else 'thick', [gid(p) for p in cyc], a[0]])
    json.dump({'deflations': n, 'basis': '1,w,w^2,w^3; w^4 = w^3 - w^2 + w - 1',
               'verts': verts, 'rhombs': out_rh}, open(out, 'w'))
    print('rhombs', len(out_rh), 'verts', len(verts))

if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
