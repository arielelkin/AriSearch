# Fresh analytic review of the Robinson height and Stokes necessity theorem

**Reviewer:** pentagrid_metric. This reviewer did not propose the invariant,
write its producer, or author its analytic formalization.

**Verdict: VALID** for the complete analytic necessity theorem in
[the source-height lemma](../lemmas/pentagrid-robinson-source-height-and-stokes.md).
The source must be an actual locally finite edge-to-edge plane tiling by
the specified unit rhombs, and the macro must be a union of whole prescribed
halves with whole source edges on its boundary. No mathematical repair is
required. This review does not rerun the separately independently checked
finite word/fan/geometry enumeration, certify any source assembly, or import
Penrose arrow legality from these necessary invariants.

## Global height: topology is an actual hypothesis

An oriented unit edge has one signed basis label E_k. Its direction fixes
that label uniquely, including the opposite orientation E_(k+5)=-E_k.
The four labels around each rhomb sum to zero. A finite path between two
vertices meets finitely many rhombs; their connected boundaries give an
edge/vertex adjacency path. Thus the source edge graph is connected.

A finite closed walk splits into simple cycles and reversed-edge
cancellations. A simple polygonal cycle encloses a bounded region, and the
edge-to-edge plane cellulation makes that region a union of complete rhomb
faces. No source face can cross an edge of the cycle. Bounded diameter and
positive minimum area, or the stated local finiteness, make the enclosed
face set finite. Summing oriented face boundaries cancels all internal
edges. This proves zero height around the cycle and hence all finite
closed walks. It does not merely prove zero projected displacement.

Therefore integration gives a global Z^5-valued vertex height, unique up
to a constant. The proof would fail for a graph with holes or without
the entire plane rhomb cellulation; neither situation is included. It
does not require a quasiperiodic source, nondegenerate phason choice,
injectivity of the linear projection, or recurrent orientations.

The projection kernel is exactly Z*(e0-e1+e2-e3+e4): the cyclotomic
minimal polynomial has degree4, is monic, and a degree<=4 integral
polynomial vanishing at z is its integral multiple. The proposed
Eisenstein argument for Phi5(x+1) is valid. A physically closed boundary
whose lift is a nonzero multiple of that kernel generator is consequently
excluded from an actual source cluster.

## Diagonal lifts and the two fixture word equations

The actual thin short diagonal is z-1=s*z^3 with lift E1-E0, equal to
D_s(3). The fat long diagonal is z^3-1=phi*z^4 with lift E3-E0, equal
to D_l(4). Rotation and conjugation give the stated signed-index formulas
in every allowed source orientation. These are endpoint differences
of the global height, not independently chosen lifts modulo the kernel.

For a positive word of length a+b*phi, coefficient comparison gives
n_u=a+n_s and n_l=b-n_s. For the stated a,b>=0 fixtures these exhaust
all positive words with0<=n_s<=b. The identity

    E_k+D_s(k)-D_l(k)=(-1)^k*R

holds at k=0 by direct signed indexing; a one-step signed basis rotation
sends R to -R and proves all k. Hence the whole side lift is the stated
base lift plus n_s*(-1)^k*R.

I independently summed the five base lifts. For U their coefficients in
(e0,...,e4) are(-1,1,-1,1,-1)=-R; for V they are(3,-3,3,-3,3)=3R.
The variable U directions have even k and the variable V directions odd
k. Exact closure therefore forces respectively one and three short
boundary edges. The resulting total boundary counts10 and13, six unit
edges in either fixture, and four/seven diagonals follow directly. A
physical boundary closure alone would not imply these equalities.

## Exterior-square signs, Stokes, and normalization

With an exactly closed height loop, changing all heights by C changes
sum H_r wedge H_(r+1) by a telescoping sum. Thus translation invariance
is valid even though C need not project to zero. Orienting every source
triangle counterclockwise makes common directed edges cancel in the
free exterior-square group. The macro's finite triangle union is a disk,
so no inner boundary component has been silently omitted.

At a triangle's unit-leg apex its other heights are two signed basis
vectors. Their wedge is exactly one signed basis wedge; there is no
factor1/2. Nondegeneracy rules out equal axes. For0<=i<j<=4 the physical
cross product of the canonical basis pair is sin((j-i)*pi/5)>0.
The counterclockwise triangle's physical cross product is positive.
Since its group wedge is plus or minus precisely that basis wedge,
its sign must be plus. This proves coefficientwise nonnegativity and
the interpretation of q_ij as actual triangle counts; it is stronger
than nonnegative total projected area.

Differences1,4 have cross product sin36; differences2,3 have sin72.
The physical functional applied to the boundary wedge gives twice area,
so the stated7/9 and9/16 thin/fat sums follow from the fixture area
identities and irrationality of phi. A whole rhomb contains two prescribed
halves of the same axis pair and gives twice that pair's wedge. Reflections
reverse plane orientation; reversing the reflected boundary to restore
counterclockwise orientation cancels that sign. Source rotations preserve
orientation and act by signed basis permutations whose induced action
permutes the positive wedges. Neither symmetry is discarded.

## Boundary pairing and exterior parent completion

Every prescribed half has exactly one diagonal, and its parent has only
one prescribed cut diagonal. A parent contributes0,1,or2 children to the
macro. Exactly one child means its entire diagonal lies on the macro
boundary: the other half is the unique adjacent source triangle there.
The whole-native-edge hypothesis prevents truncation or subdivisions by
foreign vertices. Conversely every boundary diagonal has just such a
parent. Its length symbol and signed direction identify the unordered
unit-axis pair uniquely. Therefore, for each pair,

    q_ij=2*r_ij+b_ij,

with r_ij a nonnegative integer. Both the lower bound and parity condition
are necessary; arbitrary integer boundary Stokes vectors alone need not
satisfy either.

For a counterclockwise horizontal diagonal the proposed apex offsets are
z^(k+2) for short and z^(k+1) for long. Each has unit distance from both
diagonal endpoints and positive signed distance from the diagonal line.
The second unit-distance point is its half-turn image about the midpoint,
on the exterior side. Thus the formula gives the unique entire source
parent rhomb, with counterclockwise boundary in the listed order. The
outside half is compulsory in an actual plane source even though it is
not a macro child.

Different boundary diagonals give distinct parents: one parent has one
cut diagonal and a simple convex macro boundary cannot traverse it twice.
Actual parents are source rhombs, so their interiors must be disjoint.
Any contact of positive length must be a full native unit side on both
parents by the source's edge-to-edge hypothesis. Containment checks on
inside children alone would miss violations between outside halves;
the full exterior-completion necessity is valid and materially stronger.

After removing the unique child on each boundary diagonal, every remaining
child has its mate inside. Otherwise another full diagonal would be on
the boundary and would already have been removed. Thus the residual is
exactly six whole rhombs for U or nine for V, with the stated axis-pair
counts. As a further check on normalization, these consist of three thin
and three fat rhombs for U, and three thin and six fat rhombs for V:
the removed halves are respectively1 thin+3 fat and3 thin+4 fat.
This is a necessary assembly inventory, not a proposed placement.

## Scope and conclusion

I attacked disconnected source graphs, closed loops around missing cells,
projection-kernel ambiguity, reflected triangle signs, rhomb/triangle area
factors, truncated diagonals, two boundary diagonals sharing a parent,
and overlaps hidden solely in outside halves. Each is excluded by an
explicit hypothesis or handled by the proof. No analytic gap remains.

The separately reviewed finite screen counts can be cited as finite
computational evidence; they are not re-established by this analytic
review. Passing zero height, nonnegative Stokes coefficients, parity,
or even exterior-parent packing does not construct the residual rhombs
or extend the cluster into a legal marked Penrose plane tiling. No
aperiodicity or two-shape result follows. The whole necessity theorem is
VALID exactly within its stated source and whole-triangle hypotheses.
