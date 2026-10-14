# Bounded construction cycle checkpoint audit

Date: 2026-10-14. Problem status: **unresolved**. The initial reviewed checkpoint
`99833f7` was pushed before this cycle. Three Sol agents completed the authorized
P5/Q14 experiment, nonconvex-parent construction and applied counterexample
checks, then independently reviewed one another's results. The finite domains
are closed; no larger patch or periodic quotient search is included.

## Retained results and restart boundaries

- [Exact P5/Q14 experiment](../searches/contact-pentagon-5pi7-q14-exact.md):
  all 3003 binary masks reduce to 35 closed words, 14 ring-bearing words,
  896 native rings and 364 disjoint mandatory-dimer completions. An exact
  contact audit rejects 336 by forbidden T contacts. The 28 remaining
  indexed states are four each for seven rotations of one Q shape. The
  [four displayed states](../figures/contact-pentagon-5pi7-q14-dimer-patches.svg)
  are finite necessary local data. Every state fails the one-Q translation-orbit
  model. Plane extension and periodic tilings with differently oriented Q copies
  remain open. The original-domain, one-Q and palette results have fresh
  independent reviews and exact checkers linked from the experiment note.
- [Nonconvex-parent perimeter theorem](../lemmas/nonconvex-parent-hexagon-perimeter-bound.md):
  a simple parent with p genuine corners, tiled by convex atoms with at least
  six sides and maximum side L, has perimeter at most (2p-6)L. This excludes
  an iterable expansive similarity hierarchy with finitely many such simple
  polygonal parents. The corrected proof includes flat child incidences at
  reflex parent corners and has a [fresh VALID review](nonconvex-parent-hexagon-perimeter-bound-review.md).
  It is not an unrestricted impossibility theorem for two hexagons.
- [Bounded construction cycle](../searches/nonconvex-parent-construction-2026-10-14.md):
  the 1430-signature binary-hexagon grid has no positive distinct closed metric.
  A single exact pentagon/hexagon repair supplies eight nonconvex mixed whole-edge
  parents, all excluded by endpoint angles before cover expansion. A separate
  216-branch partial-contact completion test retains 20 local P-only patches,
  including six host-switch controls. P alone is excluded by an existing reviewed
  theorem. A future construction needs a genuinely mixed partial-contact parent.
  The independent checker verifies branch-key coverage and all 20 positives;
  the 196 negative classifications also depend on the exhaustive producer and
  its source audit, not a second full independent classification.
- [Applied adversary](../searches/construction-adversary-2026-10-14.md):
  exact overlap, native alias/reflection, omission and periodic-witness checks
  are applied to both construction tracks. Positive and damaged-witness controls
  pass. Failed finite omission searches retain NO_WITNESS_IN_DOMAIN status.
  The [fresh API/one-Q review](construction-adversary-2026-10-14-review.md)
  validates the sufficient periodic-witness test and its stated restrictions.

## Verification and freshness

The pinned environment and the original 53 certificate pairs plus 277 verifiers
passed the [full 330-check replay](checkpoint-full-replay-2026-10-14.txt) before
this cycle. Dependencies and original proof artifacts were not changed.

All nine new registry entries passed: four deterministic certificate replays and
five independent verifiers. The P5/Q14 author certificate was replayed separately
through the registry; the [remaining eight-check transcript](construction-cycle-targeted-replay-2026-10-14.txt)
records three certificate replays and five verifiers, with all six new retained
certificates unchanged. The registry now contains 57 certificate pairs and 282
verifiers, 339 unique checks. A fresh full 339-check replay was not run.

All 11 changed/new Python files parse, all six new JSON certificates load, and
registry targets and argument keys are valid. The diagnostic SVG is generated
from exact retained placements and was visually inspected; it is not a proof
verifier. Current source notes and the discovery log distinguish completed
checks from remaining global obligations. Historical review defects remain in
review records; superseded pending wording and the incorrect per-word summary
were removed from the current source notes.

The highest-value P5/Q14 restart is an exact transition/compatibility analysis
between differently oriented Q neighborhoods. Construction work must change the
contact mechanism, respecting the all-hexagon perimeter obstruction and the
failure of this repair's mixed full-native seams. Neither branch currently
establishes a full-plane tiling or aperiodicity.
