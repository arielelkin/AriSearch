# Fresh review: pp-center four-face periodic family

**Verdict: VALID as a full positive sufficient family on the stated indexed carrier.**

Fresh reviewer: branching_hexagons. Independently reviewed the actual [family lemma](../lemmas/branching-hexagon-two-run-pp-center-periodic-family.md), its raw four-face quotient and new certificate. Root and structural_audit conceived the metric closure; neither is the sole reviewer. The [independent verifier](verify_branching_hexagon_pp_center_family_independent.py) imports no author module, reconstructs geometry and topology from raw data, and ignores every old numeric native angle attached to the source quotient.

## Full geometry and branch domain

The exact domain is0<delta<30,60-delta<chi<180,60+delta<psi<180, real phase exp(i delta)(exp(i chi)-1+exp(-i psi)) with negative real value-2p, and p>0,q1. Equal lengths are permitted in this positive theorem. Native A closes because each of its two alternating edge orbits sums0. Native B has p-chain2p exp(i60) and q-chain exp(i(60+delta))(exp(i chi)-1+exp(-i psi)), so the phase equation gives actual closure, not just angle closure.

Independent subtraction of the native edge directions gives turns60,60,chi+delta-60,180-chi,180-psi,psi-60-delta, each strictly between0 and180 and totaling360. Consequently the displayed native angles are exactly(240+delta-psi,120,120,240-delta-chi,chi,psi). The mixed-angle bounds follow from the same strict domain. A's turns alternate60±delta and are also strict.

Closed positive edges whose directions make one strictly ordered revolution with each turn below180 form a strictly convex polygon here. For a selected side, the cross products of cyclic subsequent edges with that side are initially positive, then negative, with possible zero only at the antiparallel direction. Their total is0 by closure. The next edge is strictly positive and the preceding edge strictly negative, so every intermediate nonadjacent vertex has strictly positive partial cross-product sum. This proves all supports on the full domain, including special phase roots; no continuity from the fixture is used.

The quadratic parametrization is exact. Rearranging closure gives Z=exp(-i psi)=1-exp(i chi)-2p exp(-i delta), and independent expansion gives|Z|^2-1=4p^2-4Kp+1-2coschi with K=cosdelta-cos(delta+chi). Thus every actual family point appears at one of p=(K±sqrt(D))/2. Conversely the quadratic gives|Z|1, and the retained negative-imaginary/psi-bound tests select its unique phase(-180,0) with psi in(60+delta,180). They reconstruct the defining metric equation. Neither root is silently discarded; at D0 there is one retained candidate, and there is no tangent denominator, vanished unit vector or singularity in the quotient proof. Positivity and all strict bounds remain explicit rather than consequences presumed for every quadratic root.

## Native side pairs, actual links and global covering

The independent checker retains only the raw species A,A,B,B, native length labels, mirror flags, paired edges and endpoint-identification data. All faces have positive native orientation. It verifies each of the24 native side occurrences is used exactly once in the12 reversed pairs and that each pair shares its actual length. Face adjacency is connected.

From the two endpoint identifications of each reversed side pair, the checker constructs the vertex-link graph afresh. Its components are exactly the eight claimed three-corner classes, and every corner-link node has degree2. Each component is therefore one connected circular link, not a disconnected collection with the same aggregate angle sum. Using the new native symbolic angle rows in(delta,chi,psi), all eight actual links sum identically(360,0,0,0). There is no requirement chi+psi240 or paired qq geometry.

The edge gluings reverse native boundary orientation, so the connected quotient is orientable. F4,E12,V8 gives Euler characteristic0; the verified circular vertex links show it is a closed surface, hence a torus. Each polygon interior and seam has its ordinary Euclidean local metric, and every vertex is flat because its positive circular link fills360. Compactness makes the resulting flat metric complete. Its simply connected complete flat universal cover develops isometrically onto the Euclidean plane. The orientable deck group consists of orientation-preserving Euclidean isometries acting freely; a nontrivial rotation would fix its center, so each nonidentity deck transformation is a nonzero translation. Properness and compact quotient yield a rank2 period lattice. Lifted face interiors are disjoint and their closed faces cover the plane. This proves actual plane coverage and independent translations for every stipulated parameter, without a selected-fixture lattice formula or a local-to-global matching assumption.

## New exact fixture and retained arithmetic

Independently embedded zeta24 in QQbar, set r=sqrt3/2-sin15 and k=sqrt(1-r^2)>0, and derived p=(1/2+cos15+k)/2. Exact comparisons establish1/2<r<1/sqrt2 and p>1. Therefore psi195-arcsin(r) lies strictly between150 and165, and the metric equation follows exactly from exp(i120)-exp(i15)-k-ir=-2p. The qq arc is neither paired{90,150} nor homogeneous: the four repeated-angle sums are respectively315, greater than360, greater than405 and greater than450. This fixture belongs to the central pp branch left outside the one-noncentral obstruction.

The verifier checks the quadratic radicand is not a square in Q(zeta24), giving the stated degree16 field; decodes all retained coordinates in its independent embedding; constructs both native polygons; verifies all six angle-unit ratios and24 strict supports per species; and matches every stored reference vertex and tile area. It checks all four retained face transformations are actual direct isometries, all12 developed seam matches have equal opposite edge vectors and pure translation holonomy, and both endpoint equations have the same translation. In the independent degree16 basis, integral Hermite forms prove the advertised lattice has exactly the Z-span of all cycle holonomies, not just the same rational rank. Its positive covolume equals both the retained value and twice each species' area, hence the four-face motif area.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_pp_center_family_independent.py

PASS full phase/quadratic identities;24 native sides,12 reverse pairs,8 independently derived single circular links360; exact degree16 fixture;48 strict supports;12 pure translation holonomies; primitive integral period span; and positive covolume=motif area.

No substantive defect remains. The theorem is sufficient for this specified carrier/domain and includes both retained quadratic branches and their coalescence. It makes no necessity assertion for arbitrary pp-center geometry, no exclusion of other qq-chain branches or carriers, and no resolution of the unrestricted two-prototile problem.
