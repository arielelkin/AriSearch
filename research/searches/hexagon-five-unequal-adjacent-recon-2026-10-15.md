# Unequal-palette adjacent-repeat gate and five-case closure

Date: 2026-10-15. **Status: independently hostile-reviewed VALID; [whole-claim review](../reviews/hexagon-five-unequal-adjacent-hostile-2026-10-15.md), [standalone independent verifier](../reviews/hexagon-five-unequal-adjacent-independent-2026-10-15.py).**

The complete proof is [the unequal adjacent-repeat lemma](../lemmas/hexagon-five-unequal-adjacent-periodicity-2026-10-15.md). It concerns numerical exactly-five-length genuine convex hexagons with unequal palettes and at least one adjacent doubled pair. No main-problem resolution is claimed.

The native gate enumerates all 11,160 raw words: A=(0,0,1,2,3,4), B repeat separation 1,2,3, shared counts 0 through 4, all shared subsets and all 120 assignments of each palette. Directed native sectors allow union colors outside 0..4, repeated corner occurrences and independently reflected arm order. All three seam-slot and far-end multiset obligations are simultaneous.

Totals (no twelve-corner cover, component-color periodic escape, residual):

| B separation | No cover | Color escape | Residual |
|---|---:|---:|---:|
|1|3668|40|12|
|2|3656|64|0|
|3|3672|48|0|

The twelve residual words have four shared values, both repeats adjacent, and reduce to three ordered classes (four raw words each):

    B1=(0,0,1,3,5,4), B2=(2,2,1,3,0,5), B3=(2,2,4,0,3,5).

B2 and B3 are species swaps, with explicit retained maps. Thus there are only two unordered classes. The compact native certificate retains every residual word/map and representative native-state atlas, rather than all negative-word atlases.

Exhausting all 2^6 star subsets with restricted native-state closure gives exactly three B1 supports and one B2 and one B3 support, total five. For B1 the supports are two four-star partitions of all twelve native corners and their six-star union. The justified two-A/two-B positive domain has 22,680 pairings, 22,608 connected pairings, four trivalent torus gluings and two angle patterns. All three source supports have positive torus implications, retaining two actual positive gluings and twelve exact Fraction weighted-row identities. No larger quotient was searched.

B2 has one A and two B necessary corona states. Only B native side 5 against itself has uncertain guest state. At its native corner 4 the star (0,10,10) supplies an A bypass through both B native side-4 incidences, whose transitions are certain. B3 has two A and one B states. Only A native side 2 against itself is uncertain; star (2,2,6) supplies the bypass through both A native side-3 incidences. Thus the certain-transition adjacency graph is connected in each actual source. Indexed state maps propagate complete relative isometries and guest states, giving a discrete cocompact symmetry group and rank-two translations. The full proof explains source equality and the group argument.

Artifacts:

- [Native producer](hexagon-five-unequal-adjacent-recon-2026-10-15.py), [compact native certificate](../certificates/hexagon-five-unequal-adjacent-recon-2026-10-15.json).
- [Support/positive-witness producer](hexagon-five-unequal-adjacent-supports-2026-10-15.py), [five-case certificate](../certificates/hexagon-five-unequal-adjacent-supports-2026-10-15.json).

Both producers print full deterministic JSON by default; --summary is optional human-readable reconnaissance, and --output PATH explicitly writes the full retained JSON. They use exact integers and Fraction only. The second producer reuses the previously reviewed generic four-face authoring routine and this author's anchored-sector corona construction. This reuse is disclosed and does not constitute independent verification of the new application.

Fresh review should independently regenerate all 11,160 words, twelve residual maps, three ordered classes and two species-swap maps; the complete five-source-support domain; both actual positive tori and twelve Fraction identities; both finite corona-state domains and their unique-transition exceptions; and the two bypass connectivity arguments. Single-species sources, especially an opposite-repeat B source, need the separately reviewed monohedral escape before relying on twelve-corner coverage.

No additional research track or larger quotient search was started after this five-case closure. Main objective remains unresolved. A successful fresh review would combine this result with the existing nonadjacent unequal-palette and all common-five results to exclude all exactly-five-length hexagon pairs from aperiodicity; that synthesis should await review.
