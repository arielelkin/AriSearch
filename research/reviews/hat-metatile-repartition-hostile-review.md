# Independent hostile review: initial hat assigned-union repartition gate

Date: 2026-10-19. Verdict: **valid within the explicitly bounded domain**.
The original two-convex-tile problem remains unresolved.

## Exact claim and assumptions

For the four retained initial assigned hat unions H/T/P/F, enumerate every
edge-connected subset of 1 through 8 constituent whole kites. Keep exactly
those whose union is a convex polygon with 5 or 6 intrinsic corners. Classify
by unrestricted Euclidean congruence, permitting reflection. Consider each
unordered pair of resulting classes and every four-region tuple of exact
covers, requiring both classes somewhere and a piece containing cells from
more than one source hat somewhere. There are three classes, 98 eligible
placements, and 3304 such tuples. Every palette admits a monohedral periodic
tiling, so none solves the target problem.

The actual domain consists of assigned unions, not the source proxy polygons.
No substitution closure, extension, or aperiodicity transfer for these unions
is assumed. Each cell is fixed at the source half-reference scale. The bound
excludes cuts through cells, more than eight cells per piece, and inter-region
pieces. Both-class use in each individual region is a different, stricter
condition, correctly noted as impossible in the producer report.

## Independent reconstruction and attacks

Reviewed the governing problem and protocol, producer, search report, source
initialization, retained JSON, and checker. Added a separate retained checker:
`research/reviews/check_hat_metatile_repartition_completeness.py`.
It imports no repartition producer and computes no convex hulls.

1. Reconstructed each initial source placement using the separately reviewed
   eight-kite certificate and the exact source init transformations. All
   assigned primitive sets match, with 4/1/2/2 source hats. The reflected H
   constituent is retained; polygon orientation normalization cannot discard it.
2. Checked that no primitive vertex lies strictly inside another primitive
   edge. Together with the existing exact pairwise zero-overlap check, this
   establishes the conforming full-edge adjacency used by enumeration. There
   is no omitted partial-edge connection. A positive-area convex union has
   connected interior, so components meeting only at vertices cannot add a
   missed convex piece.
3. Enumerated connected vertex sets in the adjacency graph independently and
   reconstructed each candidate boundary by directed-edge cancellation. A
   single boundary cycle with all positive turns and 5 or 6 corners is the
   eligibility test. It returns exactly the retained masks, including every
   rejection implicit in the producer hull test. Counts by size match:
   H: 32,49,102,232,560,1377,3377,8164;
   T: 8,9,13,17,17,11,5,1;
   P and F: 16,21,37,65,112,189,310,469.
   Eligible counts are 49,7,21,21. Graph growth is complete by a spanning-tree
   vertex ordering. Deduplication deletes only identical cell sets.
4. Recomputed every pair's exact covers by branching on the greatest uncovered
   cell, contrasting the producer's least-cell recursion. Compared sets of
   entire four-region witnesses, also requiring no duplicates. Pair (0,1)
   has counts 125,1,5,5 and 3093 admissible tuples; (0,2) has 27,1,3,3 and 211;
   (1,2) has zero covers in all four regions. No omitted or spurious tuple.
5. Audited the congruence invariant: a full labeled distance matrix determines
   a polygon up to Euclidean isometry; cyclic starts and reversal exhaust
   vertex correspondences of strictly convex polygons. The separate geometry
   checker confirms all same-class matches and all different-class failures.
   Reflection is allowed, with no restriction to lattice rotations.
6. Cross-hat flags are recomputed from source owners. Because every included
   cell has positive area, two owners mean the piece actually contains area
   from two hats. Combined with connected convexity this is genuine crossing,
   not point contact. The global rather than per-region condition is explicit.
7. Reran the existing independent periodic-carrier checker. Its two pentagons
   partition a regular hexagon in three and two congruent copies respectively.
   The new classes match these pentagons at half scale. Independently verified
   each six-corner representative using exact equal circumradii and equal
   chord lengths, with squared chord equal to squared radius. Thus it is a
   regular hexagon. Regular hexagons repeat on a translation lattice, and
   repeating their finite dissections gives a periodic tiling by either
   pentagon alone. The target permits monohedral tilings, so each palette is
   decisively excluded without any decoder or global hat assumption.

## Defects, repairs, and remaining uncertainty

No mathematical defect found in the stated bounded result. The original
checker explicitly verifies retained objects rather than enumeration
completeness. The additional checker closes this audit coverage gap by
independently testing all connected clusters and exact-cover products.
No producer repair was required. An unused producer cover helper and common
class variable have no influence on the executed enumeration.

The review verifies consistency with retained exact source initialization;
it does not newly certify that initialization against a remote publication.
That attribution is unnecessary for the finite result on the explicit cells.
The proxy/assigned-union area mismatch is disclosed and not used to transfer
any infinite tiling property. No omitted periodic carrier or accidental
reflection restriction remains within the stated domain. Beyond this domain,
no conclusion is obtained.

## Replay and retained identity

All three checks passed with assertions enabled:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_hat_metatile_repartition_completeness.py
mise exec -- conda run --no-capture-output -n arisearch python research/searches/check_hat_metatile_repartition.py
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_hat_eight_kite_convex_clusters.py
```

Reviewed gate certificate SHA256:
`2e633db488e3942617d1db68cf795c0782bca476256d0cb20fa4b2ac4f64121b`.
Periodic-carrier certificate SHA256:
`535d7c83ec6039729cc83c94af34342215e607ca0ed73de89d3ccede56ec6075`.

Final verdict: **valid**, interpreted only as the finite classification and
periodic escape result above; **not a solution of the original problem**.
