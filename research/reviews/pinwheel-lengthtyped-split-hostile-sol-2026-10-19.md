# Independent hostile review: length-typed shared seams

Date: 2026-10-19. Verdict: **valid within the declared finite-patch family**. The two-convex-unmarked-polygon problem remains unresolved.

## Claim, dependencies, and reconstruction

Reviewed the lengthtyped-split report, producer and JSON, the research problem, protocol §§8,11,19, the earlier crossboundary report, and its independent center-family hostile review/checker. The claim excludes all seven real parameters consisting of three length fractions and two handed interior affine center pairs on the specified depth-three patch. It does not exclude arbitrary seam rules or arbitrary source tilings.

I reconstructed the patch using the geometry portion of the earlier independent reviewer checker, which does not import either producer or either candidate certificate. That reconstruction directly implements the five stated normalized children, three subdivisions, exact right/long/short frames, CCW face cycles and complete planarization. Its exact containment, pairwise separating-axis interior-disjointness, area 1, 125 triangle and 81 interior vertex assertions passed. Independently reconstructed incidence, endpoint signatures, split types and centers match all 146 candidate seam records and their raw symbolic determinants. This comparison includes every eligible seam, rather than only the selected witnesses. Exact segment squared lengths are 1/125, 4/125, 1/25.

The independent reconstruction was executed through the mandated mise/Conda wrapper using a Python heredoc; it reused only the geometry prefix before `p,q=S.symbols` of `research/reviews/pinwheel-barycentric-center-family-hostile-sol-check-2026-10-19.py`, then reconstructed segment incidences from its oriented face cycles and compared every JSON raw determinant symbolically. It did not execute the new producer or overwrite its certificate. No numerical arithmetic or solver result was used for the review verdict.

## Geometric necessity and orientation attacks

For a CCW planarized face cycle, the corner cell arc runs from its outgoing segment seam through the interior center to its incoming seam. Interior centers and strictly interior seams partition each triangle into nonoverlapping fan regions, including regions at formerly flat T junctions. Gluing around a complete interior source vertex yields a simple CCW star boundary: sectors have disjoint face interiors, distinct segment interiors contain distinct seams, and centers are in distinct triangle interiors. This remains true for every allowed parameter, including exceptional collinear boundary turns.

At a shared segment ab the cell at a contains C,z,D consecutively and the cell at b contains D,z,C consecutively, after potentially exchanging C,D once. The corresponding actual turn determinants are negatives. Convexity of both simple CCW cells forces both to vanish. Their centers lie strictly on opposite sides of the segment line, so the collinear seam z lies between the centers; it is a redundant boundary point rather than a backtracking spike. The argument therefore survives removal of redundant collinear vertices and does not assume strict turns or generic parameters.

The endpoint signature is intrinsic to the incident source triangles: O,L,S are uniquely determined by the unequal legs, squared distances survive isometry, and sorting removes arbitrary incident-face order. Positive scaling also preserves each lexicographic comparison. Reflection preserves the seam decision. The center handedness uses the selected plane orientation; it is not individually reflection invariant with fixed unequal parameter pairs. The report explicitly acknowledges this and exchanges pairs under reflection, so it makes no false reflection-equivariance claim. Its family includes the fully reflection-equivariant subfamily.

## Exact witnesses and algebra

Both reported seams really occur with the reported triangle indices and frames. Their endpoints are strictly interior to T, both segments have squared length 1/125, and all four incident frames have negative determinant. Their endpoint signatures are unequal and orient them as displayed in the report. For additional audit detail, multiply every signature coordinate by 125:

* Seam (1,2) to (3,1), in units 1/25: the signatures are [(0,4,1),(0,4,1)] and [(1,1,2),(1,5,0)].
* Seam (3,11) to (5,10), in units 1/25: the signatures are [(0,4,1),(1,1,2)] and [(1,5,0),(4,0,5)].

Thus both use s0, despite having distinct environments. Direct substitution of independently reconstructed centers gives

    125 det(C-z,D-z) = A = -4 pm² + 2 pm s0 - qm² + qm s0,
    125 det(C-z,D-z) = B =  4 pm² - 2 pm s0 - 2 pm + qm² - qm s0.

The raw determinant signs agree with the certificate when incident triangles are ordered by their indices. The literal identity A+B=-2 pm holds. Opposing-turn necessity gives A=B=0, hence pm=0, contradicting pm>0. No division by an unknown expression, numerical search, or assumption about qp,pp,s1,s2 occurs. In fact this contradiction does not require the three split fractions to satisfy their bounds; those bounds ensure the geometric construction under review.

## Counterexample attempts, defects, and scope

Attacks checked: stored-edge direction mismatch, swapped long/short roles, handedness errors, reflection behavior, signature ties, T-junction omissions, incomplete endpoint stars, polynomial normalization/sign errors, exceptional collinearity, boundary centers and different seam environments. None invalidates the declared claim. Boundary centers are excluded explicitly. A finer environment type can separate the two witnesses and remains outside the theorem; unequal negative-handed center pairs by environment likewise remain outside.

No defect requiring repair was found. The report distinguishes necessary seam equations from sufficient convexity conditions; failure of the former is sufficient for this exclusion. Exhaustiveness means all parameters in this specified family on this fixed patch, not all local constructions, substitution sources or geometric retilings. The explicit two equations carry the proof, so the supplementary UNSAT core is not being promoted to a formal certificate.

No infinite-source occurrence, recurrence or extension theorem was established or needed. The valid infinite statement is conditional: any source containing this patch and obeying these rules cannot yield all convex corner-star cells there. Nothing here proves that every infinite pinwheel source contains the patch, or establishes an impossibility theorem for the original two-polygon problem. No novelty claim was audited or asserted. No discovery-log or git edits were made.
