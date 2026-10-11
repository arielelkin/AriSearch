#!/usr/bin/env python3
"""Exact necessary boundary test for an ETE unit Robinson-triangle patch.

No triangle placement or Penrose-marking claim is made.  The integer length
coefficients use the independent basis (1, phi), phi^2=phi+1.
"""
import argparse
import json
from collections import Counter
from itertools import product
from pathlib import Path

LENGTHS = {"u": (1, 0), "l": (0, 1), "s": (-1, 1)}
CORNERS = [
    ("thin36", "u", "u", 1),
    ("thin72", "u", "s", 2),
    ("fat108", "u", "u", 3),
    ("fat36", "u", "l", 1),
]


def fans(start, end, budget):
    """All labeled open walks of total angle budget*pi/5 (mirrors allowed)."""
    out = []

    def visit(current, left, walk):
        if left == 0:
            if current == end:
                out.append(walk)
            return
        for name, a, b, weight in CORNERS:
            if weight > left:
                continue
            if current == a:
                visit(b, left-weight, walk+[(name, a, b, weight)])
            if a != b and current == b:
                visit(a, left-weight, walk+[(name, b, a, weight)])

    visit(start, budget, [])
    return out


def words(a, b):
    """All ordered positive-edge words summing exactly a+b*phi."""
    out = []
    for ns in range(b+1):
        counts = {"u": a+ns, "l": b-ns, "s": ns}
        if min(counts.values()) < 0:
            continue

        def extend(prefix):
            if not any(counts.values()):
                out.append(tuple(prefix))
                return
            for symbol in ("u", "l", "s"):
                if counts[symbol]:
                    counts[symbol] -= 1
                    extend(prefix+[symbol])
                    counts[symbol] += 1

        extend([])
    assert len(out) == len(set(out))
    for word in out:
        assert tuple(sum(LENGTHS[s][i] for s in word) for i in (0, 1)) == (a, b)
    return out


def certificate():
    table = {(a, b, angle): fans(a, b, angle)
             for a, b, angle in product(LENGTHS, LENGTHS, range(1, 6))}
    records = {}
    fixtures = {
        "U": ([(1, 2), (1, 2), (1, 0), (1, 0), (1, 0)], [1, 3, 4, 4, 3]),
        "V": ([(1, 0), (1, 3), (1, 0), (0, 2), (0, 2)], [2, 2, 4, 3, 4]),
    }
    for name, (lengths, angles) in fixtures.items():
        side_words = [words(*length) for length in lengths]
        choices = 0
        passing = 0
        passing_euler = 0
        first = None
        first_euler = None
        triangle_count = 16 if name == "U" else 25
        for boundary in product(*side_words):
            choices += 1
            tests = []
            for i, word in enumerate(boundary):
                tests.extend((word[j], word[j+1], 5)
                             for j in range(len(word)-1))
                tests.append((word[-1], boundary[(i+1) % 5][0], angles[i]))
            if not all(table[t] for t in tests):
                continue
            passing += 1
            edge_count = sum(map(len, boundary))
            euler_passes = (triangle_count-edge_count+2) % 2 == 0
            if euler_passes:
                passing_euler += 1
            if first is None or (euler_passes and first_euler is None):
                chosen = [min(table[t], key=lambda w: (len(w), w)) for t in tests]
                demand = Counter(corner[0] for fan in chosen for corner in fan)
                thin, fat = (7, 9) if name == "U" else (9, 16)
                available = {"thin36": thin, "thin72": 2*thin,
                             "fat108": fat, "fat36": 2*fat}
                assert all(demand[k] <= available[k] for k in demand)
                witness = {"side_words": [list(w) for w in boundary],
                         "boundary_fans_in_side_order": [
                             {"from": a, "to": b, "angle_pi_over_5": angle,
                              "corners": fan}
                             for (a, b, angle), fan in zip(tests, chosen)],
                         "witness_native_corner_demand": dict(demand),
                         "available_native_corners": available,
                         "witness_fits_native_corner_counts": True,
                         "total_boundary_edge_count": edge_count,
                         "disk_euler_parity_passes": euler_passes}
                if first is None:
                    first = witness
                if euler_passes and first_euler is None:
                    witness["required_interior_vertex_count"] = (triangle_count-edge_count+2)//2
                    first_euler = witness
        records[name] = {"side_lengths_in_basis_1_phi": lengths,
                         "angle_after_side_pi_over_5": angles,
                         "ordered_words_per_side": list(map(len, side_words)),
                         "boundary_choices_checked": choices,
                         "boundary_choices_passing": passing,
                         "boundary_choices_passing_fans_and_disk_euler": passing_euler,
                         "first_witness": first,
                         "first_witness_also_passing_disk_euler": first_euler}
        assert first is not None
        assert first_euler is not None
    assert [r["boundary_choices_checked"] for r in records.values()] == [625, 21801]
    return {"scope": "necessary angle/length boundary-fan test only; no placement or marked-source legality",
            "field": "Q(phi), phi^2=phi+1, phi>1",
            "length_symbols_in_basis_1_phi": LENGTHS,
            "native_corner_classes": CORNERS,
            "fan_counts": [{"from": a, "to": b, "angle_pi_over_5": c,
                             "walks": len(table[a, b, c])}
                            for a, b, c in table],
            "flat_boundary_all_nine_endpoint_pairs_pass":
                all(table[a, b, 5] for a, b in product(LENGTHS, repeat=2)),
            "fixtures": records,
            "conclusion": "The necessary boundary-fan test excludes neither U nor V."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = certificate()
    rendered = json.dumps(data, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
