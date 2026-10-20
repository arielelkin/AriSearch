# Hostile review: two pentagon angle gates

Verdict: **valid** for both narrow statements. No mathematical repair required.

Reviewed: `research/lemmas/pentagon-hexagon-100-140-angle-obstruction-2026-10-19.md` and `research/lemmas/pentagon-regular-hexagon-corner-expansion-2026-10-19.md`, against the unrestricted definitions in `research-problem.md`.

## Exact geometry and local possibilities

The chosen cyclotomic root has the stated minimal polynomial and its argument fixes its embedding. The cyclic normal gaps sum to 360 degrees and lie strictly between zero and 180 degrees. Intersections of successive unit-circle tangents therefore give bounded polygons with positive edges, all support inequalities satisfied, and the stated strict interior angles. The pentagon and hexagon are distinct congruence classes. The retained Sage checker independently verifies these support and strict-turn facts using real algebraic arithmetic.

The local-finiteness argument applies to arbitrary reflections and arbitrary contacts: every tile meeting a fixed compact set lies in a bounded enlargement and contains a uniformly positive disk with disjoint interior. At a tile vertex, no other tile can contain the point in its interior. Thus the sector equation includes every possible contribution, including straight sectors from partial-edge contacts. At most one straight sector can accompany a genuine corner. The equations 5a+7b+9s=18 and 5a+6b+7c+9s=18 have respectively no solutions with a+b positive, and precisely (a,b,c,s)=(0,3,0,0),(1,1,1,0). The domains in the retained scripts include all possibilities because each positive term is at least 5. In particular, no edge-to-edge assumption has been smuggled into either proof.

## Attempted graph counterexamples

I checked directed cycles, repeated vertices across generations, merging branches, self-arrows, and zero-density defects. Each pentagon has exactly four outgoing arrows and exactly one incoming arrow. A self-arrow is impossible because its 100- and 140-degree corners are distinct points. Two sources cannot share a target, since the target has a unique 140-degree corner and that star contains only one 100-degree corner. Consequently the outgoing-neighbor map multiplies the size of every finite vertex set by four, even when its image overlaps that set or an earlier generation. No assertion that different generations are disjoint is needed. Directed cycles therefore do not defeat |S_n|=4^n.

The centroid is in its convex pentagon. A shared vertex bounds centroid displacement by 2D. Every tile in S_n is contained in the radius-(2n+1)D disk about the initial centroid. The tiles within that single generation are distinct and have disjoint interiors, so summing their areas gives the stated bound. Overlap between generations is irrelevant. Positive area and finite D make exponential versus quadratic growth contradictory. This excludes even isolated or zero-density pentagon occurrences.

## Scope and redundancy

The regular-hexagon palette was already disqualified as an aperiodic candidate by omission of the pentagon: a regular hexagon alone tiles periodically. The branching proof adds the stronger structural conclusion that pentagons cannot occur at all. It must not be counted as a newly killed viable candidate or as progress proving the unrestricted impossibility theorem. The second palette is a genuine no-tiling angle obstruction, still confined to its stated angle family. Neither review establishes novelty; no external literature assertion is used.

## Verification and remaining uncertainty

Replayed the retained Sage exact-geometry/local-equation checker and Python complete-star checker using the prescribed environment. These computations check finite algebraic geometry and finite sector equations; the infinite conclusion rests on the complete written growth argument audited above. No unresolved mathematical defect was found. No changes were made to either lemma or to the discovery log.
