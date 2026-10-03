# Hostile review: hexagon plus higher-sided polygon

**Artifact reviewed:** [hexagon-limit-and-periodicity.md](../lemmas/hexagon-limit-and-periodicity.md).

**Date:** 2026-10-02
**Claim:** A convex hexagon paired with a convex \(n\)-gon, \(n>6\), cannot
be an aperiodic pair.
**Verdict:** **Valid, using the named unrestricted convex-hexagon
classification.**

## Attacks and repairs

* Merely saying the higher-sided tiles have zero density does not produce a
  large hexagon-only disk.  The repaired proof uses a grid with
  \(R\gg L^2\): there are quadratically many candidate radius-\(L\) disks
  but only \(O(R)\) higher-tile occurrences, each affecting only uniformly
  many separated candidates.
* Sparse higher-sided tiles could form long barriers.  The grid count is
  insensitive to their arrangement and still provides a clean disk.
* The tiling need not have finite local complexity.  Compactness instead
  follows from uniform local tile-count bounds, compactness of \(O(2)\), and
  diagonal extraction of placements.  Coverage and nonoverlap are closed
  under this convergence.
* The side-count estimate is uniform for translated squares because its
  constants depend only on the finite protoset, not the square centre.
* The final step requires the unrestricted monohedral convex-hexagon
  classification, not merely an edge-to-edge conditional theorem.  Zhu,
  Wang, and Yan, arXiv:2508.01404v2 (2026), supply the full necessity proof
  with partial contacts and flips; standard Reinhardt-family constructions
  supply periodic witnesses.

## Scope

The result says nothing about two hexagons or a pentagon paired with any
higher polygon.  It does not assume the original mixed tiling is periodic,
repetitive, or edge-to-edge.
