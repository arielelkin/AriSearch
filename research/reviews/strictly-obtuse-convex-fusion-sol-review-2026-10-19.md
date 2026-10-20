# Independent hostile review: strictly obtuse convex fusion

Date: 2026-10-19. Reviewer: independent Sol review agent.
Artifact reviewed: `research/lemmas/strictly-obtuse-convex-fusion-obstruction-2026-10-19.md`.

## Verdict

**Valid.** After the first review identified the covering ambiguity below, the author replaced “covers K” by “has union exactly K”. I reread the repaired theorem and proof. The explicit exact-union hypothesis resolves the only defect found; the written proof is correct. The counterexample below applies only to the original weaker wording.

## Exact literal counterexample

Let H be the regular hexagon with vertices, in cyclic order,

`(2,0), (1,sqrt(3)), (-1,sqrt(3)), (-2,0), (-1,-sqrt(3)), (1,-sqrt(3))`.

Set K=C1=H and C2=H+(10,0). Both pieces have every interior angle 2*pi/3. Their x-coordinate ranges are [-2,2] and [8,12], so their interiors are disjoint. They cover K and N=2. Thus mere covering does not suffice. The proof uses Ci subseteq K when asserting that each sector lies in K, and when concluding Ci=K from K subseteq Ci.

## Independent validation with exact-union hypothesis

Assume henceforth `K = union_i C_i`. Every Ci is then contained in K. Subdivide the polygonal boundary of K at its vertices and every piece vertex lying on that boundary. On any resulting open interval I, a piece either contains all of I or misses I: its intersection with a supporting line of K is empty, a point, or a closed segment whose endpoints, if nontrivial, are piece vertices. An isolated point of intersection is itself a piece vertex and has already been removed. Consequently the list of pieces containing points of I is constant. Coverage makes the list nonempty. A piece containing I has a half-disc of interior locally on the inward side at each point of I. Two such pieces would overlap in their interiors. Therefore the list consists of exactly one label.

If there is only one label on the cyclic boundary, closedness places the entire boundary of K in that piece. Convexity implies K is contained in the piece; exact union gives equality. Any other full-dimensional piece would have interior overlapping this piece, a contradiction.

Otherwise a change of label occurs between consecutive intervals at a point x. Both labeled pieces contain x by closedness. For each piece, x is on its boundary: an interior point of a subset of K cannot lie on the boundary of K. At x its local tangent sector has angle strictly greater than pi/2 if x is a genuine vertex, and pi if x lies inside a side. The two open sectors are disjoint, since a shared open direction would give positive-area overlap sufficiently close to x. Both sectors lie in the tangent sector of K, which has angle at most pi. Additivity of angular measure therefore gives their angle sum at most pi, contradicting the strict lower bound greater than pi.

This supplies the minor details implicit in the boundary-label argument without any assumption on the interior dissection graph.

## Hostile cases checked

- **Partial-edge contacts:** endpoints of a piece trace on an outer edge are piece vertices, so the stated finite subdivision catches every possible label transition. No matching of complete sides is required.
- **Outer vertices:** the containing sector has angle strictly less than pi at a genuine convex vertex, strengthening the contradiction. Artificial collinear vertices have angle pi and cause no difficulty.
- **T junctions:** a piece meeting x in the relative interior of a side contributes angle pi. It cannot share x with another full-dimensional piece inside K without exceeding the available sector. Interior T junctions are irrelevant to the boundary argument.
- **Pieces touching the boundary only at points:** these contribute no open boundary intervals and cannot remove the sectors at an actual label transition.
- **Enclosed pieces or cycles in the dissection graph:** if only one piece supplies outer intervals, convexity forces that piece to equal K, excluding enclosed positive-area pieces. Thus no unproved tree, shelling, or simple-connectivity hypothesis is used.
- **Nonconnected intersections:** the intersection of two convex pieces, or of a piece with a supporting line of K, is convex and therefore connected. A piece can have separated traces on different sides of K, but the proof never requires its whole boundary trace to be connected.
- **Strict versus weak obtuseness:** with angles allowed to equal pi/2 the contradiction fails sharply. `[0,1]x[0,1]` and `[1,2]x[0,1]` partition the convex rectangle `[0,2]x[0,1]`; all piece angles are pi/2. Genuine strictly obtuse corners are essential to this argument.

## Scope and nonconsequences

No connectedness condition on the selected cluster is necessary. A genuinely disconnected union cannot be convex; a cluster disconnected under a chosen adjacency graph is still covered by the theorem whenever its geometric union is convex. The applied whole-tile fusion conclusion is valid: a finite selected cluster from a plane tiling has disjoint interiors; if its union is convex, that union is a compact convex polygon with interior, and the exact-union theorem applies. The tiles need not be congruent and the ambient tiling need not be edge-to-edge. One cannot fuse even two such whole tiles into a convex tile. Hence whole-tile convex fusion cannot decrease three or more source congruence classes to two if it accounts for the source tiles as asserted.

This does not establish that an all-strictly-obtuse source plane tiling of any specified family exists, does not exclude cutting across tiles, and says nothing about sources with right or acute corners. It does not prove periodicity or aperiodicity, nor resolve the two-prototile question. Its use on a named source still requires checking every genuine source angle. No literature or novelty claim was reviewed or established here.

Finiteness is used to obtain a finite boundary subdivision and a transition between consecutive labeled intervals. No extension to arbitrary infinite dissections follows from this proof.

## Defects, repairs, dependencies, uncertainty

Original defect found: omitted explicit exact-union/containment hypothesis if “covers” is read literally. The author repaired the theorem to “has union exactly K”; I independently reread that version and accept the repair. I made no changes to the theorem artifact. The repaired geometry is fully checked above; no computation or external theorem is needed. No unresolved geometric uncertainty remains within that scope. This review is independent of the proof author and does not certify novelty.
