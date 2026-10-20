# Conditional periodicity for all-BC balanced heptagons

## Theorem

Let `P` be the unit regular pentagon, and let `Q` be any strictly convex heptagon with angles in cyclic order `A` followed by three ordered pairs, each `BC` or `CB`, where `A=144°`, `B=α`, `C=252°−α`, and `108°<α<126°`. If `{P,Q}` tiles the plane using arbitrary isometries and contacts, the same two polygons admit a rank-two periodic tiling. This covers all four rooted reversal classes `ABCBCBC`, `ABCBCCB`, `ABCCBBC`, `ACBBCBC` and every positive metric realization that tiles, including `α=120°`. It does not assert that the given tiling is periodic.

## Proof and dependencies

The [reviewed complementary-angle flow theorem](complementary-angle-flow-necessary-theorem-2026-10-19.md) forces full-edge PPA/PBC stars except that at `α=120°` BBB vertices can occur. In the latter case its square-window branch budget bounds the total number of BBB corner incidences in a radius-`R` window by `O(R)`. Since any defective Q contributes a positive integer number of such incidences, for every fixed radius `r` there are defect-free disks of radius `r` in sufficiently large windows: fixed-radius neighborhoods of all defective tiles have only `O_r(R)` area while the window has area `Θ(R²)`. Translating disks of increasing radius to the origin and taking a locally convergent subsequence gives a tiling by the same fixed polygons with no BBB vertices. For `α≠120°`, the starting tiling already has that property. The source proof explains local compactness with fixed compact polygon shapes and positive minimum tile area.

In the defect-free tiling, each Q's sole A corner has no QQ incident side and each B/C corner has one. Consequently the six-corner path after A has the unique perfect matching `(1,2),(3,4),(5,6)`. Q sides `1,3,5` meet Q, and Q sides `0,2,4,6` meet unit P sides. Therefore those four intrinsic Q lengths equal one. This implication at `α=120°` concerns the purified tiling; BBB defects may remain in the original tiling.

The [exact four-face construction](../searches/heptagon-all-bc-qdimer-sol-2026-10-19.md) applies to **every** closed strictly convex Q of this angle word with sides `0,2,4,6` unit and arbitrary positive remaining lengths satisfying closure. It glues two P and two Q disks along twelve full edges. The eight vertex links are single PPA or PBC three-cycles of angle sum 360°, every edge is paired by a length-preserving orientation-reversing map, and Euler characteristic is `8−12+4=0`. The resulting connected compact oriented complete flat surface is a torus. Its universal cover is the Euclidean plane, tiled degree one by the lifted polygon faces, and its deck group is a rank-two translation lattice. Thus the fixed P,Q admit a rank-two periodic tiling.

The explicit seam map, symbolic angle and heading checks, exact metric cone, verifier, and JSON certificate are in the construction report. Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/heptagon-all-bc-qdimer-sol-2026-10-19.py
```

The [independent Sol hostile review](../reviews/heptagon-all-bc-hostile-sol-2026-10-19.md) passed the carrier theorem **with the four unit-side restriction** and its conditional application using the prior flow gate. No assertion is made for a Q metric whose four public sides are not unit, or for the six other balanced heptagon words.
