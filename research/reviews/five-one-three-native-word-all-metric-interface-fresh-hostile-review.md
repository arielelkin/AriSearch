# Fresh hostile review: three-word all-metric B5+1 interface escape

Date: 2026-10-13. Reviewer: sol. Verdict: **VALID** for the stated B5+1 angle interval and A words 002112,012012,012102, with all actual side metrics and original unrestricted contacts/isometries/omissions. This is restricted-family coverage, not a solution of the original problem.

## New spatial implication

The reviewed saturation theorem supplies either a pure-A field or a mixed field with every B of degree two; pure B is impossible because no BBB star is legal. For these three words the reviewed endpoint palettes force BB mask {1,4}. The separately reviewed opposite-B-seam theorem gives complete parallel B rows even if AAA is used. No strip-width bound or prior no-AAA premise is needed here.

Suppose an A row next to B has A on its other side. With the global neighbour convention used in the honeycomb encoding, its neighbour slots 1,2 are B and the other four are A. Center vertex k sees neighbour slots k,k+1. Thus slots 0,2 are AAB, slot 1 is ABB and must have A colour z, and slots 3,4,5 are AAA. The horizontal seam between adjacent boundary A cells is left side 5 against right side 2; its outer corners are left slot 0/right slot 2 and its inner corners left slot 5/right slot 3. These are the actual two endpoints of the same seam, not two independent fan tests.

In each of the three words, z occurs at exactly native corners 2,5. All twelve indexed placements consequently give exactly four eligible boundary states, placing native sides 0,3 in those horizontal side slots. At 002112 the endpoint colour map along either private side is identity (00 or 11). At 012012 and 012102 it is swap (both sides have pair 01). This map is the same for both incident copies despite their possible opposite handedness or different native side index. The outer AAB star requires its two A colours to agree. Applying the same endpoint map gives equal inner A colours, which no rainbow AAA star can contain. All x,y,z are distinct since x is not 120. No side equality, positive-closure ratio or geometric sample enters this contradiction.

Therefore the hypothesized boundary cannot occur. Each A row touching B has B on its other side; propagation from any existing B row in both transverse directions yields alternating species rows on the full integer lattice. This eliminates wide gaps, isolated B rows and one-sided B-row sets directly. Every vertex in alternating rows contains B, so the resulting actual field has no AAA anywhere.

## Independent finite reconstruction

I authored the independent endpoint-derived checker before reading the root checker:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_opposite_private_interface_independent.py

PASS: all twelve placements per word, forty-eight eligible boundary pairs, twenty-four outer-AAB-compatible pairs, no inner-AAA-compatible pair. It derives each native side index from its unordered native endpoint set, independently of the signed side-index formula. It explicitly verifies identity/swap maps, not merely their observed incompatibility.

The root checker was then read and replayed:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_three_word_boundary_interface.py

PASS with the same counts. Actual metric matching can only remove members of this angle-compatible superset, so every equality coarsening is covered. A globally reflected or oppositely oriented boundary is normalized by global indexing; local reflected native placements are included independently in the enumeration.

## All-original-tiling corollary and residual

For the pure-A saturation alternative, the settled unrestricted monohedral hexagon theorem gives a periodic omission escape. For the mixed alternative, the new interface implication supplies precisely the unused-AAA hypothesis of the independently reviewed middle-mask binary theorem. Its actual field supplies an infinite satisfying assignment; signed equality/pin finite-cover lifting and settled actual metric development yield a periodic plane tiling, possibly after squaring a glide. No bounded ring test supplies infinite tilability, and selected polygons are re-developed rather than reinserted at old coordinates.

Combining these three words with the two capacity-excluded words gives exactly five of eleven native bracelets covered on this fixed-colour B5+1 family. The residual six listed in the theorem are correct: 001122,010122,001212,010212,011202,012021. No argument here extends the interface map to them.

The actual nonmonohedral A002112 AAA patch remains a valid local counterexample to AAA-implies-monohedral. The new theorem shows such a patch cannot occur in the extracted saturated mixed B field; it does not retroactively invalidate local geometric certificates. Likewise local positive B/BB closure remains local evidence. This all-metric boundary proof covers further equality specializations independently of the forty-two-partition ledger, so no missing coarsening or higher-rank inference is used. The next obligation concerns the residual native words or a genuinely changed construction mechanism. The original acceptance criteria remain unresolved.
