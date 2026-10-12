#!/usr/bin/env python3
"""Exact pi/5 polygon geometry and a complete corner-filling dissection search.

Number model.  Z[phi] elements are integer pairs (a,b) = a+b*phi, phi^2=phi+1.
A point (or vector) of the plane is stored as (X2,Y) with X2=2*Re, Y=Im/sin(pi/5),
both in Z[phi]; the 4-tuple of integers is hashable and exact.  Every side
direction is zeta^k, zeta=exp(i*pi/5), k=0..9:
    2cos(k pi/5) in Z[phi],  sin(k pi/5)/sin(pi/5) in Z[phi].
Cross products have the sign of X2_u*Y_v-Y_u*X2_v in Z[phi] (positive factor
sin(pi/5)/2 removed).  4*dot = X2*X2' + (3-phi)*Y*Y'.  Area unit: the shoelace
sum of X2_i*Y_{i+1}-Y_i*X2_{i+1} equals 4*area/sin(pi/5).

No floating point is used in any decision.  Floats appear only in printing.

Dissection search (completeness argument, see convex-substitution-search.md):
all child sides lie in the 2N directions (N=5 by default; configure(N) for 4,6), so the plane splits
into ten basic sectors of angle pi/5; each child covers a contiguous set of
sectors at each of its corners (its angle) and five sectors at points interior
to its sides.  The uncovered part of the parent, if nonempty, is a polygon with a
convex corner; that corner is a corner of a placed child or of the parent, and
its uncovered sector is a maximal run of m<5 zero bits starting at direction a.
The child covering the sector next to ray a must have a corner there, with
outgoing CCW side in direction a and angle <= m.  Branching over all such
children is therefore exhaustive.  Pairwise interior-disjointness is the exact
separating-axis test over the five side normals (all sides are parallel to one
of five lines), containment is exact half-plane testing.
"""
from itertools import product

# ---------------------------------------------------------------- Z[phi]
def zadd(u, v): return (u[0] + v[0], u[1] + v[1])
def zsub(u, v): return (u[0] - v[0], u[1] - v[1])
def zneg(u): return (-u[0], -u[1])
# ring Z[w] with w^2 = Q0 + Q1*w ; configured by configure(N)
Q0, Q1 = 1, 1
def zmul(u, v):
    a, b = u; c, d = v
    bd = b * d
    return (a * c + Q0 * bd, a * d + b * c + Q1 * bd)
def zscale(n, u): return (n * u[0], n * u[1])

def zsign(u):
    """Exact sign of a+b*w.  phi: (2a+b)/2+(b/2)sqrt5; sqrt d: a+b*sqrt d."""
    if Q1 == 1:
        p = 2 * u[0] + u[1]; q = u[1]; D = 5
    else:
        p = u[0]; q = u[1]; D = Q0
    if p >= 0 and q >= 0:
        return 0 if (p == 0 and q == 0) else 1
    if p <= 0 and q <= 0:
        return -1
    # opposite signs: compare p^2 with 5 q^2
    if p > 0:  # q<0
        return 1 if p * p > D * q * q else -1
    return 1 if D * q * q > p * p else -1

def zfloat(u):
    import math
    w = (1 + math.sqrt(5)) / 2 if Q1 == 1 else math.sqrt(Q0)
    return u[0] + u[1] * w

ZERO = (0, 0); ONE = (1, 0); PHI = (0, 1)

# 2cos(k pi/5) and sin(k pi/5)/sin(pi/5)
C2 = [(2, 0), (0, 1), (-1, 1), (1, -1), (0, -1), (-2, 0), (0, -1), (1, -1), (-1, 1), (0, 1)]
S = [(0, 0), (1, 0), (0, 1), (0, 1), (1, 0), (0, 0), (-1, 0), (0, -1), (0, -1), (-1, 0)]
THREE_MINUS_PHI = (3, -1)   # dot weight for N=5 (Y = Im/sin(pi/5))
NDIR = 10; HALF = 5; DOTW = (3, -1); YSCALE_N5 = True

def configure(N):
    """N=5: Z[phi], Y=Im/sin(pi/5).  N=4: Z[sqrt2], N=6: Z[sqrt3], Y=2Im."""
    global Q0, Q1, C2, S, NDIR, HALF, DOTW, FULL, UNIT, THREE_MINUS_PHI
    NDIR = 2 * N; HALF = N
    if N == 5:
        Q0, Q1 = 1, 1; DOTW = (3, -1)
        C2 = [(2, 0), (0, 1), (-1, 1), (1, -1), (0, -1), (-2, 0), (0, -1), (1, -1), (-1, 1), (0, 1)]
        S = [(0, 0), (1, 0), (0, 1), (0, 1), (1, 0), (0, 0), (-1, 0), (0, -1), (0, -1), (-1, 0)]
    elif N == 6:
        Q0, Q1 = 3, 0; DOTW = (1, 0)
        C2 = [(2,0),(0,1),(1,0),(0,0),(-1,0),(0,-1),(-2,0),(0,-1),(-1,0),(0,0),(1,0),(0,1)]
        S = [(0,0),(1,0),(0,1),(2,0),(0,1),(1,0),(0,0),(-1,0),(0,-1),(-2,0),(0,-1),(-1,0)]
    elif N == 4:
        Q0, Q1 = 2, 0; DOTW = (1, 0)
        C2 = [(2,0),(0,1),(0,0),(0,-1),(-2,0),(0,-1),(0,0),(0,1)]
        S = [(0,0),(0,1),(2,0),(0,1),(0,0),(0,-1),(-2,0),(0,-1)]
    else:
        raise ValueError(N)
    THREE_MINUS_PHI = DOTW
    FULL = (1 << NDIR) - 1
    UNIT = [vec(ONE, k) for k in range(NDIR)]

# ---------------------------------------------------------------- vectors
def vec(length, k):
    k %= NDIR
    return zmul(length, C2[k]) + zmul(length, S[k])

def padd(p, q): return (p[0] + q[0], p[1] + q[1], p[2] + q[2], p[3] + q[3])
def psub(p, q): return (p[0] - q[0], p[1] - q[1], p[2] - q[2], p[3] - q[3])
def pscale(lam, p):
    return zmul(lam, p[0:2]) + zmul(lam, p[2:4])

def cross(u, v):
    return zsub(zmul(u[0:2], v[2:4]), zmul(u[2:4], v[0:2]))

def dot4(u, v):
    return zadd(zmul(u[0:2], v[0:2]), zmul(DOTW, zmul(u[2:4], v[2:4])))

UNIT = [vec(ONE, k) for k in range(10)]

def direction(v):
    for k in range(NDIR):
        if cross(UNIT[k], v) == ZERO and zsign(dot4(UNIT[k], v)) > 0:
            return k
    raise ValueError("not a pi/5 direction")

def conj(p):  # reflection in the real axis
    return (p[0], p[1], -p[2], -p[3])

def rotate(p, k):
    """multiply by zeta^k: (X+isY)(C+isS) = XC - s^2 YS + i s (XS+YC)."""
    k %= NDIR
    X2, Y = p[0:2], p[2:4]
    c2, s = C2[k], S[k]
    # N=5: new X2 = (X2*c2 - (3-phi) Y S)/2 (s^2=(3-phi)/4); N=4,6 (Y=2Im): (X2 c2 - Y S2)/2
    nx2 = zsub(zmul(X2, c2), zmul(DOTW, zmul(Y, s)))
    assert nx2[0] % 2 == 0 and nx2[1] % 2 == 0, nx2
    nx2 = (nx2[0] // 2, nx2[1] // 2)
    # new Y = X S + Y C = (X2*s + Y*c2)/2
    ny = zadd(zmul(X2, s), zmul(Y, c2))
    assert ny[0] % 2 == 0 and ny[1] % 2 == 0, ny
    ny = (ny[0] // 2, ny[1] // 2)
    return nx2 + ny

def pfloat(p):
    import math
    ys = math.sin(math.pi / 5) if HALF == 5 else 0.5
    return (zfloat(p[0:2]) / 2, zfloat(p[2:4]) * ys)

# ---------------------------------------------------------------- polygons
def polygon_from_word(angles, lengths):
    """angles[i] = interior angle (pi/5 units) at vertex i; side i joins vertex i
    to i+1; CCW; vertex0 at origin, side0 along direction 0.  Returns vertices
    or None when the polygon does not close."""
    n = len(angles)
    pts = [(0, 0, 0, 0)]
    d = 0
    for i in range(n):
        pts.append(padd(pts[-1], vec(lengths[i], d)))
        d += HALF - angles[(i + 1) % n]
    if pts[-1] != (0, 0, 0, 0):
        return None
    return pts[:-1]

def area4(pts):
    """4*area/sin(pi/5) in Z[phi]."""
    tot = ZERO
    n = len(pts)
    for i in range(n):
        tot = zadd(tot, cross(pts[i], pts[(i + 1) % n]))
    return tot

def is_strictly_convex_ccw(pts):
    n = len(pts)
    for i in range(n):
        a, b, c = pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        if zsign(cross(psub(b, a), psub(c, b))) <= 0:
            return False
    return True

def interior_angles(pts):
    n = len(pts)
    out = []
    for i in range(n):
        a = direction(psub(pts[(i + 1) % n], pts[i]))
        b = direction(psub(pts[(i - 1) % n], pts[i]))
        out.append((b - a) % NDIR)
    return out

def orientations(pts):
    """All 20 images (10 rotations x optional reflection), CCW vertex lists,
    deduplicated as point sets relative to vertex placement later."""
    res = []
    for refl in (False, True):
        base = [conj(p) for p in pts][::-1] if refl else list(pts)
        for k in range(NDIR):
            res.append(((k, refl), [rotate(p, k) for p in base]))
    return res

class Placed:
    __slots__ = ("pts", "dirs", "angles", "shape", "key", "lo", "hi")
    def __init__(self, pts, shape):
        self.pts = pts
        n = len(pts)
        self.dirs = [direction(psub(pts[(i + 1) % n], pts[i])) for i in range(n)]
        self.angles = [(self.dirs[(i - 1) % n] + HALF - self.dirs[i]) % NDIR for i in range(n)]
        self.shape = shape
        self.key = frozenset(pts)
        # projections onto the five axis normals: cross(UNIT[k], p) for k=0..4
        self.lo = []; self.hi = []
        for k in range(HALF):
            vals = [cross(UNIT[k], p) for p in pts]
            lo = vals[0]; hi = vals[0]
            for v in vals[1:]:
                if zsign(zsub(v, lo)) < 0: lo = v
                if zsign(zsub(v, hi)) > 0: hi = v
            self.lo.append(lo); self.hi.append(hi)

def disjoint_interiors(P, Q):
    for k in range(HALF):
        if zsign(zsub(P.hi[k], Q.lo[k])) <= 0 or zsign(zsub(Q.hi[k], P.lo[k])) <= 0:
            return True
    return False

def contained(P, parent_pts):
    n = len(parent_pts)
    for i in range(n):
        a, b = parent_pts[i], parent_pts[(i + 1) % n]
        e = psub(b, a)
        for p in P.pts:
            if zsign(cross(e, psub(p, a))) < 0:
                return False
    return True

def on_open_segment(p, a, b):
    e = psub(b, a)
    if cross(e, psub(p, a)) != ZERO:
        return False
    t = dot4(e, psub(p, a))
    return zsign(t) > 0 and zsign(zsub(t, dot4(e, e))) < 0

def sector_bits(start, m):
    bits = 0
    for j in range(m):
        bits |= 1 << ((start + j) % NDIR)
    return bits

FULL = (1 << 10) - 1

def runs(mask):
    """maximal cyclic runs of zero bits: list of (start, length)."""
    if mask == FULL:
        return []
    if mask == 0:
        return [(0, NDIR)]
    out = []
    for s in range(NDIR):
        if not (mask >> s) & 1 and (mask >> ((s - 1) % NDIR)) & 1:
            m = 0
            while not (mask >> ((s + m) % NDIR)) & 1:
                m += 1
            out.append((s, m))
    return out

class Dissector:
    """Search for a dissection of a convex pi/5 parent polygon into copies of
    given shapes with prescribed counts.  shapes: dict name -> reference CCW pts.
    """
    def __init__(self, parent_pts, shapes, counts, node_limit=10**6, want=1, choose_mode="min"):
        self.choose_mode = choose_mode   # "min" (default), "max" or "near": any point with a run < pi is complete
        self.anchor = parent_pts[0]; self.radius2 = None; self.radius_hit = False
        self.parent = parent_pts
        self.counts = dict(counts)
        self.node_limit = node_limit
        self.want = want
        self.nodes = 0
        self.solutions = []
        self.limit_hit = False
        # corner catalogue: (shape, oriented pts, vertex index, outgoing dir, angle)
        self.catalogue = {}  # (outdir) -> list of (angle, shape, pts relative to vertex)
        for name, pts in shapes.items():
            seen = set()
            for (_, opts) in orientations(pts):
                n = len(opts)
                for j in range(n):
                    rel = [psub(q, opts[j]) for q in opts]
                    key = frozenset(rel)
                    if key in seen:
                        continue
                    seen.add(key)
                    out = direction(psub(opts[(j + 1) % n], opts[j]))
                    inn = direction(psub(opts[(j - 1) % n], opts[j]))
                    ang = (inn - out) % NDIR
                    self.catalogue.setdefault(out, []).append((ang, name, rel))
        for k in self.catalogue:
            self.catalogue[k].sort(key=lambda t: -t[0])

    def initial_points(self):
        pts = {}
        n = len(self.parent)
        for i in range(n):
            out = direction(psub(self.parent[(i + 1) % n], self.parent[i]))
            inn = direction(psub(self.parent[(i - 1) % n], self.parent[i]))
            ang = (inn - out) % NDIR
            pts[self.parent[i]] = FULL & ~sector_bits(out, ang)
        return pts

    def parent_exterior(self, p):
        n = len(self.parent)
        for i in range(n):
            a, b = self.parent[i], self.parent[(i + 1) % n]
            if on_open_segment(p, a, b):
                d = direction(psub(b, a))
                return FULL & ~sector_bits(d, HALF)
        return 0

    def run(self):
        points = self.initial_points()
        self._dfs(points, [], dict(self.counts))
        return self.solutions

    def _choose(self, points):
        best = None
        for p, mask in points.items():
            if mask == FULL:
                continue
            for (s, m) in runs(mask):
                if m >= HALF:
                    continue
                if self.choose_mode == "near":
                    dist = self._dist2(p)
                    if best is None or dist < best[3]:
                        best = (p, s, m, dist)
                    continue
                if self.choose_mode == "max":
                    if best is None or m > best[2]:
                        best = (p, s, m)
                elif best is None or m < best[2]:
                    best = (p, s, m)
                    if m == 1:
                        return best
        if best is not None and len(best) == 4:
            if self.radius2 is not None and best[3] > self.radius2:
                self.radius_hit = True
                return None
            best = best[:3]
        return best

    def _dist2(self, p):
        x, y = pfloat(psub(p, self.anchor))
        return x * x + y * y

    def _dfs(self, points, placed, remaining):
        if len(self.solutions) >= self.want or self.limit_hit:
            return
        self.nodes += 1
        if self.nodes > self.node_limit:
            self.limit_hit = True
            return
        if all(v == 0 for v in remaining.values()):
            # area forces complete cover; verify every tracked point is full
            if all(mask == FULL for mask in points.values()):
                self.solutions.append([(c.shape, c.pts) for c in placed])
            return
        ch = self._choose(points)
        if ch is None:
            return
        p, s, m = ch
        for (ang, name, rel) in self.catalogue.get(s, []):
            if ang > m or remaining.get(name, 0) == 0:
                continue
            cpts = [padd(p, q) for q in rel]
            C = Placed(cpts, name)
            if not contained(C, self.parent):
                continue
            if any(not disjoint_interiors(C, D) for D in placed):
                continue
            newpoints = self._update(points, C, placed)
            if newpoints is None:
                continue
            remaining[name] -= 1
            placed.append(C)
            self._dfs(newpoints, placed, remaining)
            placed.pop()
            remaining[name] += 1
            if len(self.solutions) >= self.want or self.limit_hit:
                return

    def _update(self, points, C, placed):
        pts = dict(points)
        n = len(C.pts)
        # existing points on C's open sides
        for p, mask in points.items():
            for i in range(n):
                a, b = C.pts[i], C.pts[(i + 1) % n]
                if on_open_segment(p, a, b):
                    bits = sector_bits(C.dirs[i], HALF)
                    if pts[p] & bits:
                        return None
                    pts[p] |= bits
                    break
        for i in range(n):
            v = C.pts[i]
            if v not in pts:
                mask = self.parent_exterior(v)
                for D in placed:
                    m = len(D.pts)
                    for j in range(m):
                        if on_open_segment(v, D.pts[j], D.pts[(j + 1) % m]):
                            mask |= sector_bits(D.dirs[j], HALF)
                            break
                pts[v] = mask
            bits = sector_bits(C.dirs[i], C.angles[i])
            if pts[v] & bits:
                return None
            pts[v] |= bits
        return pts


def wedge_test(shapes, alpha, radius=30.0, node_limit=200000, legs=(4000, 0)):
    """Local corner obstruction.  Parent: parallelogram with apex angle alpha (units
    pi/N) at the origin, legs of length `legs` (Z[w]), unlimited child counts.
    Points are chosen nearest to the apex (float distance only orders choices;
    every choice with a run < pi is complete).  If a point with a run < pi
    would have to be chosen farther than `radius` from the apex, the test stops
    as INCONCLUSIVE ("radius").  Result "dead" means: the search tree is
    finite, every chosen point lies within `radius` of the apex, so every
    convex parent whose corner of angle alpha has both adjacent sides longer
    than the certified radius bound (see search record) has no dissection.
    Returns (status, nodes, max_vertex_distance)."""
    # parallelogram with angle alpha at the apex (origin); other corners far
    v0 = (0, 0, 0, 0); v1 = vec(legs, 0); v3 = vec(legs, alpha); v2 = padd(v1, v3)
    parent = [v0, v1, v2, v3]
    assert is_strictly_convex_ccw(parent)
    counts = {k: 10 ** 9 for k in shapes}
    D = Dissector(parent, shapes, counts, node_limit=node_limit, want=1, choose_mode="near")
    D.anchor = v0; D.radius2 = radius * radius
    maxd = [0.0]
    orig = D._update
    def upd(points, C, placed):
        r = orig(points, C, placed)
        if r is not None:
            for q in C.pts:
                maxd[0] = max(maxd[0], D._dist2(q) ** 0.5)
        return r
    D._update = upd
    sols = D.run()
    if D.limit_hit: return ("node-limit", D.nodes, maxd[0])
    if D.radius_hit: return ("radius", D.nodes, maxd[0])
    if sols: return ("solution?!", D.nodes, maxd[0])
    return ("dead", D.nodes, maxd[0])
