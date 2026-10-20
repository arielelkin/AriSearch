# Independent hostile review: four-face residual periodic escape

Date: 2026-10-19. Verdict: **PASS, scoped to the conditional positive construction on the nine retained branching strata.** No author files were edited.

Reviewed the lemma, its producer, and JSON certificate. The producer replay passed. A separate retained checker, `hexagon-last-word-four-face-independent-check-sol-2026-10-19.py` in this directory, independently enumerates the domain using graph components rather than the producer union-find, and verifies every certificate rational identity using Python Fraction rather than Sage row-space operations.

## Exhaustion and topology

Color multiplicities are 8,6,4,4,2, giving 105,15,3,3,1 perfect matchings respectively. Their product times eight handedness assignments is exactly 113400. Fixing the first handedness removes the simultaneous reflection redundancy; same-face pairing is included. Independent enumeration reproduced the eight trivalent indices 10,40,88,9198,9264,14054,14078,42535, and exactly the six face-connected indices 40,88,9198,9264,14054,14078. It reproduced all retained native endpoint classes and triples, including selected witnesses 9198 and 9264.

The actual corner adjacency multigraph has degree two at each corner and connected three-corner components. Thus its geometric vertex links are circles, not merely classes of the right cardinality. The endpoint prescription reverses boundary orientation after the specified handedness changes. All faces are connected; the quotient is consequently a closed connected orientable surface with V=8,E=12,F=4, hence a torus. Both selected witnesses have all four handednesses positive. Each paired side was independently checked to retain its exact original color.

## Affine algebra

The checker reconstructs each source matrix from the SHA256-pinned resonance JSON and verifies that the masks are exactly all its uncovered_branching entries. For all 432 tests (6 candidates x 9 strata x 8 vertices), it checks either coefficient*M=target together with coefficient dot (4,4,2,...,2)=2, or a nonzero rational nullspace separation. It reproduces the displayed positive lists and selected witnesses. In particular, no unaugmented linear span implication is substituted for the affine angle equation. This review checks use of the retained resonance source; it does not independently reprove completeness of that earlier resonance census or its classification of arbitrary tilings.

## Metric and global step

For any actual polygons satisfying the hypotheses, equal colors give interval isometries of the actual physical edges. Native END-corner indexing in the checker agrees with the producer. The quotient metric is locally Euclidean at open faces and edges, and circular vertex links with certified total angle 2pi remove every cone singularity. Its compactness gives completeness. The simply connected complete flat universal cover develops isometrically onto the Euclidean plane. The lifted polygon interiors therefore cannot overlap; their union covers the plane. Deck transformations preserve orientation; a nontrivial orientation-preserving Euclidean isometry acting freely cannot be a rotation, so all nonidentity deck transformations are translations. Compact quotient then gives a rank-two lattice. Thus periodicity follows from the constructed torus itself; no unsupported finite-patch extension is used.

There is no need to solve vector closure again: existence of the genuine convex input polygons is a hypothesis, and their unchanged edge lengths and angles define the metric used here. No equality between distinct colors is introduced. This is a positive sufficiency result on nine angle loci, not a negative theorem about larger carriers, a proof that these loci are metrically populated, or a resolution of the unrestricted original problem. The separate defect-free limit and resonance coverage implications remain explicitly external dependencies.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-last-word-four-face-independent-check-sol-2026-10-19.py

Observed: INDEPENDENT PASS: 113400 domains; 8 partitions; 6 tori; 432 exact augmented/separator tests.
