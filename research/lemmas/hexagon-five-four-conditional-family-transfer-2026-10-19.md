# Five/four four-face carrier: failed broad transfer and conditional escape

Date: 2026-10-19. Status: proved conditional lemma and exact finite gate;
[independent Sol hostile review](../reviews/hexagon-five-four-conditional-family-transfer-hostile-sol-2026-10-19.md) passed. The original positive fixture also passed its separate
Sol review.

Let A,B be strictly convex hexagons, with native side words
A=(0,1,2,0,3,4), B=(0,1,1,0,2,3), common positive lengths by color.
Write a_i,b_i for the native interior corner at the END of side i.
Assume first-support mask33416, namely

    a0+b1+b0 = 2pi,
    a1+b3+b2 = 2pi,
    a2+a3+b4 = 2pi,
    a4+a5+b5 = 2pi,
    sum(a_i)=sum(b_i)=4pi.

**Conditional theorem.** If additionally a2=b3, this pair admits an
edge-to-edge doubly periodic tiling with two A and two B per fundamental cell.
Reflections are allowed. Distinctness of lengths is unnecessary for the theorem.

## Exact topology and row gate

Replay the certificate producer:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-family-transfer-2026-10-19.py

Output: `research/certificates/hexagon-five-four-family-transfer-2026-10-19.json`.
It reads retained input certificates, never the geometric search producer.
Using Q(sqrt(3)) at its positive embedding, it independently recovers the twelve
unique reversed edge mates modulo the original two periods. Each pair retains
stored face/side, native side, handedness, and lattice offset. Faces0,1 are A
with native vertex i; faces2,3 are reflected B with native vertex5-i mod6.
Native B side for stored side i is4-i mod6. Coordinate distance checks verify
these index maps.

The circular corner links (face:stored-vertex) are:

    (0:0,1:5,3:5), (0:1,2:3,3:4),
    (0:2,1:3,2:2), (0:3,1:2,3:2),
    (0:4,2:0,3:1), (0:5,1:0,2:5),
    (1:1,2:4,3:3), (1:4,2:1,3:0).

The endpoint adjacency graph gives these eight connected degree-two links,
so every vertex has a disc neighborhood. Every edge is paired once, reversing
boundary direction, so the surface is closed and orientable. Its face adjacency
graph is connected. F=4,E=12,V=8 gives Euler characteristic zero; classification
of connected closed orientable surfaces identifies it as a torus. These are
abstract polygon gluings and do not assume the original Euclidean embedding.

The eight angle equations in that order are

    a4+a5+b5=2pi; a0+b0+b1=2pi;
    a1+a2+b2=2pi; a1+a2+b2=2pi;
    a3+b3+b4=2pi; a4+a5+b5=2pi;
    a0+b0+b1=2pi; a3+b3+b4=2pi.

In units of pi, retaining the negative right side as coordinate13, the six
support rows have rational rank5; the eight carrier rows rank4; their union
rank6. The certificate retains the actual integer rows, membership coefficients
for each carrier row lying in the support span, and an independent extra row.
That extra row is a1+a2+b2=2pi. Subtracting support row2 gives a2-b3=0;
the other new carrier row differs from support row3 by its negative.
Thus the entire obstruction has exactly codimension one. Broad transfer from
the first support alone fails this requested linear implication gate.
No claim is made that polygon closure forces this extra relation.

## Conditional geometric development proof

Glue two copies of A and two reflected copies of B using precisely those twelve
native side pairings. Each matched pair has equal length by its color, so a
unique endpoint reversing isometry identifies the whole sides. Strict convexity
supplies simple polygon discs of positive area with positive interior angles;
no edge collapses. The preceding topology is independent of the metric.
The support equations plus a2=b3 make every circular link have total angle2pi.
Consequently the quotient carries an everywhere nonsingular Euclidean metric:
face interiors have Euclidean charts, edge interiors unfold across the glued
edge, and vertex sectors unfold to a disc because their cyclic angles total2pi.
The orientation already checked makes these charts orientation preserving.

This compact flat torus is complete. Its universal cover, with lifted length
metric, is a complete simply connected flat surface and hence isometric to the
Euclidean plane. One justification is continuation of Euclidean charts along
paths: zero curvature makes development invariant under homotopies; completeness
extends every straight geodesic for all time, making development a covering of
the complete plane, and simple connectivity of the plane makes that covering
an isometry. This is the standard flat-surface development theorem, with its
completeness and nonsingular-angle hypotheses supplied here.

Deck transformations are orientation preserving Euclidean isometries acting
freely. Any nontranslation orientation preserving Euclidean isometry is a
rotation about a fixed point, so cannot be a nontrivial deck transformation.
Thus all deck transformations are translations; they form a discrete group
isomorphic to pi1(torus)=Z^2. Compactness of the quotient makes this group a
full rank lattice. This establishes trivial rotational holonomy and two
independent, nonzero translational periods for each admissible metric, without
assuming the original fixture period formulas persist. Lattice covolume is
the area of the compact flat surface, namely2 area(A)+2 area(B)>0.

The lifted polygon cell decomposition is a plane tiling: the isometry from the
universal cover preserves the disc cells, interiors are disjoint, and their
union is the entire plane. The deck lattice permutes these tiles. This proves
coverage, nonoverlap, positive area and nondegenerate periods for the conditional
family. It does not depend on a numerical continuity argument or a formal
edge-balanced chain being embedded.

## Bounded consequence for the retained grid

Among the39 retained exact metric representatives in
`hexagon-five-four-angle-grid-2026-10-19.json`, exactly18 satisfy a2=b3.
Of these,13 have no H1 species in the prior reviewed monohedral audit.
The new script independently reconstructs each of the18 selected pairs from
its exact Q(sqrt(3)) lengths and degree angles. It checks positive distinct
lengths, exact closure, total turn360, all strict supporting halfplanes, all
support rows and all carrier rows. The complete selected indices, exact angles
and lengths are retained in the new certificate. Accordingly all18 have the
conditional mixed periodic escape;13 are cases from the earlier18-member
nonmonohedral list (including the already reviewed positive fixture).
The other five members of that nonmonohedral list are untouched by this carrier.
The earlier monohedral classification is needed only to name that subset,
not for the conditional periodicity proof.

The failed broad gate is the stopping point for claims covering all first-support
metrics. No further support tests, nonlinear solver calls, or larger torus search
were made. The unrestricted research problem remains unresolved.
