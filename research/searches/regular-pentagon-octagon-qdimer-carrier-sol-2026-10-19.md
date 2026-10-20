# Regular P5 / isolated AAABBABB Q8: two-Q periodic carrier

Status: exact positive construction, internally checked; independent hostile review pending. The isolated metric admits a periodic plane tiling and therefore is not an aperiodic partner of the regular pentagon. The unrestricted two-convex-polygon problem remains unresolved. No novelty claim is made.

## Exact shapes and dependencies

Let w=exp(2 pi i/20) in the distinguished embedding of K=Q(w), and L=-w^7+w^5-w^3+2w=2cos(18 degrees). Define P_i=sum_{j=0}^{i-1} w^(4j), 0<=i<5. Define Q_0=0 and Q_{i+1}-Q_i=l_i w^(e_i), with e=(0,2,4,7,10,12,15,18), l_3=l_6=L and all other l_i=1. Closure and strict supporting half-plane inequalities are checked exactly. All copies have positive orientation.

Read AGENTS.md, research-problem.md, research-protocol.md, the 20:22 Astra assessment and stop policy, the Q8 first gate, saturated-P-star report, reviewed minimal 2P+1Q carrier and its hostile review. The imported reviewed reductions force whole-edge contacts, only PPQ at A=144 degrees and PQQ at B=126 degrees, and exactly two nonconsecutive PP sides per P. Thus normalize every P's PP sides to {0,2}, with corner roles AAAAB. Reflected regular P copies introduce no additional congruence species.

## New structural gate and complete small domain

A translation quotient has p=2q. The one-Q obstruction is already reviewed: its QQ edges have directions w^7 and w^15 and cannot pair by translation. At q=2, neither Q can self-pair, so both QQ edges must pair across the two Q faces. Fix the first Q direct with rotation 1, using global isometry and reflection. The second is either direct Q or the positively oriented reflected walk R_i=conjugate(Q_{-i mod 8}). Its reflected QQ indices are (4,1), corresponding to native (3,6).

The four exhaustive QQ tests have the following relative rotation exponents modulo 20, computed independently from each edge reversal:

| Second Q | Matching from first indices (3,6) | Required exponents | Consistent |
|---|---|---|---|
| Direct | (3,6) | (10,10) | yes |
| Direct | (6,3) | (2,18) | no |
| Reflected | (4,1) | (14,10) | no |
| Reflected | (1,4) | (2,2) | yes |

Consequently the direct case forces a half-turn Q-dimer. Reflections also permit the displayed swapped-native-label matching. Omitting it would be an erroneous chirality restriction. In the final witnesses the reflected choice gives exactly the same second geometric polygon, with different vertex indexing; the script checks equality of these vertex sets.

Each Q has two public AA, two AB and two BA sides. Each normalized P has exactly one PQ side of each type: side 1 AA, side 3 AB, side 4 BA. Label the four P faces by the lexicographic order of the Q AA darts receiving their unique AA sides. This removes only P-face relabeling, not any placement. Their remaining PQ pairings are precisely a bijection to the four Q BA darts and a bijection to the four Q AB darts, since boundaries reverse. Thus each consistent QQ case has 4!^2=576 possibilities. Each P rotation is determined by its AA side; require the other two edges to yield the same rotation. Exactly one assignment per QQ case survives. Eight PP darts have exactly 7!!=105 pairings, including same-face possibilities. Their graph has degree two on four P faces; no connectivity or simple-cycle restriction is imposed prematurely. Every pairing is checked for direction reversal, then for its complete oriented vertex cycles.

Counts: four QQ tests, two consistent; 1152 PQ bijection pairs, two rotational survivors; 210 PP matchings, four rotational survivors; two correct-star maps, both with exact degree-one certificates. This is a complete domain at exactly (p,q)=(4,2), modulo P labels and a global isometry/reflection. No arbitrary larger quotient or local patch growth was performed.

## Explicit carrier and exact certification

The adjacent JSON records both maps, all 18 dart pairs, all 12 vertex cycles, six developed polygons, rotations, translations, lattice basis and every integral edge shift. Darts enumerate P0 sides 0..4, then P1, P2, P3, Q0 sides 0..7, Q1 sides 0..7. Hence it is a finite exact coordinate and gluing certificate.

For the direct witness, the six rotations are (w^6,w^8,w^16,w^18,1,-1), and translations are

    (0, w^4+1, 2w^6-w^4-2, w^6+w^2, w^6-1, w^6-w^4-1).

A positive lattice basis is

    L1 = w^6-2w^4-w^2-3,
    L2 = -3w^6-2w^2+2.

With cross(a,b)=Im(conjugate(a)b), exact arithmetic gives

    cross(L1,L2) = sum of the six positive face areas
                 = -13w^7+8w^5-3w^3+16w > 0.

Each paired edge satisfies both endpoint equations with one of the retained integer combinations of L1,L2. The script develops a spanning tree, verifies every remaining edge equation, and checks the area identity and its strict sign for both witnesses. It verifies the two native polygons are strictly convex; direct rotations and the reversed reflected walk preserve this property.

Here is the full nonoverlap and coverage argument, avoiding a bounded translate test. Glue the six oriented closed polygon disks by the 18 orientation-reversing edge pairings. Their face adjacency is connected (the development explicitly reaches all six). The 12 computed vertex cycles are single three-corner links, each either PPQ or PQQ, with total angle exactly 2pi. Thus the quotient is a compact connected oriented surface without boundary, locally Euclidean at faces, edges and vertices, and Euler characteristic 6-18+12=0. The developed coordinates modulo the stated lattice define a continuous local isometry to the flat torus: endpoint equations make this map well-defined; the single positive link of total angle 2pi gives local winding one at every vertex.

A local homeomorphism from a compact connected surface to the connected torus has open and closed image, so is onto and is a finite covering. Its degree is total face area divided by lattice covolume. The exact positive area identity makes that degree one. Therefore the map is a homeomorphism and local isometry. Its lift tiles the entire Euclidean plane with these polygon copies, with disjoint interiors and periods L1,L2. In particular distant overlaps and holes are excluded. The argument applies to both recorded encodings.

## Replay, scope and stop

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.sage

Completed under SageMath 10.9, exact cyclotomic arithmetic and distinguished QQbar sign tests; no numerical decisions, randomness, solver timeouts or continuous sampling. Initial internal run stopped at the deliberate positive-survivor guard before certification; the retained completed script certifies both survivors and writes JSON.

This closes this isolated metric by explicit periodic escape. It establishes neither any classification of arbitrary octagons nor any result for the unrestricted pair problem. Stop at this structurally derived carrier. No q>2 gate, Git operation, or discovery-log edit was performed. Independent review should attack the reflected indexing, completeness of the AA-dart normalization, vertex link permutation, exact endpoint and area identities, and local-isometry degree-one argument.

## Direct witness edge table

The row shift (a,b) means T_f[i]-T_g[j+1]=T_f[i+1]-T_g[j]=a L1+b L2, with cyclic side indices.

| First face:side | Second face:side | Shift (a,b) |
|---|---|---|
| P0:0 | P1:2 | (0, 0) |
| P0:2 | P2:2 | (0, 0) |
| P1:0 | P3:0 | (0, 0) |
| P2:0 | P3:2 | (1, 0) |
| P0:1 | Q0:0 | (0, 0) |
| P0:3 | Q1:7 | (0, 0) |
| P0:4 | Q0:5 | (0, 1) |
| P1:1 | Q0:1 | (0, 0) |
| P1:3 | Q0:4 | (0, 1) |
| P1:4 | Q1:2 | (-1, 0) |
| P2:1 | Q1:0 | (0, 0) |
| P2:3 | Q0:7 | (0, 0) |
| P2:4 | Q1:5 | (0, -1) |
| P3:1 | Q1:1 | (-1, 0) |
| P3:3 | Q1:4 | (-1, -1) |
| P3:4 | Q0:2 | (0, 0) |
| Q0:3 | Q1:3 | (-1, -1) |
| Q0:6 | Q1:6 | (0, -1) |
