# Independent Sol hostile review: Spectre corner-mean first gate

Date: 2026-10-19. Verdict: **PASS for the stated fixed-site restricted exclusion**, subject to the shape regularity clarification below. No blocking defect found. This is not a result about other site rules or the unrestricted target.

## Material inspected and replay

Inspected the complete producer, certificate, retained author JavaScript, and the exact Q(sqrt(3)) scalar and affine primitives imported from `source-decoration-hat-patch.py`. Read [Smith et al., arXiv:2305.17743v2](https://arxiv.org/html/2305.17743v2), especially Lemma 2.1, Theorem 2.2, Section 5 and Appendix A. Author artifacts were not edited.

Replayed the complete producer in its environment, replacing only its final file write in memory with a byte-for-byte assertion against the retained certificate. It passed and returned 559 supports, 758 exposed unit edges, and witnesses (71,7), (78,5), (127,6).

Additionally regenerated the frames from the producer prefix, decoded certificate vertices directly, and tested every vertex against all 558 other finite-patch bisectors, including those omitted by the producer's distance-8 cutoff. Every slack was nonnegative and exactly two bisectors were incident at every vertex. This supplemental verification uses the same audited exact scalar implementation; it is not an independent arithmetic library or a separately implemented substitution.

## Findings

**Recurrence: pass.** Compared all fourteen exact coordinates to `buildSpectreBase`, including the long-side auxiliary midpoint, the Gamma Mystic translation and 30-degree rotation, all nine ordered label lists, all seven placement-chain entries, the left-composed reflection, and the four updated key points. They agree. Recomputing the rotation when a chain increment is zero changes no matrix. The Python simultaneous dictionary update correctly reads only the previous system. There is no accidental Hat recurrence use.

**Infinite occurrence: pass with the published theorem as input.** The primary source connects the marked hierarchy to the geometric key-point construction. Every category has Delta at child index 1. A level-4 member of a genuine infinite hierarchy therefore contains the exact level-3 Delta patch, up to a common isometry. This establishes simultaneous occurrence of the three witnesses; finite growth alone is not being used to assert extension. Odd substitution depth reverses every base tile, preserving homochirality.

**Unmarked site rule: pass for the ordinary regular smooth s-curve family.** The code removes the one straight midpoint before its stabilizer test: there are 13 genuine skeleton corners and only the identity survives all pairwise-distance comparisons in both cyclic directions. Every polygon isometry acts on these corners in one of those ways. For a regular smooth centrally symmetric edge path, endpoint tangent directions are equal when expressed along the oriented chord. Consequently replacing edges by rotated copies preserves the nonstraight corner angle jumps, and creates no additional corners within an edge. An isometry of the modified shape permutes precisely these 13 corners and hence must be the identity. The auxiliary midpoint is recoverable as the midpoint between its neighboring skeleton corners. Thus `g c` is well-defined even when arbitrary planar isometries are allowed.

Clarification, not a numerical failure: the phrase “every such X” should retain the assumption that the original nonstraight corners remain recognizable. The producer checks the skeleton stabilizer, not arbitrary boundary paths. Interpret “smooth” as a regular smooth embedded path with the stated preserved corner template, or explicitly choose a sufficiently small regular s-curve from Lemma 2.1. This supplies actual genuine Spectres and is enough for the claimed restricted exclusion. I did not certify every possible pathological parameterized smooth path with vanishing endpoint derivatives.

**Delone bounds: pass.** Exact interior membership, edge-distance greater than 1/4 and vertex-distance less than 5/2 imply an interior disk and a containing disk for each skeleton. The former gives separation at least 1/2; the latter gives covering radius at most 5/2 in a skeleton plane tiling. These estimates use the skeleton supports at exactly the same placements as the smooth source, so no containing-radius assertion about the modified supports is needed.

**Complete-neighbor argument: pass.** Oppositely oriented full-edge cancellations, together with the genuine face-to-face source occurrence, identify all possible union boundary segments. A path from the selected interior point out of the union must meet an exposed segment. The exact greater-than-13 margin therefore puts its radius-13 disk in the union, even if the finite patch has holes elsewhere. A hypothetical exterior support with site within 8 would lie wholly inside radius 10.5 and would overlap the patch interior, a contradiction. More directly, the exterior site itself is an interior point of its skeleton support and cannot lie in the patch interior. No exterior bisector can cut a cell contained in radius 4. The stated margin is conservative and sufficient.

**Exact Voronoi certification: pass.** Bisector equations in coordinates relative to the witness are correct. Nonsingular adjacent-line intersections lie exactly on their two incident bisectors. Strict other slacks, distinct side labels and positive turns certify actual nonzero polygon sides; the feasible cyclic intersections give the full bounded halfplane intersection. Vertex radius less than 4 extends to the whole convex polygon. Any omitted site at distance greater than 8 is strictly farther at every point in that polygon, by the triangle inequality. Exact two-bisector incidence rules out higher-valence degeneracies at these vertices. SciPy supplies candidate ordering only; its floating-point decisions do not establish acceptance.

Supplemental all-site checks gave the following incidences, in stored vertex order:

| index | sides | incident neighbor pairs |
| --- | --- | --- |
| 71 | 7 | (78,79), (72,79), (72,267), (267,268), (268,269), (85,269), (78,85) |
| 78 | 5 | (71,85), (85,138), (77,138), (77,79), (71,79) |
| 127 | 6 | (128,527), (527,528), (528,529), (515,529), (126,515), (126,128) |

For orientation only, floating approximations to the minimum exposed-boundary distances are 15.11624, 14.40871 and 13.52109 respectively. Acceptance uses the exact greater-than-13 predicates, not these approximations.

## Exact scope

These witnesses prove at least three planar congruence classes of Voronoi cells for this transported fourteen-point mean in a genuine infinite smooth Spectre source tiling. Side counts 7, 5 and 6 are sufficient, including under reflections. The result excludes this one rule from an only-two-class proposal. It establishes no classification of all its cells, no exclusion of other site rules, no decoder, and no aperiodicity statement about arbitrary tilings assembled from the output cells. The paper's geometric realization and hierarchy theorems are trusted mathematical inputs; their computer-assisted proof was not independently re-proved here.
