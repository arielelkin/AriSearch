# Pentagon-dimer purification for balanced complementary-angle heptagons

## Theorem

Let `P` be the unit regular pentagon and `Q` a strictly convex heptagon with one angle `A=144°`, three angles `B=α` and three angles `C=252°−α`, where real `108°<α<126°`. If `{P,Q}` tiles the plane with arbitrary isometries and contacts, it also has a tiling by the same fixed shapes in which **every P has exactly one P neighbor** across a full side. Thus the PP contact graph of that tiling is a perfect matching. Moreover, in every tiling, no P has two P neighbors, and the number of P with no P neighbor meeting a side-`R` square is `O(R)`.

The statement applies to all balanced Q7 words, although the interesting still-open application is to `ABBCCBC`, `ABBCCCB`, `ABCBBCC`, and `ACBBBCC`. It asserts neither plane existence for those words nor periodicity of the purified tiling.

## Proof

The [complementary-angle necessary theorem](complementary-angle-flow-necessary-theorem-2026-10-19.md) forces full-edge contacts and trivalent PPA/PBC stars wherever P occurs, even at `α=120°`; the extra BBB stars contain Q only. At a PPA corner, exactly one of the two incident P sides faces P. At a PBC corner, neither does. Hence PP sides on a pentagon are an independent set in its five-cycle, of cardinality at most two.

If P had two PP sides, they would flank one intervening PQ side. Both endpoints of this PQ side are PPA vertices, so the *same* Q across it would have to present an A corner at each endpoint. Q has only one A corner and therefore no AA side. This contradiction proves PP-degree two is impossible pointwise, including at resonance. Let `n_0(R)` count P with zero PP sides in a square and `n_1(R)` those with one; all boundary conventions differ by `O(R)` because the fixed polygons have bounded diameter and positive area.

Off resonance, every Q has exactly one A corner, and every A corner sits at a PPA vertex, which is the endpoint of one PP side. Counting A incidences gives `2e_{PP}(R)=q_R+O(R)`. Counting P ends of PP sides gives `2e_{PP}(R)=n_1(R)+O(R)`. The [same reviewed window theorem](complementary-angle-flow-necessary-theorem-2026-10-19.md) gives `p_R=q_R+O(R)` for the balanced Q7 inventory. Since `p_R=n_0(R)+n_1(R)+O(R)`, subtraction yields `n_0(R)=O(R)`.

At `α=120°`, the balanced B/C budget bounds BBB vertices and tiles touching them by `O(R)`. Away from those defective Q copies, the same A and side ledger applies. Enlarging the window by a fixed tile diameter changes only `O(R)` terms; thus the original tiling again has `n_0(R)=O(R)`. Alternatively use the explicit nonnegative charge certificate below on the defect-free tiles. For each fixed radius `r`, the radius-`r` neighborhoods of degree-zero P copies in a side-`R` square have area `O_r(R)`. Choose increasingly large disks avoiding them, translate their centers to the origin, and take a locally convergent subsequence of tilings by the same fixed finite shapes. The limit has no degree-zero P. PP-degree two was impossible pointwise and remains so; every P in the limit has exactly one PP side.

An exact equivalent charge certificate assigns weights `(-1,+1,+1,-1)/5` to the four P-facing Q side slots `0,2,4,6` in a defect-free tiling. Each Q's weights sum to zero. A P of PP-degree `k` receives charge `1−k`, because it has `5−k` PQ sides, of which `2k` endpoints are A. With `k∈{0,1}`, the charge is exactly its degree-zero indicator. Window cancellation gives `n_0=O(R)` directly. At resonance, the `O(R)` defective Q copies change the charge sum by only `O(R)`.

## Exact finite support and limits

The [producer gate](../searches/heptagon-mixed-discharge-sol-2026-10-19.md) enumerates all native P incidence types with both Q reflection parities for the four surviving mixed words, verifies an exact rational incidence relaxation, and retains a replayable Python checker and JSON certificate. Its rational primal flows are **not** tilings or geometric quotients. The [independent Sol hostile review](../reviews/heptagon-mixed-discharge-hostile-sol-2026-10-19.md) validates the pointwise obstruction, charge and purification after the producer's resonance wording correction.

Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/heptagon-mixed-discharge-sol-2026-10-19.py
```

The theorem supplies a PP perfect matching in some tiling whenever a tiling exists. It does not control the reflected QQ seam holonomy or provide a periodic carrier for the four open mixed words. No larger torus or local patch search follows from it alone.
