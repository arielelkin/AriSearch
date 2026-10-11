# All-obtuse pentagon partners of the regular dodecagon

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/all-obtuse-pentagon-regular-dodecagon-review.md)
is valid for the complete parameter classification and universal periodic
construction. The exact fixture and formal gluing/area proof also passed the
[fresh independent checker](../reviews/verify_regular_dodecagon_independent.py).
The seven-motif construction below is proved for a continuous exact family.
A separate fixed asymmetric algebraic member also passed complete exact
lattice-overlap and area checks. Neither result is a global solution or a
novelty claim.

## Classification theorem

Let P be a genuine convex pentagon with every angle strictly between pi/2
and pi. Let Q_n be the regular unit-side n-gon, n>=8, with all unrestricted
isometries, contacts, and omission allowed as in the
[research problem](../../research-problem.md).

* For 8<=n<=11, the pair {P,Q_n} is untileable.
* For n=12, the pair tiles if and only if P is congruent to one of the
  pentagons P(ell,p) defined below. Every member has an admitted tiling with
  two independent translational periods.

Write h=pi/12, omega=exp(2pi*i/3), s=sin(h), c=cos(h), and R=1/(2s)=2c.
Take any real parameters satisfying

    -h < p < h,
    ell > 2s^2 / (sqrt(3)*sin(h-|p|)).                     (A)

Set

    e1=exp(i*(5h-p)),    e3=exp(i*(15h-p)),
    P(ell,p)=[0, ell, ell+e1, ell*omega-e3, ell*omega].     (B)

Vertices are listed counterclockwise. Its consecutive side lengths are
(ell,1,t,1,ell), with t>0. Its consecutive angles are

    2pi/3,   a,   b,   7pi/6-b,   7pi/6-a,
    a=7h+p,
    b=7h-p-arg(sqrt(3)*ell-2s*exp(-ip)).                 (C)

The argument in (C) is the unique value in (-pi/2,pi/2); (A) makes its
real part positive. Each of the last four angles is strictly between
pi/2 and 2pi/3. Reflections send p to -p. No quotient by that symmetry is
required, and the parameter range deliberately includes both signs.

The family is not limited to four 105-degree corners. For p=0, all four
are 105 degrees and t=sqrt(3)*ell-2sin(15 degrees)>0. For p!=0 they occur
as two unequal complementary pairs and the closure generally gives four
distinct small angles. Neither this statement nor the construction asserts
that every tiling of a member is periodic. Cases n>=13 remain outside the
classification.

## 1. Local contacts and the n>=12 gate

Use the reviewed [all-obtuse forcing theorem](obtuse-edge-forcing.md):
every admitted tiling is full native-edge and trivalent. Q_n's angle is
beta=(n-2)pi/n. A star with two Q_n sectors would leave a P sector of
angle 4pi/n<=pi/2, impossible here. A three-Q_n star is also impossible.
Thus every Q_n side has a P neighbor, and two Q neighbors cannot be
consecutive side neighbors of a P. P has at most two Q side neighbors.

For centroid windows W_R of side 2R, corner and angle sums give, uniformly
in window translation,

    N_P=(n-6)N_Q+O(R),
    N_P+N_Q=Theta(R^2).

This is the same boundary argument detailed in the reviewed
[heptagon classification](all-obtuse-pentagon-regular-heptagon-classification.md):
fixed positive area and bounded diameter give only O(R) boundary tiles.
Counting P-to-Q sides now gives

    n*N_Q <= 2*N_P+O(R)
           = 2(n-6)*N_Q+O(R).

Since N_Q=Theta(R^2), n>=12. This proves the first part without a finite
search. Neither tile type can be omitted by the displayed curvature ratio.

## 2. A saturated n=12 limit

For n=12, define the nonnegative integer deficit d(P)=2 minus the number
of Q side neighbors of a P. Every Q has exactly twelve P side neighbors,
so double counting contacts and N_P=6N_Q+O(R) gives

    sum_(P centroid in W_R) d(P)=2N_P-12N_Q+O(R)=O(R).       (D)

A bad P has positive deficit, so the number of bad centroids is uniformly
O(R). Every fixed-radius disk can be translated to miss bad centroids:
otherwise O(R) disks of that radius centered at bad tiles would cover an
area of order R^2. Let such empty radii tend to infinity, translate their
centers to zero, and take a diagonal local placement limit. Fixed positive
areas bound local tile counts, centroids are bounded on each window,
and O(2) is compact. Coverage and disjoint interiors persist under this
limit. Full-side neighbors and native stars persist as well: use a radius
smaller than the distances, on either reference polygon, from a native
vertex to all its other vertices and nonincident sides. Distinct tiling
vertices are separated by that radius, since the three incident corner
wedges fill its disk and full-edge forcing prohibits an extra vertex on a
wedge ray. Extract the finite adjacent placements along with each tile.
Fixed side lengths and the separation prevent collapse or merged stars.
This is precisely the independently reviewed good-limit argument in the
heptagon classification, applied to deficit (D).

The resulting admitted plane tiling has exactly two nonadjacent Q sides
on every P. Statements henceforth refer to this potentially different
limit tiling, not to an unjustified pointwise interpretation of (D).

## 3. Forced angle and side word

Write delta=2pi-5pi/6=7pi/6. At a P,P,Q star, the two P angles sum to delta,
and each is strictly below 2pi/3 because the other is strictly above pi/2.
A P with two nonadjacent Q sides has exactly four P,P,Q corners and one
P,P,P corner. If all five native P angles were below 2pi/3, a P,P,P star
would be impossible. Exactly one native P angle is therefore at least
2pi/3; the other four are below 2pi/3 and already forced to be P,P,Q.
The large angle is the unique P,P,P corner on every P. Every P,P,P star
thus has three copies of that same angle, which must equal 2pi/3.

Label that vertex0, followed counterclockwise by vertices1,...,4 with
angles a,b,d,e. A Q side cannot be incident to vertex0. Its two
nonadjacent positions among the three remaining sides are necessarily
sides1 and3. Thus these sides have length1; sides0,2,4 have P neighbors.

Side2 has two small-angle endpoints and must match another P's side2.
It cannot match side0 or4, whose 120-degree endpoint would pair with a
strictly obtuse P corner at a Q star and exceed 360 degrees. Sides1,3 are
already Q contacts. For matching side2 to side2, either its endpoint
correspondence exchanges b,d, or it preserves their native labels.
The former gives b+d=delta; the latter gives 2b=2d=delta. In both cases,

    b+d=delta,   a+e=delta,

where the second equality follows from the P angle sum and vertex0=120
degrees. Its word is therefore (120,a,b,210-b,210-a), with a,b and their
complements all strictly between90 and120 degrees.

Let ell0,ell4 be lengths of the two sides at vertex0. These lengths must
be equal. If they differ, each such side can only match the same native
side index: it cannot match side2 by its large endpoint, and cannot match
the other large-endpoint side because of the unequal length. Around each
P,P,P vertex the three sector copies each have one incident ell0 ray and
one ell4 ray. Whole-side matching would make the three shared rays a
cycle with two labels, and at each sector the two adjacent labels would
have to differ. An odd cycle cannot have that alternating labeling.
This contradicts the existence of that P,P,P star. Set ell0=ell4=ell>0,
and denote the middle side2's positive length by t.

This odd-cycle metric argument uses no chirality convention: reflections
may reverse the sector's two side labels but each sector still supplies
one of each. The limit has the original P shape, so all conclusions apply
to the original prototile.

## 4. Complete metric parameter range

Normalize vertex0 to0 and side0 to the positive real axis. Its other
incident vertex is ell*omega, because the angle at0 is120 degrees. Put
p=a-7h. Since90<a<120, |p|<h. The unit side1 direction is 5h-p and side3
direction is 15h-p: the exterior turns at b and delta-b sum to 5pi/6.
Consequently all its coordinates are exactly (B).

The middle vector is

    M=(ell*omega-e3)-(ell+e1)
      = exp(10h*i)*(sqrt(3)*ell-2s*exp(-ip)).              (E)

Put w=sqrt(3)*ell-2s*exp(-ip). The angle at vertex2 is
b=7h-p-arg(w), with the direction branch compatible with convexity;
hence its complement is delta-b. Let q=b-7h=-p-arg(w).
The condition |q|<h forces Re(w)>0. Its imaginary part has the sign of p,
so if p!=0 its argument has the same sign as p and

    |arg(w)| < h-|p|.

For p=0 the required middle edge is positive in the exp(10h*i) direction,
so w>0. In both cases the exact equivalent length inequality is

    sqrt(3)*ell > 2s*(cos(p)+sin(|p|)*cot(h-|p|))
                = 2s^2/sin(h-|p|),

which is (A). For p=0 this says ell>2s/sqrt(3). These steps prove necessity
of the full parameter domain and positivity of t=|w|.

Conversely, (A) gives Re(w)>0 and the stated argument bound, so all four
small angles lie strictly between90 and120 degrees. The five positive
edge directions are in increasing intervals

    0,  (60,90),  (120,180),  (210,240),  300 degrees.

Their closing exterior turns are positive and sum to360 degrees. This
closed positive edge polygon is strictly convex: for any one directed
side, cross products of successive edge vectors are first nonnegative
and then nonpositive as their directions advance through one full turn;
the cumulative signed distances from that side first increase and then
decrease to zero. All nonendpoint vertices have strictly positive signed
distance because every intervening turn is nonzero. Thus (B) is a genuine
strictly convex P, and no omitted parameter branch has been admitted.

## 5. Seven-motif periodic construction for every parameter

Use the P of (B) and define

    q0=ell+R*exp(-ip),       z=(1+omega)*q0,
    u=(omega-1)*q0,         v=(omega^2-1)*q0.

Here q0 is a Q center, not the angle parameter q used transiently above.
The Q polygon centered at q0 has vertices

    x_r=q0+(P_vertex2-q0)*exp(2h*r*i), r=0,...,11.

Its radius is R and its side length is1. In particular x0=P_vertex2 and
x1=P_vertex1. Define six pentagon motifs

    A_j=omega^j*P,
    B_j=z-omega^j*P,   j=0,1,2,

and take the single Q plus these six motifs, translated by all integer
combinations of u,v. The six P copies are rotations or half-turn copies;
no extra prototile, markings, or constraints are introduced. Since
Re(q0)=ell+R*cos(p)>0,

    det(u,v)=(3sqrt(3)/2)*|q0|^2>0.                       (F)

The independent periods are therefore nonzero.

First verify the edge identities, before asserting global tiling.
At every A_j vertex0 the three A copies meet with their native120-degree
sectors; side4 of A_j pairs with side0 of A_(j+1), indices modulo3.
The B triple pairs in the same way at z. Put

    t0=0, t1=v, t2=v-u.

Side2 of A_j pairs with side2 of B_j+t_j, with endpoints exchanged.
Indeed P_vertex2+P_vertex3=z and
(omega^j-1)*z=(0,v,v-u) for j=0,1,2. The half-turn fixing their side2
midpoint produces exactly the stated counterpart.

For P-to-Q contacts the Q centers across P's unit sides1,3 are q0,omega*q0.
This follows directly by adding the regular-Q apothem to the side
midpoint on P's exterior side. A direct identity is

    P_vertex2-q0=(1/2+i*cot(h)/2)*e1,
    P_vertex4-omega*q0=omega*(P_vertex1-q0).

Thus the same Q has the correct radius and endpoints on both matching
contacts. The following table gives every Q side [x_r,x_(r+1)] its unique
opposite P side. A translation shown is applied to the whole P motif.
The P side has the reverse boundary direction.

| Q side r | P copy | Native P side |
|---:|---|---:|
| 0 | A0 | 1 |
| 1 | A2 | 3 |
| 2 | B2+v-u | 1 |
| 3 | B1+v-u | 3 |
| 4 | A1-u | 1 |
| 5 | A0-u | 3 |
| 6 | B0-u | 1 |
| 7 | B2-u | 3 |
| 8 | A2-v | 1 |
| 9 | A1-v | 3 |
| 10 | B1 | 1 |
| 11 | B0 | 3 |

Rotation by120 degrees and half-turn are symmetries of the regular Q
frame, so these are identities for all parameters, not orientation
assumptions imposed on other tilings. The table uses each Q side exactly
once and every unit P side once modulo the lattice. The [formal affine
identity checker](../searches/regular_dodecagon_gluing_identities.py) verifies
all21 paired-edge endpoint identities over CyclotomicField(24)[ell,rho],
with rho a formal complex variable rather than a sampled value. It also
traces all42 native corner labels into exactly14 three-corner vertex classes:
two beta triples and twelve complementary P-pairs with Q. Its retained
[identity certificate](../certificates/regular-dodecagon-gluing-identities.json)
and [exact record](../searches/regular-dodecagon-gluing-identities.md) make
this side-table check replayable; the analytic positivity and covering steps
remain separate obligations.

## 6. Local gluing, exact area, and whole-plane coverage

Form an abstract finite surface by taking one Q face and the six A/B faces,
then identifying their sides by the preceding table and P-to-P pairings,
with period offsets reduced modulo the lattice. All edges are glued in
opposite boundary directions. Its vertex cycles have exactly three
corners: the two A/B triple vertices have120+120+120 degrees, while each
of the twelve Q vertices has150 degrees plus either a+(210-a) or
b+(210-b). This is visible at x1 from A0 and A2, at x2 from A2 and
B2+v-u, and repeats under the indicated rotations and half-turns.
All have total360 degrees. Thus this compact connected glued object is
a surface with locally Euclidean charts at faces, sides, and vertices.
It is not being assumed to embed without overlap.

The motif coordinates define a map from that abstract surface into the
flat torus C/(Z*u+Z*v), since all paired endpoints differ by their listed
period offsets. It is a local orientation-preserving Euclidean isometry:
inside faces this is immediate, at sides the two convex polygons occupy
opposite half-neighborhoods, and at vertices the three positive corner
wedges fit successively around exactly2pi. A compact local homeomorphism
to the connected target torus covers it with a positive integer degree:
its image is open and closed, every fiber is finite, and disjoint small
inverse neighborhoods show the fiber count is locally constant.

The degree is exactly1 by the following explicit area identity. Put
q=b-7h and retain p=a-7h just for this calculation. Shoelace, or splitting
off the triangle with vertices0,ell,ell*omega, gives

    area(P)=sqrt(3)*ell^2/4 + 1/4 + t*c*cos(q).

Closure (E), multiplied by exp(ip), gives

    2s+t*exp(-iq)=sqrt(3)*ell*exp(ip),
    t*cos(q)=sqrt(3)*ell*cos(p)-2s.

Since 2s*c=1/2 and R=2c, therefore

    area(P)=sqrt(3)*ell^2/4
            +sqrt(3)*ell*R*cos(p)/2 - 1/4.               (G)

Also area(Q)=3cot(h). The identity
sqrt(3)*R^2/4-cot(h)/2=-1/4 now gives, using (F),(G),

    area(Q)+6area(P)=det(u,v).                           (H)

A degree-d local Euclidean covering multiplies target area by d, so (H)
forces d=1. The map is consequently a homeomorphism and an isometry on
each polygon. Its lifted polygons in the plane form exactly the specified
periodic motif family: they cover the plane with disjoint interiors. This
establishes the entire infinite construction without supposing finite
patches extend or relying on an unverified planar packing assertion.

This argument is unaffected by accidental coincidences between differently
named motif coordinates modulo the lattice: any such multiplicity would
be multiple abstract preimages and would contradict the degree-one result.
The finite abstract side-pairing checks are the reason local completeness
is known before the area argument; area alone is not used to infer overlap
freeness of an arbitrary proposed packing.

## 7. Independent exact fixed asymmetric fixture

Choose

    ell=2,   sin(p)=1/8,   cos(p)=sqrt(63)/8,   0<p<h.

The [exact producer](../searches/obtuse_pentagon_regular_dodecagon_witness.py)
builds the seven motifs with these coordinates. It verifies strict convex
support inequalities, regular Q12 with unit sides, P side lengths
(2,1,t,1,2), the unique120-degree P angle, four other angles strictly
between90 and120 degrees, and unequal complementary angle pairs. It
then derives the entire lattice-coordinate overlap domain: 62 potentially
intersecting distinct ordered motif/shift pairs. Exact convex clipping
finds zero area in every intersection and motif area equals det(u,v).
This is a second direct whole-plane verification for one asymmetric member,
independent of trusting the general flat-surface construction argument.

The [certificate](../certificates/obtuse-pentagon-regular-dodecagon-witness.json)
retains rational minimal polynomials and rational isolating intervals for
all nonrational coordinates and measurements. Its
[search record](../searches/obtuse-pentagon-regular-dodecagon-witness.md)
states the exact domain and replay. The fresh independent checker linked above has passed the fixture by
separating axes, all21 universal endpoint identities coefficientwise,
all14 ordered native-corner cycles, and the symbolic area identity. The
continuous-family classification and its degree-one argument have passed
the fresh hostile review separately.

## Dependencies, scope, and source boundary

The all-obtuse forcing theorem and the independently reviewed translated
limit argument are the only imported research lemmas. The angle, metric,
parameter, side-pairing, and area calculations are written explicitly.
The elementary covering argument is supplied rather than importing a
classification of periodic tilings or a monohedral escape theorem.

Every P,Q12 tiling implies the same P belongs to (A),(B), possibly after
reflection; every member has a rank-two periodic tiling. These facts
exclude strong aperiodicity throughout this restricted n=12 family.
No conclusion about n>=13, nonregular Q, or a P having any right/acute
corner is established. A [narrow current primary-source audit](../literature/regular-dodecagon-pentagon-source-audit.md)
identified a close 2025 dodecagon/deformed-pentagon construction; its exact
metric relation remains unresolved. No novelty or priority is claimed.
The unrestricted two-convex-tile target remains unresolved.
