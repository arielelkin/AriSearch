# Adjacent-low octagon alpha-alpha length obstruction

Date: 2026-10-13. Status: **Adversarially reviewed VALID** for both the initial private-side theorem and the stronger necessary metric equality.
This is a restricted-family obstruction, not an unrestricted solution or a novelty claim.

## Exact theorem

Let P be any genuine compact convex pentagon whose five interior angles are
alpha=3pi/5. Let Q be any genuine compact convex octagon whose two alpha
corners are adjacent and whose other six corners have beta=4pi/5.
Let e be the native Q side joining its two alpha corners. Suppose its length
occurs on no P side and occurs on no other Q side. Then the pair cannot tile
the plane, even allowing all isometries, arbitrary contacts, and omission.
No restrictions apply to the other native lengths: repeated lengths,
nonregular P, and reflected Q copies are included.

## Complete proof

The reviewed [all-obtuse forcing theorem](../lemmas/obtuse-edge-forcing.md)
forces any hypothesized admitted tiling to be edge-to-edge and trivalent.
Every vertex has exactly two alpha sectors and one beta sector, since the
only three-term sum from {108,144} equal to360 is108+108+144.

For each placed Q, the side e has a unique whole-side neighbour. Its length
cannot match P or another native Q side, so that neighbour is a Q using its
own e side. At either endpoint both these Q copies contribute alpha. The
remaining beta sector must therefore come from a third Q (P has no beta).
At each endpoint the initial Q has an additional Q neighbour across the
other incident native side. These two sides and e are three different
native sides. Their neighbours are distinct: two convex interior-disjoint
polygons sharing two different genuine native sides would have the
positive-area convex hull of these noncollinear segments in their
intersection. Thus every Q has at least three Q side neighbours, and at
most five P side neighbours. This inference does not assume half-turn
matching, chirality, orientation or uniqueness of the geometric placed Q:
both possible endpoint correspondences on e give two alpha sectors.

At a P corner its two side neighbours cannot both be P, since three alpha
sectors have sum324 rather than360. Consequently the P neighbour positions
in its native five-cycle form an independent set of size at most two.
Every P has at least three Q side neighbours.

Count anchors of tiles in a square of side2R, with N_P,N_Q the counts.
Bounded tile diameters and disjoint positive-radius inscribed disks give
O(R) boundary tiles; each contributes only boundedly many sides/corners.
Whole-side double counting therefore gives

    3N_P <= 5N_Q + O(R).                         (1)

Native corner counting, using two alpha sectors per beta sector at every
complete star, gives

    5N_P + 2N_Q = 2*(6N_Q) + O(R),
    N_P = 2N_Q + O(R).                          (2)

Thus6N_Q <=5N_Q+O(R), so N_Q=O(R), then N_P=O(R).
Plane coverage by bounded-area tiles instead requires
N_P+N_Q=Omega(R^2), contradiction. All constants depend only on the two
fixed shapes. This treats omitted and arbitrarily sparse species directly.

## Exact nonempty metric domain

The hypotheses are geometrically realizable. Let z=exp(pi*i/5), specified
as the algebraic root of z^10=1 with argument pi/5 (equivalently positive
real/imaginary parts and Re(z)=(1+sqrt(5))/4). Regard complex numbers as
Euclidean coordinate pairs. Define Q as the intersection of the eight
closed halfplanes

    Re(conjugate(z^k)*x) <= 1,
    k in (0,2,4,5,6,7,8,9).

Every bounding line touches the unit circle, and cyclic gaps of its outward
normals are72,72,36,36,36,36,36,36 degrees. Its corners therefore have the
stated cyclic angle word108,108,144,144,144,144,144,144, up to indexing.
Each consecutive-normal gap is below180, so all eight support lines give
positive genuine sides and the halfplane intersection is a bounded strictly
convex polygon. Its vertices are intersections of successive support lines;
this is a finite exact coordinate definition.

Put t=tan(pi/5), u=tan(pi/10). The side with normal z^2 joins the two108
corners and has length2t. The two neighbouring sides have length t+u,
and the other five sides length2u. Since0<u<t, the length2t is unique.
Choose P to be the regular pentagon of side length2u. A finite coordinate
definition is P=conv{r*w^j: j=0,...,4}, where w=z^2 and
r=u/sin(pi/5). It has all angles108 and none of its lengths equals2t. It shares the five beta/beta sides of Q, so omission of all mixed full contacts is not the obstruction.
The exact algebraic trig values are defined through z (tan and sin are
Im(z)/Re(z), Im(z)). Thus no unspecified numerical value is used.

Q has repeated lengths (multiplicities2 and5), so this exact fixture lies
outside the internally-distinct-length theorem. Its adjacent alpha corners
lie outside the nonadjacent-alpha octagon chain and private-side periodicity
theorems. The present result kills the entire stated private-alpha-alpha
metric domain, not just this fixture.

## Dependencies, computation and independent review

Only all-obtuse contact forcing, elementary convexity and finite-window
counting are imported. No finite search, solver verdict, numerical geometry,
monohedral classification or infinite extension claim is used. The initial theorem has [independent VALID review](../reviews/resumed-higher-partner-hostile-review.md). The stronger theorem has a [separate independent VALID review](../reviews/resumed-adjacent-octagon-beta-beta-review.md). These reviews check reflections, forced third-Q sectors, native endpoint neighbours, distinct-neighbour convexity and uniform boundary errors. The [independent exact support-line fixture checker](../reviews/resumed-higher-partner-fixture-check.py) verifies Q and the regular P of side2u, matching the illustrative fixture above. It checks the five shared beta/beta side lengths and that P cannot match the alpha/alpha side of length2t. The theorem proof is metric-independent outside its stated equality hypotheses.

The initial private-side statement alone does not cover e shared by P or another Q side. The independently reviewed stronger theorem below covers these cases whenever no beta/beta Q side shares the length. Actual equality with a beta/beta side remains the unresolved boundary. No full adjacent-alpha classification or aperiodicity result follows.

## Stronger necessary metric escape (independently reviewed VALID)

The uniqueness and P-private hypotheses on e can be replaced by the single
condition that its length differs from EVERY Q beta/beta-side length.
It may recur on Q alpha/beta sides or be shared by P. Under this weaker
condition the pair is still untileable.

Here is a complete additional proof. In every hypothetical tiling each
Q has at least two Q side neighbours. If e meets P, at its two alpha
endpoints the other neighbour is Q contributing beta, so both other
incident Q sides are QQ. If e meets Q on an alpha/alpha side, both endpoints
are QQQ and Q has at least three QQ sides. If e meets Q on an alpha/beta
side, its endpoint paired alpha-to-alpha is QQQ, forcing one additional
QQ side beside e. The excluded beta/beta mate is the only remaining case.
Define d_P=number of PQ sides minus3 and d_Q=number of QQ sides minus2;
both are nonnegative. The same corner and side counts as above give

    sum_P d_P + sum_Q d_Q = O(R).

Call a tile bad if its appropriate deficit is positive. Every Q lies
within uniformly bounded distance of a bad tile, as follows. If e meets P,
that P has Q neighbours along e and both adjacent sides. Its remaining
possible P-neighbour slots are adjacent, so at most one is P; it has at
least four Q neighbours and is bad. If e meets alpha/alpha Q, the initial
Q is bad. If e meets alpha/beta Q, the resulting QQQ endpoint has a third
Q supplying beta. That beta-sector Q has QQ neighbours on both sides
incident with its beta corner. Every alpha corner of Q requires an
incident QQ side (the beta sector at its star is necessarily Q).
The two sides incident with a beta corner cannot cover both adjacent
alpha corners: for an eight-cycle with exactly two adjacent alpha slots,
a beta vertex is adjacent to at most one of them. Thus at least one
additional QQ side exists on this beta-sector Q, making it bad.

The distance association from each Q to a bad tile has uniformly bounded
multiplicity by fixed inradius packing. Hence N_Q <= C*N_bad+O(R)=O(R),
then N_P=2N_Q+O(R), contradiction. This is a pointwise assignment plus
finite-window accounting, not an assumed invariant measure or good limit.
The exact tangential fixture satisfies this stronger hypothesis since its
e length is2t and all beta/beta lengths are2u<t+t.

Therefore any actually tileable adjacent-alpha108/144 pentagon/octagon pair
MUST equate the alpha/alpha length to a beta/beta Q length. This is only a
necessary condition; it gives no realization or two-tile forcing mechanism.
