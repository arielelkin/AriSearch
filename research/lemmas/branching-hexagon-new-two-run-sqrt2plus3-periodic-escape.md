# A second periodic four-face curve of two-run hexagons

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/branching-hexagon-new-two-run-second-curve-review.md). This is separate from the earlier p=cos(delta)
curve. It excludes another specified family from the main nonperiodicity
target, without resolving that target.

## Native geometry and theorem

For every real delta with0<delta<30degrees, set q=1, p=2cos(delta)>1,
and take the strictly convex native hexagons

    A lengths(p,q,p,q,p,q),
      directions(0,60+delta,120,180+delta,240,300+delta);
    B lengths(p,p,p,q,q,q),
      directions(0,90,180,210-delta,270+delta,330-delta).

The native angles before indexed edges are

    A=(120+delta,120-delta,120+delta,120-delta,120+delta,120-delta),
    B=(150-delta,90,90,150+delta,120-2delta,120+2delta).

**Theorem.** Every pair on this open curve admits a periodic edge-to-edge
plane tiling using rotations, translations and reflections. Any positive
common scaling gives the same construction.

A closes as two three-vector orbits under rotation by120degrees.
B's first three edges sum ip. Its last three directions are obtained by
rotating(0,60+2delta,120) by210-delta. The unit chain has sum
2cos(delta)*exp(i(60+delta)); multiplying by exp(i(210-delta)) gives-ip.
Thus B closes exactly as well.

All side lengths are positive. A's direction increments are60±delta,
alternating. B's increments are(90,90,30-delta,60+2delta,60-2delta,
30+delta). They are strictly between0 and180degrees and sum360.
For a closed polygon with this ordered positive edge data, every directed
side has all nonincident vertices strictly to its left: the cross products
of the other successive edges have one positive run then one negative
run, with strictly positive first term and strictly negative last term.
The partial cross sums stay positive before their final return to0.
Both shapes are consequently strictly convex throughout the stated curve.

At delta=15, p=sqrt(2+sqrt3)=(sqrt6+sqrt2)/2, and B's full native angles
are(135,90,90,165,90,150). This is the catalog tuple(90,90,90,150).
The exact certificates below verify this member in Q(zeta24).

## Explicit quotient for every parameter

Take faces0=A,1=reflected A,2=B,3=reflected B. In each reflected face,
vertex0 stays fixed and the remaining vertex order reverses after reflection
in the real axis. Its native directed side order is the reversed reference
order. Keep all six native side indices of each resulting counterclockwise
face0 through5. The [retained quotient](../certificates/branching-hexagon-new-two-run-sqrt2plus3-four-face-periodic.json)
pairs the sides as follows, always identifying a start with the other's end.

|First side|Partner side|
|---|---|
|(0,0)|(1,3)|
|(0,1)|(2,4)|
|(0,2)|(1,5)|
|(0,3)|(3,0)|
|(0,4)|(2,1)|
|(0,5)|(3,2)|
|(1,0)|(2,3)|
|(1,1)|(3,4)|
|(1,2)|(2,5)|
|(1,4)|(3,1)|
|(2,0)|(3,3)|
|(2,2)|(3,5)|

All24 side occurrences are used exactly once and each pair has equal exact
length. The gluing preserves orientation of the face interiors and its
dual graph is connected. The8 quotient vertex classes are

    [(0,0),(1,4),(3,2)], [(0,1),(1,3),(2,5)],
    [(0,2),(1,0),(2,4)], [(0,3),(1,5),(3,1)],
    [(0,4),(2,2),(3,0)], [(0,5),(2,1),(3,3)],
    [(1,1),(2,3),(3,5)], [(1,2),(2,0),(3,4)].

Remembering the reflected native corner order, the first/third classes
have sum2(120+delta)+(120-2delta)=360. The second/fourth have
2(120-delta)+(120+2delta)=360. The fifth/eighth have
(120+delta)+90+(150-delta)=360, and the sixth/seventh have
(120-delta)+90+(150+delta)=360. All are identities on the full curve.

The actual circular link at each class has one interval per native corner,
and the side endpoint gluings give a connected degree2 graph. Hence each
link is one circle and its angle is360. There is no singularity or boundary.
The quotient is a connected compact orientable flat surface with Euler
characteristic8-12+4=0: a flat torus.

Its complete universal cover is the Euclidean plane. Lifted face interiors
are disjoint and closures cover it, each a rigid copy of native A or B.
The orientation-preserving fixed-point-free Euclidean deck group consists
of translations and forms a rank2 lattice. This gives the claimed periodic
tilings without any frequency-to-existence inference.

## Exact developed delta=15 certificate

The [developed certificate](../certificates/branching-hexagon-new-two-run-sqrt2plus3-four-face-development.json)
records reference vertices, four direct rigid placements, twelve side-cycle
holonomies, the full integral cycle-translation module and native areas.
The field is Q(zeta24), z=exp(i*pi/12), with p=z+z^-1; algebraic values
are encoded as rational8-tuples in its power basis.

A primitive period basis is

    U=-3z^7-4z^5+3z,
    V=2z^5+2z^3.

In Cartesian coordinates,

    U=(sqrt6/2+sqrt2,-sqrt6-5sqrt2/2),
    V=((sqrt6+sqrt2)/2,(sqrt6+3sqrt2)/2).

Every rotational cycle holonomy is identity. The coefficient vectors of
all translations have rational rank2, and integer row Hermite normal form
computes their full generated subgroup. The covolume is10+6sqrt3.
Exact areas are area(A)=9/4+7sqrt3/4 and area(B)=11/4+5sqrt3/4.
Therefore the covolume equals2area(A)+2area(B), agreeing with a degree1
four-face periodic motif.

## Discovery scope, replay and limits

The [slot producer](../searches/branching-hexagon-new-two-run-sqrt2plus3-slot-edge-balance.py)
uses only the trivalent edge-to-edge assembly domain:12 typed corners,
150 oriented cyclic stars and55 two-ended seam keys. Its retained rational
primal has equal species frequencies and four stars of frequency1/2 each.
Reflection averaging gives one copy of each oriented A/B state, and star
adjacencies pin the twelve side pairs above uniquely. No bounded word
search, hierarchy assertion, or strip extension is used.

The exact [quotient replay](../searches/branching-hexagon-new-two-run-sqrt2plus3-periodic-quotient.py)
and [geometry replay](../searches/branching-hexagon-new-two-run-sqrt2plus3-periodic-develop.py)
are read-only by default:

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-sqrt2plus3-periodic-quotient.py
    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-sqrt2plus3-periodic-develop.py

The geometry script checks closure, exact native angles, strict support,
equal paired lengths, complete side use, actual circular links, connectedness,
exact development, translational holonomies, full integral lattice and
area equality. Explicit --output is required to retain its developed data.
The positive theorem needs no claim that every admitted tiling must be
trivalent or edge-to-edge; it constructs one periodic tiling directly.

Every pair on this second curve fails the main target's exclusion of
periodic pair tilings. No claim about a catalog survivor outside this curve,
or a general two-run classification, follows.
