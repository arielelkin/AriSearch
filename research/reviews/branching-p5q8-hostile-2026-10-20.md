# Hostile review: two branching P5/Q8 local obstructions

**Verdict: valid for the two stated exact metrics.** The pairs `(Q corner 1, reverse no)` and `(Q corner 7, reverse yes)` in the six-template report cannot tile the plane. This verdict does not cover other metrics in the continuous template families.

## Claim and assumptions checked

I reviewed `research/searches/branching-p5q8-local-obstruction-2026-10-20.md` and its Sage checker against the unrestricted problem definition and the previously reviewed six-template gate. The P angle word is `(100,110,100,120,110)`, the Q word is `(150,130,140,130,140,120,140,130)`. For both metrics, P side lengths are `(t,1,p_2,t,1)` with exact algebraic `t≈0.59767247746`, `p_2≈0.68790274191`. Q has no side of length `t`; its exact lengths are independently reconstructed in the verifier below. All side lengths are positive and the polygons close exactly.

The edge-to-edge reduction is valid. At a side-interior T junction, the opposite half-plane would require at least two angles of at least 100 degrees, exceeding 180 degrees. Two polygon corners cannot fill 360 degrees, while four exceed it. Thus every vertex in any tiling has exactly three genuine tile corners, including when reflections and initially unrestricted contacts are allowed. Since no Q side has length `t`, every P side 0 and 3 must meet a P side 0 or 3 in full.

## Independent reconstruction and attacks

The separate exact checker `research/reviews/branching-p5q8-independent-2026-10-20.sage` imports no author code. It rebuilds the algebraic side lengths from vector closure, places both reflected and unreflected P mates across each `t` edge, computes all Q corner images using a three-point isometry, and tests convex interior intersection by exact separating axes. Its placement enumeration includes every Q corner of the required angle and both orders of the two exposed P rays. A single Q image serving two vertices is checked as equality of complete vertex lists before overlap is tested.

For each metric, all twelve configurations with a reflected P mate have an endpoint with zero admissible Q placements. For the four unreflected choices `(mate at P0, mate at P3)=(0,0),(0,3),(3,0),(3,3)`, the independent Q-option counts at central P vertices `(0,1,3,4)` are respectively `(2,2,1,2)`, `(2,2,1,1)`, `(2,1,1,2)`, `(2,1,1,1)`. Each Q image at vertex 1 differs from and overlaps each Q image at vertex 3. The P mates themselves have disjoint interiors in these four branches. This gives a contradiction for every possible pair of P seams around any P tile.

The possible shared-Q escape fails by exact polygon inequality, not merely by counting corner labels. The partial-contact escape fails by the angle argument above. The species-omission escape also fails: a Q 130-degree corner cannot join two Q corners, whose angles are each at least 120 degrees; a P 100-degree corner cannot join two P corners, whose angles are each at most 120 degrees. Consequently any plane tiling would contain a P and encounter the local contradiction.

I replayed both the author and independent scripts under the repository environment. The independent script printed all eight unreflected branch checks and `PASS: both exact branching metrics are locally impossible`.

## Defects, repairs, and limits

No defect was found in the fixed-metric local obstruction. I made no edit to the author report, author checker, or discovery log. The proof depends on the exact selected Q lengths; changing free Q sides can change the overlap result. It establishes plane nonexistence for these two representatives, not an exclusion of all metrics in their template families, and not an aperiodic pair.

Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/branching-p5q8-independent-2026-10-20.sage
```
