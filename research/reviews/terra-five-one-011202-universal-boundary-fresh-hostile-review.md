# Fresh hostile review: A011202 all-metric B5+1 exclusion

Date: 2026-10-13. Reviewer: sol, independent of Terra's proof. Verdict: **VALID** at every actual metric and equality specialization in the stated B5+1 angle family, with unrestricted original contacts/isometries/omissions.

## Structural and native prerequisites

The exact four-star language is a settled reviewed dependency. This A word lacks a native 22 side, so the reviewed saturated palette excludes the outer BB masks. The middle mask {1,4} has opposite BB sides and gives complete parallel B rows by the independently reviewed row theorem, even if AAA is used. Original tilings enter through the reviewed defect-free/saturation extraction; they are not assumed edge-to-edge initially.

Both native A sides 0 and 1 omit z and are therefore necessarily AA, since middle-mask AB palettes are only 02/12. These private sides are adjacent. In a one-row A strip, its only two A neighbours are in opposite row directions. No direct or reflected native placement can put both adjacent private sides there. Every B-row face consequently borders a wider A strip or half-plane, whose boundary row has outer AAB and inner AAA vertices. This applies to isolated B rows and one-sided row sets too.

## Fresh exact boundary reconstruction

I read and replayed the retained independent certificate checker: PASS for the full two-face 288 native pair domain, twelve width-one placements, exact native AA metric indices and graph cycles. I also wrote a separate no-author-import reconstruction shared with the other resource-excluded word:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_001212_011202_boundary_resources_independent.py

PASS. It derives native sides by matching native endpoint sets, uses the opposite global row-seam direction from Terra's table, scans all twelve placements at both ends, and independently computes the true bi-infinite viable graph. All four accepted boundary edges on BOTH faces have outward resource x/x. Reversing the directed row convention reverses the graph but preserves this resource and the metric equalities.

The endpoint convention is sound: with B above, global A slot1 is the ABB z corner; the horizontal seam joins side5 to side2, with outer endpoint corners0/2 and inner corners5/3. Terra names the copies in the reverse row order, using outer2/0 and inner3/5. For B below, the two roles exchange and slot4 is z. Both checks include all native reflections and do not assume intrinsic polygon symmetry.

Every bi-infinite native path is constant at one of Terra's states 0 or 2, with loop equality a0=a3. I explicitly checked reachability FROM a cyclic component and TO a cyclic component; this rules out a hidden heteroclinic bi-infinite path through a transient bridge, which merely listing cyclic vertices would not generally do. Here the viable graph has only the two loops. Importantly the global contradiction needs none of this pruning: every accepted finite edge already has the same outward resource x/x. The surviving loops are local evidence and do not supply an infinite strip.

## B-corner resource contradiction

Every middle-mask B has one AAB vertex on each row face and four ABB vertices. The former are its mandatory s and one r corner; the latter all require r. Both adjacent boundary A rows force x/x at every outward AAB vertex.

For A001212 this would require TWO s corners, whereas B has exactly one. For A011202 it would require NO s corner anywhere, contradicting its mandatory unique s. In the present word the corresponding contradiction applies. No length matching, metric closure, boundary path frequency or finite-model inference is used. Side equalities can only delete candidates from the angle-compatible superset, so the conclusion covers all coarsenings.

The saturated mixed field is impossible. Any original tiling must therefore give a B-omitting all-A limit; reviewed actual development and the imported unrestricted monohedral hexagon theorem yield a periodic A-only tiling. Omission is allowed by the original problem. Pure B cannot occur because the retained defect-free language has no BBB. The conclusion does not claim all original tilings are periodic, and requires no binary-fibre lifting theorem.

## Nondestructive replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_011202_boundary_transfer.py

Result: PASS. Settled forcing, saturation, development and monohedral dependencies were checked for applicability, not re-audited. There is no new geometry search or solver here. This establishes full native A011202 coverage only on the explicitly stated fixed-colour B5+1 interval excluding 120. Other multiplicities, angle strata and the two remaining all-mask words are outside it. The original research problem remains unresolved.
