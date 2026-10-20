# AA-side density obstruction for a regular pentagon and 144–126 octagon

Status: proved analytic lemma, independently hostile-reviewed [VALID](../reviews/regular-pentagon-octagon-aa-capacity-hostile-sol-2026-10-19.md). This is a restricted exclusion, not a solution to the unrestricted two-convex-polygon problem.

Let P be a regular pentagon with side length one. Let Q be a strictly convex octagon with four A=144° corners and four B=126° corners. Suppose the two shapes tile the plane using arbitrary isometries and unrestricted contacts. The elementary angle argument in [the exact first gate](../searches/regular-pentagon-octagon-144-126-first-gate-2026-10-19.md) shows that every tiling vertex is edge-to-edge and has type PPQ at A or PQQ at B. In particular, every Q edge with two A endpoints faces P. Call it an AA side.

**Lemma.** In such a tiling, each P faces at most one AA side of Q. Consequently, no Q whose cyclic corner word has three or more AA sides can occur in a plane tiling. The isolated metric with cyclic word `AAAABBBB` and QQ edges (4,6) is therefore untileable.

**Local proof.** At a PPQ corner, each of the two P tiles has one incident PP edge and one incident PQ edge. At a PQQ corner, both incident P edges are PQ. Two PP edges of the same P cannot be consecutive: their common vertex would have three P corners, of total angle 324°, rather than an allowed PPQ or PQQ star. Thus the PP sides of P are a matching in its five-cycle of sides, of size at most two. An AA side faced by P has a PPQ corner at each endpoint, so the two sides of P immediately before and after it are distinct PP sides. In a five-cycle, a matching of size at most two can flank at most one side. Hence P faces at most one AA side. This statement does not assume that every P has two PP sides; a P with zero or one PP side faces none.

**Global proof.** Fix a square of side R and count tiles whose chosen interior reference point lies in it. Let p_R and q_R be the P and Q counts. Because both shapes have fixed positive area and bounded diameter, the number of tiles meeting a fixed-width neighborhood of the square boundary is O(R). The O(R) constant depends on the two shapes, not on the tiling; use disjoint tile interiors and the smaller prototile area to bound tiles in a boundary strip enlarged by one maximum tile diameter.

Count all Q A-corners and B-corners, except those in that boundary strip. A-corners occur one per PPQ vertex and B-corners two per PQQ vertex. Comparing P-corners at the same interior vertices gives

    5 p_R = 2(4 q_R) + (4 q_R)/2 + O(R) = 10 q_R + O(R),

so `p_R = 2 q_R + O(R)`. If Q has `a` AA sides, all `a q_R` such sides face P, apart from O(R) boundary discrepancies. The local lemma makes their P neighbors distinct, so

    a q_R <= p_R + O(R).

For `a>=3` the two relations imply `q_R=O(R)`, and then `p_R=O(R)`. But the area of the square is R²; bounded tile areas and O(R) boundary errors imply `p_R+q_R=Omega(R²)`. Contradiction for large R.

For the exact first-gate words, `AABBAABB` and `AAABBABB` have two AA sides, while `AAAABBBB` has three. The theorem kills the latter regardless of its locally compatible seam joins. It does not establish existence or aperiodicity for either remaining word. For `a=2`, equality of the two asymptotic counts alone does not force every P to have exactly two PP sides; sparse defects would need a separate argument.

**Same counting beyond octagons.** The local AA capacity proof applies unchanged to a strictly convex Q whose angles are all A=144° or B=126° and whose angle sum permits a polygon. If Q has `a` A corners and `b` B corners, the angle sum forces `2a+3b=20`. In any plane tiling with P, the same star count gives

    p_R = (2a+b/2) q_R / 5 + O(R).

Each public AA edge of Q still faces one P and each P faces at most one, so the number `m` of AA edges must satisfy `m <= (2a+b/2)/5`. For the nonagon case `(a,b)=(7,2)`, the two B corners must be adjacent to share their required QQ edge; this leaves six AA edges, while the bound is three. For the decagon `(a,b)=(10,0)`, all ten edges are AA, while the bound is four. Hence neither of those two specified angle palettes tiles with P. The heptagon case `(a,b)=(1,6)` has no AA edges and survives this count. This corollary uses exactly the same boundary-area argument; its exhaustive angle-palette observation was separately checked in the [heptagon-palette Sol hostile review](../reviews/regular-pentagon-heptagon-144-126-hostile-sol-2026-10-19.md).

No numerical calculation, substitution assumption, periodicity assumption, or edge-to-edge assumption is used beyond the edge-to-edge conclusion derived from the given angles. All reflections are covered because the AA count and local five-cycle argument are reflection invariant.
