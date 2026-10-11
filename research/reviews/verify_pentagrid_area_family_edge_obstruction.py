#!/usr/bin/env python3
"""Independent multiset/native-edge-link check of the U/V family ETE ban.

No author script is imported.  Enumerate angle-compatible corner multisets,
then search for actual circular endpoint-length assignments for each multiset.
"""
import argparse
import json
from itertools import product
from pathlib import Path

NAMES = ("U36", "U108", "U144", "V72", "V144", "V108")
WEIGHTS = (1, 3, 4, 2, 4, 3)


def circular_link(counts, nodes):
    """Find a circular arrangement of the given native corner multiset.

    A circle can be rotated to begin with its smallest occupied class.
    That corner may face either way; thereafter each native edge length must
    match the next corner's native edge length.  This covers mirrors too.
    """
    counts = list(counts)
    first = next(i for i, n in enumerate(counts) if n)
    a, b = nodes[first]
    initial = [(a, b)] if a == b else [(a, b), (b, a)]
    counts[first] -= 1

    def extend(current, target, path):
        if not any(counts):
            return path if current == target else None
        for i, n in enumerate(counts):
            if n == 0:
                continue
            a, b = nodes[i]
            choices = []
            if a == current:
                choices.append((a, b))
            if b == current and b != a:
                choices.append((b, a))
            for left, right in choices:
                counts[i] -= 1
                found = extend(right, target,
                               path+[(NAMES[i], left, right, WEIGHTS[i])])
                counts[i] += 1
                if found is not None:
                    return found
        return None

    for start, end in initial:
        found = extend(end, start,
                       [(NAMES[first], start, end, WEIGHTS[first])])
        if found is not None:
            return found
    return None


def length_order_check():
    # Each length has b and c coefficients in the independent basis (1,phi).
    lengths = {"A": ((1, 1), (0, 1)),
               "D": ((0, 2), (1, 1)),
               "E": ((0, 1), (0, 1)),
               "b": ((1, 0), (0, 0)),
               "c": ((0, 0), (1, 0))}

    def subtract(a, b):
        return tuple(tuple(x-y for x, y in zip(p, q))
                     for p, q in zip(lengths[a], lengths[b]))

    assert subtract("D", "A") == ((-1, 1), (1, 0))
    assert subtract("A", "E") == ((1, 0), (0, 0))
    assert subtract("E", "b") == ((-1, 1), (0, 1))
    assert subtract("E", "c") == ((0, 1), (-1, 1))
    return {"D_minus_A": "(phi-1)b+c >0",
            "A_minus_E": "b >0",
            "E_minus_b": "(phi-1)b+phi*c >0",
            "E_minus_c": "phi*b+(phi-1)c >0",
            "only_possible_length_coincidence": "b=c"}


def certificate():
    # Native corner occurrences follow directly from lengths and after-side
    # angles of the two pentagons; two equal occurrences share a class.
    distinct = [("A", "A"), ("A", "b"), ("b", "c"),
                ("b", "D"), ("b", "E"), ("E", "E")]
    merged = [("b" if a == "c" else a, "b" if b == "c" else b)
              for a, b in distinct]
    angular = [counts for counts in product(*(range(11//w+1) for w in WEIGHTS))
               if sum(n*w for n, w in zip(counts, WEIGHTS)) == 10]
    expected = {
        "b_distinct_c": {(10, 0, 0, 0, 0, 0), (4, 2, 0, 0, 0, 0),
                         (0, 2, 0, 2, 0, 0)},
        "b_equals_c": {(10, 0, 0, 0, 0, 0), (4, 2, 0, 0, 0, 0),
                       (0, 2, 0, 2, 0, 0), (0, 2, 1, 0, 0, 0)},
    }
    cases = {}
    for case, nodes in (("b_distinct_c", distinct), ("b_equals_c", merged)):
        witnesses = []
        for counts in angular:
            link = circular_link(counts, nodes)
            if link is not None:
                assert len(link) == sum(counts)
                assert sum(c[3] for c in link) == 10
                assert all(link[i][2] == link[(i+1) % len(link)][1]
                           for i in range(len(link)))
                witnesses.append({"corner_counts": counts, "circular_link": link})
        found = {tuple(w["corner_counts"]) for w in witnesses}
        assert found == expected[case], (case, found)
        assert all(counts[4] == 0 for counts in found)  # no V144
        if case == "b_distinct_c":
            assert all(counts[2] == 0 for counts in found)  # no U144
        else:
            assert {counts for counts in found if counts[2]} == {(0, 2, 1, 0, 0, 0)}
        cases[case] = {"angle_compatible_multisets_checked": len(angular),
                       "length_compatible_multiset_count": len(found),
                       "all_length_compatible_multisets": witnesses}
    # A vertex after side_i is theta_i.  The endpoints of side_i have
    # theta_(i-1),theta_i, so the middle b-side has two144 endpoints.
    after_u = (1, 3, 4, 4, 3)
    side_ends = [(after_u[(i-1) % 5], after_u[i]) for i in range(5)]
    assert side_ends[3] == (4, 4)
    assert not any(ends == (3, 3) for ends in side_ends)
    return {"status": "VALID: complete necessary vertex-link enumeration",
            "scope": "edge-to-edge plane tilings only; no partial-contact exclusion",
            "corner_class_order": NAMES, "angle_weights_pi_over_5": WEIGHTS,
            "strict_length_order": length_order_check(), "cases": cases,
            "U_native_side_endpoint_angles_pi_over_5": side_ends,
            "global_conclusion": "No V144 star; distinct b,c give no U144 star. At b=c forced U144+2U108 star requires a nonexistent U side with two108 endpoints."}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(certificate(), indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
