# Independent hostile review: weighted Penrose-center first gate

Date: 2026-10-19. Verdict: **valid for the stated fixed-source parameter interval**, with the same explicitly imported standard Robinson/Penrose base-pairing dependency as the reviewed unweighted source. Outside that interval the weighted family remains open. This is not a resolution of the main research problem.

## Claim and audit boundary

Reviewed `research/searches/penrose-weighted-center-first-gate-sol-2026-10-19.{md,py,json}`, the unweighted source and its hostile review, `research-problem.md`, and the research protocol, including §§8, 11 and 19. The claim is that the index-23 cell is an actual complete strict convex quadrilateral for every real delta in [-1/4,1/4+phi/3), under power |x-c|²-weight(c), with thin weight zero and thick weight delta. A proposed pair containing every resulting cell class consequently admits a periodic tiling by this quadrilateral alone.

The independent checker is `research/reviews/verify_penrose_weighted_center_sol_independent.py`. It imports neither producer. It rebuilds the substitution, pairing and centers in the real field Q(sqrt(5)), representing points as coordinate pairs with metric x²+((3-phi)/4)y². It consumes the claimed affine vertices rather than trusting their construction. This is a separate arithmetic and validation path from the producer's cyclotomic intersections and Bernstein turn test.

Both exact replays completed successfully:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-weighted-center-first-gate-sol-2026-10-19.py --check
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_penrose_weighted_center_sol_independent.py
```

## Hostile checks and findings

1. **Weight sign and geometric type.** Expanding |v|²-w(c) <= |v-(q-c)|²-w(q) gives 2(q-c)·v <= |q-c|²+w(c)-w(q), exactly the producer's sign. Independent reconstruction checks unit apex edges and base squared lengths 2-phi for color zero and 1+phi for color one on every triangle. Base-paired color-zero rhombs therefore have acute angle 36 degrees and are thin; color-one rhombs have acute angle 72 degrees and are thick. Index 23 really has type zero. No swapped rhomb types or reversed power convention was found. The 430 centers are distinct.

2. **Finite domain and exact interval.** All four affine vertices satisfy all 430 site inequalities at both endpoints, independently checked: 1720 affine residuals, including harmless self inequalities. Affinity makes these endpoint checks sufficient on the entire closed interval. Independently computing all nonconstant residual roots recovers exactly [-1/4,1/4+phi/3], including the claimed limiting vertex/site pairs. The finite interval is maximal for these prescribed affine vertices and supports; it is not asserted to be the maximal quadrilateral interval for the actual cell under changing supports.

3. **Actual cell rather than contained polygon.** For each of the four prescribed supporting sites, both endpoints of its corresponding edge satisfy its power line identically as a function of delta. The four cyclic turn polynomials are positive at the lower endpoint and throughout the interior, independently checked by their exact quadratic minima, with nonnegative upper-endpoint values. Hence the affine polygon is a strict convex quadrilateral with four genuine support sides throughout the half-open interval. Its four support halfplanes intersect in precisely that polygon. Since it also satisfies every other finite halfplane, the full finite-site cell equals the polygon. This closes the otherwise possible gap between a feasible quadrilateral and an actual complete cell.

4. **Endpoints and degeneracies.** The lower endpoint has four distinct vertices and four positive turns. Sites 27 and 71 touch vertex 2; their extra equalities do not remove any side or produce a zero angle. The included lower endpoint is therefore valid. At the upper endpoint affine vertices coincide and strict quadrilaterality fails. Excluding it is necessary for this certificate. The upper parameter lies below one and the lower parameter above minus one, verified exactly.

5. **Whole-plane source and collar.** Independently checked the 20 labelled level-1 triangles occur in level 5, the 890 level-5 triangle count, genuine opposite-apex same-color base pairing, all unit rhomb sides, and placement of every unmatched base on the outer decagon. The nested-source implication follows the reviewed unweighted proof: apply deterministic inflation-subdivision four times to each inclusion; the growing supports exhaust the plane. The standard infinite Robinson/Penrose base-pairing property remains an imported named-source dependency, not something inferred solely from level 5. The independent exposed-edge distance minimum is exactly 7+37phi/4 > 9. Since c is interior to its rhomb, B(c,3) lies inside the union of the retained rhombs. Any omitted genuine rhomb has disjoint interior and its center is interior to itself, so its center has distance at least three. There is no missing rhomb-radius subtraction in this argument.

6. **Uniform infinite tail.** Independent endpoint checks give |v_k|²<1 for every vertex. Convexity of squared norm extends this to all affine parameters in the closed interval; convexity of the polygon extends it to every cell point. For an omitted center at distance D>=3, and |delta|<1, the slack in the doubled power inequality is strictly greater than D²-2D-1, which is at least 2. This applies uniformly to every omitted site and every parameter under review, including negative weights. It proves the actual infinite-site cell and does not extrapolate from a finite patch size.

7. **Periodic omission and quantifiers.** Each resulting strict convex quadrilateral has the standard periodic tiling by itself using half-turn mates. The problem explicitly permits omitting a species, reflections, and unrestricted contacts; orientation-preserving copies already suffice for this witness. Consequently any proposed two-shape protoset containing every cell class of this specified source fails unrestricted aperiodicity. No census of other cell classes is needed for that implication. This neither establishes that there are exactly two output classes nor excludes a different selection of output shapes, a different rule, or parameters outside the interval.

## Defects, repairs and remaining uncertainty

No substantive defect or repair was required. Producer and independent checker both passed with assertions enabled. The exact certificate and interval are approved subject to the already disclosed standard source dependency. No new historical or novelty claim is reviewed here. Protocol §19 does not convert this bounded first gate into a reason to declare the main problem solved or the weighted family globally excluded: delta<-1/4 and delta>=1/4+phi/3 remain unclassified, and any surviving two-class candidate would still require a complete census and unrestricted shape-only forcing proof.
