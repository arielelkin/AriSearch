#!/usr/bin/env python3
"""Exact pentagon angle words and native-star incidence in pi/5 units.

This is an angular relaxation, not a polygon closure or tiling search.
The exhaustive domains are {1,2,3,4}^5 and {0,...,10}^4.
All proof-relevant calculations use integers or fractions. No solver,
stochastic seed, timeout, or prescribed length/placement domain is used.
The accompanying independent checker does not import this file.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
import json


def canonical(word):
    backward = word[::-1]
    return min([word[i:] + word[:i] for i in range(5)] +
               [backward[i:] + backward[:i] for i in range(5)])


def counts(word):
    return tuple(word.count(j) for j in range(1, 5))


def combined(*witnesses):
    result = defaultdict(Fraction)
    for witness in witnesses:
        for star, weight in witness:
            result[star] += Fraction(weight)
    return [{"star": list(star), "weight": str(weight)}
            for star, weight in sorted(result.items()) if weight]


def main():
    if __debug__ is False:
        raise RuntimeError("Run without Python optimization: checks must execute.")
    raw = [w for w in product(range(1, 5), repeat=5) if sum(w) == 15]
    words = sorted({canonical(w) for w in raw})
    multisets = sorted({tuple(sorted(w)) for w in words})
    stars = sorted(s for s in product(range(11), repeat=4)
                   if sum((i + 1) * s[i] for i in range(4)) in (5, 10))
    word_rows = []
    for word in words:
        seams = [i for i in range(5) if word[i] + word[(i + 1) % 5] == 5]
        word_rows.append({"word": list(word), "supplementary_seams": seams,
                          "periodic_halfturn_escape": bool(seams)})
    retained = [tuple(r["word"]) for r in word_rows
                if not r["periodic_halfturn_escape"]]
    assert retained == [(1, 3, 4, 4, 3), (2, 2, 4, 3, 4), (3, 3, 3, 3, 3)]

    # Exact angular incidence decompositions for each non-equiangular
    # multiset. They establish feasibility of the relaxation only.
    mono = {
        (1, 2, 4, 4, 4): [((0, 1, 0, 2), "1"), ((2, 0, 0, 2), "1/2")],
        (1, 3, 3, 4, 4): [((0, 0, 2, 1), "1"), ((2, 0, 0, 2), "1/2")],
        (2, 2, 3, 4, 4): [((0, 1, 0, 2), "1/2"),
                          ((0, 0, 2, 1), "1/2"), ((0, 3, 0, 1), "1/2")],
        (2, 3, 3, 3, 4): [((0, 0, 2, 1), "1"), ((0, 2, 2, 0), "1/2")],
    }
    W = (3, 3, 3, 3, 3)
    mixed_W = {
        (1, 2, 4, 4, 4): (2, [((0, 0, 2, 1), "3"),
                              ((1, 0, 3, 0), "1"), ((0, 2, 2, 0), "1/2")]),
        (1, 3, 3, 4, 4): (1, [((0, 0, 2, 1), "2"), ((1, 0, 3, 0), "1")]),
        (2, 2, 3, 4, 4): (1, [((0, 0, 2, 1), "2"), ((0, 2, 2, 0), "1")]),
    }
    functional = (3, 1, -1, 2)
    star_rows = [{"counts": list(s),
                  "angle_sum_units": sum((i + 1) * s[i] for i in range(4)),
                  "functional": sum(functional[i] * s[i] for i in range(4))}
                 for s in stars]
    assert all(r["functional"] >= 0 for r in star_rows)
    pair_rows = []
    for a, b in combinations_with_replacement(multisets, 2):
        row = {"multisets": [list(a), list(b)]}
        if a == W:
            row.update(status="impossible", obstruction="no legal native star",
                       tile_counts=None, star_weights=[])
        elif b == W and a == (2, 3, 3, 3, 4):
            row.update(status="feasible only with W count zero", tile_counts=[1, 0],
                       star_weights=combined(mono[a]),
                       obstruction="nonnegative functional has tile values 0,-5")
        elif b == W:
            wcount, witness = mixed_W[a]
            row.update(status="positive both feasible", tile_counts=[1, wcount],
                       star_weights=combined(witness))
        else:
            row.update(status="positive both feasible", tile_counts=[1, 1],
                       star_weights=combined(mono[a], mono[b]))
        if row["tile_counts"] is not None:
            target = tuple(sum(row["tile_counts"][j] * counts((a, b)[j])[i]
                               for j in range(2)) for i in range(4))
            actual = tuple(sum(Fraction(w["weight"]) * w["star"][i]
                               for w in row["star_weights"]) for i in range(4))
            assert actual == target
            allowed = set(a + b)
            assert all(tuple(w["star"]) in stars and
                       all(not w["star"][i] or i + 1 in allowed for i in range(4))
                       for w in row["star_weights"])
        pair_rows.append(row)

    final_pairs = [[list(a), list(b)]
                   for a, b in combinations_with_replacement(retained, 2)
                   if (a, b) != (W, W)]
    certificate = {
        "scope": "angular relaxation; unrestricted positive lengths and contacts",
        "raw_word_domain_size": 4**5,
        "ordered_valid_words": len(raw),
        "dihedral_words": len(words),
        "word_rows": word_rows,
        "multisets": [list(w) for w in multisets],
        "native_star_domain_size": 11**4,
        "native_stars": star_rows,
        "nonnegative_functional": list(functional),
        "multiset_pair_rows": pair_rows,
        "retained_aperiodicity_word_pairs": final_pairs,
        "W_to_partner_incidence_caps": [
            {"partner": list(w), "upper_ratio": cap}
            for w, cap in zip(multisets[:-1], [2, 1, 1, 0])],
        "mono_incidence_witnesses": [
            {"multiset": list(w), "star_weights": combined(mono[w])}
            for w in multisets[:-1]],
    }
    assert len(raw) == 101 and len(words) == 13 and len(stars) == 29
    assert len(pair_rows) == 15 and len(final_pairs) == 5
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
