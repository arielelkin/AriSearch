# Regular P5 / (144,124^3,128^3) Q7 exact first gate

Status: exact bounded gate completed; [independent Sol hostile review](../reviews/regular-pentagon-heptagon-124-128-hostile-sol-2026-10-19.md) PASS. This is not a plane tiling or forcing result for the surviving AA/BB words.

## Forced boundary and complete finite domain

Normalize the regular pentagon side to 1. The only stars are (108,108,144) and (108,124,128). At Q144 both incident edges meet pentagons. At every other Q corner one incident edge meets P and one meets Q. Thus, rooting the Q corners as v0=144,v1,...,v6, the four edges e0,e2,e4,e6 have length 1 and meet P; e1,e3,e5 meet Q. This assertion uses unrestricted-contact ETE: all angles exceed90 and no two angles sum180, excluding T junctions, and only triples can sum360.

For a Q-Q seam, its endpoint native angle pair must match the complementary pair under 124<->128. Thus native AA and BB edges must match each other, with equal lengths; AB edges can match themselves. There are either three AB edges or one each AA,BB,AB. These conditions give full length-compatible corner stars covering every native Q corner; all five regular P corners are geometrically identical and supported. Every convex tile lies in its native corner sector, so the complete tiles realizing one star have disjoint interiors. This establishes individual star realizations, not joint compatibility around a tile.

Rooting the unique144 removes rotations; reversing the remaining six letters removes reflection. The raw140 cyclic placements give exactly ten dihedral representatives. The script enumerates all ten.

## Exact arithmetic

Let z=exp(2*pi*i/180). Define t0=0 and ti=sum_{j=1}^i(180-angle_j). The direction of ei is z^(ti/2); all ti are even integers. The three unknown lengths u=(l1,l3,l5) solve the exact two real equations

    sum_{i in {1,3,5}} li*z^(ti/2) = -sum_{i in {0,2,4,6}} z^(ti/2).

If AA and BB occur add their length equality. Directions originate in CyclotomicField(180); real and imaginary parts and positivity are decided by Sage exact AA arithmetic, never floating point. For the one-dimensional solution spaces, the intersection of the three strict positive half-lines is decided exactly and an interior algebraic point selected. Each retained polygon is independently checked by all strict supporting-line determinant inequalities.

## Result

Write A=124, B=128;144 is prefixed to each six-letter word.

| word | outcome | QQ lengths (approximate only) |
|---|---|---|
| AAABBB | fails positivity | (-3.6602,-1.5398,-3.6602) |
| AABABB | inconsistent closure plus AA=BB | none |
| AABBAB | positive | (1.6966491,1.6966491,1.6268501) |
| AABBBA | positive | (1.4389529,1.4389529,1.3420061) |
| ABAABB | positive | (2.1750585,2.1052595,2.1052595) |
| ABABAB | positive continuum | sample (1.0266608,1.3523726,1) |
| ABABBA | positive continuum | sample (1.0266608,1.2804806,0.98017181) |
| ABBAAB | positive continuum | sample (1,1.3702912,1.0738449) |
| BAAABB | positive | (2.7782936,2.6387561,2.6387561) |
| BAABAB | positive continuum | sample (1.0273473,1.4122113,0.97489880) |

The exact unique witness AABBAB is defined by the displayed closure equations, l1=l3, and unit even-index edges; this is a finite exact algebraic specification with positivity checked by the script.

## Small periodic carrier screen

A supplemental independent internal side-pairing screen finds 2P+2Q oriented flat-torus gluings for the four all-AB words. Each pairs corresponding Q-Q slots between Q copies, so the same witness works for every positive metric in that word's closure continuum. Its 24 darts encode P0[0:5], P1[5:10], Q0[10:17], Q1[17:24]. Every boundary side is identified in reverse orientation; eight equivalence classes each have three corners and angle360. The JSON retains these pairings. Connected closed flat oriented surfaces of Euler characteristic0 develop to periodic Euclidean tilings. The four AA/BB positive metrics have no such carrier in this narrow screen; no larger-carrier or plane-extension claim follows. The screen includes both PP edges between the two P copies and nonadjacent PP self-pairings, and reflection choices. Independent carrier agent provides separate checking.

## Replay and limitations

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-heptagon-124-128-gate-sol-2026-10-19.sage

Output: neighboring .json file. Deterministic, no solver/time limit, all ten words completed. Software: repository locked Sage environment. No quotient or patch growth was used. Four isolated metric candidates survive the metric/native-star gate and the two-plus-two periodic screen. The exact unresolved obligation is plane extension versus a finite obstruction or a larger periodic carrier for those four metrics. Their local stars do not prove plane tileability or aperiodicity.
