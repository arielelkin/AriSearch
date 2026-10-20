# Eight-child convex pentagon partition with a higher-sided child

Date: 2026-10-20. Status: [independently hostile-reviewed VALID](../reviews/eight-child-pentagon-one-hexagon-hostile-2026-10-20.md); this generalizes the [reviewed eight-child P/H topology gate](../reviews/eight-child-radial-topology-hostile-2026-10-20.md). This is a necessary finite-dissection theorem. It asserts neither a realizable dissection nor a substitution or plane tiling.

## Theorem

Let a genuine convex pentagon be partitioned into exactly eight genuine convex polygonal children of positive area. Suppose every child has at least five native sides and at least one child has at least six. Arbitrary partial side contacts, reflected or rotated children, and isolated parent-boundary contacts are allowed. Then:

1. Exactly seven children are pentagons and one is a hexagon. In particular, a heptagon or higher-sided child is impossible.
2. Exactly two children have no positive-length contact with the parent boundary. They are both pentagons, meet along a whole native side, and each meets four distinct boundary children along its other four whole native sides. The hexagon is one of the six boundary children.
3. Each boundary child has exactly one connected open parent-boundary arc. The six boundary children form an actual positive-side-contact cycle. The two boundary children adjacent to both interior pentagons are opposite on this cycle.
4. There are precisely two hexagon-placement orbits under cyclic relabeling and reflection: it is one of those two shared boundary children and its boundary arc crosses one parent corner, or it is one of the four other boundary children and its boundary arc crosses two parent corners.

Consequently, a genuine convex pentagon partition containing a genuine convex child with at least seven sides, all other children having at least five sides, needs at least nine children. The six-child wheel and [seven-child mixed obstruction](../reviews/seven-child-mixed-hostile-2026-10-20.md) rule out the smaller counts. The conclusion applies to whole-polygon substitution images only when they satisfy these stated hypotheses.

## Defect and boundary ledger

Write `n_i` for the eight native side counts. Let `B` be the number of active seam nodes in open parent sides, `J` the number of active parent corners, `D` the excess seam degree, and `H_flat` the number of straight child-angle incidences. All are nonnegative integers. The [reviewed native-side identity](six-child-topology-substitution-consequences.md) gives

    L := sum_i (6-n_i) = 1+B+2J+2D+H_flat.              (1)

Since all `n_i>=5` and one `n_i>=6`, `L<=7`. If `b` distinct children have positive parent-boundary contact, their labels occur on the cyclic parent boundary. Every label change is an active boundary node, so `B+J>=b`, including when a label occupies several arcs. At least two children have positive boundary contact: otherwise one convex child contains the whole parent boundary and hence the parent.

The [reviewed seam-cycle/forest lemma](six-child-topology-substitution-consequences.md) says that a nontrivial convex partition into children with at least five sides, one with at least as many sides as the parent, has an interior child. Denote the number of children without positive parent-boundary contact by `r>=1`; then `b=8-r`.

If `r=1`, the seven boundary labels give `B+J>=7`, and (1) gives `L>=8`, contrary to `L<=7`.

## Excluding three or more interior children

The positive-length contact graph is simple and planar. Each interior child has at least `n_i>=5` **distinct** positive-contact neighbors: its native sides are covered by child contacts, and a convex neighbor with disjoint interior cannot cover positive segments of two noncollinear sides. For `r>=3`, at most `3r-6` edges join two interior children. Hence at least

    5r-(3r-6) = 2r+6                                      (2)

child-contact edges touch an interior child.

Adjoin an exterior vertex `O` with a spoke to each of the `b` boundary children. Retain all edges incident to interior children; redraw or delete existing boundary-to-boundary edges. The exterior regular-neighborhood construction in the [independent topology review](../reviews/eight-child-radial-topology-hostile-2026-10-20.md) adds a simple cycle through the boundary children when `b>=3`, and one boundary-to-boundary edge when `b=2`. These are **augmented graph edges**, not presumed actual contacts. If `b>=3`, (2) gives at least `2r+6+2b=22` edges on nine vertices, exceeding the planar bound 21. If `b=2`, it gives at least `2r+6+2+1=21`. Equality would make the nine-vertex graph maximal planar, but `O` has degree two, impossible in a maximal planar graph. Thus `r=2` and `b=6`.

Now `B+J>=6`, so (1) gives `L>=7`. Equality with `L<=7` forces

    n_i multiset = {5,5,5,5,5,5,5,6},
    B=6, J=D=H_flat=0.                                  (3)

This is the universal step: no P/H inventory or radial metric was assumed.

## Interior adjacency and saturated topology

Suppose the interior hexagon existed. It would have at least five of the six boundary children as neighbors, even if it contacted the other interior child. The other interior child would have at least four boundary neighbors. Their neighbor sets would overlap in at least three boundary children. Those three together with the two interior children and `O` give a `K_{3,3}` subgraph. Hence both interior children are pentagons and the hexagon is on the boundary. The same argument shows the two interior pentagons must contact each other: otherwise each would have at least five boundary neighbors. Given their contact, each needs at least four boundary neighbors, and three common ones would again give `K_{3,3}`. Each therefore has exactly four, their union is all six boundary children, and exactly two boundary children touch both.

Equation (3) makes the six boundary label changes simple seam endpoints in open parent sides. There can be no extra changes, so every boundary child has exactly one open boundary arc. A child with no positive boundary contact cannot touch the parent even at an isolated point: an open-side touch would have at least two incident seam edges and contribute to `D`, and a corner touch would contribute to `J`. All internal seam vertices are trivalent. Since `H_flat=0`, none of the five native sides of either interior pentagon is split by a straight incidence. Its five different neighbors therefore cover its five complete sides, one side for the other interior pentagon and four for distinct boundary children. At each simple boundary transition, the seam entering the parent begins a positive contact between the two adjacent boundary children. Thus the boundary-label cycle is an actual contact cycle.

Add `O` to this now-actual contact graph. It has `1+8+6+6=21` edges on nine vertices and is a planar triangulation. The four boundary neighbors of an interior vertex are consecutive on the six-cycle; the two four-element sets overlap at their endpoints. Therefore the two shared boundary children are opposite. With boundary order `A0,...,A5`, a representative map has interior neighbors `U:(A0,A1,A2,A3,V)` and `V:(A3,A4,A5,A0,U)` in cyclic order.

Let `k_i` count parent corners traversed by `A_i`'s sole boundary arc. The six arcs partition the five parent corners, so `sum k_i=5`. Since `J=H_flat=0`, `A_i` contributes `k_i+1` complete native sides to the parent boundary. A shared boundary child uses four further sides internally, so its native count is `k_i+5`; an exclusive boundary child uses three, so its native count is `k_i+4`. Each shared pentagon therefore has `k_i=0`, each exclusive pentagon `k_i=1`. The unique hexagon has `k_i=1` if shared and `k_i=2` if exclusive. These give exactly the two stated orbits.

## Scope of the nine-child corollary

The [six-child universal wheel](six-child-topology-universal-wheel.md) requires all six children to be pentagons. The [seven-child mixed theorem](../reviews/seven-child-mixed-hostile-2026-10-20.md) likewise forbids a child with at least six sides when all children have at least five. The theorem above excludes any seven-sided or higher child at eight children. Five or fewer children are excluded by the cited six-child lower-bound and forest arguments for this setting. No conclusion is drawn when a child has fewer than five sides, the parent is not a pentagon, or children are nonconvex or compound.
