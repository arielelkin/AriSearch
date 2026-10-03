# Current research state for two convex tiles

**Problem status:** unresolved. **Checkpoint:** 2026-10-03 review and cleanup.
No construction or complete impossibility theorem meets the acceptance gates.
No exact pair with established plane-tiling existence survives the recorded
searches. The most recent joint pentagon–hexagon pair is **falsified**.

Start with [the problem](research-problem.md), [the protocol](research-protocol.md),
and this log. [The artifact guide](research/README.md) gives the nondestructive
verification command and explains the reproduction boundary. The
[October 2 checkpoint](research/runs/2026-10-02-checkpoint.md) is historical;
its deadline and superseded next actions do not govern a resumed run.

## Established structural constraints

| Result | Status and scope | Proof and review |
|---|---|---|
| Monohedral escape; exclusion of triangles and quadrilaterals; rank-two side-count inequality | Internally checked. The torus inequality does not exclude rank-one periods. | [Side-count proofs](research/lemmas/side-count-and-monohedral-obstructions.md) |
| Every tileable finite convex protoset has a member with at most six sides | Adversarially reviewed, including partial contacts and T-junctions. | [Proof](research/lemmas/side-count-and-monohedral-obstructions.md), [review](research/reviews/global-side-count-review.md) |
| A hexagon paired with a polygon of more than six sides cannot be aperiodic | Reviewed; depends on the cited unrestricted monohedral hexagon classification. | [Proof](research/lemmas/hexagon-limit-and-periodicity.md), [review](research/reviews/hexagon-higher-side-review.md) |
| A tileable two-hexagon pair admits an edge-to-edge, trivalent limit tiling | Reviewed. Honeycomb combinatorics and at least one-third same-type contacts follow; periodicity does not. | [Proofs and review links](research/lemmas/hexagon-limit-and-periodicity.md) |
| Pentagon curvature and relative density constraints | Reviewed. An aperiodic (5,6) pair requires positive-density subdivision or excess-valence defects. | [Proof](research/lemmas/pentagon-curvature.md), [review](research/reviews/pentagon-curvature-review.md) |
| No angle multiset summing to pi forces edge-to-edge contacts | Proved and reviewed; unlike all-obtuse forcing, permits higher valence. | [Proof](research/lemmas/angle-nonresonance-edge-forcing.md), [review](research/reviews/angle-nonresonance-review.md) |
| All angles strictly between pi/2 and pi force edge-to-edge trivalence | Proved and reviewed; excludes all-obtuse (5,5) and aperiodic (5,6) pairs. | [Proof](research/lemmas/obtuse-edge-forcing.md), [review](research/reviews/obtuse-edge-forcing-review.md) |
| Convex fusion transfers strong aperiodicity under explicit source/partition hypotheses | Reviewed conditional lemma; no usable source partition certified. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/convex-cluster-fusion-review.md) |
| Finite convex multitile clusters cannot occur in everywhere-trivalent edge-to-edge convex tilings | Recorded proof and trivalent review. Fusion must use a source with combinatorial defects. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/trivalent-fusion-review.md) |
| Real corner/edge frequency balance | Reviewed necessary certificate only; not a global realization theorem. | [Proof](research/lemmas/frequency-balance.md), [review](research/reviews/frequency-balance-review.md) |

Thus the surviving side-count possibilities are a pair containing a pentagon,
or two hexagons. These constraints do not resolve either general case.
The old [structural index](research/lemmas/periodic-obstructions.md) retains
links to the reorganized proof files.

## Construction routes and exact remaining gaps

### Convex fusion and Ammann recomposition

**Status:** blocked application; the general fusion lemma remains valid.
The classical two-pentagon/one-hexagon source has not been certified strongly
aperiodic with reflections and unrestricted contacts. Exact final tiles,
legal vertex stars, species frequencies, and a global convex cluster partition
are also missing. [The source audit](research/reviews/ammann-convex-source-audit.md)
and [coordinate parameterization](research/searches/ammann-coordinate-parameterization.md)
retain recovered data. The conditional aggregate ratio is H:P = 1:2 phi;
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
are falsified. [The formulation](research/searches/two-obtuse-hexagon-encoding.md)
gives closure and local-language constraints.
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
[The joint replacement](research/searches/joint-5-6-restart.md) certifies a
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
- [Sugimoto two-type degeneracies](research/searches/sugimoto-two-type-degeneracies.md)
  have periodic escapes; the new three-type divisions permit periodic tilings
  when reflections are allowed.
- [Penrose-to-two-pentagon conversion](research/searches/penrose-to-two-pentagons-audit.md)
  produces Type-2 periodic monohedral tiles and supplies no converse forcing.

## Assumptions and reproduction boundary

Reflections, all rotations, partial-edge contacts, and omission of one tile
type remain permitted. No source construction may silently weaken that scope.
Ammann unrestricted forcing and its global fusion partition are unverified.
Completeness of the fifteen pentagon families is not assumed. Hexagon
classification is an imported preprint theorem; see the
[literature boundary](research/literature/2026-10-02-search.md) for sources,
queries, and scope. No new novelty claim is made by this cleanup.

All five retained JSON certificates and the standalone verifiers replay via
[the artifact guide](research/README.md). Generator reruns are distinguished
from independent verifiers. The joint partition's random seed and discovery
generator were not retained: only the fixed data and its certificates replay.
The new two-ended-edge check is independently implemented by the reviewing
agent; it has not received a separate hostile-agent review.
