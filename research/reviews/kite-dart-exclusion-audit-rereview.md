# Fresh rereview of the kite/dart bounded exclusion audit

Date: 2026-10-11. Verdict: **VALID within the stated marked-source,
normalized graph and varying-angle-family domain**, conditional on the
recorded exact algebra/SMT checks and the usual mathematical correctness
of Sage/Singular and Z3. This reviewer developed neither the P2 exclusion
nor its first audit. This is not an exclusion of isolated two-class
specializations rejected only by algebraic dimension, arbitrary unmarked
kite/dart tilings, or larger attachment families.

Reviewed [audit report](kite-dart-exclusion-audit.md), its three scripts,
the source, primal and algebra certificates, and relevant producer
checkpoints. No full rerun of the 9,604 pair census or 660 ideal computations
was needed; the checks below specifically address the remaining proof
gaps.

## Four no-bounded-face templates

The local leaf obstruction is valid. Independently reconstructing the
incident sectors from cyclotomic patch coordinates finds exactly 25
complete dart-2/kite-1/kite-3 stars in patch3 and 90 in patch4. Their sectors
occupy 6, 2 and 2 consecutive angular units respectively and partition all
ten units without overlaps or gaps. These are genuine complete source
stars, not truncated stars at the finite patch boundary.

Independently reading the decoration graph gives no edges for type zero,
and exactly one edge incident with dart corner 2 for each of types 54,
1 and 3. Strict interior-node conditions or distinct fixed source corners
make that segment nonzero. The two kites are undecorated. Consequently
the retained boundary graph near this source vertex has exactly one ray.

A locally finite tiling by finite convex polygons cannot have a degree-one
boundary vertex. Each incident polygon boundary entering the vertex must
leave it along another nonzero ray. A sole ray instead leaves a slit,
whose complementary angular neighbourhood is connected through all other
directions; it cannot be the boundary corner of a convex polygon.
The wholly empty graph cannot produce finite complementary polygons.
Thus all four templates are excluded, without assuming that a bounded
face occurred inside the finite sample. This uses the declared domain in
which retained decoration segments are actual polygon boundaries. Discarded
or degenerate segments change the normalized graph and must be treated as
another enumerated template.

## Legal occurrence of the source patch

Independently replaying eight alternating halfsteps in the exact
cyclotomic field confirms that all ten certificate sun triangles occur
inside one acute half-tile supertile. Their coordinates are exactly
the five-kite sun under one direct similarity, and all their vertices
are strictly inside that supertile.

Containment plus equality of total child areas alone would not prove
absence of overlaps in a general subdivision. The actual two-child rules
have a stronger elementary justification: the new point lies strictly
inside one parent side, since the coefficients \(1/\phi,1/\phi^2\)
are positive and sum to one; joining it to the opposite vertex splits
the parent triangle into the two stated triangles. The children have
disjoint interiors and cover the parent. Single-child halfsteps preserve
the triangle. Thus the exact subdivision is valid.

As an additional direct check, this reviewer generated a single acute
half-tile supertile through fourteen halfsteps, producing 987 labelled
triangles. **All 190 half-triangles of the actual 95-tile patch3 occur
among them**, with their labels and ordered coordinates agreeing under
\[
 z\longmapsto c+u z/\phi^3,
\]
where \(c,u\) are the stored sun centre and axis vector. This checks the
actual recorded patch identity, beyond merely observing that the sun and
producer use the same subdivision rules.

The recorded four-state type/chirality substitution matrix has a strictly
positive square, checked independently. Every sufficiently high
supertile therefore contains an acute supertile large enough to contain
patch3, up to a source isometry. At a fixed such order, diameters are
uniformly bounded. Any sufficiently large disk realized in a larger
supertile contains a full sub-supertile of this order: take the one
containing its centre, whose entire diameter lies in the disk. This gives
the claimed bounded-gap occurrence in the substitution-language hull
without requiring a recognizability theorem or extending the claim to
arbitrary bare kite/dart geometry.

## Bounded-face and algebra stages

A targeted read-only replay of the auditor's retained-component checker
rebuilt all 18 survivor rows. It verifies **1,194 bounded faces** and their
recorded class metrics/counts. This matters because the later congruence
stages must operate on actual retained components and complete class
lists. The execution record has now been repaired to retain this count.

The full-distance congruence criterion, cyclic/reversed correspondences
for convex polygons, positive-dimensional necessary gate, pentagon
straight-corner periodic escape, and joint-partition coverage are
mathematically appropriate. The first audit independently rebuilt their
coordinates and computations; this rereview checked their implementations
and evidence rather than repeating every ideal.

For the weakly convex hexagon flat cell, opposite signed-turn polynomials
force the stated three flat vertices. The separate extra-zero UNSAT
query makes the deleted-vertex pattern exhaustive under the necessary
interior and five-genuine-corner conditions. The remaining three
pentagons must all be one shape, and both hexagons the other. The
certificate's ten congruence ideals for pentagons 0 and 3 all have dimension
-1, so no correspondence is possible, including isolated points of that
cell. The exact source reflection and full-metric mirror map transfer
this result to the other hexagon pattern. The old incomplete direct
enumeration therefore need not be silently relabelled complete.

No excluded zero-dimensional ideal can support a continuous angle-varying
family. Conversely, algebraic dimension alone would not establish a real
family or a varying angle; the audit makes no such positive claim.

The source-language scope and all remaining engine-trust and isolated-locus
limitations in the first audit are appropriate. The global two-convex-tile
problem remains unresolved.
