# A ten-face periodic Cairo cone with two positive residual contacts

**Status: VALID complete exact sufficient subcone after fresh independent hostile review.**
The complementary positive half-cone is not asserted to tile or be untileable.

Let w=sqrt3,a>0,b>=a/w and define native sidewords

    P=(a,b,(3*w*a+b)/4,(a+w*b)/4,(a+w*b)/2),
    Q=(4*b-w*a,a,3*w*b-2*a,b,2*b).

Then P,Q have a doubly periodic plane tiling with eight original P and two
original Q faces in the period cell. Their full original positivity domain
is b>w*a/4; the present sufficient statement covers the closed higher
subcone b>=a/w only. No privacy, genericity or additional arm-order
assumption is required. Source is orbit6 flat239 of the reviewed two-cross
reduction, Pa=Qb,Pb=Qd. Both native Cairo closures hold identically.

Use native vertices0,(a,0),(a,b),(a-wc/2,b+c/2),(-e/2,we/2) with edge
directions0,90,150,240,300 degrees. Strict native convexity follows from
positive closed cyclic edge vectors: the relative support heights increase
through positive-sine directions then decrease to0 through negative-sine
directions, staying positive at every nonincident vertex. Every placed
face remains an original unmarked convex pentagon.

Write c=(3wa+b)/4,d=(a+wb)/4,e=2d,A=4b-wa,C=3wb-2a,f=2b.
For b>a/w take six P copies whole; two P copies have e split d then d.
Each Q has A split b then A-b, C split a then C-a, and f split b then b.
All pieces are positive because

    A-b=3*b-w*a>0, C-a=w*(A-b)>0.

The six whole P faces have5 atoms each, two split P have6, and two split Q
have8, totaling58. Their native dart blocks are0..4,5..9,10..14,15..19,
20..24,25..29,30..35,36..41,42..49,50..57. Pair equal full formal lengths
with0 endpoint reversal and1 preservation:

    [(43, 51, 0), (46, 54, 0), (4, 9, 0), (14, 19, 1), (24, 29, 1), (2, 12, 1), (7, 22, 1), (17, 32, 1), (27, 38, 1), (0, 30, 1), (5, 36, 1), (10, 44, 0), (15, 45, 1), (20, 52, 0), (25, 53, 1), (3, 41, 1), (8, 35, 1), (13, 40, 0), (18, 39, 1), (23, 34, 0), (28, 33, 1), (1, 57, 1), (6, 49, 1), (11, 50, 0), (16, 55, 1), (21, 42, 0), (26, 47, 1), (31, 56, 0), (37, 48, 0)]

The true vertex flag-link circles are

    [[43, 21, 52], [44, 11, 51], [46, 16, 55], [47, 26, 54], [4, 36, 5], [0, 30, 9], [14, 40, 19], [10, 45, 15], [24, 34, 29], [20, 53, 25], [2, 50, 12], [3, 41, 13], [7, 42, 22], [8, 35, 23], [17, 56, 32], [18, 39, 28, 33], [27, 48, 38], [1, 57, 31], [6, 49, 37]]

Each of19 cycles sums360:120 cubed,90+90+180 orfour90. Face adjacency is
connected. Separate exact Euclidean development has10 original face states.
It reconstructs every original native vertex/closure and checks both
endpoints, opposite CCW direction and integer period shift of every58
atomic transition. All translations and frame signs are retained explicitly
in the certificate rather than inferred from rational seam frequencies.

The periods are

    t=((3*a+11*w*b)/4,(-3*w*a+15*b)/4),
    v=(0,-w*a-3*b).

The exact polynomial shoelace identity is

    8*area(P)+2*area(Q)=-det(t,v)
                         =3*w*a^2/4+21*a*b/2+33*w*b^2/4>0.

All endpoint/integer shift and area identities hold over Q(w)[a,b], so the
construction applies throughout this sufficient subcone and all its added
resonances. At b=a/w both residuals vanish. Delete the four zero A-b and
C-a atoms from the two original Q faces, each paired with another zero
atom. The remaining boundaries and opposite CCW pair identities still
hold; original pentagons remain positive and strictly convex, and covolume
is unchanged and positive. This is an explicit subdivision merger.

For a fixed metric, lattice translates of the ten original convex faces
are locally finite. Generic integer multiplicity M has net boundary jump0
because every directed CCW boundary piece has an opposite counterpart
at identical location modulo periods. Generic paths avoid locally finite
vertices/intersections and show M constant almost everywhere. Its mean
is total original motif area/covolume=1. Thus M=1. An interior overlap
would yield a generic point with M>=2. A missing point would have an open
missing neighborhood because the locally finite closed-face union is closed,
yielding a generic point with M=0. Both are impossible. Hence the original
prototiles tile the full plane with the two independent periods.

The bounded proposal copied exact mixed frequencies0:3/5,1:1/5,9:1/5
at scale10. First exact connected candidate occurs after102808 nodes and1
complete pairing. This is a proposal generator only. A separate selected
low-subcone scale10 variant multiset exhausts20910 nodes/189 completed
pairings without a360 gluing, including when connectedness is omitted.
This bounded failure is not an untileability conclusion and does not
exclude other variants, frequencies, larger quotients or plane tilings.

[Raw high-subcone gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit6-flat239-ten-faces.json),
[Euclidean certificate](../certificates/partial-contact-cairo-mixed-quotient-orbit6-flat239-development.json),
[bounded proposal producer](../searches/partial-contact-cairo-mixed-quotient-native-search.py),
[exact development](../searches/partial-contact-cairo-mixed-quotient-native-development.py),
[record](../searches/partial-contact-cairo-mixed-quotient-double-residual-periodic.md).

The [fresh independent scoped review](../reviews/partial-contact-cairo-mixed-quotient-double-residual-periodic-review.md) accepts both the strict positive-residual domain and its equality merger.
