# Independent hostile review: all-vertex Penrose ordinary Voronoi gate

Date: 2026-10-19. Verdict: **valid**, within the specified retained Penrose source and its rhomb completions, subject to the explicitly imported standard Robinson triangle base-pairing identification. The finite three-cell certificate is independently verified. This is not a solution of research-problem.md, a full congruence census, or a theorem about other site rules.

## Claim and assumptions reviewed

Reviewed research-problem.md, research-protocol.md (especially sections 8 and 11), the three `research/searches/penrose-vertex-dual-gate-sol-2026-10-19` artifacts, the imported center generator, and its retained independent review. The claim is that distinct geometric vertices of the specified unit Penrose rhomb source, with ordinary unweighted Euclidean Voronoi cells, yield at least three incongruent cells. Their genuine side counts are 5, 6, and 7. Each persists in any plane rhomb completion containing this patch.

The standard identification of the triangle recurrence with the Penrose rhomb source, including infinite compatible base pairing, remains imported, as explicitly disclosed by the search report and previous center review. This audit does not promote finite nested inclusion into a standalone proof of that identification. No unrestricted classification of Penrose-like source variants is approved.

## Replay and independent reconstruction

Both commands completed with exit status zero using the required environment wrapper:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-vertex-dual-gate-sol-2026-10-19.py --check
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_penrose_vertex_dual_sol_independent.py
```

The retained reviewer checker imports neither producer, does not call SciPy, and does not use polygon clipping. It independently rebuilds the alternating ten-triangle sun and all five subdivision levels in CyclotomicField(10), verifies exact child area sums, level-one inclusion, opposite-side same-base pairing, all rhomb edge lengths, 430 rhombs, 476 distinct vertices, and edge multiplicities. It reconstructs all three certified polygons directly from exact JSON vectors. For every polygon edge it finds exactly one actual source-site bisector containing both endpoints; these supports are distinct. It checks strict positive turns, distinct vertices, feasibility against all 476 sites rather than only the producer cutoff subset, every squared radius, exact exposed-boundary distances, and nearby-site counts 32, 34, 30.

Thus there is no trust in numerical Voronoi combinatorics or the clipping implementation. A convex polygon feasible for every site inequality and whose every edge is a genuine site support equals the complete finite-site cell: its own supporting halfplanes already define that polygon. This also excludes spurious edges from the producer's initial rectangle.

## Hostile attacks and outcomes

**Arithmetic and degeneracy.** All final proof decisions use exact rational cyclotomic coordinates and real algebraic signs in the specified positive-imaginary embedding. The scaled determinant has positive scaling relative to the Euclidean determinant. Zero determinants, duplicate vertices, redundant collinear subdivisions, and artificial bounding facets were attacked by the independent genuine-support checks. All three cells have genuine nonzero edges and strictly positive turns. The reviewer initially tried Sage generic `abs` on cyclotomic elements in a supplementary area check; it did not implement the required embedding-specific absolute value. Replacing it by exact embedded sign times the element fixed that reviewer-only check. No author artifact required repair.

**Boundary and missing sites.** The independently reproduced squared clearances are

```text
49 + 30*zeta^2 - 30*zeta^3
40 + 23*zeta^2 - 23*zeta^3
43 + 26*zeta^2 - 26*zeta^3
```

Each is strictly above 9. The centers are retained vertices and hence in the rhomb union. Positive distance to its exposed boundary places each in its interior, so its open radius-three disk lies inside the union. Because the patch comes from disjoint actual subdivided triangles paired into rhombs, multiplicity-one edges represent its actual exposed boundary; neither a convex hull nor the outer decagon replaces that boundary in the clearance calculation.

Any source vertex missing from the retained list belongs to some non-retained rhomb. Such a vertex cannot be in the interior of the retained union: its incident rhomb has a positive-angle wedge arbitrarily close to that vertex, and this would meet retained tile interiors. This argument also covers a point lying on a retained internal edge or retained vertex. Thus every omitted vertex is at least distance three from the witness. Boundary equality is harmless.

All certified polygon vertices have squared radius either `1-zeta^2+zeta^3` or `(2-zeta^2+zeta^3)/5`, both strictly below one; convexity gives the same strict radius bound throughout the cell. For an omitted site with displacement d of norm at least 3 and any point x in this cell,

```text
|d|^2 - 2 d dot x >= |d| (|d| - 2 |x|) > 0.
```

Hence no omitted source site can truncate the cell. The all-patch-site check also independently covers retained sites beyond the producer's cutoff. No infinite neighbor enumeration is needed.

**Symmetry and count.** No quotient by symmetry is used. Side count is invariant under translations, rotations, and reflections; three different genuine side counts imply at least three congruence classes. The claim is a lower bound, not exactly three classes. A source symmetry cannot identify these three polygons. The site rule is intrinsic because every source isometry maps the set of distinct vertices to the corresponding vertex set; it uses no choice of incident rhomb or multiplicity.

**Existence and scope.** The recurrence's elementary subdivision preserves each parent triangle: child vertices lie in it, and exact areas sum to the parent area. The standard nested fixed-source construction is discussed in the previous center review. The source-identification dependency remains explicit. The boundary proof establishes robustness under every actual source completion containing this patch; it alone does not assert that every unrelated Penrose source contains the patch. For the specified source, three output types suffice to kill this fixed two-class dual proposal. No periodic omission search, arbitrary tiling decoder, or shape-only forcing theorem follows or is needed for this gate.

## Defects, repairs, and remaining uncertainty

No substantive defect found in the narrow exclusion. No repair to the searched claim was proposed or made. The independent verifier is additional review evidence, not a change to the producer. Remaining uncertainty is confined to the disclosed imported general Robinson/Penrose source identification rather than any finite arithmetic or cutoff claim. The finite result and the conditional completion robustness are valid; the original two-convex-tile research objective remains unresolved.
