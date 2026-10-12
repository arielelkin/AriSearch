# Hostile review: Ammann coordinate and count calculation

**Re-review status:** this record includes repairs or extensions made during
review. A separate independent review of the resulting version is not
established by the retained record and remains pending under
[protocol Section 8.2](../../research-protocol.md#82-review-artifacts).

**Artifact reviewed:** [ammann-coordinate-parameterization.md](../lemmas/ammann-coordinate-parameterization.md).

**Date:** 2026-10-02
**Verdict:** Coordinate formulas valid as a multibranch parameterization;
aggregate frequency algebra valid only under the stated edge-to-edge,
native-edge, boundary, and van-Hove hypotheses.

**Historical scope update (2026-10-12):** exact branches, final prototiles and
a generic forcing atlas now appear in the
[later reconstruction](../lemmas/ammann-two-class-reconstruction.md) and
[reviewed forcing proof](../lemmas/ammann-forcing-aperiodicity.md). The findings
below describe the earlier distance-only artifact; they do not assert that
these data are still missing. Its separate conditional count review gate
remains as stated above.

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
