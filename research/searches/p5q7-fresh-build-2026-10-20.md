# Fresh P5/Q7 T-contact trial: exact patch, then a plane obstruction

**Status (2026-10-20): fixed pair stopped.** A genuine three-tile partial-edge patch exists, but its displayed branch has an immediate endpoint obstruction. A direct local angle-and-side argument excludes *every* plane tiling by this fixed pair, as confirmed by the [independent hostile review](../reviews/p5q7-fresh-hostile-2026-10-20.md). No convex-pentagon classification or compactness step is needed. Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5q7-fresh-build-2026-10-20.sage
```

## Exact pair and deduplication

Let `K=Q(zeta_72)` in the embedding `zeta_72=exp(2 pi i/72)`, and set `u(d)=zeta_72^(d/5)` for the angles `d` below. Write `c(a)=cot(a/2)` for the displayed polygon interior angle `a`, evaluated exactly in this embedding. A polygon with cyclic angle word `(a_0,...,a_{n-1})` has side `j` of length `c(a_j)+c(a_{j+1})`, with indices modulo `n`; successive edge directions turn through `180-a_{j+1}` degrees. This is the standard unit-incircle polygon and closes exactly.

Take `P` with angle word `(80,110,100,120,130)`, side directions `(0,70,150,210,260)`, and lengths

```text
(c80+c110, c110+c100, c100+c120, c120+c130, c130+c80).
```

Take `Q` with angle word `(120,130,130,130,130,130,130)` and directions `(0,50,100,150,200,250,300)`. Let `L=P_4+P_2` and scale the unit-incircle Q by `s=L/(2 c130)`. Then its side lengths are

```text
(s(c120+c130), L, L, L, L, L, s(c130+c120)).
```

The replay constructs vertices by cumulative exact edge vectors and verifies closure, positive side lengths, and strict convexity in the distinguished real embedding. Approximate side lengths are `P=(1.891961,1.539307,1.416450,1.043658,1.658061)` and `Q=(3.440580,3.074511,3.074511,3.074511,3.074511,3.074511,3.440580)`; comparisons in the replay are exact algebraic comparisons. Their side counts distinguish the congruence classes. The angle words and T-contact differ from the recorded `150`-seam P5/Q7 trial, the old obtuse P5/Q7 torus and disjoint-palette metrics, the regular-pentagon families, square-lattice power cells, and the P5/H6 offsets. This is repository deduplication, not a literature novelty claim.

## Exact partial-edge patch and its forced endpoint

Put Q side 3 horizontally from `0` to `L`, with Q above it. Reflect and rotate a P copy so P side 4, of length `P_4`, runs from `0` to the split point `P_4`; put a second reflected P so P side 2, length `P_2`, runs from that point to `L`. Their split corners are respectively `P_0=80` and `P_2=100`, so they fill the lower half-plane at a T contact: `180+80+100=360`. The exact separating-axis computation finds pairwise disjoint interiors. The transformations and full coordinates are in the replay.

At the left Q/P endpoint, `Q_3=130` and `P_4=130` leave exactly a `100`-degree corner, available only at `P_2`. Both incident side lengths at that corner, `P_1` and `P_2`, are strictly smaller than the adjacent Q side `Q_2=L`. Whichever cap orientation is chosen, its edge along `Q_2` ends inside that Q side. Its far angle is `110` or `120`, leaving respectively `70` or `60` degrees at this new T point. Every tile angle is at least `80` degrees. Thus both reflected cap placements are impossible. This excludes the *displayed branch*, including partial contacts; it says nothing by itself about other covers of Q side 3.

## Global local obstruction

Q alone cannot tile: every Q corner is at least `120` degrees, so no partial-edge vertex can contain two Q corners beside a flat side; every Q `130` corner would have to enter a three-corner star, but no sum `130+a+b=360` exists with `a,b` in `{120,130}`.

The replay finds no Rao-family hit for P under ten dihedral relabelings, but this is only a diagnostic. The claimed exhaustive classification of unrestricted convex-pentagon tilings is not established in the [primary literature audit](../literature/2026-10-02-search.md). The direct argument below excludes P without using it.

Here is a stronger obstruction to a *mixed* plane tiling. An `80`-degree P corner can only lie at an `80+100` T contact or at an all-corner four-star with angles `(80,80,100,100)` or `(80,80,80,120)`; the script enumerates these exact angle sums. Both four-stars are locally impossible, including unequal side lengths and T points at their far ends:

* In `(80,80,100,100)`, at least one `80/100` adjacency occurs. Each P100 incident side (`P_1` or `P_2`) is shorter than both P80 incident sides (`P_4` and `P_0`). Its far corner is `110` or `120` inside the longer side, leaving `70` or `60` degrees, below the minimum tile angle.
* In `(80,80,80,120)`, if the 120 corner belongs to P, its incident side `P_3` is shorter than either P80 incident side and ends at a P130 corner inside that side, leaving `50` degrees. If the 120 corner belongs to Q, both its incident sides exceed either P80 side; the shorter P80 side ends at P110 or P130 inside the Q side, leaving `70` or `50` degrees.

Consequently every P80 corner would have to be T-paired with a P100 corner beside a straight tile side. The two P corners share a ray along one incident side of each. Both P100 incident sides (`P_1,P_2`) are strictly shorter than both P80 incident sides (`P_4,P_0`), by exact algebraic comparison. The P100 edge therefore ends in the interior of the longer P80 edge. Its far angle is 110 or 120 degrees, leaving a 70- or 60-degree gap beside the straight P80 side. No tile has an angle below 80 degrees. Thus the T pairing is impossible too. Every P tile has an 80-degree corner, so **no P tile can occur in a plane tiling**. Q alone cannot tile by the direct Q130 star obstruction above. Hence the fixed pair is plane-nontilable.

This conclusion is local and independent of Rao classification. It does not extend to nearby metrics or angle words without rechecking all side inequalities and corner stars.
