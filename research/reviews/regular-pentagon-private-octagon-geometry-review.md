# Fresh hostile review of the private-octagon metric classification

**Verdict: valid**, conditional on the explicitly imported, independently
reviewed all-obtuse forcing, octagon good-limit theorem, and private-chain
geometry. The exact finite classification and the whole-plane existence
certificate pass an independently structured checker. This is a restricted
family theorem, not a resolution of the unrestricted main problem.

This reviewer did not develop the [producer](../searches/regular_pentagon_private_octagon_geometry.py),
[certificate](../certificates/regular-pentagon-private-octagon-geometry.json),
or [classification lemma](../lemmas/regular-pentagon-private-octagon-metric-classification.md).
The new checker is
[verify_regular_pentagon_private_octagon_geometry.py](verify_regular_pentagon_private_octagon_geometry.py).
It does not import or execute the producer. It reconstructs closure by
determinant identities, constructs every permitted endpoint map, uses exact
separating-axis tests for overlap, and reconstructs retained intersection
areas from support-line intersections and a monotone convex hull. Thus the
overlap decision is different from the producer's clipping algorithm.

## Reduction to the twelve closures

The family assumption is exactly six unit Q sides and two distinct,
positive, nonunit sides. Distinctness makes each private length unique in
Q. A private side therefore meets the same native side of another Q, and
cannot meet P. The all-obtuse star language has one beta and two alpha
sectors. A beta/beta private side is impossible, since matching that unique
side puts beta at each endpoint on both copies. An alpha/alpha side is
excluded by nonadjacency of Q's alpha corners. Each private side must
therefore have alpha/beta endpoints, and their matching reverses the endpoint
types. Two private sides incident to the same alpha corner would give two
beta neighbors at that corner. They must cover the two alpha corners
separately. This does not assume a saturated original tiling.

Normalize the smaller cyclic separation of the alpha corners to d=2,3,4.
A rotation chooses vertex 0, a reflection chooses the direction around Q,
and side 0 is normalized to the positive real direction. The private sides
are then exactly i in {7,0} and j in {d-1,d}. This gives twelve cases,
with no length cutoff. Closure uniquely determines both unknown lengths
whenever the two relevant directions are not parallel.

The checker reconstructs all twelve directions and their vector sum. It
uses cross products to solve the two closure equations and checks every
explicit entry of the lemma's closure table. In the parallel d=2 case the
remaining closure vector is not parallel to either unknown side. In both
parallel d=4 cases it is zero and the unknown directions are opposite,
forcing equal private lengths. The other d=4 cases force unit lengths.
Thus the parallel cases leave no unexamined positive distinct solution.

The only eligible rows are

* d=2, sides (7,1) and (0,2), private lengths
  ((5-sqrt(5))/2,sqrt(5)) and their reversal;
* d=3, sides (7,2) and (0,3), private lengths (phi,2) and their reversal.

All strict supporting-side inequalities are checked for all four octagons.
The checker also explicitly constructs a reflection carrying every vertex
of the outgoing representative to incoming vertex d-k modulo 8. This
verifies congruence of the two members of each pair, including the offset
for side indices. The finite domain leaves two metric classes, Q2 and Q3.

## Mandatory collar and the complete third-neighbor gate

For an untileability argument, the six regular P neighbors on Q's unit
sides are required in the admitted **good limit tiling**, supplied by the
reviewed [octagon chain-limit theorem](../lemmas/obtuse-pentagon-octagon-chain-limit.md).
The general original-tiling periodicity theorem does not assert that every
unit Q side in the original tiling meets P. The classification lemma
correctly invokes the good-limit theorem before requiring this collar.
Its conclusions apply to an original tiling through that existence
implication, not by deleting possible original unit Q-to-Q contacts.

In the good tiling every Q has precisely its two private Q neighbors.
Those neighbors are the prescribed half-turns. The two Q motifs and all
twelve regular P placements on their unit sides form the forced chain
collar. Exact equivalence modulo its period removes duplicate P copies,
leaving eight. The checker independently verifies all possible integer
chain shifts for all ordered motif pairs: 88 comparisons in each d=2
branch and 72 in each d=3 branch. None has positive-area intersection.
This establishes only a collar, not a plane extension.

For both outgoing representatives, the selected P shares side 0 with Q
side d-1 and side 4 with the known half-turn neighbor. The checker verifies
the endpoints of these contacts. The two P neighbors of a good P occupy
nonadjacent positions. With Q slots 4 and 0 already prescribed, its third
Q neighbor must therefore be in slot 2; slots 1 and 3 would leave adjacent
P-neighbor slots. Each endpoint of slot 2 also meets P along the other
incident side, so its Q endpoint must be beta. This gives exactly four
eligible beta/beta unit sides on Q: 3,4,5,6 for Q2 and 1,4,5,6 for Q3.

For each eligible Q side, consider both endpoint bijections and both
linear parities. These are all four isometries identifying that source
segment with the prescribed P segment. Exactly two place Q on the opposite
supporting half-plane, one of each parity. The checker constructs all four
before applying this half-plane test; hence the retained eight candidates
include every rotation and reflection placement. Any intrinsic Q symmetry
could duplicate these parametrizations but could not introduce another
geometric placement. This gate makes no chirality assumption.

The reviewed [private-chain theorem](../lemmas/regular-pentagon-private-octagon-periodicity.md)
forces all Q axes to be parallel, regardless of additional unit contacts.
The checker derives the axis direction separately for all eight maps in
each branch. Q2 has just two parallel candidates, side 4 preserving and
side 6 reversing. Q3 has three, side 1 preserving, side 5 preserving, and
side 6 reversing. Every retained candidate has nonzero axis separation.
Thus this proof never relies on rejecting a coincident axis merely from
the producer's generic status label.

For both parallel Q2 candidates, the checker reconstructs both mandatory
chain collars and exhaustively checks their joint shifts. The first positive
intersection is between the old half-turn Q and the new Q translated by
one chain period. Its exact area is sin(pi/5)>0. Both placements of the
forced third neighbor therefore fail. This excludes a good plane tiling,
and hence any original plane tiling. The mirror calculation excludes the
incoming representative as well. Partial original contacts cannot evade
the argument: all-obtuse forcing and the reviewed good-limit existence
were invoked with unrestricted original contacts.

## Q3 has a certified rank-two whole-plane tiling

The checker additionally replays all parallel Q3 joint-collar comparisons:
the side-1 preserving candidate overlaps; the other two candidates have
202 and 204 complete comparisons respectively and no interior overlap.
Their retained band pieces are independently reconstructed by support
half-planes, and their total area equals the cylinder-band covolume.
The classification needs only the preserving side-5 candidate's direct
whole-plane witness; no general band-gluing theorem is inferred.

For that witness the checker reconstructs exactly the six lemma motifs

    Q, H_b(Q), S(Q,1), S(Q,2), S(H_b(Q),5), S(H_b(Q),6).

It verifies the stated period vectors, all coordinates, all four pentagon
regularity constructions, and the exact formulas for the P area, Q area,
and lattice determinant. There are two Q copies and four P copies, with
no auxiliary prototile or marking.

In lattice coordinates, subtracting each ordered pair's vertex-coordinate
bounds gives a finite interval for each integer shift coordinate. Every
integer pair in those intervals is tested. Shifts outside them cannot
intersect because one coordinate projection is disjoint. Excluding the
identical-copy comparisons gives exactly 36 comparisons, all with disjoint
interiors by exact separating axes. This is a derived complete overlap
domain, not a bounded period or neighborhood search.

The independently verified sum of the six motif areas equals the positive
lattice covolume. With pairwise interior disjointness, integrating their
periodic indicators over a fundamental cell therefore gives full cell
area. The periodic union is locally finite and closed, since the lattice
is discrete and the finitely many motifs are compact. An uncovered point
would have an uncovered open neighborhood of positive area. The area
identity excludes this. Thus these motif translates cover the entire
plane and supply an admitted doubly periodic tiling.

## Replay and limits of this audit

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_regular_pentagon_private_octagon_geometry.py
```

The checker completed successfully after also checking the final lemma's
explicit closure, motif, period, and area formulas. All arithmetic is exact
AA/QQbar arithmetic. Each nonrational certificate value is decoded from its
irreducible minimal polynomial and an exact rational interval containing
one root; no floating-point overlap decisions are used. No producer imports,
solver, stochastic choices, timeouts, or geometric cutoffs are involved.

The imported forcing and limit theorems are named reviewed dependencies;
this finite audit does not claim a second complete replay of their analytic
proofs. It establishes the geometry needed for the classification and
the direct periodic witness. Equal private lengths, other octagon angle
signatures, adjacent alpha corners, and irregular equiangular pentagons
remain outside this result. No priority or universal novelty claim is made.
