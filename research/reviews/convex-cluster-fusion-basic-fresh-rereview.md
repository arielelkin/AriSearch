# Fresh re-review: basic convex-cluster fusion lemma

Date: 2026-10-13. Independent reviewer: sol. **Verdict: VALID** for the repaired
opening statement/proof of
[convex-cluster-fusion.md](../lemmas/convex-cluster-fusion.md).
This review covers only that basic fusion lemma, not the later separate
trivalent theorem, decorated-lift variant or application frequency assertions.

The repaired hypotheses require an exact legal whole-source patch whose
support equals a compact convex polygon, a global TILE-LEVEL partition of
one actual source tiling, an unmarked source aperiodic under unrestricted
isometries/contacts, and two distinct final congruence classes. These match
the intended unrestricted target and repair the earlier omitted obligations.
Replacing the given partition proves whole-plane existence without a
compactness or local-extension assumption.

A nonzero translational period of any admitted target tiling acts freely
on its compact tiles: a compact nonempty set cannot equal its own nonzero
translate. Selecting one exact dissection on each translation orbit and
transporting it produces a source tiling invariant under that same period.
Inserted pieces lie inside their exact macro supports and cover them; macro
interior disjointness therefore gives interior disjointness of all pieces.
Partial contacts across macro boundaries are admitted by the unmarked source.
Reflected macro placements use reflected source patches, also admitted.
A source rule disallowing those placements would not meet the hypothesis.

No recognizability, unique source dissection, preferred substitution tiling,
rank-two period or forced source labels are needed. Macro symmetry ambiguity
is handled by choosing and translating an indexed dissection along an orbit.
Tilings omitting either macro type are still covered by the lift; source
strong aperiodicity quantifies over every source tiling, including omission.
The conclusion is conditional and supplies no suitable convex cluster or
actual global partition. Application to the reviewed generic unmarked Ammann
source requires its established generic forcing domain, not nongeneric shapes.

No finite search or computational replay is needed for this elementary proof.
