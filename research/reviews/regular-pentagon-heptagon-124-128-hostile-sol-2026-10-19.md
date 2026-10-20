# Independent hostile review: regular pentagon / 124,128,144 heptagon

Verdict: **PASS / valid**, for the exact finite metric/native-star gate and the stated finite four-face carrier scope. This is not a solution of the research problem. Reviewer independently read the problem, protocol, producer Markdown/Sage/JSON, and separate four-face carrier source and record.

## Contact and angle reduction

All native angles are at least 108 and at most 144. At an unrestricted contact involving a tile-side interior, the other side of its supporting line must be filled by native corner sectors totaling 180. One native corner cannot do this; two already exceed 180. Two side interiors crossing would give overlapping interiors. Thus every tiling here is edge-to-edge. A native vertex has exactly three corners, since two total at most 288 and four total at least 432. Exhaustive triples over {108,124,128,144} summing to 360 are precisely (108,108,144) and (108,124,128). The independent checker enumerates these directly.

At Q144 the other two tiles are P, so its incident sides meet P. At Q124 or Q128, the other tiles are one P and the complementary Q, so its adjacent edge neighbor types differ. Propagating around the odd seven-cycle fixes P neighbors on edges 0,2,4,6 and Q neighbors on 1,3,5. P-Q edges have length 1. Across a Q-Q edge each endpoint angle complements 124 with 128, so AA edges match BB edges and AB edges match AB edges. Three QQ slots therefore contain either three AB edges or one AA, one BB, one AB. AA/BB equality is necessary and sufficient for the individual native-star seam lengths. Because each convex polygon lies inside its native vertex sector, full tiles realizing a single star do not overlap. This proves individual stars only.

No monohedral case is omitted: P alone cannot supply a permitted vertex star, and Q alone cannot either. This conclusion applies to unrestricted contacts by the preceding ETE reduction.

## Independent exact metric reconstruction

The unique 144 fixes rotation. All 20 permutations of three A and three B reduce by reversal to ten classes; none is reversal-fixed because each multiplicity is odd. I independently enumerate permutations, construct directions using exact algebraic sine/cosine rather than the producer cyclotomic code, solve closure and AA=BB, and check positive lengths and every strict supporting determinant. The retained verifier is `research/reviews/regular-pentagon-heptagon-124-128-independent-sol-2026-10-19.sage`. It imports no producer implementation.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-heptagon-124-128-independent-sol-2026-10-19.sage

Completed successfully: exactly AAABBB and AABABB fail, and all eight other words pass. In particular the independent isolated AABBAB reconstruction has QQ lengths approximately (1.696649104,1.696649104,1.626850111), with equality, closure, positivity and strict convexity verified in AA. Its exact defining system is unit even-index lengths, exterior direction increments 180 minus the intervening native angle, closure, and l1=l3. This uniquely determines an algebraic polygon up to isometry. The four all-AB cases have a one-dimensional exact affine kernel; intersecting its strict positive inequalities is legitimate. No numerical value decides feasibility.

The producer uses z=exp(2*pi*i/180), so exponent t/2 represents t degrees correctly; all exterior increments are even. Its omission of angle144 from the cumulative increments is correct because that is the final turn back from e6 to e0. The total exterior turn is 360.

## Four-face carrier scope and implication

I inspected the separate `regular-pentagon-heptagon-fourface-carrier-sol-2026-10-19.py` source. In 2P+2Q the forced slots require eight PQ pairs, three QQ pairs and one PP pair. Assigning eight distinguishable Q PQ darts injectively to ten P darts and pairing the two residual P darts exhausts PP possibilities, including same-face PP. The six QQ darts admit exactly the recursively generated perfect matchings. The five partitions of three length symbols exhaust all possible length coincidences. Fixing Q0 orientation loses no case by global reflection; P orientation is immaterial because the regular pentagon is reflection-symmetric. Q1 reversal maps side i to side 6-i, as implemented. Rooted word reversal is legitimate.

The component pruning is safe: a partial angle multiset must be a submultiset of an allowed final triple. Endpoint identifications correctly reverse paired edges. Final connected polygon edge gluings are oriented closed surfaces; the vertex cycles and angle sums are additionally checked by the independent positive verifier. Equal seam lengths, circular links of total angle360 and convex Euclidean faces make an everywhere flat compact surface. Euler characteristic zero and orientation give a torus. Its complete flat universal cover is the Euclidean plane; deck transformations act freely, hence are translations. Thus the positive certificates give actual periodic tilings, conditional only on the separately checked metric polygon.

I replayed the separate carrier enumeration successfully: 304 cases, 21160 nodes, four SAT and six UNSAT; its independent positive verifier printed `Verified four SAT oriented flat-torus carriers independently.`

The separate enumeration includes all length partitions, so its negatives are stronger than the original producer supplemental screen at one selected metric, while still confined to the exact 2P+2Q quotient domain. Four all-AB words have periodic carriers; the other six have none in this domain, including the four positive isolated metrics. No finite no-carrier result implies absence of larger periodic quotients, singly periodic tilings, or arbitrary plane tilings. This limitation is correctly stated. Negative search remains an audited exhaustive computation, not a formal UNSAT certificate.

## Defects, repairs, and remaining obligations

No mathematical defect found in the reviewed stated claims; no repair proposed. The retained JSON metric lengths are only approximate displays, but the Sage defining system supplies the exact reconstruction and all proof-critical comparisons use AA. The independent checker verifies agreement with the JSON feasibility flags, not trust in approximate coordinates. The root still needs to integrate review status into the producer record.

For the four isolated surviving metrics, plane extension, larger periodic carriers and any universal forcing claim remain unresolved. The gate itself establishes none of those. No novelty claim was reviewed.
