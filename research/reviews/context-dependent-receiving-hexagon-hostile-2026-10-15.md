# Fresh independent review: arbitrary-context receiving-hexagon cuts

Date: 2026-10-15. **Final verdict: VALID.** I reread the complete exact [root-authored theorem](../lemmas/context-dependent-receiving-hexagon-obstruction-2026-10-15.md) and independently checked its geometry, angle identifications, midpoint invariant and both wedge branches. I contributed the shorter exceptional-branch inequality after independently attacking that branch; the root integrated it into the written proof, whose full statement and all other bridges are audited here. No solver or numerical search is a proof dependency.

## Exact claim and assumptions

The theorem excludes one common receiving-hexagon congruence class in the stated unit thin/thick Ammann source scheme, even when every proper donor-corner cut can depend arbitrarily on source context. Donor triangles (u_Z,h_Z), with 0<u_Z<1 and h_Z>0, and edge splits 0<m_Z<1 remain MARK-LOCAL. All source partitions are embedded and strict, donor nodes lie strictly inside their source rhombs, and all sixteen receiving precursor quadrilaterals are explicitly strict convex. Each receives proper cuts at exactly its two donor-node corners and remains a genuine six-corner convex polygon. Reflections are permitted.

The proof does not assume any external cut-angle or cut-distance invariance. It does not match pentagons or caps. It does not establish an unrestricted two-polygon impossibility theorem, and it does not cover changed source incidence, context-dependent donor triangles or splits, nonconvex precursors, improper cuts, or donor projections outside (0,1).

## Endpoint capacity and base angles

The actual arrow endpoint forms are unchanged by moving the split off the normal foot or changing cuts. They depend only on the retained source corner and incoming/outgoing donor-triangle base angles. I independently checked these forms in earlier reviews: thin endpoints are a=36+Xt-Yt,b=36+Yt-Xt,144,144; thick endpoints are c=108+Yt-Xh,d=108+Xh-Yt,72,72. They really occur as retained native H angles in both source parities.

The elementary capacity argument is valid: if a!=b, a,b>0 and a+b=72 make a,b,72,144 four distinct native H angles totaling 288. The other two are below 180 and cannot give total 720. Thus a=b=36 and Xt=Yt=beta. Given native angles 36,72,144, the three remaining H angles sum 468 and are each greater than 108. Therefore 36 and72 are UNIQUE native vertices. With c+d=216 one is at most108; the only available small values are36 and72, and36 would force its companion180. Hence {c,d}={72,144}, giving Xh=beta+36 or beta-36.

The thin arrow table puts each donor tail at an acute source corner36. Its internal donor apex lies strictly in that wedge, so 0<beta<36. The negative head branch is impossible. Therefore Xh=beta+36, c=72,d=144, while the Y head base angle is still unconstrained at this stage. No hidden equality of the two donor geometries has been assumed.

## The new opposite-diagonal invariant

After cutting the two opposite donor-node corners of a strict receiving quad, its vertex cycle is retained endpoint U, two external cut vertices, retained M, two internal cut vertices. Thus U and M are opposite vertices in its genuine six-cycle. Every Euclidean isometry of genuine convex polygons preserves the vertex cycle up to reversal and maps opposite vertices to opposite vertices.

In a thin X-tail H, retained U is angle36 and |UM|=m_X. In a thin Y-tail H it is angle36 and |UM|=m_Y. Since36 is unique in the common H, every such congruence sends these same native vertices and their opposites to one another. Hence m_X=m_Y.

The second comparison is also correct and does not confuse a tail split distance with a head split distance. Thick source A has two X arrows with tails at A; its retained endpoint angle is72 and |UM|=m_X. Thick source C has two Y arrows with heads at C; incoming and outgoing Y-head base angles cancel, leaving its source angle72, and |UM|=1-m_Y. Unique72 in H forces m_X=1-m_Y. Combined with the thin comparison, m_X=m_Y=1/2. Unit source-edge lengths and the internal split interval are used explicitly here.

These are intrinsic diagonals selected by a unique ANGLE vertex and its opposite, not an imposed vertex correspondence or a claim that the source edge is recognizable as a tile edge. Cut contexts play no role.

## Generic wedge branch and exact midpoint contradiction

Normalize any thin-tail receiver to U=0,M=(1/2,0), with source interior above its base. The external donor ray from U has direction -beta. The adjacent internal donor belongs to the other tail mark, whose base angle is the same beta, so its ray has direction36-beta. Proper corner cuts preserve these boundary tangent directions. Thus the two normalized thin X-tail/Y-tail hexagons have the same unordered tangent wedge {-beta,36-beta} at their unique36 vertex.

Any congruence fixes U and oppositeM and is therefore identity or reflection in their line. Reflection takes the wedge to {beta,beta-36}. For0<beta<36, equality of the unordered ray pairs occurs exactly at beta18; no angular wrapping is possible in that interval. If beta!=18, congruence is the identity.

Identity preserves vertex adjacency as well as coordinates. The external cut vertex adjacent to U is selected by the lower tangent ray, and the other external cut vertex is its next boundary neighbor, adjacent to M. Thus they are individually the same in the two normalized shapes even though their cut fractions were allowed to differ. Both external cuts lie below the base and both internal cuts above it. The two lines through U and its external cut, and through M and its external cut, meet exactly at the original external apex. They are nonparallel because U,M,t are noncollinear and the cuts are proper. Consequently the X and Y donor apex coordinates coincide, so their triangles agree and gamma_Y=gamma_X=beta+36.

I independently derived the chord threshold. In identical-donor coordinates t=L*exp(-i beta) and p=L*exp(i(36-beta)), where L=u/cos(beta). The chord tp is at distance L*cos18 from U along its normal of direction18-beta. Its positive base-axis intersection is therefore

    m_L=L*cos18/cos(beta-18)
       =u*(1+tan(beta)^2)/(1+tan(beta)*tan18).

Strict convexity puts M beyond this chord opposite U, so m>m_L. The unit donor triangle with tail beta and head beta+36 has

    u=sin(beta+36)*cos(beta)/sin(2beta+36).

Hence m_L=sin(beta+36)*cos18/[sin(2beta+36)*cos(beta-18)], exactly as stated. For0<beta<36 the denominator is positive and at most1. The numerator is strictly larger than sin36*cos18=sqrt(5)/4, because beta+36 lies strictly between36 and72, where sine increases. The exact identity follows from sin36*cos18=(sin54+sin18)/2 and the elementary golden-angle values. Since sqrt(5)>2, m_L>1/2, contradicting m=1/2. Every strict inequality and denominator sign is justified; no approximate trigonometric estimate is used.

## Exceptional beta18 branch

At beta18, the X head base angle is54. From the unit-base triangle, u_X=c=cos36 and h_X=c*k with k=tan18. This can be checked directly from h_X=u_X*k=(1-u_X)*tan54 and k*sin36=1-c. Write u_Y=v,h_Y=v*k; its geometry remains otherwise arbitrary.

For a thin acute tail receiver with external X and internal Y, the normalized points are U=0,t=(c,-ck),M=(1/2,0),p=(v,vk). The internal ray indeed has angle36-beta=18, so its x coordinate is v, not a different mark parameter. In the native order U,t,M,p, its strictly positive turn at M is

    k*((c+v)/2-2cv)>0.

Thus v<c/(4c-1)<1/2. The denominator is positive, and c>3/4 ensures all stated comparisons.

The Y apex lies left of the forced midpoint. Put delta=atan[vk/(1/2-v)] and gamma_Y=atan[vk/(1-v)], both principal angles between0 and90. The head half-apex is delta-gamma_Y, positive because the split is between base endpoints, and strictly less than delta. The function v/(1/2-v) increases strictly on0<v<1/2, giving

    theta_Yhead < atan[ck/(c-1/2)] <54.

The final inequality is exact: tan54=c/sin36, so it is equivalent to k*sin36<c-1/2. Since k*sin36=1-c, this is precisely c>3/4, true for c=(1+sqrt(5))/4. All atan arguments are positive and their denominators are positive, so no branch or inequality-direction mistake occurs.

At thick source C both incident arrows are Y heads, making the external and internal donor nodes equal in distance from C. Their angle at C is the retained source angle72. Triangle Ctp is isosceles with base angles54. Strict convexity of the receiving quad puts its opposite vertices C and M on opposite sides of chord tp, so the external head angle at t is strictly larger than54. This contradicts the previous upper bound and excludes the exceptional branch, whether its hexagon congruence would otherwise have been identity or reflection.

## Independence, rejected shortcuts and final verdict

I specifically attacked the thick72 tail/head roles, whether retained M remains opposite after arbitrary cuts, hidden cross-context pair invariance, source normal/reflection signs, the beta18 alternative, assignment of individual cut vertices under identity, apex reconstruction from edge extensions, the chord-intersection formula, its denominator range, and every exceptional-branch rational/trigonometric bound. The exact final artifact survives these attacks.

During this work I independently falsified the separate proposed bound that the thick cross-tail M angle always lies in(90,108). The retained [exact counterexample](../counterexamples/offnormal-cross-tail-m-angle-2026-10-15.md) has all four source partitions and sixteen precursor quads strict, with that angle in(108,114). It makes no common-H claim and fails the new midpoint invariant. Therefore it does not contradict this theorem. It confirms why convexity-only necessary-angle gates are weaker than the metric congruence argument. The root's final proof correctly does not use the rejected bound. Nor does it depend on the separate quadratic mirror algebra or any solver result.

The complete written proof closes the exact context-dependent-cut extension while its donor triangles and splits remain mark-local. A new construction must change one of the retained hypotheses rather than merely varying proper corner-cut fractions. Nothing here classifies arbitrary pentagon/hexagon pairs or resolves the unrestricted target.
