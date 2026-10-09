# Hostile review: deterministic hexagon-state periodicity

**Re-review status:** this record includes repairs or extensions made during
review. A separate independent review of the resulting version is not
established by the retained record and remains pending under
[protocol Section 8.2](../../research-protocol.md#82-review-artifacts).

**Artifact reviewed:** [hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md).

**Date:** 2026-10-02
**Verdict:** **Valid after strengthening “state” and globally coordinating
the honeycomb directions.**

The reviewed proof uses the honeycomb coordinatization already established
in [research/lemmas/hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md).  A full state must record tile
type, absolute linear orientation/reflection, and enough side/vertex indexing
to resolve symmetries.  It must determine relative neighbour displacement,
not just a symbolic neighbour label.  Full edge-to-edge coincidence then
makes this a finite discrete datum under the theorem's hypothesis.

Opposite transitions are inverse permutations, and path consistency makes
the two lattice generators commute on the reachable orbit (not necessarily
on unused formal states).  The finite orbit has a finite-index stabilizer.
State-periodic displacement cocycles integrate to a translation homomorphism
from that rank-two subgroup.  It is injective by disjoint tile interiors and
has discrete image by local finiteness, hence contains two noncollinear
periods.

The loose claim fails if directions mean only local side numbers, if states
omit orientation or displacement data, or if matches branch.  General finite
two-dimensional shifts can be strongly aperiodic, so finiteness alone is not
enough.
