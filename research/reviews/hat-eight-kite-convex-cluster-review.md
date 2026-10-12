# Hostile review: fixed eight-kite hat compiler gate

Date: 2026-10-12. **VALID scoped exclusion.** Every convex whole-kite cluster in the retained fixed reference hat admits a monohedral periodic tiling. Source aperiodicity cannot survive this compiler.

[The independent checker](check_hat_eight_kite_convex_clusters.py) imports no source or producer module and uses no convex-hull routine. It reads the exact Q(sqrt(3)) coordinates in [the retained gate](../certificates/hat-eight-kite-convex-cluster-gate.json), verifies all eight primitive kites are strictly convex and positively oriented, and clips every pair to prove their interiors disjoint. There are 28 checked pairs. It splits directed edges at all relevant vertices and cancels opposite segments; the union boundary agrees exactly with the retained hat outline, beyond equality of total area.

For all 255 nonempty subsets, the checker reconstructs boundary cycles by edge cancellation and tests global supporting half-planes. It independently finds exactly 16 convex unions. Seven have at least five intrinsic corners: masks 6,9,12,13,14,48,192. Intrinsic corner counts and polygon coordinates agree with the producer. This establishes both the small census and the soundness of its hull-area criterion for the disjoint retained atoms.

Unordered exact set-cover enumeration gives exactly one partition using only the eligible clusters: masks 6,9,48,192. The four pieces are congruent pentagons, so the partition has one class. It does not produce the required two distinct classes. More decisively, all five two-kite eligible clusters (6,9,12,48,192) are congruent. Three 120-degree rotations of one representative partition a regular hexagon exactly. The two three-kite clusters (13,14) are also congruent; two 180-degree rotations partition a regular hexagon exactly. The checker verifies disjoint interiors, boundary equality, six equal circumradii and six equal sides for both regular hexagons. Translating that regular hexagon in its usual honeycomb lattice yields an explicit monohedral periodic tiling by each pentagon class. Every other convex cluster is a triangle or quadrilateral and has its usual periodic monohedral escape.

Thus any final pair containing any convex whole-kite subset from this fixed compiler fails the problem's aperiodicity requirement: omission of the other tile is permitted. Adding a second class or changing which source hats receive which local partition cannot remove that escape. The source's infinite forcing theorem and source-language occurrence are not needed for this negative geometric gate.

[Controls](hat-eight-kite-convex-cluster-check.json) retain the exact source digest and all counts. The checker is nondestructive by default and supports --output PATH for temporary registered replay.

Scope: the fixed retained reference eight-kite geometry tagged Hat(1,sqrt(3)), with clusters consisting of whole atoms within that reference. Changed atom geometry, changed hat parameters, cuts through atoms and clusters crossing source-hat boundaries are not covered. The audit supplies no generalized hat-family exclusion and no new positive construction.

```bash
MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_hat_eight_kite_convex_clusters.py
```
