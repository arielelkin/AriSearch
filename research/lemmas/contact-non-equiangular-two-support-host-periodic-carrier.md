# Two-support non-equiangular host candidate has a one-Q / two-P periodic escape

Date:2026-10-13. Exact producer replay passed. The fixed fixture is included in the independently reviewed VALID [full positive family](contact-non-equiangular-two-support-symbolic-periodic-carrier.md); [complete family review](../reviews/contact-non-equiangular-two-support-full-family-hostile-review.md).
This is ONE new fixed pair, not an all-metric theorem or a parameter sweep.

Set r=sqrt2,c=cos(pi/8),t=sin(pi/8),x=w=1,u=2/3,

    y=(ru+c-t-1)/(c+t), v=u+rc(1-y), H=2u=4/3.

Integrate P native directions-22.5,45,135,202.5,270 with length word
(x,u,v,y,w). Integrate Q native directions22.5,45,90,135,202.5,225,270,315
with length word(H,u,1,v,H,u,1,v). Both polygons close and are genuine
strictly convex, with positive lengths. P angles are112.5,112.5,90,112.5,
112.5. Q angles are112.5,157.5,135,135 repeated twice. H is private
relative to P, while x=w is its sole native P alias. This changed palette
allows Q-hosted90/90 caps in the angle census; no old equiangular-Q native
forcing theorem is assumed.

The exact producer is
research/searches/contact-non-equiangular-two-support-host-candidate.py.
Its minimal QH-host cap is a positive disjoint Q/twoP patch: two guests
have u legs along half the H side and shared perpendicular v legs. The
far shared v endpoint has two nativeP112.5 corners. Only Q135 can fill
it, and both exposed P y sides have obtuse endpoints, so the corresponding
Q contacts must be whole independently of any flat-host rule. Q lacks
y, so that cap cannot extend to a plane. The producer checks the exact
shared endpoint and both y lengths. This falsifies the proposed host
branch but DOES NOT falsify the original pair.

The producer also retains the one disjoint whole-contact source ring from
its complete4^2 public unit-side domain. For global existence, use the
following explicit carrier directly; no claim about forcing the original
field's language is necessary. With source native indexing starting at0,
put

    Fplus=P+Q3-P4, Fminus=-P+Q7+P4,
    L=Q1-Q4, U=Q1-Q7+P2-P4.

The representatives are Q,Fplus,Fminus. The producer retains nine native
oriented-edge pairings, verifies every one of18 edges appears once, and
checks all36 exact endpoint coordinate identities. In each pairing the
second edge translated by its stated integer combination of L,U is the
reverse of the first. It checks

    det(L,U)>0, area(Q)+2area(P)=det(L,U).

All checks are exact real-algebraic identities/comparisons, with no numeric
tolerance and no bounded contact-to-plane inference.

The lattice ZL+ZU is discrete rank two, and its three bounded closed
representatives give a locally finite periodic family. Their integer
multiplicity has distributional gradient zero by the COMPLETE oriented
edge pairing. Its mean on a fundamental cell is area/covolume1, so it is
1 almost everywhere on the connected plane. Interior overlaps and open
gaps contradict this. The union is closed by local finiteness, so coverage
holds at every point as well. Thus this is an actual admitted rank-two
periodic tiling of the original P/Q pair, including both species.

The cap may remain a legal finite patch while admitting no global extension;
the independent whole-contact carrier proves the original pair tileable
and supplies a periodic escape. No assertion that every filling is periodic,
no family exclusion and no resolution of the unrestricted target is made.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/contact-non-equiangular-two-support-host-candidate.py
