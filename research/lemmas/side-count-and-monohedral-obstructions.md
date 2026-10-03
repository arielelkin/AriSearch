# Side count and monohedral obstructions

**Status:** elementary monohedral and torus arguments checked internally;
global side-count argument adversarially reviewed. These are necessary
conditions, not a resolution of the two-tile problem.

**Definitions:** use the unrestricted tilings and genuine polygon sides of
[the research problem](../../research-problem.md). The global side-count proof defines the
square-window patch and boundary estimates used by the other structural files.

**Review:** [global side-count review](../reviews/global-side-count-review.md).
The elementary monohedral and torus portions have no separate hostile-review
artifact; do not infer that status from the reviewed global theorem.

## Monohedral escape

### Lemma

Let \(P=\{A,B\}\).  If either \(A\) or \(B\) admits a plane tiling invariant
under a nonzero translation, then \(P\) is not aperiodic.

### Proof

A \(P\)-tiling need not use both prototiles.  Thus the periodic monohedral
tiling by that one member is a \(P\)-tiling and violates the universal
nonperiodicity condition. \(\square\)

### Corollary

Neither member of an aperiodic pair can be a triangle or a convex
quadrilateral.

For a triangle, join it to its half-turn about the midpoint of one side.  The
union is a parallelogram, whose translates by its two side vectors tile the
plane.  For a convex quadrilateral with consecutive angles
\(\alpha_1,\ldots,\alpha_4\), one of
\(\alpha_1+\alpha_2\) and \(\alpha_3+\alpha_4\) is at most \(\pi\).  Half-turn
a copy across the side joining that pair's vertices.  The two copies form a
convex centrally symmetric hexagon (with a collinear boundary vertex in the
equality case).  Its three pairs of opposite sides are parallel and equal,
so the standard translations pairing opposite sides tile the plane.  Hence
either shape has a periodic monohedral tiling, and the lemma applies.
\(\square\)

This does **not** justify rejecting an arbitrary pentagon merely because it
belongs to no currently known tiling family.  Current literature still
records completeness of the fifteen convex-pentagon families as not
definitively established.

## Lattice-periodic side-count obstruction

### Lemma

Suppose a tiling by copies of an \(m\)-gon \(A\) and an \(n\)-gon \(B\) is
invariant under a rank-two translation lattice and has \(a\) copies of
\(A\) and \(b\) copies of \(B\) in a fundamental domain.  Then

\[
        a(m-6)+b(n-6)\leq 0.
\]

This remains true with partial-edge contacts and T-junctions.

### Proof

Quotient by the period lattice.  Insert a graph vertex at every endpoint of
a partial-edge contact, obtaining a finite cell decomposition of the torus.
Suppress a collinear degree-two vertex only when it is not an original
polygon corner.  Write \(F=a+b\), and write \(E,V\) for the numbers of cell
edges and vertices.

Every remaining vertex has degree at least three.  A genuine contact
subdivision has at least three incident rays.  At an original corner the
interior angle is strictly less than \(\pi\), so two incident rays alone
cannot fill a neighbourhood without overlap or gap.  Thus
\(2E=\sum_v\deg(v)\geq3V\).  Euler's formula on the torus gives
\(V-E+F=0\), and consequently \(E\leq3F\).

Every native polygon side contains at least one cell edge, while each cell
edge has two incident faces.  Therefore
\(am+bn\leq2E\leq6(a+b)\), which is the asserted inequality. \(\square\)

### Edge-to-edge identities

In the edge-to-edge case,

\[
  2E=am+bn,\qquad
  2V=a(m-2)+b(n-2).
\]

The first identity double-counts face-edge incidences and the second follows
from torus Euler.  Equality in the side-count inequality holds exactly when
every vertex is 3-valent.

### Exact finite angle-balance obstruction

Label the angles of \(A\) by \(\alpha_1,\ldots,\alpha_m\) and those of \(B\)
by \(\beta_1,\ldots,\beta_n\).  A lattice-periodic edge-to-edge tiling
implies a finite list of vertex multisets \(t\) and nonnegative integers
\(x_t\) such that every \(t\) sums to \(2\pi\) and

\[
 \sum_t x_t\,\operatorname{mult}_t(\alpha_i)=a,\qquad
 \sum_t x_t\,\operatorname{mult}_t(\beta_j)=b
\]

for every labelled corner.  This follows by recording vertex orbits on the
quotient torus and double-counting corners.  Failure of this integer system
for every \(a,b>0\) obstructs only lattice-periodic edge-to-edge tilings; it
is not an unrestricted aperiodicity proof.

## Scope

The main problem calls a tiling periodic when it has even one nonzero
translation.  The torus lemma concerns two independent periods and must not
be silently applied to a rank-one periodic tiling.  A cylinder exhaustion
can exclude rank-one periodic tilings when **every** present tile has at
least seven native sides, but a full proof requires explicit control of the
boundary and Euler-error terms.  That extension was not promoted to a stable
lemma in this run.

## Global side-count obstruction

### Theorem

No finite set of compact convex polygons, all having at least seven native
sides and nonempty interiors, tiles the plane.  Contacts need not be
edge-to-edge.

### Proof

Fix such a finite set and suppose it tiles.  Let \(D\) be the maximum tile
diameter, \(a>0\) the minimum tile area, \(A\) the maximum tile area, and
\(s\) the maximum native side count.  The tiling is locally finite: every
tile meeting a bounded set \(K\) lies in its \(D\)-neighbourhood, and the
pairwise-disjoint tile interiors there each have area at least \(a\).

Let \(Q_R=[-R,R]^2\), and let \(\mathcal P_R\) contain every tile whose
interior meets \(\operatorname{int}Q_R\).  Put \(N=|\mathcal P_R|\) and let
\(U_R\) be their union.  The union is connected and covers \(Q_R\).  Planarize
the tile boundaries at native corners and endpoints of positive-length
contacts, suppressing collinear degree-two vertices which are not native
corners.  Write \(V,E\) for the graph counts, \(V_b\) for boundary vertices,
and \(H\) for the bounded complementary components of \(U_R\).  Its bounded
tile faces number \(N\), so planar Euler gives

\[
             V-E+N=1-H.                                      \tag{1}
\]

Every nonboundary vertex has degree at least three.  This is immediate at a
genuine contact subdivision.  At a retained convex polygon corner, two rays
cannot fill a neighbourhood: the complementary sector has angle greater
than \(\pi\) and hence cannot be the interior angle of one convex tile.
Boundary vertices have degree at least two.  Therefore

\[
  2E\geq 3(V-V_b)+2V_b=3V-V_b.
\]

Combining this with (1) yields
\(E\leq3N+V_b-3+3H\).  If \(B\) is the number of boundary graph edges, the
polygonal boundary components give \(V_b\leq B+O(1)\) and \(H\leq B\).
Consequently

\[
             E\leq3N+4B+O(1).                               \tag{2}
\]

Let \(S\) be the sum of native side counts of the selected tiles.  Every
native side contains at least one planarized graph edge, and a graph edge is
incident to at most two tile faces.  Thus

\[
             7N\leq S\leq2E.                                \tag{3}
\]

It remains to control \(B\), including arbitrary T-junctions.  A selected
tile contributing a positive-length boundary edge of \(U_R\) must meet
\(\partial Q_R\).  Otherwise the tile across an open portion of that edge
would also have interior meeting \(\operatorname{int}Q_R\) and would have
been selected.  Such boundary tiles lie in the \(D\)-neighbourhood of
\(\partial Q_R\), whose area is \(O(R)\); disjoint interiors of area at least
\(a\) show that there are only \(O(R)\) of them.

There is also a uniform bound on planarized edges contributed by one tile.
Every tile touching it lies in a region of bounded area depending only on
\(D\), so at most a constant number can touch it by the area lower bound
\(a\).  Two polygons with at most \(s\) sides have a uniformly bounded number
of boundary-contact endpoints.  Hence each boundary tile contributes at
most a fixed number of subdivisions, and \(B=O(R)\).

Equations (2)--(3) now give \(N=O(R)\).  On the other hand the selected tiles
cover \(Q_R\), so \(N\geq\operatorname{area}(Q_R)/A=4R^2/A\), a
contradiction for large \(R\). \(\square\)

### Corollary for the target

Any aperiodic pair in the target problem must have at least one member with
at most six sides.  Combining this with the monohedral escape corollary,
at least one member must be a pentagon or a hexagon.  This is only a
necessary condition: the other member can have arbitrarily many sides, and
the theorem supplies neither existence nor aperiodicity.

### Quantitative boundary form

The proof actually gives, for the square-window patch,

\[
   \sum_{T\in\mathcal P_R}\bigl(n(T)-6\bigr)\leq O(R),
\]

where \(n(T)\) is the native side count.  Thus, for an \(m\)-gon and
\(n\)-gon pair with \(m<6<n\),

\[
 (n-6)N_n(R)\leq(6-m)N_m(R)+O(R).
\]

If one type is a hexagon and the other has more than six sides, the latter
can occur only \(O(R)\) times among tiles meeting \(Q_R\), hence has zero area
density.  This density statement does not rule out an infinite sparse set of
such tiles and is not an impossibility theorem for that pair.
