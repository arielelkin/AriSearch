# The 108/144 pentagon–nonagon signature is untileable

**Status:** adversarially reviewed; [fresh hostile review](../reviews/obtuse-pentagon-nonagon-neighbour-review.md) valid.
This is a restricted impossibility theorem, not a resolution of the full target.

## Theorem

Let P be any genuine compact convex pentagon with five interior angles 3pi/5.
Let Q be any genuine compact convex nonagon with one interior angle 3pi/5
and eight angles 4pi/5. Then {P,Q} admits no tiling of the Euclidean plane.
Lengths are arbitrary. Reflections, rotations, partial contacts and omission
of either type are permitted in the initial definition.

## Forced local geometry

By the independently reviewed [all-obtuse forcing theorem](obtuse-edge-forcing.md),
every admitted tiling is edge-to-edge, with three genuine sectors at every
vertex. The only permitted angle triple is (3pi/5,3pi/5,4pi/5).
Indeed p*(3pi/5)+(3-p)*(4pi/5)=2pi implies p=2.
Consequently each vertex contains exactly one Q-tile contributing a 4pi/5
corner, and two tiles contributing 3pi/5 corners.

Distinct genuine sides of a given tile have distinct neighbours. If the
same convex neighbour shared two noncollinear whole sides, the convex
intersection of the two tiles would contain their two segments and therefore
have positive area, contradicting disjoint interiors. Genuine convexity
excludes adjacent collinear sides. This observation suffices locally and no
combinatorial simplicity beyond the actual geometric tiling is imposed.

At a P-corner, the two neighbours along the incident sides cannot both be
P: that would produce three 3pi/5 corners, of sum9pi/5. Thus the P-neighbour
positions around the five sides of any P-tile form an independent set in a
five-cycle, with at most two positions. Every P-tile has at least three
whole sides whose neighbour has type Q.

At the unique 3pi/5 corner of any Q-tile, at least one of its two side
neighbours must be a Q-tile: one of the other two sectors must have angle
4pi/5, unavailable in P. Hence every Q-tile has at least one whole side
whose neighbour has type Q, and at most eight sides whose neighbour is P.

## Global contradiction, including rare or omitted types

Choose a square W_R of side2R and count selected tiles whose centres lie in
W_R, writing N_P,N_Q and N=N_P+N_Q. Any fixed centre rule inside the tile
works, for example the area centroid. Positive minimum area and bounded tile
diameter give N=Theta(R^2), and tiles meeting a fixed-width boundary strip
number O(R). Every discrepancy between counts of a matched P-to-Q side on
its two sides comes from such a boundary tile. Therefore the preceding
local neighbour bounds imply

    3N_P <= 8N_Q + O(R).                                  (1)

Counting native alpha=3pi/5 and beta=4pi/5 sectors in complete interior stars
likewise has only O(R) boundary error. There are five alpha sectors per P,
one alpha and eight beta sectors per Q, and exactly two alpha per beta
in each full star. Thus

    5N_P + N_Q = 16N_Q + O(R),
    N_P = 3N_Q + O(R).                                    (2)

Combining (1) and (2) yields9N_Q <=8N_Q+O(R), hence N_Q=O(R),
and then N_P=O(R). This contradicts N=Theta(R^2).

The same contradiction covers a tiling with one type omitted or with a
hypothetically sparse type. No positive-density assumption was inserted.
No edge lengths, congruence restrictions or chosen orientation were used.

## Dependencies and scope

Only all-obtuse full-edge/trivalent forcing and elementary bounded-diameter
boundary-strip counting are used. The boundary argument is independent of
monohedral polygon classification and a periodic-limit theorem. No search
or floating-point computation is involved.

This removes n=9 from the 108/144 row of the earlier
[two-obtuse-angle reduction](two-obtuse-angle-pentagon-reduction.md).
The n=7 and n=8 metric families, and the 4pi/7–5pi/7 pentagon–heptagon
signature, are not excluded by this argument. The key inequality for n=8
would be6N_Q <=7N_Q+O(R), so the same proof cannot establish its impossibility.
