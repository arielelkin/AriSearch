# Five interior native children require six boundary children

Status: analytic finite-disk theorem; [independent Sol hostile review](../reviews/q7-five-boundary-incidence-hostile-sol-2026-10-19.md) **VALID**. The theorem is combinatorial and makes no claim about a plane tiling.

## Theorem

Let `G` be a simple triangulated disk graph with a boundary cycle of `b>=3` vertices and exactly five interior vertices. If every interior vertex has degree at least five, then `b>=6`.

In a convex-polygon dissection this applies when five strictly interior children each have at least five genuine native sides, all other children occupy one distinct boundary arc each, every internal seam node is trivalent, all active boundary nodes have one incident seam, and there are no flat child-angle incidences. Under these hypotheses, positive-length child contacts form the stated simple dual disk and the degree of an interior dual vertex is its native side count.

## Proof

Put `k=5`. A triangulated disk with `b+k` vertices has `E=3(b+k)-b-3=2b+12` edges. The boundary cycle supplies at least `b` boundary-boundary edges. Let `e_II` be the number of edges among the five interior vertices, and `e_IB` the cross edges. Summing interior degrees gives

    25 <= 2e_II + e_IB = e_II + E - e_BB <= e_II + b + 12,

so `e_II >= 13-b`.

Each interior vertex has at most four interior neighbors, so it has a boundary neighbor. In the embedded induced graph on the five interior vertices, any edge to a boundary vertex reaches the unbounded face without crossing the induced graph: the full disk boundary lies outside every interior-only cycle. Thus every interior vertex is incident to the unbounded face of the induced graph. This is an outerplane embedding, even if the induced graph is disconnected or has cut vertices. A simple outerplanar graph on five vertices has at most `2*5-3=7` edges. Hence `13-b<=7`, or `b>=6`.

## Application and scope

The [fixed Q7 incidence gate](../searches/q7-five-boundary-incidence-gate-2026-10-19.md) proposed ten children `7P+3Q` with five distinct boundary children and five interior children, all native and trivalent. It has `b=5` and is therefore impossible before angle or metric equations. The independent review checked the outer-face inference for disconnected and cut graphs, point contacts, T junction exclusions, and the degree/native-side correspondence. Its exact enumeration of all 1,024 labeled five-vertex graphs is supplementary to this proof.

The theorem leaves `b>=6`, altered defect allocations, nonnative/T incidences, different child inventories, and the unrestricted two-convex-polygon problem open.
