# Fresh review of complementary bands and periodic-completion synthesis

Date: 2026-10-13. Verdict: **valid in the stated restricted family**.

Reviewer independently checked `research/lemmas/contact-structure-two-private-octagon-complement-bands.md`, together with the already independently reviewed Qcore and anchored-strip completion theorems. No exact equal-private ring computation is used.

## Closed strip versus hidden holes

A QQchain is an infinite path of convex disks glued only along its two nonadjacent full side slots. Nonconsecutive tiles cannot touch; consecutive tiles cannot have a second contact outside their common side, since their convex intersection would then contain positive area. The two chosen seam edges in each disk are disjoint including endpoints by native mask spacing. Mapping each disk to a rectangle with these edges as opposite crosscuts therefore glues to a genuine closed strip, without pinched boundaries or a bounded hole. Consistent seam parameterizations exist and local finite gluing gives continuity in both directions. Nonzero two-step transport ensures properness and prevents any end accumulation. Its two facing boundary curves are proper and simple.

Translation along the core period cannot exchange the two boundary components: it preserves the two far normal halfplanes, which distinguish upper and lower sides. Each boundary is individually periodic. This point is essential; periodicity of their union alone would not have been enough.

## Chain order and component exhaustion

Disjoint proper lines confined to bounded horizontal slabs have their standard transverse order. Their upper components are nested. Only finitely many intervening chains can occur between two specified ones: each such chain has a centroid in the bounded normal region, and its own common-period invariance places a representative centroid in one fixed longitudinal interval. Those representative positive-area tiles fit in a compact enlarged rectangle. Hence packing bounds their number. This handles far-longitudinal chains, which local finiteness alone would not bound.

Whole PQanchoring gives every Ppoint distance at mostDPfrom the Qsupport. An outermost chain would leave a far normal halfplane containing no QwithinDP; impossible. The periodic packing estimate prevents order accumulation in any bounded transverse band. Thus adjacent chains exist above and below each chain and the order extends to both transverse infinities.

Two adjacent closed strips have disjoint boundary curves (nonneighbor Qcontacts are impossible), leaving one connected open band. There is no other Qchain in it, no hole inside a chain, and no outside extreme halfplane. These bands therefore exhaust the entire open complement and are each individually period-invariant. No annulus winding or finite-orbit classification is assumed; the concrete closed-strip structure proves the stronger classification directly.

## Uniform width audit

The two centroid normal coordinates in a chain differ by at most2DQ; their averagehplaces every Qpoint in[h-2DQ,h+2DQ]. Reversed average gap larger than4DQwould contradict transverse order. Every core below the lower chosen chain is contained belowh1+2DQ, and its Qtiles belowh1+3DQ; similarly all upper Qtiles lie aboveh2-3DQ. An average gap exceeding6DQ+2DPtherefore leaves its midpoint farther thanDPfrom every Q, contradicting coverage/anchoring. Hence the stated10DQ+2DPband width is valid, including overlapping reference slabs and curved/backtracking boundaries.

## Synthesis and quantifiers

Assume an arbitrary pair in this exact palette withu!=vand exactly two private Qside slots of distinct lengths admits a plane tiling. Native reduction gives whole PQanchoring. Qcore gives an actual common nonzero scaffold period. The bands theorem gives individually invariant complement components with a uniform width. The anchored-strip theorem then constructs a replacement Pcompletion with periodMvfor finiteM. It respects the same unmarked shapes and allowed isometries and covers the plane. Thus the pair admits a periodic tiling and cannot be aperiodic.

This conclusion does NOT state that the starting tiling or every Pcompletion has a period. The replacement finite-state cycle selections may change the original filling. Coincident private lengths,u=v,fewer private slots, and different angle palettes remain outside this combined theorem. No substantive defect found; component and completion hypotheses match exactly.
