# Independent hostile review of the 39 retained omission classifications

Date: 2026-10-19. Reviewer: fresh delegated reviewer, independent of the producer.

## Verdict

**VALID for the stated retained 39-case classification and 21 pair-level periodic omission escapes.** The finite output contains 26 species-level periodic carriers: eight A-only pairs, eight B-only pairs, five pairs with both, and eighteen with neither. The verifier-design defect identified below has now been repaired and independently rechecked; direct read-only inspection and independent exact checks validate the existing retained certificate. No conclusion about mixed plane tilability, mixed periodicity, or aperiodicity follows for the eighteen.

## Claim and assumptions checked

Read AGENTS.md, research-problem.md, research-protocol.md, the angle-grid search record and producer, both angle-grid and omission certificates, the omission verifier, and the explicit H1 constructor lemma. Commands used the prescribed mise/Conda environment. No new angle or periodic search was run, and discovery-log.md was not modified.

The domain audited is precisely the 39 distinct angle tuples already retained, with their exact representative metrics in Q(sqrt(3)). This review does not independently certify that these are all possible positive distinct-length cones in the original 609-assignment domain. The producer's cone argument was inspected: its cone is pointed by nonnegativity, positive feasibility is equivalent to positivity of the sum of extreme rays, and distinct-coordinate feasibility is equivalent to no difference vanishing on every ray. The polynomial avoidance bound exceeds ten times the degree. These arguments are correct. The larger exhaustion counts remain dependent on the producer and Sage's exact polyhedron implementation; no fresh enumeration was authorized here.

The five numerical lengths are positive and pairwise distinct. A has word (0,1,2,0,3,4), B has word (0,1,1,0,2,3); the sole equal opposite pair in each is (0,3). A has only one repeated pair and B's additional repeated pair is adjacent. Consequently neither can satisfy an H2 distance-two equal pair together with its required opposite pair, and neither can satisfy H3's three equal adjacent pairs, under any cyclic or reflected indexing.

The angle convention is at the end of side j. Thus e0=-e3 is equivalent to angles 0+1+2=360 degrees. There is no off-by-one error. Starting at old vertex 4 converts the equal opposite pair to edges (2,5), exactly as required by the explicit constructor. This equivalence depends only on the angle tuple and the shared color-0 length. H2/H3 length failures persist throughout the positive distinct-color part of each cone.

## Independent exact checks and attacks

Ran a separate read-only inline Sage implementation against the retained JSON, without importing either producer or verifier. It checked all 39 angle/length records against the original certificate, all four support sums, positivity and distinctness, every encoded side's squared length and exact end-angle cosine, and every strict supporting-halfplane inequality. All passed.

It exhaustively tested the finite dihedral indexings of the H2 necessary length conditions and the H3 adjacent-pair partitions for every retained polygon. All failed as claimed. It identified H1 directly by searching all three opposite directed-edge pairs, independently of the stored H1 labels.

For every one of the 26 claimed species carriers it checked T=q1, a=q2, b=q3+q4-q1 after the prescribed translation and cyclic start, and positive determinant equal to the doubled polygon area. It additionally verified both endpoint identities of all six reversed-edge pairings in the constructor lemma, rather than relying on the determinant alone. All passed. Exact output was:

    PASS retained JSON read-only: 39 pairs, 26 species carriers in 21 pairs; six exact edge pairing identities each;18 neither; counts {(0, 1): 5, (): 18, (1,): 8, (0,): 8}

These identities cancel the distributional boundary of the locally finite periodized indicator. Its mean equals one because the cell determinant equals the sum of the two representative areas. Its constant multiplicity therefore equals one almost everywhere. Closed locally finite polygons then cover everywhere and have disjoint interiors. This verifies actual doubly periodic plane carriers, including the infinite extension, without trusting a finite patch illustration.

## Imported monohedral theorem and the eighteen cases

Inspected the primary [Zhu–Wang–Yan v2 source](https://arxiv.org/html/2508.01404v2), introduction, H1/H2/H3 definitions and Main Theorem, and its explicit non-edge-to-edge setup. The theorem applies to congruent straight-sided hexagons when every tiling vertex has at least three incident tiles, which genuine convex hexagons satisfy. It permits partial-contact half vertices and does not impose direct congruence; cyclic and flipped labelings are included.

A useful logical distinction is required. Merely escaping a collection of sufficient periodic constructions does **not** establish monohedral untileability. However, if this imported completeness theorem is invoked with the checked H1/H2/H3 failures, its contrapositive **does** establish that each species in the eighteen cases cannot tile monohedrally, even with reflections and partial contacts. That stronger conclusion depends on the external theorem, not solely on this finite computation. The current report safely states only that the eighteen escape these tests. It should not be criticized for failing to prove a stronger statement it does not assert. Conversely, monohedral untileability supplies no mixed tilability or forcing theorem for those pairs.

The report's first both-species escape was included in all exact checks; it is a valid pair of strictly convex polygons. The four support sums are necessary local angle data, not an extension certificate.

## Defect found and repair status

The initial version of verify_hexagon_five_four_39_omissions.py reconstructed and overwrote the omission certificate without reading it. It therefore could silently repair corrupt carrier data. The root agent repaired the final action to load the retained JSON and assert exact equality with the independently reconstructed result, removing the write. I independently inspected this narrow repair and reran the verifier successfully with assertions enabled. The equality compares the complete object, including all vertices, carriers, counts, schema and domain. This defect is **resolved**. No new enumeration was run during the repair review.

## Precise residual uncertainty

The 39-row coverage is inherited from the retained producer; this review independently validates each retained row, not the original enumeration completeness. The cone-wide omission classification follows analytically from the fixed words, distinct-color hypothesis, and fixed angles. It excludes boundary metrics where colors coincide, and does not enlarge the angle grid. None of the eighteen has a certified mixed plane tiling or a certified universal mixed periodicity/aperiodicity result here. The global two-convex-polygon problem remains unresolved. No novelty conclusion is made.
