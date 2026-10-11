# A periodic four-face construction on the two-run hexagon curve

**Status:** freshly independently hostile-reviewed **VALID** for the full curve; see [review](../reviews/branching-hexagon-new-two-run-periodic-escape-review.md).
This is a periodic escape on a whole specified parameter curve,
not a solution of the main target.

For every real delta with0<delta<30degrees, put q=1, p=cos(delta),
and take the directed native side data

    A lengths(p,q,p,q,p,q),
      directions(0,60+delta,120,180+delta,240,300+delta);
    B lengths(p,p,p,q,q,q),
      directions(0,60,120,180-delta,240+delta,300-delta).

Angles before indexed edges are

    A=(120+delta,120-delta,120+delta,120-delta,120+delta,120-delta),
    B=(120-delta,120,120,120+delta,120-2delta,120+2delta).

**Theorem.** Every pair on this entire open curve admits a periodic
edge-to-edge plane tiling using rotations and translations of both shapes.
Reflections are not needed. Any positive common scaling also works.

The shapes close exactly. A is the sum of two three-vector orbits under
rotation by120degrees. Write C=cos(delta), S=sin(delta), and w=sqrt3.
B's first three edges sum(C,wC), and its last three sum(-C,-wC).
All edge lengths are positive. Its successive direction increments are

    A:60+delta,60-delta,60+delta,60-delta,60+delta,60-delta;
    B:60,60,60-delta,60+2delta,60-2delta,60+delta.

They lie strictly between0 and180degrees and sum360. This proves strict
convexity for the closed polygons: relative to any directed side, the
cross products of the successive other edge vectors have one positive
run followed by one negative run. The first is strictly positive and the
last strictly negative. The partial cross sums therefore remain positive
at every nonincident vertex before returning to0 at closure. Thus every
nonincident vertex lies strictly in that side's interior half-plane.

The exact numerical certificates below instantiate delta=15degrees,
where p=(sqrt6+sqrt2)/4. For that member the full geometry lies in
Q(zeta24), z=exp(i*pi/12), p=(z+z^-1)/2. The symbolic quotient proof
works for every real delta in the stated open interval.

## Explicit four-face quotient

For any delta in the stated interval, take faces0,1 to be reference A
copies and2,3 reference B copies.
Keep their six native edges indexed0 through5, counterclockwise. The
[retained quotient](../certificates/branching-hexagon-new-two-run-four-face-periodic.json)
pairs native sides as follows. A side start is identified with its partner's
end, and its end with its partner's start.

|First side|Partner side|
|---|---|
|(0,0)|(2,0)|
|(1,0)|(3,0)|
|(0,1)|(3,4)|
|(1,1)|(2,4)|
|(0,2)|(2,2)|
|(1,2)|(3,2)|
|(0,4)|(3,1)|
|(1,4)|(2,1)|
|(0,3)|(1,3)|
|(0,5)|(1,5)|
|(2,3)|(3,3)|
|(2,5)|(3,5)|

All24 native side occurrences appear exactly once, and each pair has
identical exact length. Reverse boundary gluing preserves the orientation
of the face interiors. The dual face graph is connected. The quotient
has8 vertex classes, each containing three native corners. The classes,
using (face,corner) slots, are

    [(0,1),(2,0),(3,5)], [(0,2),(2,3),(3,4)],
    [(0,4),(1,3),(3,2)], [(0,5),(1,0),(3,1)],
    [(1,1),(2,5),(3,0)], [(1,2),(2,4),(3,3)],
    [(0,3),(1,4),(2,2)], [(0,0),(1,5),(2,1)].

Every angle sum is identically360: the first and fifth are
(120-delta)+(120-delta)+(120+2delta); the second and sixth are
(120+delta)+(120+delta)+(120-2delta); the other four use
(120+delta)+(120-delta)+120. No isolated parameter equation is required.

The actual vertex-link check is essential: give each corner its link
interval and glue its two endpoints according to the side identifications.
Each retained vertex class yields a connected degree2 link graph, hence one
circle. The total angle is360, so its Euclidean metric is nonsingular.
Thus the quotient is a connected compact orientable flat surface without
boundary. Its Euler characteristic is8-12+4=0: it is a flat torus.

The complete universal cover of this flat torus is the Euclidean plane,
and its developed faces are rigid copies of A or B. Their interiors are
disjoint and their closures cover the plane. Orientation-preserving deck
isometries are fixed-point-free, so they are translations. The deck group
is a rank2 lattice; the resulting tiling is periodic. This global surface
argument supplies existence, unlike corner-frequency feasibility.

## Exact developed periods and motif area at delta=15

For the delta=15 member, the [developed certificate](../certificates/branching-hexagon-new-two-run-four-face-development.json)
contains reference vertices, all4 rotation/translation placements, all12
side-cycle holonomies, the full integral translation module and exact
native areas. All coefficients are rational8-tuples in the power basis of
Q(zeta24); the embedding is fixed by z=exp(i*pi/12).

A primitive period basis is

    U=-2z^7-3z^5+2z,
    V=2z^5+z^3.

In Cartesian coordinates,

    U=((sqrt6+3sqrt2)/4,(-3sqrt6-7sqrt2)/4),
    V=(sqrt6/2,sqrt6/2+sqrt2).

Every cycle's rotational holonomy is identity. The rational coefficient
matrix of the translational holonomies has rank2. Integer row Hermite
normal form computes their full generated subgroup, with no presumed
choice of primitive cycles. The covolume is

    9/2+3sqrt3.

The exact tile areas are

    area(A)=15/16+7sqrt3/8,
    area(B)=21/16+5sqrt3/8.

Therefore covolume=2area(A)+2area(B), matching the total four-face motif.
This is a degree1 periodic tiling, not a multiple covering.

## How the concrete quotient was located

The [actual-slot model](../searches/branching-hexagon-new-two-run-slot-edge-balance.py)
keeps all12 typed native corners, both cyclic orientations, all216 oriented
trivalent native stars and48 two-ended seam keys. Its rational primal uses
only four oriented stars with frequency1/2 each and equal species
frequencies. Those marginals concern trivalent edge-to-edge assemblies only and
are not used as an existence proof. No absence of partial contacts in
other possible tilings is required for the positive theorem.

Reflection symmetrization and actual slot adjacency expose a seam pattern.
One component uses only unreflected native face states. Same-slot seams
require two physical copies of each state. Four mixed seam types each
admit two matchings between the copies; four same-slot seams are forced.
The [guided quotient producer](../searches/branching-hexagon-new-two-run-periodic-quotient.py)
therefore searches exactly16 pre-stated two-copy lifts. The positive
quotient occurs at attempt6. No negative inference would have followed
from exhaustion of these16 lifts.

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-periodic-quotient.py
    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-periodic-develop.py

Normal replay is read-only; --output is required to retain a file.
The [geometry producer](../searches/branching-hexagon-new-two-run-periodic-develop.py)
checks native closure, strict convexity, native angles, complete side use,
actual circular links, connectedness, exact placements, translational
holonomies, full integral lattice and area equality. Independent verification
requires no solver, primal, or producer import: the explicit native geometry
and12 side pairings suffice.

Every pair on this open curve has the periodic tiling proved above,
regardless of any separate monohedral obstruction. Consequently none can
meet the main target's condition excluding periodic tilings by the pair.
No assertion about a two-run survivor outside this exact curve follows.
The endpoint delta=0 has p=q, while delta=30 makes B's fifth turn0 and
its last corner180; both endpoints are outside the theorem.
