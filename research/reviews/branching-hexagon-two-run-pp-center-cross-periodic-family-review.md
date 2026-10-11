# Fresh review: cross-slot pp-center periodic family

**Verdict: VALID for the full stated sufficient positive family.**

Fresh reviewer: branching_hexagons. Independently reviewed the actual [cross-family lemma](../lemmas/branching-hexagon-two-run-pp-center-cross-periodic-family.md), raw eight-face witness, and exact new geometric certificate. Root and structural_audit developed the construction; this is a fresh independent geometry/topology audit. The [independent verifier](verify_branching_hexagon_pp_center_cross_family_independent.py) imports no author module and derives native maps, symbolic equations, circular links and fixture geometry anew. The old balance primal and finite search failures are not proof dependencies.

## Full domain and quadratic branches

The native B directions subtract to turns60,60,psi+delta-60,180-chi,180-psi,chi-60-delta. The domain0<delta<30,60+delta<chi<180,60-delta<psi<180 makes each turn strictly between0 and180. Their sum360 fixes a single ordered revolution. The resulting native angles are exactly(240+delta-chi,120,120,240-delta-psi,chi,psi). All mixed bounds are strict as well. Positive p,q give positive edges. A closes by its alternating threefold orbits; B closes because its first-three-edge sum is2p exp(i60) and its last-three-edge sum is exp(i60) times the defining phase expression.

Closed ordered edges with these strict turns give full strict convexity. Relative to any chosen side, the subsequent normal projections are initially positive and subsequently negative, with at most antiparallel zero terms. Their total0 and the strict first-positive/last-negative terms ensure every partial sum at another nonadjacent vertex is positive. Thus the whole family has strict supports; no numerical or continuity argument is needed.

Rearrangement gives exp(i psi)=[-2p exp(-i delta)-exp(-i chi)]/[1-exp(-i chi)]. Since0<chi<180, the denominator cannot vanish. Independent polynomial expansion gives the cleared norm identity4p²+4cos(delta-chi)p+2coschi-1. Therefore every actual member occurs on one of the two displayed quadratic roots. Conversely a retained root has reconstructed unit Z, whose positive imaginary part and strict principal argument select the unique psi in(60-delta,180), and the defining phase follows exactly. Both roots, positivity filtering, discriminant-zero coalescence and angle filtering are explicit. No division by a tangent, singular unit, or assumed admissibility of a positive root is used. Equal lengths cause no defect in this positive construction.

## Reflected native indices and actual quotient links

There are two faces of each native species and chirality. For a displayed reflected polygon define its vertices by v'_j=conjugate(v_{-j}). Its directed side is-conjugate(e_{5-j}), so displayed side labels use old5-j; displayed corner angles use old-j. This independently derives both maps in the lemma. Although congruent to a reflected native polygon, every displayed face has counterclockwise boundary, making reversed-side gluings orientable.

The checker verifies all48 displayed native side occurrences appear once in the24 reversed pairs with equal actual lengths, using the converted mirror labels. The face graph is connected. It reconstructs endpoint-identification adjacency from each side pair, rather than trusting aggregated vertex classes. The16 components are all three-corner classes, and every link node has degree2; hence each is a single connected circular link. After native mirror conversion, all16 new angle rows sum identically(360,0,0,0) in(delta,chi,psi). The claimed A_L+B0+chi and A_H+B3+psi identities are distinguished from the same-slot construction's different endpoint formulas.

In particular positive B side3 mates a reflected B displayed side0, which is native side5, and positive side5 mates reflected displayed side2, which is native side3. These are the stated cross-slot qq-chain seams. At their endpoints mixed/qq slots are exchanged, not qq/qq. The reflection choices therefore implement the intended actual geometry rather than an abstract numerical star balance.

F8,E24,V16 gives Euler characteristic0. Connectedness, orientation and verified circular links make the compact quotient a torus. Its faces, seams and vertices all have ordinary locally Euclidean metric; the vertex links fill360 with positive sectors. Compactness gives completeness. The complete simply connected flat universal cover develops isometrically to the Euclidean plane. Orientable deck isometries act freely, ruling out every nontrivial rotation by its fixed center; thus they are translations. Properness and compact quotient give a rank2 lattice. Lifted closed faces cover the whole plane and their interiors are disjoint. This proves full-domain doubly periodic tilings, independently of fixture period calculations or finite search scope.

## Independent exact fixture replay

Embedded zeta24 directly in QQbar and constructed k=sqrt(1+sin²15)>0, p=(k-sin15)/2, and Z=(-2p exp(-i15)+i)/(1+i). Exact comparisons give0<p<1/2; Z is unit, its real part is positive and its imaginary part exceeds the real part. Thus45<psi<90, and the fixture satisfies all strict native bounds with chi90. Both qq angles are below120, so no repeated qq triple is homogeneous; their pair is not{90,150}. The exact cross phase equation is checked directly.

The radicand is not square in Q(zeta24), establishing the stated degree16 field. The verifier reconstructs the two native polygons and all eight direct or reflected displayed polygons. Each displayed reflected vertex equals the corresponding conjugated native vertex exactly. It checks every unit edge, converted angle-unit ratio, all192 displayed-face strict support determinants (48 per two primitive species, repeated under congruent placements), all retained reference vertices and eight tile areas. It then checks each retained developed face transform is a direct isometry, and every seam has opposite edge vectors and matching endpoint translation; all24 seam holonomies have trivial rotational part. Integral Hermite forms in the independent degree16 basis prove the primitive lattice has exactly the integral span of all these cycle holonomies. Its positive covolume equals the full8-face motif area and the retained certificate value.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_pp_center_cross_family_independent.py

PASS full cross phase/quadratic identities;48 sides,24 reversed pairs,16 independently reconstructed circular links360; both native mirror maps; degree16 fixture and192 displayed supports;24 translation holonomies; primitive integral period span and covolume=motif area.

No substantive defect remains. The result is a sufficient positive domain for this particular carrier, allowing every admissible quadratic branch and special parameter stratum. It does not classify all pp-center pairs or exclude any different carrier or qq-chain geometry. Search failures, exact positive seam primals and the unrestricted two-prototile problem retain their separate scopes.
