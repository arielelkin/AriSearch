"""Exact fixture and native-angle verification for private-arm Cairo theorem.
Finite domain and non-consequences are recorded in the corresponding lemma.
No tiling search, floating arithmetic, outputs or certificates are used.
"""
from sage.all import QuadraticField

K = QuadraticField(3, "w")
w = K.gen()


def cross(u, v):
    return u[0]*v[1]-u[1]*v[0]


def sub(u, v):
    return (u[0]-v[0], u[1]-v[1])


def fixture(c, d, e):
    c, d, e = map(K, (c, d, e))
    a = (w*c+d-e)/2
    b = (w*(d+e)-c)/2
    lengths = (a, b, c, d, e)
    vertices = ((K(0), K(0)), (a, K(0)), (a, b),
                (a-w*c/2, b+c/2), (-e/2, w*e/2))
    assert all(x > 0 for x in lengths)
    assert len(set(lengths)) == 5
    for i in range(5):
        edge = sub(vertices[(i+1)%5], vertices[i])
        assert edge[0]**2+edge[1]**2 == lengths[i]**2
        for j in range(5):
            if j not in (i, (i+1)%5):
                assert cross(edge, sub(vertices[j], vertices[i])) > 0
        next_edge = sub(vertices[(i+2)%5], vertices[(i+1)%5])
        dot = edge[0]*next_edge[0]+edge[1]*next_edge[1]
        desired = K(0) if i in (0, 2) else K(1)/2
        assert dot == desired*lengths[i]*lengths[(i+1)%5]
    return lengths


P = fixture(1, 2, 3)
Q = fixture(4, 5, 6)
arms = P[:4]+Q[:4]
assert len(set(arms)) == 8
assert set(P) != set(Q)
for e in (P[4], Q[4]):
    assert all(e != 2*r for r in arms)
full = [(u, v) for u in range(5) for v in range(4)
        if 90*u+120*v == 360]
half = [(u, v) for u in range(5) for v in range(4)
        if 90*u+120*v == 180]
assert full == [(0, 3), (4, 0)]
assert half == [(2, 0)]
print("PASS: two exact convex private-arm Cairo fixtures; 16 doubled-length exclusions; full/half stars")
