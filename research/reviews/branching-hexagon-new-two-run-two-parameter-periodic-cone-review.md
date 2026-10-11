# Fresh independent review: two-parameter alternating/two-run periodic cone

**Verdict: VALID on the complete stated open parameter domain, including p=q.**

Reviewer: branching_hexagons, freshly assigned by root. Root proposed the two-parameter synthesis and is not its sole full-domain reviewer. This is a new audit of the actual [extracted theorem](../lemmas/branching-hexagon-new-two-run-two-parameter-periodic-cone.md) and [standalone certificate](../certificates/branching-hexagon-new-two-run-two-parameter-periodic-cone.json), separate from the earlier third-curve review. The [independent checker](verify_branching_hexagon_new_two_run_two_parameter_cone_independent.py) imports no author module and executes no author producer.

## Independent raw geometry

The checker independently parameterizes delta and gamma by t=tan(delta/2),u=tan(gamma/2). It constructs all actual Cartesian edges over Q(sqrt3)(t,u) using the rational sine/cosine formulas and p=2cos(delta)/(1+2cos(gamma)). Both raw closures vanish identically, and all12 edge norms equal their required p or1 lengths. Thus closure does not depend on the retained fixture or on continuity.

On0<delta<30 and0<gamma<120-delta, gamma<120 gives cos(gamma)>-1/2, while cos(delta)>0, so p is strictly positive. The checker derives every indexed native angle and direction increment independently from the physical affine direction words, including their360 wrap. They agree with the certificate. The12 turn forms sum to360 for each polygon and are nonnegative on all four vertices of the closed parameter polygon; none is identically zero, and every maximum is below180. Every turn is therefore strictly positive in the open polygon interior and strictly below180.

Positive edges with total direction winding360 and these ordered strict turns, together with exact closure, prove strict convexity. Relative to any edge, the transverse components of the following edges first have a positive run and then a negative run, allowing isolated zero terms. The first is strictly positive and the last strictly negative. Heights rise and then fall to their final value0; they cannot reach0 early during the negative run because a later negative term would contradict closure. Every nonincident vertex has strictly positive inward height. This supplies a direct full-domain support proof; no two-dimensional sample or numerical root scan is needed.

## Every actual link and global coverage

The independent checker reconstructs the eight actual face states, reflecting their corner indices as-i mod6 and reversing side labels. All48 native side occurrences are used exactly once in24 reversed-boundary pairs, each with the same actual p/q side length. It derives the circular links by the outgoing-side to partner-incoming-corner successor permutation, without trusting the stored vertex classes. There are precisely16 cycles of three actual corners. Every cycle has affine angle coefficient triple(360,0,0), and the reconstructed classes agree with the retained certificate.

The dual face graph is connected and all boundary gluings reverse their induced orientations. The result is an oriented connected closed Euclidean surface; every edge neighborhood is nonsingular and every actual circular vertex link has angle360. Its Euler characteristic16-24+8=0 gives a compact flat torus at every individual metric. The complete simply connected flat universal cover is the Euclidean plane, with the lifted native polygons forming a covering with disjoint interiors. Its freely acting orientation-preserving Euclidean deck isometries are translations, and compactness gives a rank2 lattice. Hence the construction supplies an actual doubly periodic edge-to-edge plane tiling throughout the stated domain.

The pairing uses equality of corresponding labels, never inequality of the numerical lengths p andq. At p=q additional matching choices become available, but every chosen seam remains valid. No distinct-length hypothesis or negative binary-color obstruction is used or extended there.

## Prior curves, fixture and replay

Substitution gamma30,60,90 gives respectively p=2cos(delta)/(1+sqrt3),cos(delta),2cos(delta). All three slices lie within the open domain for0<delta<30. The independently reviewed exact delta15,gamma30 fixture and its primitive rectangular lattice remain valid; they are not the justification for the complete two-parameter result.

Completed readonly replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_new_two_run_two_parameter_cone_independent.py

Output: PASS for raw two-variable closures, all12 squared norms, native affine angle/turn derivation, all12 full-domain strict turn bounds,48 unique equal-label side occurrences,16 actual circular360+0delta+0gamma links and the connected oriented flat torus.

No substantive defect was found. Positive common scaling preserves the result. The open-domain boundary is not included, and no classification of all alternating/two-run pairs or resolution of the original unrestricted problem is claimed.
