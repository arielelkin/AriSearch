# Exact support-pivot alias candidate: every ring fails at its far endpoint

Date:2026-10-13. Status: independently reviewed VALID for this exact pair;
[hostile review](../reviews/contact-non-equiangular-alias-hostile-review.md). One changed candidate, not a metric sweep.

Let r=sqrt2,c=cos(pi/8),t=sin(pi/8). Rotate the bottom support line of the
side-one regular octagon to y=(r-1)(x-c), retaining its other seven supports.
Use the Q vertex formula of
contact-non-equiangular-octagon-one-deformation-obstruction.md with pivot c.
The native angles are112.5,157.5,135^6 and native lengths

    (H,u,1,1,1,1,1,v), H=2c-1,u=c,v=1+t.

Define P by integrating fixed directions-22.5,45,135,202.5,270 degrees
and lengths

    (x,u,v,y,w)=(1,c,1+t,r-1/(r*c),1).

Both are genuine strictly convex positive polygons. Exactly x=w is the
new native alias; the other values are distinct, H absent from every P
length. All native P and Q lengths differ from2u and2v. The exact producer
research/searches/contact-non-equiangular-octagon-alias-candidate.py checks
these claims, closure, strict support inequalities and the complete ring
and far-end domains. No claim is made about other alias metrics.

The seven full stars and the sole flat star host180+2P90 are exactly the
same complete angle census as the preceding non-equiangular fixture.
The Q-only whole-contact proof likewise survives: at a Q-hosted cap the
perpendicular guest acute legs must be equal (a shorter leg ends at112.5
inside a side, forbidden); the along-host legs are then equal. Guest far
P112.5 and host Q endpoints cannot lie inside each other's sides. Therefore
native host Q length must be2u or2v, absent. Native Q corners cannot lie
in any flat star. Thus all Q contacts are whole on both participating sides.
No blanket ETE or classification of arbitrary PP partial contacts is used.

## Complete source ring around any occurring Q

The private H side must match the unique Q H slot. Reflection across its
support line puts157.5+157.5 at an endpoint, impossible; its mate is the
midpoint halfturn. At both endpoints this createsQ112.5+Q157.5+P90, so the
adjacent u/v neighbors are uniquely determined Pacute placements. The
producer checks the QH dimer plus both acute Pguests is disjoint exactly.
A Q length-one side cannot match another Q length-one side: both endpoints
would have Q135+Q135+P90. At least one endpoint of each of the five ordinary
Q1 sides is adjacent to another Q1 side of its own polygon; the guest P90
would need an acute leg of length1, absent. Thus all five ordinary Q1 sides
match P x or w. Both endpoints of either such P native side are112.5, and
all four reflected/endpoint-fixed placements are enumerated.

At the Q135 vertices, consecutive Pguests have exposed PP lengths only
1,u,y. A mismatch ending first at nativeP112.5 is impossible against a
flat host. The only remaining unequal case has short u ending atP90 inside
long1. The length-one hosts here are native Px orPw, each with two obtuse
endpoints. A90/90 flat cap forces equal perpendicular legs and hence two
along-host u legs. Neither guest112.5 nor host112.5 endpoints may lie in
side interiors, so host length would be2u, contrary to1!=2u. Therefore all
these PARTICULAR shared PPinterfaces are whole. This does not exclude
other PP partial contacts elsewhere.

The producer checks every one of4^5 ordinary-side choices, retaining only
whole interface matching and exact pairwise disjointness. Exactly four
source rings remain, written X for a Q side matched toPx and W forPw:

    XXXXW, XXWWW, WWXXW, WWWWW.

Thus the native alias really escapes the previous contact-capacity bound,
and all four rings are positive finite patches. It does not create a plane.

## Far-end obstruction for every surviving ring

At the far endpoint of a shared PPedge with two native P112.5 corners,
only Q135 can complete the star. Its two incident sides must match the
Pnative edges exposed there by the already proved whole-Q contact property.
Q135 native side pairs are ONLY(u,1),(1,1),(1,v), ignoring endpoint order.
No pair containing y, or(u,u) or(v,v), exists.

Every one of the four source rings has an unavoidable missing native pair.
For XXXXW the central X/X shared Pw/Pw edge has two farP112.5 and would
require Q135 with(y,y). For each of XXWWW,WWXXW,WWWWW there is a consecutive
W/W interface: Px/Px gives far(u,u), orPy/Py gives far(v,v). All are absent.
The producer independently reconstructs the exact shared endpoint and each
exposed native side length for every ring, checks both far corners are
obtuse, and verifies at least one required pair is missing from the SIX
actual Q135 native corners. It prints additional witnesses as well.

Therefore no occurring Q can extend its first ring to a plane tiling.
A P-only plane tiling is also impossible: nativeP112.5 cannot be completed
from P90/P112.5, including flat hosts. The original pair is UNTILEABLE.
This is a complete local counterexample at one exact changed alias metric,
not a larger search or an exclusion of all non-equiangular partners.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/contact-non-equiangular-octagon-alias-candidate.py
