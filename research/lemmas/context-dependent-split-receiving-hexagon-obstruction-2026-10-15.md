# Arbitrary edge splits do not repair the receiving-hexagon component

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[fresh Astra review](../reviews/context-dependent-split-receiving-hexagon-astra-hostile-2026-10-15.md). This is a construction-component obstruction, not a solution
of the unrestricted two-convex-polygon problem. Angles below are in degrees.

## Theorem and exact changed domain

Use the unit thin/thick rhomb source, with native vertices A,B,C,D cyclically,
angles 36/144 and 72/108, and native arrows

    thin:  AB X A->B, BC X C->B, CD Y C->D, DA Y A->D;
    thick: AB X A->B, BC Y B->C, CD Y D->C, DA X A->D.

In each source rhomb opposite edges are donors and the other two receivers;
physical shared edges have opposite roles. For mark Z, the donor triangle
on a unit arrow T->H has one fixed pair (u_Z,h_Z), with 0<u_Z<1,h_Z>0,
measured along the arrow and its donor's inward normal. These donor triangles
remain MARK-LOCAL. All source sectors are valid and the internal donor apexes
lie strictly inside their rhombs.

On EACH physical source edge choose ANY point M in its relative interior.
There is no mark, source, parity or neighbor locality condition on these
split points. The same physical M is used by the two sides of that edge.
In particular this allows the unique receiver to choose M from its own
source/parity context and the donor to inherit it from that neighbor.

At a receiving edge U-V form strict convex native quads

    L=(U,t,M,p), R=(M,t,V,q),

where t is the external donor apex and p,q the internal donor nodes adjoining
U,V. Truncate the two donor-node corners of each quad by arbitrary proper
cuts, retaining all six genuine corners. The cut positions may depend on
arbitrary source context; no equal-radius, mark-local or cross-context
fraction identity is assumed. The source contains both thin and thick rhombs.

**Theorem.** The receiving hexagons cannot all be congruent, even with
reflections allowed. Consequently relaxing the SPLITS as well as the cut
fractions does not repair this component while the donor triangles stay
mark-local. The contradiction uses just endpoint angles, retained opposite
diagonals and one thick-source native turn; no cap or pentagon congruence,
source-neighbor classification or metric search is needed.

## 1. Endpoint capacity survives arbitrary splits and cuts

Let Xt,Xh,Yt,Yh be the positive acute base angles of the X,Y donor triangles
at their actual arrow tails and heads. Moving M within its edge changes
neither ray at the original source endpoint. Proper truncation at the two
donor nodes also leaves that original endpoint angle unchanged.

At each original source vertex its receiving quad endpoint angle is the
source angle plus its incoming donor base angle minus its internal adjacent
donor base angle. The full native table is:

| Context, occurring in either donor parity | Original source angle | Incoming base | Internal base | Retained endpoint angle |
|---|---:|---|---|---|
| thin X tail | 36 | Xt | Yt | a=36+Xt-Yt |
| thin X head | 144 | Xh | Xh | 144 |
| thin Y tail | 36 | Yt | Xt | b=36+Yt-Xt |
| thin Y head | 144 | Yh | Yh | 144 |
| thick X tail | 72 | Xt | Xt | 72 |
| thick X head | 108 | Xh | Yt | d=108+Xh-Yt |
| thick Y tail | 108 | Yt | Xh | c=108+Yt-Xh |
| thick Y head | 72 | Yh | Yh | 72 |

Each rhomb supplies both relevant tail contexts through its two receivers,
so the argument does not assume that both parities occur in the source.
There is one X receiver and one Y receiver in each source case.

Suppose all receiving hexagons are congruent to H. We have a+b=72 and
0<a,b<180. If a!=b, the four distinct native angles a,b,72,144 in H sum
to 288. Two more angles each less than 180 cannot bring this to the required
hexagon sum 720. Thus a=b=36 and Xt=Yt=beta.

H contains 36,72,144. Its remaining three angles sum to 468 and are each
less than 180; each is therefore greater than 108. In particular 36 and
72 are UNIQUE native angle vertices of H. Since c+d=216, at least one is
at most 108. It must be 36 or 72; 36 would make the other angle 180,
impossible. Hence {c,d}={72,144}, so Xh=beta+36 or beta-36.

At a thin acute source vertex both incident arrows have tails. The actual
internal donor apex lies strictly inside its 36-degree wedge, giving
0<beta<36. Positivity of Xh excludes beta-36. Consequently

    Xh=beta+36, c=72, d=144.

This is the only endpoint branch used below. Yh remains unrestricted.

## 2. A single thick Y receiver forces the unique 72 diagonal to be 1/2

The native hexagon after two-corner truncation has cyclic order

    (U,cut_on_tU,cut_on_tM,M,cut_on_pM,cut_on_pU),

or its reversal. Its retained U and M are opposite vertices. An isometry
between genuine hexagons preserves opposite vertices. Hence every occurrence
with retained endpoint angle 72 has the same distance from that endpoint
to its opposite retained M: call it D72. This uses uniqueness of the
72-angle vertex in H and no cut correspondence assumption.

Consider the Y receiving edge of ANY thick source rhomb. Its actual arrow
tail is B or D, with original angle 108; its head is C, with original
angle 72. The native table and endpoint branch show that BOTH retained
endpoint angles are 72:

    tail: 108+Yt-Xh=72;
    head: 72+Yh-Yh=72.

These are the endpoints retained in the TWO different receiving hexagons
L and R on this SAME unit physical edge. They share the SAME M. If m is
its arrow-tail coordinate, the two opposite diagonal lengths are m and
1-m. Thus

    m=D72=1-m, hence D72=1/2.

Now consider the X receiving edge in the same thick source rhomb. Its
actual tail is A, with retained angle 72+Xt-Xt=72. Its own opposite M
therefore has arrow-tail coordinate

    m_X,that_context=D72=1/2.

No identification of split parameters between different rhombs, marks or
parities has been used. Even arbitrarily assigned physical edge splits
must satisfy this local conclusion if all receiving hexagons are H.

For comparison, uniqueness of 36 only makes the thin receiving tail-to-M
distances one common D36. That value is not forced to 1/2 by diagonal
identities alone. It is unnecessary: the thick native turn already fails.

## 3. The thick X-tail turn excludes its compulsory midpoint

Normalize that thick X receiver's actual arrow to T=(0,0), H=(1,0), with
the receiver in y>0. Put u=u_X,h=h_X and r=tan(beta). Its external apex is

    t=(u,-h), h=u*r.

At T, the internal adjacent donor is ALSO an X donor at its arrow TAIL,
and its edge makes the source angle 72 with the receiving edge. Mark locality
therefore fixes its apex to

    p=(u*cos72+h*sin72, u*sin72-h*cos72)=(x,y), y>0.

This is the actual native same-X-tail incidence at thick A, including either
source parity; it is not an assumed equality of X and Y triangles. A reflected
arrow frame reverses all signed areas together and gives the same normalized
turn inequality.

For the native quad (T,t,M,p), strict convexity at M=(m,0) requires

    D=m(y+h)-u*y-h*x>0.

Because y+h>0 this is equivalent to

    m > mL = (u*y+h*x)/(y+h)
           = u*(1+r^2)/(1+r*tan36).

The last equality uses (1-cos72)/sin72=tan36. Let q=tan36. Since 0<beta<36<45,
we have 0<r<q<1. The unit donor triangle's head angle beta+36 gives

    u = tan(beta+36)/(tan(beta)+tan(beta+36))
      = (r+q)/[q*(1-r^2)+2r].

Every denominator below is positive. Set A0=q*(1-r^2)+2r. Direct expansion
shows

    2*mL-1 = P/[A0*(1+r*q)],
    P = q*(1-r*q) + q*r^2 + (2+q^2)*r^3 > 0.

Indeed r*q<1 and all displayed remaining terms are positive. Thus mL>1/2,
contradicting the compulsory m=1/2 from Section 2. Equivalently the exact
turn at that midpoint is

    D = -u*sin72*P/(2*A0) < 0,

so this actual source quad would be reflex at M, rather than merely failing
a downstream congruence condition. This completes the theorem. QED.

An equivalent trigonometric positive identity is

    2*sin(beta+36)*cos36 - sin(2*beta+36)*cos(beta-36)
      = sin36*cos(beta+36) + 2*sin(beta)^3 > 0.

The rational form above avoids any need to isolate the beta=18 mirror
wedge or reconstruct identical X/Y donor apexes. Both are superseded here.

## Exact check, source consistency and limits

The supporting symbolic checker is
[context-dependent-split-receiving-hexagon-check-2026-10-15.py](../searches/context-dependent-split-receiving-hexagon-check-2026-10-15.py).
It independently assembles all sixteen native endpoint forms from the four
source arrow/parity cases, checks the two-72 Y edges and same-X-tail thick
incidence, solves the retained 36/72 diagonal equations without equating
independent receiver contexts, and verifies the universal rational native-turn
identity over QQ(r,q). It samples no geometric parameter and does not infer
a universal inequality from a grid.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/context-dependent-split-receiving-hexagon-check-2026-10-15.py

Arbitrary physical M choices are consistent between donor and receiver by
using that one point on both sides of a source seam. No all-neighbor closure
assumption is needed. If an independently computed donor-side split rule
would disagree with the receiver's choice, it fails the underlying dissection
and is already outside the stated admissible domain. Allowing the donor to
inherit M from arbitrary source/neighbor context is INCLUDED by this theorem;
it cannot avoid the local contradiction above.

This closes only the specified receiving topology with mark-local donor
triangles and one common H. A genuine escape must change donor triangle
geometry by context, the retained endpoint/opposite-M topology, or the common
receiving-hexagon requirement. The theorem gives no assertion about arbitrary
unmarked polygon pairs, pentagon/hexagon recombinations or intrinsic shape
forcing. The fresh independent hostile review found no unresolved defect.
