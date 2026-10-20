# Rational P5/P5 double adjacent split

Date: 2026-10-20. **Status: exact local patch, stopped as a full-edge route.** The unrestricted two-convex-polygon problem remains unresolved. Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch python research/searches/double-adjacent-split-2026-10-20.py
```

## Deduplication and construction

This is a new rational fixture with two **adjacent** P sides simultaneously split by four Q copies. The split sides meet at a P angle `alpha = 360° - 2 beta`, where `cos(beta)=-5/13` and `90°<beta<120°`. The partner has a beta corner between two unit sides and a right corner at the opposite end of one of those sides. Consequently two Q copies close the exterior star at the shared P vertex, and pairs of Q right angles close the flat stars at both side midpoints. This contact topology differs from the one-side P/Q/Q midpoint fixtures, Cairo arms, the acute A/A/B long-edge T contact, source dissections, and the P5/Q6 full-edge 120-degree bridge indexed in [the deduplication audit](shape-first-dedup-audit-2026-10-20.md). The exact angle and length words printed by the verifier differ from those fixtures. This is repository deduplication, not a literature novelty statement.

In counterclockwise order, the coordinates are

```
P = ((0,0),(2,0),(2,2),(-1,3),(-238/169,240/169))
Q = ((0,0),(1,0),(1,1),(1/2,7/5),(-5/13,12/13)).
```

All consecutive turn determinants are positive: `P=(480/169,4,6,870/169,474/169)` and `Q=(12/13,1,1/2,77/130,1)`. Twice the areas are `2502/169` and `29/10`; they are distinct strict convex pentagons. Squared side words are `P=(4,4,10,450/169,4)` and `Q=(1,1,41/100,101/100,1)`. The numerical angle words, only for identification, are approximately `P=(134.7603,90,108.4349,86.0548,120.7500)` and `Q=(112.6199,90,128.6598,113.0097,95.7106)` degrees. Exact dot/cross angle data and all vertices are printed on replay.

An earlier symmetric partner `Q=((0,0),(1,0),(1,1),(7/13,17/13),(-5/13,12/13))` gave the same star but matched Rao monohedral pentagon types 2 and 4, so it was discarded before further patch growth. The stated asymmetric Q breaks that escape. For **both** stated shapes, 100-bit outward-rounded Sage interval arithmetic excludes every angle equation in the repository's reviewed transcription of Rao's 15 convex-pentagon monohedral types. The script then checks the exact algebraic side equations; the type screen has no hits. Conditional on that imported classification and its transcription, neither species tiles the plane alone. Neither polygon has consecutive supplementary angles.

## Exact five-tile patch

Take the displayed P. On each of its two sides from `O=(0,0)` to `E1=(2,0)` or `E2=(-238/169,240/169)`, place a Q with native side 0 on the first half, beta corner at O and right corner at the midpoint. Place another Q with its right corner at that midpoint and its native side 0 on the remaining half. The script prints all four exact rational placements and verifies every pair of interiors disjoint by the convex separating-axis criterion. At O the first two Q copies share the segment from `(0,0)` to `(-5/13,-12/13)`. Their beta sectors and P's alpha sector sum to 360 degrees. At each midpoint, the two Q right sectors fill the exterior half-plane and their other rays coincide exactly. Thus three local stars close without marks or imposed edge-to-edge rules.

Reflecting P in either *same native split side* collides with the first Q on the other side; the script checks this exactly. This is the extra endpoint mechanism missing from the earlier single-side fixture. It still does **not** show that the double split is compulsory in every tiling. In fact, the script enumerates all congruent P whole-side placements using any of P's three length-2 native sides. Some placements avoid the Q on the other adjacent side. The local interference excludes only the simple same-side mirror, and only after the adjacent Q is already present.

## Boundary test and limit

The exposed native side 3 of the first Q has two distinct legal full-edge Q attachments, including reflections, against the five-tile patch. The exposed native side 2 of that same Q has **zero** full-edge P or Q attachments: its squared length `41/100` is Q-private, and both candidate isometries of another Q collide with the patch. The verifier enumerates every native side of either species with that exact squared length, both target directions, and both reflection flags, retaining only exact interior-disjoint copies. Therefore this particular five-tile patch cannot extend to an edge-to-edge plane tiling. A partial-contact continuation could exist but has not been constructed or ruled out. No mixed periodic quotient was searched after this obstruction; the monohedral gate above is the completed cheap periodic-carrier check.

The construction supplies no plane existence, global shape-only forcing, or aperiodicity theorem. It should be reopened only with a concrete partial-contact continuation at the blocked Q side, preferably one that can propagate a hierarchy and survive a mixed periodic-carrier attack. Enlarging the existing full-edge branches repeats a stopped route.
