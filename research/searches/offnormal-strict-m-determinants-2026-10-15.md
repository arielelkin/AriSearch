# All off-normal M determinants and a strict positive precursor fixture

Date:2026-10-15. Status: analytical reduction and exact one-fixture positive
verification; independently hostile-reviewed VALID for this exact finite scope
([review](../reviews/offnormal-strict-m-hostile-2026-10-15.md)). No two-prototype congruence,
cap-cut admissibility or aperiodicity is claimed.

## The exact16 inequalities, in eight distinct native contexts

Use mark-local donor apex parameters (uX,hX),(uY,hY), each projection strictly
inside its unit base, and independent split parameters mX,mY in(0,1).
For a receiving edge with ACTUAL arrow T->H, put T=(0,0), H=(1,0), choose
the receiver half-plane y>0, and write its incoming donor apex as

    t=(u,-h), M=(m,0).

Let the receiver's internal donor nodes adjoining T,H have coordinates
(xT,yT),(xH,yH), respectively, with yT,yH>0. For the tail quad (T,t,M,pT)
and head quad (H,t,M,pH), the exact conditions for their turns at M are

    D_T=m(yT+h)-u*yT-h*xT >0,
    D_H=u*yH+h*xH-m(yH+h) >0.

These are LINEAR in the split parameter m. They say M lies between the
intersections of the lines t-pT,t-pH with the source edge. They do not
assume that t-M is a normal or that the M angle is obtuse.

To express x,y in the six mark parameters, define

    f(sigma,k,g)=k*cos(sigma)+g*sin(sigma),
    g0(sigma,k,g)=k*sin(sigma)-g*cos(sigma).

Here sigma is the original source angle at the endpoint, k is the internal
adjacent donor apex projection measured from that endpoint, and g its
height. At a tail endpoint set (xT,yT)=(f,g0). At a head endpoint set
(xH,yH)=(1-f,g0). The same formulas apply when the actual arrow reverses
the source boundary direction; the local receiver normal chooses the frame.

The complete distinct context table is:

| Receiving source / mark / endpoint | sigma | Adjacent donor k,g |
|---|---:|---|
|thin X tail|36|uY,hY|
|thin X head|144|1-uX,hX|
|thin Y tail|36|uX,hX|
|thin Y head|144|1-uY,hY|
|thick X tail|72|uX,hX|
|thick X head|108|uY,hY|
|thick Y tail|108|1-uX,hX|
|thick Y head|72|1-uY,hY|

Each row occurs once in each donor parity, giving ALL16 requested M
inequalities. The exact checker reconstructs the actual source-arrow
coordinates independently and verifies the f,g0 expressions for each row.
A point satisfying these necessary M inequalities must additionally satisfy
all other support and source-partition inequalities; the positive fixture
below is checked against those as well.

## The reduced endpoint-angle branch

The common-H endpoint capacity argument, independent of the normal-foot
assumption, forces Xtail=Ytail=beta and Xhead=beta+36 or beta-36. Every
X/Y donor tail occurs at a thin acute36 corner, so a valid source sector
requires0<beta<36. The minus branch would give a negative Xhead angle,
so only

    Xhead=beta+36

remains. Let Yhead=gamma. In slope variables tau=tan(beta),

    uX=(sin36+tau*cos36)/(sin36*(1-tau^2)+2*tau*cos36),
    hX=tau*uX,
    uY=cot(beta)/(cot(beta)+cot(gamma)), hY=tau*uY.

Together with mX,mY these are the proposed four continuous parameters.
The present result does not assert that the positive fixture has a common
H prototype; it satisfies this endpoint-capacity branch and tests the
strict-convexity-only inference against it.

## Exact positive fixture, derived from the linear interval bounds

Set

    tau=1/100, uY=2/5, hY=1/250,
    uX=(sin36+tau*cos36)/(sin36*(1-tau^2)+2*tau*cos36),
    hX=tau*uX,
    mX=uX+(337/1000)*hX,
    mY=uY+(708/1000)*hY.

Thus beta=atan(1/100), gamma=atan(1/150), and Xhead=beta+36 exactly.
All parameters are explicit real algebraic coordinates: cos36=(1+sqrt5)/4
and sin36=sqrt(10-2sqrt5)/4. There are no decimal or random parameters.
The rational offsets337/1000 and708/1000 were chosen inside the analytically
derived linear M intervals, not by a grid or random metric search.

The exact checker verifies:

*0<uZ<mZ<1,hZ>0 for both marks and the exact tangent identity for Xhead;
*all four thin/thick/parity source partitions: donor triangles and receiving
 quads are strict, contained in the source, pairwise interior-disjoint, and
 their areas sum exactly to the source rhomb area;
*all16 assembled receiving L/R quads are strictly convex by every support
 inequality, and all central receiving triangles are strict;
*all16 normalized M determinant inequalities above have the required strict
 signs, with their actual adjacent native donor role verified;
*BOTH external tail half-apex angles are strictly GREATER THAN108 degrees.

For the last assertion the exact cotangent at t in triangle(T,M,t) is

    cot(theta_tail)=(h^2-u(m-u))/(h*m).

Cotangent is strictly decreasing on(0,180). The checker proves for each
mark that this number is strictly below cos108/sin108, using exact real
algebraic comparisons. No floating-point angle evaluation decides it.

This is a genuine strict positive precursor partition with obtuse external
half-apex angles. It disproves any proposed universal claim that strict
source/quad convexity plus the endpoint-capacity branch forces
Xtail_half_apex<90, or even<=108, or forces one of the two tail halves to
be<=108. Thus the failed base6/head42 fixture was point-specific, and a
convexity-only reduction cannot close the whole off-normal component in
that way.

## Useful bounds that remain valid

Same-mark/same-role contexts give simple half-angle bounds. For example,
from the thin X-head row, with alpha=Xhead,

    mX < uX+hX*tan(72-alpha),
    theta_Xhead >18.

This is equivalent to strict M convexity there: substitute k=1-uX into
the head formula and use tan subtraction. In the reduced branch this gives

    theta_Xtail <126-2*beta.

It is consistent with the positive fixture. Similarly the thick Y-head
row gives theta_Yhead>54 and theta_Ytail<126-beta-gamma. These useful
necessary bounds alone do not contradict the current endpoint/cyclic-word
angle capacities. The positive fixture has small beta,gamma.

No conclusion is made that its actual H angles share one cyclic word.
That is a stronger metric/prototype-angle gate, involving the retained M
angles and all cutpoint identifications, not merely convexity. General
unequal cap fractions may also fail to form strict convex caps even when
the precursor quads are strict; none have been fitted here.

## Replay, exact scope, and next obligation

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/offnormal-strict-m-determinants-2026-10-15.py

The producer prints JSON by default and writes only with explicit --output.
Retained exact record:
`research/certificates/offnormal-strict-m-determinants-2026-10-15.json`.
The computation uses Sage exact algebraic arithmetic with cyclotomic20 and
all native source roles. Its domain is ONE algebraic parameter fixture,
ALL four source cases and ALL16 receiving quads. No solver, random seed,
parameter grid, metric congruence search or periodic quotient enumeration
is used. The analytic determinant formulas cover the full stated six-
parameter pre-closure domain; the positive evaluation concerns one point.

The precise remaining obligation is compatibility of actual geometric
receiving angles and globally shared cap fractions with ONE H6 and ONE P5
prototype, followed by exact congruence and intrinsic shape-only forcing.
A positive precursor fixture alone is not a two-class construction or an
aperiodic pair. Fresh independent review is pending.
