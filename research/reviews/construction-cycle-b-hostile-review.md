# Track B fixed bevelled-chair scheme: independent hostile review

Date: 2026-10-13. Reviewer did not develop the scheme. Original unrestricted
problem and B5+1 pause remain unchanged. Domain: the SINGLE exact P/Q pair,
its seam and four specified scale-2 chair placements; no enumeration enlargement.

## Claims and assumptions reviewed

P=(S,(1/2,0),(2,0),(2,1),R), Q=(S,R,(1,2),(0,2),(0,1/2)),
S=(1/6,1/3), R=(1,1). The proposed parent C has boundary
((1/2,0),(2,0),(2,1),R,(1,2),(0,2),(0,1/2)). The proposals are
strict convexity, two distinct congruence classes, P/Q recomposition of C,
a four-child scale-2 chair extension, and intrinsic universal parent recognition.
No edge-to-edge or handedness restriction is imported into arbitrary tilings.

## Exact independently retained evidence

[Independent checker](check_construction_cycle_b_independent.py) imports no
construction-author code. [Retained output](construction-cycle-b-independent-check.json)
contains rational vertices, areas, periods and displacement bounds. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_construction_cycle_b_independent.py

The default is read-only; --output may target disposable evidence. Exact Fraction
arithmetic verifies strict positive turns, areas P=3/2 and Q=11/8, disjoint
interiors and total parent area 23/8. C is the L chair with triangle
conv((0,0),(1/2,0),(0,1/2)) removed. The seam S--R partitions C: below the
seam belongs to P, above to Q, with S on the bevel and R the unique reflex
vertex. Each pentagon lies in C, and the matching areas and opposite seam
orientations verify coverage. Unequal areas exclude congruence even with reflection.

For P, h(x,y)=(4-x,1-y) pairs the adjacent right-angle corners
(2,0),(2,1). The carrier is the strictly convex centrally symmetric hexagon
(R,S,(1/2,0),h(R),h(S),h((1/2,0))). For Q use h(x,y)=(1-x,4-y)
and carrier ((0,1/2),S,R,h((0,1/2)),h(S),h(R)). Exact clipping verifies that
each carrier contains the two half-turn-related pentagons, their interiors
are disjoint, and their total area equals the carrier area. The carrier
lattices have generators respectively

    P: (-1/2,-1), (17/6,-1/3), determinant 3;
    Q: (1,1/2), (5/6,19/6), determinant 11/4.

For each carrier, the checker computes exact lattice-coordinate vertex ranges.
A translated carrier can overlap only when both integer displacement coordinates
are inside these ranges. It checks the encompassing [-2,2]^2 domain except zero
(24 translations per carrier); every intersection has zero area. This proves
pairwise interior-disjointness for ALL lattice translates, not just the checked
window. Carrier area equals lattice covolume, so the periodic union covers the
plane. Explicitly, the lattice family is locally finite and its tiles are closed;
if its complement were nonempty, it would be open and have positive area in
some fundamental-domain translate, contradicting the area identity. Thus both
atomic species individually admit exact infinite periodic tilings.

The unbevelled placements are id+(0,0), id+(1,1), rot90+(4,0), rot270+(0,4).
The checker validates their 12 unit cells exactly against the scale-2 L chair.
For the bevelled children, w=(3/4,1/16) lies strictly in the identity child C:
0<x<2, 0<y<1, x+y>1/2. It lies outside 2C because x+y<1.
Therefore the union of the FOUR specified bevelled children protrudes from its
intended parent. Equal total area does not repair the failure. Other children
cannot remove a point already present in the identity child. No infinite covering
from this specific substitution is proved.

## Hostile findings and universal cases

The pair is tileable, with an exact infinite-covering proof given by either
monohedral lattice carrier above. The proposed chair substitution is invalid.
Universal parent recognition requiring P to pair with Q is invalid: a tiling
using only P or only Q is admitted. The counterexample uses half-turns and
translations, already a subset of the allowed isometries. Allowing reflections
and arbitrary partial contacts cannot remove it. Its two independent nonzero
periods also refute any claim excluding a single-direction period. There is no
translation-equivariant hierarchy with growing separated nonempty marker sets
on these periodic examples.

## Repairs, uncertainty and verdict

No repair was proposed; zero of the allowed one repair was spent. Altering the
bevel endpoint on the straight corner preserves the two consecutive right
angles and hence the monohedral escape; changing the substitution alone does
not address it. This does not exclude unrelated pentagon parent mechanisms.

VALID: exact convex distinct atomic polygons, exact parent recomposition,
exact infinite tileability, and BOTH periodic omission escapes.
INVALID: this scale-2 four-chair covering and the proposed universal mixed-parent
recognition/aperiodicity claim. No novelty claim, global impossibility result,
or unattended continuation is certified.

Next obligation: a different explicit parent scheme must remove the periodic
atomic carriers and prove exact child/parent compatibility before pursuing
intrinsic multilevel recognition, including reflected and partial-contact tilings.
