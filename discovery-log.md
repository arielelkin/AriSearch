# Current research state for two convex tiles

**Problem status: unresolved.** No exact aperiodic pair or complete unrestricted
impossibility theorem meets [the acceptance criteria](research-problem.md).
**Checkpoint:2026-10-15 12:31 UTC. Main objective unresolved. Reviewed: arbitrary-partner six-distinct hexagon periodic escape; ALL hexagon pairs in which EACH member has at least five distinct numerical side lengths admit a doubly periodic escape; unrestricted Y-family untileability; full arbitrary-context-cut receiving-hexagon obstruction with mark-local donors/splits. Arbitrary physical splits are also excluded on the mark-local-donor topology; construction must change mechanism.**
The unique-B-star and complete complementary two-angle hexagon families
admit periodic escapes whenever tileable. The complementary three-angle
result covers distinct, non-120 angles on its stated resonance domain. The original acute/obtuse pentagon native
words are untileable at every metric; the reordered words have an exact
three-equality tileability criterion and a four-tile periodic carrier.
These are restricted family results, not a global impossibility theorem.

**Research frontier, updated 2026-10-15:** the unrestricted objective remains unresolved;
no construction meets all acceptance criteria. Individual branch results are checkpoints. Source-only or local
objects below are not aperiodic pairs. Historical incremental notes are
[archived](research/searches/discovery-log-2026-10-13-working-history.md).

**Previous Ammann family gate:** the fixed directed-offset Ammann topology is now
classified: all admissible two-shape realizations are the midpoint/common-
height family with periodic omission. [Exact closure and review](research/lemmas/ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md)
are preserved; the two-convex-polygon target remains unresolved.

## Construction: arbitrary cut contexts are now closed (2026-10-15)

**Proved and independently hostile-reviewed VALID:** in the unit Ammann
thin/thick three-sector receiving-quad construction, mark-local donor
triangles and mark-local edge splits cannot produce one congruent receiving
hexagon, even when every proper two-corner truncation cut varies arbitrarily
by context. [Self-contained theorem](research/lemmas/context-dependent-receiving-hexagon-obstruction-2026-10-15.md),
[first audit](research/reviews/context-dependent-receiving-hexagon-hostile-2026-10-15.md),
[second independent audit of the contributed exceptional branch](research/reviews/context-dependent-receiving-hexagon-second-hostile-2026-10-15.md).
Unique36/72 angle vertices identify opposite retained diagonals, forcing
mX=mY=1/2. Generic wedge congruence reconstructs identical donors, whose thin
quad requires m>sqrt(5)/4; the exceptional beta18 branch violates the thick
Y-head convexity bound. No solver or bounded search is a proof dependency.
This supersedes proposals to vary only truncation cuts, including external
cut pairs. It is NOT a theorem about arbitrary pentagon/hexagon pairs.

**Stronger closure, now independently reviewed VALID:** allowing EACH physical
edge split to depend arbitrarily on context also fails, while donor triangles
remain mark-local. [Short standalone proof](research/lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md),
[fresh independent Astra audit](research/reviews/context-dependent-split-receiving-hexagon-astra-hostile-2026-10-15.md).
A thick Y receiver has retained72 at BOTH endpoints, forcing its split and
the common72opposite diagonal to1/2. The thick X tail then has its own forced
midpoint. Its same-X-tail native turn is strictly negative for the entire
0<beta<36 domain, by a positive polynomial identity. The symbolic checker
reconstructs all16endpoint forms, the independent diagonal equations and
the universal rational identity. No adjacency census, metric sampling or
beta18exception is needed. Thin split D36 remains free algebraically but
cannot repair the failing thick quad. The common physical split is inherited
by the adjoining donor and receiver, so neighbor-context splits are covered.

**Construction frontier:** stop all cut/split-only searches on this topology.
A genuine escape must change donor triangles by context, retained opposite
vertex incidence, source geometry or the single receiving-H requirement.
The fresh11:00weighted-Voronoi gate has now been executed and excluded
on its entire stated small weight box, as recorded below. Fresh11:30Astra
completed the hat-cycle construction gates below; no candidate pair survived.

**Falsified auxiliary guess:** the universal thick cross-tail M-angle bound
(90,108) is false for strict precursors. The [exact counterexample](research/counterexamples/offnormal-cross-tail-m-angle-2026-10-15.md)
is retained and is not used in the new proof. Strict precursor fixtures are
controls, not two-shape constructions.

## Day-end handoff complete (user request, 2026-10-15)

The user requested the day-end wrap at 11:56 UTC. All subagents have finished
and stopped writing. Construction and exclusion tracks are closed for this
session: proved results, completed experiments, and unresolved boundaries
are distinguished below. The final [Astra direction note](research/searches/astra-direction-2026-10-15-1200.md)
records concrete restart obligations. No new research search is running.
The research changes and this log are staged for the next commit; no actual
commit or push was created during this handoff.

**Verification: all 423 registered checks passed across the day-end runs.**
The extra frozen 420-check full replay received SIGTERM (exit 143) after
330 passing checks, with no reported mathematical failure. Its remaining
90 checks were then replayed successfully, exit 0. The final theorem's two
certificate producers and independent verifier also passed separately.
The exact union of passing script names equals the current registry:
80 certificate pairs and 343 verifiers. No uninterrupted full 420- or
423-check replay is claimed.

- [Interrupted replay: 330 passes](research/reviews/day-end-420-full-registry-replay-2026-10-15.txt).
- [Successful continuation: 90 passes](research/reviews/day-end-remaining-replay-2026-10-15.txt).
- [Final theorem: three passes](research/reviews/day-end-final-three-replay-2026-10-15.txt).

The earlier [full 400-check replay](research/reviews/shared-five-length-full-registry-replay-2026-10-15.txt)
also passed. Changed Python/JSON files parse, local Markdown links resolve,
and changes are confined to the discovery log and research artifacts.
The main problem remains unresolved. No construction meets the acceptance
criteria, and no unrestricted impossibility theorem is claimed.

## Post-review corrections and authorized publication checkpoint

After the day-end staging, a fresh Astra pre-commit reviewer approved the
work as a research checkpoint, with two documentation corrections. Those
corrections are now applied: the common-five theorem links the completed
unequal-adjacent case, and the six/five separation-two proof records its
completed VALID review and bounded novelty record. The older six/five
frontier paragraph also points to the stronger current conclusions.

The [unified hexagon statement and proof map](research/lemmas/hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md#unified-statement-and-proof-map)
now states both principal results, their exhaustive branches and review
links. It separates one guaranteed nonzero period from a rank-two lattice;
no assertion of exactly rank one or a second period in every branch is
introduced. The combined necessary condition is d(A)<=5, d(B)<=5, and
min(d(A),d(B))<=4. Pentagon-containing pairs remain unresolved.

The reviewer independently reran the final 11,160-word verifier and checked
exact 423-name coverage in the day-end logs. It found no blocking error in
the principal arguments audited, while recommending external scrutiny and
a broader novelty search before a focused hexagon paper. Publication
worthiness remains provisional, and the project is not claimed close to a
solution. The user subsequently authorized these documentation corrections,
commit, and push. This follow-up changes exposition only; the proof code,
certificates, and previously recorded verification outcomes are unchanged.

## Final hexagon exclusion: each member has at least five numerical lengths

**Independently hostile-reviewed VALID:** unrestricted plane tileability of
any pair of genuine convex hexagons, EACH with at least five distinct
numerical side lengths, implies an admitted DOUBLY periodic tiling by the
same unmarked shapes. Reflections, partial contacts and species omission
remain permitted. [Complete corollary and final theorem](research/lemmas/hexagon-five-unequal-adjacent-periodicity-2026-10-15.md),
[fresh review](research/reviews/hexagon-five-unequal-adjacent-hostile-2026-10-15.md),
[no-author-import verifier](research/reviews/hexagon-five-unequal-adjacent-independent-2026-10-15.py).

The final unequal-palette adjacent branch exhausts11,160raw words. Twelve
residual words give three ordered classes and exactly five actual-support
cases: three have positive four-face tori, two have connected certain-edge
corona propagation. Independent reconstruction checks the full22,680gluing
domain, both retained witnesses and all12augmented rational identities.
No solver infeasibility or bounded negative torus search proves this result.

Together with the arbitrary-partner six-distinct theorem, any hypothetical
aperiodic hexagon pair has no six-distinct member and at least one member
with at most four numerical side lengths. Pentagon-containing pairs and
this remaining hexagon region are unresolved. Novelty is limited to the
[bounded primary-source search record](research/literature/hexagon-six-five-boundary-2026-10-15.md);
no universal priority claim is made.

## Construction track1130: completed experiments, no surviving candidate

The [fresh direction note](research/searches/astra-direction-2026-10-15-1130.md)
records completed fixed-frame and interior-cycle hat experiments. Two exact
strict convex source partitions exist: seven pieces(3P+4Q)and eight pieces
(5P+3Q). They are precursors ONLY, with no common-P/Q congruence. Exact
support determinants, pairwise separation, oriented boundary-chain
cancellation and area checks passed; retained outputs are linked in the note.
All EIGHT specifically named necessary-angle domains returned Z3UNSAT within
60000ms caps. Their cyclic/reflected correspondences, source vertex budgets,
T180budgets and interior360budgets are explicit. These are UNREVIEWED finite
solver evidence, not certified construction-impossibility theorems. Their
metric and decoder gates were NOT launched. The linear deformation diagnostic
is also exact but unreviewed and limited to its fixed frames/correspondences.

The original six-native-spoke5P+2Qring has an author elementary angle/arm
obstruction for b!=1; b1 inherits a periodic source escape. That argument is
retained in the note and not promoted to a fresh-reviewed stable theorem.
All task processes finished. No viable new two-shape point exists. Restart
only with a changed source corner-budget/cross-source incidence and an
EXACT angle-feasible two-class complex; do not replay named failed variants.

## ALL common-five-length hexagon pairs now excluded

**Proved, independently hostile-reviewed VALID, exactly certified:** two
genuine convex hexagons having the SAME five numerical side lengths admit
a doubly periodic escape whenever tileable, for EVERY location of each
doubled pair. [Complete adjacent-repeat proof and combined corollary](research/lemmas/hexagon-common-five-adjacent-periodicity-2026-10-15.md),
[fresh whole-proof review](research/reviews/hexagon-common-five-adjacent-hostile-2026-10-15.md).
The nonadjacent cases were reviewed earlier; new adjacent cases permit
repeated ray lengths and repeated native corner indices. Original tilings
still allow arbitrary rotations, reflections, partial contacts and omissions.

New complete360-word native arm-state gate: simultaneous side slots and
opposite-end corner multisets are retained. The12hard words form4classes
with41possible ACTUAL star sets. Twenty-five have positive four-face torus
witnesses certified by100exact rational row identities. Eight force all
angles120; four exact length-closure equations then force allfive lengths
equal, contradicting the numerical hypotheses. Two small pure-loop supports
contradict an even-six-cycle neighbor parity. Two all-AAB/ABB supports have
AB-parity frame propagation. Three other supports admit finite native
coronas with connected CERTAIN transition graphs (two require bypassing
one uncertain AA/BB edge type via the forced third tile). The last support
has an opposite-repeat pure Bstar and explicit monohedral two-face torus.

Fresh independent checks reconstruct all360initial/fixed microstate atlases,
all41supports,12explicit word maps, seven actual positive gluings, all100+96
weighted angle rows, four closure identities, every corona and both uncertain
edge bypasses. Finite state counts alone are NOT used as periodicity proof.
All finite-to-global steps are stated in the complete proof and survived
whole-claim hostile review. This is a substantial family theorem, not the
original unrestricted result; novelty is only relative to the bounded
[documented primary-source search](research/literature/hexagon-six-five-boundary-2026-10-15.md).

**Remaining hexagon frontier:** at least one member has at most four
distinct numerical lengths, and neither member has six. The
one-six-distinct theorem already covers any partner. No global two-hexagon
or unrestricted two-polygon impossibility is claimed.

## New power-cell construction: exact small-box family excluded

**Independently hostile-reviewed VALID:** take vertex-mean sites of the three
reviewed Ammann polygons at J=1/2+(4/5)w, with type weights(0,a,b). Throughout
|a|,|b|<=rho²/2, where rho is the minimum prototype site-to-side distance,
three actual power cells have7,6,5genuine corners. Hence at least THREE
congruence classes remain. [Stable complete proof](research/lemmas/weighted-ammann-power-small-box-obstruction-2026-10-15.md),
[independent review](research/reviews/weighted-ammann-power-hostile-2026-10-15.md).
The finite geometry checker reconstructs650source faces and checks affine
vertices at all4closed-box corners, all competitor inequalities, positive
edge projections, persistent cocircularity, exact cell-radius containment
and a certified source-boundary margin. No generic trivalence assumption.

The first review found a missing finite-to-global bridge: knowing that the
GLOBAL cell lies in a bounded disk did not bound the finite candidate.
Repaired by checking every affine candidate vertex has norm<=C at all4box
corners, then using convexity. The independent checker confirmed the repair.
A137decorated-rhomb witness patch embeds exactly in the ninth subdivision of
ONE red Robinson half. Every legal source contains this patch: compose ten
levels using the reviewed unique-composition theorem, then take the red
child present in EITHER parent type. Thus no centered-sun nesting or external
minimality theorem is assumed. Root separately checked this hierarchy use.

This seed is CLOSED on the stated fixed source metric/sites/weight box.
Do not add context weights or blindly enlarge the box as a continuation.
The unrestricted two-shape target remains open; no candidate pair is supplied.
Fresh11:30Astra is developing a genuinely changed positive object/gate.

## Complete five-length nonadjacent-repeat exclusion, unequal palettes included

**Proved, independently hostile-reviewed VALID, and exactly certified:**
if EACH of two genuine convex hexagons has exactly five distinct numerical
side lengths, and BOTH doubled side pairs are nonadjacent, tileability
implies a doubly periodic escape, regardless of how many lengths the shapes
share. [Unequal-palette proof and combined corollary](research/lemmas/hexagon-five-noncommon-nonadjacent-periodicity-2026-10-15.md),
[fresh whole-proof review](research/reviews/hexagon-five-noncommon-hostile-2026-10-15.md).
This strictly extends the common-five theorem below. Original contacts,
reflections and single-species omissions remain unrestricted.

New finite domain14880raw unequal-palette words;20hard words reduce by
explicit global color/native dihedral maps to6classes and22representative
actual supports. Three classes are intrinsically deterministic; one uses
the reviewed private-repeat theorem with its six DISTINCT numerical union
values intact. Two genuinely new classes have10supports, all covered by
five explicit positive four-face torus gluings and40exact augmented-row
identities. The no-import independent verifier exhausted30240positive
quotient candidates, rebuilt every source word/support/map, checked all
positive links/rows, and reran the private-repeat verifier. No formal-color
collision extension of the old private-repeat theorem is claimed.

**Next structural frontier:** at least one member has at most four numerical
lengths; neither may have six. The later adjacent theorem closes the last
unequal-five case.
The common-five adjacent gate once marked unreviewed is now fully closed
by the stronger theorem above. No whole two-hexagon impossibility follows.

## Complete common-five nonadjacent-repeat exclusion (2026-10-15)

**Adversarially reviewed VALID, with exact independently reconstructed
certificates:** if two genuine convex hexagons share exactly five numerical
side lengths and BOTH doubled side pairs are nonadjacent, tileability implies
a doubly periodic escape. Doubled values may agree or differ. This combines
both separation2, mixed2/3, and the new
[both-opposite3/3 theorem](research/lemmas/hexagon-both-opposite-repeat-periodicity-2026-10-15.md).
The stronger formal-source statement also permits physical coincidences
between different auxiliary colors. [Fresh whole-proof audit](research/reviews/hexagon-both-opposite-repeat-hostile-2026-10-15.md).

Both-opposite gate:120raw partner words; actual pure stars immediately give
an explicit monohedral two-face torus. Without pure stars:80no endpoint
cover,24six-color actual-contact escapes,16words in4explicit orbits. Their
226actual supports yield221positive torus escapes through884exact rational
identities; five remaining supports force indexed-frame periodicity. Four
of those require an explicit alternating-side parity on the double-occurring
species. The AB-only adjacency graph is connected by bypassing AAedges at
the third Btile, so finite-state frame propagation is global. The independent
no-import verifier checks all3*68040positive quotient domains and every
actual endpoint assignment. No larger quotient or bounded negative search.

**Remaining scope:** common-five pairs with an adjacent doubled pair,
noncommon five-value sets, lower multiplicities, pentagon-containing pairs
and all other original targets. This is not full two-hexagon impossibility.
Fresh bounded primary-literature searches are appended to the
[novelty boundary](research/literature/hexagon-six-five-boundary-2026-10-15.md);
no equivalent classification was located in that documented scope, without
claiming universal priority.

## Common five lengths: mixed repeat separations now excluded (2026-10-15)

**Adversarially reviewed VALID and exactly certified:** for two genuine
hexagons with the same five numerical side lengths, if the repeated slots
have separation2in one and3in the other, every tileable pair has a doubly
periodic escape. [Complete proof](research/lemmas/hexagon-mixed-separation-repeat-periodicity-2026-10-15.md),
[fresh independent review](research/reviews/hexagon-mixed-separation-repeat-hostile-2026-10-15.md).
All120raw partner words:96lack native endpoint cover;16split one species
into6actual seam-component colors;8form ONE explicit indexed/color orbit.
The representative has30actual-support possibilities:28imply a retained
four-face torus through112exact weighted row identities; one exact support
partitions all12native corners and forces indexed frames; one adds a
B-only opposite-repeat star and gives an explicit monohedral two-face torus.
The no-import independent verifier reconstructed all48600four-face gluings,
all4096source subsets and every row/endpoint map. No larger quotient search
or bounded negative search is used. This extends the reviewed both-sep2
class; adjacent repeats and other side-length sets remain; the later both-opposite
result above supersedes that original frontier.

## Major structural theorem: one distinct-sided hexagon is excluded (2026-10-15)

**Proved and independently hostile-reviewed VALID:** if ONE member of a
pair of genuine convex hexagons has six pairwise distinct native side
lengths, every tileable pair admits an allowed tiling with a nonzero
translation, for ARBITRARY metrics and side multiplicities of the other
hexagon. Reflections and partial contacts remain allowed in the hypothesis.
[Complete synthesis](research/lemmas/hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md).
[Final synthesis and double-pair audit](research/reviews/hexagon-six-four-double-pair-hostile-2026-10-15.md).
This is a substantial new family theorem relative to the documented
literature boundary. It is NOT the original unrestricted two-polygon result.

The exhaustive branches are:

- partner has at least five distinct lengths: the three-case6/5theorem below;
- at most three shared numerical lengths: the new
  [three-sharing theorem](research/lemmas/hexagon-six-distinct-three-shared-periodicity-2026-10-15.md),
  developed by the09:00Astra adviser. AAB corona constraints leave only two
  B words. A connected graph of forced private-AA contacts propagates
  whole-tiling symmetries. [Fresh VALID review](research/reviews/hexagon-private-a-three-shared-hostile-2026-10-15.md);
- exactly four partner lengths, all shared, multiplicities(2,2,1,1):
  [full double-pair theorem](research/lemmas/hexagon-six-four-double-pair-periodicity-2026-10-15.md).
  Its narrow deterministic stdlib certificate exhausts2160linear/192cyclic
  words and93closed supports:71direct torus rings plus22rings certified
  by88exact rational row identities. Fresh independently reconstructed
  port-cycle enumeration and actual torus gluings PASSED;
- exactly four partner lengths, all shared, multiplicities(3,1,1,1):
  [periodic private-AA chains and strip fillings](research/lemmas/periodic-private-aa-chain-escape-2026-10-15.md).
  Forced half-turn chains cannot cross, so all have one common period.
  Unavoidability bounds the intervening bands; bounded full-side paths
  derive finite exact placements, giving finite-state periodic B fillings
  with a synchronized common period. [Fresh VALID review](research/reviews/private-aa-chain-hostile-2026-10-15.md).

The synthesis needs only existence of ONE nonzero translation, not two
independent periods; it does not silently invoke a general partial-contact
rank-one-to-rank-two upgrade. The chain proof is mathematical and uses no
bounded negative search. The double-pair proof has no solver trust: its
standalone producer and narrow JSON retain every actual support and witness.
Historical B-four exploratory solver examples remain separate from that
proof certificate.

**New frontier:** any hypothetical aperiodic two-hexagon pair must have an
internally repeated side length in BOTH members. All surviving pentagon
pairs remain outside this theorem. No whole two-hexagon or unrestricted
impossibility claim follows. Do not restart searches with a distinct-sided
hexagon by changing its partner metrics or increasing quotient size.

**Current verification:** all 80 certificate pairs and 343 verifiers
(423 checks) passed across the three day-end runs documented above. The
interrupted 330-pass run plus its successful 90-check continuation cover
the frozen 420-check checkpoint; the final three additions also passed.
No uninterrupted full 420- or 423-check replay is claimed. The earlier
[full 400-check replay](research/reviews/shared-five-length-full-registry-replay-2026-10-15.txt)
passed. One earlier producer emitted summary stdout rather than retained
JSON; that interface was repaired and its exact registered replay passed.
No mathematical certificate discrepancy remained.

**Final scheduled adviser12:00UTC:** fresh Astra completed the last
unequal-palette adjacent-repeat hostile review: VALID, including the
each-at-least-five doubly periodic corollary. Its no-import independent
verifier PASSED. The optional skew-metric identity also passed review.
Final [next-session advice](research/searches/astra-direction-2026-10-15-1200.md) is retained; all advisers have finished and stopped writing. No new experiments.
Earlier advisers at09:00,09:30,10:00,10:30,11:00and11:30completed their work.
No further refresh is due after the user-requested day-end wrap unless resumed.

**Earlier reviewed adviser mathematics:** the [fixed-angle contact-deformation lemma](research/lemmas/hexagon-fixed-angle-contact-deformation-2026-10-15.md)
has passed [fresh VALID review](research/reviews/hexagon-fixed-angle-contact-deformation-hostile-2026-10-15.md).
It transfers one perturbed A6/B5 full-side
torus back to the original polygons; failure is an exact closure-matrix
row-space condition. The separate [formal-color A6/B>=5 extension](research/lemmas/hexagon-six-five-formal-color-periodic-escape-2026-10-15.md)
has passed [fresh VALID review](research/reviews/hexagon-six-five-formal-color-hostile-2026-10-15.md),
including indexed propagation even for physically symmetric polygons.
Thus an aperiodic A5/B5 pair must join each shape's repeated native slots
by seam types ACTUALLY occurring in every indexed defect-free tiling.
The [arbitrary-partner formal-color extension](research/lemmas/hexagon-six-colors-arbitrary-partner-2026-10-15.md)
has passed [fresh VALID review](research/reviews/hexagon-six-colors-arbitrary-partner-hostile-2026-10-15.md).
Thus for ANY hypothetical aperiodic two-hexagon pair, every indexed
defect-free tiling must connect two distinct native slots of EACH shape
by actually occurring seam types. This strengthens numerical repetition
to an actual-contact necessity even with an arbitrary partner.

**Construction gate closed:** the mark-local normal-foot equal-radius
thick-cap split component has passed a fresh independent audit:
[sharp obstruction](research/searches/thick-cap-split-congruence-gate-2026-10-15.md),
[VALID review](research/reviews/thick-cap-split-congruence-hostile-2026-10-15.md).
Thin whole caps make every receiving hexagon cyclic. Their alternating
angle identity forces all four source receiving endpoint angles greater
than pi/2, while mark-local base-angle cancellation makes their sum2pi.
This excludes all admissible chord parameters and reflections in the stated
component, before child congruence is used. Later work closed unequal cuts,
off-normal mark-local cuts, arbitrary context cuts AND arbitrary physical
splits while donor triangles remain mark-local; use the stronger current
[arbitrary-split theorem](research/lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md).

## General fixed-angle deformation obstruction (2026-10-15)

**Freshly reviewed VALID after repair:**
[general theorem](research/lemmas/hexagon-contact-deformation-general-2026-10-15.md),
[independent review](research/reviews/hexagon-contact-deformation-general-hostile-2026-10-15.md).
For any indexed defect-free tiling define E by actual native seams and
M:R^E->R^4 by the two fixed-direction polygon closures. If EACH repeated
A-slot difference is outside row(M), one generic kernel vector separates
ALL repeats; the changed A has six distinct lengths. One full-side
periodic changed witness transfers back even when only rank-one periodic:
restore the same infinite plane complex, develop its complete flat metric,
and conjugate the indexed translation to a fixed-point-free orientation-
preserving isometry. No finite quotient or bounded period is needed.

The strip proof is strengthened by finite-window whole-native-edge matching
conditions witnessed by the original filling. A nonprivate A edge belongs
entirely to one open separator band, so independent fills preserve them.
The monohedral dependency was repaired explicitly: source-mono cases escape
in ORIGINAL geometry; mixed changed B<=3 uses the direct corona proof;
changed B>=4 mono uses only H1/H2, whose tiny full-side tori have a new
independent checker. No H3 full-side assumption is used. Failure of
simultaneous separation means AT LEAST ONE repeated-pair functional lies
in row(M), not that all repeated pairs are rigid. This remains only a
necessary obstruction to aperiodicity; no candidate or global resolution.

**Strategic supersession:** the now-reviewed arbitrary-partner formal-color
source theorem dominates this exclusion criterion WITHIN HEXAGONS. Any E-
merged A native pair has identically zero difference functional, so a
simultaneous separating kernel direction requires six different E-colors
on A; the color theorem already gives periodic escape without any rank
condition. Do not continue closure-kernel computations on this domain as
if they bypassed connected repeated slots. The complete-flat-plane/rank-one
transfer proof remains a stable reusable geometric lemma, and the exact
rank condition remains mathematically valid, but this route is superseded
as a stronger hexagon exclusion mechanism.

## Construction sequence: normal-foot and off-normal components closed

**Normal-foot plus mark-local cuts: freshly reviewed VALID obstruction.**
[Short elementary proof](research/searches/unequal-arrow-cut-angle-obstruction-2026-10-15.md),
[fresh audit](research/reviews/unequal-arrow-cut-angle-hostile-2026-10-15.md).
The common H must contain a,b,72,144 with a+b72. If a!=b these four
angles total288, and two further angles<180 cannot make720. Thus a=b36.
The common H then has unique36/72 and four angles>108. Thin and thick
X-tail contexts share an ordered cut-angle pair(s,t), with180<s+t<270.
The three possible intervening-arc lengths0/4,1/3,2/2 in the cyclic H word
all contradict its720angle total. This rules out ALL admissible unequal
arrow-indexed mark-local fractions, not merely equal radii; thick chord
choices and P congruence are irrelevant. The478exact weighted-row
contradictions are supplementary independently checked evidence. Do not
reopen by changing those fractions or chords.

**Genuine changed hypothesis: M no longer the donor apex's normal foot.**
The full16context necessary H-angle gate has an exact rational SAT witness:
H=(36,156,144,156,72,156), Xt=Yt6,Xh=Yh42, donor apex halves120/12.
But its actual unique donor-triangle/split geometry FAILS. Exact cyclotomic
reconstruction gives8nonconvex assembled receiving quads; the other8strict
quads fail required angles, including an actual M-angle108instead of156.
[Precise one-fixture failure](research/searches/offnormal-one-fixture-geometry-2026-10-15.md).
[Fresh independent reconstruction and VALID review](research/reviews/offnormal-one-fixture-hostile-2026-10-15.md)
have passed for this fixture only. This kills ONLY this relaxed-angle witness, not the whole off-
normal component. No two-prototype geometric candidate exists.

**Stronger component CLOSED, freshly reviewed VALID:**
[off-normal mark-local truncation obstruction](research/lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md),
[full geometric audit](research/reviews/offnormal-mark-local-truncation-hostile-2026-10-15.md),
[second audit](research/reviews/offnormal-mark-local-hostile-2026-10-15.md).
Strict precursor convexity ALONE has an exact positive fixture with both
tail half-angles>108, so the attempted convexity-only obstruction is FALSE;
that witness is preserved in the new master-determinant artifact. The
successful combined argument uses actual COMMON-H METRIC CONGRUENCE:
capacity gives common tail beta and Xheadbeta36; a cyclic common cut-pair
has sum>=288, while same-mark head geometry gives Xheadhalf>18 and Yheadhalf>54.
Hence beta<9. Unique36vertex and its opposite retainedM fixmX=mY; a
base reflection preserves the thin-tail tangent wedge only atbeta18,
so the congruence is identity. Two external cut-edge lines reconstruct the
same donor apex for both marks. This forces Yheadhalf<36, contradicting>54.
The proof permits independent off-normal splits and arbitrary unequal
mark-local external cuts. NO remaining mark-local parameter search is
justified. Later arbitrary-cut/arbitrary-split proofs also close the proposed
cut-context escape. A new construction must change donor geometry by context,
source geometry/incidences, the acute-projection domain, or the single
receiving-H requirement. All angle/precursorSAT fixtures
remain counterexamples to weaker reductions, not candidates.

## All common-five-length separation-two pairs excluded (reviewed)

**Freshly reviewed VALID:** if two genuine convex hexagons have the SAME
set of five distinct numerical lengths and each repeats its doubled value
at separation two, EVERY tileable pair has a rank-two periodic escape,
REGARDLESS of whether the doubled values agree. The same-valued branch is
[the seven-orbit classification](research/lemmas/hexagon-shared-repeat-separation-two-periodicity-2026-10-15.md).
The new different-valued branch is
[the actual-seam recoloring theorem](research/lemmas/hexagon-different-repeat-separation-two-periodicity-2026-10-15.md),
with [fresh complete independent review](research/reviews/hexagon-different-repeat-separation-two-hostile-2026-10-15.md).
Both have indexed formal-source variants allowing different colors to
have the same physical length; no final matching rule is imposed.

The different-valued exact gate is96raw/48reflection-normalized Bwords:
40empty greatest endpoint-fixedpoint atlases,8covering full fixedpoints,
36closed actual-corner covers. In EACH full fixedpoint atlas, one species'
repeated native slots remain disconnected in the graph of all possible
native seams. Actual seam graphs are subgraphs; their component partitions
REFINE that fixedpoint partition. Thus one species gains six actual-seam
colors, and the reviewed six-color/ANYpartner source theorem gives periodic
escape. No new torus or numerical metric search was needed. All48words,
all8graphs including every color and loop, and all36covers have been
independently reconstructed. The combined class remains a restricted
hexagon slice; five-length sets that differ, other repeat positions,
heavier repetitions and pentagon-containing pairs are not resolved.

## Same doubled-value separation-two classification (reviewed)

Declared bounded extension of the proved torus method: both hexagons use
exactly the same five numerical lengths, the same doubled value r, and
both repeated slots have cyclic separation two. FixA=(r,x,r,y,z,t).
Independent canonicalization corrected the preliminary root orbit count:
24normalized B permutations/independent B reflection gives12words; also
quotienting A reflection with y/t relabeling gives SEVENorbits, not six.
Two pendant orbits have a missing triangle; the old12-star family is dead;
three new representatives are dead by0stars,8->0stars,12->1->0stars;
the only possibly tileable orbit is the reviewed periodic changed word.
[Complete finite synthesis](research/lemmas/hexagon-shared-repeat-separation-two-periodicity-2026-10-15.md)
and [fresh canonical/pruning review](research/reviews/hexagon-shared-repeat-separation-two-hostile-2026-10-15.md)
are now VALID, including the formal-color source variant. No new
torus size or metric enumeration is involved.

## Complete changed-word shared-repeat family theorem (2026-10-15)

**Freshly hostile-reviewed VALID, including a noninjective formal-color
source variant:** the family A=(r,x,r,y,z,t),B=(r,z,r,y,x,t) with five
pairwise distinct numerical lengths has a doubly periodic escape whenever
tileable, even from unrestricted reflected/partial-contact tilings.
[Self-contained theorem](research/lemmas/hexagon-shared-repeat-changed-family-periodicity-2026-10-15.md),
[full independent audit](research/reviews/hexagon-changed-word-connected-support-hostile-2026-10-15.md).
The source version permits distinct colors with equal physical lengths;
indexed source frames handle all physical symmetries.

Exact complete proof domain:16actual native stars, all65536supportsubsets,
171corner-covering endpoint-closed supports. The fixed positive-witness
atlas has68040four-face side pairings,12actual trivalent tori,6distinct
angle supports. Of ALL171source supports,169have chosen explicit torus
witnesses with676retained Fraction-weighted identities. Exactly2remaining
ACTUAL supports partition all12corners into4stars, forcing complete native
neighbor isometries and hence rank-two periodicity. The comparison uses
all171supports, not merely the8minimal supports. No quotient-size growth,
finite-model conjecture or bounded-negative inference is used.

This closes the changed word completely as an aperiodicity candidate.
It does not classify arbitrary repeated-side hexagons. Optional skew-angle
closure identity from the10:00adviser is NOT a dependency. The earlier
144connected-r/12minimal/11angle-flat/7maximal records remain optional
source-side detail in the same certificate, superseded by the171case proof.

## Shared-repeat gate: completed and superseded by full common-five theorem

The original word A=(r,x,r,y,z,t),B=(r,y,r,z,x,t) is untileable by its native
far-end obstruction; [proof](research/lemmas/hexagon-shared-repeat-single-family-2026-10-15.md)
and [independent review](research/reviews/hexagon-shared-repeat-single-family-hostile-2026-10-15.md).
The changed word B=(r,z,r,y,x,t) is closed by the reviewed171-support theorem,
positive four-face witnesses and two deterministic partitions. All common-
five word positions are now closed by the stronger theorem at the top.
No seam-tree refinement, angle-flat polishing or larger quotient search is
pending. Optional skew-angle closure identity is not a proof dependency;
its [independent review](research/reviews/hexagon-changed-word-skew-flat-metric-hostile-2026-10-15.md) is VALID for the standalone identity, with named flat provenance separate and unused.

## Six-distinct/five-distinct hexagon periodic escape (2026-10-15)

**New substantial reviewed structural theorem:** if one genuine convex hexagon
has six distinct native side lengths and the other has at least five, then
any admitted plane tiling implies an admitted doubly periodic tiling, including
reflections and arbitrary partial contacts in the hypothesis.
[Combined theorem and exact dependency proof](research/lemmas/hexagon-six-five-general-periodic-escape-2026-10-15.md).
This is a partial exclusion, not an unrestricted impossibility theorem.

The new exactly-five branch exhausts all positions of its repeated length:

- [Separation two](research/lemmas/hexagon-six-five-separation-two-periodicity-2026-10-15.md):
  3780 normalized numerical words, eight surviving orbits, sixteen
  endpoint-closed actual-corner supports; fourteen contain a four-face torus
  ring and two give unique intrinsic relative-neighbor isometries.
- [Opposite repeats](research/lemmas/hexagon-six-five-opposite-repeat-periodicity-2026-10-15.md):
  1890 normalized words, eight mixed orbits, twelve closed supports; ten
  contain rings, two are deterministic. Pure-B stars separately give an
  explicit two-B-face flat torus by complementary angle sums.
- [Adjacent repeats](research/lemmas/hexagon-six-five-adjacent-periodicity-2026-10-15.md):
  3780 words, twelve orbits, eleven supports, all with four-face rings.
  Repeated ray lengths and repeated native corner indices are retained;
  all three far-end checks must use one simultaneous native-arm microstate.

All three full proofs have fresh VALID hostile reviews under
`research/reviews/hexagon-six-five-*2026-10-15.md`. Independent stdlib
verifiers import no producer, reconstruct the complete numerical domains,
check actual native corner slots, and independently find whole-side torus
pairings. The adjacent verifier exhausts even all original atlas subsets,
independently confirming pruning loses no possible actual support. The
combined six registered checks PASSED with no retained certificate writes.
[Documented novelty boundary](research/literature/hexagon-six-five-boundary-2026-10-15.md)
found no equivalent theorem within the stated sources/queries. No universal
priority claim is made.

**Superseding status:** the later one-six-distinct/arbitrary-partner theorem
above closes every partner multiplicity. The current five-length results
also close EVERY pair in which each member has at least five distinct
numerical lengths; the final unequal-adjacent extension passed fresh review. Do not reopen
old6/5families by changing metrics or increasing quotient size.

**Historical adviser launch record:** the08:30invocation never initialized;
the fresh09:00retry ran successfully. All subsequent half-hour advisers
completed through11:30; fresh12:00is the final wrap-up reviewer. No result
is attributed to the stalled08:30invocation.

## Unrestricted Y-pair closure and parameter family (2026-10-15)

**New reviewed partial theorem:** the retained exact Y pentagons admit **no
plane tiling at all**, allowing all isometries and arbitrary partial contacts.
[Fixed proof](research/lemmas/pentagon-y-unrestricted-2026-10-15.md).
G endpoints cannot lie against flat sectors, and length R<2S forces GG full.
A short GC arm along a P RA ray forces a forbidden flat+A farther along that
same ray. Consequently GG matches RA; both RA and AB sides of one actual P
become full; its reviewed full BB mate would need two G endpoints, impossible.
This closes the former unrestricted partial-contact gap without a larger
finite quotient or patch search.

The [self-contained abstract obstruction and parameter theorem](research/lemmas/y-pentagon-parameter-family-2026-10-15.md)
extend this to **every rational t** in
`(5+3sqrt(2))/7 < t < 1+sqrt(2)`, with
`R=(4t-2)/3`, `k=(t+1)/3`,
`P=((0,0),(R,0),(R+1,t),(t,R+1),(0,R))` and
`Q=((t,1),(t-k,1+k),(-t+k,1+k),(-t,1),(0,0))`.
The abstract lemma assumes explicit angle and side cycles,
`0<S<R<L<2S`, `2R!=3S`, `2L!=3S`, and irrational angle coefficient.
Its shortest-side guard proof is reproduced for those hypotheses.
This is a restricted infinite family exclusion, **not** a solution of the
unrestricted two-polygon objective.

[Fresh hostile review](research/reviews/y-unrestricted-and-family-hostile-2026-10-15.md)
is VALID separately for the fixed theorem, abstract obstruction and full
rational interval. The independent checker reconstructs coordinates, strict
convexity, corner cotangents, complete stars and exact interval signs without
producer imports. Both author checkers and the independent checker passed.
[Novelty boundary](research/literature/y-pentagon-family-boundary-2026-10-15.md)
locates no equivalent theorem in the stated sources/queries; priority beyond
that boundary is not claimed. Three read-only Y checks were added to the registry.
A full frozen-checkpoint replay PASSED all62certificate pairs and310
verifiers (372checks), with copied-evidence hash preservation. See
[full log](research/reviews/y-family-full-registry-replay-2026-10-15.txt).
The six subsequently added hexagon checks separately PASSED, so all
current65certificate pairs and313verifiers (378checks) have been checked;
no single fresh all378replay is claimed.

**Closed route/restart restriction:** no more search for tilings of the fixed
Y pair or any pair in this theorem's exact domain. A new construction must
change native metrics/corner correlations or another explicit hypothesis;
no increase in patch or quotient size can repair the contradiction. The
following 2026-10-14 Y discussion is historical and its unrestricted gap is
superseded by this theorem. Current independent construction directions are
changed Q metrics, a new 72/108/126-degree pentagon/144-degree decagon palette,
and fractional partitions with three output sectors at each split.

## Historical autonomous restart (2026-10-15 08:30 UTC)

The user requested execution of `main_prompt.md`, continued research toward a
substantial novel result, and a **fresh Astra direction adviser every 30 minutes**.
First adviser launched at 08:30 UTC; next due 09:00 UTC while research continues.
No success criterion is relaxed. Locked environment verification PASSED.

Mechanisms active at that earlier checkpoint (current status above):

- **Y unrestricted contact propagation:** use the reviewed full-BB-mate theorem
  to classify previously unclassified other native sides and determine actual
  unrestricted existence or untileability. No larger whole-edge quotient.
- **New construction:** alter the fractional source topology or hierarchical
  carrier incidence rather than vary closed offsets/metrics.
- **Global structural constraints:** root examines geometric/angle obstructions
  that apply beyond fixed candidate families; adviser independently selects
  the next research direction. Fresh literature boundary in progress.

New claims require independent hostile review and exact replay before promotion.
Existing paused/closed routes below retain their restart restrictions. No new
candidate or unrestricted theorem is claimed at this restart.

## Y partial contacts and intrinsic forcing: bounded gates (2026-10-14)

The user authorized two Sol tracks and a separate Sol adversary. No excluded
candidate, closed Ammann topology, or larger census was reopened. These
tracks remain distinct; neither has an exact infinite mixed covering.

1. **Y shortest-side gate.** The [exact theorem](research/lemmas/pentagon-y-one-breakpoint-bb-obstruction-2026-10-14.md)
   now proves that every native P BB side has a full equal-length native mate,
   either P BB or Q CG, even in tilings with reflections and unrestricted
   partial contacts. The experiment classified every contact along that
   length-sqrt(2) side: two interior transitions contradict minimum native
   side length; one fails endpoint guards; a longer containing side fails
   the forced far-end corner. A four-tile diagnostic patch has disjoint
   interiors but cannot complete its forced host A vertex. The
   [fresh independent review](research/reviews/pentagon-y-bb-partial-hostile-review-2026-10-14.md)
   is VALID. Stopping condition: complete BB contact classification, with
   no patch expansion. Other sides may still split, so the older whole-edge
   propagation theorem cannot yet exclude unrestricted tilings. Further
   work needs an actual propagation rule on those remaining contacts.
2. **Intrinsic Ammann feature gate.** The [explicit c-edge scheme](research/searches/ammann-c-seam-intrinsic-feature-2026-10-14.md)
   recognizes one boundary edge in each unmarked source pentagon, including
   all ten dihedral labelings. A half-turned P1 shares that full edge with
   P1, with disjoint interiors and endpoint angle sum 216 degrees. This
   disproves the isolated local heterotypic-contact predicate; it does not
   produce a plane tiling or refute the source's full three-shape corona
   proof. The [independent hostile review](research/reviews/ammann-c-seam-feature-hostile-review-2026-10-14.md)
   is VALID for that negative scope. Stopping condition: this local bypass.
   A restart must supply a complete-corona rule for the actual two outputs,
   intrinsic source decoding, and both omission exclusions; a unique edge
   or a visibly chosen source chord is insufficient.

All four new author/reviewer checks pass in the
[targeted replay](research/reviews/y-bb-and-intrinsic-feature-targeted-replay-2026-10-14.txt).
Registry: 62 certificate pairs and 307 verifiers (369 checks).
No fresh full-suite replay was run. The unrestricted problem remains unresolved.
The user's subsequent [independent diff audit](research/reviews/y-bb-intrinsic-diff-readiness-2026-10-14.md)
found no mathematical blocker after repairs: local finiteness is now explicit,
asymmetric side cycles are allowed to distinguish endpoints and diagonal
roles, and superseded recommendations are labeled historical. The c-seam
counterpatch survives those corrections. Commit-readiness replay passed
all four new checks plus the Y source certificate, independent Y source
check, and Ammann forcing re-review (seven checks total).

## Resumed construction mechanisms: interfaces, fractional trees, strips (2026-10-14)

The user explicitly prioritized new mechanisms over larger searches in closed
families and authorized terra/sol orchestration. Three construction agents
worked independently, then cross-reviewed each other; a separate torus
balance derivation received fresh hostile review and correction. No fixed
P5/Q14, excluded mixed-contact words, quadrilateral fan, or stalled census
was resumed. The unrestricted objective remains unresolved.

| Mechanism | Explicit scheme and surviving milestone | Bounded gate, verdict, and changed assumption |
| --- | --- | --- |
| Interface-first Y pentagons | [Exact rational P5/Q5 pair](research/searches/pentagon-y-interface-2026-10-14.md): three children partition a reflection-symmetric six-sided parent. Both monohedral omissions are excluded under unrestricted contacts. [Hostile review](research/reviews/pentagon-y-interface-2026-10-14-hostile-review.md) VALID. | Complete seven native/two flat angle-star domain; whole-side and far-endpoint checks retain multiple possible stars. Intact parent cannot tile because its only legal star has unmatched lengths 4 and 2. Atomic mixed plane existence remains UNPROVED. Restart requires cross-parent seams or another repeatable parent boundary, not more intact parents. |
| Y atomic alternative assembly, full-edge torus | [Reviewed count theorem](research/lemmas/pentagon-y-full-edge-torus-balance-2026-10-14.md): every finite full-native-edge flat torus has p=6w,q=4w. [Fresh hostile review](research/reviews/pentagon-y-full-edge-balance-hostile-2026-10-14.md) VALID after correcting seven angle stars versus five length-compatible stars. | Initial 2P+2Q proposal stopped analytically before pairing enumeration. The later user-authorized 6P+4Q model returned INFEASIBLE and led to the stronger whole-edge propagation theorem below. The count theorem remains valid but its whole-edge restart is superseded. |
| Fractional Ammann bipartite two-node tree | [Exact two-pentagon infinite partition](research/searches/ammann-bipartite-tree-pentagons-2026-10-14.md): opposite triangles and quads join across source edges, with all five genuine corners and both far endpoints verified. [Independent hostile review](research/reviews/ammann-bipartite-tree-pentagons-2026-10-14-hostile-review.md) VALID. | Two exact geometry rows, no contact census. Homogeneous checkerboard rhomb carriers give each pentagon a periodic omission cover, closing the scheme. Global two-shape partition succeeds; universal translation-equivariant source decoding fails. Change the common mark-independent triangle, not its height or patch size. |
| Smaller two-hexagon strip track | [Exact mixed infinite strip covering and conditional theorem](research/lemmas/two-hexagon-repeatable-strip-cycle-2026-10-14.md); [independent hostile review](research/reviews/two-hexagon-strip-cycle-independent-2026-10-14.md) VALID. | Exact rational fixture and boundary periods. Each species also has a periodic omission. Independently reusable strips with finite complete periodic boundary states admit a periodic cycle even with branching and irrational phase drift. Change independent finite-state strip reuse; no universal row recognition or global hexagon classification follows. |

The Y pair is retained only for unrestricted partial-contact possibilities,
not as a plane-tiling candidate with existence established. Its surviving stars abg and rgg prevent an angle-only
unique-Y argument; they are not certified infinite alternatives. Preserve this
interface route independently of the fractional source route and the strip
route.

A second fractional cycle changed the assumption to X/Y-mark-dependent
triangle altitudes, with the same globally compatible tree roles. The
[exact four-case construction and analytic area gate](research/searches/ammann-mark-altitude-gate-2026-10-14.md)
gives genuine pentagons and a compatible infinite partition. Unequal heights
force at least three area values/classes; equal heights return the periodic
omission. This height-only interface is closed. [Independent hostile review](research/reviews/ammann-mark-altitude-independent-2026-10-14.md)
is VALID, with a fresh symbolic-height and eight-pentagon checker. A next scheme must
change lateral offsets or tree/quad boundaries and solve receiving-class
identities first.

The user's subsequent steering explicitly authorized a bounded 6P+4Q
periodic-counterexample experiment. The [fixed CP-SAT model](research/searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.md)
encoded fifty complete native sides, reversed equal-length pairings, exact
corner-slot counts, and reflections modulo intrinsic shape symmetries.
Circular quotient links and face connectivity would have been checked before
accepting a witness; no geometry witness was found. Predeclared stopping was
first valid torus, INFEASIBLE, or cumulative 120-second/100-rejected-pairing cap.
OR-Tools returned **INFEASIBLE in 0.051064536 seconds**, with no branches or
rejections. Its retained JSON is a historical status record, not a formal
solver UNSAT proof certificate. Read-only replay checks its metadata and the
independent mathematical obstruction, without rerunning the solver.

The solver then exposed a new [native-occurrence propagation theorem](research/lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md):
**these P and Q admit no whole-native-edge plane tiling at all**, with
reflections and no finite-quotient assumption. Following Q's GG side forces
both A and then both B corners of one actual P into abg stars, so P's BB
side needs a nonexistent length-squared-2 GG mate. The [fresh hostile review](research/reviews/pentagon-y-no-full-edge-hostile-2026-10-14.md)
is VALID and its independent Sage checker reconstructs native angles, ray
lengths and far endpoints. This supersedes every larger whole-edge quotient
search for these atoms. **Unrestricted partial-contact mixed existence and
universal recognition remain unresolved.** A restart must change contact
subdivision or the actual native endpoint correlations, not the face count.

At the end of the earlier interface-construction cycle, the registry had
**61 certificate pairs and 298 verifiers (359 checks)**. All **twelve new checks (three certificate replays and nine
verifiers) PASSED** in [combined targeted replay](research/reviews/interface-construction-2026-10-14-targeted-replay.txt).
No fresh full 359-check replay was run. Environment dependencies were
unchanged. The [independent integration audit](research/reviews/interface-construction-2026-10-14-integration-review.md) found no mathematical defects; its stale-history and transient negative-replay findings were repaired before the combined replay. The twelve checks include the two fractional cycles, their fresh
independent geometry/area checks, Y geometry and finite balance, the full-edge
propagation theorem, the fixed CP record, and the smaller hexagon strip track.

The user subsequently requested an explicit Astra assessment of further
parallel construction value. The [independent Astra assessment](research/searches/astra-construction-portfolio-assessment-2026-10-14.md)
is complete. It recommends **one new bounded directed-offset Ammann gate
with a separate adversary**, not two or three full construction searches.
Four parameters (a_X,a_Y,h_X,h_Y) measured from actual source-arrow tails
move both donor triangles and receiving quads. First construct all eight
local outputs, solve exact area/congruence/support identities over the 127
two-class partitions, then immediately attack omission and intrinsic chord/
arrow decoding. UNKNOWN, inadmissibility, more than two classes, a periodic
carrier, or absent intrinsic decoder stops that declared cycle. This is a
strategic proposal, not a surviving exact pair or reviewed theorem. No such
new solver or extra fleet was launched during the assessment.

Preserve the incompatible two-parent design proposal H=2P+Q, K=P+2Q with
phi H=2H+K, phi K=H+K: area consistency forces area(P)/area(Q)=3phi+1.
Astra does not recommend coordinate enumeration until a complete planar
incidence template and repeatable boundary rule exist. Generic extra strip
or two-hexagon searches have no new mechanism yet and remain paused; the
general two-hexagon question is still open.

**Historical restart boundary (superseded by the later gate closure below):** completed cycles stopped at exact parent/contact,
periodic-omission, or class-count contradictions. Their important claims
have independent hostile reviews and twelve new read-only checks passed.
The unresolved global obligations are an actual admissible infinite
aperiodic-pair covering and universally valid geometric recognition. At that checkpoint, the
next justified experiment was the directed-offset gate above, with fixed
local topology and an adversary; closed families and larger whole-edge Y
quotients must not be resumed. The subsequent user-authorized directed-offset gate and its exact closure are recorded below; it is no longer a launchable unresolved route.

## Three-plus-one elimination cycle: directed-offset topology closed

The user authorized the next algebraic/geometric step. Two independently
briefed Sol construction agents and one fresh hostile reviewer completed it.
**All four three-plus-one assignments are excluded exactly.** Combined with
the earlier two-plus-two theorem, every admissible two-class realization in
this four-parameter directed-offset/two-node topology is the midpoint/common-
height component, which admits periodic monohedral omission. The scheme is
closed for the aperiodic-pair objective; it is not a proof excluding all
fractional Ammann constructions or arbitrary convex pairs.

[Full three-plus-one proof](research/lemmas/ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md),
[exact invariant replay](research/searches/ammann-directed-offset-residual-invariants-2026-10-14.py),
and [fresh independent hostile review](research/reviews/ammann-directed-offset-residual-hostile-review-2026-10-14.md)
are retained. The independent reviewer reconstructs coordinates without
importing author code. All reflections/cyclic correspondences are covered
by symmetric necessary invariants; no new NLSAT query or timeout increase ran.

For each of the four singleton choices, the other three outputs must share
area, sum of squared boundary-edge lengths, and sum of fourth powers of
boundary-edge lengths. Those six polynomial equations form an exact ideal
over Q(sqrt(5)) after normalizing h_X=t*x,h_Y=t*y. Two branches give the unit
ideal. Singleton T0 gives a_X=1/2, x=(sqrt(5)-1)(y-1/2), and a quadratic
negative throughout 1/2<y<1, the interval forced by donor interior. Singleton
K1 gives a quadratic with negative discriminant. Exact independent Gröbner
computations verify all four results in about eight seconds each. This is a
computer-assisted algebraic proof on the complete fixed continuous parameter
domain, not sampling or absence of a bounded periodic witness.

The geometry agent independently supplied a [unit-chord filter](research/lemmas/ammann-directed-offset-unit-chord-filter-2026-10-14.md)
and [linear-system replay](research/searches/ammann-directed-offset-unit-chord-check-2026-10-14.py).
It excludes the eight chord-preserving cross-source maps; its remaining
thirty-two unit-diagonal alias maps are outside that partial lemma but are
covered by the full symmetric-invariant proof. The fresh hostile reviewer
also checked this filter. No alias enumeration was needed.

Review repairs: strict convex counterclockwise output/source-partition
hypotheses are explicit, so signed shoelace equality is a necessary physical-
area invariant even under reflected congruences. The final claim is that
all two-class realizations are confined to a periodic component, not that
two-class realizations are nonexistent. Read-only checkers assert the exact
ideal conclusions, real-domain contradictions, and all eight linear-map
ranks/solutions; merely printing symbolic output is not treated as a pass.

Finite bounds were four singleton ideals and eight actual linear maps,
within the predeclared forty-map domain and per-operation/cumulative exact
computation caps. The stopping condition is the complete reviewed obstruction.
At the end of that earlier elimination cycle, the registry had **62 certificate pairs and 302 verifiers (364 checks)**.
All three new checks **PASSED** [targeted replay](research/reviews/ammann-directed-offset-residual-targeted-replay-2026-10-14.txt),
with no retained certificates written. No fresh full 364-check replay was run.

**Restart condition:** abandon this fixed topology or one of its actual
interface assumptions before computational restart: the opposite two-donor-
triangle/two-receiver-quad rhomb partition, or the shared mark-directed unit-
base triangle rule. Different offsets, heights, class correspondences,
longer solver time, or larger source patches cannot evade this theorem.
An explicit changed fractional partition must again establish genuine
pentagonal-or-higher outputs, global two-shape compatibility, and then
universal intrinsic decoding. The Y partial-contact and unrestricted
hexagon possibilities remain separately preserved; no closed family is
reopened by this result. The global problem remains unresolved.

## Published checkpoint and two new bounded design cycles

The user authorized commit, push, and the recommended next work. The reviewed
checkpoint was committed as **6b9f087** (51 files) and pushed to
origin/convex-pair. That publication includes the independently reviewed
interface, fractional-tree, strip, and exact directed-offset closure results;
its new registered checks and scope were audited by Astra. No new solver
search was needed for publication.

Two independent Sol designers and a fresh Sol adversary then completed one
explicit design cycle each. The mechanisms were kept separate. **Both first
templates fail exact local gates; neither general mechanism is classified.**

- [Two-parent four-rule incidence template](research/searches/two-parent-wheel-seam-incidence-2026-10-14.md):
  H=2P+Q and K=P+2Q use three-pentagon wheels; phi H uses a three-parent
  wheel and phi K one whole-edge H/K join. All oriented seam pairings and
  far endpoints were specified and independently retraced. The inflated
  boundaries retain at least eighteen/fourteen genuine corners instead of
  nine. Allowing all base endpoint flats does not rescue this whole-genuine-
  edge topology: p_H,p_K>=6, while H similarity requires p_H+p_K<=9 and K
  similarity p_H<=4. [Fresh hostile review](research/reviews/two-parent-wheel-seam-independent-hostile-review-2026-10-14.md)
  confirms the scoped obstruction. A restart must change the macro seam
  topology (for example, several genuine-edge seam segments) or the base
  incidence, with complete new boundary words; coordinates or greater
  substitution depth cannot repair this template.
- [Split-edge two-recipient template](research/searches/ammann-split-edge-two-recipient-gate-2026-10-14.md):
  one marked subdivision per source edge divides both donor triangle and
  receiving quad into two parts, paired once across each half-edge. It is
  combinatorially complete conditional on valid source sectors, but at M
  the two output turns are C and -C for arbitrary donor apex offset. One
  output is nonconvex if C!=0; if C=0, M is straight in both and the outputs
  have at most four genuine corners. [Fresh hostile review](research/reviews/split-edge-two-piece-hostile-review-2026-10-14.md)
  confirms all source/arrow/role cases through the general local identity.
  Moving the apex or splitter alone cannot repair it. A restart must change
  breakpoint incidence (such as at least three final output sectors) or
  the actual piece pairing and boundary count. No such repair is certified.

Both cycles stopped before coordinate, congruence, or periodic-quotient
enumeration; no nonexistent two-class survivor was sent to a decoder gate.
The [independent read-only checker](research/reviews/verify_new_interface_stopping_gates_2026_10_14.py)
verifies all four oriented boundary rules, their far endpoints, the sixteen
flat-inclusive corner-budget cases, and the general split-edge determinant
identities. It imports no producer and runs no search or solver. The registered read-only check **PASSED** [targeted replay](research/reviews/new-interface-design-targeted-replay-2026-10-14.txt), with no certificate writes. The registry now contains
**62 certificate pairs and 303 verifiers (365 checks)**; no fresh full
365-check replay is claimed. The unrestricted two-convex-polygon target,
Y partial-contact possibilities, and general two-hexagon question remain
unresolved.

## Independent Astra commit-readiness audit

The user requested a fresh Astra review of the entire tracked/untracked diff
and recommendations. The [complete audit](research/reviews/astra-commit-readiness-2026-10-14.md)
reviewed all fifty pre-audit changed/new files, including all earlier
uncommitted cycles. **Verdict: READY to commit as scoped partial research.**
There are no outstanding mathematical or code blockers. Low-severity stale
current status headers and old checkpoint labels were repaired and reread;
historical UNKNOWN records and earlier review outcomes remain preserved
with later-status pointers. The audit itself adds one further new artifact.

Astra freshly replayed the directed-offset algebra certificate, independently
reconstructed residual ideals, and independent whole-edge Y obstruction:
all three targeted checks passed. It verified registry totals 62+302=364,
unique verifier paths, all seven new JSON files, relative Markdown links,
and clean git whitespace. No fresh full 364-check replay was run. The proof
trust boundary includes exact SymPy algebra shared by the independently
reconstructed verifiers, without a retained Bezout/formal proof certificate.
The historical NLSAT input is a provenance record rather than an immutable
byte-for-byte old model snapshot; no mathematical exclusion depends on it.

**Historical recommendations (the two incidence gates and the Y BB gate
have since been completed):** first one bounded incompatible two-parent incidence-design
cycle with H=2P+Q, K=P+2Q and area(P)/area(Q)=3phi+1, requiring complete
boundary words for both base and both substitution dissections before any
coordinate census. Second, conditionally, a genuinely split-edge fractional
interface with one marked subdivision point and two exchanged pieces,
requiring a new finite incidence template before solving. An optional single-
breakpoint Y seam analysis remains separate and cannot establish infinite
existence by itself. Closed directed-offset, whole-edge Y, old fan and finite-
state strip families must not be reopened by larger searches. No Git staging,
commit or push was performed for this review request.

## Historical directed-offset bounded Sol cycle (superseded by exact closure)

**Later status:** the exact three-plus-one proof above supersedes this cycle's
UNKNOWN and unresolved restart. Its historical query/status records remain
unchanged. No solver rerun was needed.

The user authorized execution of Astra's construction gate with an independent
Sol adversary. Both agents completed the fixed four-parameter topology.
[Construction and exact residual](research/searches/ammann-directed-offset-gate-2026-10-14.md),
[generator](research/searches/ammann-directed-offset-gate-2026-10-14.py), and
[fresh hostile review](research/reviews/ammann-directed-offset-hostile-review-2026-10-14.md)
are retained. **Full gate UNRESOLVED; no exact two-class survivor and no
aperiodic pair were found.** No source-patch or parameter-grid expansion ran.

Both agents independently derive arrow-preserving diagonal reflections that
identify opposite role choices within each rhomb type. Eight indexed outputs
therefore reduce to four representatives regardless of source/color-role
occurrence. All seven two-class partitions were retained initially, including
cross-species three-plus-one assignments. A tentative inference that unequal
pair means forced within-type classes was rejected before computation.

The [reviewed two-plus-two obstruction](research/lemmas/ammann-directed-offset-two-plus-two-obstruction-2026-10-14.md)
closes all three two-plus-two assignments for the target. Crosswise pairs
contradict unequal rhomb area totals. Within-type congruence requires equal
squared-edge sums, forcing a_X=1/2; area identities and strict donor interior
then force a_Y=1/2 and h_X=h_Y. This is exactly the reviewed midpoint/common-
triangle component with periodic monohedral omission. **Four three-plus-one
partitions remain.** Their cross-species congruence is still unresolved.

Bounded solver history: maximum 180-second cumulative solver wall, no more
than 127 original eight-output partitions. The command used cap160 with
30-second per-query timeout. Its first three-plus-one branch returned
UNKNOWN/timeout at 30.123 cumulative seconds. The initial driver briefly
entered its next branch, then was interrupted at 49.702 seconds with no
result. First-UNKNOWN automatic stopping is now enforced. The [historical
status record](research/certificates/ammann-directed-offset-gate-historical-run-2026-10-14.json)
is not a feasibility or exclusion certificate. No further solver query ran.

The current exact residual explicitly includes all nonincident strict support
inequalities for every source sector and all eight pentagons, strict donor
containment, twenty-four sector-pair separating-axis disjunctions, and ten
cyclic/reversed correspondences each comparing all ten squared distances.
Its real algebraic constants have defining equations and isolating intervals.
It is an **unqueried corrected system**, separate from the historical
turn-based query. No equivalence of those formulations is assumed.
The [algebra certificate](research/certificates/ammann-directed-offset-gate-algebra-2026-10-14.json)
checks symbolic area identities, exact coordinate hash and domain counts;
it is not a feasibility certificate. The adversary's independently rebuilt
checker verifies symbolic formulas and an asymmetric exact fixture with
sixteen strict source sectors and eight genuine pentagons. Global partition
follows for admissible parameters by exact sector coverage and agreement of
shared source arrows; two congruence classes remain the unsolved gate.

**Stopping/restart condition:** the first UNKNOWN reached the declared stop.
Do not increase timeout, discretize more finely, or generate larger source
patches as an automatic restart. A new algebraic elimination or geometric
invariant for the four three-plus-one assignments is required. An eventual
exact two-class survivor must immediately face the fixed two-by-two
homogeneous/wrong-arrow omission attacks and a universally valid intrinsic
chord/arrow decoder; those later gates were not executed without a survivor.

At that earlier gate checkpoint, the registry had **62 certificate pairs and 299 verifiers (361 checks)**.
Two directed-offset additions are registered read-only: exact algebra replay
and the independent symbolic/fixture check. Both additions **PASSED** [targeted replay](research/reviews/ammann-directed-offset-targeted-replay-2026-10-14.txt), with no retained certificates written. No fresh full 361-check replay is claimed.

## Three-track construction cycle (2026-10-14)

The user authorized three Sol agents on P5/Q14 transitions (Q15 in the request
was interpreted as the established Q14), mixed partial-contact parents, and
Ammann fractional resection. The bounded cycle produced an exact P5/Q14
untileability proof, an all-metric no-mixed-contact theorem for the tested
pentagon/hexagon angle words, and a periodic-omission obstruction to one new
Ammann fan transfer. These are restricted results, not a solution of the
unrestricted problem. Independent cross-reviews and replay scope are indexed
in the [cycle audit](research/reviews/three-track-construction-2026-10-14-audit.md).
No automatic patch growth, quotient growth, or additional repairs were run.

## Historical earlier restart and verification checkpoints

The reviewed checkpoint `99833f7` has been committed and pushed. The user has
authorized the exact P5/Q14 experiment and computational construction with
nonconvex parent patches, with counterexample checks inside the construction
loop. Three Sol agents completed those distinct obligations and cross-reviewed the
results. The exact finite domains are closed; further research must use the
restart conditions below, rather than increasing their bounds. No aperiodic pair or
unrestricted impossibility theorem has been established. Keep both
pentagon-containing pairs and two-hexagon pairs in scope; requiring a pentagon
is a construction preference, not a proved global necessity.

Locked environment verification passed on 2026-10-14. The pushed checkpoint registry has
53 certificate pairs and 277 verifiers (330 checks). Its entire disposable
replay **PASSED**, with no certificates written and original research files
unchanged during verification; [complete output](research/reviews/checkpoint-full-replay-2026-10-14.txt).
The [initial checkpoint audit](research/reviews/checkpoint-diff-audit-2026-10-14.md) records
its repairs, review scope and mathematical obligations. The completed construction
cycle adds four certificate pairs and five independent verifiers: all nine new
registered checks **PASSED**, and all six new retained certificates were unchanged.
That checkpoint registry contained **57 certificate pairs and 282 verifiers (339 checks)**.
This is the earlier full 330-check replay plus targeted verification of the nine
additions, not a fresh full 339-check replay. The [cycle checkpoint audit](research/reviews/construction-cycle-checkpoint-2026-10-14.md)
and [targeted replay output](research/reviews/construction-cycle-targeted-replay-2026-10-14.txt)
record the new evidence and its scope. All commands use `mise exec -- conda run
--no-capture-output -n arisearch <command>`. `mise run replay` verifies the full
registry on a disposable copy; targeted replay is `python
research/searches/verify.py --only SCRIPT` inside that environment.

Earlier progress tables, replay counts and completed-cycle narratives are in
[the historical checkpoint archive](research/searches/discovery-log-2026-10-13-checkpoint-history.md).
They preserve provenance and finite domains; current status below takes precedence.

The subsequent three-track cycle adds one certificate pair and seven verifier
entries: **58 certificate pairs and 289 verifiers (347 checks)** in the registry
at that earlier checkpoint. The eight additions passed targeted replay; no fresh full 347-check
replay was run. See the [new replay transcript](research/reviews/three-track-construction-2026-10-14-targeted-replay.txt)
and cycle audit for independent-review scope and dependency checks.

The completed tracks and next restart conditions are:

1. **P5/Q14 is now untileable:** the [forced-neighbor theorem](research/proofs/p5q14-orientation-transition-2026-10-14-untileability.md) closes the former 28-state restart set. All four normalized central states force a Q at a P native v side; all 16 indexed placements per state create a forbidden T-contact. The exact 64-witness certificate and a fresh reconstruction from atomic coordinates verify the contradiction. The full 1536-case transition domain has no survivor. With the earlier exhaustive word reduction this excludes the fixed P with every equiangular Q14. Do not enlarge patches or periodic quotients for these atoms. A restart must change the actual atomic geometry or palette and rederive its necessary contacts.
2. **Mixed partial-contact parent is excluded at every metric of these words:** the [exact offset construction and theorem](research/searches/mixed-partial-parent-2026-10-14.md) produces a genuine disjoint mixed 11-corner parent, but its exterior right-angle wedge cannot be completed. The complete argument excludes every positive-length P/Q contact for native words P=(90,120,120,90,120), Q=(90,135,135,90,135,135), including staggered and aligned-contained seams. Therefore any plane tiling uses only one species; fixed P omission remains excluded, Q-only existence is not classified by this work. A new mixed-parent route must change the far-angle correlation at right corners or the flat-star palette, not just lengths or child count. The reviewed all-hexagon polygonal-parent perimeter obstruction still applies.
3. **One Ammann fractional rule is closed:** the [center-fan transfer](research/searches/ammann-fractional-resection-2026-10-14.md) glues quarter-rhomb triangles across each rhomb edge. It gives a globally compatible fractional cover and removes equal-whole-triad counts, but every output is a strict convex quadrilateral admitting periodic omission. No contact-class catalogue or speculative repair was run. The earlier J-star 5/7 witness remains only local, with whole-triad frequency obstruction. A future surgery needs explicit convex boundary words with at least five genuine corners, global compatibility, and intrinsic decoding; merely escaping an old invariant is insufficient.

Do not relaunch the straight-edge pinwheel resection: [its entire admissible cut family has a reviewed direct periodic omission escape](research/lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md), independently of the failed200-cell compiler. The full canonical Q7 family and complete P120/105-Q12 palette also have freshly reviewed periodic carriers, not unresolved candidates. Other closed families are indexed below.

## Current mechanism registry

The unrestricted target remains unresolved. Completed B5+1, two-U, old wheel, fan, fixed-source and capped global query domains are not resumed. The mechanisms below are new analytic results or exactly specified finite computations; none establishes an aperiodic pair or a universal impossibility theorem.

| Mechanism / current status | Strongest retained result | Remaining obligation / restart condition |
| --- | --- | --- |
| Six-distinct hexagon with arbitrary hexagon partner — reviewed VALID periodic escape | [Full theorem](research/lemmas/hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md), plus [actual-seam six-color extension](research/lemmas/hexagon-six-colors-arbitrary-partner-2026-10-15.md). | No partner metric/multiplicity remains in this scope; one nonzero period suffices. Fewer distinct lengths require the separate results below. |
| Each hexagon has at least five numerical lengths — reviewed doubly periodic escape | [Complete corollary and final unequal adjacent theorem](research/lemmas/hexagon-five-unequal-adjacent-periodicity-2026-10-15.md), [independent hostile review](research/reviews/hexagon-five-unequal-adjacent-hostile-2026-10-15.md). | All common/unequal palettes and repeat positions covered; six-length cases use the reviewed six/five theorem. Never extrapolate to a member with at most four numerical lengths. |
| Rational Y-pentagon family — reviewed VALID untileability | [Unrestricted prototype theorem](research/lemmas/pentagon-y-unrestricted-2026-10-15.md), [infinite parameter family](research/lemmas/y-pentagon-parameter-family-2026-10-15.md), partial contacts included. | Different metrics outside the stated family or a changed contact mechanism; these exact metrics are closed. |
| Three-sector receiving hexagons — reviewed VALID component obstruction | [Arbitrary cuts and physical splits excluded](research/lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md) while donor triangles remain mark-local. | Must change donor geometry, source/retained-vertex incidence, projection domain or the one-H requirement. No cut/split-only scan. |
| Ammann mean-site power cells — reviewed VALID compact-family exclusion | [Exact closed weight-box obstruction](research/lemmas/weighted-ammann-power-small-box-obstruction-2026-10-15.md): mandatory7/6/5cells in every legal source. | Different sites/source metric or separately justified parameter domain; no two-class point in this box. |
| Hat interior-cycle and fixed-frame experiments — completed, limited unreviewed evidence | [11:30direction record](research/searches/astra-direction-2026-10-15-1130.md): two exact convex precursor partitions; eight necessary-angle gates Z3UNSAT. | No candidate, metric or decoder gate. Negative solver evidence is not a reviewed construction-impossibility theorem; a new proposal must change source corner-budget/cross-source incidence. |
| Affine stationary transport — reviewed VALID restricted exclusion | [Equivariant affine theorem](research/lemmas/affine-two-convex-iterable-obstruction.md), [finite transported-species extension](research/lemmas/affine-two-convex-finite-shape-transport.md); non-scalar-power inflation forces parallelograms or no polygon dissection. [Exact rectangle control](research/searches/affine-two-convex-fibonacci-rectangle-control.md). | Finite scalar-power matrices and alternative orientation-dependent hierarchies remain outside; finite transported shapes do not automatically provide their dissections. |
| All-obtuse pentagon/high partner — reviewed VALID | [PPP-density theorem](research/lemmas/contact-structure-high-partner-ppp-density.md): for n>=9 pentagon-only vertices are syndetic; no native PPP angle triple implies untileability at every metric. [Review](research/reviews/contact-structure-high-partner-ppp-density-review.md). | Pentagons with repeated-angle PPP stars, nonobtuse shapes and all other families remain. Uniform positive quadratic counts DO imply bounded gaps; earlier obtuse prose repaired. |
| One-right pentagon/equiangular octagon — reviewed reduction with residual domains | [Native reduction](research/lemmas/contact-right-angle-unrestricted-native-reduction.md), [fresh review](research/reviews/contact-right-angle-hosted-side-necessity-hostile-review.md): no Q-hosted T, all Q contacts whole, only21 native Q masks, flat hosts only three middle P sides of length2u/2v. [Private-side capacity](research/lemmas/contact-structure-right-palette-private-octagon-capacity.md) and [review](research/reviews/contact-structure-right-private-capacity-review.md). | Exactly two private Q slots are closed by the all-metric synthesis below. Zero/one-private repeated-length and zero-private host cases remain subject to the narrower classifications below; no general existence or forcing theorem follows. |
| Symmetric pentagon/octagon channels — reviewed VALID periodic escape | [Exact carrier and positive-parameter family](research/lemmas/contact-structure-right-pentagon-octagon-periodic-carrier.md); [independent quadratic-field checker](research/reviews/contact-structure-right-carrier-independent-check.py), [family slice review](research/reviews/current-exact-convex-source-right-carrier-hostile-review.md). Neither species tiles alone, but the mixed periodic motif kills every displayed pair. | A new candidate must change the symmetric channel geometry; these partners do not classify all arbitrary pairs with the palette. |
| Pinwheel three-triangle fusion — reviewed VALID finite exclusion | [Complete finite record](research/searches/pinwheel-three-triangle-convex-clusters.md), [certificate](research/certificates/pinwheel-three-triangle-convex-clusters.json), [independent checker/review](research/reviews/pinwheel-three-triangle-convex-clusters-review.md):1/6/36 anchored patches, five convex classes, four quadrilaterals and one supplementary pentagon, all periodic omission escapes. | Larger/cut/partial-side clusters are outside. Source decoding is not inherited from a selected pinwheel substitution. [Primary boundary](research/literature/pinwheel-convex-cluster-boundary.md). |
| Irrational radial fans — reviewed VALID pointwise exclusion | [Common-angle theorem](research/lemmas/three-triangle-irrational-fan-angle-obstruction.md), [review](research/reviews/three-triangle-irrational-fan-angle-hostile-review.md): any finite family with positive rational parameter multiples and theta/pi irrational is untileable, including partial contacts and omission. Exact u=(2+i)/sqrt5,u² pair killed. | Rational angles, nonzero affine intercepts and changed corner signatures remain outside. No arbitrary polygon impossibility follows. |
| Six-convex-source reconstruction — reviewed VALID exact fixture, conditional source transfer | [Recovered incidence and primary record](research/literature/current-exact-convex-source-six-reconstruction.md), [profile script](research/searches/current-exact-convex-source-six-profile.py), [explicit thin four-P motif](research/searches/current-exact-convex-source-thin-four-motif.md), [hostile review](research/reviews/current-exact-convex-source-six-hostile-review.md). Four thick/two thin faces recovered; midpoint thin collapse has explicit periodic omission. | Original Penrose arrow/kink compatibility, exact source parameters and universal decoder still unproved. Conditional frequencies(phi,phi,phi,phi,1,1) force balanced fixed macro contents(m,m,m,m,n,n), not a convex partition. |
| Six-child dissection topology — reviewed VALID universal finite theorem | [Every six-child dissection is a native wheel](research/lemmas/six-child-topology-universal-wheel.md), [fresh review](research/reviews/six-child-topology-hostile-review.md); arbitrary convex children>=5 sides, partial contacts and isolated boundary touch handled. [Substitution consequences](research/lemmas/six-child-topology-substitution-consequences.md): no uniform six-child pentagon inflation; stronger positive-conjugate P5/Qn bounds with both parent count gates. | The earlier two-size distinct-angle six-child obstruction now applies to all topologies; [combined synthesis review VALID](research/reviews/six-child-topology-two-size-synthesis-review.md). Seven-child constructions and repeated-angle boundary mappings remain unclassified. |
| General two-private octagon scaffold — reviewed VALID all-metric periodic escape | [Complete theorem](research/lemmas/contact-right-angle-two-private-all-metric-periodic-escape.md), [source review](research/reviews/contact-right-angle-two-private-general-hostile-review.md), [affine review](research/reviews/contact-structure-two-private-octagon-core-all-metric-synthesis-review.md). For every P, exactly two private Q slots force a periodic escape whenever tileable. Nonsymmetric P uses a clean typeR limit and periodic Q scaffold with anchored-band completion; [symmetric synthesis](research/lemmas/contact-symmetric-two-private-all-metric-periodic-escape.md) uses explicit symbolic carriers. Equal/distinct private lengths and all public-side aliases are covered. | Zero/one-private Q remains outside. Every original filling need not be periodic; no existence is claimed for an untileable pair. |
| Equal-private distance3 pair — reviewed VALID restricted universal-period exclusion | [Exact equal-private pair theorem](research/lemmas/contact-right-angle-equal-private-glide-periodicity.md), [finite native analysis](research/searches/contact-right-angle-distance-three-native-analysis.md), [independent ring/global review](research/reviews/contact-right-angle-distance-three-hostile-review.md). All16 radius1 choices were audited independently; clockwise reflected clipping polygons are now normalized, and repaired replays retain both original results. The unique ring transports QQ chains and all P neighbors with a common nonzero period. | Plane existence is not asserted. [Symbolic positive-parameter family](research/searches/contact-right-angle-symbolic-equal-private-glide-family.md) has a [VALID review](research/reviews/contact-right-angle-symbolic-glide-hostile-review.md). The broader two-private existence-of-a-periodic-escape theorem above is distinct from every-original-tiling periodicity. |
| Regular-pentagon six-wheel construction — reviewed VALID complete family exclusion | [Plane theorem](research/lemmas/regular-pentagon-six-wheel-plane-obstruction.md), [potential obstruction](research/lemmas/regular-pentagon-six-wheel-potential-obstruction.md), [exact script](research/searches/regular-pentagon-six-wheel-exact.py), [fresh review](research/reviews/regular-pentagon-six-wheel-hostile-review.md). All0<rho<1 pairs are untileable except rho=1-tan36°, with explicit four-Q periodic escape. | The proposed phi²-inflation[1,5]/[1,6] candidate is permanently killed. A locally disjoint cap does not extend: forbidden108/126 corners inside longer legs supply the repaired global obstruction. New angles or changed support data are required. |
| Binary octagon metric carrier — reviewed VALID unrestricted subfamily exclusion | [All-positive symbolic periodic carrier](research/lemmas/contact-right-angle-no-qq-periodic-carrier.md), [certificate](research/certificates/contact-right-angle-no-qq-symbolic-carrier.json), [independent review](research/reviews/contact-right-angle-no-qq-hostile-review.md). Every positive P in this palette has a grouped binary Q partner with an explicit four-P/one-Q periodic cell. | [Unrestricted binary-Q exclusion](research/lemmas/contact-right-angle-no-qq-binary-native-boundary.md), including partial contacts and derived noQQ, passed the fresh audit. The five-distinct/no-host zero-private domain is closed by the synthesis below; repeated-length and host-plane cases remain open. |
| One-private repeated-middle alias — reviewed VALID unrestricted family obstruction | [Complete all-host theorem](research/lemmas/contact-structure-one-private-repeated-middle-all-host-obstruction.md): w=x with x,y,u,v pairwise distinct and one private Q side is untileable. Native integer counts split into a binary-middle field obstruction or a clean all-R closure contradiction. | [Fresh complete review](research/reviews/contact-structure-one-private-repeated-middle-all-host-hostile-review.md) VALID. Other repeated-side identifications remain outside; the older two-word bridge still requires its explicit extra-middle-R premise. |
| Changed angle/size palette — reviewed VALID complete family exclusion | [Complete theta=720/n family](research/lemmas/sixty-degree-pentagon-equiangular-dodecagon-omission.md), [fresh review](research/reviews/sixty-degree-pentagon-equiangular-dodecagon-omission-hostile-review.md). For every n>=9, P has one theta/four(135-theta/4) corners and Q is an equiangular n-gon. All n!=12 pairs are untileable by complete native-star/corner-weight analysis; n=12 has an explicit central-hexagon periodic P-only escape at every metric. | Different corner signatures and nonequiangular partners remain outside. This entire specific size/angle family is closed without a monohedral classification. |
| Generic zero-private octagon — reviewed VALID full restricted synthesis | [AllR/degree-two reduction](research/lemmas/contact-right-angle-no-qq-generic-zero-private-reduction.md), [native-count(3,3,2) obstruction](research/lemmas/contact-right-angle-no-qq-zero-private-321-obstruction.md), [(4,2,2) clean-core extension](research/lemmas/contact-right-angle-no-qq-zero-private-422-core-reduction.md). New exact tagged geometry replaces numerical privacy; actual-contact persistence and mask symmetry are explicit. | [Complete fresh synthesis review](research/reviews/contact-right-angle-zero-private-full-synthesis-hostile-review.md) VALID. Side collisions and zero-private host planes remain outside. |
| Changed nonequiangular octagon — reviewed VALID exact fixture exclusion | [Exact support-line deformation](research/lemmas/contact-non-equiangular-octagon-one-deformation-obstruction.md), [fresh review](research/reviews/contact-non-equiangular-one-deformation-hostile-review.md). Q has angles112.5,157.5,135^6; its mixed acute star admits a local patch but five forced public unit edges give5q<=p while corner capacity gives4p<=13q. The pair is untileable, retaining arbitrary P-P partial contacts. | A further changed support/metric mechanism must escape these precise contact-budget bounds. No blanket ETE assumption or all-nonequiangular theorem is made. |
| One-private / all five P lengths distinct — reviewed VALID complete classification | [All-metric classification](research/lemmas/contact-right-angle-one-private-all-distinct-periodic-escape.md). Global native integer counts force dimers pointwise; all partial-contact host planes reduce to the aligned periodic ray or the crossed negative-metric ray. [Incidence audit](research/reviews/contact-right-angle-one-private-global-incidence-review.md) and [native bridge audit](research/reviews/contact-right-angle-one-private-native-bridge-hostile-review.md) are VALID. | [Fresh complete audit](research/reviews/contact-right-angle-one-private-all-distinct-complete-hostile-review.md) VALID. General repeated P side lengths remain outside. The separate w=x, pairwise-distinct x,y,u,v family is closed by the all-host obstruction above; its earlier two-word bridge exhaustion alone was insufficient. |
| Ordinary similarity / moved shared boundary — reviewed VALID scheme exclusion | [Complete straight-edge family periodic escape](research/lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md), [fresh review](research/reviews/affine-two-convex-straight-edge-resection-hostile-review.md): every admissible cut preserves equal antiparallel hexagon edges and an explicit2Q periodic carrier. Quarter fixture has covolume17/2. | [Specified200-cell compiler](research/searches/affine-two-convex-pinwheel-quarter-cut-parents.md) independently has insufficient candidates for both parents. New boundary directions/topologies are required; changing only cut position or source depth cannot rescue the scheme. |
| Genuine Q-host fixtures — reviewed exclusions and periodic escape | Nonequiangular Q8 directions(22.5,45,90,135,202.5,225,270,315), four-equal P acute/bevel lengths and private Q host H=2u. Earlier asymmetric Q-host caps fail at a missing far native side pair; the repeated P metric supplies that missing pair. | The private-H2 four-equal fixture is now [untileable after independently reviewed repairs](research/reviews/contact-non-equiangular-four-equal-repaired-hostile-review.md): genuine caps are sparse, and a clean limit requires the absent middlew. The public-H1 variant has an [exact rotated periodic carrier](research/lemmas/contact-non-equiangular-public-h-four-equal-periodic-carrier.md), now [freshly reviewed VALID](research/reviews/contact-non-equiangular-public-h-four-equal-hostile-review.md). No old equiangular whole-Q/contact theorem is imported. |
| Nonequiangular alias fixture — reviewed VALID local exclusion | [Exact support pivot c with P x=w=1](research/lemmas/contact-non-equiangular-octagon-alias-candidate-obstruction.md), [independent review](research/reviews/contact-non-equiangular-alias-hostile-review.md). All four rings in the complete4^5 native domain fail at a mandatory far PP endpoint needing a Q135 side pair absent from Q. | This specific changed alias fixture is closed; not a theorem about all nonequiangular aliases. |
| Two-support nonequiangular Q — reviewed VALID full positive family carrier | [All-positive symbolic family carrier](research/lemmas/contact-non-equiangular-two-support-symbolic-periodic-carrier.md), [independent symbolic reconstruction](research/reviews/contact-non-equiangular-two-support-carrier-independent.py). ANY positive right P(x,u,v,y,w), partner Qword(H,u,w,v)^2 and two changed supports admit1Q/2P periodic cells for arbitraryH>0; all36 endpoints and area identities passed symbolically. | [Complete third audit](research/reviews/contact-non-equiangular-two-support-full-family-hostile-review.md) VALID. Other Qwords remain outside. |
| P5/Q7 branching signature — reviewed VALID full canonical family periodic escape | [Full positive family](research/lemmas/contact-pentagon-heptagon-branched-periodic-carrier.md): every right-palette P has Q7word(A,a,u,w,v,a,B), A=v+w/√2,B=u+w/√2, and an exact2P/2Q periodic cell with true QQQ vertices. [Independent closed-coordinate reconstruction](research/reviews/contact-pentagon-heptagon-branched-independent.py) regenerates all24unrestricted integral partners symbolically. | [Fresh full audit](research/reviews/contact-pentagon-heptagon-branched-hostile-review.md) VALID. Other heptagon metrics remain outside; branching by itself does not force hierarchy. |
| P120/105 + equiangular Q12 — reviewed VALID full palette periodic escape | [Complete metric classification](research/lemmas/contact-pentagon-120-105-dodecagon-periodic-escape.md): unrestricted contacts force x=y,u=v and regular Q; every positive remaining metric has an exact6P/1Q triangular periodic cell. [Independent alternate-field native reconstruction](research/reviews/contact-pentagon-120-105-dodecagon-independent.py) verifies42whole-edge partners and all-w>0 support signs. | [Fresh complete audit](research/reviews/contact-pentagon-120-105-dodecagon-hostile-review.md) VALID. The entire stated angle palette is closed; mixed PPP and different Q angles remain outside. |
| Mixed-PPP P5/Q14 third-angle palette — exact untileability | [Forced-neighbor theorem and certificates](research/proofs/p5q14-orientation-transition-2026-10-14-untileability.md): all 64 indexed forced-Q placements have forbidden T-contact; full 1536 transition cases also fail. Fresh direct-coordinate reconstruction independently recovers the four central states and all witnesses. | Former 28-state restart is closed, including fixed P with any equiangular Q14 via the earlier complete word audit. Change atoms/palette before reopening; no larger quotient search. |
| Nonconvex polygonal-parent construction — mixed seam obstruction | [Perimeter theorem](research/lemmas/nonconvex-parent-hexagon-perimeter-bound.md) excludes all-hexagon finite polygonal similarity hierarchies. [New mixed partial-parent theorem](research/searches/mixed-partial-parent-2026-10-14.md) excludes all positive P/Q contacts for the tested 90/120 and 90/135 native words, not just their eight old full-edge parents. | Change right-corner far-angle correlations or flat palette. Side-length changes and more children cannot fix this mixed-contact obstruction. P-only controls are finite local patches; Q-only existence is not classified. |
| Ammann cross-source J-star / fractional fan — local 5/7 witness; new fan excluded | [J-star resection](research/searches/contact-structure-ammann-j-star-resection.md) remains a local strict-convex 5/7 witness with omission excluded. [New edge-fan rule](research/searches/ammann-fractional-resection-2026-10-14.md) supplies an exact global fractional cover, but all outputs are convex quadrilaterals with periodic omission. | Equal whole-triad cover still contradicts source frequencies. New >=5-corner fractional boundary words, global two-class compatibility and every-tiling decoder are required; fan rule is closed. |
| Ammann K/L replacements — reviewed fixed schemes closed | [Single triad4/8 gate](research/searches/contact-structure-ammann-corner-triad-gate.md), [four double-corner alternatives](research/searches/contact-structure-ammann-double-corner-gate.md); the6/6 branch has a separate exact Q-only periodic escape. | The [independent review](research/reviews/ammann-cross-source-resections-independent-review.md) confirms these fixed boundary gates and the 6/6 periodic omission. Any convex 6/7 realization is excluded by the reviewed hexagon/higher-side theorem, although tileability is unclassified. All four fixed double-corner schemes are closed for the target; larger or fractional replacements remain outside. |

## Inherited results and paused mechanisms

The completed unique-B-star, complementary two-angle hexagon and eleven-word
B5+1 families remain closed within their stated hypotheses. Distinct,
non-120 complementary three-angle coverage retains its stated resonance domain.
The original two exact pentagon/hexagon candidates are falsified. The full
[historical mechanism index](research/searches/discovery-log-2026-10-13-checkpoint-history.md)
links all older proofs, certificates, reviews and finite search domains.

- The [global two-hexagon census](research/lemmas/two-hexagon-global-census.md)
  remains paused: 316 stored rank-at-most-three covering types were checked;
  ranks 4 through 10 and exhaustive regeneration of the flat census were not.
  Inconclusive queries require a new geometric constraint or decomposition,
  not an increased timeout. Preserve noncovering parents if reopening.
- [Ammann three-shape forcing](research/lemmas/ammann-forcing-aperiodicity.md)
  is reviewed on its stated generic domain. Two-class convex replacement and
  universal decoding remain separate obligations; the old Lemma S density
  proposal remains unresolved. Generalized collapse exhaustiveness is still
  [unresolved outside the reviewed original domain](research/reviews/ammann-two-class-exhaustiveness-review.md).
- The [kite/dart recomposition](research/reviews/kite-dart-exclusion-audit-rereview.md),
  [edge attachments](research/reviews/kite-dart-edge-attachment-audit.md),
  fixed-unit Robinson compiler and old whole-source fusion schemes retain
  their exact exclusions. New cuts, branching incidence or a changed source
  hypothesis must be specified before any new enumeration.
- Periodic partner constructions for V/V, Y/Y, U/W and V/W do not classify
  arbitrary independently chosen metrics. Repeated-length and irrational-angle
  hexagon families retain the exclusions and residual domains in the archive.
  No closed family is reopened merely by increasing patch depth.

## Established structural constraints

| Result | Status and scope | Proof and review |
|---|---|---|
| Monohedral escape; exclusion of triangles and quadrilaterals; rank-two side-count inequality | Internally checked. The torus inequality does not exclude rank-one periods. | [Side-count proofs](research/lemmas/side-count-and-monohedral-obstructions.md) |
| Every tileable finite convex protoset has a member with at most six sides | Fresh independent re-review VALID (2026-10-10). Includes partial contacts and T-junctions. | [Proof](research/lemmas/side-count-and-monohedral-obstructions.md), [review](research/reviews/global-side-count-review.md) |
| A hexagon paired with a polygon of more than six sides cannot be aperiodic | Fresh independent re-review VALID (2026-10-10). Depends on the cited unrestricted monohedral hexagon classification. | [Proof](research/lemmas/hexagon-limit-and-periodicity.md), [review](research/reviews/hexagon-higher-side-review.md) |
| A tileable two-hexagon pair admits an edge-to-edge, trivalent limit tiling | Defect-free limit adversarially re-reviewed after the uniform sector-disk repair. Honeycomb combinatorics and at least one-third same-type contacts follow; arbitrary periodicity does not. Fresh uniform vertex-separation re-review is valid. | [Proofs and review links](research/lemmas/hexagon-limit-and-periodicity.md) |
| Pentagon curvature and relative density constraints | Reviewed. An aperiodic (5,6) pair requires positive-density subdivision or excess-valence defects. | [Proof](research/lemmas/pentagon-curvature.md), [review](research/reviews/pentagon-curvature-review.md) |
| Uniform density when a subfamily cannot tile | Fresh independent review VALID. Every fixed-radius disk meets the complementary types; area/count lower bounds follow. Hypothetical aperiodic two-hexagon pairs require both types at positive lower density in every admitted tiling. | [Density theorem](research/lemmas/two-type-uniform-density.md), [review](research/reviews/two-type-uniform-density-review.md) |
| No angle multiset summing to pi forces edge-to-edge contacts | Proved internally; repaired after hostile review; independent re-review pending. Permits higher valence. | [Proof](research/lemmas/angle-nonresonance-edge-forcing.md), [review](research/reviews/angle-nonresonance-review.md) |
| All angles strictly between pi/2 and pi force edge-to-edge trivalence | Proved and reviewed; excludes all-obtuse (5,5) and aperiodic (5,6) pairs. | [Proof](research/lemmas/obtuse-edge-forcing.md), [review](research/reviews/obtuse-edge-forcing-review.md) |
| Convex fusion transfers strong aperiodicity under explicit source/partition hypotheses | Conditional theorem has a fresh VALID review for its stated unmarked-source and exact-partition hypotheses. No usable source partition is certified. | [Proof](research/lemmas/convex-cluster-fusion.md), [fresh review](research/reviews/convex-cluster-fusion-basic-fresh-rereview.md) |
| Finite convex multitile clusters cannot occur in everywhere-trivalent edge-to-edge convex tilings | Proved internally; extended during hostile review; independent re-review pending. Fusion must use a source with combinatorial defects. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/trivalent-fusion-review.md) |
| Real corner/edge frequency balance | Proved necessary conditions; repaired after hostile review; independent re-review pending. Not a global realization theorem. | [Proof](research/lemmas/frequency-balance.md), [review](research/reviews/frequency-balance-review.md) |

Thus the surviving side-count possibilities are a pair containing a pentagon,
or two hexagons. These constraints do not resolve either general case.

## Paused binary-hexagon obligation ledger

For B with native side word `pppqqq`, use four arc categories: N has no legal
homogeneous triple; C has both native angles120; P has one120 angle and one
other angle; M has a noncentral mixed2+1 homogeneous triple. The four
homogeneous lines intersect only at C. Distinct p,q and `0<delta<30` remain
explicit hypotheses. Reflection may swap both native arc orders; exchanging
length names requires the reviewed A normalization and never changes the
aperiodicity definition.

| Domain | Strongest current result | Exact artifact / remaining obligation |
| --- | --- | --- |
| At least one N arc | Every tileable member has a reviewed periodic escape | [No-homogeneous](research/lemmas/branching-hexagon-two-run-no-homogeneous-star-classification.md), [one-noncentral](research/lemmas/branching-hexagon-two-run-one-noncentral-homogeneous-arc.md), [center/N necessity](research/lemmas/branching-hexagon-two-run-pp-center-no-qq-homogeneous-classification.md) |
| M/M, both relative native orders | Untileable; forward and complete reverse obstruction independently VALID | [Forward](research/lemmas/two-homogeneous-forward-mixed-arcs-obstruction.md), [complete reverse](research/lemmas/two-homogeneous-opposite-mixed-arcs-full-obstruction.md), [fresh whole reverse review](research/reviews/two-homogeneous-opposite-mixed-arcs-full-obstruction-review.md) |
| C/M, up to length normalization | Complete periodic-escape classification, independently VALID | [Center/mixed](research/lemmas/two-homogeneous-center-mixed-qq-classification.md) |
| C/P, up to length normalization | Complete periodic-escape classification, independently VALID | [Center/pure](research/lemmas/two-homogeneous-center-pure-qq-classification.md), [fresh whole-proof review](research/reviews/two-homogeneous-center-pure-qq-classification-review.md); all four phase/domain/native-metric transfers checked |
| C/C | Closure requires p=q, outside distinct-binary scope | Both equal120 arcs have unit chain norm2; closed positive p and q chains therefore require2p=2q |
| P/M and P/P | OPEN; no actual necessity/realization theorem retained | Both-end native contacts, allowable AA seams and actual phase must be handled. Old no-qq-homogeneity exclusion and center-slot arguments do not apply |

The [same-slot](research/lemmas/branching-hexagon-two-run-pp-center-periodic-family.md)
and [cross-slot](research/lemmas/branching-hexagon-two-run-pp-center-cross-periodic-family.md)
positive carriers are independently VALID on their full exact domains, both
admissible quadratic branches and their coalescence. They provide sufficiency,
not arbitrary-pair necessity. Equal lengths and arbitrary A remain outside the
negative binary-family classifications. No whole parent-family closure or
unrestricted impossibility theorem is claimed.

## Paused Cairo obligation ledger

[The native master reduction](research/lemmas/partial-contact-cairo-two-cross-native-reduction.md)
retains the complete72-pattern/13-orbit/7830-flat domain and493 exact seam
exclusions. Actual-order refinements and native Euclidean carriers replace
local feasible balances by reviewed periodic witnesses where proved. The
[seven-target signed native map](research/lemmas/partial-contact-cairo-mixed-quotient-seven-stratum-reduction.md)
is independently VALID. The [ray459 theorem](research/lemmas/partial-contact-cairo-mixed-quotient-fixed-ray459-periodic.md)
now has a fresh full native-geometry/links/holonomy/coverage VALID review.
[The six-target synthesis](research/lemmas/partial-contact-cairo-mixed-quotient-six-stratum-reduction.md)
removes that entire1D ray and is independently VALID after its separate synthesis review.

The conservative necessary residual targets are:

- dimension2: separated46, separated49, orbit6 flat239 only on
  `sqrt(3)*a/4 < b < a/sqrt(3)` with a=Pa,b=Pb;
- dimension1: orbit1 flat759, orbit6 flat906, orbit7 flat575.

All original positive/private active-event and actual-order domains remain
in force. Internally repeated arms and three/four shared-arm coincidences are
outside this full two-sharing reduction. No remaining primal establishes
tilability. No claim is made that every original tiling of a killed metric
is periodic; one admitted periodic witness suffices to kill aperiodicity.

Preserved bounded negatives: ray759 selected10-face proposal reached its
1,000,000-node cap; ray575 selected8-face proposal exhausted909,775 nodes;
ray906 selected10-face proposal exhausted8,995 nodes; low239 selected20-face
proposal reached its2,000,000-node cap. These are finite-model results only,
not unrestricted untileability. Exact domains and certificates remain in
[the native search](research/searches/partial-contact-cairo-mixed-quotient-native-search.py)
and corresponding subject records. Full residual-color models retained only
necessary primals. Further quotient-size or balance-model expansion is blocked
without a new geometric constraint or proved finite-model property.

## Dependency gates and closed-route restart rules

Retain the status in the structural table above. Repaired angle-nonresonance,
trivalent fusion and real frequency balance are not silently
promoted by successful finite replays. Intrinsic deterministic-state arguments
require their explicitly stated neighbor uniqueness; their repaired review
obligation is not replaced by broader periodic examples.

The fixed-unit Robinson source compiler remains closed inside the regular
fixed-slope/local-matching boundary. Its generalized audit covered409 objects,
with all mandatory V boundaries excluded; singular selections outside that
boundary are unclassified. Reopen only changed exact cuts, scale, slope or
another used assumption that removes the actual obstruction; do not rerun
intercept/residual filling searches. [Source gate and checklist](research/lemmas/pentagrid-robinson-generalized-source-gate.md).

Arbitrary V/V and Y/Y compatibility needs a new necessity invariant; selected
periodic partners are not arbitrary-pair classification. Area-compatible U/V
nonhomothetic existence and forcing remain blocked. The retained phi3 SMT
trial remains historically UNKNOWN at120.205638s; the later exact golden-U/V
search exhausted the 5U+8V parent, independently of that timeout.
[Exact old trial](research/searches/pentagrid-golden-metric-phi3-macro.md),
[later exclusion](research/lemmas/convex-substitution-golden-uv-all-lambda.md).
Ammann now has a reviewed three-shape forcing proof on its stated generic
domain, but fusion still lacks a two-class convex partition and unrestricted
forcing for the final shapes.
[Current source proof](research/lemmas/ammann-forcing-aperiodicity.md).
