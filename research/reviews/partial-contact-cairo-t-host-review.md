# Independent hostile review: private-arm Cairo contacts and untileability

**Date:** 2026-10-10. **Verdict:** valid for the complete stronger revision
read on this date. The reviewer did not develop its proof, endpoint argument,
strengthening, or exact fixture. No substantive repair was required.

**Artifact:** [partial-contact-cairo-private-arms.md](../lemmas/partial-contact-cairo-private-arms.md).
The title still emphasizes doubled-side necessity, but this review covers
its stronger untileability theorem and finite-protoset extension as well.

## Exact claims and assumptions

Each fixed strictly convex pentagon has angles after sides (a,b,c,d,e)
equal to (90,120,90,120,120). Its a,b,c,d arms join90 to120, and its single
e side joins120 to120. All four-per-species arm slots are globally pairwise
distinct in numerical length. The set of species is finite. Reflections,
rotations, omitted species and arbitrary partial contacts are allowed.
There is no assumption on e coincidences, doubled e values, periodicity,
finite local complexity or an imposed native-side matching rule.

The contact theorem says every native-side T must be on an e side, at its
midpoint, with e=2r for an arm r, and a side has at most one T. The stronger
theorem says no such protoset admits a plane tiling at all, even if these
doubled e equalities are allowed. For two pentagons this excludes every
pair with eight globally distinct arm slots. The endpoint proofs are
self-contained and do not import the older ETE obstruction.

## Attempts to falsify the proof

**Additional stars or infinitely many wedges.** Finite fixed shapes have
positive minimum area and bounded diameters, so only uniformly finitely
many tiles can meet a point. At a genuine native corner, the sectors are90,
120, or straight180. Exhausting 90u+120v+180w=360 with u+v>0 yields only
(4,0,0), (0,3,0), and (2,0,1). Two straight sectors alone describe no native
corner and do not form a subdivision. Thus no native120 corner can lie
inside a side or share a point with a90 corner. All genuine subdivisions
are T stars with exactly two90 corners opposite a straight180 sector.

**The perpendicular seam might be only a piece.** At a T, the two90 tiles
share the perpendicular ray. Both native arms there end at120. Before
one of them ends, both sides of that ray are occupied; no third tile can
insert a native vertex with a positive sector. Unequal arm lengths would
place the first120 endpoint inside the other arm. This is forbidden by
the star equation. The seam is therefore a whole native arm of each tile,
without assuming the host-side contact is whole.

**Wrong endpoint or chirality match.** The global private-arm hypothesis
identifies the species and native arm slot from its length. The90 endpoint
of the seam is identified with the90 endpoint, so a half-turn reversing
endpoints is impossible. The unique opposite-side match is reflection in
the seam line. The arms on the host line are hence equal, say r, and their
120 endpoints are x-r and x+r. Polygon symmetries cannot introduce a
second native slot of this length, because all arm slots are distinct.

**An arm host could terminate before one bank.** Let the original host
arm's120 endpoint be left of the first T x. That endpoint must equal x-r:
either other ordering puts a120 corner in a side interior. Its90 endpoint
must be y=x+h with 0<h<r, since equality with the opposing120 corner is
illegal and extending beyond it makes it an interior120 contact. At y,
the old host has90 and the opposing bank has180, forcing a second T. Its
perpendicular seam is a full same-slot arm. Reflection creates a new
collinear arm of length L=r+h extending forward to x+r+2h. The old bank's
120 endpoint at x+r is strictly inside this new arm, contradiction. This
attack verifies both T stars and excludes all native arm hosts.

**An e host could support unequal banks, endpoint offsets, or multiple Ts.**
Private-arm reflection makes its banks equal. Both of its120 endpoints
must coincide with the bank endpoints, giving e=2r and a midpoint T.
For the auxiliary at-most-one-T claim even without private arms, follow
an opposing90-to120 side from one T. A further subdivision cannot precede
its120 endpoint because both sides of the segment are occupied. That
endpoint cannot itself lie in the host interior, nor can a subdivision
follow it in the host interior without already having that forbidden120
contact. Thus multiple Ts on one native side are excluded independently
of an assumed contact count.

**An arm ray at a beta star might face a whole or partial e side.** This
is the crucial unrestricted-contact alternative. At a120 star an arm
must face either an equal whole same-slot arm or a half of an e side of
length2r. Two unequal arms would place a90 endpoint in an arm interior,
which the preceding host contradiction excludes, in either ordering.
An e counterpart shorter than r places120 inside the arm; equal length
would identify120 with90. The only remaining e alternative is longer,
with the arm's90 endpoint at its interior T and consequently e=2r.
The source does not mistakenly label this partial e contact by length r.

**Doubled e values might permit the isolated beta corner.** Suppose an
e_H side hosts a bank r=b_S or c_S. Its beta endpoint meets S's isolated
beta corner with other arm q, where q is the other of b_S,c_S. The host's
other ray is arm p=a_H or d_H. The remaining120 tile K has an arm on
at least one of the two rays, since it has just one e side. If K's arm
faces p, it is the same H slot p, hence K's other side is e_H. That side
faces q as a half-e host, requiring e_H=2q. But the original host gives
e_H=2r, contradicting r!=q. If K's arm faces q, it is the same S slot q,
whose120 endpoint is isolated; K's other side is arm r. It would have to
match p as a whole arm, contradicting global slot uniqueness. These cases
exhaust one-arm and two-arm corners; they allow e equalities freely and
even allow H=S. Thus b,c cannot be half-e banks anywhere.

**A third tile might fill the remaining isolated beta wedge differently.**
At any tile S's isolated beta corner, its b arm now has a whole same-slot
mate. Endpoint-preserving reflection gives a second copy of S with the
same isolated120 corner. The remaining120 wedge has two boundary c arms.
Neither can face e, by the previous paragraph. The third tile would
therefore need two distinct native arm slots with the globally private c
length. A single native side cannot occupy two different rays at a corner,
and no second slot has that length. This is the final local contradiction.

**Omitted types, additional species, and e/arm coincidences.** Every argument
uses numerical uniqueness only among arm slots. It never assumes e cannot
equal an arm or another e; endpoint angle90/120 differences eliminate the
misleading equal-length alternative where needed. Each occurrence has an
isolated beta corner, so omission of types does not evade the final
contradiction. The same proof works for any finite number of Cairo species
with globally private arms; no two-species pigeonhole step is used.

## Independent finite checks

The review added
[verify_partial_contact_cairo_private_arms_independent.py](verify_partial_contact_cairo_private_arms_independent.py).
It builds both exact fixtures by direct side-vector closure over Q(sqrt3),
accumulates the vertices, checks every nonincident supporting determinant,
checks all five side norms and corner cosines, and checks the eight private
arms. It independently exhausts all native stars with u=0..4 right
corners, v=0..3 beta corners and w=0..2 straight sectors. It also checks
all sixteen doubled-length exclusions, although the stronger theorem
requires none of those exclusions. Both polygons are positive, genuine,
strictly convex and noncongruent (their length multisets differ).

Commands run successfully:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_private_arms_independent.py
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-private-arms.py

The existing independent Cairo ETE checker was also replayed successfully:

    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_distinct_side_independent.py

Its1546 finite cross-equality patterns are outside the stronger proof's
dependency list; their success is supplementary and is not claimed to
verify this unrestricted theorem. None of these computations searches
plane tilings or checks the infinite conclusion. The conclusion rests on
the manual local star and endpoint contradictions audited above.

## Defects, repairs, uncertainty and scope

No counterexample or substantive proof defect was found. No repair by the
reviewer is being counted as independently reviewed. The developing agent
completed the stronger proof before this reviewer read its final revision.
The argument has no imported classification dependency. Its exact
geometry tests and angle enumeration were independently replayed.

Remaining uncertainty is outside the theorem: arm coincidences, other
angle words, arbitrary pentagon partners, periodicity or aperiodicity of
surviving families, and novelty relative to primary literature. This local
untileability result does not establish the two-convex-tile impossibility
theorem. For a tileable two-Cairo pair it provides the exact necessary
condition that at least two among its eight native arms share a length;
if each member's four arms are internally distinct, this equality must
be across species.

**Final verdict:** valid for the contact theorem and the stronger finite
private-arm Cairo untileability theorem under the explicit hypotheses.
