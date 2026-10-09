# Conditional Walton--Whittaker vertex-rank reconnaissance

**Status:** Certified exact falsification of the natural tile/mirror compiler
described below, with recorded hostile reviews of the vertex transcription
and state-assignment extension. The certificates remain exact finite evidence;
independent re-review of the repaired or extended argument is pending.
This does not exhaust alternative compilers.
See [vertex review](../reviews/walton-vertex-rank-review.md) and
[state-assignment review](../reviews/walton-state-assignment-review.md).

## Question and domain

The compiler attaches the source base decoration state to geometric type A
and its vertically mirrored decoration state to geometric type B, relabelled
into the same physical side slots.  (The proposed geometric polygons are not
assumed congruent.)  The R1 word and charge-orientation word are invariant
under this mirror while all charge signs reverse.  Thus a
corner flag records type, one of
six corner slots, and placement reflection parity: 24 flags total.  All
\(24^3=13,824\) cyclic ordered vertex triples are checked against the
transcribed R1 offset and R2 charge rules.

Clockwise side slots are top-right, right-vertical, bottom-right,
bottom-left, left-vertical, top-left.  From the source vector figure and
caption the transcription uses

* R1 crossings near the side's traversal start:
  `(1,1,0,1,0,0)`;
* base signs: `(+,+,+,-,-,-)`;
* base charge orientations:
  `(CCW,both,CW,CCW,both,CW)`.

At a vertex the code converts near-start to **near the common physical
endpoint** before comparing the two sides.  This accounts for the reversal
of polygon boundary traversal along a shared edge.  Reflection swaps the
left/right boundary rays and CW/CCW.

The enumeration finds 1,056 legal ordered triples and 98
distinct angle-incidence rows.  Adding the two per-hexagon angle-sum rows
gives rank 12 in the twelve angle deviations from \(2\pi/3\).  Therefore,
under this transcription, requiring every source-legal vertex triple forces
all twelve angles to equal \(2\pi/3\); angles have no remaining freedom to
exclude unwanted triples.  The 240 allowed oriented edge-flag pairs also
force all twelve side slots into one length-equality class.  That equality
class admits 336 oriented flag contacts forbidden by the source rule.
Moreover, equiangular equilateral hexagons are regular and the two proposed
shapes are congruent periodic monohedral tiles.  Hence this natural compiler
is falsified.

## Replay and certificate

```text
conda run --no-capture-output -n arisearch python3 research/searches/verify.py
```

The search and verifier use exact integer/rational arithmetic.  The retained
certificate contains a rank-12 basis.  The verifier independently
reconstructs the local language, checks the basis rows belong to it, and
checks their rational rank.

The arrays were checked directly against Figure 1 and its caption in Walton
and Whittaker, *An aperiodic tile with edge-to-edge orientational matching
rules*, J. Inst. Math. Jussieu 22 (2023), 1727--1755,
DOI `10.1017/S1474748021000517` (also arXiv:1907.10139v2).  Rule R2 is applied
at a shared edge exactly as stated there.

## Scope and remaining obligations

1. A finite family of alternative assignments has now been exhausted: assign
   each of the twelve rotation/reflection source states to one of the two
   geometric types, retain every compatible source-legal trivalent vertex,
   and use either alternating source-corner pattern.  The replayable search
   [walton_state_assignment_rank.py](walton_state_assignment_rank.py) checks all (2^{12}-2=4094)
   nonconstant assignments.  Of these, 4090 again have angle rank 12.  The
   four exceptional masks 63, 1386, 2709, and 4032 have rank 11, all with the
   same deviation direction

   \[
   (0,-1,0,0,0,1;\ 0,-1,0,0,0,1).
   \]

   Every exceptional language nevertheless forces all twelve side slots to
   one length class.  An equilateral hexagon with angles
   ((120^\circ,120^\circ-t,120^\circ,120^\circ,120^\circ,
   120^\circ+t)) closes only for (t=0): if
   (z=e^{i\pi/3}), the edge-vector sum is
   ((1+z^5)(1-e^{it})).  Convexity puts (t) strictly between
   (-\pi/3) and \(\pi/3\), so closure forces (t=0).  Thus this entire
   assignment family also collapses to the regular hexagon.  The certificate
   is [walton_state_assignment_rank_certificate.json](../certificates/walton_state_assignment_rank_certificate.json).
2. The certificate kills both angle and length discrimination only for the
   requirement that **all** locally legal source contacts/triples be retained.
   A nonempty aperiodic sublanguage might use fewer local configurations.

These assignment masks describe a deliberately generous algebraic relaxation:
an assignment does not by itself explain how bare geometry suppresses the other
placement states.  Since even that relaxation collapses, it is a valid no-go
for this finite compiler family, not a positive construction.

Accordingly these exact falsifications redirect the Walton route but do not
close the general two-obtuse-hexagon mechanism.  A strict sublanguage not
obtained by a state-to-type assignment, or a different matching-rule source,
remains possible.

## Relative relabeling exhaustion

A separate exact search, [walton_relative_relabeling_rank.py](walton_relative_relabeling_rank.py), removes another
choice hidden in the natural compiler.  Type A carries the source decoration
in the reference order; type B independently uses any of six cyclic shifts,
either chirality, and either global charge sign.  These are all 24 relative
dihedral/charge relabelings (a common relabeling is immaterial).  For every
choice the full 24-flag enumeration has exactly 1,056 legal ordered triples,
angle rank 12, and one forced side-length class containing all twelve slots.
Thus changing the relative phase, handedness, or global charge of the two
compiled words does not evade the regular-hexagon collapse.  The exact JSON
certificate is [walton_relative_relabeling_rank_certificate.json](../certificates/walton_relative_relabeling_rank_certificate.json).
The separately implemented
[verify_walton_relative_relabeling.py](../reviews/verify_walton_relative_relabeling.py) reconstructs all 24 languages, checks
their rational ranks and union-find length classes, and compares every count
with the retained certificate.
