# Independent audit of the first kite/dart exclusion

Date: 2026-10-11. Status: **bounded exclusion independently audited; the main problem remains unresolved**.

The requested four templates are discharged. The completed negative result applies to the marked alternating Lang–Hayes P2 substitution source and the stated uniform decoration domain. It is not an exclusion of all two convex tiles, all Penrose recompositions, or all unmarked kite/dart tilings.

## Exact domain

Each labelled source kite or dart receives the same straight-line embedded graph on its four corners and at most two distinct strictly interior nodes. Edges join corners to interior nodes, join the two interior nodes, or are source diagonals. All original source edges are erased; final tiles are the complementary faces. There are no source-edge interior endpoints, preserved source edges, conditional local-neighbour rules, or extra interior nodes. Coordinates are exact and rotations/reflections of final shapes are unrestricted. The requested construction route requires a continuous angle-varying family, rather than an isolated specialization.

Interior decoration vertices of degree one cannot be vertices of a polygon-boundary tiling; degree-two vertices must be straight and can be suppressed. A crossing of the two diagonals must be made an interior node, so the direct unsplit two-diagonal graph is correctly omitted; the subdivided crossing is represented among the spoke graphs. Interior cycles without a source corner would require at least three interior vertices. With this budget and normalized graphs, the embedded pieces have simple boundary cycles. The nonconvex dart admits fewer geometric embeddings than the abstract source disk: enumeration is a superset, and each rejection is conditional on the recorded embedding being realized with nonzero decoration edges. Degenerations that change graph incidence must be normalized as another graph in the census, rather than silently retained in an invalid embedding.

A new permutation-of-darts census, using face-cycle canonicalization rather than the producer's edge/rotation canonicalization, enumerated 184 accepted labelled rotation systems. Quotienting by interior-node interchange gives exactly the same 98 types. Every one of the 9,604 ordered source-type pairs has a recorded checkpoint row.

## Primal witnesses and four previously unresolved templates

A separately written checker validates all 9,586 rejected rows. For each recorded witness it proves the source pieces form a connected full dual component, verifies that component avoids the patch boundary, rebuilds its decoration boundary, and checks the stated slit, repeated boundary vertex, multiple boundary cycle, fixed reflex turn, or at-most-four-corner diagnosis. Identically straight vertices are suppressed by verifying real constant proportionality of the full affine edge forms; this does not invoke the producer's formal cross-product test. The independent checker also rebuilds all bounded components in the 18 retained rows and verifies the entire recorded full-distance polynomial class/count census: 1,194 bounded faces, with no missing, spurious, or incorrectly normalized representative. Counts agree: 8,096 triangle/quadrilateral escapes, 832 slits, 364 pinches, 277 multiple cycles, and 17 fixed reflex corners. A triangle or convex quadrilateral supplies a periodic tiling using that shape alone, which the problem explicitly permits.

The four undecided pairs were `(0,0)`, `(0,54)`, `(0,1)`, and `(0,3)`. Type 0 is empty; type 54 is the dart diagonal 0–2; types 1 and 3 respectively have interior spokes to corners {0,1,2} and {0,2,3}.

There is an exact closed source star consisting of dart corner 2, kite corner 1, and kite corner 3. Its sectors measure 216°, 72°, and 72°, and partition all ten angular units of π/5 without overlap or a gap. Patch3 has 25 such stars; patch4 has 90. The two kites contribute no decoration ray. Each of the three nonempty dart templates contributes exactly one nonzero ray at corner 2. Thus the erased-source boundary graph has a degree-one vertex. The boundary union of a tiling by finite convex polygons cannot have a leaf: every polygon boundary reaching that point must continue along a second ray, or otherwise reverse along the sole ray and fail to bound a polygon interior. This rules out each nonempty template, independently of whether a bounded complementary face happened to fit inside the finite patch. The empty graph of `(0,0)` also cannot partition the plane into finite polygons. These four obstructions exclude isolated parameter values as well as families within the valid graph domain.

## Why the finite source patch is relevant

A separate direct subdivision implementation verifies child containment and exact area partitions, without importing the producer's builder. It finds the original ten-triangle five-kite sun **strictly inside one acute half-tile supertile after four P2 deflations**. The ten labelled triangles equal the original sun seed up to one direct similarity. Continuing the same subdivision for three further deflations contains the recorded patch3 after its incomplete boundary halves are removed; normalizing final source edges makes that similarity an isometry. Thus the patch is legal in this particular marked substitution language, rather than merely an arbitrary assembled seed.

For two-halfstep subdivision, the matrix on acute/obtuse half-tile types with their two orientations is

```
1 1 0 1
1 1 1 0
1 0 1 0
0 1 0 1
```

Its square is strictly positive. Consequently every sufficiently high order supertile contains an acute half-tile supertile large enough to carry this sun and then patch3, up to a source isometry. A fixed sufficiently high supertile order has uniformly bounded diameter. Any legal disk substantially larger than that diameter, when realized in a still larger supertile, contains a whole such sub-supertile. This gives a uniform bound on the gaps between occurrences in every tiling of the substitution-language hull. Source reflection permutes the labelled graph census, which is closed under that permutation; the negative result covers both orientations. This is a source-hull statement, not a claim that arbitrary tilings by bare kite/dart geometry satisfy the marked substitution language.

## Convexity, arbitrary congruence, and straight-vertex loci

An independent real-coordinate encoder writes a source point as `s+t*w` and uses `w²=phi*w-1`. It rebuilds signed-turn, positive-area, nonzero-edge, strict-source-interior, distinct-node and at-least-five-genuine-corner constraints. It reproduces all ten decisive weak-convexity UNSAT exclusions among the fourteen bounded-face survivors. The surviving categories are the two five-hexagon patterns and the two seven-pentagon patterns. One independent weak pentagon query timed out; no exclusion relies on that query because the algebraic congruence gate handles both pentagon patterns.

Full squared-distance matrices characterize congruence of nondegenerate planar vertex configurations under arbitrary isometries. For convex polygon boundaries without redundant vertices, every allowed vertex correspondence is one of the cyclic shifts or reversals that the metric stage enumerates. Using separately reconstructed coordinates, the audit rebuilds all 660 congruence ideals and exactly matches every recorded Gröbner basis and dimension. The statuses are 324 unit ideals, 12 zero-dimensional loci, 304 positive-dimensional necessary survivors, 18 fixed-exterior-node loci, and 2 forced-degeneracy loci. Unit, zero-dimensional, forced-zero-edge, and fixed-exterior-point exclusions are valid necessary conditions for the requested continuous family. Dimension here is complex algebraic dimension, so retaining a locus does not establish real feasibility or angle variation.

For each hexagon pattern, an independently checked incompatible triangle of face classes excludes two congruence classes when no corners are deleted. For both seven-pentagon patterns, the audit replays all 128 partitions into at most two classes with an independent Cartesian recursion over pair ideals and **weaker** pruning than the producer: only nonpositive dimension or forced degeneracy is removed at combination steps. No locus survives. A pentagon losing a genuine corner would have at most four corners and supplies the already-applied periodic escape, so that finishes the pentagon patterns including straight specializations.

For hexagon pair `(3,1)`, opposite weak-turn polynomials force zero turns at class/vertex indices `(0,4)`, `(3,2)`, and `(4,0)`. An independently encoded, stateful SMT query proves that adding any further zero turn is impossible under the necessary interior and five-genuine-corner conditions. Deleting exactly those three vertices gives side counts `[5,6,6,5,5]`. Every two-class partition must identify all three pentagons and identify both hexagons. For pentagon classes 0 and 3, **all ten arbitrary-isometry congruence ideals, including the forced flat equation, are unit ideals**. Therefore the flat cell admits no two-class realization even at isolated coordinates. The audit independently verifies the full distance-polynomial mirror map from `(1,3)` to `(3,1)` and the reflection `z -> w²*conjugate(z)` preserving each source polygon. The incomplete direct enumeration of `(1,3)` is therefore safely replaced by the completed mirrored exclusion; its timeout remains recorded as a timeout.

## Verdict and retained limitations

Within this uniform ≤2-interior-node, erased-source-edge, marked-substitution domain, every normalized template is either geometrically incompatible with convex polygon tiling, has an admitted monohedral periodic escape, or cannot yield at most two shapes in a positive-dimensional parameter family. The four no-bounded-face templates are now excluded by local boundary-graph obstructions. No new endpoint search is needed to fill a hole in this specific campaign.

The audit is independent at the enumeration, primal-witness, coordinate/SMT encoding, and congruence-partition implementation levels. It shares Sage/Singular and Z3 with the original computation. SMT files are replayable exact rational/algebraic encodings, but there are no formally checked Z3 UNSAT proof certificates or proof-assistant verification of Singular arithmetic. Isolated two-class specializations outside the requested varying-angle route remain unsearched where the algebraic gate rejected only zero dimension. Larger attachment graphs, boundary endpoints, retained source edges, and neighbour-dependent rules remain outside this result. The global two-convex-tile problem remains unresolved.

## Replay

```
conda run --no-capture-output -n arisearch python research/reviews/kite-dart-exclusion-audit.py --output research/certificates/kite-dart-exclusion-audit.json --timeout-ms 15000
conda run --no-capture-output -n arisearch python research/reviews/kite-dart-exclusion-audit-source.py
conda run --no-capture-output -n arisearch python research/reviews/kite-dart-exclusion-audit-algebra.py
```

The algebra audit consumes the independently generated SMT file for `(3,1)`, so run the first command before it. The strengthened primal/SMT/retained-face check took 33.062 seconds; the embedding/source census took about 7 seconds and metric/joint/flat checks about 19 seconds. This host is adequate for these bounded audits; unbounded reconstruction and Gröbner growth are different workloads.
