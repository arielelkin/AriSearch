# Obtuse-angle edge-to-edge forcing

**Status:** Proved and hostile-audited.

**Review:** [obtuse-edge-forcing-review](../reviews/obtuse-edge-forcing-review.md).

## Theorem

Let a finite protoset consist of genuine compact convex polygons whose every
interior angle lies strictly between \(\pi/2\) and \(\pi\).  Then every plane
tiling by the protoset is edge-to-edge, and exactly three tile sectors meet at
every vertex.

## Proof

Finite positive-area prototiles give local finiteness.  Suppose a vertex
\(p\) of one tile lay in the relative interior of another tile's side.  The
straight-through tile occupies one open half-disk at \(p\).  In the other
half-disk, a single straight-through tile would leave no positive sector for
the tile having the genuine vertex \(p\); otherwise the half-disk must be
partitioned into genuine corner sectors.  One corner cannot fill angle
\(\pi\), because every angle is below \(\pi\), while two or more corners have
total angle greater than \(\pi\).  This is impossible.

Thus no tile vertex lies in another side's relative interior.  Any
subdivision endpoint of a positive-length interface would be such a vertex;
if one coincident side extended beyond the other's endpoint, that endpoint
would likewise lie in a side interior.  Every positive-length contact is
therefore a whole side of both tiles: the tiling is edge-to-edge.

At a tiling vertex there are now only genuine corner sectors.  Their sum is
\(2\pi\).  Since each is less than \(\pi\), at least three occur; since each
is greater than \(\pi/2\), at most three occur.  Hence exactly three meet.
\(\square\)

## Consequences

* Near-regular convex hexagons automatically close the problem's
  partial-edge and T-junction loopholes; all their tilings live on the
  honeycomb combinatorics proved elsewhere.
* Two obtuse pentagons cannot tile: the exact curvature identity with
  subdivision and valence defect both zero would give \(N=O(R)\), contrary
  to area growth.
* An aperiodic obtuse pentagon/hexagon pair is impossible: it would require
  positive-density defects by the pentagon-backbone theorem, while this
  theorem forbids every defect.
* Together with the side-count reductions, an all-obtuse aperiodic pair
  could only have side counts \((6,6)\) or \((5,n)\) with \(n\ge7\).

For the latter case, the square-window curvature identity has no subdivision
or excess-valence terms, so it sharpens to

\[
  N_5(R)-(n-6)N_n(R)=O(R)
\]

uniformly under translation of the window.  Since the tiles have uniformly
bounded positive areas, $N_5+N_n=\Theta(R^2)$.  Consequently both types
have positive uniform lower quadratic counts, and every Følner frequency
subsequence satisfies the exact ratio

\[
  f_5:f_n=(n-6):1.
\]

This rules out an all-obtuse construction in which the higher polygon is
only a zero-density defect.  It does not force bounded gaps between higher
polygons and does not establish periodicity.

These are necessary reductions, not an explicit construction.
