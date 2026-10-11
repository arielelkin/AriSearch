# Fresh independent review: sole-shared-arm Cairo forced-core obstruction

**Verdict: VALID under the stated exact arm-privacy and twelve nonresonance hypotheses.**

Reviewer: branching_hexagons, freshly assigned by root. Root and partial_contacts jointly developed the notch and overlap argument; this is a separate fresh audit. Reviewed [actual theorem](../lemmas/partial-contact-cairo-single-shared-core-obstruction.md), producer and record. The [independent checker](verify_partial_contact_cairo_single_shared_core_independent.py) imports no author module and executes no author producer.

## Native contacts and canonical partition

The hypothesis means seven globally distinct arm length classes with only Pa=Qd=s. The checker independently enumerates all36 unordered native slot pairs, preserving the complements (1,0,3,2,5,4,7,6). The only different-bank event is {b,C}; the remaining events are {s,s},{b,b},{C,C},{c,c},{d,d},{A,A},{B,B}. Each native core bank c,d,A,B occurs only in its own self-event. Different self-event totals cannot coincide because all seven arm values are distinct. The explicit b+C exclusions therefore make each core self-total unique among different-bank possibilities.

The reviewed two-T theorem excludes every unequal arm match involving a core bank. If a core arm faced an e/f-hosted fragment, the T's perpendicular whole seam would select its singleton self-event, forcing e or f=twice that core arm, expressly excluded. Equal opposite native arms are whole because their120 endpoints cannot sit in a side interior and their lengths agree; their90 endpoints also agree. Global slot privacy forces a reflected mate of the same species with preserved endpoints.

At the private core90 corner, an e/f-hosted T is excluded by the same self-total hypothesis. An arm-hosted T would force a different-bank switch with that total, also excluded. Thus the corner is a full90^4 star. The two perpendicular seam reflections force all four copies about that native corner. Each constituent's intrinsic private corner is this same center, so each original tile belongs to exactly one canonical cluster. The argument permits every other partial contact and reflection; no partition is postulated for a tiling that might not exist.

## Notch necessity with original endpoints retained

The checker reconstructs the general quadrant from the raw five directed edges, rotates about the private corner and obtains exactly the displayed quadrant vertices. Its potentially ambiguous fourth x coordinate is sqrt3*h/2>0 by closure. The clusters have four convex90, four convex120 and four reflex240 boundary corners. At a240 notch the remaining120 sector cannot split: every available macro corner or side-interior sector is90,120,180 or240. It must be occupied by one macro120 corner, whose native incident lengths are s,g_G. All such corners and both placements are covered by the cluster's axis reflections and the two notch signs.

The host g_H segment ends at an original120 corner, not at the neighboring macro90 corner. Therefore s>g_H places that120 corner inside the filler arm, impossible; s=g_H identifies it with the filler's90 endpoint, also impossible. For s<g_H the filler's90 endpoint is a genuine T on an original e/f side. Its perpendicular arm is b or C, both globally private. The reviewed whole perpendicular-seam rule forces the identical same-species native slot, whose two banks are s,s. Hence g_H=2s.

For the other filler side, g_G<g_H puts its terminal macro240 notch in the interior of a straight180 host boundary, creating incompatible sectors totaling420. If g_G>g_H, the host's original120 endpoint lies inside the filler side. Thus g_G=g_H. This tests both native endpoint orderings and does not assume fifth sides are unsplit beforehand. The reviewed private-arm monohedral theorem excludes either species alone. Applying the host-notch argument to each occurring species therefore forces e=f=2s.

## Full positive interval: overlap of actual constituents

Normalize s=1. Native closure then uniquely gives (1,z,(3sqrt3-z)/2,(sqrt3*z-1)/2,2), with the complete positive interval1/sqrt3<z<3sqrt3. The independent checker reconstructs the raw original polygon and its lower quadrant rather than importing the author's coordinate or determinant factors.

Its actual lower-left shared-arm90 endpoint is X=(-sqrt3*z/2,-3sqrt3/2); the private perpendicular edge points (sqrt3*z/2,z/2), at angle30. Deriving reflection from this direction gives the author's affine reflection. The T mate belongs to the reflected canonical cluster by its intrinsic private corner. That reflected cluster has center (3sqrt3-z)*(sqrt3/4,-3/4), strictly nonzero on the whole positive interval, so it is a distinct canonical cluster.

For the actual lower-right constituent, the independent point W=((9-sqrt3*z)/(sqrt3*z+7))*A2 is fixed by the reflection. Exact polynomial root isolation checks0<lambda<1, every strict clockwise support determinant at W, and all native convexity supports throughout the full interval. Thus W lies strictly inside that original tile and its reflected copy, producing a forbidden original-tile overlap between distinct canonical clusters. This is stronger than macro-area overlap and does not rely on sample continuity. Axis reflection covers the other notch sign.

## Replay and scope

Completed readonly replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_single_shared_core_independent.py

Output: PASS for raw general quadrant, all36 native event comparisons, singleton private-core banks, normalized raw closure, actual T reflection axis, full-interval strict fixed-point overlap and distinct center.

No substantive defect was found. The theorem proves untileability only under its sufficient core-forcing hypotheses. Its contrapositive places any tileable internally distinct sole-shared pair on at least one of the stated twelve hyperplanes. No tileability or untileability conclusion is made on those excluded resonances, and no unrestricted two-polygon classification follows.
