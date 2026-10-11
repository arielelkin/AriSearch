# Cairo pentagons with private right-angle arms: a doubled-side necessity

**Status:** proved and independently adversarially reviewed VALID (2026-10-10);
see [the hostile review](../reviews/partial-contact-cairo-t-host-review.md). This is a
necessary contact invariant and an unrestricted untileability corollary for
an explicitly restricted family. It does not resolve the main problem.

## Definitions and statements

A Cairo-angle pentagon has interior angles after successive sides
(a,b,c,d,e) equal to (90,120,90,120,120) degrees. Thus its four sides
a,b,c,d each join a90 corner to a120 corner, while e joins two120 corners.
Call the first four sides its right-angle arms. Every isometry, including
reflection, is permitted. Contacts need not be edge-to-edge.

Let P,Q be two such strictly convex pentagons. Assume the eight right-angle
arm lengths, as native slots of P and Q, are pairwise distinct. In particular
each length identifies one species and one arm slot. No assumption about
e_P,e_Q is needed in the first theorem.

**Contact theorem.** In every plane tiling by P,Q, every T-junction lies in
the relative interior of a native e side. That whole e side has length
2r, where r is one of the eight right-angle arm lengths. Each native side
has at most one T-junction.

**Untileability theorem (stronger).** Under the eight-slot private-arm
hypothesis alone, P,Q cannot tile the plane. Their e values may equal each
other, any arm value, or twice any arm value.

The same proof applies to any finite collection of Cairo-angle pentagons
whose four-per-species right-angle arm slots are globally pairwise distinct.
The two-species case is the case relevant to the main problem.

A species may be absent. The proofs cover this possibility by retaining
the same uniqueness assumption. No monohedral classification is used.

## Allowed stars and the whole perpendicular seam

At a native vertex any incident tile contributes a90 or120 corner, or a
straight180 sector. A straight sector is unique. The integer angle equations
are 90u+120v=360 or 90u+120v=180. They give only full90^4, full120^3,
and half90^2. Consequently a120 corner can neither occur inside a native
side nor coincide with a90 corner, and every native subdivision point is a
T-junction with two90 corners opposite one straight180 sector.

At such a T point x, the two90-corner tiles meet along a perpendicular ray.
Each of their native sides on this ray joins90 to120: the polygon has no
side joining two90 corners. Both tiles occupy the respective half-wedges
on this ray, so a third tile cannot meet the ray before either side ends.
If one native side were shorter, its120 endpoint would lie inside the
other's side, which the star equation forbids. Thus this perpendicular
seam is an entire native side of each tile, and their120 endpoints
coincide.

The equal lengths, by the eight-slot uniqueness hypothesis, identify the
same species and native arm slot on both sides. Both copies identify the
same90 endpoint of that slot. The only isometry identifying the slot with
these endpoint labels while taking interiors to opposite sides is reflection
in its line. Therefore the two other native arms at x extend along opposite
rays of the host line, have the same length r, and end at120 corners at
x-r and x+r in signed host-line coordinates.

## A right-to120 side cannot host a T

Suppose a host side of length L joins a120 corner to a90 corner and contains
x as an interior T. Orient its line so the120 host endpoint is left of x.
The opposing arms from the preceding paragraph extend length r on both
sides of x and end at120. The host's left120 endpoint must coincide with
the opposing120 endpoint x-r: either ordering otherwise puts a120 corner
inside a native side. Its right90 endpoint y must occur strictly between
x and x+r: the endpoint cannot pass the opposing120 corner or coincide
with it. Write y=x+h with 0<h<r. Hence L=r+h.

At y the original host tile contributes90 and the opposing tile contributes
straight180. The missing90 tile creates another T. Its perpendicular seam
is again full and identifies the same native slot on the original host
and the new tile, by uniqueness. Reflection across that seam forces the
new tile's collinear arm to extend forward from y a distance L, ending
at120 at x+h+L=x+r+2h.

The existing opposing tile ends its side at120 at x+r, strictly inside
this new side, since h<r and h>0. This is forbidden. The contradiction
excludes all right-to120 host sides, without a bound on the number of
subdivisions or an assumed full-side match on the host line.

## An e side forces the doubled equality

The only remaining possible host is an e side with both endpoints120.
Apply the same reflection conclusion at its T point x. Its two endpoints
must coincide with x-r and x+r, since any other ordering puts120 inside
an opposing or host native side. Thus e=2r.

There can be at most one interior T on any native side even without the
private-arm hypothesis: at any first T, the opposing native side in the
forward host direction ends at120. It must reach the host endpoint, since
120 cannot lie inside a native side; before it ends, both sides of the
host segment are occupied by the fixed host and this opposing tile. A
second native vertex on this open segment has no available sector.
Equivalently, two consecutive host subdivisions would require an opposing
native side joining two90 corners, which neither polygon has.

This proves the contact theorem. It now gives a stronger local obstruction.

## A beta ray matching an arm: exactly two alternatives

At a120 star, start along a native arm of length r of one incident tile.
An opposing native arm has the same length and endpoints: a shorter arm
would put90 in the interior of an arm (the excluded host case), and an
equal-endpoint mismatch90/120 is impossible. Uniqueness then identifies
the same species and native arm slot, with the two copies reflected in
the arm line.

The only other possible opposing native side is an e side. It cannot be
shorter than the arm, since its120 endpoint would be inside the arm, and
cannot have equal length, since120 would coincide with90. Hence the arm
ends at a T inside that e side. By the contact theorem the e side has
length2r. These two alternatives include every possible contact on an
arm ray from a120 vertex.

## The isolated120 arms b,c cannot be banks of a T host

Suppose an e side of a tile H hosts a T whose opposite bank tiles are
reflected copies of a tile S. Let the collinear bank arm r of S be b_S
or c_S. The120 endpoint of r is the isolated120 corner between b_S,c_S;
write q for its other arm. At that120 endpoint the host H contributes120
and its other incident side is p=a_H or d_H. The remaining sector is120
and belongs to a third tile K. Its two sides there face the arm rays p,q.

At least one of K's two incident sides is an arm, since K has just one e
side. If its side facing p is an arm, it identifies species H and slot p.
Its120 endpoint is consequently the e-adjacent120 corner of H, so its
other side is e_H. That other side faces q and must host it by the preceding
alternatives; hence e_H=2q. But the original host already had e_H=2r.
This contradicts b_S!=c_S.

If instead K's side facing q is an arm, it identifies species S and slot q.
Its120 endpoint is the isolated120 corner of S, so K's other side is arm r.
That side faces p and must match its arm length. But r is a b/c slot and p
an a/d slot, different globally unique slots even when H=S. This too is
impossible. The cases overlap harmlessly if K has two incident arms.

Thus neither isolated120 arm b nor c can be opposed by an e side anywhere
in a tiling. Every such arm must have a whole identical-slot arm mate.

## An isolated120 star is impossible

Take the isolated120 corner of any tile S, between its sides b_S,c_S.
Its neighboring tile across b_S must have exactly the same native b slot
and the same labeled120 endpoint, hence is S reflected across this arm.
These two tiles each expose their other c_S arm as the boundary of the
remaining120 sector. The third tile would have two incident sides of
length c_S on these rays. Neither side can be an e side, because c_S
cannot be a bank of an e-hosted T. Both would therefore be native arms
of the same globally unique c slot. A polygon cannot have the same native
side slot on two distinct rays at a corner. This is the final contradiction.

Every tile has this isolated120 corner, so no tiling exists. This proof
is local and uses neither an ETE assumption nor an ETE classification.
It remains valid for a species disappearing, and for more than two species
under global uniqueness of all their arm slots.

## Exact nonempty family and replay

Put w=sqrt3, the positive root of t^2-3 isolated by 1<w<2. A Cairo pentagon
with free positive lengths c,d,e has closure

    a=(w*c+d-e)/2,  b=(w*(d+e)-c)/2.

Use P with (c,d,e)=(1,2,3) and Q with (c,d,e)=(4,5,6). All five lengths
of each are positive and distinct, all eight arm slots are pairwise
distinct, and neither e is twice any arm. Exact vertices are

    (0,0), (a,0), (a,b),
    (a-w*c/2,b+c/2), (-e/2,w*e/2).

The last-side direction is300 degrees; the other side directions are
0,90,150,240 degrees. Exact supporting determinants certify strict
convexity. These two explicit polygons are therefore untileable together
under unrestricted contacts. The argument also excludes all metrics
satisfying the stated inequalities and non-equalities, a nonempty open
subset of the six-dimensional pair metric cone.

Replay the deterministic exact verification:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-private-arms.py

The script verifies the two fixtures and the finite angle equations over
QQ(sqrt3). It is not a search for tilings and does not verify the geometric
contact proof by itself. No bounded tiling enumeration or floating-point
arithmetic enters the theorem. Its finite domain is two fixed polygons,
all supporting-edge tests, their10 side lengths, the8 arm slots and
2x8 doubled-length comparisons, plus u=0..4,v=0..3 for each star equation.
No random seed, symmetry quotient, timeout or certificate is involved.

## Dependencies, scope and gaps

The proof has no imported tiling classification or previously proved
ETE-obstruction dependency. Every contact step is proved above. The proof
does not assume periodicity, a source tiling, matching marks or a finite
orientation group.

Every tileable Cairo-angle pair must have a repeated arm value among its
eight native90-to120 arm slots. If each polygon's four arm values are
internally distinct, a cross-species arm equality is therefore necessary.
A doubled e value alone does not evade this theorem. Existence, periodicity
and nonperiodicity when arm values repeat remain unclassified here. No statement that generic untileability resolves the unrestricted
two-polygon problem is made. No novelty claim is made. The proof and exact fixtures passed the
independent hostile review; primary-literature priority remains unassessed.
