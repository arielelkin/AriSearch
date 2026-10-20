# A convex heptagon cannot contain five pentagons and three heptagons

Status: proved finite-partition theorem; [independent hostile review](../reviews/q7-five-pentagon-three-heptagon-hostile-sol-2026-10-19.md) **VALID**. No novelty claim is made.

## Theorem

No compact convex heptagon with seven genuine corners has a finite partition into five compact convex pentagons and three compact convex heptagons, all of positive area with pairwise disjoint interiors. The children need not be congruent. Arbitrary point and partial-edge contacts are allowed.

## Seam accounting

Planarize all internal contacts at genuine child corners and contact endpoints, suppressing only straight degree-two points that are no child's corner. Let `I` be the number of internal seam nodes, `B` the number of active seam nodes in parent-side interiors, `J` the number of parent corners carrying seams, and `E` the number of seam edges. Let `D` be the total excess of internal seam degrees above three and active-boundary seam degrees above one; let `H` count flat child-angle incidences at internal nodes. All these counts are nonnegative. A flat child angle cannot occur at an active boundary node. The reviewed [seam-count lemma](six-child-topology-substitution-consequences.md) gives, for `F` children of native side counts `n_i` in a `p`-gon parent,

    E = I + F - 1,
    I + B + J + D = 2F - 2,
    sum_i(6 - n_i) = 6 - p + B + 2J + 2D + H.

Here `p=7`, `F=8`, and `sum_i(6-n_i)=5-3=2`, hence

    B + 2J + 2D + H = 3.                                  (1)

## Two boundary nodes cannot enclose eight children

If a convex parent has exactly two active boundary seam nodes `x,y`, its two open boundary arcs each have a constant incident child label, say `A,B`. The labels differ at the seam endpoints. The convex hull of each closed boundary arc is the cap of the parent on its side of the chord `[x,y]`. Convexity makes `A` and `B` contain their respective caps, which cover the parent. If one cap is degenerate, the other is the whole parent. Thus there is no positive-area third child. With zero or one active node, a single child similarly contains the entire parent boundary and hence the parent. An eight-child partition therefore has `B+J>=3`.

Subtracting this inequality from (1) gives `J+2D+H<=0`. Therefore

    B=3, J=D=H=0, I=11, E=18.                            (2)

The three active nodes split the parent boundary into three arcs. At each node the adjacent arcs have different child labels, because a genuine seam separates two child sectors. Three cyclic arcs with unequal adjacent labels have three distinct labels. Thus exactly three children have positive-length parent-boundary contact, each in one arc. The other five have no positive-length outer contact.

## Planar adjacency contradiction

Make the graph whose vertices are the eight children and whose edges are positive-length contacts. It is planar: draw each edge through a point inside its contact and radial paths in the interiors of its two convex children. It is simple: the intersection of two different convex children with disjoint interiors is convex and hence contains at most one contact segment. Under `H=0`, a pair contact cannot have a seam node in its relative interior, since the two host children would have flat angle incidences there. Every seam edge therefore represents a different adjacency edge, and (2) makes the graph's edge count `18`.

The three boundary seam nodes each start a contact between two of the three outer children; the three unordered pairs are distinct. Thus the outer children have `e_BB=3` graph edges. Each of the five remaining children has at least five *different* neighbors: each native side is covered in positive length by a child, and one neighbor cannot meet portions of two distinct sides, since the convex hull of those portions would give positive-area overlap. Let `e_II` be graph edges among those five children and `e_IB` cross edges. Their degree sum gives

    25 <= 2e_II + e_IB = e_II + 18 - e_BB = e_II + 15,

so `e_II>=10`. But a simple planar graph on five vertices has at most `3*5-6=9` edges. Contradiction.

## Scope and consequence

The theorem excludes the Q-parent image `5P+3Q` of the proposed whole-polygon similarity substitution matrix `[[7,5],[2,3]]`, independently of the P-parent image, scale, angles, and side lengths. It does not exclude another inventory, an arbitrary plane tiling by a pentagon/heptagon pair, or the unrestricted two-convex-polygon target.

The originating [junction-design report](../searches/two-parent-junction-design-2026-10-19.md) includes the exact defect-budget replay. The independent review audits T junctions, isolated point contacts, repeated boundary labels, disconnected seam networks, and the seam-to-graph correspondence. The integer checker is supplementary; the argument above is analytic.
