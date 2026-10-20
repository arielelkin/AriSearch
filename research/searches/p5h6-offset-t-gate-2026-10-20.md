# Offset P5/H6 complementary split: exact next-contact obstruction

**Status: proposed H0 split excluded from every plane tiling (2026-10-20).** The two P placements on H side0 have legal first contacts, and each has two legal P80 caps at its short seam endpoint. Both caps create an unfillable 50-degree sector one contact later. The fixed metric may have other host-side covers; this is a local exclusion of the named complementary split, not a proof of global untileability or aperiodicity.

## Exact shapes

Set `K=Q(zeta_36)` in the standard complex embedding and `u(d)=zeta_36^(d/10)` for directions divisible by ten degrees. Solve the two real equations

`p u(0)+q u(150) = -u(50)-(3/2)u(200)-(1/2)u(280)`

and put `L=p+q`. Solve likewise

`c u(180)+e u(280) = -L u(0)-u(50)-u(100)-(1/2)u(230)`.

The P edge directions are `(0,50,150,200,280)` with lengths `(p,1,q,3/2,1/2)` and interior angles `(100,130,80,130,100)`. The H directions are `(0,50,100,180,230,280)` with lengths `(L,1,1,c,1/2,e)` and angles `(100,130,130,100,130,130)`. Cumulative edge sums from the origin give exact coordinates. The replay checks closure, positivity, strict convexity, and pairwise distinctness of `p,q,L,c,e,1,1/2,3/2`. Approximate values are `p=1.09456226645`, `q=0.478779296751`, `L=1.57334156320`, `c=1.96227251992`, `e=1.38893095672`, with the exact inequalities `0<q<1/2<1`.

The [source triage](astra-shape-first-assessment-2026-10-20-1419.py) reports no Rao monohedral family hit for P over all 15 families and 10 dihedral relabelings, conditional on the imported complete pentagon classification. Its H-only corner obstruction gives no 130/130 numerical length bridge at H's 100-degree corner0. These first omission checks do not prove mixed tiling existence.

## Complete named-split gate

Fix H above its side0 `[0,L]`. Cover that side with P side0 of length `p` and P side2 of length `q` in either order. For each order, map each P source side in either direction and with reflection off or on: `2 × 2^4 = 32` placements. Exact separating-axis tests give exactly **two** interior-disjoint placements, one per order. Both put the P100 corner from side0 and P80 corner from side2 at the interior split point, with coincident outgoing P4 (length `1/2`) and P1 (length `1`) rays.

Let `E` be the endpoint of the short P4 side. The other P side1 continues for `1/2` beyond `E`. At `E`, the short P has angle100 while the other P contributes a straight angle180; the vacant sector is80. The only native corner with angle80 is P vertex2. Enumerate its two incident source edges, either boundary ray, and both reflection choices: eight maps. Exact ray and overlap checks leave **two distinct legal P images** for each split order. Their next contacts are fatal:

1. Native P side2 of the cap, length `q<1/2`, follows the original long seam. The cap's vertex3, angle130, lies **strictly inside** the original P side1, before its endpoint by `1/2-q>0`.
2. Native P side1 of the cap, length1, follows that seam. The original P's vertex1, angle130, lies **strictly inside** the cap's side1, because the cap extends `1/2` farther.

At either indicated point the tile with the side interior occupies180 degrees and the tile with the vertex occupies130 degrees on one side of it. The remaining sector is `360−180−130=50` degrees. Every native angle of P or H is at least80 degrees; a tile side interior occupies180 degrees. No additional tile can fill the 50-degree sector. Hence neither short-end cap can occur in any complete plane tiling. Because the eight-map enumeration covers every way to fill the compulsory 80-degree sector at `E`, **neither of the two named H0 splits can occur in a complete tiling**. The script proves strict side-interior incidence by exact collinearity and positive between-endpoint dot products, not by a drawing or numerical threshold.

Earlier counts of independent caps at the two H endpoints and their pairwise nonoverlap do not overcome this next-contact obstruction; they are omitted from the current replay. No complete classification of partial or multipiece covers of H0, no whole-side H/H exclusion, and no global untileability claim follows here.

## Comparison and replay

This changed P5/H6 metric differs from the equal-unit version [killed by a P-only omission](p5h6-complementary-t-gate-2026-10-20.md), as well as the prior P5/Q6 star and P5/Q7 metrics in the [deduplication audit](shape-first-dedup-audit-2026-10-20.md). This is a repository comparison only, not a literature novelty assertion. The proposed unusual patch cannot serve as an infinite-extension seed; further work on this fixed metric would require a different contact mechanism.

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-shape-first-assessment-2026-10-20-1419.py
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5h6-offset-t-gate-2026-10-20.sage
```
