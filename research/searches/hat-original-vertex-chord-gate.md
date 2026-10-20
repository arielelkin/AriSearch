# Exact Hat original-vertex chord gate

Date: 2026-10-19. Complete finite negative gate;
[independently Sol-reviewed](../reviews/hat-original-vertex-chord-gate-sol-review.md).

The source is the exact 13-vertex outline in
`research/certificates/hat-eight-kite-convex-cluster-gate.json`, the reviewed
reference Hat Tile(1,sqrt(3)). Its 13 coordinates agree with Craig Kaplan's creator-source
[hatviz geometry.js](https://github.com/isohedral/hatviz/blob/main/geometry.js).
The new domain uses arbitrary straight chords
between its original outline vertices. Chords must lie in the Hat, have
interiors disjoint from other chords and the outline, and give a partition
into convex polygons. No atom grid is refined or imposed. Genuine sides
exclude collinear boundary subdivisions. Isometries may reverse orientation.
Both output congruence classes must occur and each piece must have five or
six genuine sides. The declared cap is 30 seconds, with no source deformation,
Steiner vertices, chord crossings, or multiple Hats.

## Complete domain and exact outcome

A dissection with d chords has d+1 faces and 13+2d face-side incidences before
collinear simplification. Thus 5(d+1)<=13+2d and d<=2. The producer exhausts
all combinatorial noncrossing diagonals of the cyclic 13-gon, including ones
that would fail geometric containment: 1 empty set, 65 single diagonals,
and 1365 two-diagonal sets. It splits cyclic face lists and removes collinear
vertices using integer orientation. Every resulting face must have five or
six vertices and all positive turns. Pairwise squared-distance words under
all cyclic shifts and both directions identify congruence exactly, with
metric deltaX^2+3 deltaY^2. Coordinates (X,Y) represent
(X/2,sqrt(3)Y/2).

There are **zero accepted partitions**, even before imposing two classes.
The complete certificate retains the source outline, cap, combinatorial
counts, and empty survivor list. The periodic monohedral audit is not reached:
there is no candidate class pair to audit. No plane existence or aperiodicity
claim follows.

## Independent short obstruction

The separate checker uses a proof rather than the producer enumeration.
The exact negative turns occur precisely at original vertices 0,4,8,11.
Every reflex corner must be incident to a dissection chord, otherwise one
face retains its reflex angle. At most two chords can occur, so exactly two
chords must pair these four reflex corners. There are only three matchings:

* (0,4),(8,11) cuts off the face [8,9,10,11], at most four genuine sides;
* (0,8),(4,11) has alternating endpoints, hence cannot be noncrossing;
* (0,11),(4,8) cuts off the face [11,12,0], at most three genuine sides.

Consequently none belongs to the requested domain. This argument also
independently verifies the producer's empty output and does not depend on
congruence algorithms, hull routines, numerical tolerances, or prior atom
searches. The exact outline is bound to the reviewed whole-kite source.

## Scope and replay

Arbitrary new boundary points, interior Steiner points, bent cuts, changed
Hat metrics, and multiple-Hat dissections are outside this finite gate.
A successful two-class fixed Hat dissection would transfer plane existence
by dissecting every member of a known Hat plane tiling. Shape-only
recognition of Hats, exclusion of unwanted assemblies and partial contacts,
and exclusion of monohedral periodic tilings would still require proofs.
Here the necessary dissection premise already fails. Stop this original-
vertex chord topology; enlarging an atom grid is not justified.

Run from repository root with assertions enabled:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/hat-original-vertex-chord-gate.py research/certificates/hat-original-vertex-chord-gate.json
mise exec -- conda run --no-capture-output -n arisearch python research/searches/check-hat-original-vertex-chord-gate.py research/certificates/hat-original-vertex-chord-gate.json
```

No novelty claim is made. This excludes one exact changed-cut mechanism,
not arbitrary convex pairs or arbitrary Hat dissections.
