# Independent hostile review: uniform unavoidable-type density

Date: 2026-10-10. Reviewer: root agent, independent of the structural-audit
agent that formulated and wrote the claim.

## Exact claim

[The lemma](../lemmas/two-type-uniform-density.md) asserts that for a finite
fixed convex protoset P admitting a tiling, if a subset S cannot tile the
plane, its complement M is uniformly relatively dense in every P-tiling.
It gives count and covered-area lower bounds with r=L+D, including limits
of tilings with continuous orientations and partial contacts.

## Assumptions checked

Fixed finite shapes have positive area, finite diameter and a uniform
protected interior anchor disk. Arbitrary rotations/reflections are compact
in O(2). No finite local complexity or edge-to-edge hypothesis is introduced.
Non-tileability of S uses the original unrestricted convention. It is an
explicit hypothesis, not inferred from failure of finite searches. P-tileability
implies M is nonempty, so its minimum area is defined.

## Attacks and verification

* Radial enumeration: the jth anchor is uniformly bounded because covering
  a sufficiently large disk requires more than j fixed-area tiles with
  anchors in a bounded enlargement. Tie breaking need not persist; diagonal
  subsequences still give actual placements at every fixed index.
* Lost coverage: every approximating tile covering a fixed point has an
  anchor in one fixed disk, hence its index is in a uniformly bounded prefix.
  A fixed index covers the point along an infinite subsequence; membership
  in the closed limit tile persists. This covers each point without any
  illicit uncountable common-subsequence extraction.
* Duplicate occurrences and overlaps: the protected anchor disks give
  uniform 2rho separation, while an interior overlap is open and persists
  under convergence. Distinct indices cannot silently merge.
* Varying tilings and centers: negating the uniform quantifier permits a
  different tiling for each k. Translation and compactness still produce an
  S-only whole-plane tiling. A limit M anchor would eventually lie in the
  forbidden expanding disk.
* Boundary-count convention: M anchors in the closed square always have
  interior disks meeting its open interior. Thus the anchor cover proves
  the claimed interior-meeting tile-count lower bound even at the boundary.
* Double counting: one radius-r disk is counted for each distinct M anchor;
  area subadditivity requires no disjointness of these covering disks.
* Covered-area bound: using anchors in Q_(R-D) places the whole tiles in
  Q_R. Their disjoint interiors and positive minimum area justify summing
  areas. The max expression correctly handles small R.
* Frequencies: positive uniform lower limits do not imply existence of a
  frequency or specify a computable L. The lemma explicitly avoids both.

## Defects, repairs, remaining uncertainty

No defect or repair found in the general theorem. The hexagon corollary
correctly isolates its dependence on an unrestricted monohedral
classification; that external theorem is checked separately in the
structural resumption review. No computation or numerical decisions enter
this lemma. There is no claim of novelty.

**Verdict: VALID** for the exact quantified theorem and bounds. It supplies
strictly positive type marginals in any subsequently extracted frequency
system when every complementary subset is nontileable. It neither constructs
a tiling nor makes a branching adjacency language periodic.
