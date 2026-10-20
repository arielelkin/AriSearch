# Independent hostile review: five pentagons and three heptagons in a heptagon

Date: 2026-10-19. Verdict: **VALID**, with the genuine-native-polygon conventions stated below. Reviewer did not develop the proposed result. No novelty claim is reviewed.

## Exact claim and assumptions

A compact convex polygon with exactly seven genuine vertices cannot be partitioned into five compact convex polygons with exactly five genuine vertices and three with exactly seven genuine vertices, all of positive area and with pairwise disjoint interiors. All child angles are strictly between zero and pi; redundant collinear listed vertices do not count as native sides. Child congruence, similarity, side-length equality, edge-to-edge contact, and orientation restrictions are absent. Partial contacts and point contacts are permitted at the start.

Inputs independently read: research-problem.md; research-protocol.md (including sections 8, 11, 19); research/lemmas/six-child-topology-universal-wheel.md; research/lemmas/six-child-topology-substitution-consequences.md; research/searches/two-parent-p5-q7-cap-design-2026-10-19.md; and the strengthened research/searches/two-parent-junction-design-2026-10-19.md plus its Python checker.

## Independent reconstruction

Planarize the finite internal seam network at every native corner and contact, suppressing only degree-two collinear points that are not child corners. Use I, B, J, E, D, H as in the universal-wheel conventions. An interior degree-two genuine corner is impossible: two complementary convex sectors must both be pi, so the seam is straight and there is no genuine corner. Thus interior degree is at least three; active boundary degree is at least one. Euler and degree sums give

    E=I+F-1,
    I+B+J+D=2F-2.

Summing child native angles, including inserted flat incidences, gives

    sum(ni-2)+H=2I+p-2+B.

There are no flat child incidences at active boundary nodes, since a flat sector consumes the entire side-interior aperture; a parent corner has aperture less than pi. These relations give the exact defect identity

    sum(6-ni)=6-p+B+2J+2D+H.

Here p=7, F=8, and sum ni=46, so

    B+2J+2D+H=3.

There must be at least two active boundary points. With zero or one, the remaining connected boundary arc has constant child label, and closure and convexity put the entire parent in that child. Exactly two active points x,y also allow at most two children: each of the two boundary arcs has a constant label, and the convex hull of each closed arc is its corresponding cap cut off by the chord xy. The two caps cover the parent. Hence their two labels already cover it; a third positive-area child is impossible. If x,y lie on one parent side, one cap degenerates and the other is the whole parent, also excluding the eight-child case. The cap argument does not require a connected seam graph or restrictions on point contacts.

Consequently B+J>=3. Subtracting this from the budget forces

    B=3, J=D=H=0, I=11, E=18.

The three side-interior active nodes split the boundary into three open arcs. Each arc has one constant child label. A degree-one seam endpoint has distinct child labels on its two sides: a single convex child cannot occupy both sectors separated by an actual internal seam. Thus consecutive labels differ; on a three-cycle all three labels are distinct. There are exactly three children with positive outer contact, each with one arc, and five children with none.

For clarity, a full triangulated-dual theorem is unnecessary for the contradiction. Construct the ordinary positive-contact adjacency graph of the eight children. It is planar: choose a point inside each child and a point inside each contact segment, then draw the two radial pieces within the respective convex children. Distinct radial pieces in a convex child can meet only at its centre. Two different children intersect in at most one segment, by convexity and disjoint interiors. Thus the graph is simple.

Every primal seam edge supplies an adjacency. Conversely a contact segment cannot contain an extra seam node in its relative interior under H=0: both contacting children would have flat incidences there. Therefore distinct seam edges cannot represent the same adjacency, including collinear subdivision. There is exactly one graph edge per seam edge, hence exactly 18 graph edges.

Each of the three active boundary nodes has one emanating seam between the two labels of its neighboring arcs. Those three unordered label pairs are distinct. Therefore the number eBB of graph edges among the three outer children is at least three (in fact exactly three by simplicity).

Each of the five children without positive outer contact has at least five distinct neighbors. Every native side is covered in positive length by other children, because the partition is finite and that child has no positive outer contact. One neighbor cannot cover portions of two different native sides: the convex hull of those two portions has positive area and would lie in the intersection of two disjoint-interior children. Isolated boundary touches do not invalidate this neighbor argument.

Let eII count adjacency edges among these five children and eIB those between them and the three outer children. Then

    25 <= 2eII+eIB = eII+18-eBB <= eII+15.

So eII>=10. But the induced graph on five vertices is simple and planar and therefore has at most 3*5-6=9 edges. Contradiction.

## Hostile cases checked

* **T junctions:** a genuine T has a flat child incidence H>0. It is excluded by the derived budget, rather than by an initial edge-to-edge assumption.
* **Four or more sectors:** an interior node of degree greater than three contributes D>0. A boundary node with multiple entering seam rays likewise contributes D>0. Neither survives the budget.
* **Point-only outer contact:** at a parent corner this creates J>0; at a side-interior point a child with no boundary arc requires two entering seam rays and creates positive boundary excess in D. The author's stronger conclusion that the five children are strictly interior is therefore sound, although the proof above does not need it.
* **Repeated boundary labels:** three cyclic arcs with unequal neighboring labels must have three distinct labels. Point contacts cannot change the positive-arc label without an active seam node.
* **Repeated seam contacts:** convex intersections rule out disjoint contacts or contacts on different supporting lines. A third child touching the relative interior of a pair's contact introduces flat incidences on its hosts, excluded by H=0.
* **Loops or multiedges in the dual:** a genuine seam always has different children on its sides; convex intersection and H=0 exclude repeated edges. The ordinary graph proof avoids delicate exterior-dual conventions.
* **Disconnected seam network:** Euler remains valid after adjoining the parent boundary, which gives a connected cell decomposition. An isolated internal seam component would surround children, but does not change the identities or the graph contradiction.
* **Degenerate chord caps:** handled explicitly above. Positive child areas and genuine parent corners are essential hypotheses.

## Defects, repairs, and remaining uncertainty

No mathematical defect found in the strengthened Q inventory theorem. No repair was needed. The triangulated-disk statement is justified by the derived native trivalent incidences and distinct outer arcs, but it is stronger than necessary: the graph proof above makes explicit the only required correspondences and removes dependence on that presentation choice.

The supplementary restricted P-parent argument also passes: equality forces a maximal planar six-vertex interior graph, whose three vertices inside its outer triangle can connect only to interior vertices. Degree at least five then forces all nine edges of a K3,3 between those three vertices and the outer triangle, contradicting planarity.

No unresolved mathematical gap remains within these finite partition claims. This is not an impossibility theorem for convex pentagon/heptagon pairs, other substitution matrices, or unrestricted two-shape plane tilings. The main research problem remains unresolved.

## Computation scope and replay

Executed successfully:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-parent-junction-design-2026-10-19.py

The checker performs exact integer arithmetic, checks the restricted P/Q counts, and exhausts b=0..3, j=0..1, d=0..1, h=0..3 satisfying b+2j+2d+h=3 and b+j>=3. These ranges contain every nonnegative solution to that budget. It confirms the sole allocation (3,0,0,0) and 10>9. It does not computationally prove planar topology or the cap lemma; those are established analytically above. No solver, floating-point evidence, topology enumeration, timeout, or random seed is used. No discovery-log or Git operation was performed.
