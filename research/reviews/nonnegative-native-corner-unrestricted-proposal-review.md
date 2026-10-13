# Independent attack on unrestricted zero-score corner-potential proposal

Date: 2026-10-13. Reviewer: sol, independent of root proposal.
**Verdict: VALID** for additive native-corner weights with flat host score0.
The complete independent derivation is retained in
[the extracted proof](../lemmas/nonnegative-native-corner-potential-unrestricted-zero-score-limit.md).

Attacks checked: lost corners in the limit; corners of two tiles merging;
two approximating copies becoming one tile; label ambiguity at polygon
symmetries; host sectors becoming native corners; lack of uniform vertex
separation; new high-valence stars; and incomplete corner groups near the
isolating disk boundary. None invalidates the additive assertion.

Fixed geometry, positive tile area and bounded diameter give finitely many
tiles/corners in every bounded window. An isolated limit native-vertex disk
therefore contains exactly the approximating corners converging to that
vertex, for sufficiently late indexed approximants. Every actual approximating
vertex group inside it is complete and has zero score. Hosts contribute0.
Summing all groups equals the limiting corner score even if those groups
merge. Interior overlap excludes duplicate limiting tile occurrences. Carrying
indexed isometries preserves asymmetric weights under polygon symmetries.

The hypothesis must quantify over ALL ACTUAL COMPLETE corner stars of the
original field, including partial contacts and reflected placements. Native
corner valence is bounded by the positive minimum angle, so a finite positive
score gap exists. The boundary-weight and disjoint-disk arguments are valid
without global frequencies or finite local complexity.

Only additive score0 persists. A finite star language, trivalence or whole
contacts need not persist when vertices merge; none is concluded. A weight
on host sectors depending on their incidence would require a different proof.
No pentagon candidate is accepted by this theorem alone; nonnegativity and
a useful zero-core classification remain independent application obligations.

The extracted generalized artifact should receive a fresh hostile review by
an agent other than its author before being designated a stable general tool.
No computation was required. Related sparse-corner arguments in Rao Section2
are explicitly acknowledged; no novelty claim is made.
