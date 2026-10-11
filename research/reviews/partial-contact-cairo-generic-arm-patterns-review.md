# Independent hostile review of209 generic Cairo arm patterns

Date2026-10-10. Reviewer: root, independent of the author.
[Submitted computation and conditional theorem](../searches/partial-contact-cairo-generic-arm-patterns.md).

Exact claim: of all209 injective cross-arm equality patterns,22 force extra
arm equalities, and under the explicitly stated generic event/e exclusions,
147 patterns cannot tile;40 pass the necessary e-seam endpoint test.
This is not a sufficiency claim or a classification of exceptional metrics.

Checked all hypotheses and attacks:

* Four arms per species are internally distinct. A species cannot disappear
  because the separately independently reviewed private-arm theorem excludes
  its monohedral tiling, without any assumption on its e length.
* Exact vector closure is b-c=sqrt3(d-a); e=sqrt3*c+d-2a. The8-arm
  nullspaces include all positive metric solutions for each declared pattern.
* Rejecting an identically forced extra equality is sound because patterns
  declare the complete cross matching. No numerical tolerance is used.
* The187 retained exact positive fixtures certify nonempty strict positive
  cones. Normalizing lengths>=1 is sound by homogeneous scaling. Finite
  proper hyperplanes cannot cover an open relative cone, so nongeneric
  positivity fixtures do not invalidate nonemptiness of generic strata.
* All same-perpendicular right-corner slots, including identical slots of
  different physical copies, enter the event list. The equal-bank-sum
  compatibility relation is deliberately an overapproximation. Omitting
  strict switch inequalities can create false survivors but cannot reject
  a genuine contact. The relation is not transitively closed.
* Generic exclusions make every e side unsplit. Its opposite side must
  therefore be a whole e. Both same-species and identically equal cross-
  species e partners are tested with both endpoint identifications. A third
  beta sector must use an isolated(b,c) corner because an e-adjacent corner
  would put an unsplittable e against an arm. Both ray orders are included.
* Requiring an e partner for both species is sound by the omission argument
  above. Failing it excludes actual plane tilings, not merely a torus ansatz.
  Passing it certifies only a necessary local condition.

Added [independent verifier](verify_cairo_generic_arm_patterns_independent.py):
it reconstructs all patterns with declared shared labels collapsed BEFORE
closure, unlike the producer's8-slot formulation. It computes contact forms
in this different reduced basis and verifies all statuses and allowed e
seams. It separately verifies all187 retained positive fixtures and raw
8-arm/2-e values without a polyhedral solver. Every209 pattern is accounted
for once; the40 survivors comprise8 k=2 and32 k=3 patterns.

    conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_generic_arm_patterns_independent.py

No defect or repair found. The finite classification and conditional generic
untileability claims are VALID. The extra coincidence hyperplanes, repeated
arms within a species and global extensions of40 survivors remain outside
this result. No novelty or unrestricted impossibility claim is made.


## Fresh actual-slot refinement and periodic sufficiency audit

The original147/40 overapproximation remains correctly recorded. A stronger
necessary relation anchors each event to its original native arm slot i:
its perpendicular seam length is that slot's actual90-complement, so the
bank sum belongs to S_i. Opposing unequal native arms i,j require S_i and
S_j to intersect by the reviewed two-T proof. Dropping the strict switch
inequalities is safe; pooling other slots with the same bank length would
lose this necessary condition. Both fifth-side endpoint tests use actual
isolated(b,c) slots of the third species and permit both ray orders.

The independent reduced-label checker reconstructs all S_i and permitted
slot pairs, all e partner orientations and both complete classifications.
It compares every retained anchored_status, anchored_slot_compatibility,
anchored_allowed_e_seams and the aggregate22/155/32 counts. All assertions
PASS. The eight additional rejections are the former five-label-path orbit.
Their previous absence of a sufficient subset is preserved as historical
overapproximation evidence, not an unresolved final generic case.

For each final32 survivor the checker independently enumerates actual
native Cairo reflections i->3-i and species swaps. It verifies the recorded
map of one sufficient two-equality subset and recomputes their complete
orbit, giving8 two-match and24 three-match survivors. The existing Y criterion
uses side words(b,c,d,e,a), so Q_Y2=P_Y0 and Q_Y4=P_Y1 are exactly
Q_d=P_b,Q_a=P_c. Root checked these indexing and angle conventions directly
against the reviewed Y theorem. The other orbit is the new swapped-arm cone;
its independent full-cone review now returns VALID, including coalescence.
Actual positive polygons supply all positivity hypotheses of the sufficient
cones. Additional equalities merely restrict their domains and cannot remove
their periodic witness.

Verdict: **VALID** for
[the generic Cairo dichotomy](../lemmas/partial-contact-cairo-generic-periodic-dichotomy.md).
Every pair in its stated internally-distinct/generic domain is untileable
or has a doubly periodic tiling. This remains a restricted theorem, not an
unrestricted two-Cairo classification or a solution to the main problem.
