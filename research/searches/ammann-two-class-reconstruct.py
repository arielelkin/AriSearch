#!/usr/bin/env sage -python
"""Exact reconstruction of Ammann's convex recomposition of Penrose rhombs.

Replay:
  conda run --no-capture-output -n arisearch sage -python \
      research/searches/ammann-two-class-reconstruct.py [n_deflations]

All geometry is exact in K = Q(w), w = exp(i*pi/5) (CyclotomicField(10)).
Floats are used ONLY to order neighbours around a vertex when tracing faces
of the planar graph; every traced face is then re-checked exactly (strict
convexity, positive orientation) and the total face area is checked exactly
against the area enclosed, so a wrong float ordering could not pass silently.

Model.  A Penrose rhomb patch is produced by Robinson-triangle deflation
(Preshing-style labels: triangle (colour, A, B, C), A the apex, BC the base,
a rhomb = two mirror triangles sharing their base).  Each rhomb is decorated
by an orientation-preserving similarity of the reference decoration

  thin  : A=0, B=1, D=w, C=1+w, J = s + t*w ; segments JB, JC, JD
  thick : E=0, F=1, H=w^2, G=1+w^2,
          K = H + w^6 (J - B)  (rotation of triangle JBC onto HEK)
          L = F + w^7 (J - C)  (rotation of triangle JCD onto FGL)
          segments EK, HK, FL, GL, KL

(these K, L satisfy EK=CJ, HK=BJ, FL=CJ, GL=DJ and are the unique circle
intersections inside the thick rhomb; the other intersections are their
mirror images in EH resp. FG, outside the rhomb).

The reference vertex B (thin) / E (thick) may be put on the rhomb's
"B-label" or "C-label" vertex of the Robinson labelling: 4 placement
options.  Rhomb edges are erased, faces of the remaining graph are traced,
interior faces are classified up to direct and mirror congruence exactly.
"""
import sys, json, itertools
from sage.all import CyclotomicField, QQ, AA, CC, ComplexField, arg

K = CyclotomicField(10)
w = K.gen()
phi = w + w**-1            # golden ratio (2 cos 36)
iphi = phi - 1             # 1/phi

def conj(z):
    return z.conjugate()

from sage.all import QQbar
_emb = K.hom([QQbar.zeta(10)])
def QQbar_of(z):
    return _emb(z)
def QQbar_I():
    return QQbar.gen() if False else QQbar(-1).sqrt()

_IW = w - w.conjugate()       # 2i*Im(w), Im(w) = sin 36 > 0

def real_K(x):
    """Im-normalised real element of K -> AA (single conversion, exact)."""
    return AA(QQbar_of(x))

def turn(a, b):
    """exact sign-faithful value Im(conj(a) b)/Im(w) as an AA number"""
    z = conj(a) * b
    return real_K((z - conj(z)) / _IW)

def area2(poly):
    """twice the signed area divided by Im(w) (same sign as the area)"""
    s = K(0)
    n = len(poly)
    for i in range(n):
        s += conj(poly[i]) * poly[(i + 1) % n]
    return (s - conj(s)) / _IW    # real element of K

def area_sign(poly):
    x = real_K(area2(poly))
    return (x > 0) - (x < 0)

# ---------------------------------------------------------------- patch
def sun():
    tris = []
    for i in range(10):
        B, C = w**i, w**(i + 1)
        if i % 2 == 0:
            B, C = C, B
        tris.append((0, K(0), B, C))
    return tris

def subdivide(tris):
    out = []
    for col, A, B, C in tris:
        if col == 0:
            P = A + (B - A) * iphi
            out += [(0, C, P, B), (1, P, C, A)]
        else:
            Q = B + (A - B) * iphi
            R = B + (C - B) * iphi
            out += [(1, R, C, A), (1, Q, R, B), (0, R, Q, A)]
    return out

def rhombs(tris):
    by = {}
    for t in tris:
        by.setdefault(frozenset([t[2], t[3]]), []).append(t)
    out = []
    for key, ts in by.items():
        if len(ts) != 2:
            continue
        t1, t2 = ts
        assert t1[0] == t2[0]
        assert t1[2] == t2[2] and t1[3] == t2[3], "mirror partner labels differ"
        col, A, B, C = t1
        A2 = t2[1]
        cyc = [A, B, A2, C]
        if area_sign(cyc) < 0:
            cyc = [A, C, A2, B]
        out.append((col, cyc, B, C))
    return out

def place(rh, opt_thin, opt_thick, s, t):
    """Return (kind, rhomb ccw vertices, decoration points, segments)."""
    col, cyc, Bl, Cl = rh
    J = s + t * w
    if col == 0:   # thin (36 deg apex A of red triangle = acute vertex)
        anchor = Bl if opt_thin == 'B' else Cl          # reference vertex B
        k = cyc.index(anchor)
        A4, B4, C4, D4 = cyc[k - 1], cyc[k], cyc[(k + 1) % 4], cyc[(k + 2) % 4]
        u = B4 - A4
        assert D4 == A4 + u * w and C4 == A4 + u * (1 + w)
        Jp = A4 + u * J
        return ('thin', [A4, B4, C4, D4], [Jp], [(Jp, B4), (Jp, C4), (Jp, D4)])
    else:          # thick: acute vertices are the B/C labels of the blue triangle
        anchor = Bl if opt_thick == 'B' else Cl          # reference vertex E
        k = cyc.index(anchor)
        E4, F4, G4, H4 = cyc[k], cyc[(k + 1) % 4], cyc[(k + 2) % 4], cyc[(k + 3) % 4]
        u = F4 - E4
        assert H4 == E4 + u * w**2 and G4 == E4 + u * (1 + w**2)
        Kr = w**2 + w**6 * (J - 1)
        Lr = 1 + w**7 * (J - 1 - w)
        Kp, Lp = E4 + u * Kr, E4 + u * Lr
        return ('thick', [E4, F4, G4, H4], [Kp, Lp],
                [(Kp, E4), (Kp, H4), (Lp, F4), (Lp, G4), (Kp, Lp)])

def faces_of(segs, bnd_edges):
    adj = {}
    def add(a, b, tag):
        adj.setdefault(a, {})[b] = tag
        adj.setdefault(b, {})[a] = tag
    for a, b in segs:
        add(a, b, 'dec')
    for a, b in bnd_edges:
        add(a, b, 'bnd')
    fl = {}
    rot = {}
    for v, nb in adj.items():
        cv = CC(v)
        rot[v] = sorted(nb.keys(), key=lambda x: float(arg(CC(x) - cv)))
    seen = set()
    faces = []
    for v in adj:
        for x in adj[v]:
            if (v, x) in seen:
                continue
            f = []
            a, b = v, x
            while (a, b) not in seen:
                seen.add((a, b))
                f.append((a, b))
                r = rot[b]
                i = r.index(a)
                c = r[(i - 1) % len(r)]
                a, b = b, c
            faces.append(f)
    return faces, adj

def strict_convex_ccw(poly):
    n = len(poly)
    for i in range(n):
        if turn(poly[i] - poly[i - 1], poly[(i + 1) % n] - poly[i]) <= 0:
            return False
    return True

def edges(poly):
    n = len(poly)
    return [poly[(i + 1) % n] - poly[i] for i in range(n)]

def direct_congruent(P, Q):
    if len(P) != len(Q):
        return False
    e, f = edges(P), edges(Q)
    n = len(e)
    for k in range(n):
        u = f[k] / e[0]
        if u * conj(u) != 1:
            continue
        if all(f[(k + i) % n] == u * e[i] for i in range(n)):
            return True
    return False

def mirror(P):
    return [conj(z) for z in reversed(P)]

def classify(polys):
    reps = []   # (rep, count, mirrored_count)
    for P in polys:
        for r in reps:
            if direct_congruent(r[0], P):
                r[1] += 1; break
            if direct_congruent(r[0], mirror(P)):
                r[2] += 1; break
        else:
            reps.append([P, 1, 0])
    return reps

def reference_tiles(s, t):
    J = s + t * w
    A, B, D, C = K(0), K(1), w, 1 + w
    E, F, H, G = K(0), K(1), w**2, 1 + w**2
    Jp = B + w**4 * (J - B)
    Jpp = D + w**6 * (J - D)
    Kr = H + w**6 * (J - B)
    Lr = F + w**7 * (J - C)
    J2 = G + D - J
    return {'H6': [A, Jp, B, J, D, Jpp],
            'P1': [E, Jp, F, Lr, Kr],
            'P2': [Kr, Lr, G, J2, H]}

def run(ndefl, samples, options=None):
    tris = sun()
    for _ in range(ndefl):
        tris = subdivide(tris)
    rh = rhombs(tris)
    nthin = sum(1 for r in rh if r[0] == 0); nthick = len(rh) - nthin
    # boundary rhomb edges
    ecount = {}
    for r in rh:
        c = r[1]
        for i in range(4):
            e = frozenset([c[i], c[(i + 1) % 4]])
            ecount[e] = ecount.get(e, 0) + 1
    bnd = [tuple(e) for e, m in ecount.items() if m == 1]
    report = {'deflations': ndefl, 'thin': nthin, 'thick': nthick, 'options': []}
    for (s, t) in samples:
        ref = reference_tiles(s, t)
        for ot, ok in (options or list(itertools.product('BC', 'BC'))):
            segs = []
            for r in rh:
                segs += place(r, ot, ok, s, t)[3]
            faces, adj = faces_of(segs, bnd)
            # exact area bookkeeping: bounded faces must exactly tile the rhomb union
            tot = sum(area2(r[1]) for r in rh)
            pos = [(area2([a for a, b in f]), area_sign([a for a, b in f])) for f in faces]
            assert sum(x for x, sg in pos if sg > 0) == tot, 'face area mismatch'
            assert sum(1 for x, sg in pos if sg < 0) == 1, 'expected one outer face'
            interior = []
            for f in faces:
                if any(adj[a][b] == 'bnd' for a, b in f):
                    continue
                poly = [a for a, b in f]
                if area_sign(poly) <= 0:
                    continue   # outer face
                interior.append(poly)
            allconvex = all(strict_convex_ccw(p) for p in interior)
            reps = classify(interior)
            sizes = sorted(len(r[0]) for r in reps)
            # scale-free matching: rescale reference by patch edge length phi^-n
            sc = iphi**ndefl
            match = {}
            for r in reps:
                for name, R in ref.items():
                    Rs = [z * sc for z in R]
                    if direct_congruent(Rs, r[0]):
                        match[name] = ('direct', r[1], r[2])
                    elif direct_congruent(mirror(Rs), r[0]):
                        match[name] = ('mirror', r[1], r[2])
            rec = {'s': str(s), 't': str(t), 'thin_anchor': ot, 'thick_anchor': ok,
                   'interior_faces': len(interior), 'all_strictly_convex': bool(allconvex),
                   'classes': len(reps),
                   'class_sizes_vertices': sizes,
                   'class_counts_direct_mirror': [(len(r[0]), r[1], r[2]) for r in reps],
                   'matches_reference': {k: list(v) for k, v in match.items()}}
            print(rec, flush=True)
            report['options'].append(rec)
    return report

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else None
    samples = [(QQ(1) / 2, QQ(4) / 5), (QQ(9) / 20, QQ(3) / 4), (QQ(11) / 20, QQ(17) / 20)]
    # all four anchor options on a 4-fold deflated sun, then the selected option on 6-fold
    rep4 = run(4, samples)
    rep6 = run(6, samples, options=[('B', 'B')])
    sel = [o for o in rep4['options'] if o['classes'] == 3]
    assert all(o['thin_anchor'] == 'B' and o['thick_anchor'] == 'B' for o in sel) and len(sel) == len(samples)
    assert all(o['classes'] == 3 and o['all_strictly_convex'] and
               sorted(o['matches_reference']) == ['H6', 'P1', 'P2'] and
               all(v[0] == 'direct' and v[2] == 0 for v in o['matches_reference'].values())
               for o in rep6['options'])
    print('RECONSTRUCTION CHECK PASSED')
    if out:
        json.dump({'n4_all_options': rep4, 'n6_selected': rep6}, open(out, 'w'), indent=1)
