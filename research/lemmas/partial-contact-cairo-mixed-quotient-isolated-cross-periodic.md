# A second full three-parameter periodic Cairo cone from actual mixed face gluing

**Status: VALID complete construction after fresh independent hostile review.**
No existence is inferred from a seam primal or from an unextended patch.

Put w=sqrt3 and define native sidewords

    P=(a,b,c,d,e), d=a+w(b-c)/3, e=-a+w*b/3+2*w*c/3,
    Q=(A,a,c,D,f),
    A=-a+(w/3-1)*b+2*w*c/3,
    D=(w/3-1)*a+(w/3-1)*b+w*c/3,
    f=(w/3+1)*a+(1-w/3)*b.

Assume every original side is positive. Then P,Q have a doubly periodic
tiling with four original faces of each species. Both native closure
relations hold identically. The only needed special event identity is
e=A+b. No privacy or genericity restriction is required for sufficiency.
The discovery source is orbit7 flat12 in the reviewed two-cross reduction;
its native shared arms are Pa=Qb and Pc=Qc. The sufficient statement
covers its entire positive homogeneous3D metric cone and all resonances.

Use native edge directions0,90,150,240,300 degrees and native vertices
0,(a,0),(a,b),(a-wc/2,b+c/2),(-e/2,we/2). Positivity, increasing cyclic
edge directions and closure prove strict convexity: relative to any native
edge, support heights increase while subsequent edge sines are positive,
then decrease to zero while they are negative, staying positive at every
nonincident vertex. Every face below is therefore an original unmarked
convex pentagon, including when inserted subdivision points merge.

First suppose D>d. Split P's native e into A then b, both positive because
e=A+b. Split Q's native D side into D-d then d, and keep f whole. Two
copied P and two copied Q have six atoms each. With darts0..5,6..11,
12..17,18..23 in native cyclic order, pair them by

    (15,21,0),(17,23,0),(0,13,0),(6,19,0),
    (1,5,1),(7,11,1),(2,14,1),(8,20,1),
    (3,22,1),(9,16,1),(4,12,1),(10,18,1).

Here0 means endpoint reversal,1 endpoint preservation. Actual length
identities are checked as full linear forms, not at a sample. The true
vertex flag links are

    [15,3,22],[16,9,21],[17,10,18],[12,4,23],
    [0,2,14],[1,5,13],[6,8,20],[7,11,19].

All sum360 (120 cubed or90+90+180), each is a single circle. The face
graph is connected. Exact Euclidean development uses the explicit frame
transition rule from the first mixed-quotient construction and gives8
states/placements retained in the certificate. Original native coordinates,
every atomic endpoint and opposite CCW boundary orientation are checked.
Every one of48 lifted transitions has an exact integer period shift.

For D<d, split P's d side into d-D then D; keep its e split A then b.
Keep Q whole. Thus the copied P faces have seven atoms each and copied Q
faces five. Number darts0..6,7..13,14..18,19..23. Pair

    (3,10,0),(18,23,0),(0,15,0),(7,20,0),
    (1,6,1),(8,13,1),(2,16,1),(9,21,1),
    (4,22,1),(11,17,1),(5,14,1),(12,19,1).

The actual360 link circles are

    [3,17,11],[4,22,10],[18,12,19],[14,5,23],
    [0,2,16],[1,6,15],[7,9,21],[8,13,20].

This independently developed lift again gives8 original faces and48
boundary identities. Its motif agrees modulo the lattice with the first:
all frame/translation entries agree except Q's state(face3,theta9,s1),
which differs by minus the first period.

Both motifs use the exact periods

    t=(-(w/2+1)*a-b/2, -a/2+(w/2-1)*b),
    v=((2*w/3-1/2)*a+(w/2-1)*b-2*w*c/3,
       -(5*w/6+1)*a+b/2+(4*w/3+2)*c).

The complete shoelace identity is

    4*area(P)+4*area(Q)=-det(t,v)>0.

Thus the periods are independent throughout the full positive domain.
All endpoint, integer-period and area identities are polynomial identities
over Q(w)[a,b,c]. They do not rely on actual-order sample extrapolation.
For D=d use the first motif, delete the four zero D-d atomic pieces, each
paired with another zero piece, and retain all remaining boundary pairs.
All original faces stay strictly convex and the same positive area/covolume
identity holds. This is an explicit boundary subdivision merger.

For any fixed metric, lattice translates of the eight bounded original
faces are locally finite. At a generic point the integer multiplicity M
is locally constant. Every directed CCW boundary atom has an exactly
opposite counterpart at identical location modulo the lattice, so the net
jump of M across each generic boundary line is zero. Paths avoiding the
locally finite vertices and intersections show M constant almost everywhere.
Its mean on a period cell is the total original face area divided by
covolume, exactly1. Therefore M=1. Any interior overlap would give an open
set with multiplicity at least2; any uncovered point would have an open
uncovered neighborhood since the locally finite closed-face union is closed.
Both contradict M=1 at generic points. Hence this is a periodic plane
tiling by the original undecorated prototiles under the unrestricted model.

The bounded proposals scale exact mixed frequencies to four copied faces
only as a proposal generator. The actual native gluing,360 circular links,
Euclidean lift, integer boundary shifts and global area proof supply the
existence evidence. No relation between arbitrary rational balance and
surface realizability is assumed.

[Raw first gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12.json),
[first development](../certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-development.json),
[complementary gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-complement.json),
[complementary development](../certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-complement-development.json),
[bounded producer](../searches/partial-contact-cairo-mixed-quotient-native-search.py),
[development producer](../searches/partial-contact-cairo-mixed-quotient-native-development.py),
[reproducibility record](../searches/partial-contact-cairo-mixed-quotient-isolated-cross-periodic.md).

The [fresh independent full-cone review](../reviews/partial-contact-cairo-mixed-quotient-isolated-cross-periodic-review.md) accepts both strict contact orders and their equality merger.
