# A nonmonohedral AAA stratum is removed by an exact B-closure separator

Date: 2026-10-13. Status: [fresh independent hostile review VALID](../reviews/terra-five-one-002112-paired-stratum-fresh-hostile-review.md); rational certificate retained. Covers one exact side-equality stratum of
A002112 on the changed B5+1 line, not arbitrary A002112 metrics.

## Statement and finite question

Use112.5<x<126, x!=120, y=720-5x,z=4x-360, r=360-2x,s=360-2y.
Let actual A have native angles002112 and side word(a,a,b,b,c,c), all lengths
positive. B has native angles(s,r,r,r,r,r). Such an A admits a metrically
legal AAA corner star at native corners0,4,2; unlike A012012 it need not be
centrally symmetric or monohedrally tileable. Nevertheless NO positive closed
B can satisfy the necessary four AB-side lengths of a saturated mixed field.
This excludes the entire positive paired-side stratum for that mechanism.

Preceding finite domain: all64 native AAA choices/reversals for A002112, checking
whether their equalities force the H1 equality a0=a3.32 do and32 do not. Rather
than expanding any patch, the paired-side case was tested using one exact
rational angle and all16 central AAB fan choices. It provided an actual AAA
counterexample but BOTH BB lengths were negative in all16 cases. The following
analytic separator generalizes that finite result throughout the angle interval.
No unrestricted AAA=>monohedral assertion is used.

## Positive A closure and ordering, at every admitted angle

Putu=180-x in(54,67.5), u!=60, and U=exp(iu), interpreting degree arguments.
Thenv=180-y=360-5u andw=180-z=4u-180, andUVW=-1.
After rotation the six A edge unit directions are

    (1,U,-U^5,-1,-U^-5,U^-1).

Grouping paired lengths gives

    S0=1+U, S1=-(1+U^5), S2=U^-1-U^-5,
    a S0+b S1+c S2=0.

Their positive magnitudes and increasing directions are

    |S0|=2cos(u/2), theta0=u/2;
    |S1|=-2cos(5u/2), theta1=5u/2;
    |S2|=2sin(2u), theta2=450-3u.

The cyclic angular gaps2u,450-11u/2,7u/2-90 all lie strictly between0 and180.
Hence the real2x3 matrix has a one-dimensional strictly positive closure kernel;
all actual positive paired lengths are fixed up to positive scale. Its ratios
are

    c/a=cos(u/2)/cos(11u/2),
    b/a=cos(u/2)cos(7u/2)/(cos(5u/2)cos(11u/2)).

The denominator cos(11u/2) is positive on(297,371.25) degrees;
cos(5u/2) is negative on(135,168.75), and all needed magnitudes are positive.
The differences have signs

    sign(c-a)=sign[2sin(3u)sin(5u/2)]=sign(60-u),
    sign(c-b)=-sign[2sin(3u)sin(u/2)]=sign(u-60).

Thus u>60 gives a>c>b, while u<60 gives b>c>a. All three are distinct at
EVERY allowed angle; proper equal-length specializations of this paired stratum
would forceu=60 and lie outside the hypothesis. No untested specialization is
silently carried over from the distinct fixture.

## Necessary saturated B fan lengths

The reviewed capacity palette allows only BB native mask{1,4} for A002112.
It requires AB endpoint pairs12 on sides0,5 and02 on sides2,3.
The A0 corners attach through their two native02 sides1,5, whose lengths are
a,c; their remaining AA arm is native side0 of lengtha in either case.
The A1 corners attach through native12 sides2,4, lengths b,c; their remaining
AA arm is native side3 of lengthb. Therefore the two central AAB fans permit
exactly

    B side0=m0 and side5=m5 in{b,c},
    B side2=m2 and side3=m3 in{a,c}.

This includes all16 independent choices before BB endpoint consistency, actual
B positivity or chain extension. Different metric aliases were already excluded
by the positive A closure ordering above, rather than assumed absent.

## Both remaining B lengths are strictly negative

LetR=180-r=180-2u in(45,72) and E=exp(iR). Letp,q be the BB side lengths1,4.
B edge directions areE^j, j=0..5. Cramer's rule for closure gives, with
D=sin(3R)!=0,

    pD=-m0 sin(4R)-m2 sin(2R)-m3 sinR+m5 sinR,
    qD= m0 sinR-m2 sinR-m3 sin(2R)-m5 sin(4R).

Here sinR,sin(2R),-sin(4R),cosR are all strictly positive. D has the sign
ofu-60 (D=sin6u). Ifu>60, m0,m5<=c andm2,m3>=c, so each numerator is at most

    -c(sin4R+sin2R)=-2c D cosR.

Divide by positiveD. Ifu<60, the inequalities reverse, so each numerator is
at least the same quantity; dividing by negativeD reverses them again.
In BOTH cases

    p<=-2c cosR<0, q<=-2c cosR<0.

No actual positive B polygon can have these lengths. This is an exact separating
inequality for all four AB length choices and every positive scale throughout
the stated angle interval. No bounded local search is being extrapolated to
infinite tilability.

## Rational actual AAA counterexample and replay

Takei^2=-1 with positive imaginary embedding and U=(8+15i)/17. Its real part
lies exactly betweencos67.5 andcos54, and U!=exp(i60). Define the grouped vectors
S0,S1,S2 above and

    (a,b,c) proportional to(cross(S1,S2),cross(S2,S0),cross(S0,S1)),
    cross(P,Q)=(conjugate(P)Q-P conjugate(Q))/(2i), a=1.

The exact resulting values are

    a=1, b=383444911/476356015, c=1419857/1561823.

Cumulative paired edge vectors give rational complex coordinates retained in
[the certificate](../certificates/terra-five-one-002112-rational-geometry.json).
All strict nonincident support determinants are positive. Corners0,4,2 have
reversed arms(a,c),(c,b),(b,a), giving an actual disjoint three-copy AAA patch:
each convex copy lies within its corner sector and the three sectors sum360.
The lengths a0=a and a3=b differ. All generic H1/H2 conditions for native002112
require a0=a3; H3 would require120-degree angles, unavailable here. Thus the
imported three-family monohedral theorem makes this A nonmonohedral.

[Fixture producer](../searches/terra-five-one-002112-rational-geometry.py).
It tests one exact A plus sixteen exact rational B closure equations, accepting
no numerical geometry. All sixteen have negativeBB1 andBB4. The proof-critical
family result is the analytic inequality above. [Separate no-import fixture checker](../reviews/verify_terra_five_one_002112_rational_geometry.py)
PASS, including all64 equality cases over203 formal partitions. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_002112_rational_geometry.py

Fresh hostile review of the analytic separator is required before stable promotion.

## Scope and next obligation

AAA=>central and AAA=>monohedral do NOT extend to this remaining word. The
capacity theorem plus the separator instead eliminates this particular paired
AAA metric mechanism at every angle. The other non-H1 AAA equality patterns,
including four-class choices and non-paired metrics, remain unclassified.
The next concrete attack is to identify whether this sign separator follows
from more general native fan/closure inequalities, or to choose a genuinely
new actual metric where its ordering premise fails and test exact BB endpoint
compatibility. More angle samples of this eliminated paired stratum or larger
B-chain patches would add no coverage.
