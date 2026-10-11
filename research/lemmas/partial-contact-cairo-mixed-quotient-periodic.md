# An explicit three-parameter periodic Cairo partner cone from mixed native face gluing

**Status: VALID complete construction after fresh independent hostile review.**
This is a sufficient periodic construction, not an inference from rational seam balance.

Put w=sqrt3. Let a,b,c be parameters and define

    d=a+w(b-c)/3, e=-a+w*b/3+2*w*c/3,
    A=a,
    B=(w+3)*a/2+(w+3)*b/6+(w/3-1)*c,
    C=(3*w+3)*a/2+(w+3)*b/6-(2*w/3+1)*c,
    D=c,
    f=(3*w+5)*a/2+(w+1)*b/2-(w+1)*c.

Assume all ten sides of P=(a,b,c,d,e), Q=(A,B,C,D,f) are strictly
positive. Then these two original convex pentagons have an
explicit doubly periodic tiling allowing reflections and partial contacts.
No privacy or generic event restrictions are needed for the construction.
The native shared identities are Pa=Qa and Pc=Qd. The domain is a
three-dimensional open cone; homogeneity leaves two shape parameters.

Both native Cairo closures hold identically. Also f=C+d. Each native word
has edges at directions0,90,150,240,300 degrees. Positivity and closure
make these genuinely strictly convex pentagons: for any fixed oriented
edge, the other cyclic edge directions have positive sine first, then
negative sine. The successive support heights therefore strictly increase
and then decrease to zero, staying positive at every nonincident vertex.
All native turns are60 or90 degrees.

First suppose B>b. Keep P's five native vertices. On Q's native B side, insert the point at
length B-b from its 90-degree endpoint, leaving a final piece of length b.
On Q's native f side, insert the point at length C from its native120
endpoint adjacent to D, leaving a final piece of length d. These are
strict interior points because B>b and C,d>0. Thus P has five atomic
edges and Q has seven; subdivision marks are not decorations or matching
rules on the prototiles.

The bounded proposal contains two copied P faces and two copied Q faces.
Its darts are0..4,5..9,10..16,17..23 in native cyclic order, respectively.
The first two are P; each Q has atomic lengths

    a, B-b, b, C, c, C, d,

with directions0,90,90,150,240,300,300. The P lengths are a,b,c,d,e.
Pair the following darts, with0 meaning endpoints reversed and1 meaning
endpoints preserved:

    (4,9,0), (11,18,0), (0,10,1), (5,17,1),
    (1,19,1), (6,12,1), (2,14,0), (7,21,0),
    (3,23,1), (8,16,1), (13,22,1), (15,20,1).

Every paired atomic length is identical as a linear form. The actual
vertex links, reconstructed as cycles of incoming/outgoing corner flags,
are

    [4,17,5], [0,10,9], [11,1,19], [12,6,18],
    [2,15,20], [7,22,13], [3,23,14], [8,16,21].

Their native angles are respectively120+120+120 or90+90+180, summing360.
The quotient is connected. These checks supply a concrete nonsingular
flat gluing, but the existence proof below uses the retained Euclidean
coordinates and boundary identities directly.

For exact placements, write F(theta,s)=R(theta*30 degrees)*diag(1,s).
Use the native atomic coordinates retained in the certificate. Start
face0 at theta=0,s=1, translation0. Across paired dart i on a placed face
and dart j on its neighbor, let same be the last entry above. Set

    s'=s*(-1 if same else1),
    theta'=theta+s*dir(i)-s'*dir(j)+(0 if same else6) mod12,
    t'=t+F(theta,s)*V(i if same else next(i))-F(theta',s')*V(j).

The finite direction/sign lift has exactly eight states, in retained
breadth-first order:

    (0,0,1),(2,0,-1),(3,6,-1),(2,3,1),
    (1,6,1),(3,9,1),(0,3,-1),(1,9,-1).

Their translations are explicit affine forms in a,b,c in the certificate.
This gives four original P faces and four original Q faces. The exact
producer verifies every original native coordinate and closure, every
local piece endpoint and both endpoints of every transformed transition.

The two lattice periods are

    t=(-L,L), L=3*a/2+w*b/6+w*c/3=2*a+e/2,
    v=(H,H), H=(2*w+9/2)*a+(w/2+2)*b-(w+2)*c.

All48 lifted atomic edges are paired with opposite counterclockwise
orientations modulo integer multiples of t,v. The certificate retains
all48 directed transitions and their exact integer period coefficients;
they form24 inverse pairs. These endpoint identities hold polynomially
over Q(w)[a,b,c], so they apply throughout the stated cone, including
additional arm equalities or event resonances. Face orientation is reversed
after a reflection when taking its counterclockwise boundary.

The independently reconstructible shoelace identity is

    4*area(P)+4*area(Q) = 2*L*H = -det(t,v).

The left side is strictly positive by the convexity already proved, and
L=2a+e/2>0. Thus H>0, and these are two independent periods throughout
the whole domain. This avoids any period determinant or convexity claim
based on a single metric sample.

For a fixed metric, translate the eight original convex faces by the
lattice. The family is locally finite. At a generic point let M be the
number of containing interiors. Exact opposite counterclockwise boundary
pairings make every net boundary jump of M zero, including coincident
segments. A path between generic points can avoid all locally finite
vertices and intersections and cross the lines transversally. Thus M is
constant almost everywhere. Its mean over a fundamental parallelogram
is the total face area divided by its covolume, exactly1. Hence M=1.
An interior overlap would contain a generic point with M>=2. An uncovered
point would have an open uncovered neighborhood, since the locally finite
union of closed faces is closed, containing a generic point with M=0.
Both are impossible. Therefore the original unmarked P,Q tile the plane
with disjoint interiors and the two displayed periods.

For B<b use the independently developed complementary proposal. Split
P's native b side into b-B then B, and keep its native e whole. Q's native
B remains whole, and its f is still split C then d. Each of four proposal
faces now has six atoms. With darts0..5,6..11,12..17,18..23, pair

    (1,7,0),(5,11,0),(0,12,1),(6,18,1),
    (2,19,1),(8,13,1),(3,15,0),(9,21,0),
    (4,23,1),(10,17,1),(14,22,1),(16,20,1).

All split pieces are positive. Its actual circular vertex links are

    [1,13,8],[2,19,7],[5,18,6],[0,12,11],
    [3,16,20],[9,22,14],[4,23,15],[10,17,21],

again all360. Exact development gives eight original faces and the same
periods and area identity, with all48 endpoint identities checked.
Its Euclidean motif is actually identical to the first modulo the lattice:
all species/frame/translation entries agree except the (P,theta6,s1)
entry, whose complementary translation is the original translation minus t.
Thus this is a different actual boundary subdivision of the same original
periodic face family. It supplies the B<b domain with the same global proof.

For B=b use the first construction with Q's B-b piece of length0. Remove
these four zero atomic segments from the eight-face lifted motif. The
remaining positive segments still partition the boundaries of the original
strictly convex faces; every deleted segment is paired with another deleted
zero segment. The retained polynomial endpoint identities cancel every
remaining directed boundary. The unchanged strictly positive area equals
covolume, so the same multiplicity proof applies. This is an explicit
zero-subdivision merger, not a limiting assumption about coverage.

The discovery source is orbit2 flat23, actual-order chambers0 and6 of the
reviewed two-cross reduction. The construction now covers the entire
positive homogeneous3D flat, including additional equality resonances.
In the exact two-cross privacy domain B=b is absent, but it is harmless
for this stronger sufficient theorem. Necessary frequency data was used
only to propose a finite number of copied faces. No bounded-patch or
surface existence conclusion was drawn from that data.

[Bounded proposal producer](../searches/partial-contact-cairo-mixed-quotient-four-faces.py),
[raw gluing](../certificates/partial-contact-cairo-mixed-quotient-four-faces.json),
[exact development producer](../searches/partial-contact-cairo-mixed-quotient-development.py),
[geometric certificate](../certificates/partial-contact-cairo-mixed-quotient-development.json),
[complementary raw producer](../searches/partial-contact-cairo-mixed-quotient-complementary.py),
[complementary gluing](../certificates/partial-contact-cairo-mixed-quotient-complementary.json),
[complementary development](../searches/partial-contact-cairo-mixed-quotient-complementary-development.py),
[complementary geometric certificate](../certificates/partial-contact-cairo-mixed-quotient-complementary-development.json),
[reproducibility record](../searches/partial-contact-cairo-mixed-quotient-development.md).

The [fresh independent whole-cone review](../reviews/partial-contact-cairo-mixed-quotient-periodic-review.md) accepts both strict contact orders and the zero-subdivision equality case.
