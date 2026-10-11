# A full three-parameter periodic Cairo cone with two linked bank switches

**Status: VALID full-cone construction after fresh independent hostile review.**

Put w=sqrt3 and

    P=(a,b,c,d,e), d=a+w(b-c)/3, e=-a+w*b/3+2*w*c/3,
    Q=(a,B,b,D,f), B=3*w*a-2*c, D=4*a-w*b/3-2*w*c/3,
    f=2*a+2*w*b/3-2*w*c/3=2*d.

Assume all ten original native sides are positive. Then these two Cairo
pentagons have an explicit periodic plane tiling. The construction applies
to the entire positive homogeneous3D cone, including equality resonances;
no genericity or privacy restriction is needed. Its source is orbit0 flat23
of the reviewed two-cross reduction (Pa=Qa,Pb=Qc).

Both native closures hold identically. Two additional useful identities are

    D=3*a-e, B-b=w*(D-a)=w*(2*a-e).

All native vertices are0,(a,0),(a,b),(a-wc/2,b+c/2),(-e/2,we/2), and
edge directions0,90,150,240,300 degrees. Positivity with closed cyclic
edge directions proves strict convexity: relative to any native edge,
support heights strictly increase through positive-sine directions then
decrease to0 through negative-sine directions, staying positive at every
nonincident vertex. Every placed face is an original undecorated convex
pentagon. Subdivision points serve only to specify actual contacts.

If e<2*a, both B>b and D>a. Take four whole P copies and two Q copies
with B split B-b then b, D split D-a then a, and f split d then d. The
four P faces have5 atoms each; two Q faces have8 each. Number darts
0..4,5..9,10..14,15..19,20..27,28..35. Pair equal full formal lengths
using0 for endpoint reversal and1 preservation:

    (21,29,0),(24,32,0),(2,7,1),(12,17,1),(4,9,0),(14,19,0),
    (0,20,1),(5,25,0),(10,28,1),(15,33,0),(1,30,1),(6,31,0),
    (11,22,1),(16,23,0),(3,26,0),(8,27,1),(13,34,0),(18,35,1).

The actual vertex flag links are12 single cycles

    [21,1,30],[22,11,29],[24,16,33],[25,6,32],
    [2,31,7],[3,27,8],[12,23,17],[13,35,18],
    [4,26,5],[0,20,9],[14,34,15],[10,28,19].

Each sums360 as120 cubed or90+90+180. The face graph is connected.
Exact Euclidean development of angle/sign states gives12 placed original
faces, eight P and four Q, and72 actual atomic transitions. Both endpoints,
opposite CCW directions and every integer lattice shift are checked.
Its periods are

    t=(-3*a/2-5*w*b/6+w*c/3, -3*w*a/2-5*b/2+c),
    v=(-6*a,2*w*a).

The exact shoelace identity is

    8*area(P)+4*area(Q)=-det(t,v)>0.

If e>2*a, both B<b and D<a. Take two P copies with b split b-B then B,
two P copies with a split D then a-D, and two Q copies with f split d,d.
All six faces have6 atoms and all pieces are positive. Number their darts
0..5,6..11,12..17,18..23,24..29,30..35. Pair

    (1,7,0),(13,19,0),(0,24,1),(6,30,1),(2,31,1),(8,25,1),
    (3,15,1),(9,21,1),(5,11,0),(17,23,0),(12,27,0),(18,33,0),
    (14,32,0),(20,26,0),(4,35,1),(10,29,1),(16,34,0),(22,28,0).

Its12 actual360 circular vertex links are

    [1,25,8],[2,31,7],[13,27,20],[14,33,19],
    [0,11,24],[6,5,30],[3,15,32],[9,21,26],
    [4,35,16],[10,29,22],[17,34,18],[12,28,23].

The exact Euclidean development has6 original faces, four P and two Q,
with36 checked boundary transitions and independent periods

    t'=(-3*a/2-w*b/6-w*c/3, 5*w*a/2-b/2-c),
    v'=(-3*a/2-5*w*b/6+w*c/3, -3*w*a/2-5*b/2+c).

Its area identity is

    4*area(P)+2*area(Q)=det(t',v')>0.

All endpoint and area identities hold over Q(w)[a,b,c], throughout their
full domains rather than at the source metric samples. Positive original
areas ensure period independence. At e=2*a use the first motif: B=b and
D=a simultaneously, so delete the paired zero B-b and D-a atoms. Remaining
positive atoms still partition the boundaries of the original strictly
convex faces, and every surviving endpoint identity and the unchanged
positive area identity persist. No original tile degenerates.

For each fixed metric, lattice translates of its finite motif of original
faces are locally finite. Generic integer interior multiplicity M has zero
net jump across every boundary because opposite CCW directed atoms pair
at identical locations modulo integer periods. Paths avoiding the locally
finite vertices and intersections show M constant almost everywhere.
Its mean is total original motif area/covolume=1. Thus interiors cannot
overlap: any open overlap would contain a generic point with M>=2. Closed
faces cover every point: the locally finite closed union is closed, so any
missing point would have an open missing neighborhood containing a generic
point with M=0. Both contradict M=1. Therefore each displayed metric has
a periodic plane tiling by its original unmarked P,Q.

An initial scale3 proposal has two odd symbolic piece classes and cannot
pair its18 darts; this is only a bounded frequency-copy parity failure.
Both scale6 native gluing proposals and all geometric certificates are
complete. Seam frequencies were proposal data only, not surface existence
claims. The differing6/12-face lifted motifs are actual Euclidean witnesses.

[First raw gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-six-faces.json),
[first development](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-development.json),
[complementary gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-complement-six-faces.json),
[complementary development](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-complement-development.json),
[proposal producer](../searches/partial-contact-cairo-mixed-quotient-native-search.py),
[Euclidean producer](../searches/partial-contact-cairo-mixed-quotient-native-development.py),
[record](../searches/partial-contact-cairo-mixed-quotient-double-bank-periodic.md).

The [fresh independent whole-cone review](../reviews/partial-contact-cairo-mixed-quotient-double-bank-periodic-review.md) accepts both strict bank domains and their equality merger.
