# A symbolic periodic carrier with two changed octagon supports

Date: 2026-10-13. Status: independently reviewed VALID for the full four-parameter positive family; [third complete audit](../reviews/contact-non-equiangular-two-support-full-family-hostile-review.md). The exact fixture and x=w subfamily are included. No parameter sweep or assertion about every admitted filling is used.

## Exact family

Put c=cos(pi/8), t=sin(pi/8), r=sqrt2. Choose x,y,u,H>0 such that

    v=u+rc(x-y)>0,
    w=(u+v)/r-t(x+y)>0.

These are exactly the positive closure parameters of ANY right pentagon in this angle palette. Start P at0 and integrate the five edge vectors

    x(c,-t), u(1/r,1/r), v(-1/r,1/r), y(-c,-t), w(0,-1).

The formulas give exact closure u-v=rc(y-x) and
w=(u+v)/r-t(x+y). P is genuine convex with one90 and four112.5 corners.
Start Q at0 and integrate native lengths (H,u,w,v,H,u,w,v) in directions

    22.5,45,90,135,202.5,225,270,315 degrees.

Opposite vectors cancel. Its eight angles are
(112.5,157.5,135,135,112.5,157.5,135,135), and it is centrally symmetric.
All edges have positive lengths and their directions increase once through
360 with turns strictly between0 and180; the closed polygons are strictly
convex. One can also see every supporting halfplane directly: relative to
an edge, successive perpendicular increments are positive and then negative,
with a single sign change before returning to0, so intermediate vertices
are strictly inside its supporting halfplane. P and Q are distinct by side
count. No condition of numerical privacy or a flat-contact prohibition is
needed for this existence theorem.

## Entire-plane periodic construction

Index their CCW vertices P0,...,P4 and Q0,...,Q7 from the integration above.
Use the three representatives

    Q,
    Fplus=P+Q3-P4,
    Fminus=-P+Q7+P4,

and period vectors

    L=Q1-Q4,
    U=Q1-Q7+P2-P4.

The two P representatives are ordinary translation and half-turn images.
The complete reversed-native-edge pairs are given below; an index(f,i)
means side i of representative f, with f=0,1,2 as listed. Translate the
second edge by mL+nU to obtain the reverse of the first.

| First | Second | (m,n) |
| --- | --- | --- |
| (0,0) | (0,4) | (1,0) |
| (0,1) | (2,1) | (0,1) |
| (0,2) | (1,4) | (0,0) |
| (0,3) | (2,2) | (-1,1) |
| (0,5) | (1,1) | (0,-1) |
| (0,6) | (2,4) | (0,0) |
| (0,7) | (1,2) | (1,-1) |
| (1,0) | (2,0) | (0,1) |
| (1,3) | (2,3) | (-1,1) |

All18 native edges occur once. The [independent symbolic checker](../reviews/contact-non-equiangular-two-support-carrier-independent.py)
reconstructs the exact family in Q(c)[x,y,u,H], derives its ordered vector
closures and native-angle identities, and regenerates every partner without
using this table or importing the fixed-fixture producer. All36 coordinate
endpoint identities are polynomial identities. It also verifies

    det(L,U)=area(Q)+2area(P)>0.

Strict positivity follows throughout the exact domain from the positive
areas of the genuine convex polygons. Thus the period lattice is discrete.
The closed polygon translates are locally finite. Their indicator sum has
zero distributional gradient by complete reversed-edge cancellation, and
average multiplicity1 by area/covolume. It is therefore1 almost everywhere.
Interior overlaps and open gaps would have positive area, impossible. Local
finiteness makes the union closed, excluding any missing boundary point.
This proves actual legal rank-two plane tiling at every positive family
metric, with no imposed rule for other admitted tilings.

The previous [H=2u,u=2/3,x=1 fixture](contact-non-equiangular-two-support-host-periodic-carrier.md)
is included. The carrier avoids its nonextendible hosted cap, but no absence
of that cap in arbitrary other family fields is claimed here. Every positive P in this angle palette therefore has a periodic partner of this exact two-support Qword, for arbitrary H>0. This does not classify its other partners. True hosting with other Qwords remains outside.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-non-equiangular-two-support-carrier-independent.py
