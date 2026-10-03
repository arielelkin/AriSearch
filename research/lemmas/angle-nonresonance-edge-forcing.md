# Angle-nonresonance forcing of edge-to-edge contacts

**Status:** proved.

**Review:** [angle-nonresonance-review](../reviews/angle-nonresonance-review.md).

## Theorem

Let $\mathcal P$ be a finite set of genuine compact convex polygons, written
without redundant straight vertices.  Let $\mathcal A$ be the finite
multiset of their labelled interior angles.  Suppose there is no nonempty
finite sequence $\alpha_1,\ldots,\alpha_k$ drawn from $\mathcal A$, with
repetition allowed, such that

\[
  \alpha_1+\cdots+\alpha_k=\pi.
\]

Then every plane tiling by $\mathcal P$, with arbitrary isometries and
contacts allowed a priori, is edge-to-edge.

## Proof

Tilings by a finite positive-area protoset are locally finite.  Suppose a
genuine tile vertex $p$ lay in the relative interior of some other tile side.
This covers an isolated vertex-to-side touch, a subdivision endpoint of a
positive-length interface, and the case where one coincident side continues
past the endpoint of the other.

In a sufficiently small disk about $p$, the tile whose side passes through
$p$ occupies an open half-disk.  The other half-disk cannot be occupied by
a second straight-through tile: that would leave no positive sector for the
tile having the genuine vertex at $p$.  Local finiteness therefore
partitions that half-disk into finitely many genuine polygon-corner sectors.
Their angles, counted with multiplicity, sum exactly to $\pi$, contradicting
the hypothesis.

Thus no vertex-to-side contact and no interface subdivision endpoint exists.
If two positive-length
coincident sides had unequal extents, an endpoint of the shorter would lie in
the relative interior of the longer, which has just been excluded.  Every
positive-length contact is consequently one whole native side of each tile,
so the tiling is edge-to-edge. $\square$

## Finite exact check and use

If $\alpha_{\min}>0$ is the smallest prototile angle, only sequences of
length at most $\lfloor\pi/\alpha_{\min}\rfloor$ need be checked.  For
algebraic angle data represented through exact roots of unity, or for angles
given as rational multiples of $\pi$, this is a finite exact rejection test.
Numerical noncoincidence is not a certificate.

Once edge-to-edge forcing is established, the possible tiling vertices are
exactly the finite angle multisets summing to $2\pi$.  This separates two
design tasks that the all-obtuse condition conflates: excluding T-junctions
requires avoiding sums of $\pi$, while selecting desired valences and corner
languages requires controlling sums of $2\pi$.

The all-obtuse theorem is the immediate special case in which one angle is
less than $\pi$ and any two angles sum to more than $\pi$; it additionally
forces every vertex to be trivalent.  Angle nonresonance by itself does not
bound valence and therefore leaves room for the positive-density
higher-valence defects required by a potential pentagon/hexagon encoding.
