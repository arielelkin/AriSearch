#!/usr/bin/env python3
"""Small verifier for walton_vertex_rank_certificate.json."""

from fractions import Fraction
import json
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(12):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


data = json.loads(Path(__file__).with_name("walton_vertex_rank_certificate.json").read_text())
rows = data["basis_rows"]
assert len(rows) == 12
assert all(len(row) == 12 and all(isinstance(x, int) and 0 <= x <= 6 for x in row)
           for row in rows)
assert rank(rows) == 12
# Independently reconstruct the conditional local language and ensure every
# certified row really occurs (or is a per-hexagon angle-sum row).
near_start = (1, 1, 0, 1, 0, 0)
sign = (1, 1, 1, -1, -1, -1)
orientation = (-1, 0, 1, -1, 0, 1)

def boundary(flag, right):
    _variant, corner, reflected = flag
    if not reflected:
        return (corner, True) if right else ((corner - 1) % 6, False)
    return ((corner - 1) % 6, False) if right else (corner, True)

def datum(flag, right):
    variant, _corner, reflected = flag
    side, at_start = boundary(flag, right)
    near_central = near_start[side] if at_start else 1 - near_start[side]
    orient = -orientation[side] if reflected else orientation[side]
    return near_central, sign[side] * (-1 if variant else 1), orient >= 0

def compatible(a, b):
    x, y = datum(a, True), datum(b, False)
    return x[0] == y[0] and not (x[2] and y[2] and x[1] == y[1])

from itertools import product
flags = tuple(product(range(2), range(6), range(2)))
legal_rows = set()
legal_count = 0
for triple in product(flags, repeat=3):
    if all(compatible(triple[k], triple[(k + 1) % 3]) for k in range(3)):
        legal_count += 1
        row = [0] * 12
        for variant, corner, _reflected in triple:
            row[6 * variant + corner] += 1
        legal_rows.add(tuple(row))
sum_rows = {(1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1)}
assert all(tuple(row) in legal_rows | sum_rows for row in rows)
assert legal_count == 1056
assert data["ordered_triples_checked"] == 24 ** 3
assert data["legal_ordered_triples"] == 1056
assert data["rank"] == 12 and data["nullity"] == 0
parent = list(range(12))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
pair_count = 0
for a, b in product(flags, repeat=2):
    if compatible(a, b):
        pair_count += 1
        sa, sb = boundary(a, True)[0], boundary(b, False)[0]
        union(6 * a[0] + sa, 6 * b[0] + sb)
classes = [[i for i in range(12) if find(i) == root]
           for root in sorted({find(i) for i in range(12)})]
forbidden = 0
for a, b in product(flags, repeat=2):
    sa, sb = boundary(a, True)[0], boundary(b, False)[0]
    if find(6 * a[0] + sa) == find(6 * b[0] + sb) and not compatible(a, b):
        forbidden += 1
assert pair_count == data["compatible_flag_pairs"] == 240
assert classes == data["forced_length_classes"] == [list(range(12))]
assert forbidden == data["forbidden_equal_length_flag_pairs"] == 336
print("verified rank-12 Walton vertex-angle certificate")
