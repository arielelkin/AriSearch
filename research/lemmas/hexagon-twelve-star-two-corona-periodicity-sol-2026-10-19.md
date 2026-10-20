# Twelve-star two-corona changed word: universal periodic escape

Date: 2026-10-19. Author: Sol. Status: exact replay and [independent Sol hostile review](../reviews/hexagon-twelve-star-two-corona-periodicity-hostile-sol-2026-10-19.md) PASS. Restricted to A=(0,1,2,0,3,4), B=(0,0,1,1,2,3), with five pairwise distinct positive common numerical lengths. Both input polygons must be actual closed simple strictly convex Euclidean hexagons. Reflections and unrestricted contacts are admitted, and species omission is allowed.

## Restricted theorem

If this fixed pair tiles the plane, it admits a rank-two periodic tiling. No claim about other B words or the original unrestricted two-polygon problem is made.

**Dihedral relabeling corollary.** Keeping A fixed, the restricted theorem also holds for each cyclic shift or reversed cyclic shift of B=(0,0,1,1,2,3). Direct exact comparison with the reviewed180-row atlas verifies that its twelve full-corner-cover rows having twelve signed stars and two formal AA-dimer coronas are exactly this twelve-word orbit:

    (0,0,1,1,2,3), (0,0,3,2,1,1), (0,1,1,2,3,0),
    (0,3,2,1,1,0), (1,0,0,3,2,1), (1,1,0,0,3,2),
    (1,1,2,3,0,0), (1,2,3,0,0,1), (2,1,1,0,0,3),
    (2,3,0,0,1,1), (3,0,0,1,1,2), (3,2,1,1,0,0).

A cyclic shift changes only the chosen starting native side; reversal changes the traversal direction of the same physical polygon. Since reflected copies are admitted, normalize any of these words to the representative, apply the restricted theorem, and restore the native labels. This transfers periodic existence for the actual fixed polygons and requires no new metric or extension assumption.

## Exact support gate

The replay reconstructs the reviewed forced-AA-dimer atlas for precisely this B word: twelve signed stars and two formal boundary coronas. It exhausts all4096 subsets without symmetry reduction. Necessary predicates are full native-corner cover, an opposite-end continuation within the support for every selected seam, and every factor of at least one witnessed corona supplied by a selected star.

Exactly ten supports survive:

    1622,1879,2216,2473,2732,2989,3322,3579,3838,4095.

The inclusion minima are2216 and1622. The two coronas are witnessed by six and eight supports respectively, with overlap permitted. Every survivor contains a minimum; no upward-closure assumption is needed. Angles below are in units of pi; native corner i ends side i and starts side i+1.

| Minimum | Signed-star indices | Exact consequence |
| --- | --- | --- |
|2216|3,5,7,11|(a0,b0,b1), (a1,b2,b3), (a2,a3,b4), (a4,a5,b5) each sum to2.|
|1622|1,2,4,6,9,10|a0+a1+a2=2, hence a3+a4+a5=2.|

The certificate retains full augmented rational row reductions and every consecutive triple consequence. Minimum2216 forces no consecutive triple row for either species. This absence does not establish absence of monohedral periodic tilings; the mixed carrier below already supplies periodic escape.

## Universal escapes for actual metrics

For1622, the consecutive triple equation makes A sides0 and3 antiparallel. They have equal color0 length. Apply the reviewed universal equal-antiparallel-side strip construction imported in [the fixed-word synthesis](hexagon-five-four-fixed-native-unrestricted-periodicity-sol-2026-10-19.md) and proved in [the two further omissions](hexagon-five-four-two-more-universal-omissions-2026-10-19.md). It applies to every actual closed strictly convex metric with this equation and supplies a monohedral rank-two periodic tiling by A.

For2216, use four faces: faces0,1 are positive A and faces2,3 are negative B. The twelve native side pairings are

    (0,0;2,0), (1,0;3,0), (0,1;3,2), (1,1;2,2),
    (0,2;2,4), (1,2;3,4), (0,4;3,5), (1,4;2,5),
    (0,3;1,3), (0,5;1,5), (2,1;3,1), (2,3;3,3).

Each side appears exactly once. Each pair has equal numerical length by its native color. Pair oriented boundaries with reversed parameter. Opposite face signs identify matching native endpoints; equal signs identify exchanged native endpoints. The exact checker constructs all native-corner links and verifies eight degree-two triangular circles, precisely the four displayed2216 angle triples twice each. It also verifies connected face adjacency and V=8,E=12,F=4. Thus the quotient is a connected closed oriented torus. The literal pairing pattern comes from the reviewed33416 carrier, but this replay verifies it afresh for the new B word, including all changed native colors; similarity is not the proof.

These are discs made from the actual polygons, whose vector closure is assumed as part of being the input polygons. Equal-length gluing gives Euclidean neighborhoods across edges. Each circular vertex link has angle2pi by the2216 equations, giving Euclidean neighborhoods at vertices. Hence the compact quotient is complete and flat with no cone points. Its simply connected complete universal cover develops isometrically onto the Euclidean plane, and the lifted polygon discs cover with disjoint interiors. The oriented torus deck group is Z^2 acting freely by Euclidean isometries. Nontranslation orientation-preserving Euclidean isometries have fixed points, so all nonidentity deck transformations are translations. Discreteness and compact quotient give two independent periods. This proves an all-metric mixed periodic escape without any finite-patch extension inference.

## Transfer from an unrestricted plane tiling

Use exactly the reviewed defect-free trivalent edge-to-edge limit and imported monohedral periodic classification recorded, with their review provenance and scope, in [the fixed-word unrestricted synthesis](hexagon-five-four-fixed-native-unrestricted-periodicity-sol-2026-10-19.md). If an unrestricted tiling exists, the limit uses these same fixed actual polygons. If only one species occurs, the imported monohedral hexagon classification supplies a periodic tiling by that species.

If both species occur, every native corner occurs. A side5 has color4 absent from B and from other A sides, forcing AA pairs. Endpoint-preserving reflection would put two native(3,4) corners together and require a(3,3) corner at a trivalent endpoint; neither word contains one. Thus AA mates are midpoint halfturns, as in the reviewed atlas. Reflect the entire source if needed to normalize one dimer's handedness.

Take S to be all actual signed native-corner stars anywhere in this source. No restriction on global tile orientations is used. The complete local atlas pruning retains every actual star because its actual remote seam endpoints supply retained continuations at each pruning stage. Both species give twelve-corner cover. Every seam has an actual remote endpoint in S, and a chosen actual AA dimer supplies one completely witnessed formal corona. Repeated exterior tiles or other identifications only strengthen the actual requirements; the upper predicate relaxes those identifications. Therefore S is one of the ten enumerated supports. It contains2216 or1622, whose angle equations hold for the actual fixed metrics. Their respective universal carriers give a periodic tiling of the same admitted pair. This proves the restricted theorem.

## Replay and stopping scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-twelve-star-two-corona-support-sol-2026-10-19.py

Artifacts: [exact checker](../searches/hexagon-twelve-star-two-corona-support-sol-2026-10-19.py), [certificate](../certificates/hexagon-twelve-star-two-corona-support-sol-2026-10-19.json). No solver, metric sample, enlarged collar, broader B-word sweep, or inferred plane extension was used. Both minima force universal periodic escapes, so the conditional request for a surviving exact metric does not arise. Independent hostile review is pending; this file claims no review PASS.
