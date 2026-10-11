# A non-affine rational deformation cone with two physical hexagon branches

**Status:** adversarially reviewed as valid in the [independent hostile review](../reviews/branching-hexagon-rational-deformation-review.md), with a [no-author-import exact checker](../reviews/verify_branching_hexagon_rational_deformation_independent.py). No novelty claim. This is a sufficient periodic family outside the completed 120-degree metric cone, not a general classification or solution of the unrestricted problem.

## The exact family

Take three real parameters a,c,r and define directed edges

    E0=(a,0), E1=a(527,336)/625, E2=c(-3,4)/5,
    E3=(6c/5-1327a/625,264a/625),
    E4=c(-3,-4)/5, E5=a(7,-24)/25.

Define a second list

    F0=r(117,-44)/125, F1=-E4,
    F2=(1679a/625-9c/5-117r/125,
        672a/625-4c/5+44r/125),
    F3=E3, F4=-E1, F5=E5.

Let A and B start at (0,0), with vertices obtained by cumulatively adding their E and F lists. All coordinates are rational linear expressions in the parameters. The family domain is the open cone

    a,c,r > 0,
    750c < 1129a,
    30(c+r) > 47a,
    Q=2670a^2-2929ac+275ar+750c^2-330cr > 0.           (1)

**Theorem.** Throughout (1), both lists define genuine strictly convex hexagons. They admit a doubly periodic plane tiling with two A and two B faces per torus. Along A side0 there are two whole-tile locally compatible neighbor patches, one using A and one using B. The patches have pairwise disjoint interiors throughout (1). If A and B are noncongruent, these are different physical neighbor choices even after intrinsic symmetries are quotiented. The A-mate branch has the proved periodic extension. No infinite extension of the B-mate branch is asserted.

Set b=|E3| and s=|F2|. In the open subdomain where the five positive lengths a,c,b,r,s are pairwise distinct, the numerical side words are

    A=(a,a,c,b,c,a), B=(r,c,s,b,a,a).                   (2)

Both shapes have trivial intrinsic symmetry, are noncongruent, and neither shape alone admits an unrestricted plane tiling. Thus this subdomain gives genuinely branching, nonmonohedral pairs with a periodic escape.

## Closure and convexity over the entire cone

Both edge sums vanish identically. Put theta=arccos(3/5) in (0,pi/2), and t=2theta. Then 90<t<135 degrees: cos(t)=-7/25, which lies strictly between cos(135 degrees)=-sqrt(2)/2 and cos(90 degrees)=0. The latter comparison follows by squaring 7/25<sqrt(2)/2. Let gamma be the direction of (-3,4), lying between 90 and 180 degrees.

The fixed A edge directions, starting at zero, are

    0, 2t-180, gamma, direction(E3), 360-gamma, 180+t.

Here 0<2t-180<90, gamma=180-arctan(4/3), and 360-gamma=180+arctan(4/3). The y component of E3 is positive. Its x component is negative because

    6c/5 < (6/5)(1129a/750) < 1327a/625.

Also

    cross(E2,E3)=c(4516a-3000c)/3125 > 0.

Thus gamma<direction(E3)<180. These six directions are strictly cyclically ordered with every consecutive turn less than 180 degrees. For example the gap between gamma and 2t-180 is less than 180 since both lie between 0 and 180; the largest remaining potentially nontrivial gap, (360-gamma)-direction(E3), is less than 180 because direction(E3)>gamma>90.

The B directions start at 3t/2-180 (the direction of (117,-44)), followed by direction(-E4)=180-gamma. The two cone inequalities give

    cross(F1,F2)=4c(-47a+30c+30r)/125 > 0,
    cross(F2,F3)=4Q/3125 > 0.

The sector between F1 and F3 has width strictly between 0 and 180 degrees, so these two strict cross products put F2 in its interior. The remaining directions are F3, F4 at 2t, and F5 at 180+t, followed by F0 at 3t/2+180. Their successive turns are all less than 180. For the first turn, cross(F0,F1)=24rc/25>0 and its forward gap is less than 180 since F0 lies between -45 and 22.5 degrees and F1 lies between 0 and 90. (In fact this fixed t makes F0 negative.) For F3 to F4, direction(F3)>gamma>90 and 2t<270. The closing F5-to-F0 gap is t/2 in (45,67.5).

For completeness, a closed nonzero edge list with cyclically ordered directions, every turn in (0,180), is strictly convex. Fix one edge. Cross products with later edge vectors are positive until the directions pass its antipode, then negative. The partial sums therefore initially increase and subsequently decrease to zero. Every nonadjacent vertex has strictly positive partial cross product: the first subsequent edge is positive, and the last preceding edge is negative, so neither endpoint of the increasing/decreasing sequence is attained early. Every nonadjacent vertex is strictly on the inner side of every edge. This proves simplicity and strict convexity without a drawing.

The specified t/pi is irrational. Otherwise exp(it) would be a root of unity, and its trace 2cos(t)=-14/25 would be a rational algebraic integer. Rational algebraic integers are integers, a contradiction. This irrational angle is fixed throughout the cone.

## Explicit torus and global plane coverage

Write Vj and Wj for the native A and B vertices. In particular V0=W0=0, V1=E0 and W5=V5=-E5. Place the four counterclockwise faces

    face0=A, face1=E0-A,
    face2=E0-V5+B, face3=V5-B.                         (3)

Central inversion preserves their counterclockwise orientations. Put

    u=E0+F0-2V5=(39a/25+117r/125,-48a/25-44r/125),
    v=E0+2E1+E2=(1679a/625-3c/5,672a/625+4c/5).       (4)

Pair these sides with reversed endpoint order; the final column is the translation added to the second face:

| First face,side | Second face,side | Translation |
| --- | --- | --- |
| 0,0 | 1,0 | 0 |
| 0,2 | 1,2 | v |
| 2,0 | 3,0 | u |
| 2,2 | 3,2 | u+v |
| 0,1 | 2,4 | 0 |
| 1,1 | 3,4 | 0 |
| 0,3 | 3,3 | v |
| 1,3 | 2,3 | -v |
| 0,4 | 2,1 | -u |
| 1,4 | 3,1 | u |
| 0,5 | 3,5 | 0 |
| 1,5 | 2,5 | 0 |

All 24 endpoint equations are identities, independent of parameter values. One useful derivation is W4=V5+E1, W3=V5+E1-E3 and W2=F0-E4. These identities imply every row directly.

The true circular links, obtained by following a paired outgoing edge and its mate's next corner, are

    (0,0),(1,1),(3,5);  (0,1),(2,5),(1,0);
    (0,2),(1,3),(2,4);  (0,3),(3,4),(1,2);
    (0,4),(2,2),(3,3);  (0,5),(3,0),(2,1);
    (1,4),(3,2),(2,3);  (1,5),(2,0),(3,1).

Each is a three-corner circular link. The displayed placements, translated according to the seams, align the incident rays around each such link and return the first ray to itself. Equivalently the rotational holonomy of every link is the identity. Each corner sector has positive angle less than 180 by strict convexity. Therefore the sum of the three angles is a positive integer multiple of 360 and is less than 540; it is exactly 360. This justifies all variable-angle stars; the proof does not substitute the old 120-degree angles.

The closed side-paired surface is orientable and connected, with V=8,E=12,F=4. Hence it is a torus. Its Euclidean polygon metric has no vertex cone singularities and is complete because the torus is compact. Its universal cover is complete, simply connected and flat. Developing the flat charts gives a local isometry onto the Euclidean plane; completeness makes that map a covering, and simple connectivity of the plane makes it a global isometry. The lifted whole faces consequently form a plane tiling with disjoint interiors. This proves infinite extension, rather than presuming it from the local seam equations.

The zero-shift seam graph connects all four faces. The seams with shifts u and v consequently produce holonomy loops, and every seam shift belongs to Zu+Zv. Directly,

    det(u,v)=2 area(A)+2 area(B)>0,
    area(A)=768a^2/625+5308ac/3125-12c^2/25,
    area(B)=1368a^2/625-5158ac/3125+12c^2/25
            +122ar/125+168cr/625.

Thus u,v are independent translation periods of the developed tiling. The quotient need not be a minimal period cell.

## Two actual branch patches

The fixed isometries are

    R=[[-7/25,24/25],[-24/25,-7/25]],
    H=[[-527/625,-336/625],[-336/625,527/625]].

R rotates by -t; H reflects in the line of direction t. Put G=E0-W5+B. The two four-tile patches are

    A branch: A, E0-A, W5-B, G;
    B branch: A, R*B, H*B, G.

They match A side0 to the mate's side0 or side5, respectively. Every contact below is a complete native side; reflected endpoints are compared as unordered pairs to avoid a boundary-orientation error.

| Branch | Five full-side contacts |
| --- | --- |
| A | A0/mate0, A5/left5, mate1/left4, A1/G4, mate5/G5 |
| B | A0/mate5, A5/left5, mate0/left0, A1/G4, mate4/G5 |

The fixed relevant angles are A corner0=t, A corner1=360-2t, B corner0=180-t/2, B corner5=t. At the left seam endpoint the three A-branch convex corner cones are [0,t], [2t,360], [t,2t]. At the right endpoint A, mate and G occupy [2t-180,180], [180,180+t], [180+t,180+2t]. These partitions prove all pairwise interior separations involving the seam tiles by convexity.

For the B branch, the left endpoint cones are [0,t], [-180+t/2,0], [t,180+t/2]. Their widths are t,180-t/2,180-t/2 and they partition the full circle. At the right endpoint A, mate and G have the same cones as just displayed for the A branch. Again the entire polygons lie in their endpoint corner cones.

For both branches, the left filler lies in x<=0 and G lies in x>=a. For the A left filler this follows from [t,2t] being contained in [90,270], since 90<t<135. For the B left filler [t,180+t/2] is also contained in [90,270]. The cone of G, [180+t,180+2t], lies in [270,450]. Thus the filler pair has disjoint interiors as well. This proves separation of every pair of whole tiles uniformly over (1).

## No monohedral escape in the distinct-five-label subdomain

Use the independently reviewed defect-free-limit theorem from [hexagon limits](hexagon-limit-and-periodicity.md): any tiling of fixed convex hexagons admits an edge-to-edge trivalent limit tiling. Applied to a monohedral source, the limit still uses only that shape. This explicitly covers unrestricted partial contacts and reflections in the original tiling.

At a trivalent full-edge vertex, the three ray lengths x,y,z require native corner-length pairs xy,yz,zx. Reversing or reflecting a face preserves its unordered corner pairs.

A's corner graph from (2) is {aa,ac,bc}. The actual bc corner cannot belong to any three-ray star using this graph: b has only neighbor c and neither bb nor cc is available. Thus A cannot tile alone.

B's graph is {ar,rc,cs,sb,ba,aa}. Its actual rc corner cannot belong to any star using this graph: r has neighbors a,c while c has neighbors r,s, giving no permissible third ray. In particular ar exists but ac does not. Thus B cannot tile alone.

The length multiplicities of A and B are 3,2,1 and 2,1,1,1,1, proving noncongruence. The cyclic A word has only one possible nonidentity dihedral symmetry, a reflection exchanging corners0 and1. Their angles t and 360-2t differ since t!=120, so this is not an intrinsic isometry. B's four uniquely occurring labels exclude every nonidentity dihedral symmetry. The physically different A/B mates therefore survive every intrinsic symmetry quotient.

The complete mixed ray-length multisets are aaa,aab,aac,aar,abc,acr,bcs. This is only local corner-length legality. The constructed periodic quotient uses aaa,abc,acr,bcs twice each. No extension claim follows for the other local stars or for the B-mate branch.

## Exact asymmetric rational fixture

At a=1,c=3/4,r=3/2,

    A=[(0,0),(1,0),(1152/625,336/625),
       (3483/2500,711/625),(17/100,39/25),(-7/25,24/25)],
    B=[(0,0),(351/250,-66/125),(927/500,9/125),
       (2233/1250,672/625),(352/625,936/625),(-7/25,24/25)].

Their squared side lengths are

    A=(1,1,9/16,20933/12500,9/16,1),
    B=(9/4,9/16,50549/50000,20933/12500,1,1).

The five values 9/16,1,50549/50000,20933/12500,9/4 are strictly ordered and distinct. Periods are

    u=(741/250,-306/125), v=(5591/2500,1047/625).

A side0 is horizontal and side3 has nonzero vertical component, so these opposite sides are not parallel. Every 120-degree hexagon has all three opposite edge pairs parallel; affine maps preserve parallelism. Thus this pair is outside every affine image of the completed 120-degree cone. Its five-label repetition patterns also differ from the completed affine-mirror fixture.

## Computation, dependencies and scope

The [producer](../searches/branching-hexagon-rational-deformation.py) checks all 12 symbolic reversed-endpoint seam pairs, all eight three-corner circular links, area/covolume identities and all ten local-branch contacts. Its [retained certificate](../certificates/branching-hexagon-rational-deformation.json) records exact edges, vertices, periods, links, isometries and fixture comparisons.

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-rational-deformation.py

For the fixture, transform each of the four motif polygons into lattice coordinates. For each ordered motif pair, overlap is possible only at integer shifts in the exact coordinate bounds [ceil(min_i-max_j),floor(max_i-min_j)]. All 24 candidate translated pairs other than identical faces pass exact rational convex separating-axis checks. The area identity and closedness of the locally finite periodic union prove complete coverage. The 12 unordered pairs in the two local branch patches also pass independently computed rational separations. All 12 dihedral maps per shape are checked against the full pairwise squared-distance matrix.

The general cone proof uses convexity and the flat-torus construction, not extrapolation from the fixture. Imported dependencies are the elementary flat universal-cover fact and the specifically reviewed defect-free hexagon limit theorem for the monohedral exclusions. No monohedral classification is imported. The fresh independent hostile review found no unresolved defect; its checker reconstructs every formula without importing the author producer.

This closes a new explicit non-affine, irrational-angle family as a source of universal aperiodicity. It does not establish periodicity of every admitted tiling, global extension of every local branch, or impossibility for arbitrary repeated-side hexagons.
