# All positive symmetric distance-three octagon carriers

Date:2026-10-13. Status: independently reviewed VALID throughout the stated positive metric domain; [symbolic carrier review](../reviews/contact-symmetric-two-private-symbolic-carrier-hostile-review.md). Symbolic exact producer passed.
This is a genuinely changed analytic construction, not a parameter sweep.

Let r=sqrt2 and choose a>0 with (2-r)a<w<ra. Put
b=((2+r)a-(1+r)w)/2 and H=(1+r)w-ra. Define CCW pentagon

    P=((0,-w),(b,-w/2-a/r),(b+a/r,-w/2),(b,-w/2+a/r),(0,0)).

P has native word(x,a,a,x,w) and angles112.5,112.5,90,112.5,112.5.
Its four edge directions are fixed independently of parameters; b>0,
a>0,w>0 give all positive native edges, including x. Its two nonacute
legs obey x=(ra-w)/(2sin(pi/8)). Let Q start at0 with CCW edge directions
0,45,...315 degrees and lengths(H,a,a,H,a,w,w,a). All lengths are positive.
The exact native vector sum is0. Both polygons are genuinely strictly
convex: ordered positive edge directions have turns below180 and sum360;
for a chosen side the cross-height partial sums increase through directions
in its positive halfplane and then decrease to0 through the negative ones,
so every nonincident vertex has strictly positive cross-height.

No restriction on side coincidences is needed for this carrier. To apply
it specifically to a two-private source, H must additionally be absent
from the pentagon length set. Source extraction supplies that hypothesis;
the construction itself also works if additional lengths coincide.

Let Rminus be rotation by-45 and Rplus rotation by135 degrees. With native
indices starting at0, six CCW representatives are

    Q,
    Q0+Q1-Q,
    Q1-(P-P2),
    Q3+Rplus(P-P2),
    Q4+Rminus(P-P2),
    P-P2.

They comprise two Q copies and four P copies using ordinary isometries.
Let V=Q3+Q4-Q1 and U=Q5 minus the zeroth vertex of representative3
(zero-based representative indices). Explicitly,

    V=(a+rw/2,(r+1)a+(r/2+1)w),
    U=(-(r/2+1)a-(r/2+1/2)w,ra/2+w/2).

The standalone exact producer
research/searches/contact-symmetric-two-private-symbolic-carrier.py
uses Q(sqrt2)[a,w]. It verifies all72 endpoint-coordinate polynomial
identities for eighteen retained reversed-edge pairs, every one of36
native edges occurring exactly once. It verifies the rotations are exact
orthogonal matrices and the total area equals the determinant identically:

    det(V,U)=2(r+1)(a+rw/2)^2>0,
    4area(P)+2area(Q)=det(V,U).

This is a polynomial certificate valid throughout the entire stated open
domain, with no finite metric sampling and no FLC assumption.
The lattice is discrete rank two. Its six representatives are bounded,
so their closed translates are locally finite. Edge pair cancellation
makes the distributional gradient of the integer multiplicity identically
zero. On the connected plane multiplicity is constant almost everywhere;
its mean on a fundamental cell is total area/covolume=1. An interior overlap
or open gap contradicts multiplicity1. Local finiteness makes the union
closed, ruling out even isolated uncovered points. Hence the carrier is
an actual legal entire-plane periodic tiling for the original shapes.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/contact-symmetric-two-private-symbolic-carrier.py

For a clean typeR symmetric source with two private slots at distance3,
all public acute tags are a and the word is(H0,a,a,H3,a,w,w,a).
Vertical closure forces H3=(1+r)w-ra, and horizontal closure then H0=H3.
Thus private lengths must be equal. Pentagon positivity gives w<ra;
private positivity gives w>(2-r)a. Every such source metric lies in the
proved carrier domain. This supplies SOME periodic escape, not periodicity
of every filling. It covers rotations, reflections, omitted-type tilings
and unrestricted contacts because it constructs an allowed tiling directly.
