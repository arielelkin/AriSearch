# Independent hostile review: corner-transport completeness blocker

Reviewed 2026-10-19: `research/searches/pentagon-heptagon-corner-transport-blocker-2026-10-19.md`, the fixed first-gate coefficient certificate and its independent hostile review. **Verdict: passes at the expressly stated two-tile and pointwise scope. No mixed tiling or nontilability result, and no impossibility theorem for finite transport certificates.**

## Fixed metric and independent check

The certificate specifies P=(60,105,115,125,135) and Q=(150,150,120,120,120,120,120), with unit incircle and side i joining vertices i and i+1 modulo the side count. I reran the independent first-gate verifier through the required environment:

```
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/pentagon-heptagon-first-gate-sol-independent-2026-10-19.py
```

It returned `PASS: 12 stars, exact support incidences and edge vectors, strict-convex support gaps, 10395 pairings in both chiralities`. This supplies the previously reviewed metric and angle census; it is not a test of infinite extension.

## Two-tile contact completeness

For disjoint-interior strictly convex polygons, positive-length intersection lies on a common supporting line. A relative interior point of a shared segment has a polygon interior on one side of that line; putting both interiors on the same side produces overlap in a sufficiently small neighborhood. Thus opposite half-planes are necessary. Each polygon has exactly one native side on the support line because consecutive edges are noncollinear. These observations justify reducing every such contact to two side intervals.

After fixing X and a coordinate along its support, Y has precisely two relative orthogonal choices, distinguished by determinant. Opposite interior half-planes determine which directed native edge orientation goes with each determinant. Tangential translation t remains free. The overlap is exactly [max(0,t),min(L,t+M)], and positive length is equivalent to -M<t<L. Opposite supporting half-planes guarantee disjoint interiors for every such t; no additional collision test is missing for this two-tile assertion.

All comparisons among 0,L,t,t+M include full alignment, one equal endpoint, containment and both stagger directions. t=-M and t=L are excluded correctly: they give only a point. Reflections reverse native endpoint ordering and are explicitly retained; an overall reflection introduces no further relative parameter. Label retention is essential even when equal lengths or equal angles make some unlabelled placements congruent. This is a complete continuous schema, not an enumeration of finitely many metric states. The report correctly assigns isolated point contacts to angular germs rather than claiming this interval schema covers them.

## Q2-Q2 continuum and endpoint completion

For side 2, both native endpoint angles are 120. The tangent-length formula gives L=cot(60)+cot(60)=2/sqrt(3), independently of an approximate coordinate embedding. For equal intervals, the complete positive-contact offset domain is (-L,L). The report deliberately uses its positive stagger subfamily 0<t<L, whose contact is [t,L] and length L-t; it does not claim this subfamily exhausts equal-side contacts.

At t the upper Q has a flat sector and the lower Q has a 120 corner; at L these roles reverse. Their free sector at each point has angle 60. A rotated, and if desired reflected, P0 corner occupies that sector. Convexity confines the entire P to its corner wedge. In a sufficiently small disk about each endpoint the appropriate polygons coincide with their incident sector germs, so each angular star is realizable. For each fixed t, choose disk radii smaller than the separation L-t and the distances to other vertices. No uniform positive radius as t approaches L is asserted or available from this argument.

Disjoint endpoint disks justify simultaneous descriptions of the two germs. They do not justify simultaneously inserting two complete P tiles without collisions elsewhere. A P chosen at one endpoint can also interfere with the other endpoint neighborhood outside its own germ analysis. The report explicitly disclaims whole-tile and plane extension, so this limitation is not a mathematical error. The continuum survives the stated pointwise angular restrictions only; it has not been proved to survive all joint geometric restrictions of a tiling.

## What the obstruction establishes

Holding native labels, endpoint order, angular stars and relative chirality fixed leaves L-t variable. Consequently those discrete labels cannot reconstruct exact endpoint displacements or certify geometric closure using a single representative displacement. This is a valid lost-variable example. It does not show that every member occurs in a plane tiling, nor that a finite abstraction must preserve displacements, nor that every finite rational flow certificate needs a complete geometric classification.

A finite conservative overapproximation can in principle suffice for a uniform discharging inequality; an angle-only rule can ignore offsets if its identities remain sound. Conversely a calculation claiming exact joint realizability or displacement conservation must prove the necessary reduction or retain and control the offsets. The report explicitly leaves finite cell decomposition, uniform transport formulas and angle-only discharging open. Its completeness gate is therefore a justified stop for the proposed unproved exact joint-state calculation, not a universal barrier to rational LP methods. Interpret “before a finite rational transport LP one needs” in that proposed-calculation context, with the report's uniform-domain alternative, rather than as a theorem that every LP requires exact realizability states.

No substantive correction is required. The central outstanding claim remains an exact joint-state reduction or a transport inequality proved uniformly over a sound offset domain. No flow certificate, stationary geometric measure, global tiling, global exclusion, or discovery-log edit follows from this review.
