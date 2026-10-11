# Equilateral rational-angle pentagon pairs: a restricted obstruction

**Status:** adversarially reviewed, using the explicitly imported Lam--Leung
root-of-unity theorems below; [independent hostile review](../reviews/new-angle-equilateral-rational-review.md) found no unresolved defect.
This excludes a construction family, not the unrestricted problem.

## Theorem

Let `A,B` be genuine compact convex polygons. Suppose each polygon is
equilateral (the common side length may differ between `A` and `B`),
every interior angle is a rational multiple of pi, one polygon is a
pentagon, and the other is a pentagon or a hexagon. Then the pair either
admits no plane tiling or admits a doubly periodic plane tiling.
Reflections and partial-side contacts are allowed throughout.

This theorem does **not** cover unequal side lengths, irrational angles,
or a pentagon paired with a polygon having more than six sides. It uses
no completeness claim about the fifteen pentagon tiling families and no
monohedral hexagon classification.

## Imported arithmetic, with primary source checked

T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*,
Journal of Algebra 224 (2000), 91--109;
[primary preprint](https://arxiv.org/pdf/math/9511209),
Theorems 3.3, 4.8, and 6.5 (PDF pages 7, 11, 15).

Here a vanishing sum has nonnegative integral coefficients; weight counts
all terms, and minimal means no nonempty proper vanishing subsum.
A symmetric minimal sum is a rotated complete prime-root orbit.
Theorem 3.3 makes every minimal sum symmetric when the order has at most
two prime divisors. Theorem 4.8 bounds an asymmetric minimal weight below
by `(p1-1)(p2-1)+(p3-1)`, where `p1<p2<p3` are the smallest distinct
prime divisors. Theorem 6.5 identifies the equality case as a rotated sum
of products of the nonidentity `p1` and `p2` roots, together with the
nonidentity `p3` roots. These statements concern positive sums, rather
than arbitrary signed linear combinations.

Consequently the minimal positive sums of weight at most six are complete
prime-root orbits of sizes 2, 3, 5, and one asymmetric size-six sum.
Indeed an asymmetric sum has weight at least six, and equality forces
`(p1,p2,p3)=(2,3,5)`. Its terms, up to rotation, are

    exp(i*pi/3), exp(-i*pi/3), zeta5, zeta5^2, zeta5^3, zeta5^4.

A nonminimal sum splits into minimal subsums, none of weight one. Thus a
weight-five sum is either the regular five-root orbit or a triangle orbit
plus an antipodal pair. A weight-six sum is three antipodal pairs, two
triangle orbits, or the displayed exceptional minimal sum. This argument
permits arbitrary root orders and does not impose a computational cutoff.

## From arithmetic to polygon geometry

Scale each equilateral polygon to unit side length and rotate one edge to
direction zero. Rational interior angles make every directed edge a root
of unity. Polygon closure gives a positive vanishing sum with five or six
terms. Strict convexity orders the edge directions cyclically, with all
successive turns in `(0,pi)`. Repeated edge directions cannot occur.
Hence the arithmetic classification determines the polygon geometry after
cyclically sorting the roots; it is not merely a classification of a
different order of the same edge vectors.

### Nonregular pentagons have an explicit periodic tiling

For a triangle orbit and an antipodal pair, rotate the triangle directions
to `0,120,240` degrees. Swapping the pair and rotating the triangle by
120 degrees normalizes its direction parameter to `0<=theta<60`.
`theta=0` gives a duplicate direction, so a genuine pentagon has
`0<theta<60`. The sorted edge directions are

    0, theta, 120, 180+theta, 240.

Its corner angles, starting at the initial vertex, are

    60, 180-theta, 60+theta, 120-theta, 120+theta.

The endpoints of side 2, whose direction is 120 degrees, have angles
`60+theta` and `120-theta`; their sum is 180 degrees. Glue a half-turned
copy along this side, with the half-turn centered at the side midpoint.
The copies have disjoint interiors because they lie in opposite closed
half-planes. At both endpoints the combined boundary is straight. All
other boundary corners remain strictly convex. The union is therefore a
convex centrally symmetric hexagon, with exactly six genuine sides.
The following elementary hexagon lemma tiles the plane by its translates.
Keeping the two pentagons inside every translated hexagon gives a doubly
periodic monohedral pentagon tiling. Every allowed scale has the same
construction.

### Centrally symmetric hexagons tile by translations

Write the ordered side vectors as `a,b,c,-a,-b,-c`, with `a,b,c`
ordered in an open half-plane, and let `u=a+b`, `v=b+c`.
Their determinant is positive. In this basis write
`a=alpha*u+beta*v`. Positive cross products give

    0 < -beta < alpha < 1.

The six vertices in `(u,v)` coordinates are

    (0,0), (alpha,beta), (1,0),
    (alpha,1+beta), (0,1), (alpha-1,1+beta).

Cut off its portion below the unit square: the triangle with vertices
`(0,0),(alpha,beta),(1,0)`, and translate that triangle by `(0,1)`.
Cut off its portion to the left: the triangle with vertices
`(0,0),(alpha-1,1+beta),(0,1)`, and translate it by `(1,0)`.
The two translated triangles, together with the part remaining inside
the square, partition `[0,1]^2` with disjoint interiors. Thus the hexagon
is a fundamental domain for `Z*u+Z*v`, including its boundary. Its
lattice translates tile the plane. The same proof works with arbitrary
positive opposite side lengths.

A hexagon whose root sum is three antipodal pairs has exactly this central
symmetry and therefore supplies a periodic monohedral escape.

## The remaining regular-pentagon cases

If either pentagon is nonregular, its monohedral periodic tiling already
settles the theorem. Thus assume every pentagon present is regular, with
interior angle 108 degrees. A pair of regular pentagons, even at different
scales, cannot tile: a genuine tile corner would require a nonempty sum
of 108-degree sectors equal to 180 or 360 degrees, and neither is possible.

For clarity about unrestricted contacts: at a tile vertex in a locally
finite convex tiling, either every incident tile supplies a genuine
corner, and their angles sum to 360 degrees, or one incident tile
supplies a straight sector and the other genuine corner angles sum to
180 degrees. Two straight sectors would already fill the whole disk,
leaving no genuine corner. This local dichotomy follows from convexity
and local finiteness and does not assume edge-to-edge contact.

### Two triangle orbits in the hexagon

Rotate the first triangle orbit to directions `0,120,240`. Normalize
the other by rotation and reflection so `0<theta<=60`. The six directions
are `0,theta,120,120+theta,240,240+theta`. The hexagon has three
corners of each angle

    L = 180-theta, S = 60+theta.

At `theta=60` it is regular and has its usual periodic tiling. We show
that no tiling using this hexagon is possible at any other parameter,
even with the regular pentagon present and at a different side scale.

For `0<theta<30`, `L>150` and `60<S<90`. A 180-degree corner sum
cannot contain L. In a 360-degree sum containing L, the number n of
L corners is one or two. If n=1, there can be at most three S corners.
For m=0,1,2,3 S corners and k pentagon corners, the equation is

    (m-1)*theta = 180-60*m-108*k.

For m=0 its possible positive roots start at 36; m=1 has no integral k;
m=2 gives 60 or a nonpositive value; m=3 gives a nonpositive value.
For n=2, an S corner would already make the sum greater than 390.
Without S, the equation is `theta=54*k`; no value lies in `(0,30)`.
Thus an L corner cannot occur anywhere in a plane tiling.

At `theta=30`, the available angles are 150, 90, 108. The equation for
a full-angle sum containing a 150-degree corner is
`150*n+90*m+108*k=360`, with n=1 or 2. Modulo 18 it gives
`6*n=0`, which is impossible for n=1 or 2. A half-plane sum containing
150 is also impossible since all other corners exceed 30 degrees.

For `30<theta<60`, every angle exceeds 90 degrees. Hence no genuine
corner lies on a straight side, and every vertex has exactly three
corner sectors. A sum containing an S corner can have three hexagon
corners, which sums to 360 only at theta=60, or two pentagon corners,
which requires theta=84, or one pentagon corner. In the latter case
`108+2*S=360` requires theta=66, while `108+S+L=348`.
None applies in `(30,60)`. Thus an S corner cannot occur anywhere.

### The exceptional six-root hexagon

Sorting its six directions yields

    60,72,144,216,288,300 degrees,

and corner angles `60,168,108,108,108,168`. A 168-degree corner
cannot occur in a 180-degree sum, as every other available corner is
at least 60 degrees. In a 360-degree sum it occurs at most twice.
For one occurrence, `108*k+60*m=192`; after division by 12 this
is `9*k+5*m=16`, with no nonnegative integer solution. For two
occurrences the remainder is 24, smaller than every available corner.
Thus these exact convex shapes admit no plane tiling.

The possible periodic escapes and untileability cases exhaust all
arithmetic polygon classes, proving the theorem.

## Exact check, assumption ledger, and restart state

The replayable finite angular checks and the exceptional closure identity
are in `research/searches/new-angle-equilateral-rational-verify.py`;
its retained output is
`research/certificates/new-angle-equilateral-rational-certificate.json`.
Replay from the repository root:

    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-equilateral-rational-verify.py

The script proves only its explicitly bounded angle equations and closure
identity. The unrestricted root-order classification comes from the
primary theorems above; the global periodic construction is the cut-and-
translate and half-turn proof, not a finite patch inference.

Assumptions: convex polygons and arbitrary isometries/contacts are from
the problem; equilateral sides and rational angles are this route restriction;
the small-weight classification is imported and explicitly checked; all
periodic tilings and local impossibility steps are derived above.

This new route is closed within its stated family. Reopening requires
unequal side lengths or nonrational angles (or a higher-sided partner);
merely changing the rational denominator or the two side scales cannot
rescue it. No main-problem resolution or novelty claim follows.
