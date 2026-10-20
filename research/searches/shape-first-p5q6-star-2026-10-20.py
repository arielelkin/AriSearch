"""Exact P5/Q6 local patch and boundary-branch verifier (Sage Python)."""
from sage.all import AA, NumberField, PolynomialRing, QQ, matrix, vector
import importlib.util
from pathlib import Path
from itertools import combinations_with_replacement

R = PolynomialRing(QQ, 'x')
x = R.gen()
K = NumberField(x**4-10*x**2+1, 't', embedding=AA(2).sqrt()+AA(3).sqrt())
t = K.gen()
r = (t-1/t)/2 # sqrt(2)
s = (t+1/t)/2 # sqrt(3)
assert r*r == 2 and s*s == 3 and r > 0 and s > 0
V = lambda x, y: vector(K, (x, y))
l1 = K(3)
l2 = (13*r-3*s+3)/2
l3 = (3*r*s-13+5*s)/2
assert l2 > 0 and l3 > 0
PD = [V(1, 0), V(r/2, r/2), V(-(r*s+r)/4, (r*s-r)/4),
      V(-s/2, -1/2), V(1/2, -s/2)]
PL = (5, l1, l2, l3, 4)
P = [V(0, 0)]
for i in range(4):
    P.append(P[-1]+PL[i]*PD[i])
assert P[-1]+PL[4]*PD[4] == P[0]
L = (5, 1, 4, 3, 3, 2)
D = [V(1, 0), V(1, s)/2, V(-1, s)/2,
     V(-1, 0), V(-1, -s)/2, V(1, -s)/2]
Q = [V(0, 0)]
for i in range(5):
    Q.append(Q[-1] + L[i]*D[i])
assert Q[-1] + L[5]*D[5] == Q[0]

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def convex(poly):
    return all(cross(poly[(i+1)%len(poly)]-poly[i],
                     poly[(i+2)%len(poly)]-poly[(i+1)%len(poly)]) > 0
               for i in range(len(poly)))

assert convex(P) and convex(Q)
assert all(l2 != z for z in (PL[0], PL[1], PL[3], PL[4], *L))
assert l3 != 4
palette = (60, 90, 120, 135)
assert not any(sum(c) == 165 for n in range(1, 4)
               for c in combinations_with_replacement(palette, n))
assert [(c) for c in palette if 135+135+c == 360] == [90]

# Reuse the repository's reviewed Rao Table 2 transcription, evaluating its
# side equations in this exact number field (not the older pi/5 field).
spec = importlib.util.spec_from_file_location('rao_filter',
    Path(__file__).with_name('convex-substitution-shapes.py'))
rao_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rao_mod)
PA = (120, 135, 60, 135, 90)
rao_hits = []
for typ, (angle_eqs, length_eqs) in rao_mod.RAO.items():
    for sign in (1, -1):
        for off in range(5):
            amap = [(off+sign*i)%5 for i in range(5)]
            rotated = [PA[j] for j in amap]
            if not all(sum(a*b for a, b in zip(row, rotated)) == target*36
                       for row, target in angle_eqs):
                continue
            smap = ([(off+i)%5 for i in range(5)] if sign == 1 else
                    [(off-i-1)%5 for i in range(5)])
            if all(sum((c*PL[j] for c, j in zip(row, smap)), K(0)) == 0
                   for row in length_eqs):
                rao_hits.append((typ, sign, off))
assert not rao_hits

def place(poly, vertex, neighbor_a, target_a, neighbor_b, target_b):
    """Unique linear isometry taking two corner rays to target rays."""
    x = poly[neighbor_a]-poly[vertex]
    y = poly[neighbor_b]-poly[vertex]
    X = matrix(K, [[x[0], y[0]], [x[1], y[1]]])
    Y = matrix(K, [[target_a[0], target_b[0]],
                   [target_a[1], target_b[1]]])
    M = Y * X.inverse()
    assert M.transpose()*M == matrix.identity(K, 2)
    return [M*(v-poly[vertex]) for v in poly]

# Three 120-degree sectors around the origin.  The shared radial sides
# have lengths 5 (P/Qa), 1 (Qa/Qb), and 4 (Qb/P).
Qa = place(Q, 1, 0, V(5, 0), 2, V(-1, -s)/2)
Qb = place(Q, 2, 1, V(-1, -s)/2, 3, V(-2, 2*s))

def overlap(a, b):
    """Exact separating-axis test: true iff convex interiors overlap."""
    for poly in (a, b):
        for i in range(len(poly)):
            edge = poly[(i+1)%len(poly)]-poly[i]
            normal = V(-edge[1], edge[0])
            aa = [normal*v for v in a]
            bb = [normal*v for v in b]
            if max(aa) <= min(bb) or max(bb) <= min(aa):
                return False
    return True

assert not overlap(P, Qa) and not overlap(P, Qb) and not overlap(Qa, Qb)

# Attach a Q across each exterior length-3 side of Qb.  The fourth tile
# may use either of Q's inequivalent native length-3 sides (slots 3, 4).
branches = []
for host_side in (3, 4):
    h0, h1 = Qb[host_side], Qb[(host_side+1)%6]
    for new_side in (3, 4):
        # Orientation-preserving copy reverses endpoint order.  A reflected
        # copy keeps endpoint order; both lie outside the host edge.
        for reflected in (False, True):
            i, j = new_side, (new_side+1)%6
            x = Q[j]-Q[i]
            target_a, target_b = (h1, h0) if not reflected else (h0, h1)
            u = target_b-target_a
            if not reflected:
                M = matrix(K, [[(x*u)/(x*x), -cross(x,u)/(x*x)],
                               [cross(x,u)/(x*x), (x*u)/(x*x)]])
            else:
                a = (x[0]*u[0]-x[1]*u[1])/(x*x)
                b = (x[0]*u[1]+x[1]*u[0])/(x*x)
                M = matrix(K, [[a, b], [b, -a]])
            placed = [target_a + M*(v-Q[i]) for v in Q]
            assert M.transpose()*M == matrix.identity(K, 2)
            assert convex(placed) or convex(list(reversed(placed)))
            if not any(overlap(placed, z) for z in (P, Qa, Qb)):
                branches.append((host_side, new_side, reflected, placed))

print('P=', P)
print('Q=', Q)
print('P lengths=', PL)
print('P angle word=', PA, '; Rao monohedral hits=', rao_hits)
print('P lengths squared=', [v*v for i in range(5)
                             for v in [P[(i+1)%5]-P[i]]])
print('Q lengths=', L)
print('P/Q/Q star: PASS')
print('legal fourth-tile branches=', [(h, n, sw) for h, n, sw, _ in branches])
for h, n, sw, poly in branches:
    print('BRANCH', h, n, sw, poly)
