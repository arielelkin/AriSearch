"""Independent finite-window audit of three equiangular-hexagon trials."""

from collections import Counter, deque

E = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
PAIRS = (
    ((1, 4, 2, 3, 2, 4), (2, 4, 4, 3, 3, 5)),
    ((1, 4, 3, 2, 3, 4), (2, 4, 4, 3, 3, 5)),
    ((1, 2, 3, 2, 1, 4), (1, 3, 3, 2, 2, 4)),
)
STATES = {(0, 0): (1, 4, 1), (1, 0): (0, 5, -1),
          (0, 1): (1, 1, 1), (1, 1): (0, 2, -1)}


def plus(p, q):
    return p[0] + q[0], p[1] + q[1]


def minus(p, q):
    return p[0] - q[0], p[1] - q[1]


def verts(w):
    p = (0, 0)
    out = []
    for length, direction in zip(w, E):
        out.append(p)
        p = plus(p, (length * direction[0], length * direction[1]))
    assert p == (0, 0)
    # Euclidean cross products have the sign of triangular-coordinate ones.
    for i in range(6):
        a, b, c = out[i], out[(i + 1) % 6], out[(i + 2) % 6]
        u, v = minus(b, a), minus(c, b)
        assert u[0] * v[1] - u[1] * v[0] > 0
    return out


def corner_mult(w):
    return Counter(tuple(sorted((w[j - 1], w[j]))) for j in range(6))


for a, b in PAIRS:
    for w in (a, b):
        verts(w)
        assert w[0] - w[3] == w[2] - w[5] == w[4] - w[1] < 0

a, b = PAIRS[0]
ca, cb = corner_mult(a), corner_mult(b)
assert ca[(4, 4)] == 0 and cb[(4, 4)] == 1
assert ca[(2, 2)] == cb[(2, 2)] == 0
assert a[1] == a[5] == 4 and a[2] == a[4] == 2
assert sorted((b[0], b[3])) == [2, 3]
assert ca[(2, 3)] == 2 and cb[(2, 3)] == 0

# Across a private 5 seam, endpoint demands are either 2,3 at both
# vertices (half-turn) or 2,2 and 3,3 (mirror). B has neither 2,3 nor 2,2.
assert b[5] == 5 and b[4] == 3 and b[0] == 2
assert cb[(2, 3)] == cb[(2, 2)] == 0

a, b = PAIRS[2]
ca, cb = corner_mult(a), corner_mult(b)
shared = set(ca) | set(cb)
third = {x for x in set(a) | set(b)
         if tuple(sorted((1, x))) in shared
         and tuple(sorted((4, x))) in shared}
assert third == {2}
assert (ca[(1, 4)], ca[(1, 2)], ca[(2, 4)]) == (2, 2, 0)
assert (cb[(1, 4)], cb[(1, 2)], cb[(2, 4)]) == (1, 0, 1)


def state(z):
    x, y = z
    q, rem = divmod(y, 2)
    return STATES[((x - q) % 2, rem)]


def local(z):
    which, r, parity = state(z)
    return verts(tuple(PAIRS[1][which][(r + parity * k) % 6]
                       for k in range(6)))


# Develop translations by BFS through all six neighbors.  This checks
# every edge identification and every finite-window cycle, independently
# of the producer's selected rhombus checks.
domain = {(x, y) for x in range(-8, 9) for y in range(-8, 9)}
origins = {(0, 0): (0, 0)}
todo = deque([(0, 0)])
seams = 0
while todo:
    z = todo.popleft()
    p = local(z)
    for k, u in enumerate(E):
        nxt = plus(z, u)
        if nxt not in domain:
            continue
        q = local(nxt)
        # Same geometric seam runs p[k] -> p[k+1] and q[k+4] -> q[k+3].
        assert minus(p[(k + 1) % 6], p[k]) == minus(q[(k + 3) % 6], q[(k + 4) % 6])
        target = plus(origins[z], minus(p[k], q[(k + 4) % 6]))
        if nxt in origins:
            assert origins[nxt] == target
        else:
            origins[nxt] = target
            todo.append(nxt)
        seams += 1
assert len(origins) == len(domain)
periods = (origins[(2, 0)], origins[(1, 2)])
assert periods == ((4, -12), (13, -10)), periods
assert periods[0][0] * periods[1][1] - periods[0][1] * periods[1][0] == 116
for z in domain:
    for shift, p in zip(((2, 0), (1, 2)), periods):
        zz = plus(z, shift)
        if zz in domain:
            assert state(z) == state(zz)
            assert minus(origins[zz], origins[z]) == p

print("PASS closure/strict convexity for all six words")
print("PASS trial 1 corner inventory and forced missing caps")
print("PASS trial 3 unique third label and corner inventory")
print(f"PASS trial 2 finite development: {len(origins)} faces, {seams} seams")
print("periods", periods, "determinant 116")
