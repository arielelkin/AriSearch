# Fresh independent Sol review: two further universal support omissions

Date: 2026-10-19. Verdict: **PASS within the stated restricted-support scope.** No author files were changed.

Reviewed the two-more-universal-omissions lemma, four-support structural checker, retained signed-star and 39-metric certificates, prior seven-support gate, and the reviewed general equal-antiparallel strip theorem. The positive implications are valid for every closed strictly convex metric satisfying the specified native support equations. The negative claims about the remaining two supports are appropriately limited.

## Exact algebra and native indexing

Independently assembled augmented rational matrices from the sorted retained signed atlas, without importing the structural checker or its rowspace code. Exact rank-extension tests give augmented ranks 6,6,5,5 for masks 20774,22550,33416,41032 respectively; coefficient and augmented ranks agree, so the affine systems are consistent. The complete atlas was separately reconstructed by the existing independent checker, which passed for all 180 words.

For20774, the augmented rows imply a3=b5 and a4+a5+b5=2. Consequently A has both consecutive triple sums2. For22550, the six displayed consequences in the lemma all pass independent exact rank-extension tests, and both species have both triple sums2. Exhaustion of the20 triples per species agrees with the producer: precisely the two A blocks for20774, all four A/B blocks for22550, and none for33416 or41032. The producer also exhausts all15 within-species equalities and finds none for the latter two masks. The right-hand side convention is correct: augmented rows [coefficients,rhs] annihilate [angles,-1]. Handedness changes no interior-angle contribution.

Corner j lies between sides j and j+1. Thus the turns at corners0,1,2 carry the direction of side0 to side3. A triple sum2 gives an exterior-turn sum1 in units of pi. Strict convexity makes each turn positive; side3 is antiparallel to side0. Both native words assign color0 to sides0 and3, so their lengths agree for every admitted positive metric, even when distinct colors happen to have equal numerical lengths. There is no indexing or distinct-length loophole in the positive theorem.

## Universal geometric implication

The cited general strip proof supplies an actual tiling for every such hexagon. Rotate side0 east. The positive turns put sides1,2 strictly upward and sides4,5 strictly downward. Equal antiparallel sides give the common strip period v=P3-P1=P4-P0 with positive vertical component. Therefore the two lateral two-edge chains are graphs over height. The analysis shear making v vertical preserves convexity and conjugates translations and halfturns back to translations and Euclidean halfturns of the original polygon.

In sheared coordinates the chains lie on opposite sides of the positive-width slab between side0 endpoints. Repeating the polygon by integer multiples of v covers precisely a strip, with disjoint tile interiors. Each two-edge periodic boundary is invariant as a set of segments under its edge-midpoint halfturn: the halfturn swaps its two vertex classes and reverses the incident edges modulo v. Alternating the strip and its right-boundary halfturn, then translating by w=2(cR-cL), creates successive strips with disjoint interiors. The positive transverse component of w and bounded periodic boundary deviations force coverage of every horizontal line. The two periods are independent. Undoing the shear yields two translation-lattice representatives, each congruent to the original metric polygon.

This establishes the A-only periodic omission on20774 and each separate A-only/B-only omission on22550. Metric existence is unnecessary for the conditional implication. Neither angle equations alone nor area equality are being substituted for Euclidean coverage.

## Remaining-mask boundary

The row1 fixture has precisely the stated angles and radical lengths. The structural checker verifies both mask equations on this row. The independent39-metric verifier reconstructs its vectors over Q(sqrt3), proves closure, positive pairwise distinct lengths and strict convexity via all directed-edge halfplane tests, and directly tests all equal opposite-edge candidates. Neither species has H1; its A first triple is330 degrees and its B first triple390 degrees. Thus nonlinear metric closure does not universally restore H1 on either33416 or41032.

For distinct numerical color lengths, only opposite pair0,3 is equal in either native word. The finite dihedral H2 test requires an opposite equality and a distance-two equality simultaneously; every one of its12 indexings fails for each word. The two possible H3 adjacent perfect matchings also fail for each word. These are necessary length-pattern failures for the named constructors, not a claimed classification of arbitrary monohedral or mixed tilings. Numerical coincidences between colors could change these negative length arguments; the lemma explicitly restricts them to distinct colors.

The affine identity failures and one closed counterfixture establish exactly the stated boundary. They do not show that all remaining metrics fail H1, that the remaining support families have no periodic escape, or that no mixed template exists. Combining these two implications with the prior three universal support omissions leaves33416 and41032 unresolved. The unrestricted two-convex-tile problem is not settled.

## Replay

Executed independently in the prescribed arisearch environment:

- `python research/searches/hexagon-five-four-four-support-structural-gate-2026-10-19.py` — PASS, all four masks and H2/H3 label tests.
- `python research/reviews/verify_hexagon_five_four_39_omissions.py` — PASS, all39 exact strictly convex pairs and retained certificate equality.
- `python research/reviews/hexagon-five-four-forced-dimer-independent-check-2026-10-19.py` — PASS, independently reconstructed all180 fixed atlases and associated incidence data.
- `python research/reviews/hexagon-five-four-metric-independent-check-2026-10-19.py` — PASS, all446 supports, seven minima, corona counts and digest; retained UNKNOWN is not a feasibility conclusion.
- An independent inline Sage rational rank-extension calculation against the retained sorted22-star atlas — PASS for every displayed20774/22550 implication and all single-species triple tests.

Each command was prefixed with `mise exec -- conda run --no-capture-output -n arisearch`. No nonlinear solver or enlarged geometric search was used. The structural checker has no separate new certificate; its exact reconstruction and assertions are the replay evidence, with the previously retained certificates providing the atlas and counterfixture.
