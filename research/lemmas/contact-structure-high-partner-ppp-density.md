# Higher all-obtuse partners force a positive density of pentagon-only vertices

Date: 2026-10-13. Status: independently hostile-reviewed VALID; [review](../reviews/contact-structure-high-partner-ppp-density-review.md).
Restricted structural theorem, not a resolution of the two-convex-tile target.

## Statement

Let P be a genuine compact convex pentagon and Q a genuine compact convex
n-gon, n>=7, with every angle of both shapes strictly between pi/2 and pi.
If they tile the plane, all tilings are edge-to-edge and trivalent by the
reviewed [obtuse forcing theorem](obtuse-edge-forcing.md). Count tiles by
centroid in any square of side 2R, writing p_R,q_R. Let u_R count geometric
vertices in that square whose three incident tiles all have type P. Then,
uniformly in square position and in the admitted tiling,

    6u_R >= 4p_R - n q_R - O(R),
    u_R >= ((n-8)/2) q_R - O(R).

The Q tiles are syndetic for every n>=7. For n>=9, the vertices of type
PPP have positive uniform lower quadratic count and are syndetic. In particular, if no multiset of three native P angles sums to 2pi,
there is no plane tiling by P and Q. This includes every P whose five angles
are strictly below 2pi/3, with any all-obtuse Q of at least nine sides,
regardless of lengths, reflections, or arbitrary contacts initially allowed.

## Proof

Whole-side trivalence follows from obtuse forcing. Around a P tile, label
its five side-neighbor positions P or Q. These are genuine geometric
neighbors; convexity prevents one neighbor from sharing two noncollinear
sides, although the following counting bound does not require that fact.
Let m be the number of Q positions and r the number of cyclic adjacent PP
pairs. Every such pair is precisely a PPP vertex at that P tile.

A Q position is incident to at most two edges of the five-cycle, so
r>=5-2m. If m<=2 this gives r>=3-m; if m>=3, r>=0>=3-m.
Consequently m>=3-r for every binary cyclic neighbor word.

Write u,x,y,z for counts of vertex species PPP,PPQ,PQQ,QQQ within the
square, and e for the number of P-Q side contacts counted once using the
midpoint of the contact as anchor. All displayed equations below have O(R)
errors. Tile diameters are uniformly bounded and minimum tile area is
positive, so only O(R) tiles meet any fixed-width boundary strip. Every
incidence discrepancy between these centroid, vertex and midpoint counts
belongs to that strip. The constants depend only on the two polygons.

Summing m>=3-r over P tiles gives

    e >= 3p - 3u - O(R).

Each mixed vertex has two incident P-Q side contacts, and each such contact
has two endpoints. Native corner counts therefore give

    e = x+y+O(R),
    5p = 3u+2x+y+O(R),
    nq = x+2y+3z+O(R).

The first two equations and the inequality imply y>=p-3u-O(R).
Eliminating x and using z>=0 yields

    nq = (5p-3u+3y)/2 + 3z + O(R)
       >= 4p-6u-O(R),

which proves the first inequality. The reviewed
[pentagon curvature identity](pentagon-curvature.md), with no subdivisions
or excess valence, gives p=(n-6)q+O(R). Substitution proves the second.
Area coverage and bounded areas give p+q=Theta(R^2); the fixed ratio therefore
gives q>=cR^2-O(R), uniformly. For n>=9 this forces u>=c_prime R^2-O(R).
Fix a sufficiently large radius once and for all so that the uniform lower
count is positive. Every square of that radius, hence every disk of a
sufficiently larger fixed radius, contains a Q centroid; for n>=9 it also
contains a PPP vertex. This proves the claimed syndeticity. If P has no
angle triple summing 2pi, then u=0, a contradiction.

## Counterexample attempts and exact scope

The argument is a hand proof over all 32 binary side-neighbor words. It uses
no solver, metric classification, orientation restriction, or frequency
existence. The bound m>=3-r is sharp for words with m=3,r=0 and m=2,r=1.
A PQQ vertex is allowed even when Q has no angle at most 2pi/3; it has not
been silently excluded. QQQ vertices contribute the explicitly nonnegative
term 3z. PPP vertices may use three different indexed corners of P or
repeat a native angle from different copies.

At n=8 the lower bound for u is zero and gives no obstruction. At n>=9
pentagons with a native triple summing 2pi remain outside the corollary;
positive PPP incidence alone does not prove existence or periodicity.
A nonobtuse corner on either shape invalidates the full-edge/trivalent
reduction, so arbitrary acute pentagon/high-partner tilings remain open.

The fixed regular 108-degree pentagon/nonagon exclusion is subsumed by this
corollary, since 3*108 != 360. Its Q signature need no longer be prescribed.
No novelty claim is made; current primary literature review is outstanding.
