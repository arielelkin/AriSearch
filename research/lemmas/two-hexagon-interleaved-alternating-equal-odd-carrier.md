# Equal odd A sides: an explicit periodic triangular carrier for I/ALT hexagons

Date: 2026-10-12. Status: [fresh hostile review VALID](../reviews/two-hexagon-interleaved-alternating-equal-odd-carrier-review.md).

In the exact same-colour rank-nine family, let A have native angle word
(p,p,q,p,q,q), q=240-p, and let B have native word(r,s,r,s,r,s),
r=360-2p, s=360-2q. Assume 90<p<150, p!=120 and the three odd A
side lengths are equal to l>0. Every B side is then l by the reviewed
[private-seam alphabet lemma](two-hexagon-interleaved-alternating-private-seams.md).
For ANY actual strictly convex A,B with these data, there is an admitted
periodic tiling. The construction uses reflected copies and fills the plane.

## Equilateral carrier triangle and the removed corners

Write theta=p-120 degrees, alpha=60-theta=180-p and beta=60+theta=180-q.
Let a0,a2,a4 denote A's even side lengths. Set

    d=2*l*sin(theta)/sqrt(3),
    P=l*cos(theta)-l*sin(theta)/sqrt(3),
    Q=l*cos(theta)+l*sin(theta)/sqrt(3).

Both P,Q are positive because |theta|<30 degrees. The native side directions
of A are 0,alpha,120,120+alpha,240,240+beta. Its odd-vector sum is
l*sin(theta)*(sqrt(3),1). Polygon closure consequently implies

    a0=a2-d, a4=a2+d.

The support lines of A's three even sides, directions0,120,240, enclose an
equilateral triangle T. A is precisely T with its three corners cut off
by the three odd sides. Each removed corner triangle has base l and
angles(alpha,beta,60), with its two carrier-side legs P,Q by the sine law.
The carrier side lengths, computed from the even sides and their two tails,
are respectively

    a0+2Q = a2+P+Q = a4+2P = L=a2+2*l*cos(theta)>0.

The removed triangles have pairwise disjoint interiors because their
intervening even A sides have positive lengths. All three removed triangles
are congruent, even when the p,q endpoint order reverses on the third cut.

For explicit coordinates orient A side0 from(0,0) to(a0,0). Then T has vertices

    (-Q,0), (a0+Q,0), (a0/2,sqrt(3)*L/2).

These statements follow by intersecting the even supporting lines, or by
the three equal carrier-side length identities above; no drawing determines
the dissection.

## Reflection tiling and the B holes

Reflect T in its three sides to obtain the ordinary equilateral triangular
plane tiling. Assign to every carrier triangle the corresponding reflected
copy of A. The assignment is consistent around vertices: the carrier angle
is60 degrees, and the six successive incident-edge reflections give the
identity after one full turn. Equivalently colour the triangular-lattice
vertices by m+2n modulo3 in the lattice basis (L,0),(L/2,sqrt(3)*L/2).
Every triangle has all three colours, and its unique colour-preserving
isometry from the original labelled T gives the assigned copy of A.
Adjacent assignments agree by reflection in their common side.

Around each carrier vertex, the six congruent removed triangles form one
hole with six boundary sides, all of length l. The hole is a simple
six-triangle fan: every triangle lies in a distinct carrier sector. Across
each carrier edge the cut endpoint is fixed by reflection. The two incident
A corner angles at that endpoint are both p or both q, giving hole angle
360-2p=r or360-2q=s. Each cut edge has one p and one q endpoint, so those
six hole angles alternate r,s. They are all strictly between0 and180
degrees, so the simple hole is a genuine convex hexagon. A cyclic sequence
of side lengths and angles determines a polygon up to Euclidean isometry;
the hole is therefore congruent to B. Fill every hole by that B copy.

No gaps remain: every carrier triangle is partitioned into its A part and
three removed corner triangles, and all those removed parts are exactly the
filled vertex holes. Interiors are disjoint. The three-colour carrier
assignment is periodic under a finite-index triangular translation lattice
(for example translations by three times both carrier basis vectors).
Those translations preserve every A and B placement, yielding an admitted
periodic whole-plane tiling. QED.

This is a positive periodic escape, including all actual even A side lengths
satisfying polygon closure and positivity. It makes no assumption of a
previous infinite tiling except when invoking the private-seam lemma to
force equilateral B. It is not a claim that every original partial-contact
tiling follows this reflected carrier, nor a construction of an aperiodic pair.
