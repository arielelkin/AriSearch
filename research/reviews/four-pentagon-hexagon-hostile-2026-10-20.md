# Hostile audit: four congruent convex pentagons in a convex hexagon

Date: 2026-10-20. Verdict: **the stated omission theorem survives this independent audit**, subject to the already source-audited sufficient periodic constructions for pentagon Types 1, 2, and 4. This is a theorem about a four-pentagon first-parent partition, not about arbitrary pairs of convex polygons.

Producer: [obstruction report](../searches/astra-four-pentagon-hexagon-obstruction-2026-10-20.md). Independent replay: [`verify_four_pentagon_hexagon.py`](verify_four_pentagon_hexagon.py).

## Topology, including nonstandard contacts

Make the internal seams a planar graph, split at all seam intersections, and suppress degree-two seam vertices. Count only positive-length seams as edges. Isolated point contacts are at junctions already present in the planar graph: at an interior point, the sectors between polygons force incident seam edges; at a boundary point, a tile touching only at that point gives two incident seams. They cannot create a separate zero-edge component.

The seam graph has no cycle. A seam cycle surrounds at least one child with no positive-length contact with the parent boundary. Each of that child's five native sides has a positive-length neighbor contact. One convex neighboring child cannot touch two distinct native sides: its intersection with the interior child would then contain noncollinear segments, and convexity would give an intersection of positive area. Hence that child needs at least five *other* children. Only three exist. This also excludes a child wholly internal to the parent with no cyclic seam visible after suppressing flat nodes.

Let `I` be the interior seam junction count, `B` the distinct seam endpoints in relative interiors of parent sides, `J` the parent corners with incident seams, `k` the forest component count, and `h` the total flat child-side incidences at planarized seam vertices. Boundary seam nodes may have more than one incident seam; the argument does not assume they are leaves. Forest Euler for the four regions gives `B+J=3+k`. The child-corner budget, counting a seam endpoint of degree `d` as `d+1` sectors, gives `12+h=2I+4+B`. All interior junctions have degree at least three and all boundary seam nodes degree at least one, so the forest degree sum gives `I<=B+J-2k=3-k`. Combining yields `h<=1-k-J`. Since `k>=1` and `h,J>=0`, equality forces `k=1`, `J=h=0`, `B=4`, `I=2`. Degree-sum equality then forces both interior junctions to be trivalent and all four boundary seam nodes to be leaves. Thus apparent multi-seam boundary points, parent-corner seams, flat partial side contacts, and disconnected seam components are all excluded by the budget rather than by an edge-to-edge assumption.

There is one abstract tree with two trivalent interior junctions and four boundary leaves. Its planar embedding has two leaves at each junction. Each end child has the two leaves and one junction, so its pentagonal corner count forces exactly two parent corners on that boundary arc. Each middle child has both junctions and two leaves, forcing one parent corner on its arc. Up to rotation/reflection of the hexagon, the four face words in the producer follow. I checked the five seam pairs directly against those words: `(L0,T4)`, `(L4,B1)`, `(R4,T1)`, `(R0,B4)`, `(T0,B0)`.

## Independent finite check

The checker derives the two interior and four boundary angle stars from the four face words rather than copying the producer's star list. It normalizes the first face to phase zero and positive orientation; the remaining three faces have `5^3 2^3=1000` phase/reflection assignments. Exact rational ranks and rational polyhedra produce the same census:

| Status | Templates |
| --- | ---: |
| Inconsistent angle equations | 668 |
| No strictly convex angle vector | 260 |
| Strict, but forced adjacent supplementary angles (Type 1) | 50 |
| Strict survivors | 22 |

For each of the 22 survivors, the checker independently builds the five seam-length equations, using outgoing-side index `offset-i-1` under reflection. Exact row-space implication then finds a sufficient Type 2 or Type 4 angle-and-length witness. All 22 pass. It does not read either producer JSON or import the producer's Rao table. Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_four_pentagon_hexagon.py
```

Observed output:

```text
PASS independent exact 1000-template census and 22 Type 2/4 implications
{'inconsistent': 668, 'no_strict_angles': 260, 'adjacent_supplementary': 50, 'survive': 22}
```

The pentagon Type 2 equations used are `A+B+D=360°`, `c=e`. Type 4 adds `E=90°`, `d=e`, `b=c`. Type 1 uses adjacent supplementary angles. These are positive sufficient periodic tiling families, so the result does not depend on the completeness of a fifteen-family classification. Rao's [primary paper](https://arxiv.org/abs/1708.00274) and the repository's [source-audited monohedral filter](../lemmas/pentagrid-pentagon-monohedral-filter.md) support this imported sufficiency.

## Scope and residual dependence

The finite checker establishes implications for necessary angle and length equations; it does not construct any realized four-piece hexagon, and none is needed to exclude the route. A hypothetical realized partition must satisfy one of those templates and therefore has a periodic pentagon-only tiling. The claim requires all four children to be congruent **genuine strictly convex pentagons** and the parent a **genuine strictly convex hexagon**. It does not cover a four-pentagon parent, a nonconvex child, a degenerate corner, or a first-parent inventory containing a second shape.
