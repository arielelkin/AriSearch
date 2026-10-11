# Exact obstructions to two all-obtuse Penrose carriers

**Status:** adversarially reviewed; [independent root audit](../reviews/new-angle-penrose-recomposition-review.md) valid under the stated source hierarchy hypotheses. The two general
lemmas are independent of Penrose atlas forcing. The Penrose application
uses the named source hierarchy, with its tile-frequency calculation given
below. No new pair with plane existence is claimed.

## 1. Whole-parallelogram fusion cannot give a convex pentagon

**Theorem.** If a genuine compact convex polygon C is tiled by finitely many
whole parallelograms with disjoint interiors, C is centrally symmetric.
No edge-to-edge assumption is needed.

Orient every tile boundary counterclockwise. For each unoriented line
direction d present among the finitely many sides, choose one directed unit
vector u along it. Sum the signed lengths of boundary segments parallel to
u: positive for the u direction, negative for -u. Each parallelogram has
zero sum, because its opposite sides are parallel, equal, and oppositely
oriented. At an internal interface the two signed boundary contributions
cancel after subdividing into common segments. Isolated point contacts
have zero length. Thus the signed length sum on C's boundary is zero for
every d.

Strict convexity at its genuine corners means a directed side direction
appears at most once in C's cyclic side list. A side in direction u
therefore has exactly one opposite parallel side in direction -u, of the
same length. The side directions are ordered circularly, so shifting them
by pi sends index j to j+m/2, where m is the number of sides. The paired
vectors satisfy e_(j+m/2)=-e_j. Therefore v_j+v_(j+m/2) is independent
of j. Its half is the center of symmetry. In particular m is even.

Consequently a fusion of finite whole thin/fat Penrose rhomb clusters
cannot produce any convex pentagon. This obstruction acts before the
15-map atlas or converse-recognition question arises. It does not rule
out cutting the rhombs or adding other source shapes.

## 2. Rational-area pieces obstruct all-obtuse (5,n) recomposition

### General theorem

Let a source plane tiling use two fixed polygons T and t with
area(T)/area(t) irrational, and suppose their positive count frequencies
exist with N_T(R)/N_t(R) tending to an irrational value eta in large
square windows. Suppose the same plane is repartitioned into isometric
copies of two fixed genuine convex polygons P and Q, where P has five
sides, Q has n>=5 sides, and all their angles lie strictly between pi/2
and pi. Assume each final tile is a union of finitely many source pieces,
and each piece lies in one source tile and has a rational fraction of
that source tile's area. Then this repartition is impossible.

Pieces need not share a universal subdivision template, and the final
tile's source composition may initially be allowed to depend on position.
The source and final tile diameters are bounded. Pieces are used exactly
once, with disjoint interiors; they are not transported to distant source
locations. These are actual local cut/reassembly hypotheses, not extra
placement rules for the final two unmarked polygons.

### Proof

For one final tile F define its source masses

    a(F)=sum area(piece)/area(T) over its T pieces,
    b(F)=sum area(piece)/area(t) over its t pieces.

Both are nonnegative rational numbers. Its area is

    area(F) = a(F)*area(T)+b(F)*area(t).              (1)

If two congruent F tiles had distinct pairs (a,b), subtracting (1) would
express the irrational area ratio as a rational ratio, unless both
coordinate differences were zero. Thus every P copy has one fixed
rational mass vector (aP,bP), and every Q copy one fixed rational mass
vector (aQ,bQ). This conclusion does not presume a unique source
partition of the final shape.

Count source and final tiles meeting a square of radius R. Boundary tiles
from either tiling number O(R), by bounded diameters and positive minimum
areas. Each has bounded mass: the other tiling's fixed polygons which can
meet it lie in a uniformly bounded region. Conservation of each source
type's normalized area mass therefore gives

    N_T(R) = aP*N_P(R)+aQ*N_Q(R)+O(R),
    N_t(R) = bP*N_P(R)+bQ*N_Q(R)+O(R).              (2)

The all-obtuse forcing theorem makes the final tiling edge-to-edge and
trivalent. Its exact window curvature identity gives

    N_P(R)-(n-6)*N_Q(R)=O(R).                       (3)

For n=5 this contradicts the quadratic number of final tiles. For n=6,
N_P=O(R) and N_Q=Theta(R^2). For n>=7 both types have quadratic counts
and N_P/N_Q tends to n-6. Substitute (3) into (2), writing r=n-6 for
n>=6. This gives

    eta = (r*aP+aQ)/(r*bP+bQ).                     (4)

The denominator is positive: otherwise all its nonnegative terms vanish
(and when r=0 the P contribution is only O(R)), contradicting the
positive quadratic frequency of source t. Equation (4) is rational,
contradicting the assumed irrational eta. This proves the theorem.

### Penrose source hypotheses

For unit rhombs with acute angles 72 and 36 degrees,

    area(T)/area(t)=sin72/sin36=2cos36=phi,
    phi=(1+sqrt5)/2.

The geometrical Penrose source is the undecorated image of a marked
Penrose tiling, not an arbitrary tiling by these two rhombs. Its primitive
inflation hierarchy is described in Fernique--Lutfalla,
[arXiv:2211.08239v2](https://arxiv.org/html/2211.08239), Section 2.1 and
Figure 11. The same primary source proves that the fifteen radius-one
maps characterize this source; its seven radius-zero maps are insufficient.
No radius-zero replacement is made here.

Here is the frequency calculation used for the source. Bisect thick
rhombs into obtuse Robinson triangles (36,36,108 degrees) and thin rhombs
into acute Robinson triangles (36,72,72 degrees). Both half types have
half their corresponding rhomb area. The standard half-rhomb hierarchy
subdivides an inflated thick half into two thick halves and one thin half,
and an inflated thin half into one of each. The integral counts also follow
uniquely from areas: phi^2*phi=2phi+1 and phi^2=phi+1. Thus its matrix in
(thick,thin) order is

    M = [[2,1],[1,1]],  M*(phi,1)^T=phi^2*(phi,1)^T.

The other eigenvalue is phi^(-2). Counts in either high-order parent
triangle consequently have thick/thin ratio tending uniformly to phi.
To pass from parent triangles to any plane tiling in this hierarchy,
partition a square into complete fixed-order supertriangles and boundary
supertriangles. For any fixed hierarchy level the boundary contributes
O(R), while the interior tiles have ratios between those of the two
parent types at that level. Let R tend to infinity first, then the hierarchy
level tend to infinity. This proves the plane-window ratio phi. The two
halves per rhomb preserve that ratio. The only imported source property
is the standard plane-wide Robinson/Penrose inflation hierarchy, not a
new frequency theorem inferred from numerical patches.

The explicit half-rhomb recursion and its ratio proof are also displayed by
A. Treibergs in [his authored lecture notes](https://www.math.utah.edu/~treiberg/PenroseSlides.pdf),
slides 28--30,42--45,49; these provide an accessible verification of the
named hierarchy conventions. They are not being used to classify convex
final tiles. The general theorem above is independent of these sources,
conditional only on its clearly stated source area/count hypotheses.

Therefore diagonal bisections, or any finite rational-area cutting scheme,
cannot turn a geometrical Penrose tiling into an all-obtuse (5,n) tiling
with just two congruence classes. A different rational denominator or
radius-one context does not rescue this construction mechanism.

## 3. Exact sun-pentagon proposal and its failure

Let z=exp(2pi*i/5), equivalently the unique root of
z^4+z^3+z^2+z+1 with positive imaginary part and pi/3<arg(z)<pi/2.
Put u_j=z^j. The five unit fat rhombs

    R_j=conv{0,u_j,u_j+u_(j+1),u_(j+1)}, j modulo 5,

form a Penrose sun vertex patch. Their sectors at zero have angle
72 degrees and disjoint interiors. Cut R_j along the diagonal joining
u_j to u_(j+1). The five inner halves

    conv{0,u_j,u_(j+1)}

join to the exact regular pentagon

    P=conv{u_0,u_1,u_2,u_3,u_4}.

P has side length 2sin36 degrees, angle 108 degrees, and source mass
vector (5/2,0). This is an exact local convex cluster from cut rhombs,
so the whole-parallelogram obstruction does not apply to it.

However, completing the entire source plane with only this P and ONE
all-obtuse Q assembled from diagonal/rational-area pieces is impossible
by Section 2, regardless of Q's metric closure or n. Thus no global
existence claim can be made for this proposed carrier/holes system.
This is a falsified construction mechanism, not a local pattern promoted
to a candidate.

A precise way to evade the rational-area assumption is to shrink the
central pentagon by rho=phi^(-1/2). Within each R_j take
conv{0,rho*u_j,rho*u_(j+1)}. Its area fraction of R_j is rho^2/2=1/(2phi),
so the central regular pentagon has mass (5/(2phi),0), which is irrational.
The remainder inside each fat rhomb is a genuine convex pentagon with
angles (126,108,72,108,126), in cyclic order. These exact remainder shapes
have an acute corner and can no longer serve as an all-obtuse higher-sided
Q. The endpoints of either unit side adjoining the 72-degree corner have
angles 108 and 72, summing to 180. Glue two such remainder pentagons
by a half-turn along that side. Their interiors are disjoint, their two
endpoint boundary corners straighten, and their union is a convex
centrally symmetric hexagon. Its translates tile periodically, by the
explicit hexagon construction in
[new-angle-equilateral-rational-obstruction.md](new-angle-equilateral-rational-obstruction.md).
Therefore choosing this remainder pentagon as the second prototile has a
periodic monohedral escape, at every rho in (0,1), independently of the
missing thin-rhomb assignment. This exact irrational shrinkage fails as a
two-prototile mechanism; it does not eliminate other irrational-area cuts.
Thin source rhombs and other vertex environments also remain unassigned.
No complete two-type plane repartition or shape-only atlas forcing follows.

## 4. Review, scope, and restart instructions

The claims above use exact identities, signed side-length conservation,
rational independence, and the established all-obtuse curvature identity.
No finite geometric search, solver result, numerical coincidence, or
certificate of global existence is used. Fresh independent hostile review
is pending. No novelty assertion follows from the narrow source check.

The whole-rhomb route is falsified for a convex pentagon, and the rational-
area all-obtuse cut route is falsified. Reopen only with irrational source
area fractions, a final acute/right corner permitting curvature defects,
more final congruence classes, or a materially different source whose
frequency invariant changes. The first two options remain permitted by
the main problem, but no global pair is presently specified here.

The Penrose atlas theorem does remove one source-recognition uncertainty,
but these obstructions arise in forward repartition/existence before its
converse atlas-forcing obligation. Simply naming that obligation is not
an active construction mechanism.
