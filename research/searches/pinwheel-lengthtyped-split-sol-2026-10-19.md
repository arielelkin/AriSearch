# Length-typed shared seams and two handed center types: exact obstruction

Status: **independently hostile-reviewed valid within the declared finite-patch family**; see the [Sol review](../reviews/pinwheel-lengthtyped-split-hostile-sol-2026-10-19.md). This is a restricted finite-patch obstruction, not a solution of the two-convex-tile problem. One changed-mechanism cycle completed; stop this declared family under protocol §5. No numerical scan, patch enlargement, or congruence census was performed.

## Family and fixed source

Use the same exact 125-triangle depth-three patch as the [earlier midpoint report](pinwheel-barycentric-crossboundary-2026-10-19.md). For reproducibility its entire source definition is: T=((0,0),(2,0),(0,1)); subdivide using the five triangles

((0,0),(2,0),(2,1)), ((2,0),(4,0),(4,1)),
((4,0),(5,0),(4,2)), ((2,1),(4,1),(4,2)),
((2,0),(4,1),(2,1)),

first mapped by N(x,y)=(2-(2x+y)/5,(x-2y)/5), then transported to each parent by the similarity mapping the right vertex O, long-leg endpoint L, and short-leg endpoint S of T to those of the parent. Perform three subdivisions. Planarize every source edge at every source vertex lying on it. The earlier independently reviewed source verifies containment, disjoint interiors, total area 1, and 81 fully interior vertex stars. The new script imports only its exact geometry/subdivision functions, not its seam or center decisions.

The planarized segment squared lengths are exactly 1/125,4/125,1/25. Give these three types independent fractions s0,s1,s2 in (0,1); they need not coincide and may be arbitrary real numbers. To orient a segment intrinsically, let I be its incident source triangles. For each endpoint v, form the sorted list over t in I of the triples

(|v-O_t|², |v-L_t|², |v-S_t|²).

Order the two endpoint signatures lexicographically, calling the smaller endpoint a and the larger b. Place the common seam point at a+s_i(b-a). If the signatures tie, use the midpoint. This rule depends on lengths and intrinsic endpoint/incident-triangle roles and is shared consistently by both triangles; it does not consult an arbitrary stored face-edge direction. Boundary segments can be treated by their single incident triangle. Only complete interior stars matter below.

The center of a triangle is O+p_h(L-O)+q_h(S-O), where h is the sign of det(L-O,S-O), and p_h>0,q_h>0,p_h+q_h<1. There are two independent center types, written (pp,qp) and (pm,qm). This handedness distinction uses a chosen plane orientation; the family is closed under reflection by exchanging the two parameter pairs. Requiring full reflection equivariance would impose equal pairs and gives a subfamily of the exclusion. More orientation types or neighborhood-dependent centers lie outside the declared family.

At each source vertex join its incident corner regions: in each incident triangle the dual boundary arc runs from the outgoing segment seam through that triangle's center to the incoming seam. All centers are interior and all seam fractions strictly interior. These regions partition the source patch and form simple corner-star cells. Strict convexity means convexity after removal of redundant collinear boundary vertices.

## New invariant, derived before solving

**Opposing-turn lemma.** If a planarized segment ab has two incident triangles with centers C,D, and both endpoint stars are complete interior cells, convexity of both cells forces det(C-z,D-z)=0 at their shared seam point z.

Proof. The cell at a traverses the consecutive triple C,z,D; the cell at b traverses D,z,C. Their signed turning determinants are negatives of one another. A convex counterclockwise polygon has nonnegative turn at every raw vertex, including redundant vertices. Both determinants must therefore vanish. Since the centers are on opposite sides of the source segment, z lies between C and D. Thus z becomes a redundant collinear boundary vertex. This does not depend on midpoint placement, equal center parameters, or a generic-position assumption. It is a necessary condition even for weak convexity.

This invariant is the reason to derive symbolic seam equations first. It excludes incompatible center/seam assignments without a convexity scan or congruence enumeration.

## Two exact witnesses kill the entire declared family

The following frames list (O,L,S), all coordinates in units of 1/25. Both triangles at each seam have negative handedness.

| Seam oriented endpoints a,b | First incident frame | Second incident frame |
| --- | --- | --- |
| (1,2),(3,1) | ((1,2),(3,6),(3,1)) | ((1,2),(5,0),(0,0)) |
| (3,11),(5,10) | ((1,12),(5,10),(0,10)) | ((3,11),(5,15),(5,10)) |

These are source triangles 86,87 and 72,73 respectively in the deterministic depth-three list (zero based). Both endpoints of both seams lie strictly inside T. Both seams have squared length 1/125. Their endpoint signatures are unequal and orient them exactly as displayed, so their common fraction is s0.

Set p=pm, q=qm, s=s0. Direct substitution in det(C-z,D-z) gives respectively A/125 and B/125, where

A = -4p² + 2ps - q² + qs,

B = 4p² - 2ps - 2p + q² - qs.

The opposing-turn lemma requires A=B=0. But A+B=-2p. Therefore p=0, contrary to the required interior-center condition p>0. This is an exact algebraic proof covering every real admissible value of all seven parameters; no solver answer is needed. Neither the positive-handed centers nor long/hypotenuse split fractions can repair these two seams.

The obstruction depends on assigning the same short-segment fraction after the specified intrinsic endpoint orientation. It does not exclude a finer seam type separating these two environments, more center types distinguishing these negative-handed triangles, moving centers to boundaries, curved dual arcs, or another source.

## Exact computation and replay

Retained [script](pinwheel-lengthtyped-split-sol-2026-10-19.py) and [certificate](pinwheel-lengthtyped-split-sol-2026-10-19.json). Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pinwheel-lengthtyped-split-sol-2026-10-19.py

The deterministic script reconstructs the same patch with exact Fractions; enumerates its planarized segments; builds symbolic centers, intrinsic seam signatures, and determinant polynomials with SymPy; and asserts the two-witness identity A+B=-2pm before invoking a solver. The certificate retains exact frame coordinates and raw determinant formulas, as well as all 146 seams having two interior endpoints. There are four distinct recorded polynomial expressions including zero. No symmetry quotient or random seed is used. Source generation and incidence are finite and exhaustive for this patch.

A supplementary Z3 QF_NRA solve, with 30,000ms timeout, imposes p_h,q_h>0,p_h+q_h<1 and 0<s_i<1 together with all seam collinearity equations. It completes UNSAT (Z3 4.16.0) and retains precisely the two displayed equations as its tracked core. This solver result corroborates the explicit polynomial contradiction; the core alone is not offered as a formal solver certificate. Python standard-library Fractions, SymPy, and Z3 are supplied by the locked arisearch environment. No numerical arithmetic enters incidence, type ordering, or polynomial derivation.

No infinite source containing the patch is proved here; the statement is conditional for any infinite source containing this patch. No exact tile-class count is relevant because convexity already fails. No shape-only decoding, extension, or aperiodicity claim follows. No new literature/priority claim is made. Reopening requires a changed seam-environment invariant or changed center classification that actually separates these witness constraints; repeating the solve or increasing patch depth does not do so. No discovery-log or git edits were made by this worker.
