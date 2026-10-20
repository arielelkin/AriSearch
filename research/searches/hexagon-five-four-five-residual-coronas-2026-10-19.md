# Five residual representatives: exact mandatory-dimer corona gate

Date: 2026-10-19. Status: exact bounded computation; five surviving finite witnesses, independently checked by a separate implementation. No infinite extension assertion.

## Predeclared domain and cap

Exactly zero-based rows 15,16,23,26,31 of `research/certificates/hexagon-five-four-39-omissions-2026-10-19.json`. Exactly seven formal ten-edge coronas per row from the B=(0,1,1,0,2,3) atlas. A is at its stored identity placement; its private color-4 side is native slot 5. Its AA mate is `x -> A[5]+A[0]-x`. Enumerate only the 35 resulting coronas. Maximum execution 120 seconds, no seed, no larger patches, endpoint fan completion or torus enumeration. Completed in approximately 10 seconds. Coordinates and every branch use exact Sage Q(sqrt(3)), positive square root.

The earlier first-witness geometry code and second-pair local corona script were inspected. The latter's broader fan/carrier search was not run or incorporated. This gate uses only the former's seven-state domain, with the five stored exact representatives replacing its fixture.

## Results

For EACH of the five metrics, precisely corona 6 survives. It contains 10 unique tiles: four A and six B. All ten boundary vertices have exactly 360 degrees, the two central junctions use identical external tiles on their two incident boundary edges, and every distinct pair of tiles has disjoint interiors. The certificate retains full exact native-side isometries (matrix, translation, handedness, species), deduplicated patches, and all failure data.

For every row, coronas 0,1,2 fail external-tile identity at junctions (0,5), (0), (5), respectively. Each also fails angle sums and has interior overlaps. Coronas 3,4,5 pass junction identity but fail both gap-free angle sums and interior disjointness. Exact failing pairs and all ten angle totals appear in each certificate result. Thus no failure here is a timeout or merely an absent numerical match.

## Shared native incidence (read-only observation)

All five surviving witnesses have identical formal incidence. Around the ten central dimer boundary edges the neighboring `(species,native side,handedness)` list is

    (B,0,-), (B,2,-), (B,4,-), (A,3,+), (B,5,-),
    (B,0,-), (B,2,-), (B,4,-), (A,3,+), (B,5,-).

The central boundary native side sequence is A0,A1,A2,A3,A4, then the halfturned mate's A0,A1,A2,A3,A4. Thus this gate forces A0/B0, A1/B2, A2/B4, A3/A3, A4/B5 along the central dimer boundary, conditional on the reviewed trivalent edge-to-edge source and on the selected metric. Each central junction identifies its flanking B5 and B0 placements as one B tile. The root AA slot-5 midpoint-halfturn seam remains mandatory. Since the unique surviving corona is the same formal state in all five, these native contacts are shared; the Euclidean transforms differ. This is stronger local information than the angle-free upper atlas, but no global connected deterministic propagation or periodicity theorem follows from it here.

## Scope and next obligation

No metric is eliminated. Accordingly the conditional branch asking whether a zero-corona obstruction plus a defect-free edge-to-edge limit and monohedral exclusions proves unrestricted untileability is not reached. No unrestricted untileability conclusion is made, and arbitrary partial contacts/reflections in original tilings remain within the main problem's quantifier. Both neighbor handednesses admitted by the formal atlas are included; reflection of the normalized whole witness gives its opposite normalization.

The precise next obligation is to determine whether these forced local native transitions in a trivalent edge-to-edge source propagate consistently to a plane tiling or instead yield a finite necessary obstruction, and independently whether any admitted plane tiling is periodic or nonperiodic. The current finite corona alone proves neither extension nor aperiodicity. Under the requested bounded gate, stop here; do not automatically enlarge patches or search tori.

## Artifacts and replay

Producer: `research/searches/hexagon-five-four-five-residual-coronas-2026-10-19.py`.
Certificate: `research/certificates/hexagon-five-four-five-residual-coronas-2026-10-19.json`.
Independent witness checker: `research/reviews/verify_hexagon_five_four_five_residual_coronas.py`.

    mise exec -- conda run --no-capture-output -n arisearch timeout 120 python research/searches/hexagon-five-four-five-residual-coronas-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_five_residual_coronas.py

Both commands completed successfully. The checker reconstructs placements from certified orthogonal transforms, checks edge endpoints and external identity, uses independent interval projections to certify interior disjointness, and recomputes angles from exact dot products. It validates the five positive witnesses, not completeness of the seven-state combinatorial atlas; that dependency retains the earlier atlas review. Fresh hostile review of the present producer is a separate outstanding review step. The discovery log was not edited by this delegated task.
