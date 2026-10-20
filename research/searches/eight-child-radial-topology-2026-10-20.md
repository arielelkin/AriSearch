# Eight-child pentagon-parent topology for a pentagon/hexagon radial substitution

Date: 2026-10-20. Status: analytic topology gate plus finite planar check, [independently hostile-reviewed](../reviews/eight-child-radial-topology-hostile-2026-10-20.md). Scope: a genuine convex pentagon partitioned into exactly eight genuine convex children, each a pentagon or hexagon, with at least one hexagon. Arbitrary partial contacts are allowed. This is not a substitution construction or a plane-tiling result.

## Deduplication and inputs

The reviewed six-child wheel and seven-child mixed obstruction are at `research/lemmas/six-child-topology-universal-wheel.md` and `research/reviews/seven-child-mixed-hostile-2026-10-20.md`. An earlier eight-child script, `astra-eight-child-disk-gate-2026-10-20.py`, treated a distinct 7P+Q7 graph preflight. The older `contact-structure-seven-child-interior-count-gate.md` has only a partial seven-child classification. This report closes the eight-child **P/H incidence preflight** for the radial second-parent inventories 7P+H and 6P+2H, without assuming edge-to-edge contact up front.

Use the exact native-side defect identity from `research/lemmas/six-child-topology-substitution-consequences.md`:

\[
\sum_{i=1}^8(6-n_i)=1+B+2J+2D+H_{\rm flat}.
\]

Here `B` counts active seam nodes in open parent sides, `J` active parent corners, `D` excess seam degree, and `H_flat` straight child-angle incidences. The left side is 7 for 7P+H and 6 for 6P+2H, leaving boundary-defect budgets of 6 and 5 after the constant 1. Every boundary child has an open parent-boundary arc; if there are `b` such children, the cyclic boundary label word gives `B+J>=b`.

## Interior count

The reviewed seam-cycle lemma supplies at least one child without positive parent-boundary contact. Write `r` for their number, `b=8-r`. There are at least two boundary children: if only one child had positive boundary contact, closure would make it contain the whole parent boundary, and convexity would make it the entire parent. Every interior child has at least its native side count in **distinct** positive-contact neighbors, by convexity of pairwise intersections.

Add an exterior vertex `O` with a spoke to every boundary child. Retain all edges incident to interior children. For `b>=3`, add the full simple cycle through the boundary children in their outer-boundary order, using a thin exterior regular neighborhood of the `O` star. The two cycle edges at a spoke run on opposite sides of it; all added paths stay outside the parent and avoid retained interior edges. Delete and redraw preexisting boundary-boundary edges if necessary. For `b=2`, add the one boundary-boundary edge. These are **augmented** edges; they do not yet assert actual positive contact.

For `r>=3`, the induced interior graph has at most `3r-6` edges. The total number of child edges incident to an interior is at least `5r-(3r-6)=2r+6`. If `b>=3`, the `b` exterior spokes and `b` cycle edges bring the augmented graph to at least

\[
2r+6+2b=22
\]

edges on nine vertices, beyond the planar maximum 21. If `b=2`, the corresponding lower bound is `2r+6+2+1=21`. Equality with the planar maximum would make the simple graph maximal planar, but `O` has degree two, whereas every vertex of a maximal planar graph with at least four vertices has degree at least three. Thus `r>=3` is impossible, including all cases with only two boundary children.

For `r=1`, `b=7` forces `B+J>=7`, so the identity's right side is at least 8 while either inventory has left side at most 7. Thus `r=1` is impossible. Necessarily `r=2,b=6`.

If either interior child were a hexagon, it would contact at least five of six boundary children even allowing the other interior child as a neighbor. The other interior child contacts at least four boundary children. Their boundary-neighbor sets overlap in at least three children. Those three, versus the two interior children and `O`, form a `K_{3,3}` subgraph. Thus **both interior children are pentagons**, and every hexagon is on the parent boundary.

If the two interior pentagons did not contact each other, each would need at least five of six boundary neighbors, again giving `K_{3,3}`. They therefore share an edge. Each needs at least four boundary neighbors. To avoid three common boundary neighbors, each has exactly four, their union is all six, and their intersection consists of exactly two.

## Consequence for the child inventory

The 6P+2H inventory is impossible: with six boundary children, `B+J>=6`, so the identity's right side is at least 7 while its left side is 6.

For 7P+H, equality is forced throughout:

\[
B=6,\quad J=D=H_{\rm flat}=0,\quad I=8.
\]

Each boundary child occupies exactly one connected open boundary arc, and the six arc transitions occur at six simple seam endpoints, all in open parent sides. No interior child touches the parent even at an isolated point, because that would require at least two seam edges at its boundary vertex and contribute to `D`. All interior seam vertices are trivalent; no native child side is split by a straight incidence. The two interior pentagons meet on one **whole native side**, and each of their other four whole sides meets a distinct boundary child. The six consecutive boundary-child pairs have actual positive side contacts, because each intervening simple boundary seam runs inward between that pair. Thus the augmented rim cycle is in this case the actual contact cycle.

The contact graph has 9 vertices (`O` plus 8 children) and exactly `1+8+6+6=21` edges: one inner-inner edge, eight inner-boundary edges, six boundary-cycle edges, and six `O` spokes. It is a maximal planar triangulation. The inner-inner edge has two incident triangles, so its endpoints abut the two boundary children touching **both** interior pentagons. Each interior pentagon also touches two exclusive consecutive boundary children. Since there are six boundary children in cyclic order, the two shared children are opposite.

Choose the cyclic boundary order `A0,A1,A2,A3,A4,A5`. A representative incidence map is

\[
U:(A0,A1,A2,A3,V),\qquad V:(A3,A4,A5,A0,U).
\]

The listed orders are cyclic native-side neighbor words. The shared boundary children are `A0,A3`. Their cyclic neighbor words, starting with the parent-boundary arc, are `A0:(arc,A1,U,V,A5)` and `A3:(arc,A4,V,U,A2)`. The exclusive words are `A1:(arc,A2,U,A0)`, `A2:(arc,A3,U,A1)`, `A4:(arc,A5,V,A3)`, `A5:(arc,A0,V,A4)`. Reflection and rotation give all six labeled planar maps found by the exact check script.

## Native-side and parent-corner slots

Let `k_i` be the number of genuine parent corners in the boundary arc of `A_i`. The arcs partition all five parent corners, so `sum k_i=5`. Since no parent corner is active and `H_flat=0`, an arc crossing `k_i` corners uses exactly `k_i+1` whole native sides of its child. A shared boundary child has four internal-contact sides, hence native side count `k_i+5`; an exclusive child has three, hence count `k_i+4`.

There are exactly two possible hexagon-placement orbits:

1. **Shared H:** put H at `A0`. Then `k_0=1`, `k_3=0`, and `k_1=k_2=k_4=k_5=1`. The opposite shared child is a pentagon with one parent-boundary side; the H has two parent-boundary sides.
2. **Exclusive H:** put H at `A1` (symmetry covers the other exclusive labels). Then `k_0=k_3=0`, `k_1=2`, and `k_2=k_4=k_5=1`. Both shared pentagons each have one parent-boundary side; H has three parent-boundary sides.

The second case should not be discarded by assuming that the hexagon must meet both interior pentagons. Topology alone permits its boundary arc to cross two parent corners.

This map is a precise input for a phase-consistent angle and metric packing gate. It does not establish that either corner-slot pattern can be realized by the radial P/H shapes or by arbitrary convex polygons.

## Replay

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/eight-child-radial-topology-2026-10-20.py`

The script builds the saturated nine-vertex graph, checks all 4-subset choices for the two inner boundary-neighbor sets, and confirms six labeled planar incidence maps, all with opposite shared boundary children. The analytic defect and convex-contact proof above supplies the exhaustive scope; the script is a finite cross-check, not a substitute for it.
