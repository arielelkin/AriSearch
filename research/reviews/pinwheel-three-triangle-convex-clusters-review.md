# Independent hostile review of pinwheel three-triangle convex clusters

Date: 2026-10-13. Verdict: **valid** in the stated finite domain.

Reviewed producer `research/searches/pinwheel-three-triangle-convex-clusters.py` and retained certificate. Independent verifier: `research/reviews/pinwheel-three-triangle-independent-check.py`, with no producer imports.

## Domain completeness

The domain consists of unions of exactly three congruent right triangles with squared side lengths 1,4,5 and connected whole-side adjacency. Fixing one triangle by an arbitrary isometry loses no congruence class. Every connected three-vertex adjacency graph has a rooted spanning tree, so the triangles can be added in an order with each new one sharing a whole side with an earlier one. For each side, the three distinct native side lengths determine which native edge is attached. Its two endpoint correspondences give exactly two copies on the unoccupied side, including reflection and rotation. The producer's reflection and half-turn alternatives exhaust these two possibilities.

The independent checker instead reconstructs placements from all native vertex permutations and rational edge-projection/normal coordinates. It recovers all raw counts 1,6,36. The producer checks interior disjointness but does not explicitly check other contacts are edge-to-edge. I therefore checked every pair in every retained raw three-triangle patch for a vertex in another side interior: all 36 raw patches are edge-to-edge. Thus no domain leak changes this computation. This absence is specific to this finite domain and should not be assumed for larger clusters.

Convexity is tested exactly: the three tiles have total area 3 and disjoint interiors. Equality of convex-hull area to 3 implies their closed union equals the hull, because a missing point in its interior would leave an open positive-area hole, and the boundary follows by closure. The independent checker recovers exactly five convex classes, four quadrilaterals and one pentagon.

## Congruence and certificates

A complete squared-distance matrix determines a finite planar point configuration up to Euclidean isometry. For convex hulls its permissible vertex correspondences are cyclic shifts and reversals, so the producer canonicalization is complete for rotations and reflections. The independent verifier uses all vertex permutations instead and finds exactly the same five classes. Every certificate triangle is independently checked for area 1, squared edge lengths 1,4,5, interior disjointness, edge-to-edge contacts and exact hull boundary. All supplementary indices are recomputed from boundary vectors.

## Explicit periodic pentagon escape

The unique pentagon is P=((0,0),(6/5,-8/5),(2,-1),(2,0),(0,1)). Its consecutive corners at (2,0),(0,1) sum to pi, because the incoming edge at the first and outgoing edge at the second are opposite vertical vectors. Reflect P by a half-turn p -> (2,1)-p about their common side midpoint. The two pentagons are interior disjoint and exactly form the centrally symmetric convex hexagon

    H=((0,0),(6/5,-8/5),(2,-1),(2,1),(4/5,13/5),(0,2)).

It has area 6. Translation vectors v=(2,-1), w=(4/5,13/5) have determinant 6. To verify lattice packing independently, the checker transforms H into this lattice basis. Any intersecting translate must have integer coefficients within the exact coordinate ranges of H-H; it checks every such nonzero candidate by exact polygon separating axes. All are interior-disjoint. The equal area and determinant then imply covering: the lattice-periodized closed locally finite union occupies full area in the fundamental torus; any uncovered point would leave an open positive-area gap. Splitting every translated H into its two P tiles gives an unrestricted periodic monohedral P tiling. No pentagon classification import is needed.

## Scope

This proves the stated three-triangle connected full-side convex-cluster census and kills the pentagon as an aperiodic prototile. It does not prove completeness for clusters with partial contacts or more than three triangles, and does not prove that every pinwheel recomposition is periodic.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pinwheel-three-triangle-independent-check.py
