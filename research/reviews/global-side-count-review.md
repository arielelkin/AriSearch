# Hostile review: global side-count obstruction

**Re-review status:** this record includes repairs or extensions made during
review. A separate independent review of the resulting version is not
established by the retained record and remains pending under
[protocol Section 8.2](../../research-protocol.md#82-review-artifacts).

**Artifact reviewed:** [side-count-and-monohedral-obstructions.md](../lemmas/side-count-and-monohedral-obstructions.md).

**Date:** 2026-10-02
**Reviewed claim:** A finite set of convex polygons, each with at least seven
sides, cannot tile the plane, even with non-edge-to-edge contacts.
**Verdict:** **Valid after repairs.**  The corrected proof is in
[research/lemmas/side-count-and-monohedral-obstructions.md](../lemmas/side-count-and-monohedral-obstructions.md).

## Defects attacked and repairs required

1. A square-window tile union need not be a disk.  The proof now retains the
   number of holes in Euler's formula and bounds it by boundary complexity.
2. Bounding boundary tiles does not automatically bound boundary graph
   edges when T-junctions are allowed.  The proof now obtains a uniform
   neighbour bound from maximum diameter and minimum area, then uses the
   finite side-count bound to control contact endpoints per polygon pair.
3. Boundary localization can fail with an ambiguous tile-selection rule.
   The proof selects precisely the tiles whose interiors meet the interior
   of the square.  Across a patch boundary edge inside the square, the
   opposite tile would then also have been selected.
4. Local finiteness was not assumed.  It is derived from bounded diameter,
   positive minimum area, and disjoint interiors.
5. Native sides and planarized edges were kept distinct.  Subdivision can
   only increase face-edge incidences, giving the inequality needed rather
   than an unjustified equality.

## Checks performed

The review separately checked partial-edge contacts, isolated point
contacts, native convex corners, boundary vertices, holes, and the growth
rates \(B=O(R)\) and \(N=\Omega(R^2)\).  No edge-to-edge assumption is used.

## Remaining uncertainty

None for the stated finite-protoset theorem.  It does not constrain a pair
where one polygon has at most six sides, and therefore does not resolve the
main problem.
