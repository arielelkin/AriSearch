# Ten-edge bound for a six-child native interior core

**Theorem.** Let a simple plane graph triangulate a topological disk, with six distinct vertices on its outer boundary cycle and six interior vertices. Suppose every interior vertex has full graph degree at least five. Then the subgraph induced by the six interior vertices has at most ten edges.

**Substitution corollary.** In a Q-heptagon parent partitioned into `9P+3Q` native children with one split parent corner (`J=1,D=H=0`), assume a simple triangulated dual disk with six distinct single-arc boundary children and six interior children. If interior P children have degree five and interior Q children degree seven, then **every interior child is P**. No such Q-parent map can contain an interior Q child. This is a restricted incidence theorem, not an obstruction to other inventories, boundary structures, or the original two-polygon problem.

## Proof of the graph bound

Let `H` be the induced graph on the six interior vertices, with `e` edges. Suppose `e>=11`. A disconnected simple planar six-vertex graph has at most nine edges: its extremal component-size split is five plus one. If `H` has a cut vertex, partition the other five vertices into the components remaining after deletion. For a part of size `s`, the subgraph including the cut vertex has at most one edge when `s=1` and at most `3s-3` edges when `s>=2`. Summing over any partition into at least two positive parts gives at most ten edges. Therefore `H` is connected and 2-connected.

Its outer face is bounded by a simple cycle of length `l`. Euler gives `e-5` bounded faces. Since each has length at least three, `2e>=l+3(e-5)`, so `l<=15-e<=4`. A simple planar graph on six vertices has `e<=12`, and `l>=3`. Thus `l` is three or four.

Every vertex of `H` inside its outer cycle has no edge to any vertex on the disk boundary: such an edge would cross the cycle. Its full degree is therefore its degree in `H`, at least five; with only six vertices in `H`, it is adjacent to all five others. If `l=4`, the two deep universal vertices require their mutual edge, eight edges to the four outer vertices and the four outer-cycle edges: at least thirteen edges, a contradiction. If `l=3`, the three deep universal vertices require their mutual triangle, nine edges to the outer vertices and the outer triangle: at least fifteen edges, also impossible. Hence `e<=10`.

This proof uses no assertion that `H`'s bounded faces are triangles. It covers disconnected and cut-vertex cores before using the outer cycle. The disk triangulation and native degrees are needed for the corollary's budget.

## Corollary budget and scope

For the stated Q-parent disk there are `n=12` children, boundary length `b=6`, and `E=3n-b-3=27` dual edges. Let `q` be the number of interior Q children, `x` the number of edges from interior to boundary children, and `c>=0` the number of boundary-to-boundary chords beyond the six outer-cycle edges. Native degrees give `2e+x=30+2q`, while the edge partition gives `27=e+x+6+c`. Thus `e=9+2q+c`. The ten-edge theorem yields `2q+c<=1`, so `q=0`.

For a genuine convex child dissection with pairwise disjoint interiors, two children cannot share two disjoint positive-length seams: their intersection is convex and, with empty two-dimensional interior, is one straight segment or a point. This supports dual simplicity after maximal seam normalization when flat incidences are excluded. Convexity by itself does not force a child to touch the parent boundary on one arc; that single-arc and six-distinct-boundary-child scope remains explicit. Point-only contacts and different boundary budgets are outside the stated corollary.

The [analytic search record](../searches/interior-q-branching-sol-2026-10-19.md) contains the defect and native ledgers; its [arithmetic replay](../searches/interior-q-branching-sol-2026-10-19.py) checks the scalar counts. The [independent Sol hostile review](../reviews/interior-q-core-hostile-sol-2026-10-19.md) is **PASS**, including the nontriangular-core possibility, cut vertices, boundary chords and scope of convexity. No software result is used in the graph proof. The original aperiodicity objective remains unresolved.
