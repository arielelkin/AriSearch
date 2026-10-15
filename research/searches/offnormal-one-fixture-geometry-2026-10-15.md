# Exact geometry rejects the one off-normal 6/42-degree angle witness

**Later status:** the full stated off-normal mark-local receiving-hexagon
component is excluded by the independently reviewed
[combined congruence obstruction](../lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md).
The narrower calculations below retain their explicitly stated scope.

Date:2026-10-15. Status: exact one-fixture falsification. This is not a
classification of the off-normal construction component. No metric or
congruence parameter search was performed.

## Exact fixture reconstructed from the SAT angles

The H-only necessary gate had the rational-degree witness

    H=(36,156,144,156,72,156),
    b_Xtail=b_Ytail=6, b_Xhead=b_Yhead=42,
    theta_Xtail=theta_Ytail=120,
    theta_Xhead=theta_Yhead=12.

Its small independent Fraction verifier passes all16 declared source-angle
contexts. That gate did not require a single shared coordinate realization.
This experiment checks EXACTLY this one coordinate realization and no
nearby points.

On a unit donor edge with actual arrow T->H let

    h=1/(cot6+cot42), u=h*cot6,
    m=u+h*cot54,
    t=T+u(H-T)+h*n_donor,
    M=T+m(H-T).

All trigonometric arguments are degrees. Exact comparisons give
0<u<m<1 and h>0. The full donor triangle has base angles6 and42. The
T-M-t subtriangle has base angle6 at T and54 at M, hence apex120; its
complementary subtriangle has apex12. Thus the off-normal split signs
and angle reconstruction are correct, rather than a misplaced-foot bug.

For source angle sigma=36 (thin) or72 (thick), use

    A=(0,0), B=(1,0),
    C=(1+cos(sigma),sin(sigma)), D=(cos(sigma),sin(sigma)).

Use the actual thin arrows AB:A->B, BC:C->B, CD:C->D, DA:A->D;
thick arrows AB:A->B, BC:B->C, CD:D->C, DA:A->D. Both marks have the
same fixture parameters. For each of the two donor parities, construct
internal donor nodes with inward source normal and external incoming nodes
with outward source normal. This gives all16 receiving L/R quads and all
source-sector triangles/quads. No independently tuned internal node is
permitted.

All coordinates belong to the real subfield of the60th cyclotomic field.
The checker uses zeta=QQbar.zeta(60), cos(6n)=(zeta^n+zeta^-n)/2 and
sin(6n)=(zeta^n-zeta^-n)/(2*zeta^15), converted to exact real algebraic
numbers. No floating-point angle, orientation or equality is used.

## Result: source partitions valid, convex outputs fail

For ALL FOUR source species/parity cases the two donor triangles and two
receiving quads are strict convex, lie in the source rhomb, have disjoint
interiors, and have total area exactly the source rhomb area. The checker
uses all supporting-line inequalities, exact separating-axis tests and
shoelace areas. Thus the underlying source partition is valid. The central
receiving triangles C=(M,q,p) are also strict.

However EIGHT of the16 assembled receiving L/R quads are nonconvex already,
with a reflex turn at M. The remaining eight are strict convex, but NONE
has the required M angle156. The checker compares exact cotangents, whose
values determine angles uniquely in(0,180). It also compares the actual
internal donor-node angles with the required48,12 or120 where a quad is
strict. Therefore the angle gate's abstractly consistent assignment does
not lift to this exact fixture.

## Small explicit reflex certificate

Take thin sigma36, donor parity0, receiver BC, endpoint B. Write
c=cos36,s=sin36. Its internal AB donor is p=(u,h), while

    t=B+(1-u)(c,s)+h(s,-c),
    M=B+(1-m)(c,s).

The assembled quad is Q=(B,t,M,p). Its consecutive turn at t is

    cross(t-B,M-t)=h(1-m)>0.

Its next turn at M is

    Delta=cross(M-t,p-M)
         =h(1-m)(1+c)+s*((u-m)(1-u)-h^2).

The exact algebraic comparison gives

    -3254/1000000 < Delta < -3253/1000000 <0.

Thus Q has turns of opposite signs and cannot be convex. The full turn
sign sequence is(+,-,+,+), indexed at t,M,p,B. This single exact local
failure already kills the proposed coordinate witness, independently of
any later cap cuts, chord aliases, or two-class metric matching.

There is a second independent mismatch in a strict quad: thick parity0,
receiver DA, endpoint A has ACTUAL angle at M exactly108 degrees, whereas
the H-only witness demands156. The exact checker also finds its parity1
counterpart. Both are strict, so this comparison involves genuine interior
angles rather than the minor ray angle of a reflex corner.

## Replay and retained evidence

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/offnormal-one-fixture-geometry-2026-10-15.py

The default prints JSON without changing evidence; --output writes the
retained certificate explicitly. Current record:
`research/certificates/offnormal-one-fixture-geometry-2026-10-15.json`.
It records all four source-partition checks, all16 strict-convexity results,
consecutive turn signs, minor-ray cotangent comparisons, and internal-angle
comparisons where appropriate. For a nonconvex quad the minor ray angle
is deliberately NOT described as its reflex interior angle.

The original H-only SAT record and Fraction verifier remain valid within
their declared relaxed scope. The failed object is ONLY the shared
base6/head42/theta120+12 coordinate realization. No conclusion about other
off-normal angle assignments, source-context-dependent cuts or different
partitions follows. The next research step must introduce a new precise
hypothesis or derive stronger geometric angle constraints; it must not
present this SAT witness as a geometric candidate or extend its metric
search without authorization.
