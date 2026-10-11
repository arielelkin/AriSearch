# Fresh hostile review: U/W periodic continuum

**Verdict: VALID without geometric repair.** The proof covers the entire real
domain b>0, 0<c<phi*b. It is not inferred from the irrational fixture.
The family has a whole-plane periodic tiling; it is not a classification of
all pentagrid metrics or a solution of the strong-aperiodicity target.

Reviewed [the construction](../lemmas/pentagrid-u-w-periodic-continuum.md).
The reviewer produced the earlier b=c=1 periodic pair but did not develop this
parameter deformation or its degree-one argument. The independent checker
imports no author code, reconstructs native shapes from their edge walks,
checks identities as polynomials in formal real parameters, then uses exact
convex clipping rather than the author's separating-axis method for the
irrational fixture.

## The whole parameter domain is genuine geometry

With A=phi^2*b+phi*c and H=phi^2*b-phi*c, every displayed native side is
strictly positive precisely under the stated sufficient domain. U has
directions(0,4,6,7,8) and lengths(A,A,b,c,b); W has
directions(0,2,4,6,8) and lengths(b,b,H,c,H), in units pi/5.
The independent native edge walks close identically over Q(z)[b,c].
For W one can see closure directly from

    z^4+z^8=phi^(-1)z^6, 1+z^2=-phi*z^6,
    H/phi+c=phi*b.

Both turn lists have positive turns belowpi totaling2pi. The supporting-line
argument in the lemma is valid: after any chosen edge, the subsequent edge
crosses have a positive block followed by a negative block as the directions
turn through one revolution. The first increment is strictly positive and
the last strictly negative. Closure makes their total zero. Each partial
sum before the sign switch is positive; after the switch it equals the
negative of the still-negative remaining sum and is therefore positive.
Thus every nonincident vertex is strictly left of each directed side.
This establishes global convexity and the absence of crossings, without
assuming that positive edge lengths alone imply simplicity for an arbitrary
polygon. W's final interior angles are all108 degrees; U's native angle word
is36,108,144,144,108 after sides. The two shapes cannot be congruent.

No distinct-length assumption is used. Values at which b,c,H happen to
coincide are included. The boundary H=0 is excluded, so a vanishing native
side cannot enter the proof.

## Complete formal seams, actual links and area

[The independent checker](verify_pentagrid_u_w_periodic_continuum.py)
constructs the four motifs using the stated isometries, including W's
essential cyclic shift by3 in F3. It checks all20 endpoint identities for
the ten seam rows as complete polynomial identities, not merely numerical
evaluations or equations of lengths. Every one of the20 native sides occurs
once in the side involution. Face adjacency reaches all four faces.

The induced corner permutation (i,a)->(j,d+1) is bijective. Independently
traversing it gives exactly six single circular links, agreeing with the
retained certificate. The angle at each vertex is the after-side angle of
the preceding edge, so the U local vertex list is(3,1,3,4,4), not the
after-side list. Four links have angles(4,3,3) and two have(1,3,3,3).
Every total is10 units pi/5. The cumulative integer lattice shift around
each actual cycle is(0,0), also independently checked. Thus no unresolved
translation is hidden by merely counting angle-class unions.

The finite abstract gluing has no boundary, each edge has two half-disks,
and every vertex has one circle as its link. With reversed endpoints and
all face orientations counterclockwise, it is an oriented connected compact
surface with Euler characteristic6-10+4=0. A higher-genus or disconnected
quotient cannot be hidden in this construction.

Direct polynomial computation gives

    area(U)/sin(pi/5)=phi^3*b^2+2phi^2*b*c+(phi^2/2)*c^2,
    area(W)/sin(pi/5)=phi^3*b^2-(phi^2/2)*c^2,
    cross(u,v)/sin(pi/5)=-4phi^2*b*(phi*b+c),

and 2area(U)+2area(W)=-cross(u,v). The determinant is strictly negative
on the entire positive domain, so the two proposed periods are independent.
The checker reconstructs and compares every b,c coefficient vector in the
author's retained motifs and lattice. These checks are stronger than
validating only the b=c=1 specialization or the sqrt(2) sample.

## Why degree one proves actual global coverage

The map from the abstract polygon quotient to the ordinary lattice torus is
well-defined by the exact seam endpoint equations. Inside faces it is a
Euclidean isometry. Across any edge, reversed directed endpoints and strict
convexity put the adjacent faces locally on opposite sides of the same line.
At a vertex, the actual single link successively attaches positive angular
sectors in their oriented order. The seam identities align each next bounding
ray. Since the total is exactly2pi, these sectors cover a sufficiently small
disk exactly once. There is no branched vertex or local multiple wrapping.
Thus the map is an area-preserving local homeomorphism everywhere.

The compact-covering argument is complete. Its image is nonempty, open and
closed in the connected target torus, hence all of it. Each fiber is closed
in the compact source and discrete by the local-homeomorphism property,
so it is finite. Disjoint local inverse neighborhoods of that finite fiber,
together with the compact complement, give an evenly covered target
neighborhood. This proves a finite covering whose degree d is a positive
integer constant. The exact metric area equality forces d=1.

This step rules out global overlap, repeated motifs or uncovered regions;
local compatibility alone would not do so. The degree-one map is a global
homeomorphism preserving the cell interiors. Lifting the explicit face maps
to the plane yields precisely the four listed polygons and all their lattice
translates. Their interiors are disjoint and their union is the whole plane.
Both nonzero independent lattice generators are translation periods. The
negative orientation of the chosen ordered period basis does not affect the
standard orientation of the target torus or its positive area.

## Independent irrational fixture and certificate integrity

Take b=1, c=sqrt(2). The exact inequality0<c<phi holds. The reviewer
reconstructs every motif and period in QQbar, checks all60 strict supporting
halfplane tests, all four exact positive motif areas and area equality.
Each author's retained real/imaginary coordinate is independently recovered
by finding the unique exact real root of its saved rational polynomial in
the saved rational isolating interval; every such coordinate agrees with
the independently reconstructed value. The parameter's minimal polynomial
is x^2-2 with positive root in(7/5,3/2).

The independent overlap domain uses the exact inverse lattice map

    x(w)=cross(w,v)/cross(u,v), y(w)=cross(u,w)/cross(u,v).

Vertex extrema bound each convex polygon in these coordinates. For ordered
motif pair i,j, any possible intersection with translate(n,m) requires

    ceil(xmin_i-xmax_j) <= n <= floor(xmax_i-xmin_j),
    ceil(ymin_i-ymax_j) <= m <= floor(ymax_i-ymin_j).

This derives a complete finite domain, including boundary contacts. Excluding
only a motif compared with itself at(0,0) leaves38 comparisons, agreeing
with the author list. Exact Sutherland-Hodgman clipping checks the actual
convex intersection in every case, and every intersection has area zero.
This supplies independent global geometric evidence for the fixture. It is
not the proof of the whole continuum, whose global guarantee is the
degree-one argument above.

The exact fixture area ratio equals1+2phi+2phi*sqrt(2). It is outside
Q(sqrt(5)): sqrt(2) is not in that field, and if the displayed ratio were
in it, subtraction and division by the nonzero field element2phi would put
sqrt(2) there. This is an actual periodic escape with a non-golden-field
parameter and an irrational area ratio. It cannot be dismissed by an
irrationality-implies-aperiodicity shortcut.

## Replay and scope

    conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_u_w_periodic_continuum.py

The complete replay passed. Its retained
[review certificate](../certificates/pentagrid-u-w-periodic-continuum-review.json)
contains the formal identities, actual links, zero cycle shifts and all38
complete clipping comparisons. Ordinary invocation prints JSON without
writing artifacts; saving requires explicit --output. During checker
implementation, an exponent-key hashing assertion and the assumed JSON
side-pair nesting were corrected; neither was an author geometry failure.

U's monohedral exclusion remains conditional on the separately imported and
reviewed Rao classification. W's is direct:108-degree native corners cannot
sum to360, nor to180 alongside one straight side sector. Those exclusions
are not required for the periodic construction. The construction works
under the original unrestricted contact/isometry convention and supplies
one periodic tiling, sufficient to exclude strong aperiodicity for this
family. It says nothing about every tiling being periodic, other W partners,
or the remaining angle-pair families. No novelty claim is made.
