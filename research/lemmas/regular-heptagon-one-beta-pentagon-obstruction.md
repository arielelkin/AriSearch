# A regular heptagon cannot partner the four-alpha/one-beta pentagon

**Status:** adversarially reviewed; [fresh independent analytic review](../reviews/regular-heptagon-one-beta-pentagon-review.md) is valid.
This is a restricted untileability theorem. No computation, monohedral
classification, density limit, or finite-patch extension is used.

## Theorem

Let Q be the regular unit-side heptagon, with angle beta=5pi/7. Let P be
any genuine compact convex pentagon with four angles alpha=4pi/7 and
one angle beta. Then {P,Q} admits no tiling under the
[unrestricted problem definition](../../research-problem.md). Side lengths
of P are arbitrary positive reals, reflections and all rotations are
permitted, and either type may initially be omitted.

The reviewed [all-obtuse forcing theorem](obtuse-edge-forcing.md) is the
sole imported geometric result. Both alpha and beta are strictly between
pi/2 and pi, so every admitted tiling would have complete native-side
contacts and three genuine corners at every vertex. The only allowed
three-corner sum is

    alpha+2beta=2pi.

In pi/7 units the other triples have sums12,13,15 rather than14.
Thus every vertex has exactly one alpha sector and two beta sectors.

## P-to-P sides and the unique beta corner

A P side has endpoint angles alpha/alpha or alpha/beta, because P has
only one beta corner. Consider any P-to-P whole-side contact. If either
copy supplies an alpha/alpha side, the other copy necessarily supplies
alpha at at least one matching endpoint. That endpoint would have two
alpha sectors, forbidden by the star language. Hence both copies must
supply alpha/beta sides.

The endpoint correspondence must reverse alpha and beta. Matching beta
to beta at one end would simultaneously match alpha to alpha at the other.
Thus every P-to-P side is incident to the unique beta corner on each copy,
with an alpha sector contributed by its neighbor at that beta endpoint.
No side-length assumption has entered this conclusion.

At P's beta corner, its two side neighbors cannot both be Q, because
three beta sectors do not sum to2pi. They cannot both be P, because their
P-to-P endpoint correspondence would contribute two alpha sectors. Exactly
one neighbor is therefore P and the other Q. This gives exactly one
P-to-P side on each P. Every other P side has a Q neighbor. Since all Q
sides have length1 and the contacts are complete, these four P-to-Q sides
all have length1.

There is at least one P in a hypothetical tiling: a Q-only tiling would
have no alpha sector at any vertex. A P-only tiling is also impossible by
the beta-corner argument. Therefore omission of either type supplies no
exception. We may choose any P copy and apply the preceding conclusion.

## Exact closure contradiction

Label P's beta vertex0, followed counterclockwise by its four alpha
vertices. Its consecutive directed side angles, after rotating side0
onto the positive real axis, are

    0, 3pi/7, 6pi/7, 9pi/7, 12pi/7.

These follow from the four alpha exterior turns pi-alpha=3pi/7 and the
closing beta exterior turn pi-beta=2pi/7. The unique P-to-P side is
incident to vertex0, so it is side0 or side4. Reflection exchanges these
two cases while preserving the angle word. It is enough to treat side0.
Let its arbitrary positive length be L. The other four lengths are1.
Polygon closure would require

    L+sum_(j=1)^4 exp(3j*pi*i/7)=0.

Its imaginary part is independent of L. For a general real t with
sin(t/2)!=0, telescoping gives

    2sin(t/2)*sum_(j=1)^4 sin(jt)
        = cos(t/2)-cos(9t/2)
        = 2sin(5t/2)*sin(2t).

With t=3pi/7, this yields the exact nonzero value

    sum_(j=1)^4 sin(3j*pi/7)
       = sin(6pi/7)*sin(15pi/14)/sin(3pi/14)
       = -sin(pi/7)*sin(pi/14)/sin(3pi/14) < 0.

All three sine factors in the last fraction are strictly positive.
Therefore no value of L can close the five directed sides. This contradicts
the existence of P in the tiling and proves the theorem. The reflected
side4 case has the same contradiction with the reversed sign convention.

## Regular-polygon corollary

More generally, let Q be a regular n-gon with n>=7 and angle
beta=(n-2)pi/n. Let P have four identical angles alpha and one beta.
The pentagon angle sum forces

    alpha=(n+1)pi/(2n).

Then {P,Q} is untileable. For n=7 this is the theorem above. For n>=8
all corners are obtuse, so a vertex would have exactly three sectors.
If p of them are alpha, its angle equation is

    p*(n-5)=2*(n-6),
    p=2-2/(n-5).

For n>=8 this value lies strictly between1 and2 and hence is not an integer.
No vertex star exists, independently of side lengths. Scaling Q's common
side length changes none of these conclusions.

For completeness, the same four-alpha/one-beta family never gives an
aperiodic pair with any regular n-gon: n=3,4,6 admit the standard periodic
monohedral tiling by Q alone, while n=5 makes every corner108 degrees and
has no native full or half star. The heptagon theorem supplies the only
nontrivial metric exclusion after this angular filtering.

## Scope and dependencies

The regularity of Q is used in the heptagon proof only to make its seven
sides equal. A convex heptagon with seven beta angles and varying side
lengths is outside that metric step; the earlier exact periodic
[pentagon/heptagon witness](../counterexamples/two-angle-5-7-periodic-instance.md)
has such unequal lengths and is consistent with this obstruction.

The argument does not classify arbitrary pentagon/heptagon pairs, does not
produce an aperiodic pair, and makes no novelty claim. Only the previously
reviewed full-edge/trivalent forcing theorem is imported; every remaining
local contact argument and the closure identity are proved explicitly above.
No code or finite certificate is necessary for this analytic obstruction.
