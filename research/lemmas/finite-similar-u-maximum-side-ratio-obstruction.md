# Finite similar U pentagons: zero-core maximum-side propagation

Date:2026-10-13. Status: **independently adversarially reviewed VALID restricted extension;
[review](../reviews/resumed-similar-u-zero-core-review.md).** No enumeration, solver, parameter sweep or novelty claim.
No unrestricted resolution. The at-most-two-U case was already excluded by
[a reviewed arbitrary-metric theorem](../lemmas/pentagrid-two-asymmetric-u-obstruction.md);
it is not reopened here. The new domain is arbitrarily many FINITELY many
similar sizes of one fixed U metric.

## Exact objects and reviewed dependencies

A genuine convex U pentagon has vertex word(36,108,144,144,108) degrees.
Use lengths(A,B,b,c,d) with the acute corner between A and B, base c joining
the two144 corners, and b,d arms joining144 to108. Exact closure is

    A=phi*b+phi*c+d, B=b+phi*c+phi*d, phi=(1+sqrt5)/2.

Every short is less than BOTH own longs, A<phi*B and B<phi*A. Reflect the
reference metric to arrange b>d and hence A>B; the b=d mirror case is
already excluded for every finite collection by
[the reviewed native-measure/maximal-ray theorem](../lemmas/pentagrid-u-word-native-measure-and-maximal-ray.md).

Let the finite reference set comprise positive scalar multiples of this
fixed shape. All reflections, rotations, partial contacts and species
omission remain admitted. If it tiles, restrict to the sizes actually used
in its reviewed zero-score limit and normalize largest size to1.

## Potential and zero-core verification

Native weights w36=2,w108=1,w144=-2 have tile sum zero. At a vertex with
native corners, there is either no straight sector and native angle budget
10, or one straightpi sector and native budget5, in36-degree units.
Write counts n1,n3,n4. Weight=2s-5n3-10n4 when
n1+3n3+4n4=s. For s10, n4=0,1,2 gives n3<=3,2,0; for s5,
n4=0,1 gives n3<=1,0. Thus every star has nonnegative weight, and zero stars
are exactly full(108,108,144), full(36,36,144,144), half(36,144)+straightpi.
The reviewed unrestricted additive zero-score limit applies. The star list
is recovered by reclassifying the LIMIT's actual angle budgets, not by
assuming finite contact-language persistence under coalescence.

In this zero core, native108 cannot lie inside a side and cannot coincide
with native36. The reviewed maximum-ray argument excludes a globally
largest long side bordering native144 at its acute endpoint. This uses
only finiteness of sizes and the closure inequalities, not a two-type rule.

## New necessary similarity-ratio condition

Take a largest-size tile. Its A ray cannot border144; in either remaining
zero-star case (other native36 or straight sector) its shorter B ray borders
144. Call that neighbour R, of scale rho<=1.

An arm match requires its arm length to equal B, since a mismatch leaves
108 inside a native side. But an R long exceeds phi*B>A, contradiction.
A base equality rho*c=B has the same contradiction. Thus rho*c<B and
its far144 endpoint forces a new acute tile S with two long lengths

    rho*r, B-rho*c,

where r is the far arm of R. Endpoint equality follows from forbidden
interior108; it is not an imposed full-side rule.

If r=d, then B-rho*c >= rho*(B-c)>phi*rho*d, violating the strict ratio
bound between the two longs of S. Hence r=b and the near arm is d.
Moreover B-rho*c > rho*b, since B>b+c and rho<=1. Similarity fixes the
ratio of S's larger to smaller long to A/B. Therefore

    (B-rho*c)/(rho*b)=A/B,
    rho=B²/(Bc+Ab).                                (R)

This holds for EVERY largest-size tile's shorter acute144 contact.
In particular, if

    Ab+Bc < B²,                                    (E)

then rho>1 and no finite set of similar copies can tile the plane.
This is a uniform asymmetric metric exclusion without a finite-size bound.
Equality is not excluded by this calculation. If the metric passes (E)'s
complement, (R) is only necessary, not a construction.

## New exclusion of maximum acute-to-acute seams

Suppose the largest-size tile's A ray instead borders another native36
sector. The mate's shared long equals A: otherwise its108 endpoint lies
inside the other's side. Since every used scale is<=1 and B<A, the mate
also has scale1 and uses its A side. The star has adjacent36 sectors;
each remaining acute B ray borders144. By (R), both144 neighbours are
scale rho copies, with far arm b and near arm d.

The36/36 seam and opposite144/144 seam are collinear because36+144=180
on either side. Consequently the two near rho*d arms of those neighbours
coincide in full. Their far endpoints carry two108 sectors, requiring a
third144 tile K. Along both rays of that144 wedge lie A-long sides of the
rho neighbours, of length rho*A, starting at108 and ending at36.

At least one side of K incident with its144 corner is an arm, not the base.
That arm must have length AT LEAST rho*A: a shorter arm leaves its108
inside the rho*A side, forbidden in the zero core. A longer arm is not
excluded here (the other side's36 endpoint could form an allowed half-star),
but the lower bound alone suffices. Since b>d, K's scale is
therefore at least rho*A/b. Yet

    rho*A/b = A*B²/[b(Bc+Ab)] > 1.                  (I)

Indeed the strict inequality reduces to A*(B²-b²)>bBc.
Now B-b=phi*(c+d)>phi*c and A*phi>b, so

    A*(B-b)*(B+b)>A*phi*c*(B+b)>bBc.

Thus K would have scale exceeding the largest used scale1, contradiction.
All endpoint and cyclic-order arguments are unchanged by reflections.
This excludes a maximum long bordering native36 for ANY finite set of
similar copies, not just two sizes.

## Exact remaining configuration

Every largest-size tile in any hypothetical zero core must now have its
A ray start inside a straight host side, with its B ray bordering144.
The adjacent144 tile has the fixed lower scale rho from(R); if rho>1,
no such tiling exists at all. Metrics with rho<=1 still require analysis of
straight hosts, which may have different smaller similar sizes. The reviewed
at-most-two-type proof uses equal lower-type long multisets at precisely
that step; its reasoning cannot be reused for three or more sizes.

The needed next step is a NEW size/side invariant for straight-host contacts,
or an exact global tiling counterexample with a finite similar size set.
There is no finite-patch escalation or solver run, and no assertion that
these local necessities extend to the plane. The asymmetric finite-similar
case with rho<=1 remains unresolved.
