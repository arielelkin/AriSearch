# Hexagon limits and conditional periodicity

**Status:** Proved internally, with claim-specific hostile-review records.
The higher-side exclusion, defect-free limit, and conditional deterministic-
state result were repaired during review; independent re-review of those
repaired claims is pending. The honeycomb and contact-density claims retain
their recorded reviews. None proves periodicity for arbitrary two-hexagon
tilings.

**Dependencies and shared definitions:**
[side-count and monohedral obstructions](side-count-and-monohedral-obstructions.md)
defines the selected square-window patch, N, E, V, boundary vertices V_b,
boundary edges B, holes H, and uniform O(R) boundary estimates. The monohedral
classification is the named Zhu–Wang–Yan preprint cited below; it is an
imported theorem, not proved in this repository.

**Reviews:** [higher-side exclusion](../reviews/hexagon-higher-side-review.md),
[defect-free limit](../reviews/hexagon-defect-limit-review.md),
[honeycomb combinatorics](../reviews/hexagon-combinatorics-review.md),
[same-type contacts](../reviews/hexagon-contact-density-review.md), and
[deterministic states](../reviews/deterministic-hexagon-review.md).

## Exclusion of a hexagon paired with a higher polygon

### Sparse-type limit lemma

Let a plane tiling use two fixed compact polygon types \(H,K\), and suppose
the number of \(K\)-tiles meeting every translated square of side \(2R\) is
at most \(CR\), with a constant independent of the square's centre.  Then
\(H\) admits a monohedral tiling of the plane.

### Proof

Let \(D\) bound both tile diameters.  Given \(L\), choose \(R\) much larger
than \(L^2\), and place a grid of points with spacing greater than
\(2(L+D)\) inside \(Q_{R-(L+D)}\).  There are
\(\Omega(R^2/(L+D)^2)\) grid points.  A single \(K\)-tile can meet the
radius-\(L\) disks about only a uniformly bounded number of these points,
while only \(O(R)\) \(K\)-tiles meet \(Q_R\).  For sufficiently large \(R\),
some grid disk of radius \(L\) therefore meets no \(K\)-tile.

Translate the centres of such disks to the origin and let \(L\to\infty\).
Tilings by finitely many fixed compact polygons are sequentially compact in
the local placement topology.  Indeed, positive minimum area and bounded
diameter uniformly bound the number of tiles meeting a compact set; the
orthogonal parts of their isometries lie in the compact group \(O(2)\), and
a diagonal subsequence converges on every bounded window.  Coverage and
interior-disjointness persist in the limit: a missing open ball or an
interior overlap would persist for all sufficiently close approximants.
Every fixed limit window eventually lies inside a disk containing only
\(H\)-tiles.  The limiting tiling is therefore monohedral by \(H\).
\(\square\)

### Theorem

No pair consisting of a convex hexagon and a convex \(n\)-gon with \(n>6\)
is aperiodic under the target definition.

### Proof

If the pair does not tile, it fails existence.  Otherwise the quantitative
global side-count inequality gives \(N_n(Q_R)=O(R)\), uniformly under
translation of the square.  The sparse-type limit lemma produces a
monohedral tiling by the hexagon.

We now use the unrestricted classification of monohedral convex-hexagon
tilers.  Zhu, Wang, and Yan, *Hexagonal Tiling of the Plane*,
arXiv:2508.01404v2 (2026), Main Theorem, prove that such a hexagon belongs to
one of the three Reinhardt families even when the original tiling is
non-edge-to-edge; their proof includes flipped copies.  Each family's
defining matching construction supplies a periodic edge-to-edge tiling.
Hence the pair admits a periodic tiling using the hexagon alone and is not
aperiodic. \(\square\)

### Candidate reduction

Together with the earlier results, the side-count possibilities for an
aperiodic pair reduce to:

* at least one polygon is a pentagon; or
* both polygons are hexagons.

This is a necessary condition, not a construction or a classification of
mixed tilings.

## Defect-free limit for two hexagons

### Theorem

If two fixed convex hexagons admit any plane tiling, they admit a (possibly
monohedral) plane tiling which is edge-to-edge and has exactly three tile
sectors at every vertex.

### Proof

Use the square-window patch and planarized graph from the global side-count
proof.  Let \(N,E\) have their previous meanings, let \(B\) be the number of
boundary graph edges, \(V_b\) the number of boundary vertices, \(q\) the sum
of their graph degrees, and \(H\) the number of holes.  Put

\[
 I=2E-B,
 \qquad \delta=I-6N,
 \qquad D_v=\sum_{v\ \mathrm{interior}}(\deg v-3).
\]

Here \(\delta\geq0\) counts the excess cell-edge pieces created by native-side
subdivision, and \(D_v\geq0\) counts excess interior valence.  Euler's formula
and degree counting give the exact identity

\[
 \delta+2D_v=6V_b-2q-B-6+6H.                 \tag{4}
\]

Indeed, \(2E=6N+\delta+B\), while
\(D_v=(2E-q)-3(V-V_b)\); substitute
\(V-E+N=1-H\).  The boundary estimates in the global theorem give
\(V_b,H,B=O(R)\), uniformly for translated squares.  Hence
\(\delta+D_v=O(R)\): only linearly many native sides are subdivided and only
linearly much excess valence occurs in a quadratic window.

For a prescribed \(L\), choose \(R\gg L^2\) and a separated grid of candidate
centres as in the sparse-type lemma.  Each defect affects only uniformly many
radius-\(L\) candidate disks, so one disk contains no subdivision endpoint
and no vertex of degree greater than three.  Translate such disks to the
origin and take a diagonal limit as \(L\to\infty\).  In every fixed window,
contacts are eventually whole native sides and all vertices are 3-valent.
The positive minimum native-side length prevents vertices from coalescing in
the limit.  Thus the limiting tiling is edge-to-edge and everywhere
3-valent.  It is admitted by the original pair, although one type may vanish
in the limit. \(\square\)

This is a structural reduction, not a periodicity theorem.

If the original pair were aperiodic, both types would occur in every such
limit.  Otherwise one convex hexagon would tile monohedrally; the unrestricted
hexagon classification cited above would then give that member a periodic
monohedral tiling, and monohedral escape would refute aperiodicity.  Thus a
hypothetical aperiodic $(6,6)$ pair necessarily admits an edge-to-edge,
everywhere-trivalent tiling in which both types occur, even though this
argument supplies no positive lower density for either type.

### Combinatorial hexagon rigidity

Every locally finite edge-to-edge, everywhere-3-valent tiling by
nondegenerate convex hexagons is combinatorially isomorphic to the standard
hexagonal honeycomb.

To prove this, take the cellular dual.  Convexity and the edge-to-edge
condition make the tiling a regular cell decomposition: closed-cell
intersections are empty or a common vertex/edge.  The dual is a triangulation
of the plane; every dual vertex is incident to six triangles.  Give every
dual triangle the metric of a unit equilateral triangle.  Develop one
triangle into the standard triangular tessellation and continue across edges
by reflection.  Continuation around a vertex is consistent because six
angles of \(\pi/3\) fill \(2\pi\), and simple connectedness of the plane makes
the development path-independent.  Its image contains the neighbour across
every edge of every image triangle, so it is the entire triangular
tessellation.  The resulting cellular local isomorphism is a covering of the
simply connected plane and hence one-sheeted.  Dualizing gives the standard
honeycomb. \(\square\)

This conclusion is combinatorial, not geometric: the hexagons need not be
regular, and their two-type labelling and placement geometry may still be
nonperiodic.

### Unavoidable same-type contacts

In every such two-hexagon tiling, at least one third of the full-edge
contacts have the same prototile type on both sides, in the Følner-density
sense (and up to a vanishing boundary error in finite patches).

Indeed, color each vertex of the triangular dual by its hexagon type.  Every
dual triangular face has a monochromatic edge, because a triangle is not
bipartite.  Double-counting face--edge incidences, each monochromatic edge is
charged by at most its two incident triangular faces.  Thus

\[
  2E_{\rm mono}\geq F_{\triangle}.
\]

For a large triangular-lattice patch,
$F_{\triangle}=2V+O(\partial)$ and
$E=3V+O(\partial)$.  Hence
$E_{\rm mono}/E\geq1/3-o(1)$.  In particular, a proposed two-hexagon
encoding that geometrically permits only unlike-type edge contacts cannot
even realize a defect-free tiling.  This is a necessary local-language
constraint, not a periodicity result.

### Conditional deterministic-state periodicity

Fix honeycomb cells \(C_z\), \(z\in\mathbb Z^2\), with the six globally
labelled neighbour directions.  Suppose an edge-to-edge trivalent geometric
tiling by the two hexagons has a finite set of full placement states.  A state
includes prototile type, the linear orthogonal part of its isometry, and a
side/vertex indexing resolving polygon symmetries.  Assume that, for every
reachable state and global direction, the state uniquely determines both the
neighbour state and its relative displacement.

Then the tiling is doubly periodic.  Indeed, neighbour transitions and their
opposites are inverse permutations on the reachable orbit.  Path consistency
on the globally coordinated honeycomb makes the two fundamental transitions
commute there, so \(\mathbb Z^2\) acts on a finite state orbit.  Its kernel
\(K\) has finite index and rank two.  For \(p\in K\), equality of full states
and displacement determinism make
\(t_p=x_{z+p}-x_z\) independent of \(z\); translation by \(t_p\) preserves
every tile.  The homomorphism \(p\mapsto t_p\) is injective, since zero
displacement would superpose distinct cell interiors, and its image is
discrete by local finiteness.  A discrete injective image of rank-two \(K\)
cannot lie in a line, so it supplies two independent translational periods.
\(\square\)

The finite-state and deterministic-displacement hypotheses are substantial.
Finite symbolic local rules alone can be strongly aperiodic in two
dimensions, and infinitely many tile orientations or branching matches are
not covered.
