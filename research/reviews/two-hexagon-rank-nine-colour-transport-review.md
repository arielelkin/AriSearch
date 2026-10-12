# Rank-nine same-colour hexagon transport review

Verdict: VALID for the stated finite census, five angle-only witnesses, the C/C binary metric specialization, and the alternating-A period-two metric specialization. The unrestricted I and general alternating metric fibres were outside this review; the subsequent [whole-family synthesis](../lemmas/two-hexagon-complementary-angle-native-word-reduction.md) closes them with separate reviews.

The independent checker `check_two_hexagon_rank_nine_colour_transport.py` imports neither the producer nor the global SFT. It generates all twenty binary words with three ones and recovers exactly the three dihedral bracelets C, I, ALT, with orbit sizes 6,12,2. The angle offsets from 120 degrees have coefficients `(1,-1,-2,2)` times `p-120`; their only zero-sum three-element multisets are `(1,1,-2)` and `(-1,-1,2)`. Thus the exact three-corner list is the stated 36 same-colour AAB native stars for every allowed `p!=120`. This does not restrict higher-valence contacts in the original tiling; their removal uses the reviewed defect-free limit theorem.

The checker derives B-ring corner incidences by finding the canonical triangles around the origin. It derives shared-ring overlaps and the third direction in each coarse triangle by cell coordinates. Independent recursive ring assignments reproduce all six censuses and every retained triangle-deletion round:

| A/B | Rings | Core |
|---|---:|---:|
| C/C | 96 | 6 |
| C/I | 48 | 0 |
| C/ALT | 2 | 0 |
| ALT/C | 0 | 0 |
| ALT/I | 0 | 0 |
| ALT/ALT | 2 | 2 |

For C/C it independently checks the six retained indices, every successor map, bijectivity, commutation, and the three two-state orbits. These full colour-ring states, rather than the species field alone, therefore determine a periodic colour backbone. Each placed C colour word has exactly two native placements. All equality tables obtained by assigning values to the two binary endpoint maps were independently enumerated: precisely twelve table types occur and no table has three allowed pairs. The remaining native metric problem is consequently the periodic binary equality fibre covered by the separate signed-graph lifting lemma. Reflections remain among the binary choices. A colour period is not imposed on those choices; the lifting lemma may enlarge the period.

All five stripe witnesses are checked as actual native placements on their stated quotients. Every canonical angle star, every directed seam, and the complete required native side equality closure matches the certificate. These supply conditional metric witnesses, not universal extensions for the I cases.

The two index-three alternating metric witnesses pass all six angle stars and eighteen directed seams apiece. Native side maps are independently derived from corner endpoint pairs, including the one-step offset for reflections. The period-two necessity argument also survives reflections: every A corner has incident side classes E/O, and equality on the ray shared by two A sectors forces equality of their remaining two rays. Those remaining rays bound B. Applying this at all B corners makes B equilateral of side E or O. The checker verifies this local assertion in 2,592 rotated/reflected vertex cases; coincident E=O is immediate. Necessity is conditional on native A side period two and is not asserted for arbitrary alternating A metrics.

The retained JSON check is `two-hexagon-rank-nine-colour-transport-check.json`. Its checker accepts `--output PATH`; omitting that option prints results without modifying retained artifacts. Infinite metric conclusions additionally use the periodic binary equality fibre lifting lemma and the global hexagon development theorem. Reading the signed-cycle proof found no defect: its finite cover removes all cycle signs, and periodic pins remain consistent by the assumed infinite assignment. No bounded torus search substitutes for that proof.
