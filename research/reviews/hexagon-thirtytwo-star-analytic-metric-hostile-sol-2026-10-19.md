# Hostile review: thirtytwo-star analytic metric

Verdict: **FAIL / invalid as a realization of the retained native eight-star support.** The scalar implicit-function construction and its monohedral exclusions pass, but its angles are attached to the wrong native corners. No corrected construction is certified by this review.

## Claim and reviewed dependencies

Reviewed `research/lemmas/hexagon-thirtytwo-star-analytic-metric-sol-2026-10-19.md`, its same-stem producer under `research/searches/` and JSON certificate under `research/certificates/`, the native builder `research/searches/hexagon-five-four-forced-dimer-2026-10-19.py`, and the preceding thirtytwo-star candidate gate. The claimed realization uses A=(0,1,2,0,3,4), B=(0,1,2,0,3,1), five distinct positive shared color lengths, the retained native support, and excludes all H1/H2/H3 labelings. It explicitly makes no corona or plane claim.

## Decisive defect: native angles versus geometric angles

The builder defines native corner c as incident to sides c and c+1. For the positive traversal of the producer's edge word, this is the **end** of side c, namely physical vertex c+1. In contrast, the IFT construction uses phi_j=sum(k=1..j)(pi-theta_k), so theta_c is the angle at physical vertex c, the **start** of side c. Therefore the native corner-angle variable must be theta_(c+1), within each species, rather than theta_c.

For example, retained unsigned native star (A0,A1,B2) needs theta_A1+theta_A2+theta_B3=2pi. The producer instead imposes theta_A0+theta_A1+theta_B2=2pi. The correct physical star sum minus 2pi vanishes at t=0 but has derivative (1+3sqrt(3))/4, which is nonzero. Hence this retained native star is invalid for every sufficiently small positive t in the proposed IFT family.

All four shifted physical star residual derivatives are nonzero:

| Native corner triple | Required physical start-angle triple | Derivative |
|---|---|---|
| A0,A1,B2 | A1,A2,B3 | (1+3sqrt(3))/4 |
| A2,B1,B5 | A3,B2,B0 | -2-sqrt(3) |
| A3,B0,B4 | A4,B1,B5 | 3+2sqrt(3) |
| A4,A5,B3 | A5,A0,B4 | -(5+7sqrt(3))/4 |

Reflection does not repair the mismatch: each signed native corner still joins its same two native sides. This is already an angle-compatibility failure before corona development, overlap, or extension is considered. A repair would change the closure convention to native end angles (including theta_j in the turn after edge j-1), or shift every support incidence appropriately, and then recompute the Jacobian, solved minor, tangent and full monohedral audit. The present numbers cannot certify that changed problem. An independent reviewer must audit any repaired result.

## Checks that pass within the producer's own angle convention

1. Exact rank and nullspace: the displayed six-row C has rank five; its seven-column N has rank seven and C*N=0. The all-2pi/3 affine origin satisfies both totals and all four unshifted equations.
2. Closure: differentiating the actual trigonometric closure expressions independently gives exactly the retained 4-by-7 Jacobian and determinant -3 for its first four columns. Both base residuals vanish exactly.
3. IFT: the four real analytic equations solve for x0..x3 in terms of t with x4=t,x5=x6=0. The recorded tangent vector follows by exact differentiation. No numerical root finding or interval estimate is needed for this local existence statement.
4. Lengths: for 0<t<1/4 the four lengths 1+jt, j=1..4, are strictly increasing below 2, so all five lengths are positive and distinct.
5. Strict convexity and simplicity: both base polygons have successive vertices (0,0), (2,0), (5/2,sqrt(3)/2), (2,sqrt(3)), (0,sqrt(3)), (-1/2,sqrt(3)/2). They are strictly convex; strict supporting half-plane inequalities persist under small continuous vertex perturbations. Closure and positive lengths persist along the IFT curve. Thus the abstract pair really is a strictly convex closed pair near the base.
6. Exhaustive monohedral patterns: an independent enumeration uses source angles at the START of each relabeled side, rather than the producer's end-angle translation. Across all twelve dihedral readings per word, A has four H1 length matches, zero H2 and zero H3; B has four H1, two H2, zero H3. Every matched H1/H2 sum has the nonzero derivative retained in the full audit. In particular, B's H2 derivatives are plus/minus 3(1+sqrt(3))/2. Intersecting finitely many sufficiently small intervals excludes all these systems for small positive t. The auxiliary certificate field `H1_sum_derivatives` instead records the unshifted first-three sums; it is not the correct geometric H1 audit, but the separate `full_dihedral_monohedral_audit` does use the correct sums.

The words also remain distinct congruence classes because their side-length multisets differ once all five color lengths are distinct. None of these passing observations turns the wrong incidence assignment into the retained native support.

## Counterexample attempts, repairs, remaining uncertainty

Attacks checked rank deficiency, closure-sign mistakes, singular solved coordinates, accidental equal lengths, non-simple base polygons, reflected label conventions, missed B H2 patterns, and native-star attachment. The last attack succeeds exactly. No repairs were made to the source lemma or producer; this review preserves the failure and a reproducible independent checker. Existence of a corrected native-support metric remains unresolved. Corona geometry, any entire-plane tiling, and unrestricted aperiodicity are also unproved.

## Replay and scope

Run:

`mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-thirtytwo-star-analytic-metric-hostile-sol-2026-10-19.py`

The checker reads the retained JSON, reconstructs the analytic closure expressions from scratch in SymPy, verifies the exact derivative and nullspace data, enumerates 24 side readings, and reports all four nonzero native-star residual derivatives. It uses symbolic exact arithmetic with no seed, solver timeout, floating arithmetic, or geometric extension assumption. Output is scoped PASS for the scalar IFT data and FAIL for the retained native support; script exit zero means these review assertions were reproduced. The producer itself was also replayed successfully; that success does not detect the incidence mismatch.
