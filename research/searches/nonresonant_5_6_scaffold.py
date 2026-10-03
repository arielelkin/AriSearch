#!/usr/bin/env python3
"""Verify an exact rational-angle (5,6) incidence scaffold.

Angles are integer multiples of pi/60.  This verifies only angle sums,
nonresonance, labeled-corner marginals, and curvature accounting; it does not
claim a globally extendible tiling or aperiodicity.
"""

from fractions import Fraction
from itertools import combinations_with_replacement
from itertools import product
import json
from math import factorial

PENTAGON = (22, 54, 22, 32, 50)
HEXAGON = (34, 37, 33, 49, 39, 48)
ANGLES = PENTAGON + HEXAGON
PI_UNITS = 60

# Sparse nonnegative incidence certificate, with hexagon marginal normalized
# to one and pentagon marginal two.
WEIGHTS = {
    (1, 3, 5): Fraction(1),
    (2, 4, 10): Fraction(1),
    (3, 8, 9): Fraction(1),
    (4, 6, 7): Fraction(1),
    (0, 0, 0, 1): Fraction(2, 3),
    (1, 2, 2, 2): Fraction(1, 3),
}

# Adjacent side-length symbols at corners 0,...,10 for the closure formulas
# in the report.  u is the common unit length; a,b are the other pentagon
# lengths and c,d the other hexagon lengths.
CORNER_LENGTH_PAIRS = (
    ("u", "u"), ("u", "a"), ("a", "b"), ("b", "u"), ("u", "u"),
    ("u", "c"), ("c", "d"), ("d", "u"), ("u", "u"), ("u", "u"),
    ("u", "u"),
)


def cyclic_length_compatible(row, labels):
    """Whether corner side-pairs can form one cyclic full-edge star."""
    degree = {}
    adjacency = {}
    for corner in row:
        x, y = (labels[s] for s in CORNER_LENGTH_PAIRS[corner])
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
        adjacency.setdefault(x, set()).add(y)
        adjacency.setdefault(y, set()).add(x)
    if any(value % 2 for value in degree.values()):
        return False
    seen, stack = set(), [next(iter(degree))]
    while stack:
        x = stack.pop()
        if x not in seen:
            seen.add(x)
            stack.extend(adjacency[x] - seen)
    return seen == set(degree)


def sine_interval(degrees):
    """Rigorous rational sine bounds on [0,180] via alternating Taylor sums."""
    if degrees > 90:
        degrees = 180 - degrees
    pi_lower, pi_upper = Fraction(333, 106), Fraction(355, 113)
    x_lower = Fraction(degrees, 180) * pi_lower
    x_upper = Fraction(degrees, 180) * pi_upper

    def partial(x, last):
        return sum(Fraction((-1) ** k, factorial(2 * k + 1)) * x ** (2 * k + 1)
                   for k in range(last + 1))
    # On [0,pi/2], ending at the negative x^15 term is a lower bound and
    # ending at the positive x^17 term is an upper bound.
    return partial(x_lower, 7), partial(x_upper, 8)


def interval_add(*values):
    return sum(x[0] for x in values), sum(x[1] for x in values)


def interval_neg(value):
    return -value[1], -value[0]


def interval_div(numerator, denominator):
    assert denominator[0] > 0
    return numerator[0] / denominator[1], numerator[1] / denominator[0]


def main():
    assert sum(PENTAGON) == 3 * PI_UNITS
    assert sum(HEXAGON) == 4 * PI_UNITS
    max_halfplane_terms = PI_UNITS // min(ANGLES)
    pi_sums = []
    for size in range(1, max_halfplane_terms + 1):
        for row in combinations_with_replacement(range(11), size):
            if sum(ANGLES[i] for i in row) == PI_UNITS:
                pi_sums.append(row)
    assert not pi_sums

    # Every one of the fifteen currently known pentagon families fails an
    # angle condition before side equalities are considered (under every
    # cyclic/reflected labeling).  Types 1,2,6 require a three-angle 2pi
    # sum; Types 3,5 require 120-degree data (Type 5 also 60); Types 4 and
    # 10--15 require a 90-degree angle; Types 7--9 require 2x+y=2pi.
    pentagon_three_angle_sums = [row for row in combinations_with_replacement(
        range(5), 3) if len(set(row)) == 3
        and sum(PENTAGON[i] for i in row) == 2 * PI_UNITS]
    pentagon_double_plus_one = [(i, j) for i in range(5) for j in range(5)
                                if 2 * PENTAGON[i] + PENTAGON[j]
                                == 2 * PI_UNITS]
    assert not pentagon_three_angle_sums
    assert not pentagon_double_plus_one
    assert 30 not in PENTAGON and 40 not in PENTAGON

    legal_vertices = []
    for size in range(3, 6):
        for row in combinations_with_replacement(range(11), size):
            if sum(ANGLES[i] for i in row) == 2 * PI_UNITS:
                legal_vertices.append(row)
    assert all(row in legal_vertices for row in WEIGHTS)
    pentagon_only_vertices = [row for row in legal_vertices
                              if all(i < 5 for i in row)]
    pentagon_corners_in_mono_vertices = sorted({i for row in pentagon_only_vertices
                                                for i in row})
    assert 4 not in pentagon_corners_in_mono_vertices

    marginals = []
    for corner in range(11):
        marginals.append(sum(weight * row.count(corner)
                             for row, weight in WEIGHTS.items()))
    assert marginals == [Fraction(2)] * 5 + [Fraction(1)] * 6

    valence_counts = {
        size: sum(weight for row, weight in WEIGHTS.items() if len(row) == size)
        for size in (3, 4, 5)
    }
    assert valence_counts == {3: Fraction(4), 4: Fraction(1), 5: Fraction(0)}
    excess = sum(Fraction(size - 3) * count
                 for size, count in valence_counts.items())
    assert 2 * excess == 2  # pentagon marginal

    # Exhaust all 52 set partitions of the five symbolic length values.
    # A cyclic full-edge vertex exists exactly when its corner length-pairs
    # form a connected Eulerian multigraph after applying the equalities.
    compatible_partitions = []
    symbols = "uabcd"
    for partition in product(range(5), repeat=5):
        if partition[0] != 0:
            continue
        if any(partition[i] > 1 + max(partition[:i]) for i in range(1, 5)):
            continue
        labels = dict(zip(symbols, partition))
        if all(cyclic_length_compatible(row, labels) for row in WEIGHTS):
            compatible_partitions.append(partition)
    assert compatible_partitions == [(0, 0, 0, 0, 0), (0, 0, 0, 0, 1)]
    distinct_labels = dict(zip(symbols, range(5)))
    length_compatible_vertices = [
        row for row in legal_vertices
        if cyclic_length_compatible(row, distinct_labels)
    ]
    covered_corners = sorted({i for row in length_compatible_vertices for i in row})
    assert length_compatible_vertices == [(0, 4, 10), (0, 8, 8)]
    assert covered_corners == [0, 4, 8, 10]

    # Certify that the five length symbols used in the exact closure are
    # genuinely distinct, without floating-point comparisons.
    sin = sine_interval
    length_intervals = {
        "a": interval_div(interval_add(sin(84), sin(114), interval_neg(sin(132))),
                          sin(114)),
        "b": interval_div(interval_add(sin(18), sin(18), sin(48)), sin(114)),
        "c": interval_div(interval_add(sin(81), sin(114), sin(177),
                                        interval_neg(sin(147))), sin(69)),
        "d": interval_div(interval_add(sin(3), sin(66), sin(78),
                                        interval_neg(sin(150))), sin(69)),
    }
    coarse = {"a": (Fraction(1275, 1000), Fraction(1276, 1000)),
              "b": (Fraction(1489, 1000), Fraction(1491, 1000)),
              "c": (Fraction(1509, 1000), Fraction(1510, 1000)),
              "d": (Fraction(1546, 1000), Fraction(1548, 1000))}
    assert all(coarse[key][0] < value[0] < value[1] < coarse[key][1]
               for key, value in length_intervals.items())

    print(json.dumps({
        "angle_unit": "pi/60",
        "pentagon_angles": PENTAGON,
        "hexagon_angles": HEXAGON,
        "halfplane_sum_search_max_terms": max_halfplane_terms,
        "halfplane_angle_sums": pi_sums,
        "known_pentagon_family_angle_gate": {
            "distinct_three_angle_2pi_sums": pentagon_three_angle_sums,
            "double_plus_one_2pi_sums": pentagon_double_plus_one,
            "has_90_degree_angle": 30 in PENTAGON,
            "has_120_degree_angle": 40 in PENTAGON,
        },
        "all_vertex_sums_by_valence": {
            str(size): [row for row in legal_vertices if len(row) == size]
            for size in (3, 4, 5)
        },
        "pentagon_only_vertex_sums": pentagon_only_vertices,
        "pentagon_corners_in_monohedral_vertex_sums":
            pentagon_corners_in_mono_vertices,
        "certificate_weights": {str(row): str(weight)
                                for row, weight in WEIGHTS.items()},
        "corner_marginals": [str(x) for x in marginals],
        "valence_counts": {str(k): str(v) for k, v in valence_counts.items()},
        "excess_valence": str(excess),
        "selected_star_length_symbols": list(symbols),
        "selected_star_compatible_length_partitions": compatible_partitions,
        "selected_stars_force_all_pentagon_sides_equal": True,
        "distinct_length_compatible_vertex_sums": length_compatible_vertices,
        "corners_covered_by_distinct_length_vertices": covered_corners,
        "certified_coarse_length_intervals": {
            key: [str(bound) for bound in bounds] for key, bounds in coarse.items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()
