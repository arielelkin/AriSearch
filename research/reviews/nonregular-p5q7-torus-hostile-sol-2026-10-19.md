# Hostile review: nonregular P5/Q7 four-face flat torus

Date: 2026-10-19. Verdict: **valid** for the periodic counterexample and its stated conditional symbolic transfer. Independent reviewer did not develop the construction. No discovery-log or Git changes.

## Exact claim and sources

Reviewed `research/searches/nonregular-p5q7-minimal-torus-sol-2026-10-19.md`, its search `.py` and retained `.json`, `nonregular-p5q7-torus-check-sol-2026-10-19.py`, and the exact metric source `nonregular-p5q7-palette-metric-sol-2026-10-19.py`. Read root AGENTS.md, research-protocol.md and research-problem.md. Claim: these exact two convex unmarked polygons admit a translationally periodic Euclidean tiling; this kills this candidate pair, not the unrestricted problem.

## Independent exact checks

Retained independent checker: `research/reviews/nonregular-p5q7-torus-hostile-sol-2026-10-19.py`. It imports neither the solver nor any construction module or search output. It reconstructs lengths in Q(zeta72), solves Q closure independently by cross-product determinant formulas, verifies positive lengths in the exact real embedding, both closures, prescribed turns and strict supporting-line convexity. It then checks every matched edge has the same actual algebraic length, rather than merely matching labels. All checks pass.

For each seam it constructs the direct rigid map rot=-edge_d/edge_e and its translation, and checks both reversed endpoint images and rot*conjugate(rot)=1 exactly. Thus oriented polygon interiors occupy opposite sides along each edge; native chirality is consistent throughout. In particular darts15 and22 join Q side5 with reversed 125/135 endpoints, as required; a reflected endpoint assumption is not being substituted.

The checker independently builds vertex classes by union-find on BOTH endpoint identifications of each seam, then compares each class to its sector-link traversal. The eight classes are {0,6,17}, {1,5,10}, {2,16,22}, {3,13,21}, {4,12,18}, {7,15,23}, {8,14,20}, {9,11,19}. Every class consists of three distinct sectors whose angles total360. Each link is one circle. Alpha has twelve disjoint two-cycles. Face adjacency is connected; F=4,E=12,V=8, hence Euler characteristic0. The original independent checker and full exact metric script also ran successfully.

## Global existence audit

The finite quotient is Hausdorff: it is a finite compact polygon gluing along full closed edges by isometries. Each edge interior has two half-disks, and the verified connected circular links with total angle2*pi give Euclidean disks at vertices. Interiors are already Euclidean. Boundary reversal makes the disk orientations compatible. Thus it is a compact connected oriented locally Euclidean surface, hence a flat torus (also from Euler0).

Compactness gives completeness. Its simply connected complete flat universal cover develops isometrically onto R^2: flat charts continue without monodromy on the simply connected cover; completeness lifts straight segments for their full length, giving a covering of R^2, and that target is simply connected. The developing map is therefore globally injective. This supplies the global step that finite patches alone would lack.

Deck maps are orientation-preserving Euclidean isometries acting freely. A nontrivial rotation has a fixed point, so all nonidentity deck maps are nonzero translations. Proper discontinuity makes their vector subgroup discrete; compact quotient forces its span to be two-dimensional, so the group is a rank-two lattice. Polygon interiors lift disjointly and develop congruently; the convex polygon closures are their completions. Their lifts cover the plane, including boundary points, with disjoint interiors. Consequently the deck lattice gives actual translational symmetries of the tile collection, with two P and two Q orbits per chosen lattice cell. A larger symmetry group would only strengthen the counterexample.

## Omitted cases and symbolic transfer

The displayed witness uses no reflections, already permitted under the problem definition. Additional reflected placements, non-edge-to-edge contacts or one-species tilings cannot invalidate existence of this periodic tiling. Search completeness, discarded timeout cases, and the statuses of the other seven reflection assignments are unnecessary to this conclusion. The search script records connectedness after finding a witness rather than encoding it, but the retained chosen witness is connected and independently certified; this does not affect existence.

The independent checker classifies all twelve pairs by native side. Same-species matches always use the same native side index. The only cross-species index pairs are (P1,Q6),(P2,Q4),(P3,Q2),(P4,Q0). These are exactly the four stated symbolic equalities, so the conditional transfer is valid for every strictly convex realization of the same native angle words satisfying them. Accidental further equalities or failure of distinctness of L,a,b do not break the witness. No transfer to angle words or metrics violating these hypotheses is justified or claimed.

## Defects, repairs and remaining uncertainty

No mathematical defect found; no repair proposed. The word “minimal” in filenames/title is not independently certified as a separate optimization theorem; the body correctly defines and uses an exactly2P+2Q witness, which is all the counterexample needs. No claim of literature novelty or unrestricted impossibility follows from this audit.

Replay (assertions must remain enabled):

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/nonregular-p5q7-torus-hostile-sol-2026-10-19.py

The reviewer ran this command and obtained PASS for exact metric and endpoint/link audit, with F=4,E=12,V=8. This review does not rely on rerunning or trusting the SMT enumeration.
