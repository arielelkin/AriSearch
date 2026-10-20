# Independent P5/Q9 periodic and extension attack

Date: 2026-10-20. **Candidate falsified, [independently hostile-reviewed](../reviews/p5q9-hub-hostile-2026-10-20.md).** This is an independent reconstruction of route A in [the 13:49 assessment](astra-shape-first-assessment-2026-10-20-1349.md), followed by an adversarial second-ring extension check. It is not a solution to the two-convex-tiles problem.

## Exact pair and scope

Let `u(t)=(cos(t°),sin(t°))`. Define positive algebraic `b,c` by

`b(u(144)+u(276))+c(u(72)+u(216))=-u(0)`.

The P edge directions and lengths are `(0,72,144,216,276)` and `(1,c,b,c,b)`; the Q data are `(0,36,96,120,156,216,240,276,336)` and `(1,b,c,1,b,c,1,b,c)`. Integrating from the origin gives exact vertices. The independent `AA` checker verifies closure, positivity, and strict convexity. Its approximate values are `b=0.7909430735`, `c=0.8855793520`.

Every interior angle exceeds 90°. Consequently any plane tiling would be edge-to-edge: at a tile vertex in another tile's side interior, the remaining half-plane angle 180° would require at least two corners, each greater than 90°. All ordinary vertices are trivalent.

Only P side 0 and Q sides 0,3,6 have unit length. A Q unit side cannot mate Q: the two endpoint angle sums leave residual 60°, or 48°/72°, none present. A P unit side cannot mate P: reversed endpoints leave a Q156 corner, but the two outgoing lengths are `b,c` whereas a Q156 corner has outgoing lengths `1,c`; aligned endpoints leave 168° at the P96 end. Thus every unit side has a mixed P/Q mate. Reversed endpoint alignment also fails: Q156+P108 leaves P96, whose required outgoing lengths would be `c,c`, whereas its actual lengths are `1,b`. The only possible full-edge alignment pairs Q156 with P96 and Q144 with P108, with opposite tile interiors. This argument includes reflections.

P cannot tile alone: its 96° corner occurs in no all-P trivalent star. Q cannot tile alone already follows from unit-side forcing.

## Periodic quotient gate

The three P arms on a Q's unit sides have their P side-0 directions at `0°,120°,240°`. In a full-edge translational quotient with one Q and three P faces, these are the three distinct P translation orbits. At each of the six arm endpoints the required third corner is P108. Its two compatible cap placements have P unit-edge directions `48°/300°` at the Q156 endpoint and `72°/180°` at the Q144 endpoint, rotated by 120° for the other arms. None is a translate of any arm, excluding that quotient. This is only a smallest-quotient negative, not an aperiodicity claim. A simpler combinatorial exclusion is that such a quotient has nine occurrences each of edge lengths `b` and `c`, impossible to pair into full edges.

## Second-ring obstruction

The same exact checker gives a stronger local contradiction. Fix Q at the origin, its three forced P arms, and focus on Q vertices 1 and 3. Each endpoint needs a P108 cap sharing both exposed sides. Exact matching of the side lengths, vertex angle, all rotations/reflections, and nonoverlap with the four-tile hub leaves exactly two caps at each endpoint. Each cap's unit edge requires a Q owner in the alignment proved above.

At Q vertex 3, cap choice 0's forced Q owner overlaps the central Q and first P arm with strictly positive exact separating-axis margins (approximately `0.13006767` and `0.34942855`). Thus choice 1 is compulsory. Its forced Q owner then overlaps **either** P108 cap choice at Q vertex 1. For both choices the minimum of all exact convex-polygon separating-axis projection gaps is positive, approximately `0.01162896063`. Positive on every edge-normal axis proves positive-area intersection for these convex polygons. This one sector cannot occur in a tiling. Since every Q requires this sector, no tiling contains Q; and no P-only tiling exists. Hence this exact pair is **plane-nontilable**.

The script also enumerates all six cap endpoints, both choices each. Six-cap patches alone have 64 nonoverlapping choices, but when each cap's compulsory Q owner is added, no choice survives. The two-vertex contradiction above is the smaller certificate. The report makes no claim about other P5/Q9 metrics.

## Reproduction and discrepancy with earlier hub script

Run:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/q9-periodic-attack-2026-10-20.py
```

The script uses Sage `AA` real algebraic numbers for coordinates, exact comparisons, side-length matching, and separating-axis tests; printed decimals are explanatory only. Its finite domain is all 2 alignments of each Q unit arm, all P side-length-compatible placements with both isometry parities at the six Q unit endpoints, and each cap's two unit-side Q placements. The decisive certificate needs only the two named Q vertices.

The earlier [hub-gate script](p5q9-hub-gate-2026-10-20.py) reported that all 64 six-cap-plus-owner assemblies avoid overlap. Its overlap routine calls Python `max` and `min` on elements of a cyclotomic field `K`; that ordering is not the physical real ordering of the embedded projections, even when the projections are real. A concrete conflicting cap/owner pair returns `False` there and `True` with exact `AA` projection ordering. The former routine also uses `u(90)=z^(90//12)=z^7`, which rotates by 84° rather than 90°; this makes its axes incomplete, though an axis of any direction still gives a valid *positive* separation if projection ordering is correct. The corrected test must convert every projection to `AA` before extrema and use edge-normal axes.

This second-ring obstruction should receive a separate hostile review before being promoted to a stable theorem or used to close the Q9 family in the discovery log. There is no periodic witness because the pair has no plane tiling.
