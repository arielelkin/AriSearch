# A convex pentagon needs at least six pentagons in a nontrivial dissection

**Status:** adversarially reviewed as valid in the [fresh audit](../reviews/convex-pentagon-small-dissection-review.md). This is a finite dissection obstruction, not an aperiodicity theorem or a restriction on infinite plane tilings.

## Theorem

Suppose a genuine compact convex pentagon C is partitioned into F genuine compact convex pentagons with nonempty, pairwise disjoint interiors. Pieces may have partial-edge contacts and arbitrary Euclidean isometries. If F>1, then F>=6.

## Planarization and angle identity

There are finitely many polygon sides. Planarize the common boundaries at native corners and contact endpoints. Suppress degree-two straight vertices which are not genuine corners of any piece or of C. The internal seam graph consists of segments not lying on the boundary of C. Include its endpoints on the outer boundary as graph nodes.

Let I be its number of internal nodes, B the number of nodes on the relative interiors of the five sides of C, and J the number of the five original outer corners incident to an internal seam. Let H be the total number of inserted straight angle incidences on piece sides. This counts each occurrence of a piece contributing angle pi at a planarized node; all H>=0. Interior graph nodes have degree at least three: with two noncollinear rays one incident piece would have a reflex corner; with two collinear rays no genuine corner is present and the node was suppressed. Each of the B+J active outer nodes has at least one internal seam edge.

Summing the piece angles including inserted straight incidences gives

    3F+H = 2I+3+B.                              (1)

Each interior node contributes2pi, the outer original corners together contribute3pi, and each of the B additional boundary nodes contributespi. This remains true if a seam ends at an original corner or several seams share a boundary node.

Let E be the number of internal seam edges. Including the outer boundary in the connected cellulation of the disk and applying Euler gives

    F=E-I+1.                                   (2)

No assumption of edge-to-edge contact is made.

## The seams cannot be a forest

Suppose the internal seam graph is a forest with k connected components. It is nonempty because F>1, so k>=1. It has I+B+J nodes, hence

    E=I+B+J-k,
    B+J=F+k-1,                                 (3)

using (2). Degree counting, including seam leaves at the outer boundary, gives

    2E >= 3I+B+J,
    I <= B+J-2k.                               (4)

Combining (1),(3),(4) yields

    3F+H-3 = 2I+B
              <= 2(B+J-2k)+B
              = 3(B+J)-4k-J
              = 3F-3-k-J.

Thus H<=-k-J<0, a contradiction. The seam graph therefore contains a cycle.

## A cycle requires an interior piece and five distinct neighbors

Extract a simple cycle from the finite planar seam graph. Its edges lie inside C apart from possible outer-boundary endpoint contacts. The bounded side of this cycle contains positive area and is a union of piece interiors and their boundaries. Choose a piece whose interior is on that bounded side. It cannot share a positive-length segment with the boundary of C: a cycle of internal seams only touches that boundary at finitely many vertices. Consequently all five native sides of this chosen piece have positive-length contact with other pieces. Point contacts at outer corners cause no problem.

Two convex pieces with disjoint interiors can share positive-length boundary contact only on one line. Indeed their intersection is convex and has empty interior; if it contained noncollinear segments their convex hull would have positive area, contradicting disjoint interiors. The five genuine sides of a convex pentagon lie on five distinct supporting lines. Therefore the chosen piece needs five distinct neighboring pieces, one for each side. With the chosen piece itself, F>=6. This proves the theorem.

The argument does not claim that F=6 is achievable by a particular pair, only that fewer pieces are impossible. It also does not use infinite tiling compactness, pentagon classification, density, or numerical evidence.

## Consequence for an area-compatible golden pair

The exact family in [the area-compatible candidate](../searches/pentagrid-golden-metric-area-compatible.md) has area(V)=phi*area(U), where phi=(1+sqrt(5))/2. The two areas are rationally independent. Any whole-polygon substitution with linear inflation phi would therefore require

    inflated U -> 1U+1V,
    inflated V -> 1U+2V.

These have two or three pentagon pieces, violating the theorem. With linear inflation phi^2, area conservation uniquely requires

    inflated U -> 2U+3V,
    inflated V -> 3U+5V.

The first parent has only five pentagon pieces, so this substitution is also impossible. Rotations, reflections, and partial seams inside a parent do not evade the argument.

Linear inflation phi^3 requires13 and21 pieces. This theorem gives no obstruction or existence statement at those counts. A substitution using compound supertiles, transported pieces, additional shapes, or a different expansion is outside this specific consequence. No conclusion about plane tilability or all admitted tilings follows.
