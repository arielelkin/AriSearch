# Fresh independent review: complementary pp cone and specified carrier classification

**Verdict: VALID for both stated claims, with the necessity claim restricted to this fixed indexed carrier and the stated threefold A family.**

Reviewer: branching_hexagons, freshly assigned by root. Root proposed the fixed-carrier algebraic necessity and is not its sole reviewer. This reviewer did not develop the complementary branch. Reviewed [actual theorem](../lemmas/branching-hexagon-new-two-run-complementary-pp-periodic-cone.md), symbolic producer/certificate and noncentral development. The [independent checker](verify_branching_hexagon_new_complementary_pp_independent.py) imports no author module and executes no author producer. It reconstructs the geometry, topology and necessity equations independently.

## Positive cone: closure and strict geometry

The checker uses rational half-angle coordinates t=tan(delta/2),u=tan(alpha/2) over Q(sqrt3)(t,u). It constructs all actual native Cartesian edges from the physical directions, with p=2cos(delta), and verifies both raw closures and all12 edge norms identically. For B its first/third p edges cancel, and its q chain is the opposite of its remaining p edge. This is valid for every real parameter in the stated open cone, not just the developed fixture.

The indexed angle and turn forms are independently derived from the actual affine direction words with their360 wrap. They agree with the retained certificate. The closed parameter polygon has vertices(0,60),(0,120),(30,90),(30,30). Each turn is nonnegative on its four vertices, not identically zero, and has maximum below180. Thus each turn is strictly between0 and180 on the open domain0<delta<30,60-delta<alpha<120-delta. All lengths are strictly positive, since p=2cos(delta)>0.

The stated ordered closed-edge proof of strict convexity is valid throughout this domain. Relative to any directed edge the transverse components of successive edges have a positive run then a negative run, possibly with antipodal zeros. The first is strictly positive and last strictly negative. Closure makes their total0; every proper intermediate vertex height is strictly positive, including during the negative run because it is minus the remaining nonpositive terms with a strictly negative last term. Consequently all nonincident vertices have strict inward support, proving simple strictly convex native hexagons without sample continuity.

## Actual eight-face topology and global sufficiency

The checker verifies each actual unreflected/reflected face state, using vertex reversal-i mod6 and side-label reversal. It constructs the corner successor directly from the24 native reversed-boundary seam pairs. All48 side occurrences occur once, every matched label gives equal physical length, and the successor has exactly16 cycles of length3. Each actual cycle has angle coefficients(360,0,0) in constant/delta/alpha order.

The cycle types independently occur four times each: (A_high,B0,B1), (A_low,B2,B3), (A_high,A_high,B4), and (A_low,A_low,B5). Their corner classes match the retained certificate. The dual graph is connected and the reverse boundary gluings preserve consistent positive face orientations. Edges and the actual circular360 vertex links give nonsingular Euclidean neighborhoods. With16 vertices,24 edges and8 faces this is a compact connected orientable flat torus.

The complete simply connected Euclidean cover is the plane, tiled by lifted actual native faces with disjoint interiors. Its freely acting orientation-preserving Euclidean deck isometries are translations, because a nonidentity rotational isometry has a fixed point. Compactness yields a rank2 lattice. This proves the actual periodic edge-to-edge tiling at each cone metric. It is not an inference from a balance vector, a finite patch, or deformation of one drawing.

## Exact necessity for the fixed native-indexed carrier

The reviewer independently treats all six B angles as unknown while keeping A's specified alternating120+delta,120-delta angles. The actual16 link equations have rank4, and their augmented row space is precisely

    B0+B1=240-delta,
    B2+B3=240+delta,
    B4=120-2delta,
    B5=120+2delta.

There are no additional or missing link equations. This statement fixes A to the preceding threefold family and fixes the native side indexing/reflection convention. It is not a classification for arbitrary A angles or other seam pairings.

Put alpha=B1,beta=B2. Successive native turns force the displayed three p directions and q directions. Independently reconstructing those edges and rotating closure by alpha gives exactly

    p*(exp(i*alpha)-1+exp(-i*beta))+2cos(delta)=0.

The checker proves the raw Cartesian identity for arbitrary p,alpha,beta,delta. In positive half-angle variables u=tan(alpha/2),v=tan(beta/2), its sine difference factors exactly as

    sin(alpha)-sin(beta)=2*(u-v)*(1-u*v)/((1+u*u)*(1+v*v)).

Strict native convexity gives0<alpha,beta<180, so u,v are positive finite numbers. There are precisely two possible branches: u=v (beta=alpha), or u*v=1 (beta=180-alpha). The real closure on the equal branch gives p=2cos(delta)/(1-2cos(alpha)); with gamma=180-alpha this is the previously reviewed equal-pp cone. Its strict B3<180 inequality gives alpha>60+delta, exactly0<gamma<120-delta; all remaining strict angle bounds follow.

On the complementary branch the real p coefficient is-1, giving p=2cos(delta). The strict B0<180 and B3<180 bounds give60-delta<alpha<120-delta, and the other angle bounds follow. The branches intersect only at alpha=beta=90. Their separately verified closure, strict convexity and actual links prove sufficiency on both full domains.

No arbitrary binary tiling is assumed to contain this quotient; no chain condition or native-length word alone is promoted to those four link equations. The exact two-branch conclusion concerns only geometric data compatible with the specified carrier.

## Independent noncentral fixture and complete lattice domain

At delta15,alpha75 the checker reconstructs all raw native vertices exactly with real algebraic radicals, including p=2cos15=sqrt(2+sqrt3), and checks all native strict supports. It checks the retained cyclotomic reference vertices, all8 unit-rotation/direct-isometry placements and all24 opposite seam vectors and translational endpoint differences.

Every seam holonomy has integral coordinates in the retained period basis. The gcd of all2x2 minors of those integer coordinate vectors is1, proving the retained basis spans the entire primitive translation module rather than a proper-index subset. Exact motif area equals the period covolume and every face area is positive.

For every ordered pair of original faces, the checker maps all vertices through the inverse period matrix. Exact ceil/floor bounds on the two coordinate interval differences include every possibly intersecting lattice translate. All56 nonidentical candidates, maximum lattice index1, pass exact separating-axis inequalities. Translates outside these bounds have disjoint projections. Therefore all lattice face interiors are disjoint; motif-area/covolume equality and closed locally finite union prove full-plane coverage independently at this noncentral fixture.

Completed readonly replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_new_complementary_pp_independent.py

Output: PASS full complementary cone, all12 turn bounds,48 seam occurrences and16 actual links; PASS fixed-carrier rank4 necessity and exact two-branch closure; PASS8-face noncentral development, primitive integral lattice, exact area and all56 complete overlap candidates.

No substantive defect was found. Positive common scaling preserves both constructions. The open-domain boundary and all other binary-hexagon tilings remain outside this result; the unrestricted two-prototile problem remains unresolved.
