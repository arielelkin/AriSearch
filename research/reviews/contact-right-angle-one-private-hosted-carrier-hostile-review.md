# Independent hosted one-private periodic-carrier audit

Date: 2026-10-13. Reviewer: root, independently of the contact construction.
Verdict: VALID. The exact proposed ray has a legal rank-two periodic escape.

## Reviewed claim and assumptions

Reviewed [construction](../lemmas/contact-structure-one-private-x2u-periodic-carrier.md)
and frozen [coordinate certificate](../certificates/hosted-oneprivate-x2u-periodic-carrier.json).
The claim concerns one exact algebraic metric ray and ordinary similarities,
not every one-private partner, not every admitted filling, and not an
aperiodic construction. All copies are unmarked ordinary isometries and
partial contacts are allowed. No claim that the necessary finite rings
extend is used.

## Independent checks and attacks

The new [checker](contact-right-angle-one-private-hosted-carrier-check.py)
imports neither the producer nor the local-ring scripts. It reconstructs
both canonical shapes directly from the stated metric formula and native
edge vectors in the exact quartic field with its verified isolating interval.
It checks all positive distinct lengths, the exact one-private mask,
strict supporting halfplane inequalities, signs and squared native-angle
identities, and full cyclic pairwise-distance congruence for each of the
six P and two Q representatives.

It normalizes actual polygon orientations, independently splits unit edges
at their exact midpoints, and regenerates all reversed atomic-edge partners
by unrestricted integral lattice-coordinate calculation. It uses no retained
partner table to select a match and no finite translation-radius search.
All 56 atomic segments have exactly one partner, yielding 28 undirected
pairs; the regenerated map equals the retained table and is an involution.
The lattice determinant is nonzero and the exact total positive polygon
area equals its absolute value. The final checker passed in the locked
environment.

These tests specifically attack reflected vertex ordering, accidental
third shapes, gap or overlap hidden by a drawing, truncated pairing radius,
and forgetting to split one side of a flat contact. None remains.

## Entire-plane implication

The complete reversed-boundary identities cancel the distributional
derivative of the periodic covering multiplicity. Each representative is
an actual convex positive-area polygon, so multiplicity is a nonnegative
integer function; the rank-two lattice makes the sum locally finite.
Zero derivative on the connected plane implies a constant almost everywhere.
Its mean is exactly one. Positive-area interior overlaps and open gaps
are therefore impossible. Local finiteness makes the union of supports
closed, so a missing boundary point would have an open neighborhood missing
from that union, also impossible. This proves disjoint interiors and whole
plane coverage, including all boundaries. Splitting edges in the verifier
merely accounts for ordinary partial contacts and introduces no marking rule.

No repair to the mathematical construction was needed. The earlier finite
ring checks are unnecessary dependencies for the frozen witness. The
remaining uncertainty is about other pairs, not this periodic carrier.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-right-angle-one-private-hosted-carrier-check.py
