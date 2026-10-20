# Hostile review: six-interior-core obstruction

2026-10-19. Verdict: **PASS / valid within the stated triangulated-disk scope**. No counterexample or unresolved defect found. This is a finite incidence obstruction, not a resolution of the unrestricted two-convex-polygon problem.

Reviewed artifacts: `research/searches/interior-q-branching-sol-2026-10-19.{md,py,json}`. Governing context read: AGENTS.md, research-problem.md, research-protocol.md, current discovery-log substitution entries, and the corner-branching and six-boundary substitution reports. No discovery-log or Git edits were made.

## Exact reviewed claim and hypotheses

A finite simple plane graph triangulates a closed topological disk: its outer boundary is a simple cycle of six distinct boundary-child vertices, all bounded faces are triangles, and its six other vertices are interior children. Every interior P child has full degree five and every interior Q child has full degree seven. For the Q parent there are nine P and three Q children in total. Under these hypotheses no interior child can be Q.

The graph formulation requires a genuine disk embedding, not merely Euler characteristic one, and the degree must count distinct neighbors. The stated single-arc boundary condition supplies the boundary cycle in the dissection interpretation. Child phases, reflection choices, lengths and numerical angles play no role in this claim.

## Independent degree-budget derivation

Let q count interior Q children, e count interior-interior edges, x count boundary-interior edges, and c count boundary-boundary edges other than the six boundary-cycle edges. Simplicity and the boundary cycle give c>=0 and partition every edge into exactly one of these sets. Triangulation and Euler give E=3(12)-6-3=27. Summing full degrees over the six interior vertices gives 2e+x=5(6-q)+7q=30+2q. Subtracting E=e+x+6+c yields e=9+2q+c. Thus q>=1 forces e>=11; omitting chords would weaken the contradiction, not rescue a candidate.

The J=1,D=H=0 primal budgets independently agree: the Q defect identity gives B+2J=7, hence B=5; there are B+J=6 active boundary transitions. The seam identity gives I=2(12)-2-B-J=16; these become the sixteen dual triangles. The native corner ledger is 66=3(16)+2(6)+(7-1). P analogously has E=29 and e=8+2q+c; this review makes no P-only impossibility claim.

## Independent core proof, allowing nontriangular bounded faces

Let H be the induced plane graph on the six interior children. Assume e>=11. If H is disconnected, the simple planar component caps 0,1,3m-6 for component sizes m=1,2,>=3 give at most nine edges; the largest split is 5+1. Thus H is connected. If v is a cut vertex, the components of H-v have positive sizes s summing to five. Each induced component together with v has at most one edge for s=1 and at most 3s-3 edges for s>=2. There are no edges between these pieces. The maximum over partitions of five with at least two parts is ten, attained by 4+1. Thus H is 2-connected.

Its outer face boundary is consequently a simple cycle of length l. Euler gives e-5 bounded faces. Each bounded face has length at least three, even if it is not a triangle. Therefore 2e>=l+3(e-5), so l<=15-e<=4. Simplicity gives l>=3 and e<=12. There are only the following possibilities for the outer cycle length:

* l=4: two vertices lie strictly inside the cycle.
* l=3: three vertices lie strictly inside the cycle.

Every such deep vertex has no edge to an original boundary child: such an edge would cross the Jordan outer cycle of H, and every original boundary child lies outside that cycle. Consequently its full degree equals its degree in H. The full degree is at least five and a simple graph on six vertices has degree at most five. It is therefore a degree-five P child adjacent to all five other vertices. A deep Q would already be impossible by degree seven.

For l=4, two universal deep vertices force eight edges to the four outer vertices plus their mutual edge, in addition to the four outer-cycle edges: at least thirteen edges, contradicting e<=12. For l=3, three universal deep vertices force nine edges to the outer vertices, their mutual triangle, and the outer triangle: fifteen edges, again contradicting e<=12. Thus e<=10, and 9+2q+c<=10 forces q=0.

This version deliberately does not require bounded faces of H to be triangles, and so independently checks the part of the original argument most vulnerable to embedding mistakes. In the actual induced-subgraph disk setting those faces are triangles: a bounded face contains no other H vertex by definition and no original boundary vertex by Jordan separation. Any triangulating diagonal across a nontriangular empty face would have endpoints in H and would already be in the induced graph. There is no hidden missing-vertex or nontriangular-face escape.

## Scope attacks and geometry

Disconnected cores and cut vertices are covered explicitly above. Repeated vertices on the core outer face cannot survive the e>=11 reduction to 2-connectivity. Boundary chords are included with the correct positive sign. A geometric convex hull is unnecessary: “outer cycle” means the topological outer-face boundary of the inherited plane embedding. Holes, crossing edges, parallel edges or a repeated outer-boundary vertex fall outside the standalone graph hypotheses and cannot silently be inserted into this proof.

For actual convex child polygons with pairwise disjoint interiors, graph simplicity has additional geometric support. The intersection of two children is convex with empty two-dimensional interior; a positive-length intersection is therefore one connected straight segment. Two separated contacts between the same pair are impossible, as are noncollinear positive-length contacts. With maximal seams, and H=0 excluding a third-child junction in the relative interior of that common segment (which would give a flat incidence), there is one seam at most per pair. Interior native sides then have distinct neighboring children, so the degrees five/seven are justified. Point-only contacts are not seam edges.

Convexity alone does not force one parent-boundary arc per child: a convex strip across a convex parent can touch two separated sides. However, at the current Q budget there are exactly six active transitions. If six distinct children each have positive-length parent-boundary contact, their maximal positive-length arcs number at least six; any repeated arc would raise this count above six, requiring more than six transitions. Thus this specific budget excludes repeated positive-length arcs when the phrase “six boundary children” has that meaning. This does not establish that every broader convex dissection has six such children or the assumed disk structure. Isolated point contacts require separate accounting if one changes that meaning.

## Computation, defects and remaining uncertainty

The adjacent producer checks arithmetic only; it does not enumerate graphs or certify planar topology. Its partition caps and hull edge counts agree with the independent proof above. No new enumeration was needed: the proof exhausts the potential e>=11 cores without selecting an embedding or invoking a graph catalogue. No repair to the claimed theorem is necessary. The added nontriangular-face argument is an independent verification, not a replacement hypothesis.

Remaining limits are application limits: the theorem does not exclude Q parents with a different number of positive boundary arcs/interior children, other inventories, other defect budgets, or geometric models that do not produce the stated simple triangulated disk. It also does not establish any P map, angle witness, polygon dissection, plane extension or aperiodicity statement.
