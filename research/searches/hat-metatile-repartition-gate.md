# Initial hat-metatile whole-kite repartition gate

2026-10-19. Computational evidence; target remains unresolved. Declared bound:
connected edge-adjacent sets of one through eight whole constituent kites,
within each initial H/T/P/F assigned hat union, with a 180-second execution cap.
The completed run hit no cap. Stop here absent a changed mechanism.

## Exact source and realizable domain

The retained source `source-decoration-hat-patch.py` reimplements Kaplan's
hatviz initial metatiles; `init()` assigns 4/1/2/2 hats to H/T/P/F, respectively.
Each hat is half reference scale and comprises eight exact standard grid kites.
The source outlines are proxy polygons, **not** these assigned hat unions:
unsigned doubled area divided by sqrt(3) is 16/4/8/8 for actual hat unions,
versus 16.5/4.5/8/7.5 for proxy polygons. Thus this gate partitions the exact
assigned unions, not proxy polygons; it does not assert these four unions
are themselves a polygonal metatile substitution. Source aperiodicity or
plane tilability is not transferred to their repartitions. The source
primary provenance is Smith–Myers–Kaplan–Goodman-Strauss, *An aperiodic
monotile*, arXiv:2303.10798, and Kaplan's hatviz initialization as retained
in the exact producer. Existing reviewed fixed-eight-kite artifacts verify
the reference hat dissection and periodic pentagon carriers independently.

Stored integer coordinates (X,Y) mean physical coordinates
(X/4,sqrt(3)Y/4). All predicates therefore use integer determinants or the
positive definite squared metric dx²+3dy². No numeric tolerance is used.
Adjacency means a full constituent kite edge in common. On this conforming
Laves-grid patch this enumerates connected unions with interior connection;
point-only contacts cannot form a strictly convex polygon with positive area.

## Complete finite domain and result

Starting with every singleton and repeatedly adjoining every adjacent cell
outside the set enumerates every connected set of the given size: a connected
finite graph has an ordering obtained from a spanning tree. Deduplication by
bit mask removes only identical sets. Counts by sizes 1,...,8 are:

| region | cell count | connected counts | convex 5/6-gons |
|---|---:|---|---:|
|H|32|32,49,102,232,560,1377,3377,8164|49|
|T|8|8,9,13,17,17,11,5,1|7|
|P|16|16,21,37,65,112,189,310,469|21|
|F|16|16,21,37,65,112,189,310,469|21|

A cluster equals its hull iff its area equals its hull area, since all
primitive cells have disjoint interiors and the compact union lies inside
the hull. The monotone hull algorithm removes collinear intermediate points;
only exactly five or six intrinsic corners survive. Full pairwise vertex
distance words minimized over cyclic shifts and reversal classify congruence,
including reflection. Exactly three classes survive: two-kite pentagon,
three-kite pentagon, regular six-kite hexagon.

All three unordered pairs are checked. Every exact cover is obtained by
choosing a piece containing the least uncovered cell, which removes only
piece-order duplication. The common palette has exactly two classes, both
used somewhere in the four-region product, with at least one piece crossing
an internal hat boundary. For classes (0,1), per-region cover counts are
125,1,5,5, giving 3093 admissible products. For (0,2), counts are 27,1,3,3,
giving 211 products. Pair (1,2) cannot cover T. Total: 3304 witnesses, all
retained and checked. If “common two classes” instead means each region
must use both classes, there are no witnesses: T has only its four congruent
two-kite-pentagon partition. The palette interpretation is the more permissive
construction gate and does not omit that stricter interpretation.

## Hostile conclusions and remaining gaps

Every resulting palette admits a monohedral periodic tiling. The two
pentagons are exactly half-scale copies of the independently reviewed
fixed-eight-kite periodic carriers; respectively three or two copies
partition a regular hexagon. The third class is already a regular hexagon.
Hexagon lattice repetition therefore kills every palette, whether or not it
has the desired cross-hat repartition. No global decoder claim is made.

The audit script imports no gate producer. It checks all primitive pairs
for zero overlap by exact clipping, each hat's eight-cell boundary, each
retained cluster by edge cancellation and strict turns, congruence classes,
every retained witness's disjoint cell coverage, and exact matches to the
reviewed periodic carrier polygons. Enumeration completeness is the finite
growth and cover argument above, subject to fresh external hostile review.

Omissions deliberately outside the bound: cuts through kites, clusters with
more than eight cells, crossing between assigned metatiles, other initial
source decompositions, and continuous deformation. More enumeration of the
same bound cannot improve this mechanism. The gate supplies neither an
aperiodic convex pair nor any global impossibility theorem.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch timeout 180 python research/searches/hat-metatile-repartition-gate.py research/certificates/hat-metatile-repartition-gate.json
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/check_hat_metatile_repartition.py

Retained evidence: `research/certificates/hat-metatile-repartition-gate.json`.
