# Independent hostile review: pentagon / 144–126 heptagon

Reviewed 2026-10-19 against research-problem.md and research-protocol.md §§8,11,19. Reviewer did not develop the candidate. Scope is the exact local claims in `research/searches/regular-pentagon-heptagon-144-126-first-gate-sol-2026-10-19.{md,sage,json}`.

## Analytic audit

**Valid.** Dividing angles by 18 reduces the full-vertex equation to 6p+8a+7b=20, whose nonnegative solutions are (2,1,0) and (1,0,2). The straight-angle equation has right side 10 and no solution involving corners. At a tile corner, one edge-interior sector would consume 180 degrees and leave this impossible sum; two such sectors leave no room for the corner. Thus no T junction occurs. Finite positive-area prototiles ensure local finiteness, so this argument applies to unrestricted tilings. A partial collinear side contact would terminate at such a junction, so every shared side is full on both tiles.

There is a unique cyclic word with one A and six B. At A both Q sides face P. At B exactly one Q side faces Q. Hence QQ edges form a perfect matching of the six-vertex B path, uniquely edges 1,3,5; the four other edges have the unit pentagon length. This is derived from geometry, not an imposed matching decoration. The angle equation excludes each monohedral tiling, but gives no mixed-periodic obstruction.

Writing the three free lengths x,y,z, closure is two independent real equations: directions u1 and u3 are nonparallel. The displayed particular solution (t,t,t) and null vector (1,k,1), with t=2cos18 and k=2cos72, therefore exhaust the metrics. Since 0<k<1, positivity of t+h and t+kh is exactly h>-t. The JSON expression h>max(-t,-t/k) is equivalent, not a differing domain. Equal lengths force (1-k)h=0, so h=0 uniquely.

Convexity needs closure as well as positive turns. Here closure is exact and all successive exterior turns are 54 degrees except the closing turn of 36 degrees; their sum is 360 degrees. The standard closed, positive-length, locally strictly convex chain criterion gives a simple strictly convex polygon. Equivalently, for a fixed edge the cross-product increments along the remaining cyclic edge directions first have positive and then negative signs, ending at zero by closure; all intermediate vertices lie strictly on its left. This also rules out a self-intersecting interpretation of the family.

## Finite computation audit

The independent companion review checker reconstructs coordinates using QQbar.zeta(20), then converts vertices to AA and tests intersection dimension with Sage Polyhedron. It does not import the original script or reuse its separating-axis overlap function. It checks the five base tiles, all 18 individual joins against the base, and all 108 cross-target placement pairs required by the 216 triples; it compares the surviving triple list with the retained JSON.

Across a fixed target edge there are exactly three equal-length source QQ sides and two isometry parities. The two endpoint maps in the search put the new polygon outside the central one: orientation preserving reverses endpoint order; orientation reversing preserves it. These exhaust isometric full-edge attachments. A regular pentagon has only one outside geometric placement across a unit side, including reflection. Thus four P positions are forced. No partial contacts introduce additional immediate edge-neighbor choices after the unrestricted-contact reduction. Duplicate options need not be quotiented out; coincident distinct tiles have two-dimensional intersection and would fail either overlap engine. Additional incidental boundary contacts are permitted by both tests. In the stored representative contact computation every collinear boundary interval has endpoints among vertices of at least one polygon, so checking both vertex-to-edge directions records those endpoints.

All 216 triples constitute exactly the complete domain of simultaneous Q tiles across the central Q's three QQ sides at h=0. This is not the domain of every tile touching the central Q at a point, every extension of this patch, or the forced pentagon neighborhoods of the three new Q tiles. Those larger domains are explicitly disclaimed in the source note. In particular the surviving triples are geometric patches with disjoint interiors, not certificates that all boundary vertex gaps can be completed.

Replay from repository root:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-heptagon-144-126-hostile-sol-2026-10-19.sage

## Additional AA-count corollary

The appended nonagon/decagon corollary in `research/lemmas/regular-pentagon-octagon-aa-side-density-obstruction-2026-10-19.md` is valid. The polygon angle sum gives 2a+3b=20; corner counting gives 5p_R=(2a+b/2)q_R+O(R). The local pentagon AA capacity remains one. With (a,b)=(7,2), each B needs one QQ edge and no A can meet that edge, so the B vertices must be adjacent. Their single BB edge leaves six AA edges, exceeding P/Q density 3. With (10,0), ten AA sides exceed density 4. The boundary-area contradiction applies equally to nonperiodic tilings. This excludes those specified palettes, not arbitrary nonagons or decagons.

## Verdict

**Valid within the stated exact finite scope**. No mathematical defect or needed repair found. The independent checker completed successfully: `VALID: independent AA polyhedron checks; base, 18 joins, 216 triples`. No assertion of plane tilability, aperiodicity, or unrestricted two-polygon impossibility follows. The global construction and universal nonperiodicity obligations remain unresolved; no further bounded growth is justified by this review alone.
