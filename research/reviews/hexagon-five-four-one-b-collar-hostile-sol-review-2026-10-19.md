# Independent hostile review: one B collar

Date: 2026-10-19. Verdict: **valid for the exact finite whole-edge B-only collar domain**.

## Claim and dependencies

Reviewed the one-b-collar producer, Markdown statement, and JSON certificate dated 2026-10-19. The claim is that no assignment of one full-edge exterior B neighbor to each of the eight exposed edge orbits of the unchanged longitudinal strips exists without interior overlap. Rows are exactly 15,16,23,26,31. Translation-strip and strip-boundary records supply the explicit six tile orbits and the two four-edge chains. Their prior strip review independently establishes the eight exposed whole edges; this audit does not replace the upstream corona-atlas completeness review.

## Independent reconstruction

The retained verifier `research/reviews/verify_hexagon_five_four_one_b_collar_sol.py` reconstructs native B from the metric certificate and the strip from the ten-tile patch. It uses a different placement formula: writing J for quarter-turn, the map based at a source endpoint is

    x -> a + ((x-s).u)/|u|² d + det ((x-s).Ju)/|u|² Jd.

All six native sides, both endpoint assignments, and both determinants are visited whenever squared lengths agree. A native full edge has exactly these two orthogonal maps for each endpoint assignment; there is no omitted angle or translation parameter. The centroid side selects exterior placements, and the verifier additionally asserts the entire convex polygon lies on that side. This agrees with the producer's all-vertex exterior test. No reflection restriction or native color rejection is introduced.

Interior overlap is checked by interval separation on normals of all sides of both polygons. This differs from the producer's signed support-halfplane implementation. The longitudinal translate range deliberately uses a wider closed projection interval including its floor/ceiling endpoints. Disjoint open longitudinal projections exclude interior overlap, so this contains every possible conflicting translate. Touching intervals and polygon boundaries are permitted. Exact arithmetic is in Q(sqrt(3)); no numerical tolerance appears.

Every retained geometric attachment and every strip-compatibility flag agrees with this independent reconstruction. The counts are respectively (4,3,2,1) twice, (2,2,2,1) twice, (0,2,2,1) twice, (0,2,2,0) twice, and (0,1,2,1) twice. All 576 row15 products and all 64 row16 products fail pairwise attached-tile overlap. The other rows have empty candidate orbits. The certificate reports complete finite failure in every row and completed_all_rows=true; no cap or partial search is interpreted as failure.

## Attempts to invalidate the reduction

Canonicalization subtracts floor(min(x.v)/|v|²) v from the complete polygon, and its key is the sorted exact vertex set. Translating the input by kv changes the floor by k, so the canonical polygon is unchanged. Strict convex polygons have their complete geometric polygon determined by that vertex set. Reflections and cyclic starting slots therefore cannot cause a false distinction. Conversely this key identifies only actual longitudinal translates. The period is nonzero and exactly the retained strip period. No unrelated row or face representative is substituted.

A single B touching multiple required edges is permitted: selecting its canonical polygon at several edge orbits identifies those selections as one tile. Separate attached placements are tested against every longitudinal translate, and every candidate is tested against its own nonzero translates and all original strip orbits. The equal-polygon exception is legitimate identification, not permission for distinct coincident tiles. An attached exterior polygon cannot equal an original strip polygon, since the exposed edge has the original strip on its interior side. No extra incompatibility such as vertex-link completeness is imposed on surviving selections.

A transverse torus period cannot rescue a conflicting pair: the unchanged longitudinally periodic planar packing already contains both overlapping lifted polygons. Quotient identification can only identify exactly equal lifted polygons modulo a period; translating one lift does not remove the other lifts or their intersection. Here no nonoverlapping open collar survives, so area, transverse holonomy, and residual-edge closure are never acceptance tests. No flat torus is claimed.

## Scope attacks and limitations

The declared B-only domain excludes A neighbors explicitly by requiring every exposed edge to meet a whole native B edge. A mixed A/B collar could evade this test. Partial-edge contacts, multiple tiles subdividing an exposed edge, a native B edge extending beyond the exposed edge, endpoint-to-edge contacts replacing full-edge attachment, and contacts along a union of collinear native edges are outside the whole-native-edge domain. Their omission is not an unrestricted geometric obstruction. The Markdown excludes partial-edge placements and unrestricted tiling conclusions; its initial domain requires B neighbors rather than silently deriving their species from lengths.

The domain also retains longitudinal period v and the original strip. A completion whose neighbors break that period, a modified strip, or different metrics is outside. In particular arbitrary plane extensions of this strip are not excluded merely because a v-periodic collar fails. Additional B tiles beyond those chosen cannot remove interior overlaps, but changing the attachment convention can. No search of a second layer or expanded collar domain was performed.

## Defects, repairs, uncertainty

No mathematical defect or required repair was found. The producer deduplicates valid placements while retaining repeated rejected cases; this harmless asymmetry affects neither completeness nor the certificate's geometric case set. Its at-most-24 raw placements bound is conservative. Upstream correctness of the fixed metric and strip certificates remains a dependency. There is no plane existence, nonextension, aperiodicity, or unrestricted periodic-completion theorem here.

Replay completed with PASS for all five rows:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_one_b_collar_sol.py
