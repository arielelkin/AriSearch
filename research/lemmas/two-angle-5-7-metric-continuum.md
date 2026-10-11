# Full metric cone and generic periodic rigidity for a pentagon--heptagon pair

**Status:** adversarially reviewed VALID in the [independent full-domain review](../reviews/two-angle-5-7-metric-continuum-review.md), with a separate exact checker. This is a genuine four-dimensional continuous metric
classification, extending the previously retained single periodic instance.
It also classifies every generic tileable pair with exactly four shared
side-length values. A separate analytic chain argument forces a nonzero period also when
all five P lengths are shared. Repeated side lengths remain outside the
theorem.

## The exact shared-order family and theorem

Let alpha=4pi/7 and beta=5pi/7. Consider an equiangular heptagon H with
counterclockwise consecutive side lengths l0,...,l6, and a pentagon P whose
consecutive angles are (beta,alpha,alpha,alpha,alpha). In clockwise order
starting at beta, suppose P's consecutive side lengths are

    (l6,l1,l3,l5,p).

Reflections are allowed, so this choice of clockwise order imposes no
chirality restriction. This is an intrinsic shared-length/order family,
not an imposed rule on placements. All lengths are positive.

Put t=2cos(pi/7), the unique root of

    t^3-t^2-2t+1=0, 18/10<t<181/100.

Every pair in this family is parametrized uniquely by
(a,b,c,d)=(l1,l2,l4,l6) with

    l3 = t*d - (t^2-1)*b/2 + c/2,
    l5 = (t-1)*a + b/2 + (-t^2+t+1)*c/2,
    l0 = (-t^2+t+1)*a + (t^2/2-t-1/2)*b
         + (t-1/2)*c + d,
    p  = (t^2-t-1)*a - (t^2-1)*b/2 + c/2 + d.          (1)

Its full positive metric cone is precisely

    a,b,c,d,l0,l3,l5,p > 0.                            (2)

All eight inequalities are irredundant. The cone has dimension four,
nine extreme rays in its closure, and dimension three after common scale.
Every point of this cone admits the four-orbit doubly periodic tiling
specified below. If the eight lengths l0,...,l6,p are pairwise distinct,
every unrestricted tiling by this pair is that periodic tiling up to a
global isometry. Thus the generic members force periodicity by their
unmarked geometry, and no member of this cone is an aperiodic pair.

Here “unrestricted” includes reflections, partial-edge contacts, and a
potential tiling using only one type. No extra matching rule is assumed.

**Broader generic classification.** Suppose H has seven distinct side
lengths, P has five distinct side lengths, and both have the preceding
angles, without prescribing which lengths agree or their order. If their
side-length sets intersect in at most three values, the pair is untileable.
If they intersect in exactly four values and the pair tiles, an allowed
cyclic renumbering/reflection puts the pair in (1)--(2). Every tiling is
therefore doubly periodic. With exactly five common values every admitted tiling still has a nonzero
period, by the midpoint-chain argument below. Therefore no pair in this
angular family whose sides are internally distinct can be aperiodic.
The shared-order cone gives the finer doubly periodic metric classification
when exactly four values agree; it is not needed for the one-period theorem.

## Local constraints force the shared-order family

All angles are strictly obtuse, so partial-edge contacts are impossible:
a straight sector would require at least two genuine corners whose sum
already exceeds pi. All vertices have exactly three corners, with one
alpha and two beta, by 4r+5s=14. Alpha corners belong only to P.

H must occur in any admitted tiling. A hypothetical P-only tiling would
have private edges on every side, each necessarily P-P. An alpha--alpha
side cannot meet P across its full edge: both possible alignments make
an endpoint contain two alpha sectors. P has three alpha--alpha sides,
so no P-only tiling exists. A hypothetical H-only tiling is impossible
because no full vertex can supply an alpha sector. Thus both types occur.

Let an H side have a length absent from P. Distinct H lengths force it
to meet the identical numbered side of another H. Reflection across the
side line pairs beta corners with identical external adjacent lengths;
the required third sector is a P alpha corner with two equal sides,
contradicting distinct P lengths. Only the half-turn is possible. Its
endpoint external edges have the two lengths adjacent to the private H
side, and both must be sides of the incident P. Hence both neighboring
H sides are shared, and private H sides form an independent set in the
seven-side cycle. Such a set has size at most three. If at most three
values are shared, there are at least four private H sides, a contradiction.

With exactly four shared values there are exactly three private H sides.
The three cyclic gaps between them are at least two and sum to seven;
they are (2,2,3). Up to cyclic renumbering and reflection the private
sides are 0,2,4 and the shared sides are 1,3,5,6. At their endpoints the
required P alpha corner has side pair respectively

    {l6,l1}, {l1,l3}, {l3,l5}.

Distinct side lengths force these three adjacency pairs to form a single
path through P's four shared sides. Its fifth side, private length p,
joins the path ends. The beta corner cannot be one of the three forced
alpha corners, so it lies at one of the two p endpoints. Thus P's cyclic
order is (l6,l1,l3,l5,p) with beta between p and l6, or its endpoint-swapped
version. Reflecting/renumbering H by j -> 4-j exchanges these versions.
This is exactly the shared-order family of the theorem; its closures
therefore force (1), and its positive lengths force (2). No period search
or assumed lattice structure enters this reduction.

## Coordinates and the complete metric derivation

Let z=exp(2pi*i/7) and e_j=l_j*z^j. Choose h0=0 and
h_(j+1)=h_j+e_j. A closed H has sum e_j=0. Put

    d_j=h_j+h_(j+1), j=0,2,4,
    u=d2-d0, v=d4-d0, q=d0-d2+d4.

The clockwise pentagon has vertices

    P=(h6, 0, d0-h2, d0-d2+h4, q-h6)
     =(-e6, 0, -e1, -e1+e3, -e1+e3-e5).              (3)

Its first four directed sides are e6,-e1,e3,-e5, and its
last side is e1-e3+e5-e6. For the desired angles this last side must be
positive real, of length p. The clockwise turns are 3pi/7 at the four
alpha corners and 2pi/7 at beta.

Write s1=sin(pi/7), s2=sin(2pi/7), s3=sin(3pi/7), so
s2/s1=t and s3/s1=t^2-1. The two imaginary closure equations are

    s2*a+s3*b+s1*l3-s1*c-s3*l5-s2*d=0,
    s2*a-s1*l3-s3*l5+s2*d=0.

They solve uniquely for l3,l5. Real H closure solves l0, and the real
pentagon closing side solves p. Using the displayed minimal polynomial
of t gives exactly (1). Conversely (1) gives both closures identically.
A polygon with positive sides in cyclically turning directions and total
exterior turn 2pi is globally strictly convex: relative to any one edge,
the cross-products of subsequent increments are first positive and then
negative; their total is zero by closure, so every intermediate vertex
lies strictly on the interior side of that edge. This proves global
convexity of H and, with reversed orientation, P for every point of (2).
No additional nonlinear feasibility condition is missing.

The previous fixture is a=b=c=d=1. A generic exact member is

    (a,b,c,d)=(1,11/10,6/5,9/10),

for which all eight lengths in (2) are positive and distinct.

## Whole-plane tiling for the entire cone

The four placements are

    H0=H, H1=-H+d0, P0=P, P1=-P+q

modulo the lattice L=Z*u+Z*v. In the following table, a row pairs side j
of its first tile with side k of its second tile shifted by m*u+n*v.
R reverses the two physical endpoints, S preserves their order. H is
counterclockwise and P clockwise, so both cases give opposite boundary
orientations in the oriented polygon complex.

| First | j | Second | k | m | n | Endpoint order |
|---|---:|---|---:|---:|---:|---|
| H0 |0|H1|0|0|0|R|
| H0 |2|H1|2|1|0|R|
| H0 |4|H1|4|0|1|R|
| H0 |6|P0|0|0|0|S|
| H0 |1|P1|1|1|-1|S|
| H0 |3|P0|2|1|0|S|
| H0 |5|P1|3|0|0|S|
| H1 |6|P1|0|1|-1|S|
| H1 |1|P0|1|0|0|S|
| H1 |3|P1|2|0|-1|S|
| H1 |5|P0|3|1|-1|S|
| P0 |4|P1|4|0|0|R|

Every side is paired exactly once. These are coordinate identities for
all (a,b,c,d), not approximate coincidences. The identifications give eight
vertex links, each with three corners of angles alpha,beta,beta, and
therefore each of total angle 2pi. The complex is connected and orientable,
with Euler characteristic 8-12+4=0. It is thus a flat torus. The displayed
coordinates develop it into R^2/L and the seam identities make this map
well defined. Convexity, opposite side interiors and the full vertex links
make it a local homeomorphism at interior, side and vertex points.

The formal signed shoelace identity is

    det(u,v)=2*area(H)+2*area(P)>0.                     (4)

Thus L has rank two. A compact connected local homeomorphism onto R^2/L
is a finite covering. The degree is its total polygon area divided by the
lattice covolume; (4) makes this degree one. Hence it is a homeomorphism.
Lifting to the plane proves that the four lattice orbits have disjoint
interiors and cover the entire plane. This is a global proof for every
positive parameter, without a bounded overlap extrapolation or sampled
parameter verification.

## Shape-only periodic rigidity when the eight lengths are distinct

Because alpha and beta are both strictly obtuse, a straight sector cannot
meet genuine corners: even two such corners exceed pi. Every tile contact
is therefore edge-to-edge. Each full vertex has exactly three genuine
corners, and 4r+5s=14 with r+s=3 forces one alpha and two beta sectors.
An alpha corner belongs only to P.

Any edge of length l0,l2 or l4 occurs only in H, at one numbered side.
It must therefore join two H copies on the same numbered side. Given the
matched side and opposite interiors, the possible relative placements
are a half-turn about the side midpoint or reflection across its line.
Reflection pairs equal-index beta corners. At either endpoint its two
external sides then have the same length. The remaining sector must be
an alpha corner of P whose adjacent sides would have that same length,
contradicting distinct P side lengths. The only possible gluing is the
half-turn.

There is an H in any tiling. Otherwise the edge of P of private length p
joins two P copies. Reflection would place two alpha corners at one seam
endpoint, contrary to the one-alpha star. The required half-turn leaves
a beta sector at each endpoint whose two sides have lengths l5 and l6.
This cannot be P's beta corner, which has adjacent lengths p and l6.
It must be a corner of H. This contradicts the assumption of no H.

Now fix any H placement as H0. The forced half-turns across its private
sides 0,2,4 are the maps x -> d0-x, d2-x, d4-x. Their generated group
contains translations u=d2-d0 and v=d4-d0. Thus the tiling contains
all copies H0+L and H1+L. At each endpoint of their side-0 seam the
remaining sector is a P alpha corner with adjacent lengths l6,l1.
That numbered corner is unique and its two directed incident rays fix
its entire placement, including the reflection choice. These force
P0+L and P1+L. The four orbits already cover the plane by the previous
section, so no additional tile is possible. The original tiling is
exactly this doubly periodic one.

This argument handles possible reflected initial H placements by taking
that placement as the global coordinate frame. Local reflections at private
seams are excluded by the actual side lengths, not by a convention.

## A nonzero period for every internally distinct-side pair

This argument does not prescribe a shared-length order or require exactly
four common values. Suppose H has seven distinct side lengths and P has
five distinct side lengths, with the same alpha/beta angles as above, and
suppose a plane tiling exists. Since P has only five length values, choose
two distinct H side lengths absent from P. At either private H side, the
preceding local argument forces half-turn H-H gluing. This holds at every
H copy and respects every reflected orientation.

In the native H let M and N be these side midpoints and put

    U=2*(N-M), |U|>0.

Inside each H draw the chord from M to N. Strict convexity puts its open
segment inside H. The adjacent half-turn H makes the next chord the
straight continuation through the shared midpoint, so the selected private
sides generate a doubly infinite straight chain through H copies. Two
successive half-turns translate a chain tile by the image of U. Every
chain is a complete Euclidean straight line. Distinct chains cannot cross:
away from seam midpoints this would put two H interiors over the same
point; at a midpoint the only incident H are the two belonging to that
same chain, by edge-to-edge contact. Thus all chain lines are parallel.
Congruence fixes their two-step translation magnitude |U|, including
reflected H copies. Choosing one direction along their common line gives
a single vector u of length |U| such that the whole set of H copies is
invariant under both u and -u.

It remains to transfer the scaffold period to P. A P-P seam must match
the same numbered side, because P's five lengths are distinct. A side with
two alpha endpoints cannot have a P neighbor, since an endpoint would
contain two alpha sectors. Across a beta--alpha side, reflection creates
an alpha--alpha endpoint and is likewise forbidden. Thus every P-P seam
is a half-turn and has alpha+beta at each endpoint.

At P's unique beta corner the alpha sector must come from another P.
The remaining beta sector cannot also be P: two P beta corners at a
vertex share a full edge there, which would require the forbidden
reflection alignment and an alpha--alpha endpoint at its other end.
Consequently the beta star is P_beta+P_alpha+H_beta. Exactly one side
incident to that beta corner is P-P, and the other is P-H by the same
three-sector star. The remaining three sides have alpha--alpha endpoints
and cannot be P-P. Every P therefore has
exactly one P neighbor along a side, and its other four sides have H
neighbors. Of its four alpha corners, the one at the far end of the P-P
side has a P_beta+H_beta neighbor pair. Each of the other three alpha
corners has two H_beta neighbors.

Choose one such H-H-P corner of an arbitrary P. Translating the two H
neighbors by u leaves an actual pair of H tiles at the translated vertex,
with the same free alpha sector and the same two adjacent native edge
lengths. The third tile is necessarily P. Distinct P side lengths identify
its numbered corner uniquely from this adjacent pair, and the two actual
edge rays fix its isometric placement, including any reflection. It must
therefore be the translated copy P+u. Applying the same argument to -u
proves that the whole P set is invariant under u. The original unrestricted
tiling has the nonzero translational symmetry u.

In particular the fifth shared-length case cannot restore aperiodicity.
Its metrics and all possible torus structures are not classified here;
the already forced one-dimensional symmetry suffices to exclude it from
the aperiodic-pair search. Repeated side lengths are the exact loophole:
they can invalidate private-side uniqueness, prohibit the reflection
argument, or make an H-H-P corner fail to identify its entire P placement.

## Exact computation, review and remaining obligation

The certificate
`research/certificates/two-angle-5-7-metric-continuum.json` retains all eight
inequality coefficient vectors over Q(t), all nine cone rays, a relative
interior point for each irredundant facet, the twelve seam identifications,
and the eight vertex links. The producer
`research/searches/two-angle-5-7-metric-continuum.py` independently derives
all 56 triple-active ray candidates by exact linear algebra; it uses no
polyhedron backend or floating branches. It symbolically reconstructs (3)
over Q(zeta28)[a,b,c,d], verifies every seam and vertex link, and checks (4).

```text
conda run --no-capture-output -n arisearch python research/searches/two-angle-5-7-metric-continuum.py
```

Default replay prints JSON without overwriting the retained certificate.
The [first independent review](../reviews/two-angle-5-7-metric-continuum-review.md) and [fresh second hostile review](../reviews/two-angle-5-7-metric-continuum-second-review.md) both return VALID for the continuum proof, coincident-length existence, generic rigidity and arbitrary-order internally distinct period theorem. Their independent exact checkers cover the cone, fixture geometry and all eight actual corner links with zero lattice holonomy.

The genuine remaining aperiodic metric issue in this angular family has
repeated side lengths on at least one prototile. Such coincidences may
permit reflected seams or different P placements at the same scaffold
corner. The five-shared internally distinct case is now excluded by a
forced single period, although its exact metric feasibility/torus
classification is not claimed. Formula (1) and the local reduction must
not be cited as a classification of all two-angle(5,7) pairs.
