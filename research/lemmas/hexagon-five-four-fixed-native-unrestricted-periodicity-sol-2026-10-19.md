# Fixed five/four native words: unrestricted periodic escape

Date: 2026-10-19. Author: Sol. **Status: proved restricted theorem; [separate independent Sol hostile review](../reviews/hexagon-five-four-fixed-native-unrestricted-periodicity-hostile-sol-2026-10-19.md) PASS.** The final mask33416 carrier received [independent hostile Sol review PASS](../reviews/hexagon-five-four-mask33416-universal-periodicity-hostile-sol-2026-10-19.md). All imported dependencies have the reviewed status recorded below. No new enumeration is used.

## Restricted statement

Let A,B be fixed closed simple strictly convex Euclidean hexagons. In counterclockwise native order their side-length words are

    A=(0,1,2,0,3,4), B=(0,1,1,0,2,3).

Here the labels denote five pairwise distinct positive numerical lengths, common to the two polygons. Native corner i is the end of side i and start of side i+1, modulo6. Copies may use arbitrary Euclidean isometries, including reflection. A tiling may omit either species and may have partial-side contacts.

**Restricted theorem.** If this pair tiles the plane, then it admits a tiling invariant under two linearly independent translations. The periodic tiling may omit one species. The conclusion concerns existence of a periodic escape; it does not say the original tiling is periodic or edge-to-edge.

This fixes the two native words as well as the distinct-length regime. It is not a classification of other orderings, other repeated-side patterns, all convex hexagon pairs, or the original two-convex-tile problem.

**Dihedral relabeling corollary.** The same conclusion holds when B is any cyclic shift or reversed cyclic shift of `(0,1,1,0,2,3)`. Such a change only selects a new starting side or reverses the native traversal of the same physical polygon; reflected copies are already permitted. The reviewed 180-word atlas certificate contains exactly twelve full-cover 22-star B rows, and direct finite comparison shows that they are precisely this twelve-word dihedral orbit. This corollary uses no new tiling argument.

## Dependencies and their exact roles

1. [Hexagon limits and conditional periodicity](hexagon-limit-and-periodicity.md), section “Defect-free limit for two hexagons”, supplies an admitted edge-to-edge everywhere-trivalent plane tiling from any tiling of two fixed convex hexagons. A species may disappear. Its [defect-limit re-review](../reviews/hexagon-defect-limit-rereview.md) records VALID. The compactness argument preserves genuine native vertices by uniform sector-disk separation. We use neither its deterministic-state criterion nor any assertion that finite local rules force periodicity.
2. The same file imports Zhu, Wang and Yan, *Hexagonal Tiling of the Plane*, arXiv:2508.01404v2 (2026), Main Theorem: any convex hexagon admitting a monohedral plane tiling, including unrestricted contacts and flipped copies, belongs to a Reinhardt family with a periodic edge-to-edge construction. This is an imported classification, not proved here. Its use in that file is covered by the named structural resumption review. We use it only when the admitted limit is monohedral.
3. [Forced AA dimer atlas](../searches/hexagon-five-four-forced-dimer-2026-10-19.md), with [independent hostile review](../reviews/hexagon-five-four-forced-dimer-hostile-review-2026-10-19.md), supplies the necessary 22 signed stars and seven dimer corona cycles for these exact words. It is an upper atlas, not a realizability theorem.
4. [Metric support gate](../searches/hexagon-five-four-metric-gate-2026-10-19.md), with [independent hostile review and reconstruction](../reviews/hexagon-five-four-metric-hostile-review-2026-10-19.md), certifies precisely446 retained subsets of the22-star atlas, and the seven inclusion-minimal masks below. The independent checker exhausts all2^22 subsets. This synthesis uses its finite necessary-support classification, not its nonlinear solver query (which returned UNKNOWN and excludes nothing).
5. [Three block-angle universal omissions](../searches/hexagon-five-four-nonresonant-support-2026-10-19.md), with its linked PASS review, treats1118212,2625540,3543044. [Two further universal omissions](hexagon-five-four-two-more-universal-omissions-2026-10-19.md), with its linked PASS review, treats20774,22550. These are all-metric implications for closed strictly convex polygons, not sample metrics.
6. [Mask41032 universal carrier](hexagon-five-four-mask41032-universal-periodic-sol-2026-10-19.md), with its linked PASS review, supplies the mixed flat-torus escape. [Mask33416 universal carrier](hexagon-five-four-mask33416-universal-periodicity-sol-2026-10-19.md) supplies the remaining explicit carrier, with [independent hostile Sol review PASS](../reviews/hexagon-five-four-mask33416-universal-periodicity-hostile-sol-2026-10-19.md).

The older dependency reports have historically accurate unresolved-status paragraphs. Their subsequent universal escape theorems, as explicitly listed here, supply the additional conclusions used below.

## Proof: an actual tiling supplies a retained support

Start from an arbitrary admitted plane tiling. Dependency1 gives an admitted edge-to-edge everywhere-trivalent tiling T by this same pair. If T is monohedral, dependency2 gives a periodic tiling by its sole occurring species, hence an admitted periodic tiling of the pair. This handles omission in the limit without imposing full twelve-corner cover on a monohedral source.

Suppose therefore that both species occur in T. The distinct numerical lengths make full-edge color matching necessary. A side5 has color4, absent from B and all other A sides. Every A has exactly one A mate across that side, partitioning A tiles into dimers. Across the coincident side there are only the endpoint-preserving reflection and endpoint-exchanging midpoint halfturn possibilities. Reflection puts two native(3,4) corners at one endpoint; trivalence would require a third native(3,3) corner. Neither word has one. Thus each mate is the midpoint halfturn copy. These conclusions concern T, not the initial partial-contact tiling.

If necessary reflect the entire tiling so a chosen A dimer has positive handedness in the atlas convention. Let S be the subset of the22 signed stars that actually occur anywhere in this reflected tiling, using the atlas cyclic convention and preserving reflection signs. Each actual star survives the atlas pruning: all of its seam continuations occur at the remote endpoints of its actual full edges, so induction places it in every pruning round. Thus S is a subset of the reviewed upper atlas. Its finiteness does not assume finitely many global tile orientations: signed native corners and cyclic order are the only data retained.

Both species occur, so their twelve native corner types all occur and S has full corner cover. For every seam of every star in S its actual other endpoint supplies a continuation in S. The chosen A dimer has a ten-factor boundary corona of the reviewed kind. Reading its actual adjacent sectors gives one of the seven retained cycles, and its ten actual vertex stars lie in S and witness the corresponding factors. Repeated exterior tiles or other geometric identifications do not invalidate this necessary upper condition; the enumeration deliberately relaxes those identifications. Even if a dimer boundary corner is flat, its original trivalent source star remains a valid factor.

Consequently S satisfies exactly the reviewed finite predicate: full corner cover, seam closure within S, and at least one completely witnessed dimer corona. It is one of the446 retained masks. The finite classification implies that S contains an inclusion-minimal retained mask M from

    {33416,41032,1118212,2625540,20774,22550,3543044}.

This containment does not require the retained family to be upward closed. In a finite partially ordered family, descending within the subsets of S terminates at an inclusion-minimal member. Since every selected star of S actually occurs, its three genuine native interior angles sum to2pi. Hence the angles of the fixed polygons satisfy all equations of M. The argument uses the actual realized signed-star set, rather than all geometrically possible triples or the entire upper atlas. A minimum M need not itself occur as the exact support of any tiling.

## Proof: each minimum gives an escape

The following implications apply to the fixed actual closed polygons. Additional equations in S do not invalidate any implication from its subset M.

| Minimal mask M | Universal periodic escape |
| --- | --- |
|1118212,2625540,3543044|Both species separately have the equal-antiparallel-side H1 strip construction.|
|20774|A has that monohedral strip construction.|
|22550|Both species separately have that monohedral strip construction.|
|41032|A flat oriented torus carrier with two A and two reflected B faces.|
|33416|A flat oriented torus carrier with two A and two reflected B faces.|

For the first five masks, the reviewed rational angle consequences force a0+a1+a2=2pi for the species used (and the complementary triple follows from its4pi angle total). Three positive exterior turns therefore total pi. Native sides0 and3 are antiparallel and have equal length. The reviewed universal strip proof constructs a two-orbit monohedral lattice tiling for every such closed strictly convex metric, including oblique strip periods. Its temporary coordinate shear is only a proof device; after undoing it every physical copy is a translate or halfturn of the original polygon. Thus it supplies two independent translations without changing the admitted isometries.

For completeness the two mixed carrier hypotheses are the following native angle triples, each summing to2pi:

    41032: (a0,b0,b1), (a1,a2,b2), (a3,b3,b4), (a4,a5,b5).
    33416: (a0,b0,b1), (a1,b2,b3), (a2,a3,b4), (a4,a5,b5).

The respective carrier theorems provide explicit12-pair gluings of four actual polygon discs. Every native side appears once and is paired to an equal-color side with reversed oriented boundary parameter. Their eight degree-two triangular vertex links are circles, each of the four required angle triples occurs twice, and the face adjacency graph is connected. Thus V=8,E=12,F=4 gives a connected closed orientable torus. The source polygons already have exact vector closure; it is not inferred from angle rows.

Equal-length gluings give Euclidean charts across edges, and the circular links with angle2pi give Euclidean charts at vertices. The quotient is therefore compact, complete and flat without cone points. Its complete simply connected universal cover develops isometrically onto the Euclidean plane. The lifted polygon discs cover that plane with disjoint interiors. Deck transformations preserve orientation and act freely, so their nonidentity Euclidean isometries are translations, since any nontranslation orientation-preserving Euclidean isometry is a rotation with a fixed point. The torus deck group is Z^2, discrete and cocompact, hence its translation vectors span a rank-two lattice. This proves global coverage, lack of overlap, and independent periods; a bare angle-balanced combinatorial torus would not suffice without these metric and completeness steps.

Thus every possible M supplies a periodic tiling of the original fixed pair, by the seven reviewed support escapes. This proves the restricted theorem.

## Verification and limits

This file adds no enumeration, solver call, metric specialization, or patch-extension assumption. Its finite-support evidence is the independently reconstructed446-support classification; its geometric obligations are the reviewed all-metric strip proofs and flat-carrier proofs, including the independently reviewed33416 construction. Open metric families and generic-angle calculations are unnecessary for this implication. No assertion that every formal support is realizable or extends to the plane is needed.

The33416 review gate and separate synthesis review both passed. The restricted theorem follows from the listed dependencies, with the imported monohedral classification explicitly retained as an external theorem.
