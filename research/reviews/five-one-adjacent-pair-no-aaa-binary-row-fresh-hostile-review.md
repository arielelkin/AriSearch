# Fresh hostile review: no-AAA A002112 binary row escape

Date: 2026-10-13. Reviewer: sol. Verdict: **VALID** under the explicit actual-field hypotheses: mixed defect-free field, every B of BB-degree two, and no USED AAA star. Neither absence of AAA from the algebraic angle language nor an arbitrary-metric full A002112 theorem is asserted.

## Spatial reduction and native placement exhaustiveness

The reviewed saturated palette forces B mask {1,4}, since A002112 lacks the 22 endpoint pair required by the other two masks. Its AB pairs are 02 and 12. Private native A sides 0 and 3 are therefore AA. In the three used mixed stars, each A0/A1 corner has one AA arm and every A2 corner has none. Thus these are exactly the two AA sides of every A tile, and they are opposite.

In the reviewed triangular cell indexing, opposite AA sides give complete straight primitive lattice lines. Different primitive directions have determinant of absolute value one, so any two complete lines of different directions meet at an integer cell; the resulting cell would require at least four AA partners, contradicting degree two. Consequently all A rows are parallel. Every cell in each such row is A. Two adjacent A rows violate A degree two; two adjacent B rows violate saturated B degree two, because each B already has two B neighbours in its own row. Hence the species rows alternate. This is a combinatorial cell statement, not a premature assertion that their Euclidean development is translationally periodic.

Across an AA seam, a 00 side must meet 00 and an 11 side must meet 11: their endpoint corners enter only AAB0 or AAB1 respectively. Since the opposite side of each A has the other type, native phases alternate along each row, even if side lengths coincide. The four A and four B row states listed in the proof exhaust all twelve indexed placements of each species satisfying their specified opposite private/BB side positions.

## Independently checked indexing and phase pins

I wrote a separate no-author-import endpoint-derived checker:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_adjacent_pair_row_states_independent.py

PASS. It derives native side indices by matching unordered native corner endpoint sets, rather than copying the producer's signed side-index formula. It enumerates all twelve placements, derives the two-state A and B phase fibres, and proves that the two full corner profiles in each fibre agree. It reconstructs all 1024 complete B wheels and finds exactly 256 legal wheels: precisely those with identical upper-A, lower-A and B phases. It also checks every chirality pair on every AA seam, where both native side index and both endpoint colours match.

The wheel indexing is consequential: neighbour slot k corresponds to center side k-1; its shared center corner k is matched with neighbour corners k+2 and k+4. With right AA direction (1,0), upper neighbours occur at columns i and i-1, lower neighbours at i and i+1. These are the opposite-phase choices in the proof. Thus equal adjacent-row phase pins are compatible with the global lattice, and yield an actual backbone with periods 2D0 and 2D1. The pins were not inferred from a single angle profile or assumed geometric alignment.

The retained checker was read and replayed:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_adjacent_pair_binary_rows.py

PASS: 1024 wheels and 256 four-scalar equality assignments. Because AAA is unused, every vertex includes a B tile, so these B wheels exhaust all angle-star constraints; no additional A-only vertex constraint is omitted.

## Metric equality fibres and periodic development

At every cell the remaining two choices are full native placements, including reflected placements. Once the periodic species/phase backbone is fixed, all star angles hold for every bit assignment. Each remaining seam has a length on each side determined by only the bit at its incident tile. The legal two-bit relation is therefore equality of two scalar functions. Such a table has either all/none pairs, a row, a column, one pair, or a diagonal/antidiagonal; three pairs force the fourth. Pins and signed bit equalities express all cases. Arbitrary coincident actual side lengths merely change which of these tables occurs, so every metric specialization is retained.

The assumed actual field supplies a satisfying bit assignment. The already independently reviewed periodic-binary-equality-fibre theorem therefore supplies a solution on a finite-index cover of the periodic backbone. This is exactly its scope, rather than an appeal to periodic points in arbitrary binary SFTs. Its periods may exceed twice the base periods; the proof makes no unsupported universal period bound.

Full native periodic labels then enter the settled actual metric-development theorem, with positive side lengths and genuine convex actual A/B shapes as supplied by the original field. This produces a plane tiling and a nonzero translation after squaring a possible glide. The argument re-develops the new field; it does not reinsert changed native choices at unchanged old Euclidean coordinates. No finite feasibility check alone supplies infinite tilability.

## Coverage and precise residual

The lemma gives a periodic escape for every actual metric satisfying its no-AAA saturated-field hypotheses. For an original partial-contact tiling the reviewed defect-free and saturation reductions supply the needed field only if that extracted field also has no AAA; the lemma does not itself remove AAA. The paired-side AAA separator is a separate reviewed stratum and cannot classify the remaining AAA patterns or their specializations. A concrete closure/positive-B gate for those patterns remains the next obligation; repeating this settled binary enumeration has no purpose.
