# Independent hostile review: forced AA dimer finite atlas

Date: 2026-10-19. Verdict: **valid**, conditional on the stated edge-to-edge trivalent source hypotheses; finite combinatorial statements only.

## Exact claim reviewed

For A side word (0,1,2,0,3,4), B ranging over all 180 distinct permutations of (0,0,1,1,2,3), and five pairwise distinct positive numerical side lengths, every edge-to-edge trivalent source has the described AA midpoint-halfturn dimers. Its signed stars belong to the greatest fixed atlas computed by the producer. Each dimer supplies one of the enumerated ten-edge combinatorial corona cycles, after a global reflection if necessary. Full corner coverage is a necessary condition when both tile types occur. For B=(0,1,1,0,2,3), the upper atlas has 22 signed stars and seven corona cycles; its only certain side-neighbor transitions are the two signed readings of the AA seam.

Reviewed producer and explanatory Markdown under research/searches/hexagon-five-four-forced-dimer-2026-10-19.*, certificate under research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json, and original endpoint checker research/searches/hexagon-five-four-forced-dimer-check-2026-10-19.py.

## Assumptions and proof attacks

Numerical colors must be equality classes of actual lengths, not decorations. Distinctness is essential: otherwise color4 need not force an A5 neighbor. A side5 is unique in A and absent in B, hence edge-to-edge matching pairs all A tiles across that side. A polygon on the opposite side of the same segment has exactly two possible endpoint correspondences, yielding reflection in its supporting line or midpoint halfturn. Reflection puts the two (3,4) corners together at one endpoint. Trivalence then requires the third tile to have a native (3,3) corner, impossible because both words have exactly one color3 side. This excludes reflection and leaves the halfturn. Dropping trivalence invalidates the third-sector argument; dropping edge-to-edge invalidates the single-edge pairing. The retained statement explicitly uses both hypotheses.

The native corner convention puts side j endpoints at corners j-1 and j. Moving across a seam exchanges these endpoints, preserves each tile handedness, and reverses the order of the two sectors. This verifies the producer's ordered remote pair. Repeated corners are allowed in the enumeration, which is correct for an upper atlas since different copies may have the same native corner. A physical tile cannot contribute two sectors at one vertex, but allowing that possibility only enlarges the atlas.

A real source's complete star set is contained in the initial set and has a continuation for every seam. Induction places it in every pruning round. Finite monotone deletion reaches the greatest fixed point; it neither assumes that continuations chosen on different seams are globally compatible nor proves such compatibility. Both reflection signs are included without quotienting reflection; cyclic quotienting removes only the arbitrary first sector.

The halfturn dimer boundary traverses its two seam endpoints and the eight A corners 0,1,2,3, giving ten boundary edges even if some boundary angles are flat. At one endpoint, signed A ports (4,+1),(5,+1) leave the third tile between them; its outgoing/incoming native edges give the junction factor. Each ordinary A corner supplies the corresponding factor. The second half repeats this five-factor sequence because a halfturn preserves handedness. Equality of an exterior side slot and handedness across a boundary edge propagates its endpoint frame. It does not assert distinct exterior tiles, angle consistency, non-overlap, or realizability. These omissions cause no false negative for a necessary upper atlas.

Full twelve-corner cover requires both prototiles to occur in the source: then all six corners of each occurring polygon occur. A source using only B need not have all A corners. Consequently the 96 failures exclude mixed sources in this finite family, rather than all tilings of those pairs. The Markdown does not explicitly claim the stronger exclusion, but this qualification should accompany any later use.

## Independent alternative check

Retained script: research/reviews/hexagon-five-four-forced-dimer-independent-check-2026-10-19.py. It imports no producer code. It reconstructs all 180 words, signed entry/departure dictionaries, side endpoint sets, all cyclic color-compatible triples, complete pruning histories, fixed sets, native corner coverage, certain transitions, and all ten-edge corona sets. The certificate agrees exactly, including the seven fixture coronas. This goes beyond the original checker's retained-incidence checks and excludes missing stars or omitted corona cycles in the recorded finite domain.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-four-forced-dimer-independent-check-2026-10-19.py

Result: PASS independently reconstructed all 180 greatest fixed atlases, pruning rounds, corner coverage, certain transitions and ten-edge corona sets.

## Defects, repairs, uncertainty

No mathematical defect found in the conditional finite claim. No producer repair was needed. The original checker does not certify completeness; the additional independent reconstruction addresses that verification limitation. Both implementations still rely on the explicitly audited native port model rather than an external formal proof system.

The claim that a suitable edge-to-edge trivalent source is available for every tileable two-hexagon pair is an external reduction, not established in these three files and not certified by this review. Actual Euclidean stars must also satisfy angle equations and metric closure; those are not tested here. Therefore the fixture refutes a deterministic-propagation inference from this upper atlas alone, not deterministic propagation in actual realizable supports. No existence theorem for the fixture, periodic tiling theorem, aperiodicity theorem, unrestricted no-go theorem, or novelty claim follows.

## Final verdict

**Valid** as an exact finite necessary upper atlas and conditional forced-dimer lemma. The original two-convex-tile problem remains unresolved. Any promotion to an actual-source theorem needs the source reduction and angle/metric realizability arguments separately.
