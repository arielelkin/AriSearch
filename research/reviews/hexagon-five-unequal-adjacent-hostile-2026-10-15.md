# Independent hostile review: unequal five-length adjacent-repeat hexagons

Date: 2026-10-15. **Verdict: VALID** for the complete restricted theorem in [the lemma](../lemmas/hexagon-five-unequal-adjacent-periodicity-2026-10-15.md), and for the two-case corollary stated below. This is independent review by an agent who did not author either new producer, either certificate, or the theorem. The unrestricted problem remains unresolved.

## Exact claim and trust boundary

If two genuine convex hexagons each have exactly five distinct numerical side lengths, have unequal five-value palettes, and at least one doubled pair is adjacent, then unrestricted plane tileability implies an admitted doubly periodic tiling by the same unmarked shapes. The doubled numerical values may differ. Reflections, partial contacts, species omission and arbitrary orientations are allowed in the original hypothesis.

This review uses the previously reviewed defect-free hexagon limit, six/five formal-color source theorem, opposite-repeat monohedral two-face construction, and elementary discrete cocompact plane-group argument as named dependencies. It does not reclassify arbitrary monohedral hexagons or rely on the older global-coordinate deterministic-state claim whose status differs. The complete indexed propagation argument needed here is reproduced in Section 7 of [the six/five formal-color source theorem](../lemmas/hexagon-six-five-formal-color-periodic-escape-2026-10-15.md).

## Independent finite reconstruction

The [standalone verifier](hexagon-five-unequal-adjacent-independent-2026-10-15.py) imports no author program, no existing review program, and no solver. It reads the two retained JSON certificates and reconstructs their proof-relevant domains using integer combinatorics and exact rational arithmetic. Its default mode writes no evidence.

For the initial native gate it enumerates unordered corner triples WITH repetitions and all eight independent choices of directed arms. For three sectors every ordering is a cyclic rotation or reversal of the sorted reading; reversing all arm choices supplies the reversed reading. Thus this independent enumeration covers every actual ordered trivalent vertex, including repeated numerical rays and reflected copies. It retains the actual native side slots and both endpoint corner multisets, not only colors. It matches the residual fixed atlases retained by the author.

Every actual vertex survives endpoint pruning: following any of its three physical full sides supplies a state with the same native slot pair and the computed other endpoint corners. Sorting seam records can add false positives but cannot remove an actual configuration. Connecting every surviving slot pair produces an upper graph for actual seam components. When a doubled pair is disconnected there, it is disconnected in the actual graph, giving six formal source colors on one species and at least five on its partner. The formal-color theorem explicitly permits equal numerical values on differently named colors, so this recoloring application is valid.

The verifier regenerates all 31 unequal palettes, all 120 assignments per palette and all three B separations: 11,160 raw words. It uses no initial symmetry quotient. The counts by B separation are exactly

| Separation | No twelve-corner cover | Six-color escape | Residual |
|---|---:|---:|---:|
|1|3668|40|12|
|2|3656|64|0|
|3|3672|48|0|

Every residual word, native-state count and retained pointwise equivalence map is checked. Each map is a bijection on the whole union palette and independently reads each side word dihedrally. A reflected side reading i -> s-i induces corner reading i -> s-i-1; this is a legitimate relabeling of the whole polygon, including its angle data. No equality between unequal physical lengths is introduced. The twelve words split into the three stated ordered classes, four each; the explicit species-swap maps give two unordered classes. The proof retains all three ordered classes and hence does not need a hidden swap inference.

For each of these three six-star atlases the verifier exhausts ALL 64 subsets, restricts the states to that subset, repeats simultaneous endpoint pruning, and requires both full corner coverage and equality of the surviving star set with the selected subset. It reproduces exactly 3+1+1 supports, with every retained microstate, corner count and species count. Equality with an actual source support is justified: restrict to its actual occurring star set; every actual state still survives, and no star outside that set was included. This does not claim that every formally admitted support is realizable.

## Positive B1 witnesses

The checker independently enumerates the fixed two-A/two-B gluing domain. Its vertex test uses cycles of the permutation “edge mate, then boundary successor,” rather than the author’s endpoint union/find. These cycles are circular vertex links. It obtains 22,680 pairings, 22,608 connected quotients, four trivalent torus candidates, and two distinct angle supports, exactly as retained.

More importantly, it checks both actual retained gluings directly: every side occurs once, all paired physical lengths agree, the face adjacency graph is connected, and there are eight circular links of length three. The oriented face cycles glue by reversed boundary endpoints, so the resulting closed surface is orientable with V=8,E=12,F=4. It is a topological torus even where a pairing is within one face; the circular-link test verifies the local manifold condition there.

For each of the three EXACT B1 supports, the selected positive witness has four target angle equations. The verifier checks all twelve retained Fraction combinations against every one of the 13 augmented coordinates, including the constants. Thus the actual source metrics give total angle 2pi at each quotient vertex. No numerical angle solving, generic-rank assumption or new polygon closure solve is required.

A compact surface glued from these actual Euclidean polygons is complete. The angle equations make it nonsingular and flat; its complete simply connected cover is the Euclidean plane. The lifted face interiors are disjoint and cover that plane, and the orientable flat torus has two independent deck translations. This is a positive unmarked tiling with the original shapes. Exhausting the 22,680 domain is an audit check; only the verified positive witnesses and source implications are needed for the theorem.

## B2/B3 complete corona propagation

The verifier reconstructs each host corner by fixing its native arm order and enumerating both orders and both independent arm orientations of its two guests. It then matches the guest-side and guest-corner ports at BOTH endpoints of every host side. They must name the same entire guest native side with its two distinct endpoints. It independently repeats reciprocal-state pruning and checks every corner option, every initial and fixed tile state, and every guest-state choice against the certificate. All actual indexed tile states survive these necessary tests.

For B2 there is one A state and two B states. Exactly B native side 5 is uncertain, with two guest-state choices across another B side 5. Checking all surviving seam states shows that its native corner 4 endpoint pairs with the other copy’s native corner 4, in star (0,10,10). The third tile A therefore joins the two B copies through their B native side 4 incidences. Both are certain transitions.

For B3 there are two A states and one B state. Exactly A native side 2 is uncertain, across another A side 2. Its corner 2 endpoint pairs with corner 2 in star (2,2,6); the third tile B joins both A copies through their A native side 3 incidences, again certain transitions. The checker verifies the endpoint multisets and unique bypass stars, not merely the repeated edge colors.

All other ports have precisely one guest-state choice; since the only uncertain matches are same-native-slot matches, every retained edge is certain in BOTH directions. Every deleted edge in the connected full-side adjacency graph has the stated two-retained-edge bypass, so the retained graph is connected.

An indexed frame and corona state fix the full relative neighbor isometry across a retained edge: ordered images of two distinct endpoints and the opposite interior half-plane determine exactly one plane isometry. A map between any two occurrences of the same type and finite state consequently propagates through the connected retained graph to a symmetry of the whole framed tiling. This includes reflected copies and polygons with physical symmetries; native endpoint indices are retained throughout. The image tiles cover the whole plane, so propagation produces a surjective symmetry, not merely a local embedding.

There are finitely many tile-state orbits, hence the symmetry group acts cocompactly. Local finiteness and the finite stabilizer of a compact polygon make it discrete. Its translation subgroup cannot have rank zero: the orientation-preserving subgroup would consist of commuting rotations about one center and be finite. It cannot have rank one: only four orthogonal maps preserve that lattice axis, leaving a group that cannot act cocompactly on the plane. Thus it has rank two. Finite states alone would not justify this conclusion; the verified connected certain-edge graph supplies the essential additional hypothesis.

## Omission, contacts and full quantifiers

The original unrestricted tiling is used only to obtain the reviewed full-side trivalent limit. This legitimately removes partial contacts for the chosen source without asserting anything about all original tilings. Fixed polygons have genuine corners and nonempty interiors, as required by that limit theorem.

A normalized adjacent-repeat shape has only pure corner multisets (0,0,0),(0,1,1),(0,5,5), so it cannot tile alone in such a source: its corners 2,3,4 would be missing. A separation-two five-length hexagon has no pure stars. An opposite-repeat partner has exactly its two three-corner pure triangles; occurrence of either makes its complementary triple sum 2pi and supplies the reviewed two-face monohedral periodic escape. This handles a source that omits A as well as any source containing such a pure B star. Outside that escape both species occur and all twelve native corners occur, justifying the complete-cover gate. Pure repeated-ray stars are not silently deleted from the adjacent atlas.

Different numerical values remain distinct throughout the native domain. The theorem does not extend to arbitrary identifications between its palette labels. Auxiliary actual-contact colors are introduced only after the defect-free source exists and are discarded in the final unmarked conclusion. No matching rule, chirality rule, prescribed tiling hierarchy, or forced use of both species has been added to the original problem.

## Corollary audit

**VALID:** whenever EACH of two genuine convex hexagons has at least five distinct numerical side lengths, unrestricted tileability implies an admitted DOUBLY periodic tiling.

There are precisely two cases. If either member has six distinct lengths, the already reviewed [six/five general theorem](../lemmas/hexagon-six-five-general-periodic-escape-2026-10-15.md) applies directly because its partner has at least five. If neither does, both have exactly five. Equal palettes are covered by the reviewed complete common-five classification. Unequal palettes with both repeats nonadjacent are covered by [the reviewed noncommon theorem](../lemmas/hexagon-five-noncommon-nonadjacent-periodicity-2026-10-15.md); the remaining unequal cases have an adjacent repeat and are covered by the present result. These alternatives exhaust the stated scope.

For precision, cite the six/five theorem for the doubly periodic conclusion in the first case. The broader arbitrary-partner six-distinct synthesis states only existence of a nonzero translation in its full scope. Together the broader synthesis and this corollary imply that a hypothetical aperiodic hexagon pair has no six-distinct member and has at least one member with at most four distinct numerical lengths. Neither theorem resolves that remaining hexagon family or any pentagon-containing pair.

## Replay and verdict

Executed successfully, exit status 0:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-unequal-adjacent-independent-2026-10-15.py

Output:

    PASS: complete 11160-word domain, 12 residual words, 3 ordered/2 unordered classes, all maps
    PASS: exact 22680-gluing domain, four trivalent tori, two retained positive witnesses and circular links
    PASS: all five exact supports, complete coronas, both two-edge bypasses, 12 augmented rational identities
    PASS: independent unequal-five adjacent-repeat finite proof inputs

No mathematical defect or repair was required. Remaining uncertainty concerns the unrestricted problem, not an unfilled step of this restricted theorem. No novelty or priority claim is made by this review. The reviewer did not modify either producer, either certificate, the registry, the discovery log, or Git state.
