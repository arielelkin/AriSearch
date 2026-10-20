# Two twelve-star one-corona orbits: species separation

Date: 2026-10-19. Author: Sol. Status: exact finite certificate and [independent Sol hostile review](../reviews/hexagon-two-twelve-star-one-corona-pure-hostile-sol-2026-10-19.md) PASS.

Fix A=(0,1,2,0,3,4). Consider separately B=(0,0,2,1,1,3) and B=(0,1,0,2,1,3). Assume five distinct positive native color lengths and actual closed strictly convex hexagons. Every endpoint-closed signed trivalent native star in either word atlas is species-pure. Each atlas has twelve stars, four A-only and eight B-only, full native-corner cover, and one formal forced-AA-dimer corona. The two B dihedral orbits each have twelve elements and are disjoint. These assertions were rerun separately for all twenty-four words, with no word outside those orbits inspected.

## Finite calculation

The retained script imports the reviewed native atlas builder. Its domain consists of cyclic ordered triples of the twenty-four signed corner ports, with repeated corners allowed. It tests literal native-side color equality and iteratively deletes stars lacking opposite-endpoint continuation at any seam. All decisions are integer combinatorics. Every retained triple is checked to have a single species. There is no support-subset enumeration, metric query, solver timeout, randomness, or larger patch search. Certificate records both representative star lists, pruning rounds, formal coronas and all orbit words.

## Geometric implication

An edge-to-edge trivalent plane tiling by the given polygons has every actual signed star in the initial native atlas and in every endpoint-pruning iterate: the actual star at the opposite endpoint witnesses continuation. Thus actual stars lie in the fixed atlas. Any full A/B edge contact has mixed stars at its endpoints, contradicting species purity. The whole-edge adjacency graph of a locally finite polygonal edge-to-edge tiling of the plane is connected: join two tile interior points by a compact path perturbed to avoid vertices and cross edges transversely; local finiteness makes the crossed tile sequence finite. Consequently such a trivalent plane tiling uses only one species.

The reviewed defect-free hexagon limit and monohedral periodic classification, imported precisely as in `hexagon-five-four-fixed-native-unrestricted-periodicity-sol-2026-10-19.md` and its linked PASS review, therefore give the same restricted unrestricted-contact consequence as the reviewed ten-star case: if an actual pair in either word family tiles, it admits a periodic monohedral escape. This statement retains those imported hypotheses and dependencies. It makes no assertion that an arbitrary formal word or corona has a closed convex metric or extends to a plane tiling.

The all-species-pure first gate settles the assigned mixed-source branch. A 4096-support calculation and metric construction would have a vacuous mixed-source premise, so are not run. The original unrestricted two-convex-polygon problem remains unresolved; the 32-star/100-corona orbit is outside this work.

## Replay and restart

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-two-twelve-star-one-corona-pure-sol-2026-10-19.py`

Certificate: `research/certificates/hexagon-two-twelve-star-one-corona-pure-sol-2026-10-19.json`.

Exact remaining obligation for integration: fresh independent hostile verification of the finite purity assertion and imported-dependency application. No constructive candidate gate survives these two mixed ETE branches. Reopen only upon a concrete failure of the native-atlas hypotheses or a different geometric mechanism, not by extending bounded support enumeration.
