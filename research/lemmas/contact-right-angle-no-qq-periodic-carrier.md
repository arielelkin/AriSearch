# Every one-right pentagon has an exact grouped-octagon periodic partner

Date: 2026-10-13. Status: independently reviewed VALID symbolic construction; [hostile review](../reviews/contact-right-angle-no-qq-hostile-review.md). This constructs a periodic escape, not an aperiodic pair.

## Exact family and theorem

Put r=sqrt(2), c=cos(pi/8), t=sin(pi/8), using the defining data8c^4-8c^2+1=0,9/10<c<1,r=4c^2-2,t=r/(4c). Choose real x,y,v>0 and define

    u=v+rc(y-x),
    w=(u+v)/r-t(x+y).

Requireu>0andw>0. These are precisely positive edge-length closure conditions for the pentagon below. No noncoincidence condition is needed by this carrier construction.

Let

    a=xc+u/r=yc+v/r,
    C_y=-w-xt+u/r,
    z=(x-y)(c+t)/2=-C_y-w/2,
    A0=(-a,-w-C_y), B0=(-u/r,-u/r), C0=(0,0),
    D0=(-v/r,v/r), E0=(-a,-C_y),
    P0=(A0,B0,C0,D0,E0).

P0is convex with one90corner atC0and four112.5corners. Its cyclic side lengths arex,u,v,y,w. Every genuine pentagon with that native angle palette can be brought to this form by an isometry and the indicated naming of its sides.

DefineF(s,t)=(t,s), G(s,t)=(-t,-s). Put

    V=(2a,-2z), U=(-2z,2a), L=U-V,
    Q=(D0,G(E0),U+B0,U+A0,
       L-D0,L-G(E0),-V-B0,-V-A0).

The consecutive Qedge lengths arey,x,x,y,y,x,x,ywith directions starting at67.5degrees and turning45degrees successively. Thus Qis a genuine convex equiangular135-degree octagon, distinct from P0by side count.

**Theorem.** The lattice translates by mV+nU, m,ninZ, of the five polygon representatives

    P0, F(P0), -P0, G(P0), Q

form a plane tiling. Reflections and the half-turn are allowed isometries. In particular this unmarked convex pair admits two independent periods and cannot be aperiodic. This conclusion holds for the full positive family, whether or not other admitted tilings have QQcontacts or partial contacts.

## Geometry and positive lattice covolume

For P0the edge directions are-22.5,45,135,202.5,270degrees. The two displayed closure equations give exactly zero total edge vector. Positive side lengths with these ordered directions make a genuine convex polygon, with turns67.5,67.5,90,67.5,67.5.

The Qformula gives its first two edges y(t,c)andx(-t,c), followed by45-degree rotations and the stated positive length word. This proves convexity and its angle palette for the entire parameter domain, not a sampled metric. Opposite vertices sum toL, so Qis centrally symmetric.

The identity

    w=2a-(c+t)(x+y)

implies a>(c+t)(x+y)/2>|z|because x,y,w>0. Hence

    det(V,U)=4(a^2-z^2)>0.

The shoelace identity is

    4area(P0)+area(Q)=det(V,U).

It is verified symbolically overQ(c)[x,y,v], not numerically. Both polygon areas are positive by convexity.

## Complete oriented boundary cancellation

Index the five CCW representatives as0=P0,1=F(P0)with reversed vertex order,2=-P0,3=G(P0)with reversed vertex order,4=Q. Index each native edge by its starting vertex. The following14pairs cancel all28oriented edges. Each listed translation(m,n)means the SECOND edge translated bymV+nUis exactly the reversed FIRST edge:

| First(tile,edge) | Second(tile,edge) | (m,n) |
|---|---|---|
| (0,0) | (4,2) | (0,-1) |
| (0,1) | (1,2) | (0,0) |
| (0,2) | (3,1) | (0,0) |
| (0,3) | (4,7) | (0,0) |
| (0,4) | (2,4) | (-1,0) |
| (1,0) | (4,4) | (1,-1) |
| (1,1) | (2,2) | (0,0) |
| (1,3) | (4,1) | (0,-1) |
| (1,4) | (3,4) | (0,-1) |
| (2,0) | (4,6) | (1,0) |
| (2,1) | (3,2) | (0,0) |
| (2,3) | (4,3) | (1,-1) |
| (3,0) | (4,0) | (0,0) |
| (3,3) | (4,5) | (1,0) |

Every endpoint identity holds as a polynomial identity inx,y,vwith coefficients in the specified exact quartic field. The table remains valid at coincident-length parameters; no combinatorial uniqueness is needed.

## Why cancellation and area prove the entire plane tiling

LetNbe the multiplicity function summing the indicator of every polygon in the periodic family. It is locally finite because the lattice is discrete and the five representatives are bounded. Each CCW polygon's distributional indicator gradient is supported on its oriented native edges. The table pairs every edge with an oppositely oriented identical edge modulo the lattice, so these gradients cancel and the distributional gradient ofNis0. A locally integrable function with zero distributional gradient on connectedR2is constant almost everywhere.

Its average in a fundamental parallelogram is the sum of representative areas divided by the covolume, which equals1. ThusN=1almost everywhere. If two polygon interiors overlapped, their open intersection would have positive area andN>=2there, a contradiction. The periodic union of their closed supports is closed by local finiteness. Any uncovered point would therefore leave an open positive-area gap withN=0, also a contradiction. Thus the family covers the whole plane with disjoint interiors.

This proof establishes existence without first presuming nonoverlap, without a finite-patch extension claim and without imposing matching rules. The cancellation and covolume are exact certificates for this explicit infinite family.

## Computation and scope

The retained certificate is `research/certificates/contact-right-angle-no-qq-symbolic-carrier.json`. Producer `research/searches/contact-right-angle-no-qq-symbolic-carrier.py` verifies field identities, the Qedge word, all14symbolic pairs and the area identity. Its finite identity domain is the28native representative edges and possible shifts in{-1,0,1}^2; the retained pairing table independently proves the needed equalities, so no larger search domain is necessary. Polynomial identity verification covers the full declared positive parameter domain.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-right-angle-no-qq-symbolic-carrier.py --check research/certificates/contact-right-angle-no-qq-symbolic-carrier.json

The motivating noQQsource analysis is a restricted branch of arbitrary right-palette tilings. This carrier itself is a legal periodic tiling of the original two shapes and does not rely on imposing that source rule. An arbitrary equiangular Qpartner with a different native side word is outside this construction. Independent review is complete. No novelty claim is made; documented literature comparison remains pending.

The complete native angle sequence and side-length sequence determine the convex Qup to an isometry, since each successive edge direction is fixed by its preceding exterior turn. The carrier wordy,x,x,y,y,x,x,yis a cyclic shift ofx,x,y,y,x,x,y,y. Thus the escape uses the same Qcongruence class as the grouped binary source, not a newly selected metric partner.
