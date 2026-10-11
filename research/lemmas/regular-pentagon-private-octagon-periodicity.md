# Periodic escape for a regular pentagon and an octagon with two private sides

**Status:** adversarially reviewed as valid for the strengthened direct
every-tiling theorem in the [fresh re-review](../reviews/regular-pentagon-private-octagon-periodicity-review.md). This is a restricted theorem, not a solution
of the unrestricted two-convex-polygon problem. No computation is used.

## Theorem and exact hypotheses

Let P be the regular unit-side pentagon. Let Q be a genuine compact convex
octagon with exactly two nonadjacent interior angles alpha=3pi/5 and six
interior angles beta=4pi/5. Suppose exactly six Q sides have length1, and
the remaining two sides have distinct positive lengths x,y, each different
from1. Then every admitted plane tiling by {P,Q} has a nonzero translational
symmetry. Consequently the pair either is untileable or admits a periodic
escape, and cannot be an aperiodic pair
under the [unrestricted problem definition](../../research-problem.md).

No positions of the two private sides are assumed in advance. Reflections,
rotations, partial contacts, and omission of either prototile are permitted
in the original tiling definition. The period is proved for each original
admitted tiling, including tilings with additional unit-side Q-to-Q contacts. No defect-free limit is needed.
Only one nonzero translation is established, without a rank-two lattice or
a finite band model.

## Local contacts and the private-edge graph

Let T be any admitted plane tiling. By the independently reviewed
[all-obtuse forcing theorem](obtuse-edge-forcing.md), all native sides match
completely and every vertex has three genuine corner sectors. The only
possible angle triple is (alpha,alpha,beta): three alpha sectors sum to9pi/5,
one alpha and two beta to11pi/5, and three beta to12pi/5. Thus two beta
corners cannot occur at the same vertex.

A Q side of length x or y cannot meet unit-side P. It therefore matches
the same unique-length native side of another Q copy. Nonadjacency of Q's
two alpha corners excludes an alpha/alpha side. A beta/beta private side
would match another beta/beta side and give two beta sectors at each endpoint,
which is impossible. Each private side consequently has alpha/beta endpoints.
Since both copies match that same native side, their endpoint correspondence
must be reversed: equal-type correspondence would give a forbidden beta/beta
endpoint. These statements apply in the original tiling, without saturation
or limiting arguments.

Form the graph whose vertices are Q copies, with edges only at their private
side contacts. Every vertex has degree2. The two neighbors are distinct:
interior-disjoint genuine convex polygons cannot share two different whole
native sides, because the convex hull of those noncollinear side segments
would have positive area in their intersection. No tile neighbors itself.
This is a simple degree2 graph. Additional Q-to-Q contacts at unit sides are
allowed, but are not edges of this private-contact graph.

At a P corner both side neighbors cannot be P: three alpha corners do not
sum to2pi. The P-to-P neighbor positions therefore form an independent set
in the cycle of five P sides and number at most2. In particular every P
has at least three Q side neighbors. This is a pointwise fact about T,
not an averaged tile-count statement.

## A private-side neighbor is a half-turn

Fix a reference Q and write e_x,e_y for its two private sides, with midpoints
a,b. Let FQ be any placed copy, where F is a plane isometry. Its neighbor
across e_x has form GQ. Because e_x is the unique side of length x, the
common side is G(e_x). Opposite alpha/beta endpoint correspondence forces
F and G to identify the two native endpoints in reversed order. Hence
F^(-1)G swaps the endpoints of e_x.

There are exactly two plane isometries swapping those two fixed points:
the half-turn H_a(z)=2a-z and reflection in their perpendicular bisector.
The latter preserves the half-plane containing the interior of reference Q.
If used for the neighbor, both copies would have interior on the same side
of the shared segment and would overlap in a small neighborhood of any
point of its relative interior. This is forbidden. The half-turn places
the neighbor on the opposite side of the supporting line. Therefore the
neighbor is precisely F H_a Q. The identical argument for y gives F H_b Q,
where H_b(z)=2b-z. This argument includes reflected F without fixing an
absolute orientation or imposing chirality.

The midpoints a,b are distinct: they belong to the relative interiors of
two different sides of a genuine convex polygon. Put d=b-a, so d!=0.

## Every private-contact Q chain has a straight axis and a two-step period

In each Q copy draw the closed segment joining its two private-side
midpoints. Its relative interior lies strictly inside that copy. Indeed
an open chord between boundary points on distinct genuine sides of a
convex polygon lies in its interior; a boundary chord would require both
points to lie on one supporting face, impossible here.

Starting at reference Q, follow the private-contact Q neighbor across e_y.
The next copy is H_b Q. Its midpoint chord joins b to H_b(a)=2b-a=b+d. Thus its chord
extends [a,b] along the same straight line, by exactly the same displacement d.
The next Q neighbor across its x side is

    H_b H_a Q = Q+2d.

Induction in both directions gives precisely the copies

    Q+2n*d,       H_b Q+2n*d,       n in Z.             (1)

Their successive chords are the segments

    [a+k*d, a+(k+1)*d],             k in Z.

They partition the entire affine line a+R*d. No finite cycle is possible:
following the chain advances this nonzero chord displacement, or, after two
steps, translates the compact polygon by nonzero2d. Degree2 in the
private-contact graph leaves no branch or additional chain member. Extra
unit Q-to-Q contacts do not alter this chain. In a placed chain the same
formulas are carried through its initial isometry F. Its axis is an exact line, and its tile set
is invariant under the nonzero translation

    u_F=2 L_F d,

where L_F is F's orthogonal linear part. All Q chains have period-vector
length2|d|, regardless of rotation or reflection. No bounded-width or
finite-state assumption has been used.

## Distinct chain axes are parallel

Distinct Q chains have disjoint midpoint-chord axes. To see this, a point
in the relative interior of a chord lies in the interior of its Q tile.
It cannot lie in any chord of another chain: that chord lies in another
closed Q tile, and a tile interior cannot contain any point of another tile
with nonempty interior without causing an interior overlap.

At a chord endpoint, the point is the relative interior midpoint of a
private side. Complete-side contact means that only the two Q copies
sharing that side occur in a sufficiently small neighborhood of the point.
A third tile cannot touch that midpoint: a native corner on it would
subdivide the side, excluded by all-obtuse forcing, and another straight
sector would conflict with the two half-neighborhoods already filled. Both incident Q
copies belong to the same chain. Thus endpoints cannot create an
intersection between axes of distinct chains either.

The axes are entire affine lines. Two nonparallel affine lines intersect,
so all Q-chain axes are parallel. Choose a period u from one chain. Since
every chain period is parallel to u and has the same length, its vector is
u or -u. Invariance under either sign is equivalent. Consequently translation
by u permutes all Q tiles of T, not merely their union of boundaries.

## Regular P propagates the common translation to the whole tiling

There is a unique regular unit pentagon on a prescribed side segment in a
prescribed supporting half-plane. Its center is the perpendicular-bisector
point at the fixed pentagon apothem, on the chosen side of the supporting
line; that center and the two side endpoints determine the polygon. Any
reflected or rotated placement satisfying these data gives the same
geometric copy. Thus there is no remaining endpoint or orientation choice
for the P neighbor across a given unit Q side.

Every P in T has at least three Q side neighbors, so choose one shared
side and its neighbor Q_0. Translation by u sends Q_0 to an existing Q tile
Q_0+u and sends that shared unit side to a side s+u. The actual neighbor
across s+u exists by whole-side contact. It cannot have type Q: if it did,
translating that Q copy by -u would give an existing Q tile across the
original side s, where the original P is already the unique neighbor. This
would contradict interior disjointness. Here invariance of the entire Q
tile set under both signs of u is essential; regular-P uniqueness alone
would not exclude a Q neighbor.

The actual neighbor across s+u is therefore P. By uniqueness of the regular
pentagon across that specified segment, it is exactly P+u. Translation by
u sends every P tile into the P tile set. The same argument with -u gives
the reverse inclusion.

Both the Q and P tile sets of T are invariant under u!=0. T is an admitted
plane tiling with a nonzero translational symmetry, proving the theorem.
There is no need to synchronize finite bands, pump cut states, establish a
second period, or assume finitely many absolute positions.

## Dependencies, scope, and remaining families

The sole nontrivial imported result is the reviewed all-obtuse full-edge
and trivalent forcing theorem. The prior octagon chain-limit theorem is
not required: chains here use only the two private edges, regardless of
other Q-to-Q contacts. All remaining arguments are elementary rigid geometry
of whole-side contacts and regular polygons. No solver, bounded
period search, algebraic-angle classification, or external monohedral
classification is used.

The theorem does not cover an irregular equiangular pentagon, equal private
lengths, additional unit or repeated nonunit Q sides, adjacent alpha corners,
or a different octagon angle signature. In those situations private contacts
may no longer fix a single half-turn, or the P placement may branch. Aperiodic
construction or unrestricted impossibility for those families remains open.
