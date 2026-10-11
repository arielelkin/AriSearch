# A periodic pentagon partner for every metric in the Y angle family

**Status:** adversarially reviewed VALID in the [fresh independent audit](../reviews/general-y-pentagon-partner-review.md), with symbolic boundary/period checks and complete coordinate-overlap checks for two concrete metrics.
No novelty claim is made. This is a new general-metric construction in the
present research run, beyond the earlier two-parameter Y/Y seam family.

The [second fresh independent hostile review](../reviews/general-y-pentagon-partner-fresh-review.md) also returns VALID throughout the angle and metric domains, including reflections, convexity and full-plane coverage. Both reviews distinguish the selected periodic partner from an arbitrary independently specified pair.

## Statement and scope

Let pi/2<theta<3pi/4, k=-cos(theta), h=sin(theta), and

    d=1-2k^2>0, gamma=2pi-2theta.

Let P be any strictly convex pentagon whose counterclockwise angle word is

    Y=(pi/2,theta,pi/2,theta,gamma).

Write its vertices v0,...,v4 and positive native side lengths L0,...,L4.
After a direct isometry its directed unit side vectors are

    e0=(1,0), e1=(k,h), e2=(-h,k),
    e3=(-2kh,2k^2-1), e4=(0,-1),

and v0=0. In particular v1=L0 e0 and v2=v1+L1 e1. These hypotheses impose
only closure of the five actual edges, not the two-parameter relation of
the earlier periodic witness.

There is an explicitly defined strictly convex pentagon Q, having an angle
word dihedrally equivalent to Y and not congruent to P, such that {P,Q}
admits a doubly periodic whole-plane tiling using both shapes. The tiling
uses four faces per centrally symmetric hexagon carrier, two copies of
each shape. Contacts on carrier seams may be partial-edge contacts.

This asserts that every such P has *some* periodic partner Q. It does not
assert periodicity for every independently specified pair P,Q, and does
not solve the unrestricted two-convex-polygon problem. When theta=2pi/3
there are only two distinct native angle values; the same construction
still works. The three-angle statement is obtained by excluding that value.

## Coordinates and positive parameters

Put S=L0+L1+L2+L3+L4 and define

    lambda=S+kL0/d,
    delta2=(k lambda-kL1+L0)/h,
    delta4=(L1+d lambda-kL0)/h,
    w=(k,-h), A=v1, B=A+lambda w, C=(A+B)/2.

All these lengths are positive. Indeed lambda>S>L1, so
k lambda-kL1+L0>0; and

    L1+d lambda-kL0=L1+d S>0.

Also lambda exceeds every native side length of P.

Define q0,...,q4 by

    q0=v0=0,
    q1=v0+delta4 e4,
    q2=2C-v2,
    q3=B=2C-v1,
    q4=A=v1.

The key exact identity is

    lambda w=L1 e1-L0 e0+delta4 e4-delta2 e2.

Its x coordinate follows from the definition of delta2. Its y coordinate
is hL1-delta4-k delta2=-h lambda, using h^2+k^2=1 and d=1-2k^2.
Consequently q2=q1-delta2 e2 and the five directed sides of Q are

    delta4 e4, -delta2 e2, L1 e1, -lambda w, -L0 e0.

They close exactly. Their five successive interior angles are

    (pi/2,theta,pi/2,gamma,theta).

This is the reflected angle word Y. The cyclic direction turns are
pi/2, pi-theta, pi/2, 2theta-pi, pi-theta, each strictly between 0 and pi.
Positive lengths and this strictly cyclic direction order prove strict
convexity: for any fixed directed edge, perpendicular vertex heights first
increase while subsequent directions lie in its positive transverse
semicircle, then decrease to the height zero at closure. Nonincident
vertices have strictly positive heights. Thus each edge is a genuine
supporting edge and there is no crossed or concave polygon.

Q has a side of length lambda, whereas every P side has length less than
lambda. Hence their side-length multisets differ and P,Q are two distinct
congruence classes.

## Four-face dissection of a convex central hexagon

For a point z write z*=2C-z, and use P* and Q* for the central half-turn
copies of the entire polygons. Define the hexagon H by the ordered vertices

    v3, v4, q1, v3*, v4*, q1*.

Its directed sides are

    L3 e3, (L4+delta4)e4, -(L2+delta2)e2,
    -L3 e3, -(L4+delta4)e4, (L2+delta2)e2.

For example q1=v4+(L4+delta4)e4 and
v3*=q2-L2 e2=q1-(L2+delta2)e2; the remaining sides follow by the half-turn.
All lengths are positive, and the consecutive directions have positive
turns pi-theta, 2theta-pi, pi-theta, repeated twice. The same supporting-
height argument proves that H is strictly convex. Its opposite vertices
sum to 2C, so it is centrally symmetric. Its angle word is
(theta,gamma,theta,theta,gamma,theta).

P,Q,P*,Q* have matching oppositely traversed internal edges: P and Q
share v0v1, P and Q* share v1v2, P* and Q* share their half-turn images,
and P* and Q share theirs. Q and Q* share the spine AB. All remaining
boundary segments concatenate to the six sides of H. Thus their oriented
polygon boundary chains sum exactly to the oriented boundary chain of H.

This chain identity proves a dissection, without assuming an embedded cut
tree. At any point away from the finitely many edge lines, the sum of the
four polygon winding numbers equals the winding number of H. Every polygon
is strictly convex and counterclockwise, so its winding number is 1 on its
interior and 0 on its exterior. The winding number of H is likewise 0 or
1. Hence two face interiors never overlap, no face interior lies outside H,
and the four faces cover H away from those lines. Their finite closed union
then covers every point of H. This also excludes all putative edge-tree
crossings that would create an overlap or an uncovered region.

## Explicit lattice and full-plane coverage

Put

    x=L3 e3, y=(L4+delta4)e4, z=-(L2+delta2)e2,
    u=x+y, v=y+z.

The six directions are x,y,z,-x,-y,-z in cyclic order. All three pairwise
positive-direction determinants det(x,y),det(x,z),det(y,z) are positive.
The carrier area is

    area(H)=det(x,y)+det(x,z)+det(y,z)=det(u,v)>0.

The central hexagon tiles the plane by the lattice generated by u,v. Here
is a self-contained flat quotient proof of that standard parallelohexagon
fact. Pair each of its three pairs of opposite sides with reversed
boundary endpoint order. The exact neighbor displacements are -v, u-v,
and u for sides x,y,z, respectively. Every side has one equal-length mate;
the quotient is orientable and connected. Its corner-successor permutation
has the two cycles {0,2,4} and {1,3,5}. Each contains theta,theta,gamma, so
each circular vertex link has total angle 2pi. It has V-E+F=2-3+1=0 and no
cone singularities, hence is a compact flat torus. Its complete simply
connected flat universal cover is the Euclidean plane; the developed side
holonomies are precisely integer combinations of u,v, and both occur.
The nonzero determinant proves the two periods are independent. Therefore
translating H by this lattice gives a full tiling with disjoint interiors.

Equivalently, one may use the elementary centrally symmetric hexagon
translation-tiling theorem. The stated flat-cover argument makes its local
and global hypotheses explicit; it never infers infinite extension from
an arbitrary finite patch.

Insert the proved four-face dissection into every carrier. The carrier
lattice periods preserve the motif and give a doubly periodic {P,Q}-tiling.
On opposite carrier sides the P and Q subsegments can have different cut
locations. The resulting right-corner T contacts are permitted by the
unrestricted definition of tiling; no edge-to-edge assumption is imposed.

## A sufficient compatibility test for an independently specified pair

Reflect Q and choose its right corner corresponding to q2 as native
corner 0. Its angle word becomes Y, and its native side lengths are

    (delta2,delta4,L0,lambda,L1).

Therefore the same proof supplies a criterion for a given pair. If two
positive closed Y pentagons P and Q, normalized to the same theta, have

    length_Q(2)=length_P(0), length_Q(4)=length_P(1),

then their actual lengths, not newly chosen ones, already give this periodic
carrier. Put lambda=length_Q(3). The two Q closure equations force its
remaining lengths to be delta2 and delta4 as defined above. These are
positive because Q is a genuine pentagon. The convex-chain cancellation
and carrier argument require only their positivity, not the choice
lambda>S used to guarantee a distinct newly constructed partner. Thus any
already distinct pair satisfying these two edge equalities has a doubly
periodic tiling, even when its other lengths do not match whole sides.
This is a sufficient condition; no necessity or general classification is
asserted.

## Concrete exact instances and replay

The exact checker in
[general-y-pentagon-partner-verify.py](../searches/general-y-pentagon-partner-verify.py)
uses Sage AA, independently checks native angles, strict supporting sides,
the four-face chain and carrier coordinates, a complete overlap domain of
all lattice translates, and exact motif-area/lattice determinant equality.
Its direct coverage argument uses disjoint interiors, density one, and the
closed locally finite lattice union. This is also a planar-coordinate check
of the global carrier construction, independent of the flat-cover argument.

The finite domain contains k=2/5 and k=1/3, each with

    L1=2, L2=3, L3=1,
    L0=hL2+2khL3-kL1, L4=hL1+kL2-dL3.

All lengths are positive. These are points of the three-dimensional closure
cone outside the earlier two-parameter Y/Y family: if that family held with
t=L3, its second free parameter would satisfy s=(L1-hL3)/b,
b=d/(2k), and then L2=bL3+hs. The checker proves this last equality fails.
At k=2/5, theta/pi is irrational by 2cos(theta)=-4/5 being rational and
nonintegral. At k=1/3 the same argument uses -2/3.

Exact replay:

```text
conda run --no-capture-output -n arisearch python3 research/searches/general-y-pentagon-partner-verify.py
```

The replay environment is Python 3.12.13 and SageMath 10.9.
The completed replay checks 38 possible lattice overlaps for each of the
two instances (76 comparisons total). No solver, randomized seed, timeout
or memory cap is configured. The two
examples are finite exact checks of the analytic construction, not a finite
search promoted to an unrestricted theorem. Its general metric conclusion
rests on the formulas and complete proof above. Novelty and arbitrary
independently specified partner pairs are outside this artifact's claims.
