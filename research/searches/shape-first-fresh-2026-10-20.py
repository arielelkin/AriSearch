"""Exact local and periodic-carrier checks for a fresh H6/H6 pair.

Run: mise exec -- conda run --no-capture-output -n arisearch python research/searches/shape-first-fresh-2026-10-20.py
Coordinates use the triangular basis e0=(1,0), e1=(1/2,sqrt(3)/2).
"""

from collections import Counter

U = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
W = ((1, 4, 3, 2, 3, 4), (2, 4, 4, 3, 3, 5))
FAILED = ((1, 4, 2, 3, 2, 4), (2, 4, 4, 3, 3, 5))
ALL_SHARED = ((1, 2, 3, 2, 1, 4), (1, 3, 3, 2, 2, 4))
OLD = ((5, 3, 3, 4, 4, 2), (1, 3, 3, 2, 2, 4))
STATE = {(0, 0): (1, 4, 1), (1, 0): (0, 5, -1),
         (0, 1): (1, 1, 1), (1, 1): (0, 2, -1)}


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def polygon(word):
    vertices = [(0, 0)]
    for length, direction in zip(word, U):
        vertices.append(add(vertices[-1], (length * direction[0],
                                          length * direction[1])))
    assert vertices[-1] == vertices[0]
    return vertices[:-1]


def reflect(p):
    return (p[0] + p[1], -p[1])


def rotate(p):
    return (-p[1], p[0] + p[1])


def rotate_n(p, n):
    for _ in range(n):
        p = rotate(p)
    return p


def overlap(p, q):
    """Strict interior overlap of two convex lattice polygons, by SAT."""
    for source in (p, q):
        for i, a in enumerate(source):
            b = source[(i + 1) % len(source)]
            e = sub(b, a)
            det = lambda x: e[0] * x[1] - e[1] * x[0]
            left = [det(x) for x in p]
            right = [det(x) for x in q]
            if max(left) <= min(right) or max(right) <= min(left):
                return False
    return True


def canonical(word):
    w = list(word)
    return min(tuple(v[i:] + v[:i]) for v in (w, w[::-1]) for i in range(6))


def corners(word):
    return {tuple(sorted((word[i - 1], word[i]))) for i in range(6)}


def corner_counts(word):
    return Counter(tuple(sorted((word[i - 1], word[i]))) for i in range(6))


def quotient(z):
    x, y = z
    carry, y = divmod(y, 2)
    return ((x - carry) % 2, y)


def face(z):
    tile, r, eps = STATE[quotient(z)]
    return polygon(tuple(W[tile][(r + eps * k) % 6] for k in range(6)))


def step(z, k):
    neighbor = add(z, U[k])
    p, q = face(z), face(neighbor)
    assert sub(p[(k + 1) % 6], p[k]) == sub(q[(k + 3) % 6], q[(k + 4) % 6])
    return sub(p[k], q[(k + 4) % 6])


def walk(headings):
    z = (0, 0)
    displacement = (0, 0)
    for k in headings:
        displacement = add(displacement, step(z, k))
        z = add(z, U[k])
    return z, displacement


def main():
    # First symmetric-private-seam seed dies at the end of one arm.
    assert corners(FAILED[0]) == {(1, 4), (2, 4), (2, 3)}
    assert FAILED[0][0] == 1 and 1 not in FAILED[1]
    assert FAILED[0][1] == FAILED[0][5] == 4
    assert FAILED[0][2] == FAILED[0][4] == 2
    assert FAILED[1][1] == FAILED[1][2] == 4
    assert {FAILED[1][0], FAILED[1][3]} == {2, 3}
    assert (4, 4) in corners(FAILED[1]) and (4, 4) not in corners(FAILED[0])
    assert (2, 2) not in corners(FAILED[0]) | corners(FAILED[1])

    # An all-shared alternative fails by corner-demand inequalities.
    ca, cb = map(corner_counts, ALL_SHARED)
    assert set(ALL_SHARED[0]) == set(ALL_SHARED[1]) == {1, 2, 3, 4}
    assert (ca[(1, 4)], ca[(2, 4)], ca[(1, 2)]) == (2, 0, 2)
    assert (cb[(1, 4)], cb[(2, 4)], cb[(1, 2)]) == (1, 1, 0)
    combined = corners(ALL_SHARED[0]) | corners(ALL_SHARED[1])
    assert [x for x in {1, 2, 3, 4}
            if tuple(sorted((1, x))) in combined
            and tuple(sorted((4, x))) in combined] == [2]

    for w in W:
        assert min(w) > 0
        assert w[0] - w[3] == w[2] - w[5] == w[4] - w[1] != 0
        assert sorted(Counter(w).values()) == [1, 1, 2, 2]
        assert len(polygon(w)) == 6
    assert canonical(W[0]) != canonical(W[1])
    assert {canonical(w) for w in W} != {canonical(w) for w in OLD}
    assert corners(W[0]) == {(1, 4), (3, 4), (2, 3)}
    assert corners(W[1]) == {(2, 5), (2, 4), (4, 4), (3, 4), (3, 3), (3, 5)}

    # AA private-1 seam, two B(4,4) caps, and each cap's BB private-5 mate.
    a, b = map(polygon, W)
    aa = [reflect(p) for p in a]
    assert set(aa) == {sub((1, 0), p) for p in a}
    cap_left = [sub(p, b[2]) for p in b]
    cap_right = [add(sub(rotate_n(p, 3), rotate_n(b[2], 3)), (1, 0)) for p in b]
    patch = [a, aa, cap_left, cap_right]
    for cap in (cap_left, cap_right):
        seam_sum = add(cap[5], cap[0])
        patch.append([sub(seam_sum, p) for p in cap])
    assert all(not overlap(patch[i], patch[j])
               for i in range(6) for j in range(i))

    # Four-cell HNF quotient <(2,0),(1,2)>: all twelve edge classes.
    for z in STATE:
        for k in range(3):
            neighbor = add(z, U[k])
            assert step(z, k) == tuple(-v for v in step(neighbor, k + 3))
        for k, j in ((0, 1), (1, 2), (2, 0)):
            first = add(step(z, k), step(add(z, U[k]), j))
            second = add(step(z, j), step(add(z, U[j]), k))
            assert first == second
    p0 = walk((0, 0))
    p1 = walk((0, 1, 1))
    assert p0 == ((2, 0), (4, -12))
    assert p1 == ((1, 2), (13, -10))
    assert p0[1][0] * p1[1][1] - p0[1][1] * p1[1][0] == 116
    print("fresh pair W:", W)
    print("first seed: forced absent (2,2) cap; plane-nontilable")
    print("all-shared seed: corner-demand inequalities; plane-nontilable")
    print("six-tile local patch: exact nonoverlap")
    print("periodic quotient: four faces, twelve seam equalities")
    print("periods in triangular coordinates:", p0[1], p1[1])


if __name__ == "__main__":
    main()
