# Exact two-map periodic transfer: regular P5 / Q7(144,126)

Status: internally proved symbolic transfer; independent hostile review pending. Scope is exactly the two reviewed normalized 2P+2Q pairing maps at h=0, with their prescribed native edge labels. No further pairing search or larger inventory is used.

**Result.** For every real `h > -t`, BOTH fixed maps yield a periodic tiling of the entire Euclidean plane by the regular unit pentagon P and the first-gate heptagon Q(h). Thus the exact admissible parameter locus is the entire first-gate interval `(-t,infinity)`. In particular the periodic escape transfers to every member of this metric family. This excludes this whole family from the main aperiodicity objective; it does not classify arbitrary tilings or other polygon families.

## Exact geometry and admissibility

Set `w=exp(2*pi*i/20)`, using the distinguished complex embedding of `K=Q(w)`, `t=w+w^-1=2cos18°`, and `k=-(w^3+w^15)/w^9=2cos72°`, with `t>0` and `0<k<1`. Define P's vertices as partial sums of `w^(4j)`, j=0,...,4. Define Q's vertices as partial sums of

`1, (t+h)w^3, w^6, (t+kh)w^9, w^12, (t+h)w^15, w^18`.

All identities below are polynomial identities in `K[h]`; h can subsequently specialize to any real number, including transcendental values. The two closure identities are

`1+w^6+w^12+w^18+t(w^3+w^9+w^15)=0`,

`w^3+k*w^9+w^15=0`.

Let `x=h+t`. Its odd edge lengths are `x, (1-k)t+kx, x`; all are positive precisely on the declared domain x>0. The other edges are unit. The turns of Q are 36° at vertex0 and 54° at its other vertices, hence its interior angles are 144°,126°,...,126°. P has unit edges and turns72°. The replay additionally certifies strict convexity directly, without inferring it from a drawing: for each of P's 15 and Q's 35 nonincident vertex/edge tests, the signed cross product of the edge with the vector to that vertex is a nonzero polynomial with nonnegative real algebraic coefficients after substituting h=x-t. Every such cross product is therefore strictly positive for every x>0. These 50 exact polynomials and coefficient-sign certificates are retained in JSON. This proves simplicity, nonempty interiors and strict convexity throughout the full interval. At h=-t two QQ edges vanish, so that endpoint is inadmissible as this seven-sided strict-convex family; the requested domain excludes smaller h.

## Fixed maps, rotations, translations and every edge equation

Use faces F0,F1=P and F2,F3=Q, with counterclockwise native boundaries. Darts0,...,4 belong to F0;5,...,9 to F1;10,...,16 to F2;17,...,23 to F3, in native edge order. Map0 has the following pairs and start-minus-opposite-end displacement coefficients `(a,b)`, meaning `a L1+b L2`:

| Paired darts | Contact | (a,b) |
|---|---|---|
|0,5|PP|(0,0)|
|1,16|PQ|(0,0)|
|6,23|PQ|(0,0)|
|4,17|PQ|(0,0)|
|9,10|PQ|(0,0)|
|2,21|PQ|(1,0)|
|3,12|PQ|(0,1)|
|7,14|PQ|(-1,0)|
|8,19|PQ|(0,-1)|
|11,18|QQ|(0,-1)|
|13,20|QQ|(1,-1)|
|15,22|QQ|(1,0)|

Map1 is exactly the exchange of the Q face names: replace every dart10,...,16 by dart17,...,23 respectively, and conversely. The script stores each unordered pair with its smaller dart first. The first nine displacement coefficients in the table stay the same under this exchange; the last three reverse sign because sorting reverses their oriented pair. Both complete maps, equations, and vertex cycles are retained in JSON. No equivalence beyond this specified Q-name exchange is imposed.

Normalize a global direct isometry by F0=P. Choose face lifts along the spanning tree `(0,5),(1,16),(4,17)`, so these three edge displacements are zero. These are unit PP/PQ edges at every parameter, so their reversed-edge vector and endpoint equations determine rotations and translations without dividing by any parameter-dependent length. For map0 their unique solution is

`F0=P, F1=1-P, F2=1-w^6 Q(h), F3=w^6 Q(h)`.

Map1 exchanges F2 and F3. The rotations all have unit modulus. Before this normalization arbitrary face translations are allowed: for a paired native edge `(f,i),(g,j)`, with rotations r_f,r_g and translations c_f,c_g, its equations are

`r_f E_fi + r_g E_gj = 0`,

`r_f v_fi+c_f - r_g v_g,j+1-c_g = a L1+b L2`,

`r_f v_f,i+1+c_f - r_g v_gj-c_g = a L1+b L2`.

Here E is the native edge vector, and subscripts wrap cyclically. These are the full reversed-edge vector, start contact and end contact equations. Choosing lifts along a spanning tree is always legitimate for a translational quotient: recursively translate each new face lift by its current integral gluing displacement. The given tree then fixes the relative rotations and translations. The replay derives them from those equations, rather than assuming the h=0 values, and verifies all three equations for each of the twelve pairs as polynomial identities. Translations of individual representatives by lattice vectors change their lift descriptions only.

The resulting lattice is

`L1(h)=w*h+2w^4+w^2+2`,

`L2(h)=(w^7-w^5+w^3-w)*h+3w^6-w^4+w^2-3`.

Every vector and contact residual is identically zero. Thus neither edge closure nor rotational or translational holonomy forces h=0.

Reflections are allowed physically. They introduce no omitted branch here: the replay verifies the polynomial set identities `w^8 conjugate(Q(h))=Q(h)` and `w^6 conjugate(P)=P`. Any reflected copy of either polygon can therefore be expressed as a direct isometric placement with its induced native boundary relabeling. The maps themselves retain exactly their specified native pairing labels, as requested. The displayed direct placements already prove existence throughout the domain, independently of any completeness claim about other pairing maps.

## Vertex holonomy and positive lattice determinant

For map0, the vertex cycles of next-after-mate are

`(0,6,17), (1,10,5), (2,22,16), (3,13,21), (4,18,12), (7,15,23), (8,20,14), (9,11,19)`.

The first two are APP, with angle sum144+108+108=360; the six others are PBB, with sum108+126+126=360. These cycles are combinatorial and unchanged with h. Map1 has their Q-name exchanged cycles. For each cycle the sum of its directed endpoint displacements is the zero polynomial. This is the complete vertex translational holonomy check, in addition to the opposite-edge vector checks. Every corner has positive angle and the link of each quotient vertex is a single cycle.

Write `cross(a,b)=Im(conjugate(a)b)` and let `a0=sin36°=(w^3-w^7)/2>0`. The replay proves

`D(h)=cross(L1,L2)=a0*x^2+(4+k)*x+2*t+4*a0`, where x=h+t.

All three coefficients are strictly positive. Hence D>0 for every h>-t; there is no exceptional zero determinant within the interval. The replay also proves the polynomial identity

`D(h)=area(F0)+area(F1)+area(F2)+area(F3)=2 area(P)+2 area(Q(h))`.

All areas use the exact signed shoelace formula. Thus the rank-two lattice `Lambda(h)=Z L1(h)+Z L2(h)` is discrete for every claimed parameter. No sign is decided numerically.

## Whole-interval nonoverlap and coverage proof

This proof uses the quotient map and its degree, so no sampled overlap test is extrapolated to an interval.

For any fixed admissible real h, glue four abstract closed polygons by the map's twelve reversed-edge isometries, producing X. Every edge is paired exactly once; all vertex links are the eight three-cycles above. Thus X is a compact connected surface without boundary. Connectedness follows already from the PP/PQ spanning tree. Its polygon charts and gluing are oriented consistently because every boundary pairing reverses direction. There are 8 vertices,12 edges,4 faces, so its Euler characteristic is zero; it is an oriented torus. More directly for the argument below, X is locally Euclidean: at an edge two half-disks join, and at a vertex its consecutive positive-angle sectors have total angle2pi. The unchanged star cycles and exact vector/endpoint equations ensure these are consecutive sectors under the displayed placements, with no rotational or translation defect.

The explicit face placements descend to a continuous map `phi:X -> T=R^2/Lambda(h)` because both endpoints of every paired edge have exactly the same image modulo Lambda. On face interiors this map is an orientation preserving Euclidean isometry locally. Across an edge the two CCW face interiors lie on opposite sides of their oppositely directed common edge. At a vertex, follow its link cycle: each successive sector shares the next ray, all sectors occur with the consistent orientation, and their angles are positive and sum exactly2pi. Therefore they cover one small disk exactly once. These observations prove that phi is a local isometry, and in particular a local homeomorphism, at every point of X. They do not assume prior nonoverlap of distinct representative polygons in the plane.

A local homeomorphism from compact X has closed image; its image is also open and nonempty. Since T is connected, phi is onto. Compactness also makes it a proper local homeomorphism and hence a finite covering: around any point of T, its finitely many preimages have disjoint local inverse neighborhoods, and compactness excludes further sheets after the target neighborhood is shrunk. The number N of sheets is constant on connected T. Local Euclidean isometry implies `area(X)=N area(T)` by partitioning T into evenly covered measurable regions. The exact area identity above gives N=1. Consequently phi is a homeomorphism and a global local isometry.

It follows that the interiors of the four face polygons project injectively and disjointly to T, and their images cover T including every boundary. Lifting to R^2 shows that all polygons `Ff+m L1+n L2`, f=0,...,3 and m,n integral, have pairwise disjoint interiors and cover the entire plane. This proves both nonoverlap and full coverage for every h>-t, including possible incidental boundary contacts. Both nonzero lattice generators are translation symmetries. The entire argument applies to map1 after exchanging the two Q names.

## Exact computation record, assumptions and stop

Mathematical question: transfer these two specified reviewed maps over the complete real admissible interval. Finite combinatorial domain: exactly2 maps,12 paired edges and8 vertex cycles per map, plus50 convexity polynomials shared by both maps. Parameter arithmetic is symbolic over K[h], with exact ordered AA comparisons solely on the algebraic coefficients after h=x-t. This is not a sampled parameter search. The replay contains the two maps explicitly and imports no prior search code or certificate. There is no solver, random seed, symmetry enumeration, timeout or resource cutoff. Software: SageMath10.9. Completion: all polynomial and sign assertions pass; retained JSON is stdout of the successful complete replay. During script assembly an incorrect optional P reflection multiplier and JSON serialization failure were corrected; no claim depends on either failed run.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-heptagon-periodic-transfer-sol-2026-10-19.sage

Companions: same basename `.sage` and `.json`. The elementary compact local-isometry covering argument is supplied in full above; no external classification of tilings or computer-assisted topological claim is imported. Definitions of P,Q and the two maps agree with the [reviewed first gate](regular-pentagon-heptagon-144-126-first-gate-sol-2026-10-19.md) and [reviewed h=0 carrier](regular-pentagon-heptagon-minimal-torus-sol-2026-10-19.md), whose [hostile review](../reviews/regular-pentagon-heptagon-minimal-torus-hostile-sol-2026-10-19.md) is background rather than a premise of this script's polynomial checks. The only restriction h>-t is the family hypothesis; convexity, closure, all gluing identities, angle sums and rank two are derived and certified as described. The degree-one argument supplies the global step analytically.

Stop after this exact two-map transfer gate under protocol§5. No larger inventory or map enumeration, generic patch growth, Git operation, or discovery-log edit was performed. Independent Sol hostile review should attack convexity signs over the unbounded interval, reflection handling, pair orientation under Q exchange, tree normalization, local injectivity at quotient vertices, exact determinant/area identity, and the degree-one implication to full plane coverage. No assertion is made about all tilings admitted by the shapes; the periodic witness for each parameter suffices to exclude aperiodicity of this family. The original unrestricted two-convex-tile research problem remains unresolved.
