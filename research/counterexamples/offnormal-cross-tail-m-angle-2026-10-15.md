# Exact counterexample to a cross-tail angle bound

Date: 2026-10-15. Status: exact counterexample independently constructed and replayed. This refutes one proposed necessary-angle bound; it is not a common-H construction or an aperiodic tile pair.

## Refuted claim

The proposed claim was that, in the identical-donor off-normal branch with all sixteen receiving precursor quads strict and 0<beta<9, 72<theta_tail<90-2beta, the thick cross-tail quad's retained split-point angle M always lies between 90 and108. It is false: the exact fixture below has that angle strictly between108 and114.

The SAME mark-local donor triangle is used for X and Y. Write beta=arctan(1/100), gamma=beta+36 degrees and set

    u=sin(gamma)*cos(beta)/sin(2beta+36), h=u/100,
    q0=cot(72+beta), q=q0-1/10000,
    m=u-h*q.

Every trigonometric value is exact algebraic: cos(beta)=100/sqrt(10001), sin(beta)=1/sqrt(10001), and the fixed36/72-degree values belong to the real cyclotomic field. All source edges have unit length. Copy the apex (u,h) using each actual donor arrow and source inward normal, use split coordinate m on that arrow, and use the standard native thin/thick arrow tables.

## Exact checks

The standalone [checker](offnormal-cross-tail-m-angle-2026-10-15.py) imports no author producer. It checks 0<u,m<1, h>0, the four complete source partitions, source containment, exact pairwise separating axes and area coverage, all sixteen strict receiving quads, and strict central receiving triangles. It explicitly verifies beta<9 and 72<theta_tail<90-2beta using exact tangent/cotangent comparisons.

For thick donor parity0, receiver BC, endpoint B, the incoming edge is a Y-tail while the adjacent internal AB node is an X-head. In a normalized local frame its retained source vertex is0, external apex is(u,-h), split is(m,0), and internal donor node is

    p=(a,b)=Lhead*(cos(72-beta),sin(72-beta)),
    Lhead=h/sin(gamma).

This is the thick cross-tail case with retained endpoint angle72. The checker directly reconstructs it from the source coordinates and verifies that its M-angle cotangent is strictly between cot114 and cot108. Thus its actual convex interior angle satisfies108<angle_M<114. The latter is compatible with the previously derived H capacity requirement that unspecified angles exceed108; convexity alone does not close this branch.

The fixture was analytically selected near the strict thin-tail boundary, not found by a scan. At q=q0 the same-mark acute-tail quad is degenerate and theta_tail=72. Increasing m by exactly h/10000 makes it strict. The cross-tail M angle exceeds108 at that limit: it is90+atan(q0)+atan(b/(m-a)), and, with m>a as in this fixture, b/(m-a)>tan(beta) whenever m<1 because the reverse inequality would require m>sin72/sin(36+2beta)>1 for0<beta<9. The exact retained perturbation preserves the counterexample, as checked directly.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/counterexamples/offnormal-cross-tail-m-angle-2026-10-15.py

Observed result: PASS four source partitions and sixteen strict quads; cross-tail M angle strictly between108 and114. No floating-point angle or orientation decisions, random scan, optimization, cap cuts, or P/H congruence search is used.

## Exact scope

Only the proposed universal M-angle bound is falsified. No cut fractions making all receiving hexagons congruent have been supplied. In particular this fixture does not meet the later common-H opposite-diagonal constraint m=1/2; that stronger metric invariant can obstruct the full construction without contradicting this counterexample. The broader off-normal construction claim requires its separate proof and audit.
