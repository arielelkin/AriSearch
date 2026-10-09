# Current research state for two convex tiles

**Problem status:** unresolved.
**Checkpoint:** 2026-10-09 repository audit; mathematical state from the October 3 review.
No construction or complete impossibility theorem meets the acceptance gates.
No exact pair with established plane-tiling existence survives the recorded
searches. The most recent joint pentagon–hexagon pair is **falsified**.

Start with [the problem](research-problem.md), [the protocol](research-protocol.md),
and this log. Stable proofs, exact search records, certificates, source audits,
and adversarial reviews are stored by subject under `research/`. Verification
commands and their scope are recorded below.

## Established structural constraints

| Result | Status and scope | Proof and review |
|---|---|---|
| Monohedral escape; exclusion of triangles and quadrilaterals; rank-two side-count inequality | Internally checked. The torus inequality does not exclude rank-one periods. | [Side-count proofs](research/lemmas/side-count-and-monohedral-obstructions.md) |
| Every tileable finite convex protoset has a member with at most six sides | Proved internally; repaired after hostile review; independent re-review pending. Includes partial contacts and T-junctions. | [Proof](research/lemmas/side-count-and-monohedral-obstructions.md), [review](research/reviews/global-side-count-review.md) |
| A hexagon paired with a polygon of more than six sides cannot be aperiodic | Proved internally; repaired after hostile review; independent re-review pending. Depends on the cited unrestricted monohedral hexagon classification. | [Proof](research/lemmas/hexagon-limit-and-periodicity.md), [review](research/reviews/hexagon-higher-side-review.md) |
| A tileable two-hexagon pair admits an edge-to-edge, trivalent limit tiling | Defect-free limit proved internally and repaired after hostile review; independent re-review pending. Honeycomb combinatorics and at least one-third same-type contacts follow; periodicity does not. | [Proofs and review links](research/lemmas/hexagon-limit-and-periodicity.md) |
| Pentagon curvature and relative density constraints | Reviewed. An aperiodic (5,6) pair requires positive-density subdivision or excess-valence defects. | [Proof](research/lemmas/pentagon-curvature.md), [review](research/reviews/pentagon-curvature-review.md) |
| No angle multiset summing to pi forces edge-to-edge contacts | Proved internally; repaired after hostile review; independent re-review pending. Permits higher valence. | [Proof](research/lemmas/angle-nonresonance-edge-forcing.md), [review](research/reviews/angle-nonresonance-review.md) |
| All angles strictly between pi/2 and pi force edge-to-edge trivalence | Proved and reviewed; excludes all-obtuse (5,5) and aperiodic (5,6) pairs. | [Proof](research/lemmas/obtuse-edge-forcing.md), [review](research/reviews/obtuse-edge-forcing-review.md) |
| Convex fusion transfers strong aperiodicity under explicit source/partition hypotheses | Conditional lemma proved internally; repaired after hostile review; independent re-review pending. No usable source partition certified. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/convex-cluster-fusion-review.md) |
| Finite convex multitile clusters cannot occur in everywhere-trivalent edge-to-edge convex tilings | Proved internally; extended during hostile review; independent re-review pending. Fusion must use a source with combinatorial defects. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/trivalent-fusion-review.md) |
| Real corner/edge frequency balance | Proved necessary conditions; repaired after hostile review; independent re-review pending. Not a global realization theorem. | [Proof](research/lemmas/frequency-balance.md), [review](research/reviews/frequency-balance-review.md) |

Thus the surviving side-count possibilities are a pair containing a pentagon,
or two hexagons. These constraints do not resolve either general case.

## Construction routes and exact remaining gaps

### Convex fusion and Ammann recomposition

**Status:** blocked application; the general fusion lemma remains valid.
The classical two-pentagon/one-hexagon source has not been certified strongly
aperiodic with reflections and unrestricted contacts. Exact final tiles,
legal vertex stars, species frequencies, and a global convex cluster partition
are also missing. [The source audit](research/reviews/ammann-convex-source-audit.md)
and [coordinate parameterization](research/lemmas/ammann-coordinate-parameterization.md)
retain recovered data. The conditional aggregate ratio is H:P = 1:2 phi,
assuming the marking graph edge/vertex counts and face-incidence hypotheses;
the split between pentagon species is unproved. Earlier figure-based
frequency estimates are superseded.

**Reopening condition and next action:** retrieve the primary unrestricted
forcing proof and exact diagram data, or propose a different certified convex
source. Only after source and frequency hypotheses are established should
cluster enumeration resume. Trivalent edge-to-edge sources cannot support
finite convex multitile fusion. Identifying/deleting an Ammann class remains
unsupported because the published forcing uses distinguishing lengths.

### Two obtuse hexagons as a rule compiler

**Status:** general mechanism open; the recorded Walton compiler families
are falsified. For each geometric type, positive side lengths and angles
in `(pi/2, pi)` must satisfy total exterior turn `2 pi` and exact vector
closure. Equal side lengths and corner triples summing to `2 pi` define
the reflection-closed local language. Every unwanted triple must be
excluded without destroying closure; local feasibility alone does not
prove global extension or aperiodicity.
[Walton reconnaissance](research/searches/walton-encoding-reconnaissance.md)
records 1,056 source-legal triples: the natural transcription and all 24
relative relabelings force regular hexagons. The 4,094 Boolean state-assignment
search leaves four angular deformations, all eliminated by equilateral
closure. [The one-block lemma](research/lemmas/walton-one-block-obstruction.md)
states the narrower equivariant compiler theorem and its exclusions.

**Reopening condition and next action:** produce a different source, a proved
extendible strict sublanguage, or a neighborhood/hierarchy-dependent encoding.
Do not repeat the completed transcription or relabeling searches. General
branching or infinitely oriented two-hexagon tilings remain outside the
conditional deterministic-state periodicity theorem.

### Nonresonant pentagon and hexagon synthesis

**Status:** both exact pairs explored so far are falsified.
[The original scaffold](research/searches/nonresonant-5-6-angle-scaffold.md)
has certified rational angles, positive exact closure, balanced corner counts,
and monohedral exclusions, but its full-edge stars omit required corners.
[The joint replacement](research/searches/joint-5-6-synthesis.md) certifies a
new positive closure and nine initial vertex rows. The October 3
[two-ended-edge review](research/reviews/joint-5-6-two-ended-review.md)
reduces all 94 ordered/chiral configurations to 12 and then zero.
Consequently the replacement also admits no plane tiling. Its proposed torus
search and periodic-chain synchronization task are superseded.

**Reopening condition and next action:** change the side partition or angle
data. Jointly enforce angle sums, distinct length classes, positive polygon
closure, consistent face chirality, and both endpoints of every shared edge.
Run the cheap endpoint filter before any global map search. A survivor must
still prove global existence and universal nonperiodicity; local feasibility
is insufficient. The rational angle constraints and classification-free
pentagon monohedral exclusion remain reusable.

## Other closed shortcuts

- [Forgetting Penrose arrows](research/counterexamples/forgetting-penrose-arrows.md)
  admits periodic rhomb tilings.
- [Convex carrier and reflected-edge obstructions](research/lemmas/convex-mark-encoding-obstructions.md)
  block faithful edge-local jigsaw encoding, while leaving nonlocal forcing open.
- [Sugimoto two-type degeneracies](research/literature/sugimoto-two-type-degeneracies.md)
  are reported by the primary source to have periodic escapes; the new
  three-type divisions permit periodic tilings when reflections are allowed.
- [Penrose-to-two-pentagon conversion](research/literature/penrose-to-two-pentagons-audit.md)
  produces Type-2 periodic monohedral tiles and supplies no converse forcing.

## Assumptions and reproduction boundary

Reflections, all rotations, partial-edge contacts, and omission of one tile
type remain permitted. No source construction may silently weaken that scope.
Ammann unrestricted forcing and its global fusion partition are unverified.
Completeness of the fifteen pentagon families is not assumed. Hexagon
classification is an imported preprint theorem; see the
[literature boundary](research/literature/2026-10-02-search.md) for sources,
queries, and scope. No new novelty claim is made by this cleanup.

## Exact verification and retained evidence

From the repository root:

```text
conda run --no-capture-output -n arisearch python3 research/searches/verify.py
```

The [runner](research/searches/verify.py) finds the checkout from its own path,
so an absolute invocation also works from another working directory. It
captures generated JSON in memory, compares parsed values with all five
retained certificates, and runs three independently implemented verifiers.
It never overwrites certificates. Assertions must remain enabled; a mismatch,
script error, or failed assertion gives a nonzero exit status.

| Finite record | Exact domain and result | Retained certificate and review |
|---|---|---|
| [Walton natural compiler](research/searches/walton_vertex_rank.py) | All 24 corner flags, 24^2 ordered contacts, and 24^3 ordered triples; 1,056 legal triples force rank 12 and one length class. Falsified compiler. | [Certificate](research/certificates/walton_vertex_rank_certificate.json), [independent verifier](research/reviews/verify_walton_vertex_rank.py), [review](research/reviews/walton-vertex-rank-review.md) |
| [Walton relabelings](research/searches/walton_relative_relabeling_rank.py) | All 24 relative shift/chirality/charge choices, each with the complete flag domain; every case collapses to regular hexagons. | [Certificate](research/certificates/walton_relative_relabeling_rank_certificate.json), [independent verifier](research/reviews/verify_walton_relative_relabeling.py), [review](research/reviews/walton-state-assignment-review.md) |
| [Walton state assignments](research/searches/walton_state_assignment_rank.py) | All 4,094 nonconstant assignments of twelve states, both alternating corner patterns; four rank-11 cases fail equilateral closure. | [Certificate](research/certificates/walton_state_assignment_rank_certificate.json), [review](research/reviews/walton-state-assignment-review.md); no standalone independent exhaustive verifier |
| [Nonresonant scaffold](research/searches/nonresonant_5_6_scaffold.py) | Fixed rational angles, all possible half-plane and 3–5-sector full-angle sums, and all 52 partitions of five length symbols; exact full-edge obstruction proves these shapes untileable. | [Certificate](research/certificates/nonresonant_5_6_scaffold_certificate.json), [report](research/searches/nonresonant-5-6-angle-scaffold.md), [review](research/reviews/nonresonant-5-6-scaffold-review.md) |
| [Joint local closure](research/searches/joint_5_6_local_verify.py) | Fixed rational angles and side partition; all full-angle rows, cyclic orders, and binary corner flips; positive exact closure and nine local rows. | [Certificate](research/certificates/joint_5_6_local_certificate.json), [report](research/searches/joint-5-6-synthesis.md) |
| [Joint endpoint obstruction](research/reviews/verify_joint_5_6_two_ended.py) | All 94 ordered/chiral configurations of that fixed pair; endpoint filtering leaves 12, then zero. These shapes admit no plane tiling. | [Review and finite result](research/reviews/joint-5-6-two-ended-review.md); regular-hexagon positive control retained |

These computations use integers and exact rational arithmetic, with rational
intervals for trigonometric closure. No solver or stochastic seed is used.
Angle multisets and length partitions are enumerated canonically; ordered-star
checks include every distinct order and reflection flag. Generator reruns repeat
the original algorithms; they are not independent implementations. The endpoint
verifier reconstructs stars and endpoints independently but depends on the
original closure certificate for distinct side lengths.

The retained checks completely enumerate their stated finite domains. Replay
has no configured timeout or memory cap. Original runtime limits and Python
versions were not recorded; do not infer them. The October 9 replay environment
is Conda `arisearch`, Python 3.12.13 on Linux x86_64, using only the standard
library. All five certificate comparisons and three independent verifiers
passed in this environment; the retained JSON files were unchanged. See the
[environment specification](.devcontainer/environment.yml) and
[lockfile](.devcontainer/conda-lock.yml). This records current replay conditions;
it does not supply the original execution record required by protocol Section
11.1. Only fixed-data verification of the joint partition is retained; its
discovery procedure is not part of the replayable evidence.

## Review coverage and restart obligations

The current proofs and their claim-specific reviews retain the stated
hypotheses, objections, repairs, and scope. Repaired or extended claims are
marked as pending independent re-review in their artifacts and review records;
the existing review verdicts describe the historical checks and do not
establish the separate re-review required by
[protocol Section 8.2](research-protocol.md#82-review-artifacts).
The elementary monohedral/torus arguments, convex edge-encoding
obstructions, and the group-theoretic one-block upgrade have no separate
whole-claim hostile-review record. Their status remains internally proved,
rather than independently certified by the script runner. The new endpoint
verifier likewise has no subsequent independent hostile review. Arrange fresh
reviews before relying on these claims as fully audited cornerstones.

No replay establishes a global mixed tiling, universal aperiodicity, or
completeness of a literature search. Blocked applications remain closed until
the reopening conditions above are met. Resume from the exact fixed data and
current falsifications, not from the discarded torus or chain-synchronization
plans for the untileable joint pair.
