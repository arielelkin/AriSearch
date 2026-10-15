# Six-distinct / five-distinct hexagons: independent exact angle-endpoint gate

Date: 2026-10-15. Status: completed independent computational cross-check.
This record is not itself the complete structural theorem or an independent
solver-UNSAT certificate. The root agent's support-mask enumeration supplies
a separate solver-free check of the relevant finite implication.

## Question and exact domain

A has cyclic numerical-length word (0,1,2,3,4,5). B has five distinct
numerical lengths, its unique repeat separated by two side slots.
The eight representative B words supplied by the independent classification
are, in order:

    (0,2,0,3,6,4), (0,2,4,6,5,6), (0,2,0,3,5,6),
    (0,2,0,3,1,4), (0,1,4,2,5,2), (0,1,5,2,4,2),
    (0,1,0,2,5,3), (0,1,5,1,4,2).

This program does NOT verify completeness of that supplied representative
list. Its exact domain is these eight words, all their numerical triangle
stars with ACTUAL corner slots, all injective four-shared-slot selections,
and rational angle/support assignments specified below. Corner i, 0<=i<6,
is the corner after side i of A; corner 6+i is after side i of B.

## Exact model

There are twelve real angle variables measured in units pi, strictly between
zero and one. Each polygon's six angles sum to four. For every triangle in
the union length graph, choose one actual corner occurrence on each of its
three edges; this yields the complete finite list of potential trivalent
stars. Each star has an independent active Boolean. Active implies its
three angles sum to two. Every actual corner occurs in at least one active
star. Active stars therefore overapproximate the stars actually used by a
hypothetical everywhere-trivalent whole-edge tiling.

For each four-slot matching (one side slot of A to one equal-length side
slot of B), assign formal shared labels to the four matches and different
private labels to the other four side slots. Retain the matching only when
its formal graph has four triangles partitioning all twelve actual corners.
The gate asks for a model in which NONE of these ring's four angle equations
hold simultaneously. The numbers of formal rings are 1,1,1,1,0,2,0,2.

In the endpoint-enhanced gate, every active star and each of its three rays
must admit an active star at the opposite end of that whole side. The two
tiles sharing the ray are fixed by their actual corner slots. Each actual
corner's two incident lengths are different, so the ray length selects one
of its two native sides uniquely. Following that side gives its far-end
actual corner. The two far-end corners must occur together in an active
star. If their indices coincide, they represent two copies of the same
actual corner; that cannot occur in a numerical triangle star, so the
original star is forbidden. This is a necessary condition on any actual
whole-edge trivalent tiling, without assuming independent star choices
can be realized geometrically.

Finally a third gate additionally demands that some actual corner belong
to at least two different active stars. UNSAT then means that all no-ring
endpoint-closed supports must partition the twelve actual corners.

## Results

All eight angle/coverage gates are SAT: the naive angle-only ring strategy
fails for every representative.

With endpoint support, six no-ring gates are UNSAT. The exceptions are the
second and eighth representatives. Their retained SAT models have active
stars respectively

    second: (0,1,6), (2,3,7), (4,8,10), (5,9,11);
    eighth: (0,1,11), (2,3,10), (4,7,9), (5,6,8).

These are exact abstract-angle/support models, not polygon realizations.
They refute an argument using only these constraints to force a standard
four-triangle ring. For both, the third (branching) gate is UNSAT. Indeed,
the branching gate is UNSAT for all eight representatives. Thus the exact
finite models support this dichotomy: a legal four-triangle ring exists,
or every actual corner has a unique active star. The second case is suited
to the intrinsic neighbor-determinism periodicity argument; it need not
admit the standard four-face ring quotient.

A small discarded construction experiment also appears in the certificate:
for rings leaving B's repeated slots private, explicitly pair four faces
A0,A1,B0,B1, with B reflected, test sixteen common-crossing parity choices
and the three perfect matchings of the four repeated private B side
occurrences. Only the standard second-representative ring support appears
among connected eight-vertex trivalent quotients. This experiment is not
used in the dichotomy or any impossibility theorem. It merely rejects the
specific proposed crossed-private-side repair of the two SAT examples.

## Replay and limitations

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-five-2026-10-15.py

The command writes
[the retained gate record](../certificates/hexagon-six-five-angle-gate-2026-10-15.json).
It uses Python and the locked Z3 package, exact linear rational arithmetic,
no random seed, and a 60-second timeout PER gate. There are 24 gates, all
of which completed SAT or UNSAT with no UNKNOWN. SAT angles and active
supports are retained as exact rational strings. There is no orientation,
coordinate, or period-size enumeration in these gates. No angle model is
promoted as a convex-polygon tiling witness.

A final proof should use the separate exact support-mask and linear-span
verification, plus the reviewed defect-free limit and either the explicit
four-face ring construction or intrinsic neighbor determinism. This record
is an independent solver-based corroboration; bounded failure to find a
periodic tiling plays no role.
