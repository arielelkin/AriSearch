# Last word: four-face periodic escape on all nine branching strata

Date: 2026-10-19. Status: exact producer and replay PASS, with [independent Sol hostile review PASS](../reviews/hexagon-last-word-four-face-hostile-sol-2026-10-19.md). The original problem remains unresolved.

## Statement

Let genuine strictly convex hexagons have native words A=(0,1,2,0,3,4), B=(0,1,2,0,3,1), with a shared positive physical length for each color. Corners are at the END of the indexed side. If their angles satisfy the source rows of any of the nine branching strata in the retained resonance certificate, then the same unmarked polygons admit a doubly periodic plane tiling. No new metric realization is asserted. Distinctness of the five colors is permitted and no equality between different colors is introduced.

## Exact bounded gate

Reuse precisely the prior 113400 labeled pairing/handedness domain: two A faces, two B faces, every equal-color perfect matching, all eight handedness assignments after fixing the first face positive. There is no larger quotient search, no new corona search, no random seed, timeout, floating arithmetic, or numerical solver. Native endpoint gluing is opposite endpoints for equal handedness, equal endpoints for opposite handedness; these both reverse oriented face boundaries.

Eight candidates have eight corner classes of size three BEFORE face connectivity. Their enumeration indices are10,40,88,9198,9264,14054,14078,42535. Only SIX are connected:40,88,9198,9264,14054,14078. The two others cannot supply the required connected torus. Each retained corner adjacency graph is checked to be connected of degree two and hence a circular link. Face adjacency is connected. Oriented boundary reversal gives orientability, and Euler characteristic is8-12+4=0, so each retained surface is a torus.

Two row families suffice (each triple occurs twice):

* P: (0,1,8), (2,6,7), (3,10,11), (4,5,9), realized by9198 and14054.
* Q: (0,7,8), (1,2,6), (3,10,11), (4,5,9), realized by9264 and14078.

|stratum|selected labeled torus|all passing indices|
|---:|---:|---|
|3162|9198|9198,9264,14054,14078|
|3778|9198|9198,14054|
|3802|9198|9198,9264,14054,14078|
|3814|9198|9198,14054|
|27672|9264|9264,14078|
|27714|9198|9198,14054|
|27738|9198|9198,9264,14054,14078|
|27750|9198|9198,14054|
|27836|9264|9264,14078|

The JSON retains every gluing pair, handedness, corner class and vertex triple, all nine source matrices, every one of the6x9x8 row tests, and exact rational coefficients or separating rational nullspace vectors. Source row order is the two polygon totals followed by the stratum unsigned triples in their certificate order. The code checks coefficient*M=target and the augmented RHS identity coefficient dot(4,4,2,...,2)=2 in pi units. Thus the affine implication includes constants, not just an unaugmented claim. Equivalently x=alpha-2/3 makes every source equation homogeneous.

## Geometric sufficiency

Take the actual convex metric polygons, using reflected copies exactly when the certificate handedness is negative. Each paired side has the SAME original numerical color and therefore exactly equal physical length; glue by its endpoint-prescribed interval isometry. Each face interior and each open edge has a Euclidean neighborhood. Every circular vertex link has total angle2pi by the certified augmented identities, so every vertex also has a Euclidean neighborhood. The connected compact orientable torus therefore has a complete flat Euclidean metric. Its universal cover is the Euclidean plane; lifting its four polygon faces gives a plane tiling with disjoint interiors. The deck lattice of a flat torus supplies two independent translations. This is a positive construction for every metric satisfying the hypotheses, without a polygon vector-closure search or an assumption that a formal patch extends.

If an unrestricted tiling is the starting input, the separately reviewed [defect-free limit theorem](hexagon-limit-and-periodicity.md) supplies an everywhere-trivalent full-side source. When the exact resonance census places that source in one of these nine strata, its unchanged polygon angles satisfy the source rows, and the construction above gives a periodic escape for the same polygons. Monohedral cases and the other census strata require their separately stated reductions. This note does not silently impose mixed full corner cover on an arbitrary initial tiling.

## Replay and scope

Producer: `research/searches/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.py`.
Certificate: `research/certificates/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.json`.
The certificate pins the resonance source SHA256 and Sage version. All proof-relevant arithmetic is Sage QQ. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.py --check

Expected: CHECK PASS; EXHAUSTED113400 candidates6, followed by the nine positive lists displayed above. A nonpassing torus/stratum row test is only a bounded failed witness, and implies no absence of larger carriers or of tilings. Under protocol section5, this new explicit positive mechanism closes the nine specified angle loci; no enlargement of a blocked bounded search is authorized or needed. This is not a resolution of the full two-polygon problem and makes no novelty claim.
