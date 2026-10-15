# Connected repeated-side support gate for one changed hexagon word pair

Date: 2026-10-15. Status: exact necessary-condition reduction, independently reconstructed by the concurrent hostile reviewer; see the review record when retained. No metric feasibility or tiling existence follows from the finite survivors.

The sole word pair is A=(r,x,r,y,z,t), B=(r,z,r,y,x,t), with five distinct positive physical lengths. Corners are indexed after their side: a0,...,a5 have integer indices0,...,5 and b0,...,b5 have indices6,...,11. Start with an actual full-side trivalent plane tiling whose actual r-seam graph connects the four native r slots A0,A2,B0,B2. Reflected tiles are allowed.

## Exact finite domain and necessity bridge

The native corner graph has sixteen triangles, listed in the linked certificate. Every vertex of the source tiling uses one of these triples. Adjacent native side labels differ, and there are no loop corners. Three rays around a trivalent vertex therefore have three different labels; a repeated native corner index cannot occur in such a triple. Each prototype's own corner graph is triangle-free, so a source tiling cannot be monohedral. Both prototypes occur, hence all twelve native corner slots occur somewhere.

Let S be the set of native star triples that actually occur. It covers all twelve corners. For each star and each of its three seams, the two native tile corners at the opposite end of that full seam must occur together in another member of S. The checker imposes exactly this far-end availability, without claiming a common global placement for different witnesses.

For each of the six pairs of distinct r slots, both endpoint correspondences are checked. Exactly one correspondence passes, with exactly one third corner at each endpoint. Consequently an actual seam of that slot pair forces two specific members of S. Connectivity of the actual four-slot seam graph implies it contains one of the sixteen labeled spanning trees of K4. Its three edges force their corresponding endpoint stars into S. Loops do not connect distinct native slots.

The complete computational domain is all 2^16 subsets of the sixteen-star atlas, tested for: (1) containing all stars forced by at least one of the sixteen trees, (2) covering all twelve native corners, and (3) far-end availability for all three seams of every selected star. Exactly144 subsets pass. Exactly12 of these are minimal under inclusion. Every actual S in the stated connected-r branch therefore contains one of those12 minimal subsets. This is a finite logical implication, with no finite-model or global-extension assumption.

For each minimal subset, attach its star equations (sum of the three angles equals2pi) and the two native polygon sums (each4pi). Exact rational row reduction gives11 distinct affine flats. Checking row-space inclusions reduces the necessary union to seven maximal flats, whose retained IDs are0,2,5,6,7,8,10. The augmented last column is the right-hand side and every angle is measured in units of pi. No strict-angle feasibility test is silently used.

## A small algebraic summary

Set D=a0-a1, E=b0-b1, F=a2-b2 and G=a5-b5. The seven flats imply the following weaker necessary trichotomy:

* flats2,5,6: F=G=0;
* flats0,8,10: D=E=0;
* flat7: D=G=-E=-F.

The full rows in the certificate remain authoritative; this trichotomy discards additional equations and is not a replacement for them.

Flat5 implies the four stars (a0,a2,b3), (a1,a5,b4), (a3,b0,b2), (a4,b1,b5). These are precisely the old private-repeat torus's binary corner-choice parameters both equal to0. Its literal side gluings still join equal physical lengths when the two previously private repeated lengths are identified. This is a positive witness transfer, not an invocation of a theorem requiring six distinct numerical lengths.

## Artifacts and replay

Producer: [exact support gate](hexagon-changed-word-connected-support-gate-2026-10-15.py).
Certificate: [native supports and rational flats](../certificates/hexagon-changed-word-connected-support-gate-2026-10-15.json).

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-changed-word-connected-support-gate-2026-10-15.py --output research/certificates/hexagon-changed-word-connected-support-gate-2026-10-15.json

The certificate retains the complete atlas, all trees, every far-end requirement, all144 accepted support masks, all12 minimal supports, all11 exact augmented RREF systems, and their containment relations. A four-face torus atlas is a separate positive-witness experiment; failure to find a torus in that domain cannot exclude any of these source systems.

## Expanded same-word gate: no repeated-side connectivity assumption

At the root's request, the producer additionally enumerates all subsets in the SAME 2^16 native-star domain that cover all twelve corners and satisfy all far-end requirements, omitting only the connected-r tree condition. Exactly171 subsets pass and there are exactly8 inclusion-minimal subsets, each containing four stars. These are retained in `all_endpoint_closed_cornercover_masks` and `all_minimal_supports`. Original connected-branch fields and flat IDs are unchanged.

For this expanded result, start with any actual full-side trivalent tiling by the stated word pair. Its actual star support belongs to the171-subset domain, so contains one of the8 minimal supports. No formal-color theorem, contact-connectivity necessity, metric deformation, finite quotient bound, or actual r-seam connectivity is required for that implication. The prototype-occurrence and far-end arguments above still apply. Whether a given minimal support has a suitable torus witness is a separate exact positive-certificate question.

The expanded raw-support domain is the preferable source for a final family theorem if the root's independent periodic witnesses or geometric determinism cover all cases; the older seven connected-r flats remain a useful checked intermediate reduction.
