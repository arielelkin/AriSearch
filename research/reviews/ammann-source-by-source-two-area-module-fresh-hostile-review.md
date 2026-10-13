# Fresh hostile review: source-by-source two-area module

Date: 2026-10-13. Reviewer: sol, independent of Luna's module extraction.
Verdict: **VALID**, with the source-by-source scope stated in the lemma. No unrestricted two-shape impossibility is established.

## Independently reconstructed argument

For each of the three actual positive-area source shapes, an exact finite dissection into copies of two fixed target shapes gives a_i=n_iP bP+n_iQ bQ, with nonnegative integer counts and unsigned target areas. Reflections and internal partial contacts do not change this identity. Therefore the source-area rational rank cannot exceed two. This argument makes no assumption about algebraicity, convexity, contact matching, target recognizability or plane extension.

If the source rank is two, bP and bQ must be rationally independent; otherwise every source area lies in a one-dimensional rational span. Since all source areas lie in their span, the spans coincide. Substitution into the primitive integer source relation consequently forces its coefficient relation separately on both integer count columns. This is valid even if one source omits one target type. If an entire target type is unused, the source rank already gives a contradiction.

For a relation k_i n_i+k_l n_l+k_m n_m=0, put g=gcd(|k_l|,|k_m|). Then g divides k_i n_i, so g/gcd(g,|k_i|) divides n_i. Positivity excludes a relation supported on a single source coordinate, so g is positive. This also covers a zero k_i: the resulting divisor is one. No assertion that these divisibilities suffice for a dissection is made.

## Rational sample and exact replay

I independently reconstructed the normalized coefficient matrix over Q with rows (1,71/200,-71/200) and (0,2/5,3/5). It has rank two and primitive kernel (-71,120,-80). The divisors for H,P1,P2 respectively are 40,1,1. In particular each individual target count in H is a nonnegative multiple of forty. Positive H area forces at least one nonzero count, so a nonempty compiler uses at least forty pieces in H. This excludes every one-piece or two-piece H dissection that can be completed source by source on the other two source shapes, regardless of its cuts; it is stronger than an exclusion of only one-each two-piece cuts.

The retained independent checker was read and replayed:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_ammann_h_midpoint_cut_area_gate.py --check research/certificates/ammann-h-midpoint-cut-area-gate.json

Result: PASS. It reconstructs the affine source vertices at J=1/2+(4/5)w, verifies the H midpoint cut words, strict convexity, noncollinear degree-three cut endpoints and exact area partition. Its cross-product denominator w-conjugate(w) gives areas normalized by sin36. It derives both other source areas and the two unique rational target-count vectors (-1289/1800,5111/1800), (-1177/600,2023/600); their negative first coordinates already kill this fixed seed. No producer import or solver is used.

The 300 imported pentagon-family tests are unnecessary to this obstruction and were not independently repeated here. Their advertised local nonmonohedral scope supplies no target tilability or forcing claim.

## Rank-three application and review dependency

Given the displayed source area identities H/sigma=1, P1/sigma=phi-f, P2/sigma=f, irrationality of phi gives rational rank three exactly when f is outside Q(phi): a relation qH+q1 phi+(q2-q1)f=0 forces q2=q1 and then all three coefficients zero. Thus every such actual source parameter excludes all source-by-source two-target dissections, with no restriction on piece number. Neither G* membership nor source aperiodicity is needed for this area exclusion; genuine positively oriented source polygons are needed when interpreting oriented formulas as unsigned areas.

The reviewed module uses the separately extracted area-rank artifact for its explicit N1000 G* certificate. I authored that earlier artifact and do not present this review as independent hostile certification of its prime-valuation or G* proof. The general module argument and rational J0 reconstruction above are independent of that certificate; its explicit-sample applicability retains its separate review gate.

## Limits and next justified actions

Cross-boundary target recomposition invalidates the per-source integer count hypothesis and is not excluded. Rank-two parameters with higher-piece cuts are not excluded merely by this modulus. Passing an area gate would still require actual geometric source dissections and an infinite shape-only forcing mechanism. The integer lower bound supplies no justification for enumerating forty-piece cuts. A concrete cross-boundary reassembly or changed source parameter is the next useful proposal; arbitrarily enlarging the rejected midpoint search is not.
