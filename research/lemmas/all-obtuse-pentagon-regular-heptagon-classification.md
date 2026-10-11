# Classification of all-obtuse pentagon partners of the regular heptagon

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/all-obtuse-pentagon-regular-heptagon-review.md)
is valid, including the full analytic classification. The positive witness
has passed an exact independently structured checker. This
result excludes a restricted family, and does not resolve the unrestricted
research problem. No novelty claim is made.

## Theorem and precise scope

Let Q be the regular heptagon with side length 1, and let P be any genuine
compact convex pentagon whose five interior angles lie strictly between
pi/2 and pi. Under the [unrestricted tiling definition](../../research-problem.md),
{P,Q} tiles the plane if and only if P is congruent to the following pentagon
P*: its consecutive angles are

    gamma, alpha, alpha, alpha, gamma,
    alpha = 4pi/7,   gamma = 9pi/14,

its four sides between consecutive entries in that displayed word have
length 1, and its closing gamma-to-gamma side has length

    L = sin(pi/7)/sin(3pi/14).

The word, these side lengths, and convexity uniquely determine P* up to
unrestricted isometry. The exhibited tiling has two linearly independent
translation periods. Consequently every pair in this restricted family is
untileable or has a periodic escape from strong aperiodicity. The conclusion
asserts existence of a periodic tiling when a tiling exists; it does not
assert that every tiling of P*,Q is periodic.

Reflections, arbitrary rotations, partial contacts, and omission of a type
are permitted throughout. Neither an initial angle alphabet nor equal P
side lengths are assumed. Rescaling both polygons gives the corresponding
statement for any common regular-heptagon side length.

## Dependencies and boundary counts

The only imported geometric forcing result is the reviewed
[all-obtuse edge-to-edge theorem](obtuse-edge-forcing.md): every admitted
plane tiling here has complete native-side contacts and exactly three
genuine corners at each vertex. We also use the reviewed
[four-alpha/one-beta heptagon obstruction](regular-heptagon-one-beta-pentagon-obstruction.md)
in the k=4 case below. Neither import is a monohedral classification.

Fix hypothetical shapes P,Q and an admitted tiling. Choose each tile's
centroid as its reference point. Let N_P,N_Q count reference points in a
translated square W_R of side 2R, and count vertex stars by the location of
their vertex. Every displayed O(R) bound below is uniform in translation,
with constants depending only on these fixed shapes. Their positive minimum
area and bounded diameter imply that only O(R) tiles meet a fixed-width
boundary strip and that N_P+N_Q=Theta(R^2). Each tile supplies only finitely
many sides and corners, so changing between tile-reference-point and
vertex/edge-location counting changes a total by O(R).

Let V be the number of stars. Corner and angle totals give

    3V = 5N_P + 7N_Q + O(R),
    2V = 3N_P + 5N_Q + O(R).

Subtracting after multiplication to eliminate V gives

    N_P = N_Q + O(R).                                      (1)

Thus both types have uniformly positive quadratic counts. This also covers
omission: no admitted tiling can omit either type or use one only with
subquadratic counts. No existence or frequency convergence is inferred
from (1).

## The native-angle saturation gate

Put beta=5pi/7, Q's angle. No Q,Q,Q star exists because 3beta!=2pi.
Write X,Y,Z for numbers of Q,Q,P; Q,P,P; and P,P,P stars, respectively.
Counting sectors of each tile type gives

    7N_Q = 2X + Y + O(R),
    5N_P = X + 2Y + 3Z + O(R).

Eliminating Y, then using (1), yields

    X = (14N_Q-5N_P)/3 + Z + O(R)
      = 3N_Q + Z + O(R).                                  (2)

The P corner at every Q,Q,P star has angle
alpha=2pi-2beta=4pi/7. Let k be the number of P's five native angles exactly
equal to alpha; k is a fixed integer attached to the prototile. At most
kN_P+O(R) P-alpha sectors are available in W_R, so

    kN_P >= X + O(R).

Equations (1),(2), Z>=0, and N_P=Theta(R^2) imply k>=3. This is the precise
saturation gate; it uses actual whole-plane counts, not bounded patches.

If k=5, the P angle sum is 20pi/7 rather than 3pi, impossible. If k=4,
the remaining P angle is 3pi-4alpha=beta, and the imported one-beta
obstruction excludes a tiling with arbitrary P side lengths. Hence k=3.
Let theta,psi be the two other P angles. Both are obtuse, neither equals
alpha, and theta+psi=9pi/7.

## Nonnegative defects and an admitted defect-free limit

Let B_alpha count P-alpha corner incidences at stars other than Q,Q,P.
It is an actual nonnegative integer. Every Q,Q,P star supplies exactly
one P-alpha incidence, so

    B_alpha = 3N_P-X+O(R).

Together with (1),(2), this gives

    B_alpha + Z = 3(N_P-N_Q)+O(R) = O(R).                   (3)

Both terms on the left are nonnegative. A P tile is bad if at least one of
its alpha corners is not Q,Q,P, or if it is incident to a P,P,P star.
Counting these flags bounds bad-tile reference points in W_R by
B_alpha+3Z+O(R), and hence by O(R), uniformly in translation. Q tiles are
never declared bad. Equation (3) is not a pointwise assertion about the
original tiling.

For every fixed radius H, some disk of radius H contains no bad reference
point. Otherwise every point in a large square W_R would be within H of a
bad reference point in its H-enlargement. There are O(R+H) such points, and
their radius-H disks have total area at most O((R+H)H^2), less than 4R^2
for sufficiently large R. This contradicts covering W_R. Choose such disks
with H tending to infinity and translate their centers to the origin.

Here are the compactness details needed to obtain a plane tiling. In each
fixed bounded region, the translated tilings have uniformly finitely many
tiles whose centroids lie there, since all these tiles lie in its bounded
D-enlargement and have disjoint interiors of fixed positive area. Their
centroid coordinates are in a compact set and their orientation matrices
lie in compact O(2). By successive subsequences on larger regions, extract
a diagonal locally finite collection of convergent tile placements; one
may choose the exhaustion boundaries to avoid the countably many limit
centroids. Every point x remains covered: choose a covering tile in every
member of the subsequence, whose centroid is at distance at most D from x,
and extract its convergent placement in that compact region. Its closed
limit polygon still contains x. Two limit polygons cannot overlap in their
interiors, because an open intersection disk would persist in sufficiently
close placements. Distinct retained copies cannot collapse to the same
polygon for the same reason. Thus the limit is an admitted plane tiling.

Native stars and their type labels also persist. For explicit control,
choose r>0 smaller than, for either reference shape at any native vertex,
the distances to every other native vertex and every nonincident side.
At a tiling vertex the three incident corner wedges cover B(v,r). Another
tiling vertex in that disk would enter one of their interiors, or lie on a
wedge ray and subdivide a full native side, both impossible. Consequently
distinct vertices are uniformly separated. Extract the finite whole-side
neighbors and corner tiles along with each selected tile. Shared sides and
vertex incidences persist under convergence; their fixed positive lengths
and the vertex separation prevent collapses or merging stars. The three
retained incident corners exhaust the angle 2pi. Every limit P tile and
these neighbors have reference points inside the growing good disks for
large enough H. Therefore all three of its alpha corners are Q,Q,P and
there is no P,P,P star in the limit.

This limit may differ from the original tiling. Only now do we apply those
pointwise conclusions. The all-obtuse forcing theorem applies to the limit
as an admitted tiling, independently of the preceding persistence argument.

## Forced sides and exact polygon closure

In the limit, a theta or psi corner cannot be Q,Q,P because its angle is
not alpha, and cannot be P,P,P. It is therefore P,P,Q. An alpha corner is
Q,Q,P, so both of its incident side neighbors have type Q. Any P-to-P side
must consequently have theta and psi endpoints. Such a side can exist only
if these two corners are adjacent. At each of them the P,P,Q star requires
exactly one incident P-to-P side, so the edge connecting them is the unique
P-to-P side of P. Its other four sides have Q neighbors and hence length 1.

Label the four-unit-edge chain from theta to psi counterclockwise and put
its first directed edge on the positive real axis. At the three intervening
alpha corners the exterior turn is t=pi-alpha=3pi/7. Its unit edge vectors
are consequently

    1, exp(it), exp(2it), exp(3it).

Their sum is

    S = exp(3it/2)*sin(2t)/sin(t/2)
      = exp(9pi*i/14)*sin(pi/7)/sin(3pi/14)
      = L*exp(9pi*i/14),                                  (4)

where L>0. The remaining side must have vector -S, directed at 23pi/14.
The preceding unit edge is directed at 9pi/7=18pi/14. Hence the exterior
turn at psi is 5pi/14; the turn from the closing side back to the first
side is also 5pi/14. Both remaining interior angles are gamma=9pi/14.
These directions and lengths fix the entire polygon up to isometry.
Since the limit uses exactly the same shape P, the original prototile must
be P*. No assertion of periodicity of that original tiling has been used.

## Exact positive periodic witness

All the following coordinates are in the complex plane. Put

    zeta = exp(pi*i/7),
    D = cot(pi/7),     R = 1/(2sin(pi/7)).

For purely algebraic defining data, zeta is the unique root of
x^6-x^5+x^4-x^3+x^2-x+1 whose real part is in (9/10,91/100) and imaginary
part in (43/100,44/100). D and R have the displayed exact expressions in
its real and imaginary parts. The certificate below also records every
nonrational real coordinate by its rational minimal polynomial and a
rational isolating interval.

Define six auxiliary centers

    c0=0, c1=D, c2=D(1+zeta^3),
    c3=D(1+zeta^3+zeta^6), c4=D(zeta^3+zeta^6), c5=D*zeta^6,

and k=(0,3,6,7,10,13). Define

    u=c2,  v=c4,  C=c3,
    h_j=c_j+R*zeta^(k_j+1),  j=0,...,5,
    a=R*zeta^3,  b=C-a.

Four cyclic polygons, with vertices in counterclockwise order, are

    Q0 = [ R*zeta^(2j+1) : j=0,...,6 ],
    Q1 = [ D-q : q in Q0 ],
    P0 = [ a,h0,h1,h2,b ],
    P1 = [ C-p : p in P0 ].

Take all copies of these four polygons translated by n*u+m*v for all
integers n,m. Q1 and P1 are half-turn copies, so the construction uses just
two congruence classes. The producer checks exactly that every polygon is
strictly convex, Q0 is regular with unit sides and angle beta, and P0 has
four unit sides, closing length L, and consecutive angles
(gamma,alpha,alpha,alpha,gamma). All these angles are obtuse, and P0 is the
P* determined by (4). The determinant det(u,v) is strictly positive, so
u,v are independent nonzero periods.

## Finite certificate implies whole-plane coverage

The [producer](../searches/all_obtuse_pentagon_regular_heptagon_witness.py)
and [certificate](../certificates/all-obtuse-pentagon-regular-heptagon-witness.json)
retain exact coordinates, lengths, angle cosines, areas, periods, and the
complete list of 26 nontrivial potentially intersecting translated pairs.
No finite patch extension is presumed.

Here is the completeness argument for the overlap domain. Let A be the
matrix with columns u,v and map all motif vertices to lattice coordinates
A^(-1)p. For motifs i,j and coordinate a=0,1, the only translations (n,m)
that can give any intersection satisfy, in that coordinate,

    ceil(min_i[a]-max_j[a]) <= shift[a]
                            <= floor(max_i[a]-min_j[a]).

Convex polygons' coordinate extrema occur at vertices. This finite product
of integer intervals therefore covers every possible intersection, without
assuming any orientation restriction in the original problem. Remove only
the identical copy (i=j,n=m=0). The producer enumerates the resulting 26
comparisons and clips convex polygons in exact AA arithmetic, verifying
that each intersection has area zero. For convex polygons with nonempty
interiors, positive interior intersection would have positive area. Thus
all distinct copies in the infinite periodic family have disjoint interiors.

It also verifies exactly

    2 area(Q0) + 2 area(P0) = det(u,v).                      (5)

The lattice is discrete and the motif bounded, so the periodic family is
locally finite and its union is closed. Integrating its nonoverlapping tile
indicators over a lattice fundamental parallelogram counts the total motif
area, which by (5) is the parallelogram area. A complementary point would
lie in an open complementary disk; periodicity would give positive missing
area in a fundamental domain, contradicting (5). Hence the union covers
the entire plane. This proves existence directly, without an unverified
carrier packing or hole-filling claim.

The [search record](../searches/all-obtuse-pentagon-regular-heptagon-witness.md)
provides the exact domain, environment, and replay command. The source's
assertions are proof relevant and must be run without Python optimization.
The [fresh independent checker](../reviews/verify_all_obtuse_regular_heptagon_independent.py)
has passed, using separating-axis tests rather than importing the producer
or its clipping implementation. The full analytic reduction has separately passed the fresh hostile review
linked above.

## Scope and remaining research obligations

The general reduction allows all obtuse P angles and all positive side
lengths, and uses a translated good limit solely to determine the shape.
The converse supplies an admitted doubly periodic tiling. No condition is
imposed on arbitrary original tilings, no finite orientation alphabet is
assumed in the reduction, and no density statement is upgraded to a
pointwise statement in an original tiling.

The hypotheses that Q is regular and every P corner is strictly obtuse
are essential scope limits. Pentagons with right or acute corners, or
nonregular heptagons, are not classified. Arbitrary convex pairs remain
unresolved. Current primary literature has not been searched for this
specific classification, so it is preserved as an internally proved
restricted result with no novelty assertion.
