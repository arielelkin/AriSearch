# Hostile review: seven-child mixed pentagon obstruction

Date: 2026-10-20. Verdict: **VALID**, conditional only on the previously reviewed finite partition and defect lemmas cited by the author. This review checks the new planar and boundary arguments independently; it does not assert a tiling result.

## Planar augmentation

The positive-length contact graph of convex children is simple and planar. Adding one exterior vertex O with one spoke to each child having positive outer contact is planar even if an interior child reaches the boundary at isolated points: choose the spoke contact in an open outer arc, and route its exterior portion outside the parent. For b boundary children, remove any existing boundary-to-boundary edges temporarily. In a small regular neighborhood of the star at O, connect consecutive spoke endpoints along the two sides of the spokes and around O. Choosing b−1 consecutive pairs gives a path on all b boundary vertices. The arcs can be made disjoint except at common endpoints, and do not meet retained interior-incident edges. If a proposed path edge was already present, replacing its old drawing preserves its single edge count. Thus a planar augmentation retaining every interior-incident edge and containing at least b−1 distinct boundary-to-boundary edges exists. The argument does **not** require two consecutive boundary labels to have actual positive contact.

Every interior child has at least five distinct neighbors. Each native side has positive contact with a neighboring child because the child has no positive outer contact. A second side cannot have the same neighbor: the intersection of two convex polygons is convex and cannot contain positive segments on different supporting lines while their interiors are disjoint. With r≥3 interior children, the induced interior graph has at most 3r−6 edges, so at least 5r−(3r−6)=2r+6 distinct child edges are incident to an interior vertex. The b exterior spokes and b−1 augmented boundary edges bring the total to at least 2r+6+2b−1=19, exceeding the planar maximum 3·8−6=18. This also covers r=5, b=2. For r=2, each interior has at least four of five boundary neighbors; their sets share at least three, giving K3,3 with O. Hence r=1, using the cited reviewed lemma for r≥1.

## Boundary labels and defect

Each of the six boundary children has at least one open parent-boundary interval. Remove the finitely many active seam nodes from the cyclic parent boundary. Each remaining interval has one constant child label. At any label change, the separating point is an active node: in a side interior it contributes to B; at a parent corner it contributes to J. The cyclic label word contains all six distinct labels, possibly with repeats, so it has at least six changes. Distinct changes occur at distinct active nodes; consequently B+J≥6. An interior child touching the parent at an isolated point can create an extra active node but cannot erase a label change. A parent corner without an active seam cannot change labels.

The reviewed identity gives sum(6−n_i)=1+B+2J+2D+H_flat≥1+B+J≥7. For seven children with n_i≥5, the same sum is at most seven, and equality forces every n_i=5. The theorem follows. In fact equality forces B=6 and J=D=H_flat=0, though no complete seven-pentagon topology is asserted.

## Limits and deduplication

This closes the seven-child *mixed* P-parent count for whole convex children, including partial contacts. Combined with the reviewed six-child wheel, a P-parent image containing a convex hexagon needs at least eight children. It does not exclude eight-child images, arbitrary plane tilings, nonconvex or compound parents, or multiple species outside the whole-polygon substitution setting.
