#!/usr/bin/env python3
"""Cross-check of the vertex-star conventions of ammann-forcing-angles.py
against genuine Ammann tilings (decorated Robinson-deflation Penrose patches).

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-forcing-patchcheck.py \
      research/certificates/ammann-forcing-angles.json 6 \
      research/certificates/ammann-forcing-patchcheck.json

Faces of the decorated patch are produced by ammann-two-class-reconstruct.py
(exact in Q(w)); each interior face is identified exactly with H6/P1/P2
(direct or mirror, with its vertex labelling); at every vertex whose incident
interior faces fill 360 degrees the cyclic star (corner names + orientation)
is formed and compared with the viable star list in the certificate.
Expected: every observed star is viable; observed stars cover the viable list.
"""
import sys, json, importlib.util, os
from sage.all import QQ, CC, arg

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rec', os.path.join(HERE, 'ammann-two-class-reconstruct.py'))
rec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rec)
K, w = rec.K, rec.w

VNAMES = {'H6': ['A', "J'", 'B', 'J', 'D', "J''"],
          'P1': ['E', "J'", 'F', 'L', 'K'],
          'P2': ['K', 'L', 'G', 'J2', 'H']}

def identify(poly, ref):
    """return list of (name, ori, labels-per-vertex-of-poly)"""
    for name, R in ref.items():
        if len(R) != len(poly):
            continue
        e, f = rec.edges(R), rec.edges(poly)
        n = len(e)
        for k in range(n):
            u = f[k] / e[0]
            if u * u.conjugate() == 1 and all(f[(k + i) % n] == u * e[i] for i in range(n)):
                # poly[k+i] corresponds to R[i]
                lab = [None] * n
                for i in range(n):
                    lab[(k + i) % n] = VNAMES[name][i]
                return name, 'd', lab
        M = rec.mirror(R)    # M[i] = conj(R[n-1-i])
        e = rec.edges(M)
        for k in range(n):
            u = f[k] / e[0]
            if u * u.conjugate() == 1 and all(f[(k + i) % n] == u * e[i] for i in range(n)):
                lab = [None] * n
                for i in range(n):
                    lab[(k + i) % n] = VNAMES[name][n - 1 - i]
                return name, 'm', lab
    return None

def main():
    certp = sys.argv[1]
    nd = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    cert = json.load(open(certp))
    s, t = QQ(cert['J0']['s']), QQ(cert['J0']['t'])
    viable = set()
    def canon(seq):
        n = len(seq)
        refl = [(nm, 'm' if o == 'd' else 'd') for nm, o in reversed(seq)]
        return min(tuple(x[k:] + x[:k]) for x in (seq, refl) for k in range(n))
    for st in cert['viable_stars']:
        viable.add(canon([(c[0], c[1]) for c in st]))
    tris = rec.sun()
    for _ in range(nd):
        tris = rec.subdivide(tris)
    rh = rec.rhombs(tris)
    ecount = {}
    for r in rh:
        c = r[1]
        for i in range(4):
            e = frozenset([c[i], c[(i + 1) % 4]])
            ecount[e] = ecount.get(e, 0) + 1
    bnd = [tuple(e) for e, m in ecount.items() if m == 1]
    segs = []
    for r in rh:
        segs += rec.place(r, 'B', 'B', s, t)[3]
    faces, adj = rec.faces_of(segs, bnd)
    sc = rec.iphi ** nd
    ref = {k: [z * sc for z in v] for k, v in rec.reference_tiles(s, t).items()}
    corners_at = {}
    nfaces = 0
    for f in faces:
        if any(adj[a][b] == 'bnd' for a, b in f):
            continue
        poly = [a for a, b in f]
        if rec.area_sign(poly) <= 0:
            continue
        idn = identify(poly, ref)
        assert idn is not None, 'unidentified face'
        name, ori, lab = idn
        nfaces += 1
        n = len(poly)
        for i in range(n):
            v = poly[i]
            # direction of the cw ray of the corner in the plane: to poly[i+1] (face is ccw)
            d = CC(poly[(i + 1) % n] - v)
            corners_at.setdefault(v, []).append((float(arg(d)), name + '-' + lab[i], ori,
                                                 poly[(i + 1) % n], poly[i - 1]))
    observed = {}
    for v, cs in corners_at.items():
        # complete star: the cw ray of each corner is the ccw ray of exactly one other
        cw = {c[3]: c for c in cs}
        ccw = {c[4]: c for c in cs}
        if set(cw) != set(ccw) or len(cw) != len(cs):
            continue
        seq = [cs[0]]
        while True:
            nxt = cw.get(seq[-1][4])
            if nxt is None or nxt is seq[0]:
                break
            seq.append(nxt)
        if len(seq) != len(cs):
            continue
        key = canon([(c[1], c[2]) for c in seq])
        observed[key] = observed.get(key, 0) + 1
    bad = [k for k in observed if k not in viable]
    unseen = [k for k in viable if k not in observed]
    print('faces', nfaces, 'complete vertices', sum(observed.values()), 'distinct stars', len(observed))
    for k, m in sorted(observed.items(), key=lambda x: -x[1]):
        print(m, k)
    print('observed but not viable:', bad)
    print('viable but not observed:', unseen)
    assert not bad
    print('PATCH CHECK PASSED' + ('' if unseen else ' (all viable stars observed)'))
    if len(sys.argv) > 3:
        json.dump({'J0': [str(s), str(t)], 'deflations': nd, 'interior_faces': nfaces,
                   'complete_vertices': sum(observed.values()),
                   'observed_star_counts': [[list(map(list, k)), m] for k, m in observed.items()],
                   'observed_not_viable': bad, 'viable_not_observed': unseen},
                  open(sys.argv[3], 'w'), indent=1)

if __name__ == '__main__':
    main()
