# Hostile review: corrected corona59 finite geometric patch

Verdict: **PASS**, scoped strictly to the ten-face finite patch of `research/lemmas/hexagon-thirtytwo-corona59-local-patch-sol-2026-10-19.md`. No conclusion about unbounded extension, periodic escape, or the original problem follows.

## Independent exact verification

The retained independent checker is `research/reviews/verify_hexagon_thirtytwo_corona59_local_patch_hostile_sol_2026_10_19.py`. It imports neither the producer nor the formal builder. Starting from the recorded native coordinates and state list, it independently develops all ten boundary incidences, verifies the two duplicate placements, and checks every retained face is a rigid native copy with the stated handedness. It checks strict convexity, all 45 tile pairs by exact supporting axes, native colors on every shared edge, the 32 vertices and 41 edges, and the absence of vertex-only contacts. Result: ten faces, 19 shared whole edges, 26 strictly separated pairs, ten triple vertices.

The producer was also replayed successfully, reporting the retained star indices 5,15,20,23. The independent checker verifies actual native corner multisets rather than trusting these star indices: the four multisets are {0,1,8}, {2,7,11}, {3,6,10}, {4,5,9}. Its corner index at native vertex j is j-1 modulo six, so these are precisely the end-corner equations in the lemma. Reflections do not change which native angle occurs there.

## Persistence and seam audit

The shared-edge decomposition is exactly one central-central edge, ten central-exterior edges, and eight exterior-exterior edges. Every outer face attaches directly to a central face. At eight ordinary central-boundary corners, three supported angles sum to 2pi. Because the relevant native side colors coincide, their lengths coincide for the whole analytic length path. Once each outer face is placed on its central edge with the base handedness, the angle sum forces the two residual rays to agree and the equal lengths force their other endpoints to agree. This proves all eight remaining exterior-exterior edges exactly, not just to first order.

At the two seam endpoints the central native angles are A4,A5 and the outside angle is B3. The support equation A4+A5+B3=2pi makes the two independently prescribed placements of that B tile agree: its incident sides are B3 and B4 with the matching colors. Position, corner, handedness and one directed side determine its rigid placement uniquely. Thus labels 0=9 and 4=5 persist exactly. No extra gluing cycle remains after these ten stars.

For each of the 19 neighboring pairs, convexity and the established common whole edge keep the two interiors on opposite sides; their base orientations select those opposite sides continuously. For each of the other 26 pairs the independent check finds a strict separating axis at zero. Its finite set of strict inequalities persists under continuous vertex motion. Taking the intersection of these finitely many neighborhoods with the analytic branch and strict-convexity neighborhood proves the asserted sufficiently-small-positive-t patch. There is no appeal to numerical tolerances or to a finite patch extending indefinitely.

## Replay

`mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_thirtytwo_corona59_local_patch_hostile_sol_2026_10_19.py`

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-corona59-base-patch-sol-2026-10-19.py`

Assumption ledger: the corrected analytic IFT branch and its four exact support equations are the named input; this review checks their local geometric consequence. The base certificate is checked independently. The plane-extension and universal-periodicity obligations remain outside scope and unproved by this audit.
