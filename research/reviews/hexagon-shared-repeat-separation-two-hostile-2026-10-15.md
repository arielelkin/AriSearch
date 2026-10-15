# Fresh whole-claim review: shared doubled color at separation two

Date: 2026-10-15. **Final verdict: VALID.** I read the complete exact [classification theorem](../lemmas/hexagon-shared-repeat-separation-two-periodicity-2026-10-15.md), its new producer/certificate, the previous killed-word dependency, and the reviewed surviving-word theorem. I independently reconstructed all new finite domains, and directly reran the older killed-word native pruning as an additional check. No producer imports, numerical metric assumptions or solver answers enter the new checker.

## Exact mathematical scope

The numerical theorem assumes two genuine convex hexagons each has exactly the same set of five distinct physical side lengths, the same length is doubled in both, and those repeated sides have cyclic separation two in both. If such an unmarked pair admits any plane tiling, including reflections and partial contacts, the pair admits a full-side doubly periodic tiling.

The stronger source variant uses the same five DISTINCT formal side colors with the same doubled color and separation-two pattern. Equal colors prescribe equal positive physical lengths, while different colors may have equal lengths. It assumes an indexed, color-matching, full-side everywhere-trivalent source and concludes an unmarked doubly periodic full-side escape. It does not assume that unmarked geometry forces the source colors. This is one slice of repeated-side hexagon pairs, not a classification of arbitrary hexagon pairs or a solution of the unrestricted two-polygon problem.

## Independent canonical-action audit

Normalize A=(r,x,r,y,z,t). The repeated r pair determines one short arc with a single middle symbol. Any B can be rotated so its r slots are 0 and2 and written (r,m,r,a,b,c). Reversal exchanges a and c and preserves m,b. The 24 permutations of the four singleton symbols therefore give twelve independent-B-reflection classes. This normalization does not discard a reflection direction of a placed polygon: it merely reindexes its reference, and reflected occurrences remain allowed.

The only color relabelings preserving the normalized A up to native dihedral reindexing are identity and y<->t. The unique repeated symbol r is fixed, the unique short-arc middle x is fixed, and the long path y,z,t can only be fixed or reversed. In particular z is fixed. These are common renamings of the color parameters, not an assertion that physically distinct y and t edges can be interchanged by a symmetry of a fixed physical A. Reflecting/reindexing A and consistently renaming the five parameter names is legitimate for a theorem covering all such metrics. The same reindexing can be carried through every source occurrence.

My checker derives the two relabelings from all twelve dihedral views of A, independently of the producer's S4 stabilizer test. It normalizes B by filtering its full dihedral orbit for repeated slots 0 and2, rather than using the producer's four-tuple reversal formula. The resulting twelve forms give exactly SEVEN orbits under the derived A action. No prototype exchange is used or required. The orbit sizes sum to twelve and match every retained certificate tuple.

The seven representative tuples (m,a,b,c) are:

    (x,y,z,t), (x,y,t,z), (y,x,z,t), (y,x,t,z),
    (y,z,x,t), (z,x,y,t), (z,y,x,t).

The fifth representative's other normalized tuple is (t,y,x,z). I found the first prose draft listed its unnormalized reflected tuple instead. The author corrected this table entry before final review; the producer, certificate and orbit coverage were already correct. No mathematical case was omitted by that transcription error.

## Native source necessity and complete pruning

Neither native word has equal adjacent colors. At a full-side trivalent vertex the three rays have three distinct formal colors; otherwise their intervening native corner would have equal adjacent colors. Its actual native corner pairs therefore form a numerical-color triangle. One actual corner index cannot appear twice, since that would duplicate the same two ray colors instead of supplying three distinct pairs. Physical equality of different colors does not change this reasoning for a color-matching source.

Each individual word has a four-cycle plus a pendant edge as its color graph, and no triangle. Thus no source can use one type alone. Both occur, so all twelve actual native corners occur. For the two middle-x orbits, x has only neighbor r in both graphs. The rx corner can belong to no triangle even though those native corners must occur. This excludes both pendant orbits directly.

For each nonpendant word the checker independently generates complete stars by choosing three distinct ray colors and actual corner ports on their three pairs. It reconstructs native side endpoint sets explicitly. For every selected star, a ray color chooses one native side at each incident corner; the two tiles across that full side meet again at the two far native corners. Some actual star must contain them. If the two indices coincide, no allowed three-distinct-ray star can contain both copies.

Starting from the full atlas, delete every star with any absent far-end continuation in the current atlas. All actual stars survive each deletion round by induction: their actual full-side continuation is another actual star. This is a necessary-source invariant. Empty pruning therefore proves untileability of that source; no finite local survivor is promoted to a plane tiling.

For the three new representatives, the independently reproduced atlas-size traces are:

    B=(r,y,r,x,z,t): 0;
    B=(r,y,r,x,t,z): 8 -> 0;
    B=(r,z,r,x,y,t): 12 -> 1 -> 0.

I check every retained deleted-star certificate: its two seam corners really belong to the star, the ray color is their unique shared arm, its listed far corner pair is correct, and no permitted completion is present in the entire current atlas. Every round's full input and survivor lists agree with the independent reconstruction. The final singleton in the last trace is (4,6,11); its z ray gives far corners (3,7), absent in that singleton.

The checker also independently exhausts all original support subsets for the new words: 1+256+4096=4353 masks. None covers all corners while retaining every needed continuation. This corroborates the stronger empty-atlas induction; it adds no global extension assumption.

For the older excluded representative B=(r,y,r,z,x,t), I independently recover its full 12 -> 1 -> 0 pruning trace directly from the same native definitions. Thus its transfer from the old numerical interpretation to formal colors has been checked afresh, without relying on physical length inequalities or treating an old source theorem as a black box outside its hypotheses.

These checks exclude exactly six of the seven orbits under the stated formal-source assumptions.

## Surviving orbit and full geometric conclusion

The sole surviving orbit is the already reviewed changed family

    A=(r,x,r,y,z,t), B=(r,z,r,y,x,t).

I previously performed the fresh whole-claim audit of [its complete theorem](hexagon-changed-word-connected-support-hostile-2026-10-15.md), including its stronger noninjective formal-color source variant. Its all-171 native-support domain gives 169 explicit positive torus choices via 676 exact raw-angle-row identities and two exact four-star supports with indexed native-neighbor determinism. The first route constructs compact flat tori in the original metrics; the second proves a discrete cocompact framed symmetry group with rank-two translations. Physical polygon symmetries are resolved by the given source indices, not by an unjustified assumption of geometric asymmetry. Both conclusions are full-side doubly periodic witnesses for the original unmarked shapes.

No absence from a bounded torus search is used. The surviving-word theorem already supplies its own complete native support bridge and unbounded geometric escape proof; this classification adds only exhaustive word reduction and the six exclusions.

For the numerical unrestricted statement, the reviewed defect-free-limit theorem is applied first to the original uncolored tiling, yielding a full-side trivalent source of the original shapes. Numerical side lengths are the five distinct source colors, so every full seam matches a color. The formal source classification then applies. A monohedral limit is impossible here by the individual triangle-free color graph; it is not silently discarded. No color rule is required in the final unmarked tiling. In the noninjective formal variant the source is explicitly assumed already full-side and color-matching, so an uncolored limit is not being asked to preserve colors.

## Independent replay and remaining scope

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-shared-repeat-separation-two-independent-2026-10-15.py

Observed result: PASS 24 permutations, twelve B-reflection forms, two independently derived A relabelings, seven complete orbits; both pendant exclusions; all three new pruning traces and deleted-star records; the older killed-word pruning; all 4353 supplementary new support masks. The checker imports no producer and uses only finite integer sets and tuples. No random seeds, timeouts, geometry tolerances or solver calls occur.

I attacked missing A stabilizers, invalid physical relabeling, an incorrect six-orbit reduction, discarded B reflections, repeated corner indices, ambiguous ray arms, missing native far endpoints, accidental extra physical length equalities, improper transfer of the older exclusion, disappearing types in a defect-free limit, and confusion of necessary local support with global existence. The exact corrected artifact survives these attacks. The only repair needed was the prose canonical-table entry noted above; I reread the corrected entry and the complete synthesis before returning VALID.

Pairs with different five-length alphabets, different doubled values, other repeat separations, more length repetitions, or a pentagon remain outside this theorem. No tilability sufficiency for every metric in the surviving orbit is asserted, and the main unrestricted objective remains unresolved.
