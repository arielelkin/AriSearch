#!/usr/bin/env python3
"""Integer-lattice model of a hat patch and of hat decorations.

Used as a module by source-decoration-hat-search.py.

Lattice: the hat outline (Kaplan's hexPt units) has integer coordinates in
the basis e1 = (1,0), e2 = (1/2, sqrt3/2).  A patch hat is an exact image of
the reference hat under an isometry; after scaling by 2 every patch vertex
is an integer lattice point.  Everything below is integer arithmetic:
  dot2(a,b)  = 2<a,b> = 2a1b1 + a1b2 + a2b1 + 2a2b2
  cross(a,b) = a1b2 - a2b1      (true cross = sqrt3/2 * cross)
The 12 lattice isometries fixing 0 are rotations by 60k (matrix R^k with
R = [[0,-1],[1,1]] acting on coordinate columns) and their compositions
with the reflection S = [[1,1],[0,-1]].
"""
import json, math
from fractions import Fraction as Fr
from math import gcd

HAT = [(0, 0), (-1, -1), (0, -2), (2, -2), (2, -1), (4, -2), (5, -1), (4, 0),
       (3, 0), (2, 2), (0, 3), (0, 2), (-1, 2)]

def matvec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])
def matmul(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]
R = [[0, -1], [1, 1]]
S = [[1, 1], [0, -1]]
I2 = [[1, 0], [0, 1]]
ISOS = []
M = I2
for k in range(6):
    ISOS.append((M, False)); ISOS.append((matmul(M, S), True)); M = matmul(R, M)

def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def cross(a, b): return a[0] * b[1] - a[1] * b[0]
def dot2(a, b): return 2 * a[0] * b[0] + a[0] * b[1] + a[1] * b[0] + 2 * a[1] * b[1]
def norm2(a): return dot2(a, a)

def half(a):
    """0 for directions in [0,180), 1 for [180,360) -- exact"""
    y = a[1]                       # sign of true y = sign(a2)
    if y > 0: return 0
    if y < 0: return 1
    return 0 if (2 * a[0] + a[1]) > 0 else 1

def ang_lt(a, b):
    ha, hb = half(a), half(b)
    if ha != hb: return ha < hb
    return cross(a, b) > 0

def ccw_turn_le180(a, b):
    """is the ccw angle from direction a to direction b in (0, 180]?"""
    c = cross(a, b)
    if c > 0: return True
    if c < 0: return False
    return dot2(a, b) < 0          # exactly 180 (opposite); 0 angle excluded

def to_lattice(X, Y):
    """exact Q(sqrt3) point (as (a,b) pairs: a + b sqrt3) -> integer lattice coords at scale 2"""
    # real point = 1/2 (u + v/2, sqrt3 v / 2)  ->  v = 4Y/sqrt3, u = 2X - v/2
    xa, xb = X; ya, yb = Y
    # Y = ya + yb sqrt3 must be a multiple of sqrt3: ya == 0
    assert ya == 0, (X, Y)
    v = 4 * yb
    assert xb == 0
    u = 2 * xa - v / 2
    assert u.denominator == 1 and v.denominator == 1
    return (int(u), int(v))

def load_patch(path):
    H = json.load(open(path))
    hats = []
    for h in H:
        V = [to_lattice((Fr(p[0][0]), Fr(p[0][1])), (Fr(p[1][0]), Fr(p[1][1]))) for p in h['verts']]
        # find isometry: V[i] = M HAT[i] + t
        found = None
        for M, refl in ISOS:
            t = sub(V[0], matvec(M, HAT[0]))
            if all(add(matvec(M, HAT[i]), t) == V[i] for i in range(len(HAT))):
                found = (M, refl, t); break
        assert found is not None
        assert found[1] == h['reflected']
        hats.append({'label': h['label'], 'M': found[0], 'refl': found[1], 't': found[2], 'verts': V})
    return hats

def apply(h, p):
    return add(matvec(h['M'], p), h['t'])

def seg_proper_cross(p1, p2, q1, q2):
    d1 = cross(sub(p2, p1), sub(q1, p1)); d2 = cross(sub(p2, p1), sub(q2, p1))
    d3 = cross(sub(q2, q1), sub(p1, q1)); d4 = cross(sub(q2, q1), sub(p2, q1))
    return ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))

def point_in_closed_poly2(p2x, p2y, poly):
    """p given at doubled coordinates (to test midpoints); poly integer.  Returns
    'in', 'on', 'out' exactly."""
    P = (p2x, p2y)
    n = len(poly)
    Q = [(2 * x, 2 * y) for x, y in poly]
    for i in range(n):
        a, b = Q[i], Q[(i + 1) % n]
        if cross(sub(b, a), sub(P, a)) == 0 and min(a[0], b[0]) <= P[0] <= max(a[0], b[0]) \
                and min(a[1], b[1]) <= P[1] <= max(a[1], b[1]):
            return 'on'
    wn = 0
    for i in range(n):
        a, b = Q[i], Q[(i + 1) % n]
        if a[1] <= P[1]:
            if b[1] > P[1] and cross(sub(b, a), sub(P, a)) > 0:
                wn += 1
        else:
            if b[1] <= P[1] and cross(sub(b, a), sub(P, a)) < 0:
                wn -= 1
    return 'in' if wn != 0 else 'out'

def reference_data(poly=HAT):
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    pts = []
    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            r = point_in_closed_poly2(2 * x, 2 * y, poly)
            if r != 'out':
                pts.append(((x, y), r))
    P = [p for p, r in pts]
    segs = []
    n = len(poly)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            a, b = P[i], P[j]
            d = sub(b, a)
            if gcd(abs(d[0]), abs(d[1])) != 1:
                continue
            if point_in_closed_poly2(a[0] + b[0], a[1] + b[1], poly) == 'out':
                continue
            if any(seg_proper_cross(a, b, poly[k], poly[(k + 1) % n]) for k in range(n)):
                continue
            segs.append((i, j))
    on_boundary = {i for i, (p, r) in enumerate(pts) if r == 'on'}
    return P, segs, on_boundary
