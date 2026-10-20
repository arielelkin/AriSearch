# One-chirality Hat Voronoi gate: independent hostile review

2026-10-19. **PASS, scoped; valid under the stated genuine Hat hierarchy existence/occurrence input.**

Reviewed the report, producer and certificate for the two fixed rules retaining respectively the positive and negative determinant sites at native p0=(5/8,5sqrt(3)/8). The claim is that each rule has at least three incongruent ordinary Voronoi cells. This excludes these two rules only; it does not resolve the main construction problem.

## Independent computation

Retained checker: `hat-single-chirality-independent-check-2026-10-19.py`. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hat-single-chirality-independent-check-2026-10-19.py

The checker passed. It imports the retained source geometry/arithmetic module, but never imports or executes the producer and never uses SciPy. It regenerates every level-one H/T/P/F cluster and the depth-three H source. It matches all 1,156 source frames and independently checks that their linear columns are orthogonal and have squared norm 1/4. The factor two therefore restores native Hat size exactly; no assumption of constant proxy-outline inflation is needed.

All eight oriented occurrence rows agree, including reflected parents. The positive-frame counts are H=(22,3), T=(3,1), P=(12,2), F=(14,2), with the two signs reversed under reflection. The checker verifies that each covering assignment includes every constituent Hat once, uses a retained site with the required absolute sign, and bounds all thirteen vertices by the claimed exact maximum strictly below 100. Each assignment uses one fixed site for its entire Hat. Convexity of the closed disk then covers that Hat, including its concave parts. Reflection preserves distances while reversing the determinant selection. This is a uniform hierarchy argument, not a finite-patch density extrapolation.

The checker independently cancels transformed primitive kite edges, recomputes exact distances to all exposed segments, and matches each recorded minimum strictly above 400. It recomputes every cutoff neighbor list using exact squared distances at most 400. Starting with the radius-10 disk's containing square, it independently clips by every neighbor halfplane using exact Q(sqrt(3)) segment intersections. Its resulting vertex sets and exact shoelace areas agree with every certificate cycle. All vertices have squared radius strictly below 100. Its invariants are:

| sign | Hat | sides | area/sqrt(3) |
|---|---:|---:|---|
| -1 | 510 | 6 | 4233954347/81711360 |
| -1 | 518 | 6 | 596323597/9467064 |
| -1 | 514 | 6 | 99383642899633/1726465308288 |
| +1 | 519 | 5 | 23484642059/3199878312 |
| +1 | 508 | 7 | 1359041891/158138064 |
| +1 | 516 | 7 | 3064090381/282983904 |

## Hostile checks and assumptions

Attacks considered: reflected parents losing the retained sign; changing the assigned site from vertex to vertex; incorrect half-size source normalization; confusing the overlapping construction patch with a genuine supertile; idealized outline clearance concealing actual missing Hats or holes; omission of infinite-source sites; floating-point facet mistakes; redundant or zero-length sides; and area equality under reflections. No unresolved defect was found.

The producer's primitive-grid predicates are sound: all kites are standard faces of one common hex-center lattice, with distinct sector centroids and edge multiplicity at most two. Thus cancellation gives the actual union boundary, including holes; it does not rely on a proxy metatile outline. Native kite decomposition and source recurrence were also addressed in the retained earlier existence-gate hostile review. The present independent checker reuses the geometry module and does not independently re-prove its field arithmetic or published substitution theorem.

For a target in its own Hat interior, clearance greater than 20 to every actual boundary segment implies that its closed radius-20 disk is in the union. An omitted site's intrinsic point is interior to its omitted Hat, whose interior cannot overlap this union in a genuine source tiling. Such a site is consequently outside that disk. Global radius 10 follows from the oriented finite covers throughout the hierarchy. Every Voronoi cell lies in the radius-10 site disk, so sites farther than 20 cannot trim it. Exact clipping also places every certified vertex strictly inside radius 10, eliminating any artificial square boundary. The producer's strictly positive consecutive cross products establish genuine sides. Three unequal area/side-count pairs for each sign give three incongruent cells, including congruence with reflection.

The depth-three H patch must occur in an infinite legal source; finite disjointness alone does not prove extension. The report explicitly imports the genuine hierarchical Hat theorem and occurrence input, consistent with the retained source provenance and earlier source audit. This dependency remains an assumption of this scoped result and is not transferred to arbitrary Voronoi tilings.

Defects found: none. Repairs made: none to author artifacts. Remaining uncertainty: published hierarchy/occurrence input and retained exact arithmetic are trusted dependencies. Verdict: **valid, scoped PASS**.
