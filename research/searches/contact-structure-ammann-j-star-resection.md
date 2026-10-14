# Ammann J-star: exact local pentagon/heptagon resection

Date: 2026-10-13; reviewed 2026-10-14. **Independently reviewed VALID for the fixed local geometry, count obstruction and omission audit** ([review](../reviews/ammann-cross-source-resections-independent-review.md)). This is a LOCAL positive geometry witness, not an aperiodic tile pair.

At the exact generic source J0 use H,P1,P2, ζ and J′ as defined in the reviewed Ammann forcing lemma. Place the three source faces

    H, A=1+ζ−ζP1, B=1+ζ+ζ²−P2.

Their H-J/P1-J′/P2-J2 corners coincide at J. Their three shared full edges terminate at 1,ζ,1+ζ. This differs from the c-dimer K/L incidence. The exact producer checks pairwise disjoint convex interiors and the complete ten-edge outer boundary. Only 1 and ζ are reflex; the forced straight binary seam is [1,ζ]. Its two boundary arcs have four and six edges.

The pentagon is H with the native J vertex removed: (ζ,J″,0,J′,1). The heptagon is (1,A3,A4,1+ζ,B0,B1,ζ), using zero-based original face indexing. The independent review corrected the original note's transposed B1/B0 labels; the original producer's boundary slices already used the correct order. Both are genuinely strictly convex, have five/seven nonflat sides and positive area, and their areas sum to the three source areas. The exact producer prints all coordinates as rational polynomials in ζ, whose minimal polynomial is ζ⁴−ζ³+ζ²−ζ+1. All geometric decisions are exact; initial decimal displays are supplementary only.

This provides exactly two local output classes and an exact replacement diagram. It does not provide a global two-class tiling. In particular, covering a source tiling solely by bounded disjoint H/P1/P2 triads would impose equal source counts up to O(R) boundary error. The [reviewed anchored-count lemma](../lemmas/ammann-anchored-count-split-fixed-cluster-obstruction.md), Lemmas1–2, instead gives p1(R)/h(R),p2(R)/h(R)→φ and h(R)=Θ(R²); separate absolute densities are unnecessary. The alternative J-star contains H twice and P1 once, and must not be silently treated as this same triad. A different boundary-crossing transfer could alter those counts; none is proved here.

Both outputs are now excluded as monohedral tiles at this exact fixture. The strict heptagon cannot tile alone by the [reviewed global side-count theorem](../lemmas/side-count-and-monohedral-obstructions.md). For the pentagon, every native angle is at least72°, and only its vertex0 (the original H vertex0, index2 in the displayed pentagon) has angle72°. The independent checker exhausts all251 nonempty native angle multisets with at most five corners: the only360° relation is five copies of that72° corner. It also checks every possible180° multiset (at most two corners) and finds none. Thus T-junctions are impossible, while the other four corners cannot be surrounded even in an edge-to-edge monohedral tiling. This directly proves the pentagon cannot tile alone; no pentagon-family completeness assumption is used. The proof and exact angle-product census are in the independent review/checker.

Before this pair can be accepted, obligations are: construct a globally compatible resection with ONLY these same two output shapes; prove at least one full-plane tiling; and show every unmarked mixed output tiling, with all reflections/partial contacts allowed, reconstructs the reviewed aperiodic source. No decoder, forced reunion, global patch partition or aperiodicity is asserted. The monohedral audit removes only omission, not mixed periodic escape.

Replay: mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-structure-ammann-j-star-resection.py
