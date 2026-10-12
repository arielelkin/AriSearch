# Independent hostile review of the boundary-point spoke dual

Date: 2026-10-12. Reviewer independent of the mechanism author.

**Verdict: VALID within the exact stated source and network domain.**
This is a local obstruction for the full spoke dual, not an exhaustive
classification of neighbour-dependent recompositions or all Penrose sources.

Reviewed:

* `research/lemmas/penrose-boundary-dual-spoke-obstruction.md`;
* `research/reviews/penrose-boundary-dual-trivalent-star.json`;
* `research/reviews/verify_penrose_boundary_dual_trivalent_star.py`;
* the fixture-producing exact patch script and the repaired candidate
  statement in `research/lemmas/ammann-two-class-reconstruction.md`.

## Topology, crossings and slits

Convexity and strict placement are essential and sufficient. A ray from
an interior p_r meets the boundary of its convex source polygon in only
one point. Distinct edge-interior q_e therefore produce distinct outgoing
rays. The spokes inside one source tile intersect only at p_r; spokes in
different tile interiors cannot intersect. At shared source edges only
the two incident spokes meet, at the designated shared q_e. There are no
unaccounted crossings or accidental extra network vertices.

A source tile is divided into sectors indexed by its consecutive boundary
corners. Across each erased source edge, the open subinterval from either
endpoint to q_e joins exactly the two corner sectors indexed by that same
endpoint. Thus the equivalence class of corner sectors is indexed by one
source vertex. It cannot pass to the other endpoint without crossing a
spoke. Each such union is a disk around the finite source star with the
simple alternating boundary stated in the theorem. Distinct p_r lie in
distinct tile interiors, and distinct q_e in distinct edge interiors, so
the alternating boundary has no repeated vertices.

This also answers the slit concern raised for the older graph-mask
search. Every spoke separates the sectors of two distinct consecutive
source vertices, and globally belongs to their two different faces.
No spoke is a dangling bridge inside a single face. Consequently passing
to face closures cannot silently fill an internal slit or fuse faces in
this construction. Intentional extra edges, omitted spokes, or later
face fusion would change the theorem's declared domain.

Local finiteness gives a finite incident star. The spokes in that star
avoid its source vertex by strict placement. Other source tiles cannot
accumulate there. Hence a sufficiently small disk around the source
vertex belongs to the corresponding network face; its area is positive.
No uniform global lower bound on p/q distances is needed.

## Convexity and the periodic escape

At each q_e there are exactly two rays and two distinct incident faces.
Their local sectors sum to 2pi. Convexity of both closures forces both
sectors to equal pi, so the two rays are opposite. The neighboring source
interior points are therefore collinear with q_e between them. This
argument requires convexity of both faces, as the statement assumes;
convexity of only the selected trivalent face would not suffice.

Removing these straight subdivisions leaves at most one intrinsic corner
per incident source tile. At valence three, a nonempty compact convex
polygon with positive area and at most three intrinsic corners must be
a genuine triangle. Mirror conventions cannot evade this conclusion.
The periodic triangle escape uses only a half-turn and translations,
so even restricting to orientation-preserving isometries would retain it.
The target protoset convention permits a tiling to omit its other shapes;
requiring both shapes in every tiling would be a different problem.

## Exact fixture and source scope

The companion verifier passed. It uses exact cyclotomic arithmetic and
an explicitly chosen real algebraic embedding, not floating-point signs.
It checks unit-edge convex parallelograms, the three central angles,
shared radial edges with centers on opposite sides, and exact center-line
intersections strictly inside both segments. It also checks that the
three-center triangle strictly contains the central source vertex.
Those tests establish the concrete geometric star and centered triangle.
They do not independently certify arrow matching or extendability to an
infinite marked Penrose source.

A fresh run of the claimed producer with deflation count three generated
60 rhombs and 76 vertices. Comparing every stored coordinate and marked
corner frame at rhomb IDs 0,2,7 with this output passed. The central vertex
is incident to exactly those three rhombs in the regenerated patch.
Thus the fixture's producer provenance is checked rather than merely
copied from its metadata.

The stronger statement that every marked Penrose tiling contains this
fixture still requires the appropriate source-language legality and
repetitivity/minimality result. The mechanism explicitly makes no such
new universal claim. Its theorem applies to an actual edge-to-edge
source tiling with any trivalent vertex; its Penrose corollary is
conditional on the source containing the retained star. Nothing here
proves an obstruction for arbitrary bare-rhomb sources lacking that star.

## Repaired older Ammann wording

The reconstructed two-parameter Ammann proposition now states uniqueness
only after discarding strata containing triangle or quadrilateral
prototiles. This matches the independent 130-system review: low-corner
strata are excluded as aperiodic candidates by monohedral escapes, without
claiming their congruence-collapse points have been classified. The status
and scope paragraphs also keep generalized decoration exhaustiveness
separate. No residual closed-boundary uniqueness overclaim was found.

## Replay

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_penrose_boundary_dual_trivalent_star.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/ammann-two-class-patchdata.py 3 /tmp/hexagon_strategy_penrose_patch3.json

Both runs passed on 2026-10-12. The producer comparison additionally checked
that each retained rhomb's kind and four coordinates, its central corner,
and the complete incident-rhomb list agree. No source producer, mechanism
lemma, fixture, original certificate, discovery log or environment file was
modified during this review.
