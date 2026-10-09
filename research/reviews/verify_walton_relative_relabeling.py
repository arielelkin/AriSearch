#!/usr/bin/env python3
"""Independent verifier for the 24-case Walton relabeling certificate."""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path

near_word = (1, 1, 0, 1, 0, 0)
sign_word = (1, 1, 1, -1, -1, -1)
turn_word = (-1, 0, 1, -1, 0, 1)
flags = tuple(product((0, 1), range(6), (0, 1)))


def rays(flag):
    kind, corner, mirror = flag
    del kind
    if mirror:
        return (corner, True), ((corner - 1) % 6, False)
    return ((corner - 1) % 6, False), (corner, True)


def mark(flag, right, case):
    kind, _corner, mirror = flag
    side, begins = rays(flag)[right]
    if kind == 0:
        source, handed, charge = side, 1, 0
    else:
        shift, handed, charge = case
        source = (shift + handed * side) % 6
    near = near_word[source]
    orient = turn_word[source]
    if handed < 0:
        near, orient = 1 - near, -orient
    if not begins:
        near = 1 - near
    if mirror:
        orient = -orient
    return near, sign_word[source] * (-1 if charge else 1), orient >= 0


def legal(a, b, case):
    x, y = mark(a, True, case), mark(b, False, case)
    return x[0] == y[0] and not (x[2] and y[2] and x[1] == y[1])


def rational_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    for column in range(12):
        pivot = next((i for i in range(rank, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][column]
        a[rank] = [x / scale for x in a[rank]]
        for i in range(rank + 1, len(a)):
            if a[i][column]:
                scale = a[i][column]
                a[i] = [x - scale * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


certificate = json.loads((Path(__file__).resolve().parents[1] / "certificates" /
    "walton_relative_relabeling_rank_certificate.json").read_text())
assert certificate["relative_choices"] == 24
expected = {(r["shift"], r["chirality"], r["charge_flip"]): r
            for r in certificate["results"]}
assert len(expected) == 24

for case in product(range(6), (1, -1), range(2)):
    pairs = {(a, b) for a, b in product(flags, repeat=2) if legal(a, b, case)}
    rows = {(1,) * 6 + (0,) * 6, (0,) * 6 + (1,) * 6}
    count = 0
    parent = list(range(12))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in pairs:
        x = 6 * a[0] + rays(a)[1][0]
        y = 6 * b[0] + rays(b)[0][0]
        x, y = root(x), root(y)
        if x != y:
            parent[y] = x
    for triple in product(flags, repeat=3):
        if all((triple[i], triple[(i + 1) % 3]) in pairs for i in range(3)):
            count += 1
            row = [0] * 12
            for kind, corner, _mirror in triple:
                row[6 * kind + corner] += 1
            rows.add(tuple(row))
    classes = [[i for i in range(12) if root(i) == r]
               for r in sorted({root(i) for i in range(12)})]
    record = expected[case]
    assert len(pairs) == record["compatible_ordered_flag_pairs"] == 240
    assert count == record["legal_ordered_triples"] == 1056
    assert len(rows) == record["distinct_angle_rows_including_sums"]
    assert rational_rank(rows) == record["angle_rank"] == 12
    assert classes == record["forced_length_classes"] == [list(range(12))]

print("verified all 24 Walton relative relabelings")
