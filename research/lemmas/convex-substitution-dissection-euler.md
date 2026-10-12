# Euler identity for convex dissections and its substitution consequences

**Status:** proved internally (convex-substitution route, 2026-10-11); not yet
independently reviewed. Finite-dissection statements only; nothing here is a
plane-tiling or aperiodicity theorem.

## Setting

A convex p-gon C (genuine corners) is partitioned into F >= 1 compact convex
polygons ("children") with pairwise disjoint interiors. Partial-edge contacts
and arbitrary isometries are allowed. Planarize: graph vertices are the p
corners of C and every point that is a genuine corner of some child.
Classify the non-corner vertices:

* V_b: on the relative interior of a side of C (child angles sum to pi);
* V_T: interior points lying on the relative interior of a side of one child
  (the other child corners there sum to pi);
* V_f: interior points where only child corners meet (sum 2pi).

Let c(v) be the number of child corners at v. The minima are c>=1 at a corner
of C, c>=2 at V_b and V_T vertices (each child angle is < pi), c>=3 at V_f
vertices. Let X >= 0 be the total excess of c(v) over these minima, and n_T the
number of corners of child T.

## Identity

    sum_T (6 - n_T) = 6 - p + V_b + V_T + 2X,          (E)
    2F = 2 + V_b + V_f + V_T + X.                        (F)

Proof. Degrees: a vertex with c corners has c+1 incident edges at a corner of
C, a V_b or a V_T vertex (one straight sector), and c edges at a V_f vertex.
Hence 2E = sum n_T + p + V_b + V_T. Euler for the disk, V - E + F = 1 with
V = p + V_b + V_T + V_f, gives
p + V_b + 2V_f + V_T + 2F - sum n_T = 2. Corner counting gives
sum n_T = p + 2V_b + 3V_f + 2V_T + X. Eliminating sum n_T yields (F), and
6F - sum n_T gives (E). (Check: a 3x2 brick parallelogram dissection with two
offset rows has p=4, V_b=4, V_T=2, X=0 and four quadrilaterals: 8 = 8.)

## Consequences

1. **No hexagon is a union of >= 2 convex polygons with >= 6 sides each.**
   With p=6 and all n_T>=6, (E) gives 0 >= V_b+V_T+2X >= 0, so V_b=V_T=X=0:
   every side of C is a whole side of one child and every corner holds one
   child corner, so one child contains two consecutive sides at every corner,
   hence all of the boundary, and F=1. A pentagon (p=5) cannot be dissected
   into children with >= 6 sides at all, since (E) has positive right side.

2. **No homothetic substitution for (hexagon, hexagon) or (hexagon, n>=7)
   pairs.** If lambda*A (a hexagon) were partitioned into copies of A and B,
   both with >= 6 sides, item 1 forces a single child, i.e. lambda=1.
   The same holds for any finite iterate (lambda^k A) and for compound
   supertile hierarchies whose supertiles are the hexagons themselves.
   It does not exclude non-self-similar tilings by such pairs.

3. **A convex pentagon cannot be partitioned into 2, 3 or 4 convex polygons
   each with 5 or 6 sides.** With all n_T in {5,6}, sum(6-n_T) = N5 <= F, so
   (E),(F) give V_b + V_T + 3X <= V_f. Each connected component of the seam
   graph meets the boundary of C in at least two points (a component touching
   it at one point would make the child around it nonconvex), so V_b+X >= 2.
   * F=2: two pieces from one chord have at most 9 corners in total.
   * F=3: (F) gives V_b+V_f+V_T+X=4; the inequalities force V_b=V_f=2,
     V_T=X=0, i.e. a simple seam graph with degrees (1,1,3,3): impossible.
   * F=4: V_b+V_f+V_T+X=6. The solutions with N5=1+V_b+V_T+2X<=4 are
     (V_b,V_T,V_f,X) in {(3,0,3,0),(2,1,3,0),(1,0,4,1)}, each with N5=4=F,
     i.e. four pentagons, excluded by the reviewed
     [six-pentagon lemma](pentagrid-golden-metric-small-substitution-obstruction.md);
     and (2,0,4,0). In the last case the two boundary vertices have seam
     degree 1 and the four interior vertices seam degree exactly 3 (X=0).
     If the boundary points are joined to each other, the interior vertices
     span K4; otherwise each boundary edge ends at an interior vertex, at
     different ones (degree sequence (1,3,3,3) on four vertices is not
     graphic), so the interior vertices span K4 minus an edge. Either graph
     contains a triangle with no vertex or edge inside it (the remaining
     interior vertex is joined to the boundary of C, so it lies outside).
     That triangle is a face, i.e. a child with at most three corners, a
     contradiction.

   Hence in every homothetic two-tile substitution with a pentagon A and a
   pentagon or hexagon B, the parent lambda*A has at least 5 children.
   For the inflation lambda=phi with lambda^2 irrational and lambda^2 the
   Perron root of a nonnegative integer 2x2 matrix, the only matrices are
   [[1,1],[1,2]] and [[2,1],[1,1]] (trace 3, determinant 1): one parent would
   have 2 or 3 children, so lambda=phi is impossible for every such pair
   (any angles, any side lengths).

4. **Every convex pentagon with all angles in multiples of pi/4 tiles alone.**
   Angles are in {1,2,3} (units pi/4) and sum to 12. If no adjacent pair sums
   to 4, an angle 1 would need both neighbours equal to 2, leaving 7 for the
   other two angles (max 6); without 1 the word is in {2,3} and five such
   angles summing to 12 contain two adjacent 2s. So some adjacent pair is
   supplementary, the other three consecutive angles sum to 2pi, and the
   pentagon is Rao/Reinhardt type 1 (no length condition), which tiles
   periodically. With item 2, no pi/4-angle pair can be a homothetic
   two-tile substitution (the only remaining pair type is (hexagon,
   hexagon)). Exhaustive word check: `convex-substitution-cyclotomic.py`
   prints the empty pi/4 pentagon word list.

## Scope

Items 1-3 are finite dissection facts. Item 2 rules out self-similar
substitutions, not tilings. Item 4 uses only the classical type-1 pentagon
tiling.
