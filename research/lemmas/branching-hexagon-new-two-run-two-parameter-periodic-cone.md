# A two-parameter periodic cone of alternating/two-run hexagon pairs

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/branching-hexagon-new-two-run-two-parameter-periodic-cone-review.md). This strengthens the three previously extracted
one-parameter constructions without changing their retained artifacts.
It is a positive tiling theorem, not a general classification or a solution
of the main target.

## Exact parameter domain and native shapes

Let delta and gamma be arbitrary real angles in degrees satisfying

    0<delta<30, 0<gamma<120-delta.

Set q=1 and

    p=2cos(delta)/(1+2cos(gamma)).

Take native hexagons with counterclockwise directed side data

    A lengths(p,q,p,q,p,q),
      directions(0,60+delta,120,180+delta,240,300+delta);
    B lengths(p,p,p,q,q,q),
      directions(0,gamma,2gamma,gamma+120-delta,
                 gamma+180+delta,gamma+240-delta).

The native angles before indexed edges0..5 are

    A=(120+delta,120-delta,120+delta,120-delta,120+delta,120-delta),
    B=(60+gamma-delta,180-gamma,180-gamma,60+gamma+delta,
       120-2delta,120+2delta).

**Theorem.** For every point in this open two-dimensional parameter domain,
A and B admit a periodic edge-to-edge plane tiling by rotations, translations
and reflections. Any positive common scaling also works. The theorem
includes p=q and imposes no distinct binary-length restriction.

Because gamma<120-delta<120, cos(gamma)>-1/2, so the denominator of p
is positive. Also cos(delta)>0; every native side has positive length.
The lengths may coincide. The side pairing below remains valid when they do.

## Exact closure and strict convexity on the full domain

A closes as the sum of two three-vector orbits under rotation120degrees.
B's first three native edges sum

    p(1+exp(i gamma)+exp(2i gamma))
      =p(1+2cos(gamma))exp(i gamma)
      =2cos(delta)exp(i gamma).

Its last three directions are a rotation by gamma+120-delta of the
unit chain(0,60+2delta,120). The latter sums

    exp(i60)+exp(i(60+2delta))
      =2cos(delta)exp(i(60+delta)).

After the stated rotation, the q-chain sum is
2cos(delta)exp(i(gamma+180)), the opposite of the p-chain sum. Thus B
closes exactly for every real parameter, not only at an algebraic fixture.

The successive direction increments are

    A:60+delta,60-delta,60+delta,60-delta,60+delta,60-delta;
    B:gamma,gamma,120-gamma-delta,60+2delta,60-2delta,
      120-gamma+delta.

All lie strictly between0 and180 and sum360. For B, the only potentially
zero terms are gamma,120-gamma-delta,60-2delta and120-gamma+delta;
the domain makes all positive, with the last>2delta. Every term is at
most150 on the closed parameter polygon, so the upper bound is strict.
A's increments lie between30 and90.

For any chosen directed side of either closed polygon, the cross products
of the successive remaining edge vectors have one positive run followed
by one negative run. The first is strictly positive and the last strictly
negative. Their partial sums remain positive before their final return to0.
Every nonincident vertex therefore lies strictly in that side's interior
half-plane. Both shapes are nondegenerate strictly convex hexagons for
every parameter in the stated open domain.

## A fixed eight-face flat quotient

Use precisely the native side pairing of the third-orbit eight-face
construction. The [standalone cone certificate](../certificates/branching-hexagon-new-two-run-two-parameter-periodic-cone.json)
contains all8 face states,24 native side pairs and16 vertex classes.
Faces0,1 are unreflected A;2,3 reflected A;4,5 unreflected B;6,7 reflected
B. In a reflected state native vertex0 stays fixed, and the vertex order
reverses after reflection in the real axis. Native side order consequently
reverses. Every side is paired start-to-partner-end.

The certificate checks all48 native side occurrences appear exactly once,
and both sides of every pair have the same label p or q. Each match is
therefore metrically exact throughout the parameter domain, including the
coincidence locus p=q. The quotient's dual face graph is connected.
All gluings reverse the induced boundary direction, so its face orientation
is consistent and the surface is orientable.

The actual circular link of each vertex class is a connected degree2 graph
of its three corner intervals. All16 native angle sums are identically
360+0delta+0gamma after applying the actual reflected native corner order.
Only four forms occur:

    (120+delta)+(180-gamma)+(60+gamma-delta)=360,
    (120-delta)+(180-gamma)+(60+gamma+delta)=360,
    2(120+delta)+(120-2delta)=360,
    2(120-delta)+(120+2delta)=360.

Thus every circular link has angle360. The quotient is a connected compact
orientable Euclidean surface without boundary or singularities, with
Euler characteristic16-24+8=0. It is a flat torus for every individual
parameter point. This conclusion uses exact closure, strict convexity,
actual circular links and angle identities, not continuity from a sample.

The complete universal cover of this flat torus is isometric to the
Euclidean plane. Its lifted faces have disjoint interiors and closures
cover the plane, each a rigid native A or B. Every orientation-preserving
fixed-point-free Euclidean deck isometry is a translation; the deck group
is a rank2 lattice. The resulting plane tiling is periodic. Neither
frequency feasibility nor finite neighborhood coverage supplies this
existence argument.

## Previous curves and an exact fixture

The cone contains all three native curves already extracted, for the full
interval0<delta<30:

|gamma|p|Earlier construction|
|---:|---|---|
|60|cos(delta)|[first curve](branching-hexagon-new-two-run-periodic-escape.md)|
|90|2cos(delta)|[second curve](branching-hexagon-new-two-run-sqrt2plus3-periodic-escape.md)|
|30|2cos(delta)/(1+sqrt3)|[third curve](branching-hexagon-new-two-run-third-curve-periodic-escape.md)|

The previously recorded first/second4-face quotients and their exact
periods remain valid. The cone theorem supplies this additional8-face
quotient at those same parameter points. No claim that either period
lattice is the full symmetry group of a tiling is needed.

At delta15,gamma30, p=1/sqrt2. The
[exact developed fixture](../certificates/branching-hexagon-new-two-run-third-orbit-eight-face-development.json)
checks native geometry in Q(zeta24), all side matches, actual links,
rigid placements, translational holonomies, the full integral cycle lattice
and motif-area equality. Primitive rectangular periods there are
(x,0),(0,2x), x=sqrt6/2+sqrt2. Its covolume7+4sqrt3 equals
4area(A)+4area(B). These sample computations support only this fixture;
the proof on the full cone is the symbolic argument above.

The distinct-length catalog remains a separate finite result. Allowing
p=q here requires no extension of its binary-color obstruction domain:
this is a direct positive side pairing which is valid even with extra
metric coincidences.

## Exact symbolic replay and limits

[Producer](../searches/branching-hexagon-new-two-run-two-parameter-periodic-cone.py):

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-two-parameter-periodic-cone.py

Normal replay is read-only; explicit --output is required for retained
writes. The producer checks complete side use, label equality, connected
oriented face gluing, every actual circular link and all16 affine coefficient
triples(360,0,0). It also verifies each direction increment has nonnegative
minimum and maximum<180 on the closed parameter polygon with vertices
(0,0),(30,0),(30,90),(0,120). Each nonconstant increment is then strictly
positive in its interior; constant increments are positive. Denominator
positivity, exact trigonometric closure and strict support are proved above.

No period bound or randomization occurs. This proves a specified open
parameter family has periodic tilings; it makes no universal claim about
all alternating/two-run hexagon pairs and does not resolve the main target.
