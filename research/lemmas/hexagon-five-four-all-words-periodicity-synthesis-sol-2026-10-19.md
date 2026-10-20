# Every five/four B word: restricted periodic-existence synthesis

Date: 2026-10-19. Status: all dependencies, including the positive carrier, independently hostile-reviewed PASS; [whole synthesis hostile review](../reviews/hexagon-five-four-all-words-synthesis-hostile-sol-2026-10-19.md) PASS. The original two-convex-polygon problem remains unresolved.

## Exact statement

Let A and B be actual closed simple strictly convex Euclidean hexagons. For five pairwise distinct positive numbers L0,...,L4 their counterclockwise native side-length words are A=(0,1,2,0,3,4) and any permutation B of (0,0,1,1,2,3), where label c denotes numerical length Lc. Corner i ends side i and starts side i+1 modulo six. Tiles are unmarked copies under arbitrary Euclidean isometries, including reflection. Partial-side contacts and tilings omitting a species are admitted.

**Restricted theorem.** If this pair tiles the Euclidean plane, it admits a tiling invariant under two linearly independent translations. This asserts existence of a periodic escape for the unchanged physical polygons; it does not assert periodicity of every tiling.

## Dependencies

The reviewed defect-free limit and imported monohedral classification are precisely those in [hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md), with [defect-limit re-review VALID](../reviews/hexagon-defect-limit-rereview.md). The external theorem used is Zhu, Wang and Yan, *Hexagonal Tiling of the Plane*, arXiv:2508.01404v2 (2026), Main Theorem, imported there: a monohedrally tileable convex hexagon has a periodic construction. This synthesis does not independently establish that classification.

The native atlas is [the complete 180-word forced-dimer atlas](../searches/hexagon-five-four-forced-dimer-2026-10-19.md), with its linked independent hostile PASS review. It includes all signed native corner ports, repeated corner types and opposite-end seam pruning. An atlas is a necessary upper bound, never an assertion of geometric realization.

The following table lists the seven full-cover dihedral representatives and the exact remaining proof dependency. Each orbit has twelve words; all seven are disjoint.

| B representative | Signed stars / formal coronas | Reviewed periodic-existence argument |
| --- | --- | --- |
| (0,0,1,1,2,3) | 12 / 2 | [two-corona theorem](hexagon-twelve-star-two-corona-periodicity-sol-2026-10-19.md) |
| (0,0,1,2,3,1) | 10 / 1 | [ten-star theorem](hexagon-changed-word-ten-star-periodicity-sol-2026-10-19.md) |
| (0,0,2,1,1,3) | 12 / 1 | [species-purity theorem](hexagon-two-twelve-star-one-corona-pure-sol-2026-10-19.md) |
| (0,1,0,2,1,3) | 12 / 1 | [species-purity theorem](hexagon-two-twelve-star-one-corona-pure-sol-2026-10-19.md) |
| (0,1,2,0,1,3) | 16 / 4 | [sixteen-star theorem](hexagon-sixteen-star-periodicity-sol-2026-10-19.md) |
| (0,1,1,0,2,3) | 22 / 7 | [fixed-word theorem](hexagon-five-four-fixed-native-unrestricted-periodicity-sol-2026-10-19.md) |
| (0,1,2,0,3,1) | 32 / 100 | [reviewed resonance census](../searches/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.md) and [new positive carriers](hexagon-last-word-four-face-residual-periodic-escape-sol-2026-10-19.md), [positive-carrier hostile review PASS](../reviews/hexagon-last-word-four-face-hostile-sol-2026-10-19.md) |

The [retained orbit comparison](../certificates/hexagon-five-four-all-words-orbits-sol-2026-10-19.json) checks the complete atlas against the set of distinct permutations: 180=96+7*12. The 96 other rows lack full twelve-corner cover. This comparison uses integer tuples, no color permutations and no identification between A and B. Historical pending paragraphs in individual artifacts are superseded only by their explicit linked PASS reviews, not by this synthesis.

## Reduction from unrestricted contacts

Suppose an admitted tiling exists. The reviewed defect-free limit gives an everywhere-trivalent edge-to-edge tiling T using the same fixed polygons. It need not retain both species. If T uses one species, the imported monohedral theorem supplies a periodic tiling by that polygon. This is an admitted tiling of the pair, so this branch is complete before any full-cover assumption.

Assume both species occur in T. Every native corner of each then occurs at an actual vertex. Because the five lengths are distinct, coincident full sides must have the same numerical color. All actual signed stars survive every necessary atlas pruning round: each actual seam has its actual opposite endpoint as a continuing witness. Induction on pruning rounds proves this containment even if T has infinitely many global tile orientations. The finite data retain native corner types and relative handedness, not absolute orientations. Thus the atlas for this B must cover all twelve corners. This rules out a mixed T for each of the 96 non-full-cover words. It does not rule out unrestricted tilings for those words; it forces the preceding monohedral-limit escape.

For the remaining 84 words, select the unique orbit in the table. Dihedral changes of B only change its native starting side or reverse traversal. For reversal, reflect the chosen prototype representative as needed; arbitrary reflected copies are admitted, so its physical congruence class and periodic-existence question are unchanged. A and the numerical labels Lc remain fixed. Side-index reversal also reindexes corners: one must not transfer an angle-index equation without that induced reindexing. Applying the theorem to the normalized polygon and transporting the actual tiling back avoids this mistake. The first six rows are settled by their reviewed restricted theorems.

## Seventh orbit: actual support versus affine angle support

Normalize B=(0,1,2,0,3,1). Use the same mixed ETE trivalent T. Its actual signed-star set S lies in the reviewed 32-star upper atlas. A side5 has unique color4, absent from B, and hence an A mate. The endpoint-preserving reflection option would put two native (3,4) corners at an endpoint and require an unavailable (3,3) corner, so the mate is a midpoint halfturn. Normalize one actual dimer to positive handedness by a global reflection if needed. Its actual boundary stars witness one of the 100 formal coronas. Repeated neighboring tiles or identifications do not spoil this necessary relaxed condition.

Let alpha be the twelve actual interior angles in pi units. Let C(alpha) consist of **all** of the census's sixteen unsigned triples whose actual angle sum is 2, whether or not those triples occur in T. This generally exceeds the unsigned projection of S. Put x=alpha-(2/3,...,2/3). Polygon totals and all selected triple equations are homogeneous rational equations in x. Therefore C(alpha) is closed under the census's rational row-span closure: an implied triple equation must hold at alpha and so belongs to C(alpha). It is consequently one of the 628 enumerated closed masks. No converse claim that alpha is a generic point of that affine space is required.

Lift every triple of C(alpha) to every signed atlas star and apply the census seam pruning. The actual S remains inside at every step, by its actual remote endpoints. Consequently the pruned support has full twelve-corner cover and witnesses the actual dimer's formal corona. Using this potentially larger support is valid for these necessary filters. In particular, it cannot be among the 300 further census strata rejected for lack of full cover. It is not legitimate to identify S with the full compatible angle support or to impose all upper-atlas equations on alpha.

The exhaustive reviewed partition of 628 closed masks now gives exactly these possibilities:

1. One of 306 pure-triple escape strata. Its angle equations imply a consecutive triple sum 2 for A or B, so equal-color opposite sides0 and3 of that actual polygon are antiparallel. The reviewed universal strip construction gives a monohedral doubly periodic tiling for every closed strictly convex metric satisfying this equation.
2. One of thirteen deterministic residual strata. Their pruned signed-neighbor tables have exactly one complete relative placement at every signed native side. Restricting to actual stars cannot add alternatives. Every side state actually used has its actual neighbor, so no used state loses its unique continuation. The reviewed intrinsic determinism theorem therefore gives two independent periods for T. The argument uses the admitted infinite tiling T, not formal local extension.
3. One of nine branching residual masks 3162,3778,3802,3814,27672,27714,27738,27750,27836. Their source rows hold at alpha by construction. The new positive four-face carrier theorem supplies an equal-color gluing valid for every actual polygon metric satisfying those rows. Witness 9198 handles all except 27672 and 27836, for which witness 9264 applies. This positive-carrier dependency has [independent hostile review PASS](../reviews/hexagon-last-word-four-face-hostile-sol-2026-10-19.md).

These cases exhaust 306+300+13+9=628 masks, with the rejected 300 impossible for the current mixed source. The census priority matters: pure-triple cases are taken first even when their other necessary filters fail.

## Why the positive carriers are sufficient

The positive-carrier certificate records two A and two B copies, including chosen reflections, with all 24 sides paired exactly once to equal-color sides by oriented boundary reversal. Native endpoint identifications and connected circular triangular vertex links are checked, rather than inferred from angle sums alone. The quotient is a connected closed oriented surface with V=8,E=12,F=4, hence a torus. Exact augmented rational row identities force every vertex-angle sum to 2pi from the source rows. The actual polygon vector closures are input hypotheses; they are not supplied by angle feasibility.

These equal-length side gluings give a Euclidean metric across edges; the circular links with total angle2pi give Euclidean neighborhoods at vertices. Compactness implies completeness. The complete simply connected flat universal cover is isometric to the Euclidean plane. Lifting the actual polygon discs gives full coverage with disjoint interiors. Deck transformations preserve orientation and act freely; any nontranslation orientation-preserving Euclidean isometry is a rotation with a fixed point. Thus the deck group acts by translations. Since the quotient is compact and its fundamental group is Z^2, its periods form a rank-two lattice. No finite-patch extension or numerical closure inference occurs.

Every branch has now produced an admitted doubly periodic tiling of the same fixed pair, completing the stated restricted implication.

## Scope, replay, and review obligations

Five pairwise distinct color lengths, the exact A word, the B multiset, actual strict convexity and closed polygon metrics are essential stated hypotheses. Labels are bookkeeping for genuine numerical equalities, not matching marks imposed on tiles. Arbitrary reflections, original partial contacts, species omission, and possible loss of a species in the defect-free limit have all been included. No metric realization of a formal angle support is asserted. No full two-convex-polygon impossibility theorem or novelty claim follows.

Replay commands for imported computations are in the linked artifacts. The decisive new positive replay is:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.py --check

The [independent positive-carrier review](../reviews/hexagon-last-word-four-face-hostile-sol-2026-10-19.md) and [whole-synthesis hostile review](../reviews/hexagon-five-four-all-words-synthesis-hostile-sol-2026-10-19.md) passed. The latter checked the C(alpha) closure/pruning containment, 96-word monohedral branch, dihedral transfer, and external classification provenance.

Orbit comparison replay (read-only, exact integer tuples):

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_all_words_orbits_sol.py
