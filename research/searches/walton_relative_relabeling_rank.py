#!/usr/bin/env python3
"""Exhaust relative dihedral relabelings of two Walton decorated hexagons.

Type 0 carries the published decoration in the reference slot order.  Type 1
carries any of its twelve dihedral relabelings and may independently reverse
all charges.  For each of the 24 relative choices, enumerate all geometric
placement flags and all source-legal trivalent vertices, then compute exact
angle rank and forced side-length classes.
"""

from fractions import Fraction
from itertools import product
import json

NEAR_START = (1, 1, 0, 1, 0, 0)
SIGN = (1, 1, 1, -1, -1, -1)
ORIENTATION = (-1, 0, 1, -1, 0, 1)  # CCW, both, CW


def boundaries(flag):
    _tile_type, corner, reflected = flag
    if not reflected:
        return ((corner - 1) % 6, False), (corner, True)
    return (corner, True), ((corner - 1) % 6, False)


def decoration(tile_type, physical_side, relative):
    """Return near-physical-start, sign, orientation in unreflected placement."""
    if tile_type == 0:
        source_side, chirality, charge_flip = physical_side, 1, 0
    else:
        shift, chirality, charge_flip = relative
        source_side = (shift + chirality * physical_side) % 6
    near = NEAR_START[source_side]
    orientation = ORIENTATION[source_side]
    if chirality == -1:
        near = 1 - near
        orientation = -orientation
    sign = SIGN[source_side] * (-1 if charge_flip else 1)
    return near, sign, orientation


def edge_data(flag, ray, relative):
    tile_type, _corner, reflected = flag
    side, at_start = boundaries(flag)[ray]
    near_start, sign, orientation = decoration(tile_type, side, relative)
    near_central = near_start if at_start else 1 - near_start
    if reflected:
        orientation = -orientation
    return near_central, sign, orientation >= 0


def compatible(a, b, relative):
    x, y = edge_data(a, 1, relative), edge_data(b, 0, relative)
    return x[0] == y[0] and not (x[2] and y[2] and x[1] == y[1])


def rank(rows):
    a = [[Fraction(x) for x in row] for row in set(rows)]
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


def main():
    flags = tuple(product(range(2), range(6), range(2)))
    results = []
    for shift, chirality, charge_flip in product(range(6), (1, -1), range(2)):
        relative = shift, chirality, charge_flip
        pairs = {(a, b) for a, b in product(flags, repeat=2)
                 if compatible(a, b, relative)}
        rows = {(1,) * 6 + (0,) * 6, (0,) * 6 + (1,) * 6}
        triples = 0
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

        for a, b in pairs:
            union(6 * a[0] + boundaries(a)[1][0],
                  6 * b[0] + boundaries(b)[0][0])
        for triple in product(flags, repeat=3):
            if all((triple[i], triple[(i + 1) % 3]) in pairs for i in range(3)):
                triples += 1
                row = [0] * 12
                for tile_type, corner, _reflected in triple:
                    row[6 * tile_type + corner] += 1
                rows.add(tuple(row))
        results.append({
            "shift": shift, "chirality": chirality,
            "charge_flip": charge_flip,
            "compatible_ordered_flag_pairs": len(pairs),
            "legal_ordered_triples": triples,
            "distinct_angle_rows_including_sums": len(rows),
            "angle_rank": rank(rows),
            "forced_length_classes": [
                [i for i in range(12) if find(i) == root]
                for root in sorted({find(i) for i in range(12)})
            ],
        })
    print(json.dumps({"relative_choices": 24, "results": results},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
