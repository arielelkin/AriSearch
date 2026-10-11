# Fresh hostile review of the V/W periodic continuum

**Reviewer:** pentagrid_metric. This reviewer did not find the dimer
matching, derive the V/W family, or write its producer.

**Verdict: VALID** for the whole real domain b>0,c>0, the exact four-face
seam and area proof, and the retained b=1,c=sqrt(2) fixture. No mathematical
repair is required. This is a periodic escape family, not a classification
of all V/W pairs or a solution of the original research problem.

Reviewed [lemma](../lemmas/pentagrid-v-w-periodic-continuum.md),
[independent checker](verify_pentagrid_v_w_periodic_continuum.py), and
[fresh review certificate](../certificates/pentagrid-v-w-periodic-continuum-review.json).
The checker imports no author code. It reuses generic exact clipping and
root-decoding routines from this reviewer's earlier U/W audit, with a new
independent native-side reconstruction and new formal identities.

## Exact native shapes and whole-domain convexity

Set E=phi(b+c),D=2phi*b+phi^2*c,H=2b+phi^2*c. These are positive for
every b,c>0. I reconstructed V first from the native side lengths
(b,D,b,E,E) in directions(0,3,6,7,9)*pi/5, rather than accepting the
author's octagon coordinates. The native angle word at its vertices is
(4,2,2,4,3)*pi/5, equivalent to the claimed angle-after-side word.
Closure is an exact identity in Q(z)[b,c].

Independently building Q from its eight side vectors gives the central
symmetry q_(j+4)=q4-q_j and q4=D*z^2. Rotating the native V by z^4 and
translating by q3 reproduces precisely[q3,q4,q0,q1,q2]. The other half
is its half-turn q4-V. Q's positive-side convexity makes the connecting
diagonal partition into these two pentagons exact, with disjoint interiors.
The D side really joins the two72 corners; the fixed dimer is not merely
an area-compatible shape.

W is independently built from(b,H,b,E,E) in directions(0,2,4,6,8)*pi/5,
with all108-degree native angles. Its closure and w3=phi*E*z^2 are formal
identities. Its angle multiset differs from V, so the two congruence classes
are distinct.

The checker proves all78 strict support inequalities for V,W,Q throughout
the whole positive domain: each normalized support polynomial is nonzero
and has only nonnegative real coefficients in b,c. Evaluating at b,c>0
therefore gives a strict positive value. This is a coefficientwise universal
positivity proof, not a sampled metric assertion. It confirms the analytic
direction-ordered convexity argument and excludes self-crossing or an
unnoticed limiting sign branch.

All four motifs are rotations/half-turns/translations of these native
polygons. In particular p->q4-p and p->b-p preserve plane orientation.
The construction uses no reflection restriction as a placement rule:
an orientation-preserving witness is admitted under unrestricted isometry.

## Actual seams, circular links, and lattice

Each of the ten reversed side pairings has both endpoint identities
checked as a polynomial identity in b,c. Every one of the20 motif sides
occurs exactly once. Face adjacency is connected. I independently traced
the side-involution/successor permutation, obtaining these actual links:

    (00,23,34),
    (01,12,31,22),
    (02,21,32,11),
    (03,14,20),
    (04,30,13),
    (10,33,24).

Here ij denotes face i, native vertex j. The first, fourth, fifth and
sixth have angles(4,3,3); the other two have(2,2,3,3). Each has total
2pi. The accumulated integer lattice shift around each link is exactly
(0,0), checked explicitly. Thus these are single circular links and
ordinary Euclidean vertex neighborhoods, not just multisets or union
classes. The quotient has6vertices,10edges,4faces and Euler characteristic0.

The independently reconstructed periods are

    u=2b+E*z-D*z^2, v=2phi*E*z^2.

Their normalized determinant is the exact polynomial

    cross(u,v)/sin36=2phi^3*(b+c)*(3b+c)>0.

Consequently they span an ordinary lattice for every allowed parameter.
Degenerate periods cannot occur anywhere in the claimed open domain.

## Area and the global covering argument

Exact native shoelace gives the three full identities

    area(V)/sin36=(3phi+2)b^2+(4phi+2)bc+(phi+1/2)c^2,
    area(W)/sin36=(3phi+1)b^2+(4phi+2)bc+(phi+1/2)c^2,
    area(Q)=2area(V).

The checker compares every polynomial coefficient, including the mixed
coefficient, with the retained author certificate. It verifies
2area(V)+2area(W)=cross(u,v) as a formal identity. These facts are not
extrapolated from the irrational fixture.

The abstract side quotient is a compact connected oriented surface.
Its motif-coordinate map into R^2/(Zu+Zv) is well-defined by the reversed
seam identities. Convex opposite support half-planes prove local isometry
across edges. At a vertex the actual single ordered link, seam-compatible
rays, positive corner sectors, and total2pi prove local isometry across
the whole disk. There is no assumption that the abstract surface already
embeds in the plane.

A compact local homeomorphism onto the connected torus is a finite cover:
its image is nonempty/open and compact/closed; local injectivity gives
discrete fibers, compactness makes them finite, and finitely many local
inverse neighborhoods give an evenly covered neighborhood. Its degree
is a positive integer. Local Euclidean area preservation and the exact
source-area/target-area identity force degree1. Thus no quotient face
overlap or multiple preimage can survive. Lifting its four faces by the
ordinary lattice yields exactly the stated full-plane periodic motif set.

This global argument is valid for arbitrary real positive b,c. The
convex dimer alone, an angular torus alone, or area equality without the
preceding local-isometry checks would not prove plane coverage.

## Independent exact irrational fixture

For b=1,c=sqrt(2), I reconstructed all motif and period coordinates from
the formal native shapes, without using the saved coordinate values.
The checker then decoded every saved rational or root-isolated real
algebraic coordinate and compared it to this reconstruction. All motif
coordinates, periods, areas, and determinant agree exactly. The positive
sqrt(2) defining polynomial and isolating interval agree as well.

For every ordered motif pair, independently derived lattice-coordinate
bounding boxes give the complete integer translation range capable of
intersecting it. There are32 nontrivial comparisons, matching the complete
retained list. For each, exact convex polygon clipping computes the actual
intersection; every intersection has area0. This uses clipping rather than
the author's separating-axis predicate. The60 direct strict supporting
half-plane checks and exact total-area/covolume identity also pass.

The retained fixture therefore has disjoint interiors at every lattice
translation. Its complete comparison range is geometrically derived;
it is not a guessed translation bound. The fixture independently supports
the family theorem, while the universal proof remains the formal torus
and positivity argument above.

Replay without mutation:

    conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_v_w_periodic_continuum.py

Use `--output` only to explicitly retain another review certificate.

## Scope and verdict

The discovery search stopped on one witness; it did not exhaust its full
pairing domain. This review certifies the displayed positive family and
does not turn that search into a V/W classification. Reflections and
partial contacts remain allowed by the research problem; an admitted
periodic full-edge witness is already sufficient to defeat aperiodicity
for this family. Omission causes no additional proof obligation for a
counterexample using both types. No monohedral theorem or external
source legality is required.

All parameter, circular-link, convexity, degree-one covering, and exact
fixture obligations pass. The theorem is VALID for every b,c>0, with
no novelty claim and no conclusion for other V/W metrics, U/V, or V/V.
