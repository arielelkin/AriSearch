# Hostile review: Ammann coordinate and count calculation

**Artifact reviewed:** [ammann-coordinate-parameterization.md](../searches/ammann-coordinate-parameterization.md).

**Date:** 2026-10-02
**Verdict:** Coordinate formulas valid as a multibranch parameterization;
aggregate frequency algebra valid only under the stated edge-to-edge,
native-edge, boundary, and van-Hove hypotheses.

## Corrections imposed

* The distance constraints generally yield two circle-intersection branches,
  not unique points \(K,L\).  Exact inside/incidence tests must choose them.
* The free point \(J\) is not selected by the published unequal-length
  condition, so no exact prototile triple has yet been defined.
* Frequency statements are asymptotic; boundary errors cannot be dropped in
  finite Penrose patches.
* The face-degree identity requires every marking-graph edge to be one whole
  native pentagon/hexagon side.  T-junctions or suppressed straight vertices
  invalidate it.
* The aggregate identity \(P=2T\) contains no information about how the two
  pentagon congruence classes split.  Equal splitting remains unproved.

## Algebra checks

Subtracting \(|K|^2=a^2\) and \(|K-q|^2=b^2\) gives
\(K\cdot q=(a^2-b^2+1)/2\).  Expanding the thin-rhomb coordinates yields
\(1+\cos36^\circ-J\cdot d\).  Translating the same calculation by \(F\) for
\(L\) yields \(1+\cos36^\circ-x\).  Both square-root branches in the
orthogonal coordinate were retained.

The conditional equations \(h+p=t+2T\) and
\(6h+5p=6t+10T\) solve to \(h=t,p=2T\), as recorded.
