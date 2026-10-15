# Off-normal mark-local truncations cannot share one receiving hexagon

Date:2026-10-15. Status: independently hostile-reviewed VALID;
[full geometric review](../reviews/offnormal-mark-local-truncation-hostile-2026-10-15.md)
and [second independent audit](../reviews/offnormal-mark-local-hostile-2026-10-15.md). This is a construction-component obstruction, not a theorem for
arbitrary pentagon/hexagon pairs or a solution of research-problem.md.
All angles below are in degrees.

## Exact domain and claim

Use the unit thin/thick Ammann rhombs, with source angles36/144 and72/108,
and the native arrow table of the reviewed
[unequal-cut obstruction](../searches/unequal-arrow-cut-angle-obstruction-2026-10-15.md).
The boundary arrows on vertices A,B,C,D are

    thin: AB X A->B, BC X C->B, CD Y C->D, DA Y A->D;
    thick: AB X A->B, BC Y B->C, CD Y D->C, DA X A->D.

For each mark Z choose one triangle on a unit arrow T->H with interior
apex coordinate t_Z=(u_Z,h_Z), where0<u_Z<1 and h_Z>0. Copies use the
normal into their donor source. Choose independently a base split
M_Z=(m_Z,0),0<m_Z<1. There is NO normal-foot condition m_Z=u_Z.
All triangles and three-sector source partitions must be embedded and
strict as in the cited construction. In particular each internal donor
apex lies strictly inside its source rhomb.

For a receiving edge, assemble the quads (U,t,M,p) and(M,t,V,q), with
external donor apex t and neighboring internal donor nodes p,q. Require
all16receiving quads across both species and both donor parities to be
strict convex. Truncate each at its two donor-node corners, producing a
genuine convex hexagon. Along the EXTERNAL arrow-tail rays tT,tM, choose
the two cut fractions using only mark Z and native ray role, consistently
across source contexts. Other cuts may be unrestricted for this theorem,
provided the stated receiving hexagons exist.

**Theorem.** These16receiving hexagons cannot all be congruent to one
unmarked hexagon H, even allowing arbitrary rotated/reflected prototype
correspondences. Therefore the off-normal extension with mark-local cuts
cannot yield a two-class pentagon/hexagon construction. No cap or pentagon
congruence condition is needed in the proof.

## 1. Endpoint capacity fixes the base-angle branch

Let Xt,Xh,Yt,Yh be the donor base angles at arrow tails/heads. They lie
in(0,90) since0<u_Z<1. At a retained source endpoint, the receiving quad
angle is the source angle plus the incoming external base angle minus
the outgoing internal base angle. The actual arrow table gives

    thin: a=36+Xt-Yt, b=36+Yt-Xt, 144,144;
    thick: c=108+Yt-Xh, d=108+Xh-Yt,72,72.

Each retained endpoint is still a native vertex in its truncated H.
Thus H contains a,b,72,144,c,d, possibly with equal values. Strict convexity
gives a,b,c,d in(0,180), a+b72, c+d216. If a!=b, the four DISTINCT values
a,b,72,144 occupy four angles totaling288. Two further angles<180 cannot
bring the total to720. Hence a=b36 and Xt=Yt=beta.

Select one36, one72 and one144 angle of H. Its three remaining angles sum
468 and are each<180, so each is>108. Thus36 and72 are UNIQUE vertices,
and every other H angle is>108. Since c+d216, at least one is at most108;
it must be36 or72. Value36 would require the other180, forbidden. Therefore
{c,d}={72,144}, and Xh=beta+36 or beta-36.

A thin rhomb has a36source corner whose two arrows have tails there.
Their internal donor apices must lie inside that acute wedge, so0<beta<36.
The negative branch beta-36 is impossible. Consequently

    Xt=Yt=beta, Xh=beta+36, c=72, d=144.

In particular every X-tail and Y-tail receiving H has endpoint angle36
in thin contexts and72in thick contexts.

## 2. A geometric head-corner bound independent of cut distances

Suppose a source vertex U has two incident arrows of the SAME mark and
both have their HEAD at U. In the receiving quad U,t,M,p, the external
and internal donor nodes have equal distances Ut=Up: they are head nodes
of the same mark-local unit-base triangle. Its angle at U is exactly the
source angle sigma, since incoming/outgoing base-angle transfers cancel.
Therefore triangle Utp is isosceles with base angles(180-sigma)/2.

Strict convexity of the quad in that native order places M beyond segment
tp on the side opposite U. Indeed UM is its interior diagonal, with t,p
on opposite sides. The donor half-angle at t between tU and tM is strictly
larger than the angle between tU and tp. Hence

    theta_head > (180-sigma)/2.

This can also be checked by the strict native turn at M. The thin X-head
context at source B has sigma144, and the thick Y-head context at source C
has sigma72. They therefore give

    theta_Xhead>18, theta_Yhead>54.

The split M lies strictly inside the unit base. Its ray from t divides
the donor apex angle into positive tail/head parts. The full apex angle
for mark Z is180-beta-gamma_Z, where gamma_Z is its head base angle.
Thus, using gamma_X=beta+36,

    theta_Xtail<126-2beta<126,
    theta_Ytail<126-beta-gamma_Y<126.

No normal-foot assumption appears here. Convexity alone does NOT force
these tail angles below90or108; a separately retained strict precursor
fixture demonstrates that and does not contradict this combined argument.

## 3. A complete cyclic common-pair lower bound

**Lemma.** Let a convex hexagon H contain36,72,144 among its angles.
Suppose an ordered pair(s,t) occurs immediately after36in one boundary
direction and immediately after72in either boundary direction. Then

    s+t>=288.

As in Section1,36and72are unique and the other four angles are>108.
Neither s nor t can be36 (its thin triple would repeat that unique vertex)
or72 (its thick triple would repeat that unique vertex). Thus both are
among the four large angles. Remove36and72from the six-cycle. The two
intervening runs of large vertices have lengths0/4,1/3or2/2, up to exchange.

For0/4, each small vertex can only point into the four-vertex run. Reading
from opposite ends forces its angles(s,t,t,s). Hence720=108+2(s+t),
so s+t306.

For1/3, only the three-vertex run is long enough for either pair. Its
angles must be(s,t,s), while the isolated angle is v. The sum gives
2s+t+v612. Value144 must equal s,torv. If s144, t+v324 and v<180 give
t>144. If t144,2s+v468 give s>144. If v144,2s+t468 and s<180 give
s+t>288. Thus every case gives s+t>288.

For2/2, if the two occurrences use DIFFERENT runs, the four angles must
be(s,t,t,s), again giving s+t306. If they use the SAME run in opposite
directions, s=t=q. Write the other two angles u,v. Then2q+u+v612.
If q144,2q288; otherwise144is uorv and the other angle<180 forces
q>144. This includes cases where both runs have equal angles, with no
assumption of distinct large values. These cases exhaust every orientation
and prove the lower bound. No finite search is assumed.

At every external X-tail donor corner, the ordered pair of receiving
hexagon angles at the cuts along tT,tM depends only on that mark and ray
role. Thin/thick contexts give triples(36,s,t) and(72,s,t) in the commonH.
Truncating a convex corner of angle theta_Xtail gives

    s+t=180+theta_Xtail.

The lemma therefore forces theta_Xtail>=108. Combine this with the X-head
bound of Section2 and full X apex angle144-2beta:

    108 <= theta_Xtail <126-2beta, hence beta<9.

## 4. Unique endpoint and opposite split fix the full donor geometry

A thin-tail receiving hexagon has cyclic native word

    (T,cut_on_tT,cut_on_tM,M,cut_on_pM,cut_on_pT).

Its retained source vertex T is the UNIQUE36vertex of H. Therefore ANY
congruence between a thin X-tail and a thin Y-tail receiving hexagon maps
TtoT. Its opposite native vertex, three steps around the six-cycle, isM;
it is mapped toM regardless of which boundary orientation the congruence
uses. Thus the distance TM is common. Unit source edges give

    m_X=m_Y=m>0.

Normalize both receiving coordinate frames by T=(0,0),M=(m,0), with their
source interiors above the base and the external donor below it. Their
boundary tangent ray directions atT are exactly

    {-beta,36-beta}.

The first is the ray to the external donor; the second is the ray to the
internal donor in the adjacent edge's triangle. Both base tail angles are
beta, so this wedge is identical in X-tail and Y-tail contexts. An isometry
fixing both T and M is either the identity or reflection in their base
line. Reflection preserves the displayed unordered pair only when beta18:
the reflected pair is{beta,beta-36}, and matching it to the original pair
forces beta18 (the nonswapped alternative is impossible for0<beta<36).
But beta<9, so reflection is excluded. Their congruence in these normalized
frames MUST be the identity.

It therefore fixes their external cut vertices individually. Those lie
below the base, while the two internal cuts lie above it. The original
external apex is recovered uniquely as the intersection of the two lines

    line(T,cut_on_tT) and line(M,cut_on_tM).

The lines are distinct and nonparallel because the cuts are proper and
the apex has positive height. Consequently the X and Y donor coordinates
agree, u_X=u_Y and h_X=h_Y. Their head base angles agree as well:

    gamma_Y=gamma_X=beta+36.

With the same split m, the two whole donor triangles and their apex
half-angles agree. The Y-head half-angle is therefore

    theta_Yhead=144-2beta-theta_Xtail <=36-2beta<36.

This contradicts theta_Yhead>54 from the thick same-mark Y-head context.
The contradiction proves the theorem. QED.

## Scope, dependencies and hostile-review questions

The proof is mathematical and uses no solver, coordinate sampling, numerical
angle estimate or bounded negative search. Its inputs are the actual arrow
incidences, genuine convexity, equal source-edge length, mark-local donor
triangles/splits and external tail cuts, and ONE congruence class for all
receiving hexagons. It permits off-normal splits, unequal radial fractions,
reflections and arbitrary inner-cut choices. It does not prohibit changing
the source topology, allowing context-dependent external cut pairs, moving
donor projections outside the stated interval, or abandoning the one-H
requirement. It does not classify arbitrary convex tile constructions.

The independent reviewer must attack the same-mark isosceles head bound,
the actual arrow/base-angle identifications, completeness and orientation
of the three cyclic cases, and the unique36/opposite-M congruence followed
by tangent-wedge reflection exclusion and exact donor-apex reconstruction. The prior exact angleSAT and
strict-quadSAT fixtures are deliberately preserved: they refute any attempt
to replace the combined congruence argument by either necessary gate alone.
