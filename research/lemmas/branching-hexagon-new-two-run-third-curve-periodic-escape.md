# A third periodic curve of two-run hexagons

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/branching-hexagon-new-two-run-third-curve-periodic-escape-review.md). This curve differs from both p=cos(delta) and
p=2cos(delta). Its delta15 member supplies the third periodic catalog orbit.

## Native curve and closure

For every real0<delta<30degrees, put q=1, w=sqrt3 and

    p=2cos(delta)/(1+w),
    A lengths(p,q,p,q,p,q),
      directions(0,60+delta,120,180+delta,240,300+delta);
    B lengths(p,p,p,q,q,q),
      directions(0,30,60,150-delta,210+delta,270-delta).

Angles before indexed edges are

    A=(120+delta,120-delta,120+delta,120-delta,120+delta,120-delta),
    B=(90-delta,150,150,90+delta,120-2delta,120+2delta).

**Theorem.** Every pair on this curve admits a periodic edge-to-edge plane
tiling by rotations, translations and reflections. Positive common scaling
also preserves the construction.

A closes as two independent three-vector orbits under rotation120.
B's p-chain sum is p(1+w)exp(i30)=2cos(delta)exp(i30). The unit q-chain
(0,60+2delta,120) has sum2cos(delta)exp(i(60+delta)); rotating it by
150-delta gives2cos(delta)exp(i210), the opposite vector. Thus B closes.

All edge lengths are positive. A's successive direction increments are
60±delta, alternating; B's are(30,30,90-delta,60+2delta,60-2delta,
90+delta). They lie strictly in(0,180) and sum360. Relative to any side,
the following edge cross products have one positive run then one negative
run, with strictly positive first and strictly negative last term. Their
partial cross sums remain positive before final closure. Hence every
nonincident vertex lies strictly in that side's interior half-plane:
both polygons are strictly convex for every parameter in the interval.

At delta15, p=1/sqrt2. B has directions(0,30,60,135,225,255) and native
angles(75,150,150,105,90,150), the catalog tuple(150,150,90,150).

## Explicit eight-face quotient

Take faces0,1 unreflected A,2,3 reflected A,4,5 unreflected B,6,7 reflected
B. A reflected face keeps native vertex0 fixed and reverses the remaining
vertex order after reflection in the real axis. Its counterclockwise side
indices0..5 follow the reversed side order. The
[quotient certificate](../certificates/branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json)
uses these native side pairs, identifying starts with partner ends:

|First side|Partner side|
|---|---|
|(0, 0)|(6, 4)|
|(1, 0)|(7, 4)|
|(0, 1)|(7, 2)|
|(1, 1)|(6, 2)|
|(0, 2)|(2, 1)|
|(1, 2)|(3, 1)|
|(0, 3)|(4, 4)|
|(1, 3)|(5, 4)|
|(0, 4)|(2, 3)|
|(1, 4)|(3, 3)|
|(0, 5)|(7, 0)|
|(1, 5)|(6, 0)|
|(2, 0)|(4, 5)|
|(3, 0)|(5, 5)|
|(2, 2)|(7, 1)|
|(3, 2)|(6, 1)|
|(2, 4)|(4, 3)|
|(3, 4)|(5, 3)|
|(2, 5)|(5, 1)|
|(3, 5)|(4, 1)|
|(4, 0)|(5, 0)|
|(4, 2)|(5, 2)|
|(6, 3)|(7, 3)|
|(6, 5)|(7, 5)|

All48 native side occurrences appear exactly once and every pair has equal
exact length. The reverse boundary gluing preserves face orientation, and
the dual face graph is connected. The16 vertex classes are

    [(0, 0), (6, 5), (7, 0)],
    [(0, 1), (6, 4), (7, 3)],
    [(0, 2), (2, 2), (7, 2)],
    [(0, 3), (2, 1), (4, 5)],
    [(0, 4), (2, 4), (4, 4)],
    [(0, 5), (2, 3), (7, 1)],
    [(1, 0), (6, 0), (7, 5)],
    [(1, 1), (6, 3), (7, 4)],
    [(1, 2), (3, 2), (6, 2)],
    [(1, 3), (3, 1), (5, 5)],
    [(1, 4), (3, 4), (5, 4)],
    [(1, 5), (3, 3), (6, 1)],
    [(2, 0), (4, 0), (5, 1)],
    [(2, 5), (4, 3), (5, 2)],
    [(3, 0), (4, 1), (5, 0)],
    [(3, 5), (4, 2), (5, 3)].

For every class the symbolic angle sum is360+0delta. There are precisely
four possible angle identities:

    (120+delta)+150+(90-delta)=360,
    (120-delta)+150+(90+delta)=360,
    2(120+delta)+(120-2delta)=360,
    2(120-delta)+(120+2delta)=360.

The actual endpoint-gluing link of each class is connected of degree2,
so it is one circle. Its angle is360, making every vertex nonsingular.
The result is a compact connected orientable flat surface without boundary,
with Euler characteristic16-24+8=0: a flat torus. Its complete universal
cover is the Euclidean plane, covered by the lifted native polygon faces
with disjoint interiors. Orientation-preserving fixed-point-free Euclidean
deck transformations are translations; their group is a rank2 lattice.
Thus this is a global periodic tiling throughout the curve, not an
inference from local corner frequencies or continuity of a single sample.

## Exact delta15 development

The [developed certificate](../certificates/branching-hexagon-new-two-run-third-orbit-eight-face-development.json)
works in Q(zeta24), with z=exp(i*pi/12), p=(z^3+z^-3)/2. It records native
vertices, all8 direct placements of the specified reflected/reference
faces,24 side holonomies and the full integral translation module.
Every rotational holonomy is identity, and the rational coefficient
matrix of all translations has rank2. Integer row Hermite normal form
computes the full subgroup rather than a possibly nonprimitive subset.

The retained basis is

    U=z^7+(5/2)z^5+(5/2)z^3+(1/2)z,
    V=4z^7+8z^5+6z^3.

Put x=sqrt6/2+sqrt2. In Cartesian coordinates U=(x,2x), V=(2x,6x).
The integer determinant1 basis change H=3U-V, K=V-2U gives the simpler
primitive rectangular periods

    H=(x,0), K=(0,2x).

Their covolume is7+4sqrt3. Exact areas are

    area(A)=3/4+5sqrt3/8, area(B)=1+3sqrt3/8.

Therefore covolume=4area(A)+4area(B), agreeing with the degree1 eight-face
motif and ruling out hidden covering multiplicity.

## Finite search and replay

The complete catalog native-slot balance produces a rational four-star
primal at this tuple. Reflection averaging pins10 nonself typed side pairs
and4 same-slot pairs. Two physical copies of each oriented face state give
8 faces. Each nonself pair has two matchings and each same-slot pair is
forced: the exact finite search domain is1024 lifts. Attempt278 supplies
the positive quotient above. Failure of1024 lifts would not have implied
infinite untileability.

[Guided quotient producer](../searches/branching-hexagon-new-two-run-third-orbit-periodic.py),
[exact development producer](../searches/branching-hexagon-new-two-run-third-orbit-periodic-develop.py):

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-third-orbit-periodic.py
    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-third-orbit-periodic-develop.py

Normal replay is read-only; --output is required for retained writes.
The sample development checks closure, native angles, strict support,
side use, exact equal paired lengths, actual circular links, connectedness,
rigid placements, translational holonomies, integral lattice and motif area.
The general curve relies on the explicit symbolic geometry and unchanged
oriented flat quotient, requiring no sample-to-curve continuity assumption.
No unrestricted two-run classification or main-target resolution follows.
