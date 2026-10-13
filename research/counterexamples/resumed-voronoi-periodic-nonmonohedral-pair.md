# Resumed intrinsic construction: exact Voronoi (5,8) pair and repeatable parent

Date: 2026-10-13. **Status: exact periodic construction, internally proved;
independent hostile review VALID. Falsified as an aperiodic pair.**
No old metric sweep or closed enumeration was resumed. No novelty claim is made.

## Mathematical question and exact object

Can an exactly repeatable nonconvex parent use precisely two convex atomic
classes while neither atomic class permits a monohedral plane tiling?
Yes. This is an existence seed and a counterexample to treating the omission
filter as sufficient; it is not a candidate for the unrestricted target,
because an explicit periodic mixed tiling survives.

Let d=(1/10,49/100), L=Z², and S=L+{0,d,-d}. For s in S, define

    V(s)={x in R² : ||x-s||² <= ||x-t||² for every t in S}.

Define Q=V(0), P=V(d)-d. Their counterclockwise exact vertices are:

    P=((160601/410000,7003/20500),
       (-7601/100000,2499/10000),
       (-12399/100000,-2299/10000),
       (2/5,-3301/9800),
       (167399/410000,-6593/20500));

    Q=((1/2,-1501/9800),
       (1/2,1501/9800),
       (-2399/100000,2601/10000),
       (-201601/410000,863/5125),
       (-1/2,1501/9800),
       (-1/2,-1501/9800),
       (2399/100000,-2601/10000),
       (201601/410000,-863/5125)).

Both are strictly convex, with respectively five and eight genuine vertices;
therefore they are distinct congruence classes, including reflections.
Their areas are

    area(P)=11659735201/40180000000,
    area(Q)=8430264799/20090000000,
    2 area(P)+area(Q)=1.

Every Voronoi cell is an isometric copy of P or Q: translation by L preserves
S, and inversion x -> -x preserves S and maps V(d) to V(-d).
Thus V(-d)=-P-d. Exactly three site orbits become exactly two polygon classes.

## Exact finite Voronoi verification domain

For each of s=0,d,-d, work in local coordinates y=x-s. Same-coset neighbors
s+(±1,0),s+(0,±1) imply y lies in B=[-1/2,1/2]².
For t=n+b, b in {0,d,-d}, n in {-2,-1,0,1,2}², clip B by

    (t-s) dot y <= ||t-s||²/2.

This is a domain of exactly 75 sites for each cell, including the self site,
which supplies no inequality. This finite domain is complete, not a bounded
patch surrogate. If n lies outside it, some coordinate of q=t-s has absolute
value at least 3-98/100 > 2. For every y in B,

    2 q dot y <= |q_x|+|q_y| < q_x²+q_y².

The final strict inequality follows because u²-|u|>2 for one coordinate,
whereas v²-|v|>=-1/4 for the other. Hence every omitted-site constraint is
redundant on B. Exact rational half-plane clipping gives the displayed
coordinates. All consecutive cross products are strictly positive.

## Whole-plane existence and directly repeatable parent

S is discrete and contains Z². Every x in R² has a nearest point of S:
Z² bounds the nearest distance, and only finitely many sites occur within
that bounded distance. Thus the cells V(s) cover the entire plane. Their
interiors are pairwise disjoint because strict nearest-site inequalities
cannot hold simultaneously for different sites. This proves plane existence
without extrapolating finite patches or assuming a substitution.

Set

    C=Q union (P+d) union (-P-d).

The side of Q from q_1 to q_2 lies on the d/0 bisector and coincides with
the side of P+d from its vertex 2 to its vertex 3. The negative side is
shared with -P-d. The remaining boundaries form a simple fourteen-gon C,
with four reflex vertices and area 1. Equivalently, writing p_i for the
listed local P vertices, q_i for the listed Q vertices, and w_i=p_i+d,
its counterclockwise boundary is

    (q_0,q_1,w_4,w_0,w_1,q_2,q_3,q_4,
     q_5,-w_4,-w_0,-w_1,q_6,q_7).

The parent has connected interior, and its two seams are genuine full sides.
Each parent contains 2P+Q, not merely two pieces. This bypasses the elementary
restriction that a union of only two convex pieces has at most two reflex
vertices. No marking is used.

The parents C+n, n in Z², cover the entire plane with disjoint interiors:
their atomic cells partition S into the triples {n,n+d,n-d}. This establishes
pointwise parent compatibility at every lattice location. The parent is
repeatable by translation; no homothetic rep-tile or substitution is claimed.
The atomic tiling and parent tiling have exact periods (1,0) and (0,1).
This defeats aperiodicity decisively even though neither atomic class can
be omitted in a plane tiling.

## Both omission tilings are impossible, including partial contacts

For a strictly convex polygon with CCW edge vectors e_(i-1),e_i, let

    z_i=(-e_(i-1) dot e_i)+i cross(e_(i-1),e_i).

Then z_i has argument equal to the interior angle theta_i in (0,pi).
Multiplication by a positive real number does not change this argument.
Clearing denominators and dividing by the positive gcd gives these primitive
Gaussian-integer phases:

    P: 349+2050i, -151+500i, -51+500i,
       -1501+4900i, -3551+2050i;

    Q: -90+49i, -10+49i, -2399+1000i,
       -3399+4100i, repeated in the same order.

Exact dot/cross inequalities show all P angles exceed pi/3. For example,
if the incoming/outgoing dot product t is nonnegative, cos(theta)<=0;
otherwise 4t²<||e_(i-1)||²||e_i||² implies cos(theta)<1/2.
All Q phases have negative real part, so every Q angle exceeds pi/2.

At a native vertex of a monohedral tiling, local finiteness holds because
there is a positive common inradius and bounded common diameter. At most
one incident tile can contribute a straight edge-interior sector of pi.
Consequently the corner angles of incident tiles sum either to 2pi (no
straight sector), or to pi (one straight sector). This covers unrestricted
partial-edge contacts and both orientations.

For P, a full star has at most five corners and a half star at most two.
For Q, these bounds are three and one. A full-star phase product must be a
positive real number; a half-star phase product must be a negative real
number. The exact finite tests enumerate all count vectors:

    P: k in N^5, 1 <= sum(k) <= 5, exactly 251 vectors;
    Q: k in N^4, 1 <= sum(k) <= 3, exactly 34 vectors.

Repeated Q angles may be combined into these four coordinates without losing
any product. For P the only real product is k=(1,1,1,1,1), with product
-11470481270217401. It cannot form a full star, and its five corners exceed
the two-corner half-star bound. For Q none of the products is real. Thus
neither shape admits any possible native-corner star in a monohedral tiling.
Neither P alone nor Q alone tiles the plane. This uses no imported pentagon
classification and makes no edge-to-edge assumption.

## Concrete period-breaking modification and exact failure

Move just the site d to d'=(1001/10000,49/100), leaving all other S sites
fixed, and call the new set S'. This is a concrete globally defined point-set
modification, not an assumed local extension. S' is still discrete and
relatively dense, so its Voronoi cells still cover the entire plane.

S' has no nonzero translational period. If S'+t=S', then S and S+t differ
only at finitely many points. Their symmetric difference is Z²-periodic,
so a finite difference must be empty. Therefore S+t=S. The nonempty finite
set S symmetric-difference S' would then be t-invariant, impossible for a
nonzero translation.

However the new origin cell Q' is still a strictly convex octagon and is
not centrally symmetric. Its exact coordinates are retained in the
certificate. The first two vertices are

    (1/2,-1501/9800), (1/2,2143143/14000000),

and opposite vertices retain the corresponding unperturbed negative-side
coordinates. In a centrally symmetric eight-gon, all four sums of opposite
vertices must coincide; exact rational comparison disproves this for Q'.
Every original Q is centrally symmetric, whereas every original P has only
five genuine corners. Thus Q' is congruent to neither original shape.
Cells sufficiently far from the defect still include both original P and Q
classes. The modification creates at least a third congruence class, violating
the two-shape gate. It does not give an aperiodic pair.

More generally, finding a nonperiodic arrangement of these SAME exact P,Q
could never repair the pair: the periodic Voronoi arrangement remains an
admitted tiling. A successful successor must change the metric shapes and
remove the periodic carrier, while proving exact two-class closure of the
new globally compatible geometry. No such change is established here.

## Computation, retained evidence, and restart

Producer: [resumed_intrinsic_voronoi_pair.py](../searches/resumed_intrinsic_voronoi_pair.py).
Certificate: [resumed_intrinsic_voronoi_pair.json](../certificates/resumed_intrinsic_voronoi_pair.json).

Replay without changing retained evidence:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_voronoi_pair.py --check research/certificates/resumed_intrinsic_voronoi_pair.json

This is a deterministic singleton construction: one fixed site motif, three
75-site Voronoi domains, one isolated site displacement, and the two stated
complete angle-product domains. Python standard-library Fraction and integer
arithmetic decide all proof-relevant statements. There is no numerical
tolerance, seed, solver, parameter sweep, timeout or incomplete enumeration.
The command completed successfully. Exact coordinates and every real-product
witness are retained. Independent hostile review is [VALID](../reviews/resumed-intrinsic-construction-hostile-review.md); the independent verifier imports no producer.

**Surviving content:** an exact globally repeatable two-class convex (5,8)
covering with both monohedral omissions impossible; an explicit mixed-periodic
escape; an exact third-class obstruction to one specified period-breaking
phason. No unrestricted impossibility theorem or final solution follows.
**Restart condition:** a concrete global metric deformation or different
aperiodic-site mechanism with provable exact two-class closure and no admitted
periodic carrier. Neither further search over this fixed periodic pair nor
repeating the isolated-defect experiment can advance universal forcing.
