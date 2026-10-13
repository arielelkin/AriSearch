# Fresh hostile review: seven middle-mask no-AAA words

Date: 2026-10-13. Reviewer: sol. Verdict: **VALID** under the explicit actual mixed defect-free, saturated-B and unused-AAA hypotheses. This is conditional seven-word coverage, not a complete changed-multiplicity theorem.

## Four exact exclusions

The settled saturated palette forces mask {1,4}, so AB endpoint pairs are only 02 and 12. Every A side whose endpoints omit colour 2 is AA. A native corner of colour 0 or 1 with two such arms would have two A neighbours and hence a USED AAA star, which is excluded by hypothesis. Direct cyclic indexing finds this at corner 1 for 001212,010212,011202, and corner 0 for 012021. This excludes these four mixed fields at every side-length specialization; it does not exclude their fields using AAA.

For 002112,012012,012102 the private sides are exactly native 0 and 3. No-AAA forces these to be the entire AA degree-two set: corners 0/1 must have one AA arm and colour 2 has none. Their opposite positions yield the same full primitive-row argument independently reviewed in the adjacent-pair theorem. It applies here without metric assumptions: all A rows are parallel, and exact degrees force alternating A/B rows.

## Fresh independent phase reconstruction

The retained checker was read and replayed: PASS for all seven words, 3072 wheels. I additionally wrote a no-author-import checker using native endpoint sets to derive side maps and all four A/B row states:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_middle_mask_phase_independent.py

PASS: 12288 complete native wheels. Unlike the retained checker, this reconstruction allows both neighbouring B cells to have independent phases, not only the phase already prescribed by horizontal alternation. Thus the upper/lower phase pin is not proved conditionally on an assumed B-row phase relation. All B-neighbour phases give the same star test, because their corners incident to BB seams are always r.

The script groups A states by their full six-corner profiles, taking the profile of (1,+) as zero. Each group has exactly two full native states; it derives horizontal AA endpoint conditions and both vertical/offset relations rather than importing the state table. Results are exactly (h,v,o)=(1,0,0),(1,1,1),(0,0,1) for 002112,012012,012102 respectively. Wheel outcomes are independent of all chirality choices. All direct/reflected indexed states are included.

The neighbour-slot convention was checked in the preceding independent adjacent-pair review: slot k is center side k-1, and upper neighbours occur at columns i,i-1 while lower occur at i,i+1. This produces the stated profiles p0 XOR h*i XOR v*j on A row 2j, and B offset o. The two initial phases are both available. In particular 012102 has constant profile along every row; it was not lost by assuming horizontal alternation. The common species/profile periods 2D0 and 4D1 follow directly, without claiming those are already Euclidean periods.

## Metrics, development and residual scope

No AAA vertex remains, so every actual vertex contains B; complete B wheels exhaust the angle constraints. Every remaining two-state native fibre yields binary-valued seam lengths. Arbitrary side equalities merely alter the equality tables, which retain the separately reviewed pins/signed-equality classification. The actual field supplies a satisfying assignment, so the reviewed finite-cover lifting theorem applies to this periodic binary network. Full native periodic labels enter the settled actual metric-development theorem, producing a plane tiling and a nonzero translation after a possible glide is squared. No finite census supplies the existence premise.

No further review of the settled binary-cover or polygon-development proof was required. The table is conditional on unused AAA, not on its algebraic impossibility. The original unrestricted tiling must first pass the separate defect-free and saturation extraction; that extraction alone does not remove AAA. The all-mask words 001122,010122 are outside this argument. The two no-saturated-mask words are already separately covered. A012012 used-AAA has its independently reviewed central omission gate, while the other used-AAA cases retain exact closure and compatible-B obligations. The paired A002112 separator does not classify their additional metric strata.
