# Corrected end-corner IFT branch realizes formal corona 59 locally

Status: **Independently hostile-reviewed valid** for the local ten-tile patch; see [review](../reviews/hexagon-thirtytwo-corona59-local-patch-hostile-sol-2026-10-19.md). No plane extension follows.

## Statement and definitions

Use words A=(0,1,2,0,3,4), B=(0,1,2,0,3,1), edge lengths (2,1+t,1+2t,1+3t,1+4t), and the corrected **end-of-side** angle convention alpha_j at the junction of sides j and j+1. Let the polygons be the analytic branch certified by `research/searches/hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.py`: the same affine support nullspace and free coordinates x4=t,x5=x6=0 as in the original metric construction, but closure directions phi_j=sum_(k=0)^(j-1)(pi-alpha_k). Its solved Jacobian determinant is -3/4. The support equations are

- alpha_A0+alpha_A1+alpha_B2=2pi;
- alpha_A2+alpha_B1+alpha_B5=2pi;
- alpha_A3+alpha_B0+alpha_B4=2pi;
- alpha_A4+alpha_A5+alpha_B3=2pi.

For every sufficiently small positive t this branch geometrically realizes builder corona59 as an embedded patch of ten tiles, consisting of the central AA dimer and its eight distinct exterior neighbors. In particular its interiors are pairwise disjoint. This conclusion concerns a finite patch only.

## Exact base embedding

Write polygon vertices v_j with side j from v_j to v_(j+1). At t=0 both native polygon shapes have vertices

(0, 2, 5/2+i sqrt(3)/2, 2+i sqrt(3), i sqrt(3), -1/2+i sqrt(3)/2).

The first central A is P with these vertices, and the second is Q_j=P_5-P_j. Thus their native sides5 coincide with opposite traversal. Traverse the dimer boundary in the order Q sides0..4 then P sides0..4. The exterior side/handedness states on these ten edges, as read from corona59 states1..10, are

(9,+), (1,+), (8,+), (6,-), (10,+), (9,+), (1,+), (8,+), (6,-), (10,+).

Global native sides0..5 belong to A and6..11 to B. Label these ten incidences0..9. Incidences0 and9 are the same exterior B tile, and incidences4 and5 are another single exterior B tile. Retain labels0,1,2,3,4,6,7,8, together with P,Q.

The exact base checker develops these ten faces and verifies:

- 32 vertices, 41 edges, ten faces;
- 19 shared whole edges, all with matching native edge colors;
- ten triple vertices, with native signed stars precisely among retained indices5,15,20,23;
- every pair sharing a point shares a full edge: there are no vertex-only contacts;
- the other26 tile pairs have a strict supporting-line separation.

All comparisons use exact arithmetic in Q(sqrt(3)); the cyclic sector order is checked by exact cross products. The supporting-line inequalities for all45 distinct tile pairs, native stars at all ten triple vertices, and exact coordinates are retained in the certificate.

## Persistence proof

For small t place P and Q along their common side5. Place each exterior tile along the prescribed boundary side, on the exterior side, with its prescribed handedness. Strict convexity and analytic dependence hold on some neighborhood of zero.

At any ordinary dimer boundary vertex, two exterior tiles and one central tile meet. Their prescribed native angle sum is exactly2pi by one displayed support equation. Their prescribed other incident sides have the same edge color, as verified at the base and fixed by their native labels. Hence those two rays coincide with opposite side traversal, and their equal lengths identify the far endpoints. Thus the two exterior tiles share the same whole edge for every small t, rather than merely touching to first order.

At each dimer seam endpoint the analogous star consists of the two central A tiles and one B tile. The angle equation alpha_A4+alpha_A5+alpha_B3=2pi forces the exterior tile placed from either incident central edge to be the same rigidly placed B tile: it has corner B3 and incident sides3 and4. This justifies the exact duplicate identifications0=9 and4=5 for every small t.

These ten stars account for all the nontrivial gluing cycles: the two central tiles are placed first, each external tile is fixed by one central edge, and every remaining shared edge joins two such exterior tiles at a central-dimer boundary vertex. Thus no unproved holonomy or extension condition is being assumed. The exact base edge table has one central-central edge, ten central-exterior edges, and eight exterior-exterior edges.

Every adjacent pair consequently continues sharing its full edge. Convexity puts their interiors in opposite open half-planes of that edge; the choice of opposite sides persists from the base placement. The26 remaining pairs are disjoint compact polygons with positive separation at t=0, so remain disjoint by continuity. Intersect these finitely many neighborhoods and the convexity neighborhood. This proves a nonoverlapping realization of the entire formal corona for all sufficiently small positive t.

## Replay, evidence, and limitations

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-corona59-base-patch-sol-2026-10-19.py`

Certificate: `research/certificates/hexagon-thirtytwo-corona59-base-patch-sol-2026-10-19.json`. This fixed finite check uses SymPy exact symbolic arithmetic and the retained deterministic formal builder. No solver, numerical tolerance, random seed, or timeout is used. Its finite domain is this one corona and its45 distinct tile pairs. The persistence argument above is analytic and exact; it does not infer an infinite object from a finite search.

A supplementary representative neighboring A/B edge jet check is retained at `research/searches/hexagon-thirtytwo-corona59-geometry-sol-2026-10-19.py` and its certificate. It finds zero first-order gap along their shared edges0/3, in agreement with the exact angle-gluing argument, but the proof does not rely on this supplementary check.

The original **start-of-side** IFT branch fails all32 formal star angle equations after consistent native reindexing; see `research/counterexamples/hexagon-thirtytwo-corona-index-obstruction-sol-2026-10-19.md`. That is a different branch. This corrected positive patch result does not repair or reinterpret the original branch.

Protocol5 boundary: this supplies the missing finite geometric-corona gate for the corrected branch. An unbounded extension mechanism and the exclusion of periodic mixed tilings remain unproved. Enlarging finite coronas alone would not resolve those obligations.
