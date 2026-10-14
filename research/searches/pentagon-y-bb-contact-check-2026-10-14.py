"""Exact diagnostic for the sole longer-containing BB contact profile.

Run: mise exec -- conda run --no-capture-output -n arisearch python
     research/searches/pentagon-y-bb-contact-check-2026-10-14.py

This checks the four-tile contact patch and its fatal far-endpoint order;
the exhaustion proof is in the companion lemma, not inferred from this script.
"""

from itertools import combinations
from sympy import Matrix, Min, Max, simplify, sqrt

S, F = sqrt(2), sqrt(5)
P = [(0, 0), (2, 0), (3, 2), (2, 3), (0, 2)]
Q = [(2, 3), (1, 4), (-1, 4), (-2, 3), (0, 2)]
J = Matrix([[0, -1], [1, 0]])


def host(point):
    x, y = point
    return (simplify((x - y + 1) / S), simplify((x + y - 5) / S))


def isometry(poly, src_i, src_j, dst_i, dst_j, reflect=False):
    u = Matrix(poly[src_j]) - Matrix(poly[src_i])
    v = Matrix(dst_j) - Matrix(dst_i)
    length2 = simplify(u.dot(u))
    assert simplify(length2 - v.dot(v)) == 0
    matrix = (v * u.T + (-1 if reflect else 1) * (J * v) * (J * u).T) / length2
    return [
        tuple(simplify(x) for x in Matrix(dst_i) + matrix * (Matrix(point) - Matrix(poly[src_i])))
        for point in poly
    ]


def sign(value):
    value = simplify(value)
    if value == 0:
        return 0
    if value.is_positive:
        return 1
    if value.is_negative:
        return -1
    raise AssertionError(f"undecided algebraic sign: {value}")


def positive_area_overlap(first, second):
    # Convex separating-axis theorem, with exact radicals and strict area.
    for poly in (first, second):
        for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
            nx, ny = y2 - y1, x1 - x2
            a = [nx * x + ny * y for x, y in first]
            b = [nx * x + ny * y for x, y in second]
            if sign(Min(*a) - Max(*b)) >= 0 or sign(Min(*b) - Max(*a)) >= 0:
                return False
    return True


host_p = [host(vertex) for vertex in P]
mate_p = isometry(P, 1, 2, (0, 0), (F, 0))
overhung_q = isometry(Q, 0, 4, (S, 0), host_p[1], reflect=True)
flush_q = isometry(Q, 1, 2, (0, 0), mate_p[0])
patch = [host_p, mate_p, overhung_q, flush_q]

assert host_p[3] == (0, 0) and host_p[2] == (S, 0)
assert mate_p[1] == (0, 0) and mate_p[2] == (F, 0)
assert overhung_q[0] == (S, 0) and overhung_q[4] == host_p[1]
assert flush_q[1] == (0, 0) and flush_q[2] == mate_p[0]
assert flush_q[0] == (-F / 5, -3 * F / 5)  # C on host B--A side
for first, second in combinations(patch, 2):
    assert not positive_area_overlap(first, second)

# The host A occurs strictly after the forced C but before either possible
# native P arm from the B corner that must fill the C+flat junction.
assert sign(F - S) > 0
assert sign(S - (F - S)) > 0
assert sign(F - (F - S)) > 0

print("exact four-tile contact patch: disjoint; forced B arm overruns host A")
