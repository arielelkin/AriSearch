# Independent hostile review: pinwheel common affine center / midpoint cells

Date: 2026-10-19. Reviewer: fresh Sol worker, independent of the producer. Verdict: **valid, restricted to the stated finite patch and common interior center rule**. No target solution is certified. The existence of an infinite source containing this patch is not established here and is not needed for this verdict.

## Claim and assumptions

Reviewed `research/searches/pinwheel-barycentric-crossboundary-2026-10-19.md`, its producer and centroid/fifth JSON fixtures, the center-family producer/JSON, and both supplied check scripts, against `research-problem.md` and protocol §§8,11,19. The claim is that the given depth-three 125-triangle patch, planarized at every source vertex, cannot have all convex midpoint/corner-star cells for any single pair p>0, q>0, p+q<1 used in the right/long/short affine frames of every source triangle.

This review preserves a separate reconstruction in `research/reviews/pinwheel-barycentric-center-family-hostile-sol-check-2026-10-19.py`. It imports neither producer, nor source coordinates or symbolic triples from the family certificate. It constructs the five normalized children directly from the stated integer source coordinates, applies the right/long/short affine frames recursively, and derives the cell boundaries from planarized face cycles. Fixture comparison happens only after reconstruction.

## Geometry and boundary order attacks

The reconstructed 125 rational triangles lie inside T, have pairwise disjoint interiors by exact separating-axis checks, and have total area 1, equal to T. Each retains squared-leg ratio 4 and a right angle. Thus no gap or overlapping source interior is hidden in the finite substitution patch. The frames can reverse orientation: that is handled by orienting each geometric face counterclockwise after subdivision; long and short endpoints are assigned by exact squared length, never by storage order.

Every edge is split at every source vertex lying on its closed segment. Concatenating these oriented split edges gives a face cycle, including the formerly flat T junctions. At a vertex v, each incident face supplies the oriented boundary arc (outgoing segment midpoint, face center, incoming segment midpoint). Exact checks establish one incoming and outgoing arc at each seam and a single cycle containing every incident face. There are 81 fully interior vertex cells. This reconstructs the claimed raw indexing with the least midpoint as cycle start.

For an interior center, each face sector is partitioned by segments from that center to successive boundary split vertices/midpoints. The arcs run inside separate face interiors; midpoints glue across adjacent faces. Distinct centers cannot coincide since they lie in disjoint triangle interiors. Centers cannot equal seam midpoints. Distinct radial seam points cannot coincide after planarization. Consequently the assembled cell is a simple, counterclockwise corner-star boundary for the entire parameter domain. A convex cell therefore requires every raw turn to be nonnegative. Retaining collinear raw vertices cannot invalidate this necessary condition. At the fixed centers, the checker additionally verifies that every removed zero-turn vertex lies between its neighbors, excluding an illicit removal of a backtracking spike.

## Decisive symbolic test

Direct reconstruction gives the consecutive signed determinants

| Source vertex | Raw index | Turn |
| --- | ---: | --- |
| (1/25,2/25) | 0 | F/125 |
| (1/25,2/25) | 2 | G/125 |
| (1/25,22/25) | 6 | -G/125 |
| (1/5,1/5) | 4 | -F/125 |

Here F=-4p²+3p-q²+q/2 and G=-4p²+p-q²+q/2. These are symbolic identities in independently derived coordinates. Convexity of all cells implies F>=0, -F>=0, G>=0, -G>=0, hence F=G=0. Since F-G=2p, p=0 follows, contradicting p>0. This argument includes weakly convex boundaries and every exceptional interior parameter value. It does not rely on strict-turn tests, generic position, numerical sampling, or the Z3 result. Moving to p=0 changes the specified interior-center construction and is outside the claim.

## Fixed fixtures, congruence, and replay

Independent reconstruction matches every centroid and fifth fixture cell up to cyclic shift and reversal of its full squared-distance matrix. Centroids give 81 cells, 50 convex, 31 nonconvex, and 3 congruence classes among the convex subset. Fifth centers give 81 cells, 40 convex, 41 nonconvex, and 2 classes among the convex subset. Full pairwise squared distances, minimized over polygon cyclic shifts and reversal, correctly classify these simple convex boundaries up to Euclidean isometry, including reflections. Equal adjacent side lengths alone were not used. These class counts apply only to the convex subset of the finite patch; neither count supplies a two-prototile construction.

Both supplied independent checks passed. The minimal centroid T-star has the reported reduced pentagon and turns 110,45,-10,90,120. Both fixed-center producers replayed successfully with the counts above. The family producer completed UNSAT for 465 nonidentically-zero turn constraints (Z3 4.16.0, configured 30000 ms timeout), retaining the stated six core entries. The four-identity algebra, independently verified, carries the proof rather than that solver core.

Commands all used the repository environment wrapper. Replay each suffix below after `mise exec -- conda run --no-capture-output -n arisearch`:

```
python research/searches/pinwheel-barycentric-crossboundary-2026-10-19.py
python research/searches/pinwheel-barycentric-crossboundary-2026-10-19.py --center fifth
python research/searches/check-pinwheel-barycentric-crossboundary-2026-10-19.py
python research/searches/pinwheel-barycentric-center-family-2026-10-19.py
python research/searches/check-pinwheel-barycentric-center-family-2026-10-19.py
python research/reviews/pinwheel-barycentric-center-family-hostile-sol-check-2026-10-19.py
```

The independent reconstruction completed with all assertions passing. The finite domain is the deterministic depth-three patch and all its interior planarization vertices; no symmetry reduction or random seed is involved. Exact Fractions determine all incidence, order, separation, collinearity and fixed-center signs; SymPy checks polynomial identities.

## Defects, repairs, and remaining scope

No mathematical defect was found in the scoped obstruction, and no repair to its proof was needed. The supplied family checker alone verifies certificate triples rather than source incidence; the independent reconstruction in this review closes that verification dependency. The supplied minimal checker does not verify all patch counts; this review independently checked all of them.

The possible nonextension of the finite source patch cannot defeat the finite-patch theorem. It would, however, defeat any unsupported universal assertion that every infinite pinwheel source must contain these stars. The report correctly claims only that an infinite source *containing this patch* is excluded. No existence, recurrence, recognizability, or global occurrence theorem for the source is certified here. Arbitrary locally legal sources, alternative substitutions, changed seam rules, and environment-dependent center choices remain outside this result.

Final verdict: **valid** for the explicit finite-patch common-interior-center exclusion and the reported finite fixture counts. **Unresolved** for the main two-convex-unmarked-tile problem and any stronger exclusion of all source tilings without a separate patch-occurrence argument. No discovery-log or git operation was performed.
