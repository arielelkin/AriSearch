"""Independent exact two-endpoint obstruction for the P5/Q9 hub.

Run: mise exec -- conda run --no-capture-output -n arisearch python
     research/reviews/p5q9-hub-hostile-check-2026-10-20.py
"""
from sage.all import AA, CyclotomicField

K = CyclotomicField(30)
z = K.gen()
bar = lambda x: x.conjugate()
u = lambda d: z ** (d // 12)  # all polygon directions below are divisible by 12
A, B = u(144) + u(276), u(72) + u(216)
D = A * bar(B) - bar(A) * B
b, c = (B - bar(B)) / D, (bar(A) - A) / D


def polygon(lengths, dirs):
    v = [K(0)]
    for length, direction in zip(lengths, dirs):
        v.append(v[-1] + length * u(direction))
    assert v[-1] == 0
    return tuple(v[:-1])


P = polygon((1, c, b, c, b), (0, 72, 144, 216, 276))
Q = polygon((1, b, c) * 3, (0, 36, 96, 120, 156, 216, 240, 276, 336))


def map_edge(poly, i, start, finish, reflected):
    source = poly[(i + 1) % len(poly)] - poly[i]
    target = finish - start
    assert source * bar(source) == target * bar(target)
    scale = target / (bar(source) if reflected else source)
    return tuple(start + scale * (bar(x - poly[i]) if reflected else x - poly[i]) for x in poly)


def signed_projection(edge, point):
    # Positive multiple of cross(edge, point), with an AA order embedding.
    val = (bar(edge) * point - edge * bar(point)) / (z - bar(z))
    assert val == bar(val)
    return AA(val)


def overlap(X, Y):
    for poly in (X, Y):
        for i in range(len(poly)):
            edge = poly[(i + 1) % len(poly)] - poly[i]
            xx = [signed_projection(edge, p) for p in X]
            yy = [signed_projection(edge, p) for p in Y]
            if max(xx) <= min(yy) or max(yy) <= min(xx):
                return False
    return True


# Q's three unit sides get the only locally admissible P arm orientation:
# P vertex 0 (96 degrees) meets Q vertex 0, 3, or 6 (156 degrees).
arms = [map_edge(P, 0, Q[j], Q[(j + 1) % 9], True) for j in (0, 3, 6)]
hub = (Q, *arms)
assert all(not overlap(hub[i], hub[j]) for i in range(4) for j in range(i + 1, 4))


def cap_and_owner(qv, qother, arm, arm_vertex, arm_other):
    """Enumerate P108 full-edge caps independently from corner ray matching."""
    vertex = Q[qv]
    qray = Q[qother] - vertex
    pray = arm[arm_other] - vertex
    assert arm[arm_vertex] == vertex
    result = []
    for k in (2, 3):  # only corners with 108 degrees and lengths {b,c}
        for t in ((k - 1) % 5, (k + 1) % 5):
            source = P[t] - P[k]
            if source * bar(source) != qray * bar(qray):
                continue
            other_idx = (k + 1) % 5 if t == (k - 1) % 5 else (k - 1) % 5
            for reflected in (False, True):
                scale = qray / (bar(source) if reflected else source)
                other = P[other_idx] - P[k]
                mapped = scale * (bar(other) if reflected else other)
                if mapped != pray:
                    continue
                cap = tuple(vertex + scale * (bar(x - P[k]) if reflected else x - P[k]) for x in P)
                if any(overlap(cap, h) for h in hub):
                    continue
                owner = map_edge(Q, 0, cap[0], cap[1], not reflected)
                # Q's other two unit sides have Q156 at their initial vertex;
                # after gluing they are the identical unmarked polygon image.
                for qside in (3, 6):
                    alt = map_edge(Q, qside, cap[0], cap[1], not reflected)
                    assert set(alt) == set(owner)
                if (k, cap, owner) not in result:
                    result.append((k, cap, owner))
    return result


# Q vertex 1 is the far endpoint of side 0; Q vertex 3 is the near endpoint
# of side 3. Both must receive a cap in any edge-to-edge extension.
c1 = cap_and_owner(1, 2, arms[0], 1, 2)
c3 = cap_and_owner(3, 2, arms[1], 0, 4)
assert [k for k, _, _ in c1] == [2, 3]
assert [k for k, _, _ in c3] == [2, 3]

# At Q vertex 3, the vertex-2 cap's owner hits the original hub. For the
# vertex-3 cap, its cap/owner pair hits both possible pairs at Q vertex 1.
assert any(overlap(c3[0][2], h) and c3[0][2] != h for h in hub)
assert all(not any(overlap(c3[1][2], h) for h in hub) for _ in (0,))
for _, cap1, owner1 in c1:
    pair1 = (cap1, owner1)
    pair3 = (c3[1][1], c3[1][2])
    assert any(overlap(x, y) and x != y for x in pair1 for y in pair3)
print("CERTIFIED: both Q-vertex-3 cap choices are obstructed after compulsory Q ownership")
