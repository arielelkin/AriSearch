# Independent hostile review: complementary-angle flow

Date: 2026-10-19. Reviewer: independent Sol reviewer. Verdict: **PASS for the stated necessary gate only**. No substantive mathematical error found. This is not a proof of metric realization, plane extension, periodicity, or novelty.

Reviewed both `research/searches/complementary-angle-flow-sol-2026-10-19.md` and its `.py` companion. I independently enumerated the finite domain without importing or executing the companion: generated all ternary strings, retained prescribed multiplicities and the least member of each explicit rotation/reversal orbit, and propagated adjacent binary edge choices while enforcing each vertex degree immediately. This differs from the author's position-combination construction and complete bit-mask degree filter. Computation used integers and rational arithmetic under the repository environment wrapper.

## Analytic audit

* **Contacts and omission:** The fixed finite prototile family has positive minimum area and finite maximum diameter, proving local finiteness. All corner angles exceed or equal 108 degrees and are strictly below 180 degrees. A vertex in an open side leaves a straight-angle sector which cannot contain one corner or two corners. With local finiteness this excludes all partial side contacts. A genuine vertex therefore has exactly three corners. Neither tile's presence was assumed. Reflections preserve every step.
* **Star exhaustiveness:** Independently testing unordered angle multisets of sizes two, three and four gives exactly PPA and PBC identically, and BBB at alpha=120. The endpoint alpha=126 is not included. Four or more corners are impossible by the angle lower bound. Thus the resonance inventory is exhaustive over the entire open interval, including irrational alpha.
* **Square counts:** The boundary-neighborhood estimate is valid for Euclidean neighborhoods as well as the larger square enclosure. It remains an upper bound when R is smaller than twice the strip width. Disjoint tile interiors and whole-tile containment give an O(R+1) bound uniformly in placements and reflections for fixed Q. Incidence discrepancies occur only in such a strip. Coverage combined with 5p=(2a+c)q+O(R+1) proves q=Omega(R^2), including the zero coefficient case. The deductions b=c off resonance, b>=c at resonance, and every strict capacity/budget exclusion therefore require no density hypothesis. These statements do not assume a positive frequency limit exists.
* **Integer inventories:** The exterior-angle identity and its generic and resonant reductions are correct. The listed seven resonant solutions are the full nonnegative solution set satisfying b>=c; the four generic solutions are exhaustive.
* **Physical edge rules:** The endpoint complement rule off resonance is independent of reflection parity. At resonance the permitted corner pairs are BC and BB, and the stated edge-type possibilities follow. The text correctly avoids imposing the generic complement rule at BBB.
* **AA capacity:** At a PPA endpoint the P side not facing A faces P. Consequently a P side facing AA must have PP neighbors at both ends. Consecutive PP sides would create a forbidden star, and a pentagon has at most two nonconsecutive PP sides. Such a pair flanks at most one side, proving the claimed capacity even with repeated neighbors and reflected tiles. Formula (2) has the correct negative 3z/10 correction.
* **Resonant budget:** Summing degree-two B assignments gives 3z with only boundary error; the global average target is exactly b-c. Taking the minimum and maximum over all locally allowed assignments is a necessary condition even when different copies choose different assignments. O(R) exceptional counts do not imply absence, as the manuscript explicitly notes.

## Independent finite results

Here “local” means that at least one QQ edge subset meets the degree constraints before AA capacity and the global t budget. B and C remain distinct throughout dihedral reduction.

| Mode | (a,b,c) | All dihedral words | Local words | Gate survivors |
|---|---|---:|---:|---:|
| generic | (10,0,0) | 1 | 1 | 0 |
| generic | (7,1,1) | 4 | 1 | 0 |
| generic | (4,2,2) | 33 | 11 | 7 |
| generic | (1,3,3) | 10 | 10 | 10 |
| resonance | (0,6,0) | 1 | 1 | 1 |
| resonance | (1,3,3) | 10 | 10 | 10 |
| resonance | (2,4,1) | 9 | 5 | 1 |
| resonance | (4,2,2) | 33 | 11 | 7 |
| resonance | (5,3,0) | 5 | 1 | 0 |
| resonance | (7,1,1) | 4 | 1 | 0 |
| resonance | (10,0,0) | 1 | 1 | 0 |

The ten generic heptagon representatives and seven generic octagon representatives agree exactly, letter for letter, with the manuscript. At resonance the additional representative is AABBBBC, whose permitted t values are exactly {1,3}. Its target is 3 and m=1. BBBBBB has locally permitted t values {0,2,4,6}; its target is 6. The inventory has no A or C, so P has no permitted star and is absent in any actual plane tiling. Thus every actual edge is QQ and t=6, although the isolated local degree filter permits smaller t.

For balanced resonant heptagons, t=2 is possible exactly for ABBBCCC, ABBCCBC, ABCCBBC, ACBBBCC and ACBBCBC. Their t sets are {0,2}; the other five have {0}. Each balanced octagon survivor has only t=0. These checks confirm the claimed boundary-order defect conclusions and exact absence claim for the octagon branch.

## Minor wording refinement

In section 5, “All other words have t_max<=1” should read “All other locally admissible words have t_max<=1; the remaining words admit no local assignment.” Of the nine (2,4,1) dihedral words, only five admit a local assignment, so t_max is undefined for four. This is a definitional precision issue and does not change any exclusion or survivor.

The reviewed result is a complete necessary combinatorial gate under the stated strictly convex two-prototile assumptions and usual plane-tiling convention of coverage with disjoint interiors. Its stopping point is correctly limited: no remaining survivor is certified tileable or periodically realizable by this argument.
