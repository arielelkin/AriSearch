# A full periodic Cairo partner family with the shared right-angle pair exchanged

**Status: independently hostile-reviewed VALID; see [the fresh full-cone review](../reviews/partial-contact-cairo-reversed-right-pair-periodic-review.md) and its no-author-import checker.** The periods and placement were proposed
by root and checked at u=4/5 before this full-parameter proof was developed.
No existence conclusion relies on that sample.

Let w=sqrt3 and 1/w<u<w. Define native Cairo sidewords

    P=(1,u,(3w-u)/2,(wu-1)/2,2),
    Q=(u,1,(3wu-1)/2,(w-u)/2,2u).

Then P,Q admit an explicit doubly periodic tiling, allowing reflections
and partial contacts. For u!=1 each shape has four distinct arms and their
only shared arm labels are Pa=Qb=1,Pb=Qa=u. At u=1 they coincide, giving
the already reviewed adjacent-repeat monotiling. No universality claim
for all their tilings is made; the periodic witness is enough to exclude
this family from the original aperiodic target.

Both native closures hold identically. Positivity is exactly 1/w<u<w:
Pd>0 and Qd>0 give those bounds and all other sides are then positive.
Write native vertices for any word L=(a,b,c,d,e) as

    0,(a,0),(a,b),(a-wc/2,b+c/2),(-e/2,we/2).

These are genuine convex pentagons throughout the interval. The exact
producer verifies all30 nonincident strict support determinants: each is
positive at4/5 and its complete exact real-root set has no root in the
interval. Native side-square identities and closure are also checked.

For L define the quadrant pentagon

    T(L)= [0,(d,0),(d+e/2,we/2),
           (d+(e-a)/2,w(e+a)/2),(0,c)].

If R120 is rotation through120, these vertices are R120*(native_i-native3)
for i=3,4,0,1,2. Thus T(L) is an isometric native copy. Let S(L) be its
four coordinate-axis reflections. Put four P faces at S(P), and four Q
faces at CW90*S(Q)+(0,3w). Repeat all eight by periods

    t=(wu,-w), v=(3wu,3w), det(t,v)=18u>0.

Every face is listed counterclockwise, reversing its vertex order after
an orientation-reversing reflection. Its boundary is subdivided by
bisecting only the native e side. Each face then has six directed atomic
edges, so there are48 atoms. The8 faces are numbered0..7 in order P thenQ,
with reflection signs (-1,-1),(-1,1),(1,-1),(1,1). Inside each face number
six atoms0..5 from T's edge0->1, first half1->2, second half1->2,
edge2->3,edge3->4,edge4->0, transformed and reversed as appropriate.
A global atom is6*face+local.

The following24 pairs use each atom exactly once. An entry(i,j,m,n)
means atom_i=(A,B), atom_j=(C,D) satisfy

    A=D+m*t+n*v, B=C+m*t+n*v.

    (0,6,0,0), (1,15,-1,0), (2,34,1,-1), (3,46,1,-1),
    (4,32,2,-1), (5,17,0,0), (7,14,-1,0), (8,13,-1,0),
    (9,19,-1,0), (10,39,1,0), (11,23,0,0), (12,18,0,0),
    (16,33,2,-1), (20,40,2,0), (21,28,2,0), (22,38,1,0),
    (24,30,0,0), (25,44,-1,0), (26,43,-1,0), (27,37,-1,0),
    (29,41,0,0), (31,45,-1,0), (35,47,0,0), (36,42,0,0).

All endpoint identities are polynomial identities in Q(w)[u], independently
of parameter value and arm ordering. They cancel every directed boundary
segment modulo the lattice, including internal core axes and actual T
subdivisions. They do not require any T to be forced in another tiling.

The native areas are

    area(P)=9u/4+w(1-u^2)/8,
    area(Q)=9u/4-w(1-u^2)/8.

Thus total area of eight motif faces is18u, equal to lattice covolume.

For completeness, here is the global coverage/no-overlap argument.
For a fixed u, the lattice translates of these eight bounded faces form a
locally finite periodic family. Away from their boundary segments define
M(x) as the number of interiors containing x. M is a nonnegative integer
and locally constant. The directed boundary pairing above makes the net
jump of M across every generic boundary segment zero: counterclockwise
face boundaries have the interior on their left, and each matched segment
has the opposite direction and the identical location modulo lattice.
Choose a path between any two generic points, perturbing it to avoid the
locally finite boundary vertices and intersections and cross boundary lines
transversally. Every crossing has zero net jump, so M has the same value
on every open face of the resulting arrangement. Hence M is constant
almost everywhere on the connected plane, or equivalently on its torus.
Its torus integral equals the sum of the original eight face areas,
including multiplicities, so its mean is18u/18u=1. Therefore M=1.

If two distinct original occurrences had overlapping interiors, that
open overlap would contain a point off all boundaries with M>=2,
contradiction. The union of all closed faces is locally finite and closed.
An uncovered point would have an open uncovered neighborhood, containing
a generic point with M=0, also contradiction. Hence the original convex
faces tile the entire plane with disjoint interiors and the two explicit
independent periods. No finite-patch extension or numerical extrapolation
is used.

The exact search is only a finite proposal generator for boundary pairs;
the24 symbolic endpoint identities, strict convexity and area identities
are the certificate. Every identity holds throughout the positive interval.
This construction is independent of the pending complete two-cross flat
classification. Once that reduction is reviewed it supplies periodic escape
for its orbit4 flat20, which is exactly this native family after scaling.

[Producer](../searches/partial-contact-cairo-reversed-right-pair-boundary.py),
[certificate](../certificates/partial-contact-cairo-reversed-right-pair-boundary.json),
[reproducibility record](../searches/partial-contact-cairo-reversed-right-pair-boundary.md).
