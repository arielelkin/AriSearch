#!/usr/bin/env python3
"""Exact discrete verifier for the joint (5,6) restart language."""

from fractions import Fraction
from functools import reduce
from itertools import combinations_with_replacement, permutations, product
import json
from math import factorial

ANGLES = (22, 54, 22, 32, 50, 34, 37, 33, 49, 39, 48)
SIDE_CLASS = (0, 2, 0, 1, 2, 2, 3, 1, 4, 0, 1)
PI_UNITS = 60
P_DIRECTIONS = (0, 18, 132, 216, 246)
H_DIRECTIONS = (0, 69, 150, 183, 246, 282)


def adjacent_classes(corner):
    if corner < 5:
        return SIDE_CLASS[(corner - 1) % 5], SIDE_CLASS[corner]
    j = corner - 5
    return SIDE_CLASS[5 + (j - 1) % 6], SIDE_CLASS[5 + j]


def arrangements(row):
    found = set()
    for order in set(permutations(row)):
        for flips in product((0, 1), repeat=len(row)):
            rays = []
            for corner, flip in zip(order, flips):
                left, right = adjacent_classes(corner)
                rays.append((right, left) if flip else (left, right))
            if all(rays[i][1] == rays[(i + 1) % len(row)][0]
                   for i in range(len(row))):
                found.add((order, flips))
    return found


def interval_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def interval_neg(a):
    return -a[1], -a[0]


def interval_mul(a, b):
    values = [a[i] * b[j] for i in (0, 1) for j in (0, 1)]
    return min(values), max(values)


def sine_interval(degrees):
    degrees %= 360
    sign = 1
    if degrees > 180:
        degrees -= 180
        sign = -1
    if degrees > 90:
        degrees = 180 - degrees
    pi_lower, pi_upper = Fraction(333, 106), Fraction(355, 113)
    x_lower = Fraction(degrees, 180) * pi_lower
    x_upper = Fraction(degrees, 180) * pi_upper

    def partial(x, last):
        return sum(Fraction((-1) ** k, factorial(2 * k + 1)) * x ** (2 * k + 1)
                   for k in range(last + 1))
    result = partial(x_lower, 7), partial(x_upper, 8)
    return result if sign > 0 else interval_neg(result)


def determinant_interval(matrix):
    total = (Fraction(0), Fraction(0))
    for perm in permutations(range(len(matrix))):
        inversions = sum(perm[i] > perm[j] for i in range(len(perm))
                         for j in range(i + 1, len(perm)))
        term = (Fraction(1), Fraction(1))
        for i, j in enumerate(perm):
            term = interval_mul(term, matrix[i][j])
        total = interval_add(total, interval_neg(term) if inversions % 2 else term)
    return total


def closure_intervals():
    matrix = []
    for directions, offset in ((P_DIRECTIONS, 0), (H_DIRECTIONS, 5)):
        for trig in (lambda d: sine_interval(90 + d), sine_interval):
            matrix.append([
                reduce(interval_add,
                       (trig(directions[j]) for j in range(len(directions))
                        if SIDE_CLASS[offset + j] == side_class),
                       (Fraction(0), Fraction(0)))
                for side_class in range(5)
            ])
    coefficient = [row[:4] for row in matrix]
    rhs = [interval_neg(row[4]) for row in matrix]
    denominator = determinant_interval(coefficient)
    assert denominator[0] > 0
    result = []
    for column in range(4):
        replaced = [row[:] for row in coefficient]
        for i in range(4):
            replaced[i][column] = rhs[i]
        numerator = determinant_interval(replaced)
        quotients = [numerator[i] / denominator[j]
                     for i in (0, 1) for j in (0, 1)]
        result.append((min(quotients), max(quotients)))
    return denominator, result


def main():
    angle_rows = []
    for valence in range(3, 6):
        for row in combinations_with_replacement(range(11), valence):
            if sum(ANGLES[i] for i in row) == 2 * PI_UNITS:
                angle_rows.append(row)
    language = {row: arrangements(row) for row in angle_rows if arrangements(row)}
    expected = {
        (0, 4, 10), (1, 3, 5), (2, 4, 10), (3, 8, 9), (4, 6, 7),
        (0, 0, 0, 1), (0, 0, 1, 2), (0, 1, 2, 2), (1, 2, 2, 2),
    }
    assert set(language) == expected

    mixture = [
        ((1, 3, 5), (1, 0, 0), 4), ((1, 5, 3), (0, 1, 1), 2),
        ((10, 4, 2), (0, 0, 0), 4), ((4, 10, 2), (1, 1, 1), 2),
        ((9, 3, 8), (0, 0, 0), 4), ((3, 9, 8), (1, 1, 1), 2),
        ((7, 4, 6), (0, 0, 0), 4), ((7, 6, 4), (1, 1, 1), 2),
        ((0, 0, 0, 1), (0, 1, 0, 0), 4),
        ((2, 2, 2, 1), (0, 1, 0, 0), 2),
    ]
    flip_counts = [0] * 11
    row_counts = {}
    for order, flips, copies in mixture:
        canonical = tuple(sorted(order))
        assert (order, flips) in language[canonical]
        row_counts[canonical] = row_counts.get(canonical, 0) + copies
        for corner, flip in zip(order, flips):
            flip_counts[corner] += copies * flip
    assert flip_counts == [4] * 5 + [2] * 6
    assert row_counts == {
        (1, 3, 5): 6, (2, 4, 10): 6, (3, 8, 9): 6, (4, 6, 7): 6,
        (0, 0, 0, 1): 4, (1, 2, 2, 2): 2,
    }
    mono_p_corners = sorted({i for row in language if all(x < 5 for x in row)
                             for i in row})
    mono_h_rows = [row for row in language if all(x >= 5 for x in row)]
    assert mono_p_corners == [0, 1, 2]
    assert mono_h_rows == []
    closure_determinant, length_intervals = closure_intervals()
    coarse_intervals = ((Fraction(106, 10), Fraction(107, 10)),
                        (Fraction(79, 10), Fraction(8)),
                        (Fraction(53, 10), Fraction(54, 10)),
                        (Fraction(145, 10), Fraction(146, 10)))
    assert all(coarse[0] < exact[0] < exact[1] < coarse[1]
               for coarse, exact in zip(coarse_intervals, length_intervals))

    print(json.dumps({
        "angle_unit": "pi/60",
        "side_class_by_slot": SIDE_CLASS,
        "compatible_language": {
            str(len_): [list(row) for row in sorted(language) if len(row) == len_]
            for len_ in (3, 4, 5)
        },
        "compatible_arrangement_counts": {str(row): len(options)
                                            for row, options in language.items()},
        "chirality_flip_counts": flip_counts,
        "vertex_row_counts": {str(row): count for row, count in row_counts.items()},
        "pentagon_corners_in_mono_rows": mono_p_corners,
        "hexagon_only_rows": mono_h_rows,
        "closure_normalization": "L4=1",
        "closure_determinant_interval": [str(x) for x in closure_determinant],
        "closure_length_coarse_intervals": [[str(x) for x in interval]
                                             for interval in coarse_intervals] +
                                            [["1", "1"]],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
