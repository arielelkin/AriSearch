# Two prescribed pentagon words: dissect Ammann's hexagon

**Date:** 2026-10-11. **Status:** the requested varying-angle route is
excluded throughout this small family by exact necessary equations.
The [fresh independent audit](../reviews/boundary-attachment-ammann-h-gate-review.md)
passes all twelve exact gates, including the signed-area repair. This is a
concrete two-shape construction attempt, not a claim about all Penrose
recompositions. It was run after the root confirmed completion
of the earlier kite/dart and hexagon audits.

## Family and intended construction

Use the exact reconstructed Ammann shapes \(H(J),P_1(J),P_2(J)\), with
\(J=s+t\omega\), \(\omega=e^{i\pi/5}\), from
[the coordinate record](../lemmas/ammann-two-class-reconstruction.md).
The two final boundary words are prescribed in advance:
\[
P_1=[0,J',1,L,K],\qquad
P_2=[K,L,1+\omega^2,J_2,\omega^2].
\]
Do not change these shapes or add independent point coordinates. Seek a
partition of every \(H(J)\) into exactly two congruent copies chosen
from \(P_1(J),P_2(J)\), permitting every rotation and reflection.
A successful dissection would turn an existing Ammann tiling into a
tiling by just these two shapes. It would introduce attachments inside
old source boundaries while crossing the original rhomb boundaries
through the already recomposed polygons. The intended free parameter
is a curve of \(J\) values along which a normalized polygon angle varies;
cut-position freedom alone is not such a parameter.

This is not a claim that the intended curve exists. It is tested below
before any reconstruction argument. If the parent three-shape set is
strongly aperiodic at a parameter, its two-shape subset inherits the
no-periodicity property, but it still needs plane tilability. Existing
parent forcing hypotheses must be checked at that parameter; nothing in
this attempt assumes the forcing theorem for every \(J\).

## Completeness of the two-piece geometry gate

If a convex hexagon is partitioned into two convex polygons with disjoint
interiors, a separating line puts the two interiors on opposite sides.
Coverage forces the two polygons to be exactly the intersections of the
hexagon with these half-planes. Thus their common interface is a straight
hexagon chord. This covers any two-piece convex dissection, not merely
a particular choice of internal segment.

For both pieces to have five actual corners, both chord endpoints must
lie strictly inside opposite hexagon edges: three original hexagon corners
and two new endpoints belong to each piece. An endpoint at an old corner,
a flat degeneration of \(H\), or a flat degeneration of either prescribed
pentagon leaves a convex piece/member with at most four corners, which
has a monohedral periodic escape. Those cases fail the stated tiles-alone
gate and cannot supply a successful pair. We therefore test strict
hexagons and strict pentagons.

Each chord is one full side of both pentagons, so its length must appear
in both prescribed side cycles. Set
\[
a=|J-(1+\omega)|,\quad b=|J-1|,\quad
r=|J-\omega|,\quad c=|K-L|.
\]
The exact coordinate producer checks all side norms before forming ideals:
\[
H:(a,b,b,r,r,a),\quad P_1:(a,b,a,c,a),\quad P_2:(c,r,r,a,b).
\]
Consequently
\[
\operatorname{per}H=2a+2b+2r,\quad
\operatorname{per}P_1=3a+b+c,\quad
\operatorname{per}P_2=a+b+2r+c.
\]
The difference between the sum of piece perimeters and the outer perimeter
is twice the shared-side length. Together with area additivity this gives:

| Piece multiset | Area condition | Shared length | Necessary side equality |
|---|---|---|---|
| \(P_1+P_2\) | \(\lvert A_H\rvert=\lvert A_1\rvert+\lvert A_2\rvert\) | \(a+c\) | \(b=a+c\) |
| \(2P_1\) | \(\lvert A_H\rvert=2\lvert A_1\rvert\) | \(2a+c-r\) | equal to \(a,b,\text{or }c\) |
| \(2P_2\) | \(\lvert A_H\rvert=2\lvert A_2\rvert\) | \(r+c\) | equal to \(a\text{ or }b\) |

All side lengths are positive. In the mixed case the only possible shared
\(P_1\) side is \(b\), because \(a+c>a,c\). The producer additionally
retains the redundant original mixed control \(r=a+c\); an actual such match would also need \(r=b\).
The two same-shape rows give three and two perimeter cases. Each is
checked for both signs of the listed signed area, for ten necessary ideals.
Together with two original positive-orientation mixed controls, twelve
ideal rows are retained. The mixed case is excluded for every orientation
by the stronger absolute-area argument below. Side-length collisions
are allowed and none is omitted.

## Exact results

Work over \(F=\mathbb Q(\sqrt5)\) with the positive real embedding, and
use the polynomial ring \(F[s,t,a,b,r,c]\). Four equations set the squares
of \(a,b,r,c\) to their exact coordinate squared norms. Each case adds its
area and shared-length equation. No positivity, convexity or source
admissibility conditions are needed to obtain the negative result: the
algebraic set being tested is a superset of all genuine dissections.

With twice area divided by \(\operatorname{Im}\omega\), the exact area
identities are
\[
 A_H=2,\qquad A_1+A_2=1+\sqrt5.
\]
Here \(A_1,A_2\) are the listed **signed** areas; a physical copy has
area \(|A_i|\), permitting either cyclic orientation. Consequently
\[
 |A_1|+|A_2|\ge |A_1+A_2|=1+\sqrt5>2=|A_H|.
\]
Thus the mixed dissection is impossible at **every real** \(J\), regardless
of orientation, even before any cut geometry. The original two mixed
positive-orientation controls also have unit ideals.

All ten same-shape ideals, including both \(A_i=1\) and \(A_i=-1\),
are zero-dimensional. Retained exact Groebner
bases contain a pure-power leading monomial for each of the six variables,
which separately certifies the finite-dimensional quotient criterion.
Hence only finitely many complex \(J\) values can satisfy even these
necessary equations. Positive side lengths select only some of those
values and cannot create a continuous family. The prescribed final
shapes therefore cannot retain any varying angle parameter in this
entire two-piece family. Changing only a cut position at a fixed \(J\)
does not change either final shape.

No positive-dimensional candidate reached the periodic or reconstruction
gates. Isolated same-shape necessary specializations were not claimed to
be actual dissections and were not classified further, because they lie
outside the requested varying-angle route. The exact scope excludes
recomposing \(H\) with adjacent pentagons, cutting \(H\) into three or
more pieces, and changing the two prescribed final boundary words.

## Artifacts and restart

[Producer](boundary-attachment-ammann-h-gate.py) and
[certificate](../certificates/boundary-attachment-ammann-h-gate.json)
retain the coordinate-derived norm and area polynomials, twelve equation sets,
full exact Groebner bases, dimensions, pure-power controls, and script hash.
The twelve ideal computations took less than 0.1 seconds after Sage
startup. A fresh independent verifier separately reconstructed the complex-coordinate
side norms and areas and matched all twelve exact ideals and pure-power
controls. It also checked strict convexity and unequal exact normalized
angle values at two initial source parameters, confirming genuine angle
variation before imposing the dissection gate. See the
[review](../reviews/boundary-attachment-ammann-h-gate-review.md) and
[independent certificate](../certificates/boundary-attachment-ammann-h-gate-review.json).
This is an audited small necessary-domain exclusion, not a formal
verification of the computer algebra engine.

```sh
conda run --no-capture-output -n arisearch python research/searches/boundary-attachment-ammann-h-gate.py --output research/certificates/boundary-attachment-ammann-h-gate.json
```

The remaining construction gap is to specify different two final boundary
words with a real open convex parameter family and a varying normalized
angle. These exclusions motivate different final boundary words before enlarging
the interior-point alphabet. Any new
family still faces monohedral and mixed periodic escapes before new
source-recognition work.


## Fresh-review repair

The first seven-case record implicitly used positive listed signed areas
for same-shape pieces. A fresh reviewer identified that the intended
all-orientations geometry requires absolute areas. The repair preserves
the universal mixed-case exclusion using the triangle inequality above
and adds all five negative-area same-shape ideals. Both signs now have
zero-dimensional necessary loci. The producer does not infer positivity
from an unproved source-admissibility condition.
