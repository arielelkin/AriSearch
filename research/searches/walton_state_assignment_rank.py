#!/usr/bin/env python3
"""Exhaust two-type assignments of Walton orientation/reflection states.

This is a deliberately narrow follow-up to ``walton_vertex_rank.py``.  A
source state is (rotation modulo six, reflection parity).  Each of its twelve
values is assigned geometric type 0 or 1.  For every nonconstant assignment
we retain all source-legal trivalent vertices that the assignment realizes,
and compute the rank of their angle equations together with the two polygon
angle-sum equations.  Arithmetic is over the rationals after a modular
screen; the finite domain has 2^12-2 assignments.
"""

from fractions import Fraction
from itertools import product
import json

from walton_vertex_rank import legal_triples


PATTERNS = ((0, 2, 4), (1, 3, 5))


def source_state(flag, source_corner):
    """Invert placement of a source state into (type, geometric corner, flip)."""
    tile_type, corner, reflected_placement = flag
    rotation = ((source_corner - corner) if not reflected_placement
                else (source_corner + corner)) % 6
    source_reflection = tile_type ^ reflected_placement
    return rotation + 6 * source_reflection


def rank(rows, modulus=None):
    matrix = [list(row) for row in set(rows)]
    result = 0
    for column in range(12):
        pivot = next((i for i in range(result, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[result], matrix[pivot] = matrix[pivot], matrix[result]
        scale = matrix[result][column]
        if modulus:
            inverse = pow(scale % modulus, modulus - 2, modulus)
            matrix[result] = [(x * inverse) % modulus for x in matrix[result]]
        else:
            matrix[result] = [Fraction(x, scale) for x in matrix[result]]
        for i in range(result + 1, len(matrix)):
            if matrix[i][column]:
                scale = matrix[i][column]
                matrix[i] = [x - scale * y
                             for x, y in zip(matrix[i], matrix[result])]
                if modulus:
                    matrix[i] = [x % modulus for x in matrix[i]]
        result += 1
    return result


def main():
    # Each realization gives a partial Boolean assignment and one angle row.
    realizations = []
    for triple in legal_triples():
        row = [0] * 12
        for tile_type, corner, _reflected in triple:
            row[6 * tile_type + corner] += 1
        for corners in PATTERNS:
            required = {}
            for flag, source_corner in zip(triple, corners):
                state = source_state(flag, source_corner)
                tile_type = flag[0]
                if state in required and required[state] != tile_type:
                    break
                required[state] = tile_type
            else:
                ones = sum(1 << state for state, value in required.items() if value)
                fixed = sum(1 << state for state in required)
                realizations.append((fixed, ones, tuple(row)))

    sum_rows = ((1,) * 6 + (0,) * 6, (0,) * 6 + (1,) * 6)
    histogram = {}
    minimum = 12
    minimizers = []
    for mask in range(1, (1 << 12) - 1):
        rows = set(sum_rows)
        occurrences = 0
        for fixed, ones, row in realizations:
            if mask & fixed == ones:
                rows.add(row)
                occurrences += 1
        value = rank(rows, 1_000_003)
        histogram[value] = histogram.get(value, 0) + 1
        record = {"mask": mask, "distinct_rows": len(rows) - 2,
                  "realizations": occurrences}
        if value < minimum:
            minimum, minimizers = value, [record]
        elif value == minimum:
            minimizers.append(record)
    # A modular rank is a lower bound for rational rank.  Recheck every
    # modular minimizer exactly; equality certifies the reported minimum.
    exact_minimum = min(rank(set(sum_rows) | {
        row for fixed, ones, row in realizations if item["mask"] & fixed == ones
    }) for item in minimizers)
    assert exact_minimum == minimum

    # For each exceptional assignment, compute side-slot equivalence generated
    # by every edge occurring in a retained vertex.  This is intentionally
    # repeated rather than inferred from angle rows.
    for item in minimizers:
        mask = item["mask"]
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

        retained = set()
        for triple in legal_triples():
            for corners in PATTERNS:
                required = {}
                for flag, source_corner in zip(triple, corners):
                    state = source_state(flag, source_corner)
                    if state in required and required[state] != flag[0]:
                        break
                    required[state] = flag[0]
                else:
                    if all(((mask >> state) & 1) == value
                           for state, value in required.items()):
                        retained.add(triple)
                        break
        # Boundary formulas duplicated here to keep this extension explicit.
        def right_side(flag):
            _tile_type, corner, reflected = flag
            return (corner - 1) % 6 if reflected else corner

        def left_side(flag):
            _tile_type, corner, reflected = flag
            return corner if reflected else (corner - 1) % 6

        for triple in retained:
            for i in range(3):
                a, b = triple[i], triple[(i + 1) % 3]
                union(6 * a[0] + right_side(a),
                      6 * b[0] + left_side(b))
        item["retained_ordered_triples"] = len(retained)
        item["forced_length_classes"] = [
            [i for i in range(12) if find(i) == root]
            for root in sorted({find(i) for i in range(12)})
        ]
    print(json.dumps({
        "source_states": 12,
        "nonconstant_assignments": (1 << 12) - 2,
        "source_legal_ordered_triples": 1056,
        "corner_patterns": [list(x) for x in PATTERNS],
        "consistent_realizations": len(realizations),
        "rank_histogram": histogram,
        "minimum_rank": minimum,
        "minimum_rank_exactly_rechecked": exact_minimum,
        "minimum_nullity": 12 - minimum,
        "minimizers": minimizers,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
