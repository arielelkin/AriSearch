# Two equilateral rational-angle hexagons: exact periodic escape classification

**Status:** adversarially reviewed; [independent root hostile review](../reviews/new-angle-two-equilateral-hexagons-review.md) valid.
The exact symbolic and endpoint checks pass. This is a restricted two-hexagon
result, not the unrestricted problem.

## Theorem and complete alternatives

Let A and B be genuine compact convex hexagons. Assume each is equilateral
(with possibly different common side lengths) and every interior angle is a
rational multiple of pi. Reflections, partial contacts, and omission of one
type are allowed. Then the pair either admits no plane tiling or admits a
doubly periodic plane tiling.

More precisely, use the geometric classes below. If either member is centrally
symmetric, it supplies a periodic monohedral tiling. If neither is central,
the only tileable case is two triangle-orbit hexagons of the same side length,
with normalized parameters a,b in (0,60) degrees satisfying b=2a or a=2b.
That case has a three-face flat-torus construction. Every remaining case is
untileable. In particular, this includes the acute-angle range of the larger
parameter, not just the all-obtuse subcase.

The rational-angle restriction is used in the arithmetic classification.
No assertion about arbitrary equilateral hexagons with irrational angles is
made. The explicitly given two-triangle construction itself works for every
real a in (0,30).

## Established dependencies

1. The positive weight-six root-of-unity classification and its passage to
   cyclic convex edge order are proved, with checked primary imports, in
   [the equilateral rational-angle obstruction](new-angle-equilateral-rational-obstruction.md).
   Its arithmetic source is T. Y. Lam and K. H. Leung, *On vanishing sums of
   roots of unity*, [primary preprint](https://arxiv.org/pdf/math/9511209),
   Theorems 3.3, 4.8, 6.5. The imported statements concern nonnegative sums,
   arbitrary root orders, minimal subsums, and the unique asymmetric weight-six
   equality case. Their already reviewed use is unchanged here.
2. The defect-free-limit theorem in
   [hexagon limits](hexagon-limit-and-periodicity.md) has been independently
   re-reviewed after its vertex-separation repair: any tiling by two fixed
   genuine convex hexagons has an admitted edge-to-edge tiling with exactly
   three native corners at every vertex. Either type may disappear.
   Only this theorem is used from that file, not its monohedral classification
   or honeycomb-combinatorics claims.
3. A centrally symmetric genuine convex hexagon tiles by its translations;
   the elementary cut-and-translate proof is in the first dependency.

The source tiling can be completely non-edge-to-edge. All deductions about
three-corner sums apply to the admitted limit, rather than assuming such
contacts in the given tiling.

## The three geometric classes

Scale a member to unit side length and rotate one edge to direction zero.
Its rational angles make its six directed sides roots of unity whose positive
sum vanishes. The checked weight-six classification has exactly three forms.

* Three antipodal pairs. Their cyclic convex ordering gives opposite side
  vectors e0,e1,e2,-e0,-e1,-e2. The hexagon is central.
* Two triangle orbits. After rotation and reflection their cyclic edge
  directions are 0,theta,120,120+theta,240,240+theta, with 0<theta<=60.
  Theta=0 would repeat an edge direction, so is excluded by genuine convexity.
  Theta=60 is the regular central hexagon. Put a=60-theta for the remaining
  class H(a), where 0<a<60. Its angles alternate 120-a and 120+a, three of
  each. Unit edge lengths together with this cyclic angle order determine
  its congruence class; closure already follows from the two triangle orbits.
* The exceptional minimal six-root sum. Its sorted edge directions are
  60,72,144,216,288,300 degrees. Call the resulting hexagon S. In cyclic order
  its corners are 60,168,108,108,108,168. There are one 60, three 108 and two
  168 corners per copy.

No other arithmetic class or cyclic geometry remains. Central members settle
our target immediately, since the other member may be omitted. Henceforth
both members are noncentral, thus of type H(a) or S.

## Preliminary exclusions and scale

A monohedral edge-to-edge trivalent H(a) tiling is impossible for a>0. Any
three corners sum to 360 plus an odd nonzero multiple of a, because their
three deviations are each +a or -a. A monohedral trivalent S tiling is also
impossible: no three of its available angles 60,108,168 sum to 360.
In particular, a 168 corner cannot occur in such a tiling.

If the two members have different common side lengths, the defect-free limit
has no mixed-type full-edge contact. Its face adjacency graph is connected:
a path between tile interiors, perturbed away from the locally finite vertex
set, crosses full edges and yields a chain of adjacent faces. Hence every
face has the same type. This contradicts the preceding monohedral exclusions.
Thus no noncentral pair with unequal side scales tiles.

For equal side scales, set that common length to one. The only remaining
pair classes are H(a),H(b), H(a),S, and S,S.

## Two triangle-orbit classes force ratio two

At a trivalent vertex the three base angles 120 already sum to 360, so its
three deviations must sum to zero. Three corners of one type cannot do this.
For two H(a) corners and one H(b) corner, the a-deviation sum is -2a,0,or2a,
and the remaining deviation is -b or b. Positive a,b therefore force b=2a,
with the two a signs equal and the b sign opposite. A star with one H(a)
and two H(b) corners similarly forces a=2b. These are the only possibilities.

Since every vertex of an admitted limit must have a legal star, a pair with
neither relation is untileable. Relabel the types if necessary so b=2a.
The range b<60 is equivalent to 0<a<30. Every legal star then has two A=H(a)
faces and one B=H(2a) face; there are exactly two angle patterns:

    (120+a,120+a,120-2a),
    (120-a,120-a,120+2a).

No density or frequency assumption is used to deduce the relation.
We next build a full geometric periodic tiling for every parameter in that
range. This also handles 15<=a<30, where B has corners at or below 90.

## Explicit three-face flat torus

Use three counterclockwise polygonal faces indexed c=0,1,2. Faces 0 and 1
are copies of A and face 2 is B. Each face has sides j=0,...,5, with side j
running from corner j to corner j+1 modulo six. Choose corner labels on
faces 0 and 1 so even corners have angle 120+a and odd corners 120-a.
Choose labels on face 2 so even corners have angle 120-2a and odd corners
120+2a. The A labels are a cyclic shift of the initial edge-direction
normalization, which begins with 120-a; no new prototile is introduced.
Both A references use that same counterclockwise word; neither reference
is reflected. B uses its counterclockwise word beginning at a 120-2a
corner. Orient the quotient by these face interiors. Its development then
places every reference by an orientation-preserving Euclidean isometry,
so the witness does not require reflected tile copies.

For every c=0,1,2 and j=0,1,2, pair side (c,j) with side

    (c + delta_j mod 3, j+3),  delta_0=1, delta_1=2, delta_2=1.

Pair each edge by its length-preserving isometry reversing boundary endpoint
order. All edge lengths are one. These nine pairs use all eighteen sides
exactly once. Explicitly they are:

| first side | second side |
| --- | --- |
| (0,0) | (1,3) |
| (0,1) | (2,4) |
| (0,2) | (1,5) |
| (1,0) | (2,3) |
| (1,1) | (0,4) |
| (1,2) | (2,5) |
| (2,0) | (0,3) |
| (2,1) | (1,4) |
| (2,2) | (0,5) |

Writing (c,j) for corner j of face c, the individual seam endpoint pairs
in table order are:

    (0,0)~(1,4), (0,1)~(1,3);
    (0,1)~(2,5), (0,2)~(2,4);
    (0,2)~(1,0), (0,3)~(1,5);
    (1,0)~(2,4), (1,1)~(2,3);
    (1,1)~(0,5), (1,2)~(0,4);
    (1,2)~(2,0), (1,3)~(2,5);
    (2,0)~(0,4), (2,1)~(0,3);
    (2,1)~(1,5), (2,2)~(1,4);
    (2,2)~(0,0), (2,3)~(0,5).

Actual reversed-endpoint identification gives exactly six vertex classes:

    {(0,0),(1,4),(2,2)},  {(0,1),(1,3),(2,5)},
    {(0,2),(1,0),(2,4)},  {(0,3),(1,5),(2,1)},
    {(0,4),(1,2),(2,0)},  {(0,5),(1,1),(2,3)}.

Here (c,j) denotes corner j of face c. Each vertex link is a three-sector
cycle. At every even class the angle total is
2(120+a)+(120-2a)=360, and at every odd class it is
2(120-a)+(120+2a)=360. The face adjacency graph is connected. Reversing
endpoint order on CCW face boundaries makes the surface orientable, and its
Euler characteristic is V-E+F=6-9+3=0. It is therefore a torus.

Equip it with the intrinsic Euclidean metric of its polygon faces. The
three-sector sums remove every cone singularity; it is a compact complete
flat torus. Its universal cover is a complete simply connected flat surface,
thus globally isometric to the Euclidean plane (continue a Euclidean chart
by flat development; completeness gives the whole plane, and simple
connectedness makes the covering one-sheeted). The lifted polygon cells
therefore cover the plane with disjoint interiors as genuine copies of A
and B. This is the required global geometric tiling, not just a formal
angle atlas or a locally realizable patch.

The deck transformations preserve orientation and act freely. An
orientation-preserving Euclidean isometry with nontrivial rotation has a
fixed point, so every nonidentity deck transformation is a translation.
The deck group is Z^2, is discrete by proper discontinuity, and is cocompact
because the torus is compact; it gives two independent translation periods.
The resulting plane tiling is doubly periodic, with two A faces and one B
face per torus fundamental domain.

## The exceptional class cannot occur with one triangle class

If an admitted limit contains S, each native 168 corner must belong to a
three-corner star. Two further angles from H(a) or S must total 192.
The only possibilities are:

* Two H(a) corners: 2(120-a)=192, requiring a=24.
* One H(a) and one 108 corner: 120-a+108=192, requiring a=36.
* One H(a) and one 60 corner: 120+a+60=192, requiring a=12.

Two further S corners never total 192. Two 168 corners leave only 24,
smaller than every available angle. Thus a is one of 12,24,36 if S appears.
For each value the complete three-corner list gives a missing S corner:

| a | H(a) angles | all legal triples, degrees | unavailable S corner |
| --- | --- | --- | --- |
| 12 | 132,108 | 132+60+168 | 108 |
| 24 | 144,96 | 144+108+108; 96+96+168 | 60 |
| 36 | 156,84 | 84+108+168 | 60 |

The list distinguishes coincident 108 angles of different types when a=12;
the numerical impossibility is the same for both. Each copy of S has all
three corner categories, so no S copy can occur at any parameter. Removing
S would leave a monohedral H(a) limit, which was excluded above. Hence H(a),S
is untileable. The S,S case has no legal trivalent star and is untileable too.

This exhausts every noncentral case and proves the theorem.

## Exact verification, scope, and restart state

The independent-from-geometry script
[exact symbolic verifier](../searches/new-angle-two-equilateral-hexagons-verify.py)
checks all twenty three-corner multisets of the four affine triangle angles;
all fifteen three-corner multisets containing a sporadic 168 label; all
thirty-five angle triples at each of a=12,24,36; the S-only triple list; and
all nine torus edge gluings using reversed-endpoint union-find, vertex links,
connectivity, Euler characteristic and exact affine angle sums. Its retained
[certificate](../certificates/new-angle-two-equilateral-hexagons-certificate.json)
and [search record](../searches/new-angle-two-equilateral-hexagons-search.md)
make the finite check replayable.

    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-two-equilateral-hexagons-verify.py
    conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_equilateral_hexagons.py

The script does not prove the imported unlimited-root-order classification,
the compactness/defect-free limit theorem, or the flat universal-cover fact.
These are the explicit proof dependencies above. There is no bounded rational
angle denominator, finite patch inference, or positive tile-frequency premise.

The entire equilateral rational-angle (6,6) route is closed under its stated
assumptions. Reopening requires non-equilateral side lengths or irrational
angles permitting additional equilateral closure classes. The result does
not settle any remaining repeated-length, irrational-angle, or pentagon route.
