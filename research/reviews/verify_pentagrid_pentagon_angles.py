#!/usr/bin/env python3
"""Independent exact certificate audit, with partition-based enumeration.

Does not import the producer or use a polyhedral/linear-program solver.
This checks only the stated finite angular theorem and its rational
incidence witnesses, never geometric closure or plane tilability.
"""
from fractions import Fraction
from itertools import combinations_with_replacement, permutations
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def partitions(total, least=1, largest=4):
    if total == 0:
        yield ()
    for first in range(least, min(total, largest) + 1):
        for suffix in partitions(total - first, first, largest):
            yield (first,) + suffix


def orbit_min(word):
    return min(tuple(word[(offset + sign * j) % 5] for j in range(5))
               for sign in (-1, 1) for offset in range(5))


def vector(word):
    return tuple(sum(x == k for x in word) for k in (1, 2, 3, 4))


root = Path(__file__).resolve().parents[2]
c = json.loads((root / "research/certificates/pentagrid_pentagon_angles.json").read_text())
multis = sorted(w for w in partitions(15) if len(w) == 5)
raw_words = {w for m in multis for w in permutations(m)}
words = sorted({orbit_min(w) for w in raw_words})
require(c["raw_word_domain_size"] == 1024, "word domain")
require(c["ordered_valid_words"] == len(raw_words) == 101, "ordered words")
require(c["dihedral_words"] == len(words) == 13, "dihedral words")
require(c["multisets"] == [list(w) for w in multis], "multisets")
require([tuple(r["word"]) for r in c["word_rows"]] == words, "word rows")
remaining = []
for row in c["word_rows"]:
    word = tuple(row["word"])
    seams = [j for j in range(5) if word[j] + word[(j + 1) % 5] == 5]
    require(row["supplementary_seams"] == seams, "seam list")
    require(row["periodic_halfturn_escape"] == bool(seams), "escape flag")
    if not seams:
        remaining.append(word)
U, V, W = (1, 3, 4, 4, 3), (2, 2, 4, 3, 4), (3, 3, 3, 3, 3)
require(remaining == [U, V, W], "remaining words")
expected_pairs = [[list(a), list(b)]
                  for a, b in combinations_with_replacement(remaining, 2)
                  if (a, b) != (W, W)]
require(c["retained_aperiodicity_word_pairs"] == expected_pairs, "surviving pairs")

stars = sorted({vector(p) for total in (5, 10) for p in partitions(total)})
require(len(stars) == 29, "star count")
require(c["native_star_domain_size"] == 14641, "star domain")
require([tuple(r["counts"]) for r in c["native_stars"]] == stars, "star list")
f = tuple(c["nonnegative_functional"])
require(f == (3, 1, -1, 2), "functional")
for row in c["native_stars"]:
    s = tuple(row["counts"])
    angle_sum = sum((i + 1) * s[i] for i in range(4))
    value = sum(f[i] * s[i] for i in range(4))
    require(row["angle_sum_units"] == angle_sum, "star angle sum")
    require(row["functional"] == value and value >= 0, "star functional")


def witness_sum(rows, available):
    result = [Fraction(0) for _ in range(4)]
    seen = set()
    for row in rows:
        s, weight = tuple(row["star"]), Fraction(row["weight"])
        require(s in stars and s not in seen, "witness star/duplicate")
        seen.add(s)
        require(weight > 0, "positive star weight")
        require(all(not s[i] or i + 1 in available for i in range(4)), "available angles")
        for i in range(4):
            result[i] += weight * s[i]
    return tuple(result)


require(len(c["multiset_pair_rows"]) == 15, "pair count")
require([tuple(tuple(w) for w in row["multisets"])
         for row in c["multiset_pair_rows"]] ==
        list(combinations_with_replacement(multis, 2)), "pair completeness")
for row in c["multiset_pair_rows"]:
    a, b = map(tuple, row["multisets"])
    allowed = set(a + b)
    allowed_stars = [s for s in stars
                     if all(not s[i] or i + 1 in allowed for i in range(4))]
    if a == b == W:
        require(not allowed_stars, "all108 obstruction")
        require(row["status"] == "impossible" and row["tile_counts"] is None
                and row["star_weights"] == [], "empty case")
        continue
    amounts = row["tile_counts"]
    require(len(amounts) == 2 and all(Fraction(n) >= 0 for n in amounts), "tile amounts")
    require(sum(map(Fraction, amounts)) > 0, "nonzero tile amounts")
    target = tuple(sum(Fraction(amounts[j]) * vector((a, b)[j])[i]
                       for j in range(2)) for i in range(4))
    require(witness_sum(row["star_weights"], allowed) == target, "incidence equality")
    if b == W and a == (2, 3, 3, 3, 4):
        require(sum(f[i] * vector(a)[i] for i in range(4)) == 0, "zero partner functional")
        require(sum(f[i] * vector(b)[i] for i in range(4)) == -5, "negative W functional")
        require(row["status"] == "feasible only with W count zero"
                and amounts[1] == 0, "zero W classification")
    else:
        require(row["status"] == "positive both feasible"
                and all(Fraction(n) > 0 for n in amounts), "positive both classification")

require(len(c["mono_incidence_witnesses"]) == 4, "mono count")
require([tuple(r["multiset"]) for r in c["mono_incidence_witnesses"]]
        == multis[:-1], "mono completeness")
for row in c["mono_incidence_witnesses"]:
    m = tuple(row["multiset"])
    require(witness_sum(row["star_weights"], set(m)) == vector(m), "mono witness")

caps = c["W_to_partner_incidence_caps"]
require(len(caps) == 4 and [tuple(r["partner"]) for r in caps] == multis[:-1], "caps")
for row in caps:
    m = tuple(row["partner"])
    cap = Fraction(row["upper_ratio"])
    require(sum(f[i] * vector(m)[i] for i in range(4)) == 5 * cap, "cap dual identity")
    pair = next(r for r in c["multiset_pair_rows"] if r["multisets"] == [list(m), list(W)])
    require(Fraction(pair["tile_counts"][1]) == cap * pair["tile_counts"][0], "cap attained")
print("PASS: 101 ordered words, 13 dihedral words, 29 full/half stars; "
      "15 complete incidence cases and five surviving angle-word pairs.")
