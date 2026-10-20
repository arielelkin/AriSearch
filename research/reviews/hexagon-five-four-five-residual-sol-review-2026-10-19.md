# Fresh hostile audit of the five residual mandatory-dimer coronas

Date: 2026-10-19. Verdict: **valid within the explicitly fixed 35-case domain**, conditional on the earlier formal atlas and source reduction. No extension or unrestricted tiling theorem is certified.

Reviewed producer and report: `research/searches/hexagon-five-four-five-residual-coronas-2026-10-19.py` and `.md`; corresponding certificate; the separate positive-witness checker; rows 15,16,23,26,31 of the 39-case metric certificate; and the seven retained formal coronas for B=(0,1,1,0,2,3). Governing problem and protocol were read. No larger search was performed.

## Independent reconstruction

The retained audit script `research/reviews/hexagon-five-four-five-residual-sol-audit-2026-10-19.py` reconstructs all 35 cases from source vertices and formal states rather than accepting certified placements. Rotation/reflection matrices are solved directly from endpoint equations. It compares every certified isometry, patch, identity failure, overlap pair, angle sum and tile count with reconstruction. Exact two-dimensional Polyhedron intersection, independent of the producer's separating-axis implementation, decides every distinct-pair overlap. Arithmetic is Q(sqrt(3)) throughout.

All five metrics have positive, pairwise distinct color lengths, exact native side lengths for the two words, and strictly convex polygons. The source angles are interiors at the **end of side i**, hence at vertex i+1; the audit explicitly checks this shift. The producer's unused fixed `angles`, `L`, and direction-table constants do not control any geometric branch. Coordinate-derived angle computations are correct for these five varying metrics.

For each row only corona 6 survives. Its ten distinct tiles are four A and six B, with neighbors (B0,-), (B2,-), (B4,-), (A3,+), (B5,-), repeated twice. Every matrix is orthogonal with the indicated determinant and maps the prescribed native endpoints to the full central boundary edge. Exact geometric equality identifies neighbors at both seam endpoints; state-label agreement alone is never substituted. All distinct polygons have intersection dimension at most one. Ten boundary vertices each receive 360 degrees of disjoint tile sectors. This certifies a neighborhood of the central dimer: shared edge interiors are covered on the opposite side, and vertex sectors close the endpoint neighborhoods.

## Attempts to invalidate the negative cases

For all five rows coronas 0,1,2 fail external-tile identity at junctions [0,5], [0], [5], respectively. Coronas 3,4,5 pass that identity test. Every one of the 30 rejected cases independently has a positive-area overlap, and every stored vertex-angle total was reproduced. Thus rejection does not rely on interpreting an angular deficit in an already overlapping patch.

As compact exact witnesses, in rows 15 and 16 coronas 3,4 have overlap pair [6,5], while corona 5 has [9,2]. In rows 23,26,31 coronas 3,4 have [4,3], while corona 5 has [8,7]. Indices refer to each certificate's deduplicated patch order. The audit reconstructs and checks the complete lists, including the additional overlaps in row 16. All failed cases 0,1,2 likewise have nonempty exact overlap lists, independently checked in full.

## Scope attacks and remaining uncertainty

Both handednesses appearing in the atlas are respected. The central AA mate is the midpoint halfturn across native side 5. Reflection of a normalized patch supplies the opposite whole-patch normalization; it creates no missing metric case here. Unordered-vertex-set identity is sound for these strictly convex polygons.

The five positive finite witnesses tolerate boundary contacts between outer tiles. This does not impose an unmentioned condition on their exposed perimeter. The proof of a covered neighborhood of the central dimer uses its full boundary edges and exact endpoint sectors. General partial-contact tilings are outside this finite formal corona classification: this audit proves no claim that every unrestricted original tiling possesses this normalized trivalent edge-to-edge source. Atlas completeness, the five-row residual reduction, and any passage from unrestricted tilings to that source remain earlier dependencies, not newly proved conclusions. The statement of shared native transitions is valid conditional on those dependencies and these five exact representatives; it establishes no propagation or plane extension.

No substantive defect was found, and no producer repair was made. The small supplied checker correctly validates the five positive witnesses but does not independently establish rejection of the other 30; the fresh script closes that finite verification gap. No novelty or global periodicity claim was reviewed.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-four-five-residual-sol-audit-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_five_residual_coronas.py

The fresh script finishes with PASS for all 35 reconstructions. No randomness, solver search, or floating-point decisions occur.
