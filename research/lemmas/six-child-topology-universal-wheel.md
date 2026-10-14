# Every six-child convex pentagon partition is a pentagonal wheel

Date:2026-10-13. Status: independently hostile-reviewed VALID;
review: research/reviews/six-child-topology-hostile-review.md.
This is a finite partition topology theorem, not an infinite tiling theorem.

## Theorem

Let a genuine compact convex pentagon C be partitioned into exactly six genuine
compact convex polygons of positive area with disjoint interiors, each with at
least five native sides. Arbitrary partial contacts and isometries are allowed.
Then all six children are pentagons. Exactly one child is strictly interior.
Its five full native sides contact five different outer children. Each outer
child contains exactly one genuine parent corner, unsplit and equal to one
native child corner. Each of its two adjacent native sides lies completely on
a parent side. Each parent side is the union of the two complete native sides
of its endpoint children. All inner vertices are trivalent; exactly five seams
join the central pentagon vertices directly to distinct points in the relative
interiors of the five parent sides. No additional seams or T-junctions occur.
Thus the fixed six-child wheel topology is forced by the hypotheses.

## Dependencies and conventions

Use the proved finite-dissection theorem / cycle argument in
pentagon-higher-partner-positive-conjugate-bound.md to obtain at least one
child with NO positive-length outer-boundary contact. Call any such child
an interior child for now; it might initially touch C at isolated points.
An adjacency means positive-length shared boundary, not a point contact.
Two convex polygons with disjoint interiors intersect in a convex set with
empty planar interior. Thus one child cannot touch another along segments
on two different supporting lines.

Planarize seams at all genuine child corners and contacts. Suppress straight
degree-two nodes that are no child corner. Let I be internal nodes; B seam
nodes in relative interiors of parent sides; J parent corners incident with
seams; E internal seam edges; H straight child-angle incidences. All nodes
are finite because the six polygons have finitely many sides. All interior
nodes have seam degree>=3. Every active boundary node has seam degree>=1.
The five parent sides, split where needed, are not seam edges.

## Exactly one interior child

Every interior child has at least five distinct positive-length neighbors:
every native side must be covered by some child boundary, and different sides
require different neighbors by convex intersection. With six children it is
therefore adjacent to every other child and has exactly five sides.

The adjacency graph is planar: choose one point in each polygon interior and
join it to relative-interior points of each shared contact segment. The
straight pieces stay in their convex polygon interiors apart from contact
points, and do not cross within a polygon except at their common centre.
Adding the exterior face O retains planarity; it is adjacent to precisely
the children with positive-length outer contact.

If three or more children were interior, three of them versus the remaining
three child vertices give a K3,3 subgraph. If exactly two were interior, those
two and O versus any three of the remaining four children give K3,3. Both
contradict planarity. Hence there is exactly one interior child Z, and the
other five children each have positive-length outer contact. Z is a pentagon.
Each of its five sides is shared in full with one distinct outer child:
there are only five other children and none can share two central sides.
Moreover, no exterior seam can meet the relative interior of a central side:
its two incident outer children would both contact Z at that point, but at
least one already contacts a different central side, giving a positive-area
convex intersection. Thus the central cycle has exactly its five native
vertices; possible flat incidences at those vertices remain allowed for now.

## The five central vertices require distinct boundary endpoints

At a central vertex, the only other children that can touch it are the two
neighbors of its incident central sides. Any other child has positive contact
with a nonincident central side. Convexity of its intersection with Z would
then include the convex hull of that segment and the central vertex, a
positive-area triangle, impossible. Consequently an interior central vertex
has exactly three child sectors. The third seam between its two outer
neighbors leaves this vertex. A central vertex on the parent boundary is
already a seam node there, incident with its two central edges.

Remove the five central cycle edges from the seam graph. Call the remaining
edges exterior seams. No closed cycle consisting of exterior seams is
possible. A Jordan seam cycle has a bounded side contained in C; because its
edges are internal, it contains no positive-length part of the parent boundary.
If its bounded side does not contain Z it contains an extra interior child;
if it contains Z it also contains an outer child (the cycle is exterior to Z),
again giving an extra interior child. Both contradict uniqueness of Z.

Likewise no exterior-seam path joins two distinct central vertices, even if
it passes through boundary nodes. Take a simple such path, shortened so its
interior meets no central vertex. Together with either of the two central
boundary arcs it forms a Jordan curve. At least one of the two bounded
regions is outside the interior of Z and has nonempty interior. That region
is partitioned by whole outer child interiors. Its boundary contains only
central edges and exterior seams, which have no positive-length parent-boundary
contact. Its intersection with the parent boundary consists of finitely many
nodes. Thus it contains an outer child with no positive outer contact,
contradicting uniqueness. This also rules out two root branches sharing a
boundary endpoint, and a root branch reaching a central vertex already on the
parent boundary.

It follows that each interior central vertex belongs to an exterior-seam
forest component containing no other central vertex. It has degree one in
this forest. All other internal nodes have degree>=3; therefore that finite
tree must have a boundary node. Each central vertex already on the parent
boundary counts as a boundary node itself. These five boundary nodes are
distinct by the preceding path argument. Consequently

    B+J >=5.                                            (1)

This step deliberately does NOT assume Z lies strictly inside C; its isolated
outer contacts are removed only by the next exact count.

## Euler and native-angle defect budget

Put

    D=sum_internal(degree-3)+sum_active_boundary(seam_degree-1) >=0.

Euler for the disk gives6=E-I+1, hence E=I+5. The seam-degree sum gives

    2E=3I+B+J+D, hence I+B+J+D=10.                       (2)

For child side counts ni the angle sum in units pi is

    sum(ni-2)+H=2I+3+B.

All native child boundary corners are included. No straight child-angle
incidence can occur at an active boundary node: its straight pi sector would
consume the entire parent side aperture and leave no sector for a seam. A
parent corner has aperture<pi. Thus H accounts only for internal flat
incidences, including any partial contacts. Since sumni>=30, we obtain

    15+H <=2I+B.

Eliminate I using(2):

    B+2J+2D+H <=5.                                      (3)

Combining(1),(3) forces B=5,J=0,D=0,H=0,I=5,sumni=30.
All children therefore have five sides. A central vertex on the parent
boundary would have seam degree>=2 and contribute to D, impossible. Z is
strictly interior, so all five I nodes are its five genuine vertices. There
are no other internal nodes, and all five B nodes have seam degree one.
The exterior seam graph therefore consists of exactly five straight edges
from those central vertices to distinct outer-boundary points. No additional
exterior component or extra outer-child adjacency exists.

## One parent corner per outer child

Each outer child has a central side, its two incident radial seams, and a
connected parent-boundary arc between the radial endpoints. Let k be the
number of genuine parent corners on that arc. The arc contributes k+1 native
sides; the central side and two radial seams contribute three. H=0 guarantees
none of these corners is a suppressed straight child angle. Thus

    ni=k+4=5, so k=1.

Every outer child has exactly one original parent corner. The five boundary
endpoints lie one per parent side, since the five successive arcs each
contain one parent corner. No seam splits a parent corner (J=0). The two
outer child sides adjacent to each parent corner are complete native sides,
and each parent side is exactly their union. This is the required wheel.

## Scope and replay

The proof is analytic; no finite enumeration, solver or numeric geometry is
used. It does not assume source frequencies, matching rules, congruence among
children or edge-to-edge contacts. The >=5-side condition and exactly six
children are essential. Seven or more children, fewer-sided children and
nonconvex parents are outside the theorem. Its application to the existing
two-size wheel obstruction additionally requires that theorem's native-angle
and scale hypotheses. No unrestricted plane-tiling impossibility follows.
