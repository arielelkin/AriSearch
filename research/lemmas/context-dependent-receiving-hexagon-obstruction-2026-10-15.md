# Arbitrary cut contexts do not repair the receiving-hexagon construction

Date:2026-10-15. Status: independently hostile-reviewed VALID;
[first audit](../reviews/context-dependent-receiving-hexagon-hostile-2026-10-15.md) and
[second audit](../reviews/context-dependent-receiving-hexagon-second-hostile-2026-10-15.md). This is a restricted construction-component obstruction, not a
solution of the unrestricted two-convex-polygon problem. Degrees throughout.

**Stronger result:** the [arbitrary-physical-split theorem](context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md)
now excludes arbitrary split contexts as well as arbitrary cuts, with only
mark-local donor triangles retained. Its shorter thick-source proof avoids
the exceptional thin-wedge branch below.

## Exact construction domain

Use unit thin/thick rhombs, with source angles36/144 and72/108, and arrows

    thin: AB X A->B, BC X C->B, CD Y C->D, DA Y A->D;
    thick: AB X A->B, BC Y B->C, CD Y D->C, DA X A->D.

For each mark Z choose one donor triangle on a unit arrow T->H. Its apex
has coordinates(u_Z,h_Z), with0<u_Z<1 and h_Z>0, using the normal into its
donor rhomb. The triangle is the same in every context of that mark.
Choose one split M=(m_Z,0) on that arrow,0<m_Z<1, again mark-local and
independent of the apex projection. All source sectors are embedded and
strict, with each internal donor apex strictly inside its rhomb.

For every receiving edge form the two native quads(U,t,M,p),(M,t,V,q),
with external donor t and neighboring internal donor nodes p,q. Require
all16receiving quads across both rhomb species and both donor parities to
be genuine strict convex quadrilaterals. Truncate their TWO donor-node
corners by proper cuts, making genuine convex hexagons. Cut fractions may
now depend ARBITRARILY on source species, parity, mark and other context.
There is NO cross-context cut-angle or cut-distance invariance hypothesis.
The two retained native vertices of each hexagon are its original source
endpoint and the edge split M; they are opposite in its six-cycle.

**Theorem.** The16receiving hexagons cannot all belong to one congruence
class, even allowing reflections. Thus changing only the cut contexts does
not repair this three-sector/cap construction while donor triangles and
splits remain mark-local. The proof does not use cap or pentagon matching.

## 1. Endpoint angle capacity

Let Xt,Xh,Yt,Yh be the base angles of the two donor triangles at actual
arrow tails/heads. All are in(0,90). A retained receiving endpoint angle
is its source angle plus its incoming external base angle minus its
outgoing internal base angle. The complete native arrow table gives

    thin: a=36+Xt-Yt, b=36+Yt-Xt,144,144;
    thick: c=108+Yt-Xh, d=108+Xh-Yt,72,72.

Every value is a genuine angle of the common receiving hexagon H. Strict
convexity gives a,b,c,d in(0,180), a+b72, c+d216. If a!=b, the four DISTINCT
values a,b,72,144 occupy four native angles summing288. Two further
angles<180 cannot make the hexagon total720. Therefore a=b36 and

    Xt=Yt=beta.

H contains36,72,144; its other three angles total468 and are each<180,
so all three exceed108. Thus36and72 are UNIQUE native angle vertices ofH,
and every other H angle exceeds108. Since c+d216, one of c,d is at most108.
It must be36or72;36would make the other180, impossible. Hence

    {c,d}={72,144}, Xh=beta+36 or beta-36.

At an acute thin source corner both incident donor arrows have tails.
Their internal donor nodes lie strictly inside its36wedge, forcing
0<beta<36. Thus only Xh=beta+36 is positive, and c72,d144.

## 2. Unique opposite-vertex diagonals force every split to the midpoint

After truncating the two donor corners, a receiving hexagon has native
cyclic order

    (U,cut_on_tU,cut_on_tM,M,cut_on_pM,cut_on_pU),

possibly reversed. Its retained M is opposite retained U, independent of
the cut choices. Every isometry of genuine hexagons preserves adjacency
and opposite vertices.

Thin X-tail and Y-tail contexts have retained endpoint angle36. Because
this angle is UNIQUE inH, their congruences toH identify the same endpoint
and its same opposite vertex. Their common diagonal length is respectively
m_X and m_Y, since source edges have unit length. Therefore m_X=m_Y.

At thick source A, both incident arrows have X tails; the retained angle
is72and its opposite diagonal has length m_X. At thick source C, both
incident arrows have Y heads; the retained angle is72and that diagonal
has length1-m_Y. Angle72is also UNIQUE inH, so these diagonals agree:

    m_X=m_Y=1/2.

This metric conclusion uses no placement rule and no cut locality.

## 3. The generic wedge branch contradicts midpoint convexity

Normalize a thin-tail receiving hexagon by U=T=(0,0),M=(1/2,0), with its
source interior above the base. The external donor is below it. Its two
boundary tangent directions at the unique36vertex are

    {-beta,36-beta}.

These are the same in thin X-tail and Y-tail contexts. A congruence between
them fixes U and oppositeM. It is either the identity or reflection in
the base line. Reflection preserves this tangent wedge only if beta18,
as matching{beta,beta-36} to the original pair shows.

Suppose beta!=18. The congruence must be identity in this normalization.
It maps the external cut vertices individually: they are below the base,
while both internal cut vertices are above. The original external donor
is the intersection of line(U,cut_on_tU) and line(M,cut_on_tM). Proper cuts
and h_Z>0 make these distinct nonparallel lines. Thus the two marks have
identical donor coordinates u_X=u_Y=u,h_X=h_Y=h. Their head base angles
are equal, so each is gamma=beta+36.

Consider a thin-tail quad in these identical-donor coordinates. Write
r=tan(beta), t=(u,-h), h=ur, p=exp(i36)*t, and M=(m,0). The chord from
t to p meets the base at

    m_L=u(1+r^2)/(1+r tan18).

The strict turn at M, or the interior-diagonal criterion for the convex
quad(U,t,M,p), requires m>m_L. The unit donor triangle has

    u=sin(beta+36)cos(beta)/sin(2beta+36).

Substitution gives

    m_L=sin(beta+36)cos18 / [sin(2beta+36)cos(beta-18)].

For0<beta<36, the denominator is positive and at most1. The numerator is
strictly greater than sin36cos18=sqrt(5)/4>1/2. Therefore m_L>1/2,
contradicting the forced m=1/2. No generic wedge branch is possible.

## 4. The exceptional mirror wedge is also impossible

It remains to consider beta18. Then Xhead54, so the unit X donor has

    u_X=c=cos36, h_X=c k, k=tan18.

Write u_Y=v,h_Y=vk,0<v<1. At a thin acute tail context with external X
and internal Y, the native coordinates are

    U=0, t=(c,-ck), M=(1/2,0), p=(v,vk).

The strict turn at M is

    det(M-t,p-M)=k[(c+v)/2-2cv] >0.

Thus v<c/(4c-1)<1/2. In the Y donor triangle, M is to the right of the
apex projection v. Its head half-angle therefore satisfies

    theta_Yhead
      =atan(vk/(1/2-v))-atan(vk/(1-v))
      <atan(vk/(1/2-v))
      <atan(ck/(c-1/2)).

The last bound substitutes v<c/(4c-1); the rational function v/(1/2-v)
is strictly increasing there. Finally

    ck/(c-1/2)<tan54=c/sin36

is equivalent to k sin36<c-1/2, or1-c<c-1/2. This holds because
c=cos36>3/4. Consequently theta_Yhead<54.

But at thick source C the two Y-head donor nodes have equal distances
from C and retained source angle72. Their triangle with C is isosceles,
with base angles54. Strict convexity of the receiving quad places M
beyond its chord, so the external donor head half-angle MUST exceed54.
This is the geometric head bound reproduced in the independently reviewed
[mark-local-cut obstruction](offnormal-mark-local-truncation-obstruction-2026-10-15.md),
and follows directly by splitting a strict convex quad along its diagonal.
We have a contradiction. The exceptional branch is excluded as well,
proving the theorem. QED.

## Scope and independent audit obligations

No finite enumeration, SAT answer, numerical angle or coordinate sampling
is a proof dependency. The proof uses actual endpoint-angle transfers,
unique-angle opposite diagonals, complete plane-isometry alternatives,
strict native turns and elementary trigonometry. It permits ANY proper
context-dependent cut fractions. Its critical retained hypotheses are
mark-local unit-base donor triangles and splits, acute base projections,
the actual source incidences, proper two-corner truncations preserving
opposite retained vertices, and a single receiving-hexagon congruence class.
Changing those genuinely changes the construction mechanism.

The earlier off-normal strict precursor examples remain valid. They do
not supply a common receivingH and therefore do not challenge this proof.
The relaxed angleSAT example likewise is not a two-prototype realization.
The proposed universal cross-tail M-angle interval(90,108) was separately
falsified by an exact precursor and is NOT used here. A quadratic L>U
mirror-branch algebra check also exists but is unnecessary for this shorter
midpoint proof.

Fresh review must independently audit all retained-vertex diagonals and
arrow roles, the beta18 wedge alternative, donor-apex reconstruction,
the m_L formula and bound, and the exceptional beta18 head-angle inequality.
This is a construction obstruction, not an unrestricted impossibility
result for arbitrary unmarked convex polygon pairs.
