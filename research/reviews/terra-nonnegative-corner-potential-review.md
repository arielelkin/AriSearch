# Hostile review: nonnegative corner potential zero-star limit

Date: 2026-10-13. Reviewer: terra, independent of author sol.
Claim reviewed: research/lemmas/nonnegative-corner-potential-zero-star-limit.md.
Verdict: VALID under its explicitly stated actual edge-to-edge hypotheses.
This is not a review of any downstream resonance application.

## Assumptions checked

Finite fixed genuine convex polygons have positive minimum area, bounded
maximum diameter, positive minimum corner angle and positive minimum vertex
to nonincident-side distance. Every original contact is a whole native side;
every incident tile contributes a native corner at every vertex. The zero
per-tile weight condition and nonnegative scores hold on the actual field.
Native isometries are indexed before extraction and retained thereafter.

## Attacks and resolutions

1. Irrational/negative native weights and absence of a positive-score gap:
   the finitely many native slots and uniformly bounded valence leave only
   finitely many star multisets. Positive scores therefore have a strictly
   positive minimum even for arbitrary fixed real weights.
2. Vanishing-density positive stars with no clean translates: uniform O(R)
   counts hold in every translated square, not only one exhaustion. The grid
   argument counts quadratic disjoint candidate disks against linear bad
   vertices and proves arbitrarily large positive-star-free disks.
3. Boundary cancellation concealing quadratic positives: only incomplete
   stars can cancel. Each selected tile at such a star is within2D of the
   centroid-selection boundary, so area packing bounds all such corner
   contributions uniformly by O(R).
4. Infinite local complexity or rotations destroying compactness: bounded
   window occupancy and compact O(2) give indexed placement subsequences
   without an FLC premise. Native indices are finite discrete data, carried
   along with the convergent isometries.
5. New partial contacts, coalesced vertices or changed star type in the limit:
   uniform sector-disk separation prevents vertex coalescence. Whole-side
   partners of any given convergent tile can be retained in a subsequence;
   their limiting native sides remain identical and their sectors fill the
   star disk. A new corner subdividing such a side would introduce an extra
   positive-angle sector into already covered disk interior. This is excluded
   by interior-disjointness. The argument therefore preserves complete star
   labels, edge-to-edge contacts and trivalence where present.
6. Coverage loss on a limit boundary point: locally only finitely many limit
   polygons meet a compact disk, so their union is closed. A missing point
   would have a missing open neighbourhood, contradicting coverage persistence.
7. Symmetric polygons with differently weighted equivalent corners: retention
   of indexed isometries, rather than reassignment after limit formation,
   prevents changing scores by a fresh symmetry choice.

## Defects, repairs and remaining scope

No consequential defect found and no repair required. The whole-side
hypothesis is essential to the star-persistence argument; the author correctly
forbids applying the tool directly to a partial-contact field without another
reduction. No periodicity, positive species density, bounded positive-star
spacing or removal of positive stars in every source tiling is concluded.
The only imported ingredients are fixed-shape compactness and a sector-disk
argument written out in the lemma. No computational verification is required.
