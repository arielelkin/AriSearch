# Sixteen-star native-word family: universal periodic escape

Date: 2026-10-19. Author: Sol. Status: proved with exact replay and [independent Sol hostile review](../reviews/hexagon-sixteen-star-periodicity-hostile-sol-2026-10-19.md) PASS.

Let A,B be closed simple strictly convex Euclidean hexagons with native side words
A=(0,1,2,0,3,4), B=(0,1,2,0,1,3). Labels denote five pairwise distinct positive lengths common to both polygons. Native corner j lies between sides j and j+1, modulo six. Arbitrary isometries, reflection, omission of a species, and partial-side contacts are admitted.

**Restricted theorem.** If this pair tiles the plane, it admits a tiling invariant under two independent translations. The same holds for every dihedral reindexing of B. This is a restricted family result, not a solution of the original two-convex-tile problem.

## Exact finite gate

The producer [hexagon-sixteen-star-support-sol-2026-10-19.py](../searches/hexagon-sixteen-star-support-sol-2026-10-19.py) imports the reviewed native upper-atlas builder. Its deterministic certificate is [hexagon-sixteen-star-support-sol-2026-10-19.json](../certificates/hexagon-sixteen-star-support-sol-2026-10-19.json). The atlas has 16 signed cyclic stars and four formal ten-factor AA-dimer boundary coronas. The certificate explicitly records stars, the twelve corner-cover masks, three remote-endpoint continuation requirement masks per star, and the ten factor requirement masks per corona. The predicate checks full corner cover, every seam continuation for every included star, and at least one corona whose ten factors are witnessed. All 65536 subsets are checked, including asymmetric handed supports.

Exactly 190 masks pass. Their inclusion minima, ordered by cardinality then integer, are:

| Mask | Star indices | Angle rank |
| --- | --- | --- |
|4740|2,7,9,12|4|
|10372|2,7,11,13|4|
|16772|2,7,8,14|4|
|32936|3,5,7,15|5|
|33924|2,7,10,15|4|
|16598|1,2,4,6,7,14|5|

Indices use the certificate's sorted signed-star list; bit i means star i. Each angle matrix starts with the two polygon angle-total rows (sum=4), followed by the selected stars in increasing index (sum=2), in units of pi, and includes the right-hand side as column 13. Exact rational rowspace membership proves **a0+a1+a2=2 for every minimum**. The certificate supplies its RREF and an explicit rational row combination producing this augmented target. It also lists all forced consecutive triple sums of either species. Additional stars add equations and cannot invalidate this consequence. Every retained support contains some minimum: descending in the finite family suffices, without assuming upward closure.

The producer also compares the complete reviewed 180-word atlas: its twelve full-cover 16-star B rows are exactly the twelve cyclic and reversed cyclic reindexings of this B. No additional metric or geometric equivalence is assumed.

## From an arbitrary plane tiling to the gate

We import the reviewed defect-free everywhere-trivalent edge-to-edge limit from [hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md), with VALID [defect-limit re-review](../reviews/hexagon-defect-limit-rereview.md). If only one species remains in this limit, the imported monohedral convex-hexagon classification and periodic construction in that lemma give the required escape. These dependencies and the precise omission branch are identical to those stated in [the fixed-word unrestricted synthesis](hexagon-five-four-fixed-native-unrestricted-periodicity-sol-2026-10-19.md).

If both species remain, all twelve native corners occur. Distinct lengths force edge colors to match. A side5 has unique color4, absent from B, and therefore forces an AA dimer. Reflection across it would put two native (3,4) corners at one endpoint, requiring a third (3,3) corner in the trivalent tiling; neither word has one. Thus its mate is the side-midpoint halfturn copy. Reflect the whole tiling if necessary so a chosen dimer has positive handedness.

The set S of actual signed native stars survives every atlas pruning round, since every actual edge has its actual remote endpoint. S covers all corners and witnesses its own seam continuations. The chosen dimer's actual ten boundary stars witness one of the four formal corona cycles. Possible repeated exterior tiles and identifications do not affect this necessary relaxed condition. Hence S is one of the 190 retained masks, and contains one of the six minima above. No local support is asserted to extend to a plane tiling.

## Universal geometric conclusion

Each minimum forces a0+a1+a2=2. The three positive exterior turns between A sides0 and3 therefore sum to pi. Those sides are antiparallel and their lengths agree because both have color0. The reviewed universal equal-antiparallel-side strip construction in [the nonresonant support artifact](../searches/hexagon-five-four-nonresonant-support-2026-10-19.md), section “Universal periodic omission on the three block-angle supports”, supplies a two-orbit monohedral lattice tiling by this very metric A. Strict convexity gives height-monotone lateral chains; halfturn-related neighboring strips cancel their boundaries and cover the plane with disjoint interiors. The proof permits oblique strip periods, and its coordinate shear is undone, so the physical copies use only translations and halfturns. Thus this is an all-metric implication and the periodic escape may omit B.

There are no surviving minima requiring a metric search. In particular, a closed strictly convex metric on one of these necessary supports excluding the A H1 strip escape cannot exist. No solver timeout, enlarged collar, or local-to-global extension inference is used. The branch is closed by the proved periodic carrier, rather than blocked at an extension conjecture.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-sixteen-star-support-sol-2026-10-19.py

This passed using exact integer masks and Sage rational arithmetic. The certificate exposes the full finite predicate and row-combination witnesses for independent reconstruction. Separate hostile review remains required before promotion to reviewed status.
