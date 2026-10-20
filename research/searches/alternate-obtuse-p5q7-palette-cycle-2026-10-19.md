# Alternate obtuse P5/Q7: one bounded design cycle

Status: bounded angle inventory complete; the one exact metric pair attempted is falsified as a tiling pair. No aperiodicity claim. No literature novelty claim. Independently hostile-reviewed valid within the stated finite scope; see [review](../reviews/alternate-obtuse-p5q7-palette-cycle-hostile-2026-10-19.md).

## Question and finite domain

Enumerate nondecreasing P angle multisets of length five in {95,100,105,110,115,120} summing to 540 degrees and Q angle multisets of length seven in {120,125,130,135,140,145,150} summing to 900 degrees. Exclude the previously studied P=(100,100,110,115,115), Q=(125,125,125,130,130,130,135). There are exactly 20*46-1=919 pairs. No cyclic-word equivalence or geometric symmetry reduction is imposed at this stage.

For each palette enumerate all unordered typed triples of angles, with repetition, summing to 360 degrees. Each typed angle must occur. Rational nonnegative star weights must consume exactly the corner counts of one P and one Q. The equal P:Q normalization is necessary for any plane tiling: full-edge trivalence gives `3V=5P+7Q+O(R)`, while Euler counting in growing windows gives `V=2(P+Q)+O(R)`, hence `P-Q=O(R)`. Any subsequential normalized star frequencies therefore use P:Q=1:1. This is exact Z3 linear rational arithmetic. For survivors test exact nonnegative integer star multiplicities consuming one and two copies of each polygon. No timeout is set; the stated finite domain completed. Z3 4.16.0; deterministic enumeration, no randomized search.

Results: 266 palettes fail angle participation, 200 fail rational balance, 453 pass rational balance. All 453 pass the 2P+2Q integer angle inventory test. Thus no palette in this domain obtains a four-face obstruction from these corner counts alone. This is not a claim that any four-face torus actually embeds or satisfies metric constraints. The JSON retains counts and a rational witness for the selected palette. Exact replay reconstructs every finite decision.

## One changed cyclic word and exact metric gate

Take cyclic words P=(95,105,110,115,115) and Q=(125,125,125,125,130,130,140), both different from the old palette. Realize each as a polygon circumscribed about a unit circle. In K=Q(zeta_144), zeta_144=exp(2*pi*i/144), choose outward unit normals N_0=1 and N_i=N_(i-1)*zeta_144^((180-A_i)*2/5). The vertex at angle A_i is V_i=2*N_(i-1)*N_i/(N_(i-1)+N_i), with cyclic subscripts. The Sage artifact verifies every support-line incidence, every support half-plane inequality, positive side lengths, and each squared side length. All angles are strictly between 90 and 180 degrees and sum correctly, so these distinct vertices define strictly convex polygons with the stated cyclic angles. Algebraic coordinates and side lengths are retained in the metric JSON.

A side between angles a,b has length cot(a/2)+cot(b/2). Every P angle is at most 115 degrees and every Q angle at least 125 degrees. Strict decrease of cot on (0,90 degrees) gives every P side length at least 2*cot(57.5 degrees), strictly greater than 2*cot(62.5 degrees), an upper bound for every Q side length. Therefore the side-length sets are disjoint. Sage also checks all 35 cross-type equalities in the cyclotomic field and finds none. No numerical equality is used.

## Why this metric pair cannot tile

In a tiling by strictly obtuse convex polygons, a corner cannot meet the interior of another tile edge: that tile contributes a flat 180-degree angle, leaving 180 degrees, which cannot be filled by one corner less than 180 degrees or by two or more corners each greater than 90 degrees. Thus all side contacts must be full edge contacts. At a vertex exactly three corners meet, since two corners sum below 360 degrees and four exceed it. This also applies when reflections are allowed.

No P-only star exists because every P angle is at most 115 degrees, so three sum to at most 345 degrees. No Q-only star exists because every Q angle is at least 125 degrees, so three sum to at least 375 degrees. Hence any tiling would require both types. The adjacency graph of tiles in a plane tiling is connected, so some full edge would join P to Q. Their side-length sets are disjoint, a contradiction. This kills this fixed unit-incircle metric pair; it does not kill this angle palette with other side lengths or relative scales.

## Replay and scope

Run from repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/alternate-obtuse-p5q7-palette-cycle-2026-10-19.py
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/alternate-obtuse-p5q7-metric-cycle-2026-10-19.sage
```

The first script and its JSON are the exact finite angle inventory. The second script and its JSON give and verify the one exact convex realization. No solver certificate for an unbounded tiling statement is asserted. A serialization error in the initial Sage run occurred after geometry assertions; it was repaired and the complete command rerun successfully.

Stop this route after this cycle: no concrete geometric tiling survivor was obtained. Reopening would require a new side-length matching mechanism or materially different star/forcing graph; another bounded negative inventory alone would not establish aperiodicity. Existence and shape-only forcing remain wholly unproved for any alternate surviving angle inventory.
