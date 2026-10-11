# A ten-face periodic Cairo cone with four-to-one species counts

**Status: VALID complete full-cone construction after fresh independent hostile review.**

Put w=sqrt3 and define

    P=(a,b,(3*w*a+b)/4,(a+w*b)/4,(a+w*b)/2),
    Q=((3*w*a-b)/2,a,(11*a-3*w*b)/2,b,5*(w*a-b)/2).

Assume a>0 and0<b<w*a. This is exactly their full positive native side
cone. Then P,Q admit an explicit periodic plane tiling with eight original
P and two original Q per period cell. No arm privacy, genericity or strict
extra order assumption restricts sufficiency. The discovery source is
orbit6 flat142 in the reviewed exact two-cross classification; Pa=Qb,
Pb=Qd. Both Cairo closure relations hold identically.

Native vertices for word(a,b,c,d,e) are0,(a,0),(a,b),
(a-wc/2,b+c/2),(-e/2,we/2), with edge directions0,90,150,240,300 degrees.
Every positive closed native word is strictly convex: relative to each
oriented edge, the subsequent support heights increase while edge sines
are positive and then decrease to0 while negative; all nonincident heights
remain strictly positive. Native support, angle and side identities thus
hold throughout the full metric cone, rather than at a single sample.

Write c=(3wa+b)/4,d=(a+wb)/4,e=2d,A=(3wa-b)/2,
C=(11a-3wb)/2,f=5(wa-b)/2. Take six P copies whole. Two more P copies
have c split b then c-b and e split d then d. Each Q has A split c then
A-c and C split a then C-a, retaining f whole. Every inserted point is
strictly interior throughout the full domain because

    c-b=A-c=3*(wa-b)/4>0,
    C-a=3*w*(wa-b)/2>0.

The six whole P faces have5 atoms each; the two split P and two split Q
have7 each, for58 atomic darts. In retained face order their dart blocks
are0..4,5..9,10..14,15..19,20..24,25..29,30..36,37..43,
44..50,51..57. Pair the following equal full symbolic piece lengths,
with0 meaning endpoint reversal and1 endpoint preservation:

    [(48, 55, 0), (50, 57, 0), (33, 45, 0), (40, 52, 0), (4, 9, 0), (14, 19, 1), (24, 29, 1), (2, 12, 1), (7, 22, 1), (17, 44, 1), (27, 51, 1), (0, 37, 1), (5, 30, 1), (10, 46, 0), (15, 47, 1), (20, 53, 0), (25, 54, 1), (1, 31, 1), (6, 38, 1), (11, 32, 0), (16, 56, 1), (21, 39, 0), (26, 49, 1), (3, 36, 1), (8, 43, 1), (13, 35, 0), (18, 34, 1), (23, 42, 0), (28, 41, 1)]

The true vertex flag links, each a single circle, are

    [[48, 16, 56], [49, 26, 55], [50, 27, 51], [44, 17, 57], [33, 11, 46], [34, 18, 45], [40, 21, 53], [41, 28, 52], [4, 30, 5], [0, 37, 9], [14, 35, 19], [10, 47, 15], [24, 42, 29], [20, 54, 25], [2, 32, 12], [3, 36, 13], [7, 39, 22], [8, 43, 23], [1, 31, 6, 38]]

All19 link cycles sum360 (120 cubed,90+90+180, orfour90). The face graph
is connected. The exact Euclidean frame/sign development has10 states,
one placement for each original face, retained as affine coordinates in
the certificate. It reconstructs every original native vertex and closure,
checks both transformed endpoints and opposite counterclockwise direction
for all58 transitions, and retains each integer period coefficient.

The explicit independent periods are

    t=(-(9*a+w*b)/4,(w*a+3*b)/4),
    v=(-(9*a+w*b)/4,-(17*w*a+3*b)/4).

The exact shoelace/covolume identity is

    8*area(P)+2*area(Q)=det(t,v)
                         =81*w*a^2/8+27*a*b/4+3*w*b^2/8>0.

All boundary endpoint and area identities hold as polynomial identities
over Q(w)[a,b]. Every directed CCW atomic edge is canceled by its opposite
at identical location modulo integer multiples of t,v. No polygon gluing
sufficiency is assumed solely from equal lengths or rational corner sums.

For any fixed metric, lattice translates of the ten bounded original
convex faces form a locally finite family. Generic interior multiplicity
M has zero net jump across every boundary segment because of those exact
opposite CCW pairs. Paths avoiding the locally finite vertices and line
intersections show M constant almost everywhere. Its mean over a lattice
cell is original motif area/covolume, exactly1. Thus M=1. Any overlapping
interiors would contain an open set with M>=2 at generic points. The locally
finite closed-face union is closed, so any uncovered point would have an
open uncovered neighborhood with M=0 at a generic point. Both are impossible.
Hence the original undecorated convex faces tile the whole plane periodically.

The bounded proposal copied the exact mixed frequency3/5,1/5,1/5 at scale10
(native variants0 six times,3 twice,9 twice). It found the displayed actual
native gluing after2221741 search nodes and1 complete pairing. That finite
search only proposes the witness; the complete native-coordinate, vertex
links, Euclidean boundary and global area proof establish existence.
No negative conclusion from a failed or smaller proposal is used.

[Raw gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit6-flat142-ten-faces.json),
[Euclidean certificate](../certificates/partial-contact-cairo-mixed-quotient-orbit6-flat142-development.json),
[bounded producer](../searches/partial-contact-cairo-mixed-quotient-native-search.py),
[exact development](../searches/partial-contact-cairo-mixed-quotient-native-development.py),
[record](../searches/partial-contact-cairo-mixed-quotient-four-to-one-periodic.md).

The [fresh independent full-cone review](../reviews/partial-contact-cairo-mixed-quotient-four-to-one-periodic-review.md) accepts all native geometry and the whole-plane periodic construction.
