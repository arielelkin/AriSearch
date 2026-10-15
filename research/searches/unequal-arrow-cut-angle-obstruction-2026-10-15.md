# Unequal arrow-indexed cap cuts: a certified angle obstruction

**Later status:** the full stated off-normal mark-local receiving-hexagon
component is excluded by the independently reviewed
[combined congruence obstruction](../lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md).
The narrower calculations below retain their explicitly stated scope.

Date: 2026-10-15. Status: exact elementary rewrite independently hostile-reviewed VALID
([review](../reviews/unequal-arrow-cut-angle-hostile-2026-10-15.md)). Supplementary exact finite certificates
also verify the angle obstruction. No metric search or main-problem
solution is claimed. This closes a newly changed construction component,
not arbitrary fractional partitions.

## Changed exact construction domain

Use the three-sector+cap source partition and complete cap indexing in
`thick-cap-split-congruence-gate-2026-10-15.md`. Replace the equal radial
cut distances by

    c_i=t+r_(Z,i)(N_i-t), 0<r_(Z,i)<1.

The six fractions depend only on mark Z and ARROW-INDEXED ray role i and
are identical in every source species/parity context. Keep thin caps as
hexagons; split each thick cap by a chord joining interior points of its
opposite edges0 and3 into two pentagons. Keep all receiving output words
specified in that artifact. All source sectors, cuts and final polygons
are assumed strict and embedded; inadmissible choices are already excluded.

The donor apex still has the normal-foot rule

    M=T+a_Z(H-T), t=M+h_Z n_donor,
    0<a_Z<1, h_Z>0,

on each unit source edge with arrow T->H. Offsets/heights are mark-local.
No condition that the new thin caps are cyclic is imposed.

**Theorem.** No admissible realization in this changed domain has only
one pentagon congruence class P and one hexagon congruence class H.
The contradiction uses receiving H polygons alone; all P aliases, thick
chord parameters, and cap/child matching choices are automatically covered.
It holds under every reflected or rotated prototype correspondence.

## Source endpoint angles, with correct arrow roles

Use degrees for exact rational angle equations. Let Xt,Xh,Yt,Yh be the
donor triangle base angles at actual arrow tail/head for marks X,Y.
All are strictly between0 and90, by the normal-foot rule. Write

    a=36+Xt-Yt, b=36+Yt-Xt,
    c=108+Yt-Xh, d=108+Xh-Yt.

The thin rhomb has source angles36,144,36,144. The thick has72,108,72,108.
At a source vertex the receiving quad's retained original endpoint angle
is the rhomb angle plus the incoming triangle base angle minus the outgoing
donor base angle. The exact native arrow table is

    thin:  AB X A->B, BC X C->B, CD Y C->D, DA Y A->D;
    thick: AB X A->B, BC Y B->C, CD Y D->C, DA X A->D.

For either donor parity, the four thin receiving endpoint angles are
{a,b,144,144}; the thick ones are {c,d,72,72}. Incoming X-tail corners
specifically have angle a in thin contexts and72 in thick contexts.
Incoming Y-tail corners have b in thin contexts. This mark distinction
must not be erased. Strict convexity gives a,b,c,d in(0,180), with

    a+b=72, c+d=216.

Every such endpoint remains a genuine uncut corner in a receiving hexagon.
Thus a common prototype H must contain the numerical values

    144,72,a,b,c,d,

possibly with coincidences, among its six angles. Its six angles lie in
(0,180) and sum720.

## First elementary lemma: necessarily a=b=36

If a!=b, the four required H angles a,b,72,144 are all distinct: a,b
are positive and sum72, so each is less than72. Their sum is288. The two
remaining H angles are each strictly less than180, making the entire sum
strictly less than648, contrary to720. Hence a=b=36 and Xt=Yt.

H therefore contains36,72,144. Its three remaining angles sum468; since
each is below180, each is strictly above108. Thus36 and72 each occur exactly
once, and the other FOUR H angles are all strictly above108. This capacity
fact will replace any search over H angle coincidences.

## A common external cut-angle pair

The donor node's ray0 goes to actual arrow tail T, ray1 to M, ray2 to H.
Its cut points c0,c1 depend only on mark Z: the original triangle T,M,t
and the two fractions r_(Z,0),r_(Z,1) do, independently of donor source
species or parity. Thus every receiving hexagon using the arrow-tail
half of an X donor has the SAME ORDERED pair of new angles (s,t) at c0,c1,
when its boundary is read from retained endpoint T through c0,c1 toward M.
This assertion concerns a local geometric pair, not a preferred direction
of the prototype H; all prototype D6 directions are included below.

The original quad corner at the external apex in that half is90-Xt.
Truncating a convex corner of angle theta by an arbitrary chord between
its incident rays creates two angles whose sum is180+theta. Equal radii
are unnecessary for this sum identity. Consequently

    s+t=270-Xt, so 180<s+t<270.

A thin X-tail receiving H therefore contains cyclic triple (36,s,t), and
a thick X-tail receiving H contains (72,s,t), each up to arbitrary D6
correspondence. A thin receiving H also has a144 corner.

## Second elementary lemma: the cyclic word is impossible

A thin X-tail receiving H contains ordered triple (36,s,t), and a thick
X-tail receiving H contains (72,s,t), each in either cyclic direction.
The two small angles36 and72 are unique. Hence neither s nor t can be36
(the thin triple would repeat it) or72 (the thick triple would repeat it).
The preceding capacity fact and s+t<270 give

    108<s,t<162.

Delete36 and72 from H's cyclic word. Four large-angle occurrences remain,
in the two arcs between the two small angles. Up to swapping the arcs,
their sizes are0/4,1/3,or2/2. Each small angle's triple must point into an
arc with at least two large entries. These cases include ALL rotations,
reflections, repeated angle values, and choices of D6 correspondence.

* In the0/4 case, both small angles point into the four-entry arc from
  opposite ends. Its entries are (s,t,t,s). The entire H sum is
  108+2(s+t)<648, contradiction.
* In the1/3 case, both point into the three-entry arc. Its entries are
  (s,t,s), with one other large entry v. The H sum is
  108+(s+t)+s+v<108+270+162+180=720, contradiction.
* In the2/2 case, if the two triples point into different arcs, four large
  entries are covered and the first case's sum bound applies. If they
  point into the SAME arc from opposite ends, s=t=q<135. Its entries are
  (q,q). The other arc must contain the required144 angle, since q<135;
  denote its other entry by v<180. The H sum is
  108+2q+144+v<108+270+144+180=702, contradiction.

No cyclic H word exists. This proves the theorem by an elementary angle
argument; the finite rational certificates below are corroboration only.

## Supplementary exact certificate and finite scope

Supplementary certificate:

    research/certificates/unequal-cap-minimal-angle-2026-10-15.json

Generator and small verifier:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/unequal-cap-minimal-angle-certificate-2026-10-15.py --output research/certificates/unequal-cap-minimal-angle-2026-10-15.json
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/unequal-cap-minimal-angle-certificate-2026-10-15.py --verify research/certificates/unequal-cap-minimal-angle-2026-10-15.json

The generator uses rational row reduction and strict Fourier-Motzkin
elimination on6 angle variables, preserving all row-combination weights.
The separate --verify path DOES NOT call either elimination procedure:
it reconstructs the complete ordered406+72 branch domain, reconstructs
all input rows, and checks exact Fraction-weighted sums. For a strict
certificate it verifies nonnegative inequality weights with at least one
positive weight, and that all variable coefficients vanish while the
constant is nonpositive. For an equality certificate it checks a nonzero
constant with all variable coefficients zero. Observed result: PASS.

The earlier bounded Z3 subgate
`unequal-cap-h-angle-gate-2026-10-15.py` directly models16 receiving H words
from the actual four source/parity arrow contexts, all12 aliases each,
strict original quad angles and mark-local external cut pairs. It returned
UNSAT within its60-second declared cap. Its retained JSON is corroboration
only, not a dependency of the certified proof. No P metric congruence or
larger quotient/patch search was run.

## Correction provenance and remaining construction escapes

An early proposed864-branch reduction incorrectly gave BOTH thin angles
36+Xt-Yt and36+Yt-Xt to the same X-tail external pair. The second belongs
to Y-tail contexts. That reduction was withdrawn immediately, before
promotion. Its certificate was replaced; no theorem relies on it. The
corrected certified route first derived Xt=Yt by the independent203-partition
angle lemma, and only then compared the genuine X-tail36/72 contexts. The final
478-branch certificate has the corrected domain. The elementary capacity
and cyclic-arc proof, supplied independently by the root, now makes that
certificate unnecessary for the main theorem. A minimal three-triple
subgate without the144 requirement was SAT, for example H angles
(36,269/2,269/2,72,164,179); this is only a discarded subgate diagnostic,
not a full prototype or geometric candidate.

This obstruction survives unequal radial fractions because normal-foot
external half-triangles and consistent mark-local fractions still identify
external cut-angle pairs across thin/thick contexts. A new construction
must change that shared pair mechanism (for example source-context-
dependent cuts), the normal-foot rule, the global single-H requirement,
or the source incidence/arrow geometry. Merely varying the six mark-local
fractions or thick chord parameters cannot evade the proved angle gate.
Angle infeasibility closes precisely this construction component, not all
convex pentagon/hexagon constructions. Fresh independent review is pending.
