# Public-H four-equal fixture: the acute-on-H branch gives a periodic carrier

Date:2026-10-13. Adversarially reviewed VALID.
Fresh whole-witness review: `research/reviews/contact-non-equiangular-public-h-four-equal-hostile-review.md`.
Independent exact checker: `research/reviews/contact-non-equiangular-public-h-periodic-independent.py`.
This is one exact incidence change from the true-hostH2 fixture, not an Hsweep.

Let r=sqrt2,c=cos(pi/8),t=sin(pi/8),w=r-2t in(0,1). Start P at0 and
integrate directions-22.5,45,135,202.5,270 with lengths(1,1,1,1,w).
Start Q at0 and integrate directions22.5,45,90,135,202.5,225,270,315,
ALL with length1. The Pangles are112.5,112.5,90,112.5,112.5; Qangles
are112.5,157.5,135,135 repeated twice. Q is centrally symmetric. Both
polygons are strictly convex and positive, and distinct by side count.
All Qlengths now occur in P: there are NO private slots and no native
length2 host. Old private-edge source forcing cannot be inherited.

The exact producer
research/searches/contact-non-equiangular-public-h-four-equal.py verifies
shape closure/support inequalities and native lengths; native directions
fix the angle words. It retains a unique actual whole-w P-dimer and all
sixteen disjoint two-Q attachments at its two225-degree union corners.
Optional --rings replays the complete256 clean high-corner extension
domain, with64 disjoint six-tile survivors; none is asserted to extend
merely from those local checks. The plane construction below is separate.

Set the exact rotation

    R=[[t,-c],[c,t]],
    S=Q1-R*P2, S1=Q1+R*P1.

Use representatives

    Q, F0=R*P+S, F1=-R*P+S1,

and periods

    L=Q3=(c+1/r,t+1/r+1),
    U=Q4-S-S1=(-c-t,r+1+c-t).

R is orthogonal with determinant1. Thus F0/F1 are ordinary congruent
Pcopies. This carrier realizes the new alternative where P90 is on the
Qhigh endpoint along the PUBLIC Hside; U's guest is P112 instead.
It is not the old forced-acute-on-U language. The w-dimer pairing is
S1-S-R(P0+P4)=L, checked exactly by the producer.

With zero-based representatives Q,F0,F1 and native side indices, the
following table translates the second edge by mL+nU to reverse the first:

| First | Second | (m,n) |
| --- | --- | --- |
| (0,0) | (1,2) | (0,0) |
| (0,1) | (2,0) | (0,0) |
| (0,2) | (1,3) | (1,0) |
| (0,3) | (0,7) | (1,0) |
| (0,4) | (2,2) | (0,1) |
| (0,5) | (1,0) | (0,1) |
| (0,6) | (2,3) | (-1,1) |
| (1,1) | (2,1) | (0,0) |
| (1,4) | (2,4) | (-1,0) |

All18 edges occur exactly once. The producer checks all36 exact endpoint
coordinate identities and

    det(L,U)=area(Q)+2area(P)>0.

The two independent periods generate a discrete lattice; its three bounded
closed representatives form a locally finite family. Their integer
multiplicity has zero distributional gradient by COMPLETE oriented edge
cancellation, and its mean equals1 by the positive area/covolume identity.
Thus multiplicity is1 almost everywhere. Interior overlaps or open gaps
have positive area and cannot occur; the union is closed by local finiteness,
so every point is covered. This proves actual admitted rank-two periodic
plane existence with both original unmarked shapes.

Neither species tiles alone in this palette, but no omission exclusion is
needed for this explicit periodic escape. No claim says every original
filling is periodic, every local patch extends or all public-Hmetrics work.
The main unrestricted two-convex target remains unresolved.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/contact-non-equiangular-public-h-four-equal.py
