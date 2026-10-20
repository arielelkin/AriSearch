# Rational P5/P5 half-side contact experiment

Date: 2026-10-20. Status: **exact local patch; rejected as a forcing lead**. This is not an infinite tiling or an aperiodicity claim.

## Deduplication before construction

I checked the [shape-first audit](shape-first-dedup-audit-2026-10-20.md), the Y-interface pair, the Ammann bipartite resection, the Cairo pairs, pentagrid U/V/W, and the two earlier P5/P5 long-edge tracks. The present pair has rational integer vertices, no source-tile partition or symbolic source, and an exact **two-Q half-side attachment** to one P. Its side-squared words `(25,5,18,20,10)` and `(25,5,17,20,5)` and angle cosines derived from the dot words below differ from all those exact fixtures; in particular Q has two acute angles and P has none, so this is neither the 90/120 Cairo case, the pentagrid angle words, nor the `(60,60,150,120,150)` long-edge family. The mechanism is also different from the prior A/A/B T contact: the proposed split is P/Q/Q and uses two congruent halves of a P side. This is a new *fixture*, not a novelty claim about the literature.

## Exact fixture and checks

In counterclockwise order, set

```
P = ((0,0),(5,0),(6,2),(3,5),(-1,3))
Q = ((0,0),(5,0),(6,2),(2,3),(-2,1)).
```

Consecutive oriented turn determinants are `P=(15,10,9,18,14)` and `Q=(5,10,9,12,8)`, all positive. Twice their areas are 48 and 32, so they are strictly convex and incongruent. Squared native side lengths are as above. At each vertex, the dot product of the two rays pointing to neighboring vertices is `P=(-5,-5,-3,-6,-2)` and `Q=(-10,-5,2,-14,6)`. Thus Q's vertices 2 and 4 are acute. Neither polygon has a consecutive supplementary angle pair: for every native side, the preceding and following sides are nonparallel. This rules out that simple half-turn monohedral escape, **not** all monohedral tilings.

P's side from `(3,5)` to `(-1,3)` has squared length 20 and midpoint `M=(1,4)`. Its two halves each have squared length 5, matching Q sides 1 and 4. The exact script enumerates all isometric copies (including reflections) with one of those full Q sides on either half of P's side, filters interior overlaps by the convex separating-axis theorem, and joins one legal copy on each half. It finds four individual placements per half and **six distinct nonoverlapping P/Q/Q three-tile patches**. The six ordered branch IDs `(Q edge index, target direction, reflection)` are:

```
first half       second half
(1,0,1)         (1,1,0)
(1,0,1)         (4,0,1)
(1,1,0)         (4,0,1)
(4,1,0)         (1,0,1)
(4,1,0)         (1,1,0)
(4,1,0)         (4,0,1)
```

One exact patch uses P as above and the two Q copies

```
Q1 = ((3,10),(3,5),(1,4),(0,8),(2,12))
Q2 = ((-5,6),(-1,3),(1,4),(-8/5,36/5),(-6,8)).
```

Each Q meets its assigned half of the P side, and their interiors are pairwise disjoint. At M the copies leave an angular gap; the patch does not force a flat star or an extension. Also Q side 3 has the **full** squared length 20, so P's same side has two different legal whole-side P/Q attachments. Consequently the half-side split is not a compulsory local feature. There is no observed recursion or scarce placement that justifies growing this fixture.

## Scope and replay

The `--scan` reconnaissance enumerates the 2,401 integer Q templates `((0,0),(5,0),(6,2),(c,d),(e,f))` with `c,d in [2,8]`, `e in [-2,4]`, `f in [1,7]`. After requiring strict convexity, unequal area, an acute Q angle, no consecutive supplementary pair, and no Q side of squared length 20, 82 templates support a two-Q half-side patch, of which 22 have a completed midpoint star. These counts concern only that finite coordinate box and contact prescription. The selected Q in this first report was found before the no-full-side filter; a changed fixture is recorded separately in [the completed-midpoint report](terra-p5p5-closed-midpoint-2026-10-20.md). The focused replay is:

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-p5p5-halfside-2026-10-20.py
```

No species omission classification or periodic-carrier search has been completed. The immediate full-side alternative and six split branches suffice to stop this particular forcing idea. Plane tilability remains unknown.
