# Hostile independent review: single-type Ammann mean-site Voronoi gate

Reviewer: independent Sol agent. Date: 2026-10-19.

Claim reviewed: the three ordinary Voronoi rules retaining only H6, P1, or P2 arithmetic source vertex means, at J=1/2+(4/5)w, each fail the proposed two-class, at-least-five-corners gate in every legal reviewed Ammann source.

## Assumptions and attacks

Read the authoritative research problem and protocol. The unrestricted unmarked two-polygon problem is unresolved by this calculation. This review uses the previously reviewed exact source certificate, reconstruction, and arbitrary-depth legal marked-rhomb composition theorem as dependencies; it does not reprove that theorem or import aperiodicity into Voronoi cells.

Attacked source extendability, every-source occurrence, distant competitors, boundary-straddling missing source tiles, degenerate Voronoi corners, reflections and cyclic ordering. No defect identified.

The producer clips convex halfplanes exactly over AA and deletes zero turns. My independent verifier instead enumerates feasible intersections of pairs of competitor lines. For every retained cell it checks all finite same-type competitors, exact strict turns, the claimed corner count, coordinate minimal polynomials, and exact boundary separation. It compares complete pairwise vertex distance matrices under every cyclic shift and both orientations, independently of the producer's edge Gram test. The script reconstructs both rhomb patches, independently selects the entire radius-defined neighborhood, compares its exact typed decorated frames with the certificate and verifies every translated frame in the ninth subdivision of one red half.

## Mathematical cutoff and density audit

A finite cell whose vertices have norm at most B lies in the B-disk by convexity. A competitor at distance d>2B has positive slack d(d-2B) throughout that disk. Thus the exact checks 2B<4 and every omitted finite site farther than 2B suffice. A source polygon has diameter at most 2R, using its vertex-mean radius R. A missing tile intersecting the patch boundary cannot have its mean closer than boundary-distance minus 2R; a tile entirely outside cannot have its interior mean inside the patch. The strict boundary clearance therefore excludes every missing mean from the relevant disk. The artificial square contributes no edge since no output vertex touches it; the resulting bounded polygon is the actual unconstrained halfplane intersection.

For occurrence, every rhomb meeting the context disk has a vertex within an additional distance less than 2, so the retained radius criterion covers all decorations determining these contexts. Exact decorated frame matching gives an actual supertile embedding, without an assumption about centered sun extension. Iterating reviewed Lemma 6 ten times gives level-10 Robinson halves in each legal source. Both substitution colors contain a red child, yielding a level-9 red half carrying the embedded contexts. Unit Robinson-half diameters are less than 2; therefore each source point is within 2 phi^10 of one site of every retained type. Positive prototype interior inradii ensure uniform separation. Ordinary global cells consequently exist and are bounded.

Reversing a polygon negates and reverses its edge list; the global negation cancels from its Gram matrix, so the producer's reversal convention correctly allows reflections. Strict positive turns after deletion of collinear vertices certify genuine corners.

## Replay and verdict

Independent command:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-single-type-voronoi-independent-sol-2026-10-19.py

**Verdict: PASS / valid within the stated fixed-rule scope.** Independent replay completed successfully: H6 faces 75/73 have 6/4 corners; P1 faces 76/71/70 have 6/5/6 corners with the hexagons incongruent even allowing reflection; P2 faces 81/72/79 have 5/7/6 corners. All 209 independently selected decorated frames embed exactly. No repairs were required. No producer artifacts were edited. Remaining uncertainty is limited to the explicitly inherited source reconstruction and hierarchy dependencies, not a new extension or aperiodicity assertion.
