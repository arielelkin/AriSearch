# Independent integration audit: interface construction cycle

Date: 2026-10-14. Reviewer: terra_interfaces. The reviewer authored the Y
interface construction and mark-height cycle, but did not develop the
6P4Q CP-SAT model or whole-edge native-occurrence propagation proof.
This audit concerns those independently developed additions and integration
scope; it does not replace their fresh claim-specific hostile reviews.

CP-SAT model source audit: no actionable mathematical defects found.
Squared lengths are exact integer invariants, despite the note's wording
"numerical lengths." The native vertex slots, endpoint reversal equations,
perfect matching, and exact label counts are necessary for the declared
whole-native-edge torus domain. The intrinsic reflections y=x for P and
x=0 for Q justify normalization to directly oriented prototype faces.
Permuting identical faces and equal-star slots justifies the fixed R and D
placements. No actual reflection case is lost.

The lazy positive validation checks single circular corner links and face
connectivity. Vertex IDs are constant on corner cycles by the pairing
equalities. With 15 actual cycles and 15 nonempty specified slots, each
slot has exactly one cycle, so the specified angle totals are preserved.
A rejected pairing cannot be repaired by relabeling slots to change its
actual links or connectivity; the pairing-only nogood is sound. No
positive witness was obtained, so this validation was not used to assert
a plane covering. The saved INFEASIBLE result is a reproducible fixed-model
solver status, correctly distinguished from a formal proof certificate.

Whole-edge propagation proof source audit: no defects found. A Q's native
GG side cannot match GG because that would require a length-4 GG ray, while
the sole star with GG has length-2 GG ray. It must match a P RA side. The
actual P reached there has both R sides adjacent to G corners, forcing
both its A corners into ABG stars. Its AB sides then force both actual B
corners into ABG. Their shared BB side would need a native length-2 GG
mate, which does not exist. The proof retains actual indexed occurrences
and both far endpoints, and reflections preserve all used correlations.
This excludes all whole-native-edge plane coverings independently of the
solver count. It leaves arbitrary partial contacts outside. Fresh hostile
proof review was pending at this audit's source-read time.

One actionable integration defect was reported to root: the earlier
full-edge-torus-balance lemma still states that no ten-face experiment was
executed or authorized in this cycle. The subsequently authorized completed
6P4Q run makes that current-cycle prose stale. It should describe the earlier
stage and link the completed run and stronger propagation proof. The lemma's
mathematical necessary-count statements are unaffected.

Readonly registry inspection: the new area/interface/strip producers and
claim-specific checkers are present in research/searches/verify.py. An
initial transient incompatibility between the registered CP-SAT --check
entry and its null-witness negative record was reported and repaired before
completion of this audit. The final --check accepts the declared negative
metadata and invokes the independent exact native-propagation checker; it
explicitly neither reruns the solver nor claims a formal UNSAT certificate.
Source reinspection confirms the repair. Root/author reported its targeted
check passed.

No full repository replay was run by this reviewer. Root reported eight
initial targeted checks passing and the independent symbolic mark-height
check passing, with combined targeted replay and final registry additions
still being integrated. This audit does not certify a later registry state
or promote finite solver exclusions into unrestricted existence results.
