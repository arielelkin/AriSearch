# A six-face periodic Cairo bank-transfer cone

**Status: VALID full-cone construction after fresh independent hostile review.**

Let w=sqrt3 and

    P=(a,b,c,d,e), d=a+w(b-c)/3, e=-a+w*b/3+2*w*c/3,
    Q=(a,B,b,D,f),
    B=-3*w*a+2*b+2*c,
    D=-2*a+w*b/3+2*w*c/3=e-a,
    f=-4*a+4*w*b/3+2*w*c/3.

Assume all ten original sides are positive. Then P,Q have an explicit
periodic plane tiling by four original P and two original Q faces per
period cell. This sufficient theorem has no privacy, arm-order or generic
restrictions beyond those positive native sidewords. Both Cairo closure
relations hold identically. The discovery source is orbit0 flat11 in the
reviewed two-cross reduction (Pa=Qa,Pb=Qc).

Use native vertices0,(a,0),(a,b),(a-wc/2,b+c/2),(-e/2,we/2) and native
edge directions0,90,150,240,300 degrees. Positive closed cyclic edge
vectors give strict convexity: support heights relative to each oriented
edge increase through the positive-sine directions and then decrease to0
through negative-sine directions, remaining strictly positive at nonincident
vertices. All faces below are these original unmarked convex pentagons.

First suppose B>b. Two P copies remain whole; two P copies have e split
a then D (since e=a+D); each Q has B split B-b then b. All pieces are
positive. Number darts of these six faces by0..4,5..9,10..15,16..21,
22..27,28..33. Pair equal formal lengths with0 endpoint reversal,
1 endpoint preservation:

    (4,9,0),(23,29,0),(27,33,0),(2,12,1),(7,18,1),
    (3,19,1),(8,13,1),(15,26,1),(21,32,1),(0,14,1),
    (5,20,1),(10,28,1),(16,22,1),(1,25,0),(6,31,0),
    (11,24,1),(17,30,1).

The actual single-cycle vertex links, not just corner counts, are

    [4,20,5],[0,14,9],[23,17,30],[24,11,29],[27,10,28],
    [22,16,33],[2,25,12],[3,19,8,13],[7,31,18],
    [15,1,26],[21,6,32].

Each sums360:120 cubed,90+90+180, orfour90. The face graph is connected.
Exact frame/sign Euclidean development produces six placed original
faces, with explicit translations retained in the certificate. All native
coordinates and closure, both endpoints of every transformed boundary
atom, opposite CCW orientation, and integer period shifts are checked.

For B<b, keep two P copies whole. Two P copies have b split b-B then B
and e split a then D. Both Q copies remain whole. Number darts0..4,
5..9,10..16,17..23,24..28,29..33 and pair

    (4,9,0),(11,18,0),(28,33,0),(1,26,0),(6,31,0),
    (2,13,1),(7,20,1),(3,21,1),(8,14,1),(12,25,1),
    (19,30,1),(16,27,1),(23,32,1),(0,15,1),(5,22,1),
    (10,29,1),(17,24,1).

Its independently reconstructed actual links are

    [4,22,5],[0,15,9],[11,30,19],[12,25,18],[28,10,29],
    [24,17,33],[1,16,27],[2,13,26],[6,23,32],
    [7,20,31],[3,21,8,14],

again all360 circular. Its exact development also has six original faces
and all34 directed atomic endpoint identities, paired inversely.

The first motif uses periods

    t=(3*a/2+w*b/6-2*w*c/3, w*a/2+3*b/2),
    v=(-9*a/2+3*w*b/2+2*w*c, -3*w*a/2+3*b/2).

The complementary motif uses t and v-t. Its determinant is unchanged.
The exact polynomial shoelace identity for either motif is

    4*area(P)+2*area(Q)=-det(t,v)>0.

This ensures independence throughout the whole positive domain. All atom
endpoint/integer-shift and area identities are identities over Q(w)[a,b,c],
not extrapolations from a sample. If B=b, use the first motif and remove
the two zero B-b atoms, paired together. Remaining positive atoms still
subdivide the original boundaries and all cancellation identities persist;
the original polygons remain strictly convex and covolume remains positive.

For each metric, lattice translates of the six original faces form a
locally finite family. Their generic interior multiplicity M is integer
and locally constant. Opposite CCW boundary atoms at identical locations
modulo the lattice give net boundary jump0. Paths avoiding the locally
finite boundary vertices/intersections show M constant almost everywhere.
Mean multiplicity is total original face area/covolume=1. Thus no open
interior overlap can exist, and no point can be uncovered: the locally
finite closed-face union is closed, so a missing point would have an open
missing neighborhood. Both would contradict M=1 at generic points.
Therefore these original convex faces tile the entire plane periodically.

A scale3 initial frequency proposal fails atomic parity (three odd color
classes, retained exact certificate), only as a bounded proposal. Doubling
to six concrete faces finds the displayed native gluings. Neither frequency
feasibility nor parity failure is a global tiling conclusion; the explicit
Euclidean boundary/area proof supplies sufficiency.

[Raw first gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-six-faces.json),
[first Euclidean certificate](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-development.json),
[complementary gluing](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-complement-six-faces.json),
[complementary Euclidean certificate](../certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-complement-development.json),
[proposal producer](../searches/partial-contact-cairo-mixed-quotient-native-search.py),
[development producer](../searches/partial-contact-cairo-mixed-quotient-native-development.py),
[record](../searches/partial-contact-cairo-mixed-quotient-bank-transfer-periodic.md).

The [fresh independent whole-cone review](../reviews/partial-contact-cairo-mixed-quotient-bank-transfer-periodic-review.md) accepts both strict bank domains and their equality merger.
