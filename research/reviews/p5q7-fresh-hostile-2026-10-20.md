# Hostile review: tangential P5/Q7 fixed trial

## Scope and replay

I independently inspected `research/searches/p5q7-fresh-build-2026-10-20.sage` and replayed it with

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5q7-fresh-build-2026-10-20.sage
```

The program exits successfully. It verifies exact cyclotomic closure, strict convexity, and pairwise interior disjointness of the displayed three-tile *finite* patch. The printed side lengths are numerical renderings of exact elements; the assertions use `AA` in the distinguished embedding. This review establishes a stronger obstruction than the producer's proposed global counting argument: **this fixed pair admits no plane tiling**. Consequently its finite patch cannot extend indefinitely.

## Endpoint lemma for unrestricted contacts

Suppose two tiles have a common boundary ray from a vertex, and one incident side has strictly smaller length. At the endpoint of that shorter side, if the longer side continues through the point, its tile contributes a straight angle of 180 degrees. The shorter tile contributes the angle at its far endpoint. The remaining sector must be filled by one or more tile corners. Here every tile angle is at least 80 degrees, so a remaining sector below 80 degrees is impossible. This argument allows reflections, rotations, and partial-edge contacts; it does not assume edge-to-edge placement.

The exact script inequalities give

| Tile corner | Incident side lengths, approximately | Far-end angles |
| --- | ---: | --- |
| P80 | 1.892, 1.658 | 110, 130 |
| P100 | 1.539, 1.416 | 110, 120 |
| P120 | 1.416, 1.044 | 100, 130 |
| Q120 | 3.441, 3.441 | 130, 130 |

The inequalities needed below are strict and exact: each P100 side is shorter than each P80 side; each P80 side is shorter than each Q120 side; and both P120 sides are shorter than each P80 side.

## Exhaustion of a P80 vertex

Any plane tiling containing P must complete its 80-degree corner. With all angles at least 80 degrees, the only all-corner stars containing 80 degrees are `(80,80,80,120)` and `(80,80,100,100)`. The only star using a straight side is `(80,100,180)`.

1. In `(80,100,180)`, the P80 and P100 sectors share a ray. Every P100 incident side ends strictly inside the corresponding P80 side. Its far angle is 110 or 120 degrees, leaving 70 or 60 degrees beside the straight P80 edge. Both are impossible. **The proposed forced T pairing fails at its first endpoint.**
2. Every cyclic order of `(80,80,100,100)` has a P80/P100 adjacency. The same short P100 side gives the identical impossible 70- or 60-degree remainder.
3. In `(80,80,80,120)`, the 120-degree corner is either P120 or Q120. If Q120, the adjacent P80 side ends first along the Q side; its far angle is 110 or 130 degrees, leaving 70 or 50 degrees. If P120, its side leading to P130 has length about 1.044, strictly shorter than either incident P80 side. It ends inside that side, leaving `180−130=50` degrees. All cyclic orders fail.

Thus **no P80 corner can occur**, so no tiling can contain P.

## Q-only exclusion

The Q angles are 120 and 130 degrees. A Q130 corner cannot be completed by a straight side, since this would require another 50-degree corner. Three or more Q corners total at least `130+120+120=370` degrees. Hence Q cannot tile the plane alone. Together with the P80 obstruction, the fixed pair is plane-nontilable.

## Correction to proposed count and Rao gate

The producer's printed `P-only Rao hits: []` is a useful family filter, but the repository's literature audit (`research/literature/2026-10-02-search.md`, lines 72–76) explicitly records that the 15-family list has not been definitively established as exhaustive for unrestricted convex-pentagon tilings. Zero hits cannot by itself prove P-only plane non-tilability here. The global 130-degree density count is unnecessary after the local P80 obstruction. If used separately, its naïve finite-torus form only addresses doubly periodic tilings; a one-period strip and sparse Q occurrence require additional argument.

## Disposition

Stop this exact fixed-metric pair. Preserve the finite patch as a nonoverlap certificate and the P80 endpoint obstruction as the decisive exclusion. It supplies neither a plane tiling nor an aperiodic pair under the stated objective.
