# Second hostile review: context-dependent receiving hexagons

Date: 2026-10-15. **Final verdict: VALID on the exact stated construction domain.**

Reviewed the complete [theorem](../lemmas/context-dependent-receiving-hexagon-obstruction-2026-10-15.md)
and the [first review](context-dependent-receiving-hexagon-hostile-2026-10-15.md).
This reviewer did not supply the theorem's Section4 midpoint/head-angle
argument. I had previously checked an alternative quadratic mirror
obstruction and discussed the generic branch with root; I therefore state
that prior involvement explicitly. Here I independently reconstructed the
new exceptional branch from its coordinates, checked every inequality and
angle branch, and audited its integration into the entire written proof.
The first review's authorship of the short exceptional argument is not
used as evidence for that argument's validity.

## Exact claim and preserved hypotheses

The theorem excludes one common congruence class for ALL16 receiving
hexagons in the stated unit thin/thick rhomb source scheme. Donor triangle
coordinates and edge splits remain mark-local; 0<u_Z<1, h_Z>0 and0<m_Z<1.
Internal donor nodes lie strictly inside their source rhombs, all receiving
quads are strict convex, and proper cuts at the two donor-node corners
produce genuine six-corner convex polygons. Reflections and completely
context-dependent cut fractions are included.

These hypotheses are materially used. In particular, the proof does not
cover context-dependent donor triangles/splits, changed arrow incidences,
improper cuts, a receiving shape with collapsed vertices, different source
edge lengths, or allowing multiple receiving-hexagon classes. No cap or
pentagon congruence, global tiling existence, universal decoding or general
two-polygon impossibility statement is established.

## Independent endpoint and diagonal audit

I reconstructed the sixteen endpoint angle transfers directly from the
four arrow pairs on each rhomb, both donor parities, and both endpoints
of each receiving edge. With incoming base angle I and neighboring internal
donor base angle O, the boundary rays have directions -I and sigma-O,
so the retained angle is sigma+I-O. Symbolic evaluation gives exactly

    thin: 144, 36+Xt-Yt, 36+Yt-Xt;
    thick: 72, 108+Yt-Xh, 108+Xh-Yt.

Each species has eight endpoint contexts, including both mixed transfer
orders. Thus the angle ledger is complete, with no omitted reflected
context or assumption that X/Y donors already agree.

If a!=b, a+b72 with a,b positive makes a,b,72,144 four distinct angles
of H totaling288. The other two angles, each strictly below180, cannot
supply the required remaining432. Hence Xt=Yt=beta. Once H contains36,72,
144, its other three angles sum468 and each exceeds108. This indeed makes
36 and72 individually unique. The c+d216 argument correctly forces their
values to be72 and144. Strict inclusion of a thin-tail donor in its acute
36 wedge gives0<beta<36, excluding the Xhead=beta-36 branch.

The native vertex cycle after two opposite donor-corner truncations is
(U,externalcut1,externalcut2,M,internalcut1,internalcut2). Proper cuts and
six genuine corners are essential: U and M are opposite vertices of the
actual polygon. Euclidean congruences preserve this cyclic relation even
under reflection. Unique36 in thin X/Y-tail receivers therefore gives
mX=mY. Unique72 compares thick source A, where both arrows are X tails,
with thick source C, where both arrows are Y heads. The opposite-vertex
distances are mX and1-mY, respectively. Thus mX=mY=1/2. This identifies
actual diagonals from unique angles; it imposes no artificial vertex
matching and does not assume that the base diagonal is an H side.

## Generic branch audit

After normalizing U=0,M=(1/2,0), with source interior above the base, the
thin-tail boundary rays are {-beta,36-beta}. Reflection in UM changes them
to {beta,beta-36}; within0<beta<36 these sets agree only atbeta18. An
isometry fixing the two distinct points U,M has only the identity/reflection
alternatives. Thus beta!=18 forces identity between normalized X/Y
receiving hexagons.

The external cut vertices lie strictly below the base and the internal
ones strictly above it. Identity therefore identifies the two external
cut vertices individually, also preserving their adjacency to U and M.
The two original external edges are recovered by extending the appropriate
lines from U and M; they intersect at their donor apex because proper cuts
preserve both rays and the donor apex has nonzero height. Therefore the
X/Y donor triangles coincide even though none of their cut fractions were
assumed equal. Their common head angle is beta+36.

I rederived the chord threshold from t=L exp(-i beta) and
p=L exp(i(36-beta)), L=u/cos(beta). Their chord has normal direction18-beta
and distance L cos18 from the origin, so its base-axis intercept is
mL=L cos18/cos(beta-18). Strict convexity of(U,t,M,p) places M beyond this
chord, hence m>mL. Substituting the unit-base triangle's sine-law formula
gives exactly

    mL=sin(beta+36)cos18/[sin(2beta+36)cos(beta-18)].

For0<beta<36 the denominator is positive and no greater than1, while the
numerator is strictly greater than sin36cos18=sqrt5/4>1/2. This contradicts
m=1/2. No unproved angle-parameter existence, selected numerical beta,
cut invariance or generic-rank assumption enters this branch.

## Independent hostile audit of the NEW midpoint mirror branch

Set beta18, c=cos36 and k=tan18. The X head angle54 determines its unit-base
triangle by uX=c,hX=ck. Let the Y apex projection be v, so hY=vk. In a thin
acute context with external X and internal Y, rotating the internal
Y donor vector(v,-vk) by36 gives(v,vk): the identities are
cos36+k sin36=1 and sin36-k cos36=k. Thus the theorem's coordinate p is
correct and does not quietly assume uY=uX.

The quad order U,t,M,p is counterclockwise: its turn at U is positive
because t lies below and p above the base. Its strict M turn must therefore
be positive as well. Direct expansion yields

    det(M-t,p-M)=k[(c+v)/2-2cv].

Since k>0 and4c-1>0, this givesv<c/(4c-1). Because c>3/4,
c/(4c-1)<1/2, so every subsequent denominator involving1/2-v is positive.

For the Y donor triangle with apex(v,vk), both M=(1/2,0) and the head
H=(1,0) lie to its right and below it. Their downward ray angles are
-arctan[vk/(1/2-v)] and-arctan[vk/(1-v)]. Thus the actual head half-apex
angle is their positive difference

    thetaYhead=arctan[vk/(1/2-v)]-arctan[vk/(1-v)].

There is no supplementary-angle ambiguity: both principal arctangents
lie in(0,90), and the first is larger because1/2-v<1-v. In particular
this difference is strictly below its first term.

The function v/(1/2-v) has derivative(1/2)/(1/2-v)^2>0. Substituting the
strict upper bound vmax=c/(4c-1) gives exactly

    vmax/(1/2-vmax)=c/(c-1/2).

Therefore thetaYhead<arctan[ck/(c-1/2)]. The comparison with54 uses
positive quantities throughout:

    ck/(c-1/2) < tan54=c/sin36
    iff k sin36<c-1/2
    iff 1-c<c-1/2
    iff c>3/4.

The final inequality is exact since c=(1+sqrt5)/4 and sqrt5>2. Hence the
strict upper bound thetaYhead<54 is fully justified.

Independently, at thick C both incident arrows have Y heads. The two donor
apices are equal-distance points from C, with included angle72, so their
triangle with C has base angle54. In the strict receiving quad, the chord
tp is a diagonal; at external t it lies strictly inside the receiving
corner between tC and tM. Consequently angle(C,t,M)>angle(C,t,p)=54.
The first is exactly the Y donor head half-angle just bounded above. This
is a strict contradiction. It does not depend on whether the exceptional
hexagon congruence was identity or base reflection, nor on any chosen
truncation distances.

This checks every step of Section4 independently. The earlier quadratic
L>U obstruction is consistent but unnecessary and was not substituted
for the new written midpoint argument.

## Exact checks, defects and verdict

As an ancillary check, I used Sage exact number-field arithmetic with
4c²-2c-1=0 to verify the midpoint determinant identity, the vmax substituted
ratio, and its positive denominators. Exact real-algebraic arithmetic
verified k sin36=1-c, ck/(c-1/2)<c/sin36, and
sin36cos18=sqrt5/4. I also regenerated all sixteen symbolic endpoint
transfers from the arrow table. All checks passed; the mathematical
argument above supplies the proof without relying on a solver or floating
point decisions.

No defect requiring a mathematical repair was found. The scope statements
correctly separate this component obstruction from the original problem.
The preserved strict-quad fixtures do not supply common H and therefore do
not contradict the midpoint invariant. The falsified universal cross-tail
M-angle bound is explicitly absent from the proof.

**Verdict: VALID.** The complete theorem, including the independently
reconstructed beta18 midpoint branch, excludes arbitrary context-dependent
truncation cuts within the exact stated mark-local donor/split and source
incidence domain. The unrestricted two-convex-polygon problem remains
unresolved.
