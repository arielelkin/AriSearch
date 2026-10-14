# Independent diff readiness review: Y BB and intrinsic c seam

Date: 2026-10-14. Verdict: **READY for commit as scoped partial research**.
The unrestricted two-convex-polygon problem remains unresolved.

Scope: inspected the uncommitted tracked diff and all new research
artifacts: the Y full-BB-mate lemma and diagnostic, the intrinsic Ammann
c-seam note and audit, their independent reviews/checkers, and retained
targeted replay. Also checked governing research instructions, source angle
and side-word dependencies, discovery-log integration, and replay registration.
No construction search or larger census was run for this review.

## Mathematical challenge

The Y proof survives independent challenge of zero, one, and multiple interior
transitions. The longer containing-side case is essential: the surviving
P AB contact is killed by a forced B arm passing the host A endpoint, rather
than by the existence of its overlap-free four-tile precursor. Reflections
do not introduce new side lengths or endpoint types. The proof establishes
full equal-length mating on BB only; it does not establish edge-to-edge
contacts elsewhere, mixed-plane existence, or nonperiodicity.

The Ammann half-turn gives a legitimate local P1-P1 full-c contact with
disjoint interiors and endpoint angle sum 216 degrees. It refutes only the
isolated local heterotypic-contact predicate. The source three-shape vertex
atlas may reject that patch farther away; no plane extension or global
counterexample is inferred.

## Findings and repairs

1. The Y author proof originally left local finiteness and native-corner
   endpoints implicit. The revised proof includes the contained-disk packing
   argument and explains why consecutive transitions delimit a full native
   guest side. Re-read and accepted.
2. The Ammann review conflated reflection with absence of an intrinsic
   directed endpoint distinction. The asymmetric side cycles can identify
   both c endpoints and canonically name vertices and diagonals. Revised
   author/reviewer wording correctly says that this does not prove an X/Y
   rhomb-arrow rule or select a forced source decoder. Re-read and accepted.
   Counting five diagonals is an inventory, not a geometric proof that they
   are indistinguishable or that all are viable source cuts.
3. The discovery-log latest-gate label described the previous Ammann family
   closure. It is now labeled previous. Historical next-work recommendations
   and an already-incorporated angle-bound request were also flagged for
   explicit historical/repaired wording before staging.

The root completed the final wording-only cleanup identified in item 3
and aligned the author checker comment with item 2 before staging. These
are scope and staleness repairs, not unresolved mathematical obligations
in the lemmas.

## Integration and validation

All four new checker paths are registered once. The increment from 303 to
307 verifiers is consistent with 62 certificate pairs and 369 total checks.
The retained targeted replay records four passing new checks and explicitly
does not claim a fresh full-suite replay. The root separately reports seven
passing targeted source/new checks. This reviewer inspected the scripts and
retained output; the root performed that fresh seven-check replay.
`git diff --check` passed during this review. No Git mutation was performed
by this reviewer.

The next justified Y step requires a fixed exact propagation argument on
remaining contact types. An Ammann restart requires a specific complete-corona
rule for the actual two outputs, with decoding and omission obligations.
Neither larger patches nor further c-word enumeration closes these gaps.
