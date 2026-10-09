# Hostile review: defect-free limit for two hexagons

**Re-review status:** this record includes repairs or extensions made during
review. A separate independent review of the resulting version is not
established by the retained record and remains pending under
[protocol Section 8.2](../../research-protocol.md#82-review-artifacts).

**Artifact reviewed:** [hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md).

**Date:** 2026-10-02
**Verdict:** **Valid after replacing a heuristic slack argument by an exact
finite-patch identity.**

## Exact audit identity

For a selected hexagon patch let \(B\) be its boundary-edge count,
\(I=2E-B\) its face-edge incidence count,
\(\delta=I-6N\), and
\(D=\sum_{v\text{ interior}}(\deg v-3)\).  If \(V_b\) is the boundary vertex
count, \(q\) their total degree, and \(H\) the hole count, Euler and degree
counting give

\[
 \delta+2D=6V_b-2q-B-6+6H.
\]

The established boundary estimates imply \(\delta+D=O(R)\).  This identity
is essential; merely writing \(E=3N+O(R)\) does not separately control both
types of defect.

## Issues checked

* \(\delta\) is the sum of \(k-1\) over native sides split into \(k\) graph
  pieces, so it detects partial contacts and T-junctions.
* \(D\) detects all interior vertices of valence above three.
* A separated-grid count supplies arbitrarily large defect-free disks even
  when defects form long barriers.
* Compactness needs no finite-local-complexity assumption.
* Positive minimum native-side length prevents defect-free vertices from
  collapsing together in the limit.
* The limit may use only one of the two types.  The theorem therefore says
  “admitted by the pair,” not that both types survive.

## Non-consequence

An edge-to-edge trivalent tiling by two convex hexagons has not been proved
periodic.  The limit theorem alone does not eliminate the \((6,6)\) case.
