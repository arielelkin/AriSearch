"""Independent exact audit of the Y pair's shortest-side contact gates.

No author module or certificate is imported. This checks the coordinate
inventory, all possible pi-complement corner multisets, and the exact length
inequalities used by the one-breakpoint and contained-edge arguments.
"""

from itertools import combinations_with_replacement
from sympy import sqrt


P = ((0, 0), (2, 0), (3, 2), (2, 3), (0, 2))
Q = ((2, 3), (1, 4), (-1, 4), (-2, 3), (0, 2))
LABELS = {"P": "r a b b a".split(), "Q": "c g g c d".split()}
ANGLES = {"r": (2, 0), "a": (4, -1), "b": (1, 1),
          "c": (3, -1), "g": (3, 0), "d": (0, 2)}


def lengths_squared(poly):
    return tuple((poly[(i + 1) % len(poly)][0] - v[0]) ** 2 +
                 (poly[(i + 1) % len(poly)][1] - v[1]) ** 2
                 for i, v in enumerate(poly))


assert lengths_squared(P) == (4, 5, 2, 5, 4)
assert lengths_squared(Q) == (2, 4, 2, 5, 5)

# Angles are in the exact formal basis (pi/4, theta), theta=atan(2).
flat_complements = []
for n in (1, 2, 3):  # theta>pi/3 makes four positive corners impossible.
    for word in combinations_with_replacement(ANGLES, n):
        if tuple(sum(ANGLES[x][i] for x in word) for i in range(2)) == (4, 0):
            flat_complements.append("".join(word))
assert sorted(flat_complements) == ["bc", "rr"]

s, q = sqrt(2), sqrt(5)
assert 2 * 2 != 3 * s      # rr breakpoint endpoint equations
assert 2 * q != 3 * s      # bc breakpoint, both long arms
assert q - s > 0
assert q - s < s           # contained-edge repair: host A inside forced P side
assert 2 * s > q           # no native edge can overhang both ends in critical case

# Native side profiles as unordered endpoint labels; reflection is included.
edges = []
for name, poly in (("P", P), ("Q", Q)):
    labels = LABELS[name]
    for i, length2 in enumerate(lengths_squared(poly)):
        edges.append((name, tuple(sorted((labels[i], labels[(i+1) % len(poly)]))), length2))
assert sorted((a, b, v) for a, b, v in edges if v == 2) == [
    ("P", ("b", "b"), 2), ("Q", ("c", "g"), 2), ("Q", ("c", "g"), 2)]
assert {v for _, _, v in edges} == {2, 4, 5}
assert sorted((name, ends, v) for name, ends, v in edges if v > 2) == [
    ("P", ("a", "b"), 5), ("P", ("a", "b"), 5),
    ("P", ("a", "r"), 4), ("P", ("a", "r"), 4),
    ("Q", ("c", "d"), 5), ("Q", ("c", "d"), 5),
    ("Q", ("g", "g"), 4)]

# At a flush B+D end, the residual has a theta coefficient absent from
# every individual corner, and its size is below two minimum c corners.
bd_residual = tuple((8, 0)[i] - ANGLES["b"][i] - ANGLES["d"][i]
                    for i in range(2))
assert bd_residual == (7, -3)
assert bd_residual not in ANGLES.values()
assert sum(ANGLES[x][0] for x in ("a", "b", "g")) == 8
assert sum(ANGLES[x][1] for x in ("a", "b", "g")) == 0

print("PASS: exact native edges, flat stars, and BB endpoint length gates")
