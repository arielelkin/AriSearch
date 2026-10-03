#!/usr/bin/env python3
"""Exact rank test for the two-charge Walton--Whittaker angle encoding.

Domain: 24 corner flags (proposed charge variant, one of six corners,
reflection parity)
and all 24^3 ordered vertex triples.  Arithmetic is rational/integer only.
"""

from fractions import Fraction
from itertools import product
import json

NEAR_START = (1, 1, 0, 1, 0, 0)
SIGN = (1, 1, 1, -1, -1, -1)
# -1 = counterclockwise only, 0 = both, +1 = clockwise only.
ORIENTATION = (-1, 0, 1, -1, 0, 1)


def boundaries(flag):
    """Return (side slot, central endpoint is side start) for left/right rays."""
    _flip, corner, reflected = flag
    if not reflected:
        return ((corner - 1) % 6, False), (corner, True)
    return (corner, True), ((corner - 1) % 6, False)


def edge_data(flag, ray):
    flip, _corner, reflected = flag
    side, at_start = boundaries(flag)[ray]
    near_central = NEAR_START[side] if at_start else 1 - NEAR_START[side]
    # This local sign-flipped variant is a construction hypothesis, not yet
    # certified as an independently selectable Walton--Whittaker source tile.
    charge = SIGN[side] * (-1 if flip else 1)
    orientation = ORIENTATION[side]
    if reflected:
        orientation = -orientation
    has_clockwise = orientation >= 0
    return near_central, charge, has_clockwise


def edge_compatible(left_flag, right_flag):
    a = edge_data(left_flag, 1)
    b = edge_data(right_flag, 0)
    r1 = a[0] == b[0]
    r2 = not (a[2] and b[2] and a[1] == b[1])
    return r1 and r2


def legal_triples():
    flags = tuple(product(range(2), range(6), range(2)))
    for triple in product(flags, repeat=3):
        if all(edge_compatible(triple[k], triple[(k + 1) % 3]) for k in range(3)):
            yield triple


def angle_row(triple):
    row = [0] * 12
    for flip, corner, _reflected in triple:
        row[6 * flip + corner] += 1
    return tuple(row)


def rank_and_basis(rows):
    matrix = []
    basis = []
    pivots = []
    for original in rows:
        row = [Fraction(x) for x in original]
        for reduced, pivot in zip(matrix, pivots):
            if row[pivot]:
                scale = row[pivot]
                row = [x - scale * y for x, y in zip(row, reduced)]
        pivot = next((i for i, x in enumerate(row) if x), None)
        if pivot is None:
            continue
        scale = row[pivot]
        row = [x / scale for x in row]
        matrix.append(row)
        pivots.append(pivot)
        basis.append(tuple(original))
    return len(pivots), basis, pivots


def main():
    triples = tuple(legal_triples())
    rows = {(1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1)}
    rows.update(angle_row(t) for t in triples)
    rank, basis, pivots = rank_and_basis(sorted(rows))
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

    flags = tuple(product(range(2), range(6), range(2)))
    compatible_flag_pairs = 0
    for left, right in product(flags, repeat=2):
        if edge_compatible(left, right):
            compatible_flag_pairs += 1
            left_side = boundaries(left)[1][0]
            right_side = boundaries(right)[0][0]
            union(6 * left[0] + left_side, 6 * right[0] + right_side)
    length_classes = []
    for root in sorted({find(i) for i in range(12)}):
        length_classes.append([i for i in range(12) if find(i) == root])
    forbidden_equal_length_pairs = 0
    for left, right in product(flags, repeat=2):
        left_side = boundaries(left)[1][0]
        right_side = boundaries(right)[0][0]
        if (find(6 * left[0] + left_side) == find(6 * right[0] + right_side)
                and not edge_compatible(left, right)):
            forbidden_equal_length_pairs += 1
    print(json.dumps({
        "corner_flags": 24,
        "ordered_triples_checked": 24 ** 3,
        "legal_ordered_triples": len(triples),
        "distinct_equation_rows": len(rows),
        "rank": rank,
        "nullity": 12 - rank,
        "pivots": pivots,
        "basis_rows": basis,
        "compatible_flag_pairs": compatible_flag_pairs,
        "forced_length_classes": length_classes,
        "forbidden_equal_length_flag_pairs": forbidden_equal_length_pairs,
    }, indent=2))


if __name__ == "__main__":
    main()
