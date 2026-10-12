#!/usr/bin/env python3
"""Exact hat-monotile patches (Smith-Myers-Kaplan-Goodman-Strauss 2023).

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/source-decoration-hat-patch.py LEVELS OUT.json

Independent re-implementation in exact arithmetic over Q(sqrt3) of the
H/T/P/F metatile substitution as published in Kaplan's reference viewer
(hatviz, hat.js/geometry.js; read as data, not executed).  Numbers are
a + b*sqrt3 with a, b rational (class Q3).  Output: list of hats, each as
(label, reflected?, 13 vertices) in exact coordinates.

Verification (exact): every hat is decomposed into 8 kites of the
deltoidal trihexagonal grid; no kite is covered twice; every grid kite
within the inscribed disc of the covered region is covered (gap-free core).
"""
import sys, json
from fractions import Fraction as Fr

class Q3:
    __slots__ = ('a', 'b')
    def __init__(self, a, b=0):
        self.a = Fr(a); self.b = Fr(b)
    def __add__(s, o):
        o = q3(o); return Q3(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o):
        o = q3(o); return Q3(s.a - o.a, s.b - o.b)
    def __rsub__(s, o):
        return q3(o) - s
    def __neg__(s):
        return Q3(-s.a, -s.b)
    def __mul__(s, o):
        o = q3(o); return Q3(s.a * o.a + 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = q3(o); n = o.a * o.a - 3 * o.b * o.b
        return s * Q3(o.a / n, -o.b / n)
    def sign(s):
        a, b = s.a, s.b
        if a >= 0 and b >= 0:
            return 0 if (a == 0 and b == 0) else 1
        if a <= 0 and b <= 0:
            return -1
        # opposite signs: compare a^2 vs 3 b^2
        d = a * a - 3 * b * b
        if a > 0:
            return 1 if d > 0 else (-1 if d < 0 else 0)
        return -1 if d > 0 else (1 if d < 0 else 0)
    def __eq__(s, o):
        o = q3(o); return s.a == o.a and s.b == o.b
    def __hash__(s):
        return hash((s.a, s.b))
    def __float__(s):
        return float(s.a) + float(s.b) * 3 ** 0.5
    def key(s):
        return (s.a, s.b)
    def __repr__(s):
        return '(%s+%s*r3)' % (s.a, s.b)

def q3(x):
    return x if isinstance(x, Q3) else Q3(x)

R3 = Q3(0, 1)
HR3 = Q3(0, Fr(1, 2))
ZERO, ONE, HALF = Q3(0), Q3(1), Q3(Fr(1, 2))

def pt(x, y):
    return (q3(x), q3(y))
def hexPt(x, y):
    return (q3(x) + Fr(1, 2) * q3(y), HR3 * y)
def inv(T):
    det = T[0] * T[4] - T[1] * T[3]
    return [T[4] / det, -T[1] / det, (T[1] * T[5] - T[2] * T[4]) / det,
            -T[3] / det, T[0] / det, (T[2] * T[3] - T[0] * T[5]) / det]
def mul(A, B):
    return [A[0] * B[0] + A[1] * B[3], A[0] * B[1] + A[1] * B[4], A[0] * B[2] + A[1] * B[5] + A[2],
            A[3] * B[0] + A[4] * B[3], A[3] * B[1] + A[4] * B[4], A[3] * B[2] + A[4] * B[5] + A[5]]
def padd(p, q): return (p[0] + q[0], p[1] + q[1])
def psub(p, q): return (p[0] - q[0], p[1] - q[1])
# exact cos/sin for multiples of 60 degrees used in the construction
def trot_k60(k):
    c = [ONE, HALF, -HALF, -ONE, -HALF, HALF][k % 6]
    s = [ZERO, HR3, HR3, ZERO, -HR3, -HR3][k % 6]
    return [c, -s, ZERO, s, c, ZERO]
def ttrans(x, y): return [ONE, ZERO, q3(x), ZERO, ONE, q3(y)]
def rotAbout(p, k60):
    return mul(ttrans(p[0], p[1]), mul(trot_k60(k60), ttrans(-p[0], -p[1])))
def transPt(M, P):
    return (M[0] * P[0] + M[1] * P[1] + M[2], M[3] * P[0] + M[4] * P[1] + M[5])
def matchSeg(p, q):
    return [q[0] - p[0], p[1] - q[1], p[0], q[1] - p[1], q[0] - p[0], p[1]]
def matchTwo(p1, q1, p2, q2):
    return mul(matchSeg(p2, q2), inv(matchSeg(p1, q1)))
def intersect(p1, q1, p2, q2):
    d = (q2[1] - p2[1]) * (q1[0] - p1[0]) - (q2[0] - p2[0]) * (q1[1] - p1[1])
    uA = ((q2[0] - p2[0]) * (p1[1] - p2[1]) - (q2[1] - p2[1]) * (p1[0] - p2[0])) / d
    return (p1[0] + uA * (q1[0] - p1[0]), p1[1] + uA * (q1[1] - p1[1]))
IDENT = [ONE, ZERO, ZERO, ZERO, ONE, ZERO]

hat_outline = [hexPt(0, 0), hexPt(-1, -1), hexPt(0, -2), hexPt(2, -2),
               hexPt(2, -1), hexPt(4, -2), hexPt(5, -1), hexPt(4, 0),
               hexPt(3, 0), hexPt(2, 2), hexPt(0, 3), hexPt(0, 2), hexPt(-1, 2)]

class Hat:
    def __init__(self, label):
        self.label = label
class Meta:
    def __init__(self, shape):
        self.shape = list(shape); self.children = []
    def add(self, T, g):
        self.children.append([T, g])
    def evalChild(self, n, i):
        T, g = self.children[n]
        return transPt(T, g.shape[i])
    def recentre(self):
        n = len(self.shape)
        cx = sum((p[0] for p in self.shape), ZERO) / n
        cy = sum((p[1] for p in self.shape), ZERO) / n
        self.shape = [(p[0] - cx, p[1] - cy) for p in self.shape]
        M = ttrans(-cx, -cy)
        for ch in self.children:
            ch[0] = mul(M, ch[0])

H1h, Hh, Th, Ph, Fh = Hat('H1'), Hat('H'), Hat('T'), Hat('P'), Hat('F')

def init():
    Ho = [pt(0, 0), pt(4, 0), (q3(Fr(9, 2)), HR3), (q3(Fr(5, 2)), 5 * HR3), (q3(Fr(3, 2)), 5 * HR3), (q3(Fr(-1, 2)), HR3)]
    H = Meta(Ho)
    H.add(matchTwo(hat_outline[5], hat_outline[7], Ho[5], Ho[0]), Hh)
    H.add(matchTwo(hat_outline[9], hat_outline[11], Ho[1], Ho[2]), Hh)
    H.add(matchTwo(hat_outline[5], hat_outline[7], Ho[3], Ho[4]), Hh)
    H.add(mul(ttrans(Fr(5, 2), HR3), mul([-HALF, -HR3, ZERO, HR3, -HALF, ZERO], [HALF, ZERO, ZERO, ZERO, -HALF, ZERO])), H1h)
    To = [pt(0, 0), pt(3, 0), (q3(Fr(3, 2)), 3 * HR3)]
    T = Meta(To)
    T.add([HALF, ZERO, HALF, ZERO, HALF, HR3], Th)
    Po = [pt(0, 0), pt(4, 0), (q3(3), 2 * HR3), (q3(-1), 2 * HR3)]
    P = Meta(Po)
    P.add([HALF, ZERO, q3(Fr(3, 2)), ZERO, HALF, HR3], Ph)
    P.add(mul(ttrans(0, 2 * HR3), mul([HALF, HR3, ZERO, -HR3, HALF, ZERO], [HALF, ZERO, ZERO, ZERO, HALF, ZERO])), Ph)
    Fo = [pt(0, 0), pt(3, 0), (q3(Fr(7, 2)), HR3), (q3(3), 2 * HR3), (q3(-1), 2 * HR3)]
    F = Meta(Fo)
    F.add([HALF, ZERO, q3(Fr(3, 2)), ZERO, HALF, HR3], Fh)
    F.add(mul(ttrans(0, 2 * HR3), mul([HALF, HR3, ZERO, -HR3, HALF, ZERO], [HALF, ZERO, ZERO, ZERO, HALF, ZERO])), Fh)
    return [H, T, P, F]

RULES = [['H'], [0, 0, 'P', 2], [1, 0, 'H', 2], [2, 0, 'P', 2], [3, 0, 'H', 2], [4, 4, 'P', 2],
         [0, 4, 'F', 3], [2, 4, 'F', 3], [4, 1, 3, 2, 'F', 0], [8, 3, 'H', 0], [9, 2, 'P', 0],
         [10, 2, 'H', 0], [11, 4, 'P', 2], [12, 0, 'H', 2], [13, 0, 'F', 3], [14, 2, 'F', 1],
         [15, 3, 'H', 4], [8, 2, 'F', 1], [17, 3, 'H', 0], [18, 2, 'P', 0], [19, 2, 'H', 2],
         [20, 4, 'F', 3], [20, 0, 'P', 2], [22, 0, 'H', 2], [23, 4, 'F', 3], [23, 0, 'F', 3],
         [16, 0, 'P', 2], [9, 4, 0, 2, 'T', 2], [4, 0, 'F', 3]]

def constructPatch(H, T, P, F):
    ret = Meta([]); shapes = {'H': H, 'T': T, 'P': P, 'F': F}
    for r in RULES:
        if len(r) == 1:
            ret.add(IDENT, shapes[r[0]])
        elif len(r) == 4:
            Tm, g = ret.children[r[0]]; poly = g.shape
            Pp = transPt(Tm, poly[(r[1] + 1) % len(poly)]); Qp = transPt(Tm, poly[r[1]])
            ns = shapes[r[2]]; npoly = ns.shape
            ret.add(matchTwo(npoly[r[3]], npoly[(r[3] + 1) % len(npoly)], Pp, Qp), ns)
        else:
            chP = ret.children[r[0]]; chQ = ret.children[r[2]]
            Pp = transPt(chQ[0], chQ[1].shape[r[3]]); Qp = transPt(chP[0], chP[1].shape[r[1]])
            ns = shapes[r[4]]; npoly = ns.shape
            ret.add(matchTwo(npoly[r[5]], npoly[(r[5] + 1) % len(npoly)], Pp, Qp), ns)
    return ret

def constructMetatiles(patch):
    bps1 = patch.evalChild(8, 2); bps2 = patch.evalChild(21, 2)
    rbps = transPt(rotAbout(bps1, -2), bps2)
    p72 = patch.evalChild(7, 2); p252 = patch.evalChild(25, 2)
    llc = intersect(bps1, rbps, patch.evalChild(6, 2), p72)
    w = psub(patch.evalChild(6, 2), llc)
    Ho = [llc, bps1]
    w = transPt(trot_k60(-1), w)
    Ho.append(padd(Ho[1], w))
    Ho.append(patch.evalChild(14, 2))
    w = transPt(trot_k60(-1), w)
    Ho.append(psub(Ho[3], w))
    Ho.append(patch.evalChild(6, 2))
    nH = Meta(Ho)
    for ch in [0, 9, 16, 27, 26, 6, 1, 8, 10, 15]:
        nH.add(*patch.children[ch])
    nP = Meta([p72, padd(p72, psub(bps1, llc)), bps1, llc])
    for ch in [7, 2, 3, 4, 28]:
        nP.add(*patch.children[ch])
    nF = Meta([bps2, patch.evalChild(24, 2), patch.evalChild(25, 0), p252, padd(p252, psub(llc, bps1))])
    for ch in [21, 20, 22, 23, 24, 25]:
        nF.add(*patch.children[ch])
    AAA = Ho[2]; BBB = padd(Ho[1], psub(Ho[4], Ho[5])); CCC = transPt(rotAbout(BBB, -1), AAA)
    nT = Meta([BBB, CCC, AAA]); nT.add(*patch.children[11])
    for m in (nH, nP, nF, nT):
        m.recentre()
    return [nH, nT, nP, nF]

def expand(g, T, out):
    if isinstance(g, Hat):
        out.append((g.label, T)); return
    for Tc, gc in g.children:
        expand(gc, mul(T, Tc), out)

def build(levels, use_patch=True):
    tiles = init()
    for _ in range(levels):
        tiles = constructMetatiles(constructPatch(*tiles))
    out = []
    # NB: the construction patch contains placements that the supertile step
    # discards (they overlap); only expand genuine supertiles.
    expand(tiles[0], IDENT, out)
    hats = []
    for lab, T in out:
        det = T[0] * T[4] - T[1] * T[3]
        hats.append((lab, det.sign() < 0, [transPt(T, p) for p in hat_outline]))
    return hats

# ------------------------------------------------------------- verification
def area2(poly):
    s = ZERO
    for i in range(len(poly)):
        x0, y0 = poly[i]; x1, y1 = poly[(i + 1) % len(poly)]
        s = s + (x0 * y1 - x1 * y0)
    return s

def ref_kites():
    """the 8 grid kites of the reference hat (hexPt units, hex side 2):
    try all 12 cosets of the hex-centre lattice; exactly one gives 8 kites
    with centroids inside the hat and total area = hat area."""
    rot = [hexPt(2, 0), hexPt(0, 2), hexPt(-2, 2), hexPt(-2, 0), hexPt(0, -2), hexPt(2, -2)]   # hex vertices (dist 2)
    mids = [hexPt(1, 1), hexPt(-1, 2), hexPt(-2, 1), hexPt(-1, -1), hexPt(1, -2), hexPt(2, -1)]  # edge midpoints at 30+60k
    A = area2(hat_outline)
    found = None
    for ox in range(-6, 7):
        for oy in range(-6, 7):
            c0 = hexPt(ox, oy)
            ks = []
            for i in range(-4, 5):
                for j in range(-4, 5):
                    c = padd(c0, padd(transPt([q3(i), ZERO, ZERO, ZERO, q3(i), ZERO], hexPt(2, 2)),
                                      transPt([q3(j), ZERO, ZERO, ZERO, q3(j), ZERO], hexPt(-2, 4))))
                    for k in range(6):
                        kite = [c, padd(c, mids[k]), padd(c, rot[(k + 1) % 6]), padd(c, mids[(k + 1) % 6])]
                        cen = (sum((p[0] for p in kite), ZERO) / 4, sum((p[1] for p in kite), ZERO) / 4)
                        if point_in_poly(cen, hat_outline):
                            ks.append(kite)
            if len(ks) == 8 and sum((area2(k) for k in ks), ZERO) == A:
                found = ks
                return found
    raise RuntimeError('no kite decomposition')

def verify(levels):
    """exact tiling checks on the patch"""
    tiles = init()
    for _ in range(levels):
        tiles = constructMetatiles(constructPatch(*tiles))
    out = []; expand(tiles[0], IDENT, out)
    RK = ref_kites()
    cents = {}
    for idx, (lab, T) in enumerate(out):
        for k in RK:
            kk = [transPt(T, p) for p in k]
            cen = (sum((p[0] for p in kk), ZERO) / 4, sum((p[1] for p in kk), ZERO) / 4)
            key = (cen[0].key(), cen[1].key())
            if key in cents:
                return {'ok': False, 'overlap_at_hat': idx}
            cents[key] = (idx, kk)
    # common grid: the hex centres (kite vertex 0) of all kites must form one lattice coset;
    # check via: every kite centre-vertex c satisfies (c - c_ref) in the hex-centre lattice
    # (basis b1 = (3/2, sqrt3/2), b2 = (0, sqrt3) after the 1/2 scale)
    c_ref = next(iter(cents.values()))[1][0]
    b1 = (q3(Fr(3, 2)), HR3); b2 = (ZERO, R3)
    det = b1[0] * b2[1] - b1[1] * b2[0]
    for idx, kk in cents.values():
        d = psub(kk[0], c_ref)
        u = (d[0] * b2[1] - d[1] * b2[0]) / det; v = (b1[0] * d[1] - b1[1] * d[0]) / det
        if u.b != 0 or v.b != 0 or u.a.denominator != 1 or v.a.denominator != 1:
            return {'ok': False, 'off_grid_hat': idx}
    # gap-free core: all grid kites with centre within radius r of the patch centroid are covered
    xs = [float(kk[0][0]) for i, kk in cents.values()]; ys = [float(kk[0][1]) for i, kk in cents.values()]
    cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
    # largest radius r such that every grid hex centre within r has all 6 kites covered
    hexes = {}
    for idx, kk in cents.values():
        hexes.setdefault((kk[0][0].key(), kk[0][1].key()), [kk[0], 0])[1] += 1
    # enumerate lattice hex centres near the patch and find the nearest incomplete one
    import math
    best = None
    rad = max(math.hypot(x - cx, y - cy) for x, y in zip(xs, ys))
    nmax = int(rad / 1.5) + 3
    for i in range(-nmax, nmax + 1):
        for j in range(-2 * nmax, 2 * nmax + 1):
            c = padd(c_ref, padd((b1[0] * i, b1[1] * i), (b2[0] * j, b2[1] * j)))
            r = math.hypot(float(c[0]) - cx, float(c[1]) - cy)
            if r > rad + 2:
                continue
            got = hexes.get((c[0].key(), c[1].key()), [None, 0])[1]
            if got < 6 and (best is None or r < best):
                best = r
    return {'ok': True, 'hats': len(out), 'kites': len(cents), 'covered_core_radius': best,
            'patch_radius': rad, 'reflected_hats': sum(1 for l, T in out if (T[0] * T[4] - T[1] * T[3]).sign() < 0)}

def point_in_poly(p, poly):
    # exact winding test (non-degenerate: p not on boundary)
    wn = 0
    x, y = p
    n = len(poly)
    for i in range(n):
        x0, y0 = poly[i]; x1, y1 = poly[(i + 1) % n]
        c = ((x1 - x0) * (y - y0) - (x - x0) * (y1 - y0)).sign()
        if (y0 - y).sign() <= 0:
            if (y1 - y).sign() > 0 and c > 0:
                wn += 1
        else:
            if (y1 - y).sign() <= 0 and c < 0:
                wn -= 1
    return wn != 0

if __name__ == '__main__':
    lev = int(sys.argv[1]); outp = sys.argv[2]
    hats = build(lev)
    json.dump([{'label': l, 'reflected': r,
                'verts': [[[str(p[0].a), str(p[0].b)], [str(p[1].a), str(p[1].b)]] for p in V]}
               for l, r, V in hats], open(outp, 'w'))
    print('hats', len(hats), 'reflected', sum(1 for h in hats if h[1]))
    print('verification', verify(lev))
