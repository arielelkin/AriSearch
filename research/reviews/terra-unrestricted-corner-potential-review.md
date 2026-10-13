# Hostile review: unrestricted additive zero-score translated limit

Date: 2026-10-13. Reviewer: terra, independent of author sol and root proposal.
Claim reviewed: research/lemmas/nonnegative-native-corner-potential-unrestricted-zero-score-limit.md.
Verdict: VALID under actual nonnegative native-score hypotheses.
No downstream angle/count application is reviewed here.

## Exact assumptions checked

Finitely many fixed genuine convex shapes of positive area; native collinear
subdivisions removed; indexed native-corner weights sum to zero per shape;
EVERY complete actual native vertex score of the source tiling is nonnegative.
Flat hosts contribute zero. Original reflections, partial contacts and arbitrary
valences are allowed. Indexed isometries are retained through extraction.

## Counterexample attacks

1. Arbitrary real weights could have positive scores tending to zero: impossible
   because positive minimum native angle bounds native-corner multiplicity at
   every vertex; finitely many indexed slots then give finitely many score sums.
2. Flat hosts might introduce unbounded uncounted score: they contribute zero.
   Area packing bounds all incident tiles anyway, and each host native corner
   is counted at its own geometric position.
3. Negative boundary sums might mask quadratic positive vertices: incomplete
   vertices have selected/unselected tile centres within2D, hence all relevant
   selected tiles lie in a fixed-width boundary strip. Their absolute native
   weight is uniformly O(R), so nonnegative complete scores remain O(R).
4. Sparse vertices without arbitrarily large clean disks: the uniform translated
   O(R) bound counts bad points against a quadratic grid of disjoint disks.
   This gives the required clean translates without any density/FLC premise.
5. Vertex coalescence could change a zero score: the author correctly does not
   preserve a star language. In a small disk containing one LIMIT native vertex,
   tracked finite native occurrences are in bijection with all occurrences at
   that limit vertex. Entire approximating vertex groups have zero score;
   additivity therefore preserves zero through every coalescence.
6. A partial-contact host could become native in the limit: its native corner
   occurrence must also converge into the small disk, and its weight is counted
   in its whole approximating vertex group. The flat-host-zero convention does
   not discard the genuine native occurrence in that group.
7. Untracked tiles could add a limit vertex corner: bounded diameter and uniform
   local area packing let a larger compact window track every tile that can
   meet the small disk. Extra entering tiles cannot evade that finite list.
8. The small-disk groups might omit other native corners at the same position:
   inclusion is by geometric position, so every native occurrence there is
   included. All other limiting corner positions stay outside2rho; for late
   approximants no boundary crossing or partial star truncation is possible.
9. Coverage or duplicate occurrences might fail under compactness: closed
   polygons and finite local occupancy preserve point coverage. Coincident
   limit tiles or positive interior overlap would persist for sufficiently
   close approximants, contradicting source interior-disjointness.
10. Shape symmetries could change corner weights after extraction: finite
    indexed isometries remain part of the convergent placement data. Native
    labels are never freely reassigned at the limit.

## Defects, repairs and limitations

No consequential defect found; no repair required. No vertex-separation claim
is needed or imported. Whole-side contacts, trivalence and finite star-language
persistence are correctly NOT concluded. The argument gives existence of one
zero-score translated limit, allows species disappearance and proves no
periodicity by itself. Nonnegative scores checked only on a desired trivalent
language would not authorize use on an unrestricted source field; actual
partial/hosted and higher-valence configurations must meet the hypothesis.
The proof is analytic; no computational test or external classification is
required for this transfer statement.
