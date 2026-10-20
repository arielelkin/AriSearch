# Seven-child convex pentagon dissection theorem

Date: 2026-10-20. Status: [independently hostile-reviewed VALID](../reviews/seven-child-mixed-hostile-2026-10-20.md). This is a finite partition theorem, not a tiling theorem.

**Theorem.** Suppose a genuine convex pentagon is partitioned into exactly seven genuine convex polygons, each with at least five native sides. Partial contacts and isolated boundary touches are allowed. Then every child is a pentagon. Consequently a pentagon parent containing a hexagon or any higher-sided child needs at least eight children, using the reviewed [six-child wheel theorem](six-child-topology-universal-wheel.md) for smaller partitions.

**Proof.** A child is *interior* when it has no positive-length contact with the parent boundary. The reviewed [forest/cycle lemma](six-child-topology-substitution-consequences.md) gives at least one interior child. A convex child with at least five sides has at least five distinct positive-contact neighbors when interior: a single convex neighbor cannot contact two noncollinear native sides without overlapping its interior.

Let `r` be the number of interior children and `b=7-r` the number with positive outer contact. At least two children have positive outer contact, since one convex child containing the entire parent boundary would equal the parent. Form the simple planar contact graph and add an exterior vertex `O` joined once to each of the `b` boundary children. In a regular neighborhood of the exterior star, edges can be drawn between consecutive neighbors of `O` without crossing any edge incident to an interior child. Retaining a spanning path gives at least `b-1` distinct boundary-to-boundary edges in an augmented simple planar graph. These added edges are combinatorial; the corresponding children need not actually touch.

If `r>=3`, the graph induced by the interior children has at most `3r-6` edges. Their total degree is at least `5r`, so at least `5r-(3r-6)=2r+6` distinct edges are incident to an interior child. Together with `b` exterior spokes and `b-1` augmented boundary edges, the graph has at least `2r+6+2b-1=19` edges on eight vertices, exceeding the planar maximum `18`. If `r=2`, each interior child meets at least four of the five boundary children. Their neighbor sets share at least three, yielding a `K_{3,3}` subgraph with `O`. Thus `r=1` and `b=6`.

Use the reviewed exact [native-side defect identity](six-child-topology-substitution-consequences.md)

\[
\sum_{i=1}^{7}(6-n_i)=1+B+2J+2D+H_{\mathrm{flat}},
\]

where `B` and `J` count active seam nodes in parent side interiors and at parent corners, and `D,H_flat>=0`. Six distinct boundary-child labels occur on the cyclic parent boundary, so at least six label changes occur, each at a distinct active seam node. Hence `B+J>=6` and the right side is at least seven. Since all `n_i>=5`, the left side is at most seven, with equality only when every `n_i=5`. ∎

The original [proof development](../searches/astra-seven-child-mixed-obstruction-2026-10-20.md) and its [independent review](../reviews/seven-child-mixed-hostile-2026-10-20.md) give the planar augmentation and isolated-contact conventions in more detail.
