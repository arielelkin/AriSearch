# Seven-child mixed pentagon partition obstruction

Date: 2026-10-20. Status: proved and [independently hostile-reviewed](../reviews/seven-child-mixed-hostile-2026-10-20.md). No claim about arbitrary plane tilings follows.

## Claim

If a genuine convex pentagon is partitioned into seven genuine convex polygons, all with at least five sides, then all seven children are pentagons. Consequently an ordinary pentagon substitution parent containing any higher-sided child requires at least eight children, using the previously reviewed six-child theorem to exclude smaller counts.

Contacts may be partial; an interior child means one with no positive-length outer boundary contact, and may initially touch the parent at isolated points.

## Planar graph augmentation

Take the simple positive-contact child adjacency graph, and add an exterior vertex O adjacent to each boundary child once. This graph is planar: use centers and segments inside the convex children, and noncrossing arcs in the exterior. Write r for the number of interior children and b for boundary children, so r+b=7. A nontrivial convex partition has b>=2: if only one child had positive boundary contact, closure would make it contain the whole parent boundary, and convexity the parent itself.

The graph can be augmented by edges between boundary children until those b vertices induce a connected graph, retaining planarity and every edge incident to an interior child. To see this, take the cyclic order of the b spokes at O. For each consecutive pair of spokes, draw an extra edge between their child endpoints running close to one spoke, around O in the sector between the spokes, and close to the other spoke. Use disjoint narrow strips, and take the two distinct sides of each spoke. These paths have no crossings. Already existing edges between boundary children may be retained or removed in favor of these paths; they are irrelevant to the lower bound. Retain a spanning tree of the newly connected boundary-child graph, giving at least b-1 distinct boundary-boundary edges. For b=2 only one such edge is needed.

This is an augmentation, not the assertion that consecutive outer-boundary labels share positive contact. The latter can be false when an interior child touches the boundary at an isolated point.

## Number of interior children

Every interior child has at least five distinct neighbors. Its native sides are all covered by other children, and convex disjoint-interior polygons cannot share segments on two distinct support lines.

There is at least one interior child, by the reviewed seam-forest/cycle argument for a convex pentagon partition into children with at least five sides.

If r=2, b=5. Each interior child is adjacent to at least four boundary children, since it has only one possible interior neighbor. Their two boundary neighbor sets overlap in at least three children. Together with O those two interior vertices form the first part of a K3,3 subgraph, a contradiction.

If r>=3, let e_II be the number of edges between interior children. Simplicity and planarity give e_II<=3r-6. The number of child edges incident to at least one interior is at least 5r-e_II>=2r+6. The augmented graph additionally has at least b-1 boundary-boundary edges and b exterior spokes. Thus it has at least

    2r+6+(b-1)+b = 2(r+b)+5 = 19

edges. It is a simple planar graph on eight vertices, so it has at most 18 edges. Contradiction. Therefore r=1 and b=6.

## Native-side defect budget

Use the reviewed exact partition identity

    sum_i(6-n_i) = 6-p+B+2J+2D+Hflat,

where p=5, B counts active seam nodes in open parent edges, J counts active parent corners, D is the nonnegative excess seam-degree sum, and Hflat counts inserted straight child-angle incidences. Every one of the b boundary children occupies a nonempty open boundary arc. Label changes can occur only at active seam nodes. A cyclic sequence containing b distinct labels needs at least b transitions, even if labels repeat. Therefore B+J>=b=6. The identity yields

    sum_i(6-n_i)>=1+B+J>=7.

But seven children with n_i>=5 have sum_i(6-n_i)<=7, with equality only if every n_i=5. This proves the claim. If any child has six or more sides, the left side is at most six, an immediate contradiction.

## Dependencies and scope

The reviewed finite partition/forest result is in `research/lemmas/pentagon-higher-partner-positive-conjugate-bound.md`; the exact defect identity and six-child theorem are in `research/lemmas/six-child-topology-substitution-consequences.md` and `research/lemmas/six-child-topology-universal-wheel.md`. The older incomplete seven-child investigation is `research/searches/contact-structure-seven-child-interior-count-gate.md`.

The new ingredient needing hostile review is the planar augmentation, replacing an invalid literal boundary-adjacency argument. This proof does not provide an eight-child dissection, a substitution, plane existence, or intrinsic recognition.
