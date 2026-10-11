# A periodic escape for a scalene equiangular pentagon and a private-edge octagon

**Status:** adversarially reviewed VALID in the [independent audit](../reviews/private-chain-distinct-pentagon-review.md), and superseded by the [universal original-tiling theorem](private-octagon-adjacent-corner-rigidity.md). This extends the
reviewed straight private-chain mechanism to pentagons with distinct lengths.
It proves existence of a periodic escape when the pair tiles, not periodicity
of every original tiling. The original unrestricted problem remains open.

## Theorem

Let P be a genuine compact convex equiangular pentagon, with all angles
alpha=3pi/5 and five pairwise distinct native side lengths. Let Q be a genuine
compact convex octagon with two nonadjacent alpha corners and six
beta=4pi/5 corners. Suppose Q has two native side lengths x,y such that

- x and y are distinct;
- each occurs on exactly one native side of Q; and
- neither occurs among the side lengths of P.

If {P,Q} admits any plane tiling under the original unrestricted definition,
then it admits a plane tiling with a nonzero translational symmetry. Therefore
such a pair cannot be strongly aperiodic. No condition on the other six Q
lengths, absolute orientations, reflections, or original edge subdivisions
is imposed.

## Dependencies and why a limit is used

The [reviewed all-obtuse theorem](obtuse-edge-forcing.md) makes every admitted
tiling edge-to-edge and trivalent. The
[reviewed octagon chain-limit theorem](obtuse-pentagon-octagon-chain-limit.md)
provides another admitted whole-plane tiling T in which each P has two
nonadjacent P side neighbours and exactly one P,Q,Q corner, while each Q
has exactly two Q neighbours. Every Q-to-Q seam has alpha/beta endpoints on
both copies, in opposite correspondence; every endpoint star is P,Q,Q.
These are precisely the theorem's hypotheses, without a new limiting step.

We use this good limit T, rather than asserting that an original tiling with
possible sparse defects already has the saturated contact structure. It is
enough to find one period-bearing admitted tiling to refute strong aperiodicity.
Neither prototile may disappear in this limit: the chain-limit theorem
establishes these neighbour relations for every tile, and no all-obtuse
pentagon-only or octagon-only plane tiling exists.

## Actual private seam isometries

Every x- or y-side must meet another Q, since it cannot match any side of P.
Each Q already has exactly two Q sides in T, so those are exactly its two
private sides. A beta/beta private side would have to match the identical
unique native beta/beta side of a second Q and give two beta sectors at an
endpoint, impossible. Q has no alpha/alpha side by nonadjacency of its alpha
corners. Thus both private sides are alpha/beta sides.

Because each private value occurs only once on Q, matching copies use the
same native side. The endpoint correspondence must exchange alpha and beta.
The isometry carrying the reference copy to its neighbour therefore exchanges
the two endpoints of that native side and carries its interior to the opposite
side of the supporting line. The unique such Euclidean isometry is the
half-turn about the side midpoint. (The alternative reflection exchanging
endpoints is reflection in the perpendicular bisector and preserves the
interior half-plane, hence overlaps.) This argument permits reflected
reference placements: if F places one Q, its neighbour is F composed with
the native half-turn.

## Every Q belongs to a straight chain with a common period

Let a,b be the distinct midpoints of the two private native sides, and set
u0=2(b-a), a nonzero vector. Draw the chord[a,b] inside each Q. Across a
private seam, the neighbour chord is the half-turn image of this chord about
its shared endpoint. Thus the two chords concatenate in a straight line.
Every Q has two such seams, so its chain extends in both directions.
Starting from F(Q) and crossing the b-side then the a-side gives

    F(Q) -> F(2b-Q) -> F(Q+2(b-a)).

Consequently its entire chain is invariant under the nonzero translation
u_F=L_F*u0, where L_F is the orthogonal linear part of F. Every chord has
positive fixed length and straight continuation, so the chain cannot close
into a finite cycle and its concatenation fills its whole infinite axis.

Two distinct chain axes cannot meet. An open chord lies inside its Q
interior. If a point belonged to chords of distinct chains with at least one
open chord, either two tile interiors would intersect or a boundary point
of one tile would lie inside another tile, which is also impossible for
compact convex tiles with disjoint interiors. If both chords end there,
the point is a native side midpoint. Full-side matching allows only the two
copies sharing that side; they lie in the same private chain. Thus distinct
axes are disjoint straight lines and hence parallel.

All u_F are therefore parallel and have the same length|u0|, even with
reflected copies. Choose u from one chain; every other chain is invariant
under u or -u and thus under u. Since every Q belongs to one such chain,
the entire set of Q occurrences in T is invariant under u.

This is the same midpoint-chord mechanism as in the
[reviewed regular-pentagon theorem](regular-pentagon-private-octagon-periodicity.md),
whose period proof does not depend on the geometry of the pentagon.

## Unique pentagon completion at its P,Q,Q corner

At a P,Q,Q corner the two Q occurrences prescribe the remaining alpha
wedge and both whole side segments of P incident to that corner. Their
lengths form an unordered pair of distinct P lengths.

In a five-cycle whose edge lengths are pairwise distinct, that unordered
adjacent pair appears at exactly one native vertex: each numerical length
identifies a unique native side, and two different sides share at most one
native vertex. At that vertex, assigning the two different lengths to the
two prescribed rays fixes the Euclidean placement uniquely. Reflections do
not introduce a second placement: swapping the rays would swap unequal
lengths. Thus at most one actual placed copy of P fills those two prescribed
segments and the alpha wedge.

Every P in T has exactly one such P,Q,Q corner by the chain-limit theorem.
Translation by u carries its two neighbouring Q copies, their shared vertex,
and the prescribed P side segments to identical translated data in T. The
third sector there must again be a P sector: the good tiling's Q-to-Q seam
endpoints are all P,Q,Q. The preceding uniqueness forces that P to be
exactly the original P translated by u. Applying the same argument to -u
shows bijection, not merely one-sided inclusion. Every P occurrence is
therefore invariant as a set of tiles under u. Together with the Q set,
this proves that T has the nonzero period u.

## Scope, review obligations, and next boundary

The proof uses no computation, rational-length assumption, or imported
monohedral classification. It gives a theorem for arbitrary real length
values under its explicit private-side and internal-distinctness assumptions.
Regular P has a different symmetry-based uniqueness proof; its five equal
lengths do not satisfy this theorem's distinctness hypothesis.

The exact broader rigidity condition is that every pair of incident side
segments and its alpha wedge determine at most one placed P copy. The proof
would remain valid under that intrinsic condition. Repeated lengths whose
adjacent pairs admit different placed polygons are outside the present
statement. Octagons with repeated private values, adjacent alpha corners, or only one
private length remain outside it. Extra unshared lengths satisfy the stated
hypotheses but force untileability: in the good limit the two private sides
x,y already consume every Q-to-Q side slot.

A fresh reviewer should attack midpoint-chain continuation with reflections,
all-chain period agreement, native wedge uniqueness, defect-limit scope and
the possibility of P omission. The theorem is not promoted before that review.
No novelty claim is made.
