# Independent hostile review: adjacent-low octagon private-side obstruction

Date:2026-10-13. Reviewed claim: research/searches/resumed-higher-partner.md, pentagon P with five108° corners and octagon Q with adjacent108° corners and six144° corners; Q's108–108 native side length occurs neither on P nor elsewhere on Q. Claim: no unrestricted plane tiling exists. Reviewer developed the separate golden-triangle compiler mechanism and did not develop this theorem.

## Assumptions checked

The all-obtuse forcing dependency was read in full. Its hypotheses hold for both shapes; it rules out partial-side contacts and implies exactly three genuine corner sectors. Integer angle sums give precisely two108° and one144° at every star. Arbitrary rotations/reflections preserve these assertions. Native side equality at each edge is therefore mandatory.

The unique private side forces another Q through the same native side. Either endpoint correspondence leaves two108° sectors at both endpoints, so a third Q fills each remaining144° sector. The two nonprivate sides incident to the endpoints are distinct. Convexity implies each has a distinct placed neighbour: if any two different sides of one strict convex polygon were shared with one other convex polygon, the convex hull of those noncollinear segments would lie in both polygons and have positive area, contradicting interior-disjointness. Hence at least three distinct Q side-neighbours, at most five P side-neighbours.

At P any adjacent pair of P side-neighbours would give three108° sectors, impossible. Its cyclic neighbour word has at most two P slots, including the wraparound pair. Thus P has at least three Q side-neighbours. No checkerboard colouring or orientation convention is hidden here.

## Counterexamples attempted

- Reflected private-side matching: both ends retain108°, so it cannot avoid the third-Q inference.
- One third Q servicing both endpoints of the private side: it would share two distinct native sides of the initial Q, excluded by convex intersection.
- One neighbour sharing several edges or a nonstraight partial interface: whole native sides are forced and convexity excludes repeated neighbours.
- Sparse, omitted or nonuniform-density species: the window inequalities force both tile counts O(R), while coverage forces quadratic total growth, so no density-limit assumption is needed.
- Counting along boundaries: a fixed finite protoset has positive inradii and bounded diameter; tiles crossing a fixed-width square boundary strip are O(R) by disjoint inscribed-disc packing. Side and corner degree is bounded. Counting complete stars differs from native tile-corner incidence by O(R). This validates both the side inequality and5N_P+2N_Q=12N_Q+O(R).
- Exact metric fixture: independently reconstructed from support-line intersections over Sage AA, not from the author's tangent diagram. All vertices satisfy all support inequalities and strict orientation; cosine angle word is exactly108,108,144×6. Side lengths are t+u,2t,t+u,2u×5. Private2t is unique. The updated regular-P side2u matches exactly the five BB Q sides and differs from2t. The checker reconstructs that regular pentagon and verifies its exact side lengths.

## Defects and repairs

No unresolved mathematical defect found. No repair was proposed. The proof needs exactly the stated private-length hypothesis; dropping it invalidates the same-slot inference and this review makes no claim in that case. Distinct-length or nonadjacent-alpha theorems were not imported. No novelty claim is assessed.

The fixture check uses one exact algebraic object and no finite search or solver. Script: research/reviews/resumed-higher-partner-fixture-check.py. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed-higher-partner-fixture-check.py

Result: PASS: eight strict support vertices, exact angle word, unique alpha-alpha length, repeated others.

## Verdict

**VALID** for the stated entire private108–108 side family, including arbitrary other metrics, reflections, unrestricted contacts and omitted species. This is a restricted untileability theorem; it does not resolve arbitrary pentagon/higher-polygon pairs. Standard Euclidean local finiteness, the read all-obtuse lemma, and Sage exact real algebraic arithmetic are the remaining ordinary trust dependencies. No computation supplies the global theorem.
