# A common period in every internally distinct all-obtuse pentagon–higher tiling

**Status:** adversarially reviewed VALID in the [fresh written-artifact audit](../reviews/distinct-length-obtuse-direct-common-period-review.md). This is a restricted-family result and does not resolve the
unrestricted two-convex-polygon problem. No literature priority is claimed.

## Theorem and hypotheses

Let P be a genuine compact convex pentagon and Q a genuine compact convex
n-gon, n>=7. Every interior angle is strictly between pi/2 and pi. Within
each polygon, all its native side lengths are pairwise distinct; numerical
values may coincide between P and Q. Then every admitted whole-plane tiling
by unrestricted isometric copies of P and Q has a nonzero translation period.
Rotations, reflections and unrestricted original contacts are included.

Only the reviewed [all-obtuse contact theorem](obtuse-edge-forcing.md) is
imported. No rational-angle hypothesis, good-limit extraction, corner-density
condition, finite graph enumeration or flat-torus classification is used.
The separately reviewed [higher-polygon theorem](distinct-length-obtuse-pentagon-higher.md)
further shows that a tileable pair has n=7 and admits a rank-two periodic
witness. The new assertion here concerns every original tiling, and only
asserts one nonzero period of that tiling.

## Full contacts and absence of monochromatic stars

Fix an admitted tiling T. The all-obtuse theorem makes every side contact a
whole native-side contact and every vertex a trivalent vertex with three
genuine corner sectors. In particular each side has exactly one side mate.

Give each actual numerical side length a symbol. The native symbols of P
form a simple five-cycle; those of Q form a simple n-cycle. At any tiling
vertex the three ray symbols are pairwise distinct: each pair bounds one
of its three polygon corners, whose adjacent native lengths are distinct.
If all three incident tiles were P, the three ray symbols and their three
corner adjacencies would form a triangle in the simple five-cycle. There is
no such triangle. The same argument in the n-cycle forbids QQQ. Therefore
PPP and QQQ stars never occur. This argument also excludes a tiling using
just one species.

## Every Q-to-Q seam is a same-index half-turn

An internally distinct Q length identifies one native side index uniquely.
Thus two Q copies meeting along a side match this same index. Write Q0 for
one copy and use its placed coordinates. An isometry taking Q0's specified
side to that side has, on the two segment endpoints, either the fixed or
the exchanged correspondence. The four possible segment-preserving
isometries are identity, reflection in the perpendicular bisector,
reflection in the supporting line, and the midpoint half-turn. The first
two preserve the supporting interior half-plane and would give positive
interior overlap along the side. Hence the only support-opposite choices
are reflection in the side line and the midpoint half-turn.

For the side-line reflection, each endpoint is fixed, so the two Q corners
at that endpoint are corresponding copies of the same native corner. The
two remaining outer rays there have equal lengths: both are the same
adjacent native Q side. The third tile is P because QQQ is impossible. Its
two adjacent whole native sides would therefore have equal lengths,
contrary to P's internally distinct lengths. The reflection branch is
excluded. Every Q-to-Q seam is consequently a midpoint half-turn. Reflected
placed copies are covered because the comparison uses an isometry of the
actual first placed polygon, with the unique native length fixing its side.

## Two private sides give a common period to all Q copies

At most five distinct Q length values occur on P. Hence Q has at least
n-5>=2 private length values, each occurring once on Q and absent from P.
Select any two of their fixed native side indices. Both sides of every Q
copy meet Q copies, by full-side matching. Let a,b be their midpoints in
one reference Q, and put d=b-a. The midpoints are distinct, so d!=0. The
open chord (a,b) lies in the strict interior of Q: distinct genuine sides
of a strictly convex polygon cannot have a boundary segment between their
relative interior points.

Form the graph whose vertices are Q occurrences and whose edges use just
these two selected private contacts. Every Q has degree two. Its two mates
are distinct: two different whole sides shared by the same two convex
polygons would put the positive-area convex hull of these sides in their
intersection. Across either selected contact, the midpoint half-turn
continues the chord as a straight interval. With H_a,H_b denoting the
half-turns, the chain contains

    Q, H_b(Q), Q+2d, H_b(Q)+2d, ...

and all backwards translates, since H_b composed with H_a is translation
by 2d. Each step continues an interval of length |d| with no reversal or
branch. These intervals cover an entire straight line; a finite cycle is
impossible because its lifted straight progression has positive length.
For a placed copy F(Q), the corresponding chain has period 2 L_F d, where
L_F is the orthogonal linear part of F. Every chain period has length
2|d|>0.

Different chain axes are disjoint. If one axis intersects the interior of
a chord of another chain, it puts an actual different Q tile or its side
inside a Q interior, producing positive-area interior overlap. At a chord
endpoint, the point is in the relative interior of a whole selected native
side, and the only two incident tiles are its two matched Q copies, which
are in the same chain. Thus different axes cannot intersect there either.
Disjoint entire plane lines are parallel. Their equal-length periods are
therefore the two signs of one fixed nonzero vector u. Both signs preserve
each chain. Every Q lies in one chain, so the entire set of actual Q
occurrences is invariant under u and -u. Additional Q-to-Q contacts do not
enter the selected graph and do not affect this conclusion.

## The prescribed adjacent Q data transfer the period to all P copies

At any P corner its two side neighbors cannot both be P, since PPP is
impossible. Consequently P-neighbor side slots are nonadjacent and number
at most two in its five-cycle. Every P thus has at least three Q side
neighbors. Any three slots in a five-cycle contain two consecutive slots.
Choose such a pair for a P occurrence P0, meeting at a corner v. Its two
Q neighbors determine the remaining P corner wedge and its two adjacent
whole side segments.

Translate those two Q copies and the prescribed data by u. They are actual
Q copies. They meet at v+u, and full contacts and trivalence provide an
actual third tile R occupying the translated residual wedge. If R were Q,
Q-set invariance under -u would produce an actual Q tile R-u with a positive
corner sector inside P0 at v. This contradicts disjoint interiors. Thus R
is P.

The ordered lengths of the two prescribed whole segments identify two
unique native sides of P, and their common native vertex is unique. Because
the lengths are distinct and the segments are noncollinear, the three
endpoints determine at most one placed copy of P, allowing both rotations
and reflections. The translated prescribed data therefore force R=P0+u.
This proves inclusion of every translated P in the actual P set. Apply the
same argument with -u to obtain its reverse inclusion. Both species, hence
the whole original tiling T, are invariant under the nonzero translation u.

## Dependencies, verification and scope

The argument is geometric and requires no bounded computation. A fresh
independent reviewer checked the star-cycle exclusion, both opposite-side
isometry branches, chain completeness and nonintersection, and the pullback
exclusion of a Q third tile. The written-artifact review is retained in
[the independent review](../reviews/distinct-length-obtuse-direct-common-period-review.md).

For n>=8 the earlier separately reviewed theorem says there is no admitted
tiling; the present implication is consistent and vacuous there. For n=7
it strengthens periodic-witness existence to a period in every admitted
original tiling. A second period of every original tiling is not asserted.
Repeated native lengths on either polygon, a nonobtuse angle and arbitrary
two-hexagon pairs remain outside this theorem. No global unrestricted
impossibility conclusion follows.
