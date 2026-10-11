# Fresh review of the small pentagon dissection obstruction

Reviewed 2026-10-10 by an agent who did not develop the theorem or the
area-compatible metric family.

**Verdict: valid.** Every nontrivial finite partition of a genuine compact
convex pentagon into genuine compact convex pentagons contains at least
six pieces. Partial contacts and reflections do not invalidate the proof.
The substitution consequences are valid under the separately stated area
ratio area(V)/area(U)=phi. The family's exact area identity and convexity
are a separate computation, not established by this topological review.

Reviewed artifact:
[small substitution obstruction](../lemmas/pentagrid-golden-metric-small-substitution-obstruction.md).
This result does not prove that any two pentagons tile the plane, that a
substitution exists at a larger inflation, or that an admitted tiling is
aperiodic.

## Hostile cases checked

The main attacks were seams ending at original parent corners, several
seams meeting one boundary point, internal T-junctions, collinear side
subdivisions, disconnected internal seam components, a cycle touching
the parent boundary at vertices, a cycle enclosing several cells, a cell
touching the parent only at a point, and one neighbor matching several
subsegments of a cell side. Each is allowed by the proof; none creates
an exception to the theorem.

The distinction between native corners and inserted straight sectors is
essential. Merely counting native angles at every interior junction would
omit a pi sector at T-junctions. The artifact correctly retains H, the
number of inserted straight incidences, in the angle identity. The number
J of original parent corners supporting seams is also retained. Its sign
strengthens the forest contradiction rather than creating a missing case.

## The cellulation and Euler step

The boundary graph, including the parent's outer boundary, is connected.
To justify this without assuming edge-to-edge contact, choose interior
points of any two cells and join them by a generic polygonal path in the
parent's interior. It can avoid the finitely many subdivision vertices
and cross all contacted side segments transversely. The successive cells
share positive boundary segments, so the cell adjacency graph is connected.
Each individual convex cell has a connected simple boundary. Shared
segments therefore connect all cell boundaries. Their union includes the
parent's outer boundary and is the required connected graph.

After planarization and removal of inessential straight degree-two nodes,
its vertex count is I+B+5 and its edge count is E+B+5. Its bounded faces
are exactly the F cell interiors: convex cells have no holes and their
interiors contain no seams. Euler's formula gives F=E-I+1. This remains
valid when the internal seam graph itself has several components.

Every internal node has at least three seam rays. Two noncollinear rays
would give one of the two adjacent cells a reflex angle. Two collinear
rays have no native strict corner and are suppressed. The finite convex
partition precludes isolated internal endpoints: a ray ending in the
interior cannot separate the surrounding disk into the required convex
cell sectors. Each active outer node has at least one seam ray, including
each of the J active original parent corners. These observations justify
the degree lower bound even at T-junctions or higher-degree stars.

## Independent forest contradiction

For clarity, write f=F, n=I, b=B, j=J, h=H. At original parent corners,
the pieces' corner sectors sum to the parent corner angles, totaling3pi.
At additional boundary nodes their sectors sum to pi. At internal nodes,
all sectors, including any straight one, sum to2pi. Thus

    3f+h=2n+b+3.

If the internal seam graph were a forest with k>=1 components, its edge
count would be E=n+b+j-k. Euler would imply b+j=f+k-1. The degree bound
2E>=3n+b+j then gives n<=b+j-2k. Consequently

    h=2n+b+3-3f
       <= 2(b+j-2k)+b+3-3f
       = -k-j < 0.

Since h counts incidences, it is nonnegative. This contradiction proves
that a cycle exists without a numerical bound on junction counts or any
assumption about the angles of individual pieces. For f>1 the internal
seam graph is nonempty, so k>=1 is justified.

## The cycle-to-interior-cell implication

A finite planar graph containing a cycle contains a simple polygonal
cycle. Its edges are internal seams; they meet the parent boundary at
most in the finitely many graph vertices. The Jordan curve encloses a
nonempty open region within the convex parent.

Choose a point in that open region away from the finitely many cell
boundaries. It lies in the interior of one cell. That cell's interior is
connected and disjoint from the seam cycle, so it is entirely on the
bounded side. A cycle enclosing several cells causes no difficulty: one
of those cells is enough.

The cycle's closed bounded region can touch the parent's boundary only
at points of the cycle itself. Indeed if a parent-boundary point were
strictly inside the Jordan region, a small disk around it would extend
outside the parent, contrary to the region being contained in that
convex parent. Since the cycle's contact with the parent boundary is
finite, the selected cell has no positive-length outer-boundary contact.
It may touch an outer corner or side at an isolated point. This does not
remove an entire side from the argument.

Each genuine side of the selected cell has positive-length contact with
at least one other piece. To see this despite partial seams, choose a
generic point of its side in the parent interior, avoiding all finite
subdivision endpoints. A small disk across that side is covered by the
other pieces; at least one of their sides shares a positive interval of
the chosen supporting line. The finite subdivision assumption ensures
that such generic points exist.

## Five distinct neighbors

For two convex pieces with disjoint interiors, their intersection is
convex and has empty interior. It therefore cannot contain segments on
two distinct supporting lines: their convex hull would have positive
area. A genuine convex pentagon's five sides have five distinct
supporting lines. A neighbor may match several collinear subsegments of
one native side, but cannot serve another native side. Therefore the
chosen cell has at least five distinct neighboring cells. Including
itself, there are at least six pieces.

This argument does not require whole-edge contacts or neighbor polygons
of a common congruence class. No planar-graph density, infinite limit,
or local-to-global extension is used.

## Area-count consequence and its limits

Assume area(V)=phi*area(U), with phi=(1+sqrt5)/2. Its irrationality makes
the integer coefficients of 1 and phi unique. Inflation by linear factor
phi multiplies area by phi^2=1+phi. The required piece counts are then
(1U,1V) for a U parent and (1U,2V) for a V parent. Both violate the
six-piece theorem.

Linear inflation phi^2 multiplies area by phi^4=2+3phi. The U parent
requires five pieces, again impossible; the V parent's eight-piece count
does not rescue a substitution that also needs a U rule. Linear inflation
phi^3 instead gives phi^6=5+8phi and phi^7=8+13phi, hence totals13 and21.
The reviewed theorem gives no conclusion at those totals.

These are exact algebraic consequences, not geometric subdivision
witnesses. Compound supertiles, nonhomothetic expansions, or transported
fragments are outside this particular whole-parent consequence. The
review does not infer that any unrestricted tiling must be substitutive.

## Source boundary and remaining uncertainty

The focused primary-source comparison is preserved in
[the source audit](../literature/convex-pentagon-small-dissection-source-audit.md).
Frettlöh and Richter give a six-piece convex pentagon dissection in their
2019/2020 primary paper. That confirms that six-piece configurations are
already in the literature; it neither invalidates this lower bound nor
establishes its priority. No universal novelty claim is justified.

No mathematical defect or repair was needed in the general theorem.
This is an analytic proof, so no finite search or computation is trusted
to establish the unbounded dissection claim. The exact area-compatible
family remains subject to its separately assigned geometric audit.
