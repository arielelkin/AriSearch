# Exact minimal periodic carrier for the nonregular P5/Q7 pair

Status: **Explicit periodic certificate, independently hostile-reviewed valid.** Date 2026-10-19. See [review](../reviews/nonregular-p5q7-torus-hostile-sol-2026-10-19.md). The fixed pair is killed for aperiodicity.

## Claim and metric dependency

The exact polygons defined and verified in `nonregular-p5q7-palette-metric-sol-2026-10-19.py` admit a translationally periodic plane tiling with two copies of each per translation cell. Thus this particular pair cannot satisfy the aperiodic-pair target. This does not resolve the unrestricted two-convex-polygon problem.

Native counterclockwise angles are P=(115,115,100,110,100), Q=(130,130,130,125,125,125,135). Native directed side labels are P=(L,1,1,1,1), Q=(1,a,1,b,1,1,1). The metric dependency proves closure, strict convexity, and positive actual lengths. No floating-point decision occurs in this certificate.

## Exact gluing certificate

Take four oriented polygon disks P0,P1,Q0,Q1. Enumerate their directed boundary edges consecutively 0..4,5..9,10..16,17..23, each in native order. Let rho advance by one edge on its polygon. Glue each edge d to alpha(d), reversing its boundary parameter, where

    alpha = [5,16,21,12,17,0,23,14,19,10,9,18,3,20,7,22,1,4,11,8,13,2,15,6].

Alpha is a fixed-point-free involution and every matched pair has equal side label. In particular Q side5 pairs darts15 and22 with reversed endpoints, the legitimate same-chirality half-turn pairing of its125/135 endpoints.

The vertex cycles of rho composed with alpha are

    (0,6,17), (1,10,5), (2,22,16), (3,13,21),
    (4,18,12), (7,15,23), (8,20,14), (9,11,19).

The angles indexed by every cycle total exactly360 degrees. The darts in a cycle correspond to polygon corner tails. Opposite boundary gluing identifies the head of alpha(d) with the tail of d, explaining the permutation rho(alpha(d)). Connectivity under rho and alpha is checked. Consequently the quotient is a connected compact orientable surface without boundary, with F=4,E=12,V=8 and Euler characteristic0; every vertex link is one circle.

## Why this gives an actual periodic tiling

Glue the actual strictly convex Euclidean polygon disks with those equal-length orientation-reversing edge maps. Interior points are Euclidean; edge interiors have two Euclidean half disks; each vertex has exactly three sectors of total angle2*pi. Hence the quotient has an everywhere Euclidean metric, with no cone singularities. It is compact, therefore complete. Its universal cover is a complete simply connected flat surface, isometric to the Euclidean plane. One elementary proof develops its local Euclidean charts along paths: trivial fundamental group makes development single valued; completeness gives lifting of every straight segment, hence the developing local isometry covers the plane; the plane is simply connected, so that covering is an isometry.

Deck transformations preserve orientation because the quotient is orientable. An orientation-preserving Euclidean isometry is a translation or a rotation. A nonidentity rotation fixes a point, impossible for a nontrivial deck transformation. All deck transformations are therefore translations. Compactness forces their translation vectors to form a rank-two lattice. The lifts of the four polygon disks cover the plane with disjoint interiors because a covering map is locally injective and the original disks have disjoint interiors in the quotient. Each lifted disk is congruent to its original polygon: its developed interior is a single Euclidean polygon interior, and completion adds its boundary. Thus these lifts are a valid translationally periodic tiling. This proof does not assume that a locally legal plane patch extends; the finite closed flat surface supplies existence directly.

## Computation domain and replay

`nonregular-p5q7-minimal-torus-sol-2026-10-19.py` searches only quotients with exactly2P+2Q, allowing all eight reflection choices after fixing P0 native orientation. Variables pair the24 darts; constraints enforce equal labels, opposite-parameter boundary gluing, and three-cycles with angle sum360. No spatial coordinates or numerical tolerance are used. Z3 4.x exact integer/array SMT; recorded exact version is in the JSON. Seed0, timeout6000ms per reflection assignment. The retained JSON contains complete results of the optimized pass and witnesses. The first expression-heavy discarded implementation timed out in all8 cases; this is an implementation observation, not an UNSAT claim. No larger quotient search is authorized or performed.

The independent checker hardcodes just the displayed witness, reconstructs all native words, and verifies every involution, label, vertex, connectivity and Euler assertion without importing Z3 or the search output:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/nonregular-p5q7-torus-check-sol-2026-10-19.py

The search can be replayed separately:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/nonregular-p5q7-minimal-torus-sol-2026-10-19.py

The certificate depends only on the checker and metric verification, not search completeness, timeout behavior, or trust in Z3. The flat-surface argument is the necessary unbounded step.

## Conditional symbolic transfer

The same gluing works for any two strictly convex polygons with these native angle words whenever their corresponding native side lengths satisfy

    P4=Q0, P3=Q2, P2=Q4, P1=Q6.

Indeed the other paired edges always join two copies of the same native side: P0 to P0 and Q1,Q3,Q5 to their counterparts. The four equalities above are precisely the additional cross-species requirements. They need not all have unit length; neither L,a,b nor their distinctness is required for this periodic witness. (Distinctness matters only to separate shape-forcing arguments.) Each of the eight displayed vertex cycles retains total360 independently of these lengths. Thus all genuine strictly convex metric realizations of this same angle/edge-equality scheme admit this periodic escape. No assertion is made for metric realizations that violate these four equalities.
