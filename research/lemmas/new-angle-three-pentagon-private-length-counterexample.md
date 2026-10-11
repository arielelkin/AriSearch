# Three-angle pentagon trial: a mixed periodic escape with irrational private lengths

**Status:** the105-degree and irrational-angle positive periodic witnesses
passed [fresh independent review](../reviews/new-angle-three-pentagon-periodic-review.md).
The bounded mixed-word obstruction is awaiting independent re-review after
repairing its equality-relation count (four stored labelings, three relations). This is a direct counterexample to a proposed
irrational private-length forcing step, not an unrestricted impossibility
result. Both the exact 105-degree witness and an exact irrational-angle extension
are retained with complete geometry and global tiling certificates.

## New narrow angle family and unrestricted necessary system

Choose 90<theta<135 degrees, excluding 112.5 and 120. Each pentagon has two
right corners, two theta corners, and one gamma=360-2theta corner. These
are three distinct angles, all at least 90 and below 180. The angle sum is
2*90+2theta+gamma=540. Avoid adjacent rights, since that would independently
supply the known half-turn periodic escape. There are two possible angle
words up to rotation and reflection:

    X=(90,gamma,90,theta,theta),
    Y=(90,theta,90,theta,gamma).

No edge-to-edge assumption is imposed on a source tiling. At a native
corner there are either full genuine sectors summing 360, or one straight
sector and genuine sectors summing 180. Two straight sectors cannot coexist
with a genuine corner. Since every corner is at least 90, a half star has
exactly two right corners. A full star has 3 or 4 sectors; if 4, all are right.
Enumerating the ten possible three-corner multisets analytically gives the
permanent star(theta,theta,gamma), and additional stars only at theta 112.5
or120. Specifically90+2gamma=360 selects112.5;3theta=360,
theta+2gamma=360 and3gamma=360 select120. The other equations select only
excluded endpoints or no parameter. Thus the complete native sector language
throughout this open family is

    full: (90,90,90,90) or (theta,theta,gamma),
    half: (90,90), together with one straight sector.

This is a finite system proved for a continuum of parameters, with no
rational-angle denominator cutoff. It includes all reflections and partial
contacts. A positive minimum angle prevents any omitted higher valence.

Let N be total tile count in a square-window patch, V4 the number of full
four-right vertices, V3 the number of theta,theta,gamma vertices, and T the
number of half two-right native stars. The fixed-size boundary strip has
only O(R) tiles, hence native-corner counting gives

    V3=N+O(R),    4V4+2T=2N+O(R),
    equivalently 2V4+T=N+O(R).

Both polygons have the same multiplicities, so no rare-type or omission
assumption enters these necessary relations. These relations do not assert
global existence; the following explicit construction supplies it for a
new metric pair.

## Concrete105-degree pair

Set theta=105,gamma=150 and put

    a=(sqrt(6)+sqrt(2))/4,
    b=(sqrt(6)+3sqrt(2))/4,
    c=1+sqrt(3)/2,
    t=1, s=sqrt(5).

In counterclockwise native side order, define

    P=(ct+s/2, at+bs, bt+as, t, t/2+cs),
    Q=(t/2+cs, bt+as, at+bs, s, ct+s/2).

Both have angle word Y=(90,105,90,105,150). Set their starting vertex to
(0,0) and starting side direction to 0. Their consecutive unit side vectors
are

    (1,0),
    ((sqrt(6)-sqrt(2))/4, (sqrt(6)+sqrt(2))/4),
    (-(sqrt(6)+sqrt(2))/4, (sqrt(6)-sqrt(2))/4),
    (-1/2,-sqrt(3)/2),
    (0,-1).

Multiplying these vectors by the stated side lengths and taking successive
partial sums is an exact coordinate definition of P and Q. The vectors close
exactly for both polygons. The unit direction angles are 0,75,165,240,270;
their turns give precisely the stated native angle word. Every length is
positive. The exact verifier also checks that every nonincident native
vertex lies strictly to the left of every directed side, proving genuine
strict convexity without a numerical drawing.

Write six positive labels

    x0=at+bs, x1=t, x2=t/2+cs,
    x3=bt+as, x4=s, x5=ct+s/2.

Then P=(x5,x0,x3,x1,x2),Q=(x2,x3,x0,x4,x5). For t=1,s=sqrt(5), all six
labels are distinct. The four labels x0,x2,x3,x5 are shared; the private
side lengths are x1=1 andx4=sqrt(5), whose ratio is irrational. Each shape
separately has five distinct side lengths. The two polygons are not
congruent. Their unique gamma corner fixes any possible cyclic angle-word
isomorphism, and its neighboring angles90 andtheta exclude reversal;
congruence would therefore preserve native side indices. Native side3 has
different lengths t ands.

Neither shape has consecutive angles summing 180. Thus this witness does
not obtain its periodic escape from the earlier adjacent-angle construction.

## Full mixed torus with actual endpoint identifications

Take counterclockwise faces 0=P0,1=P1,2=Q0,3=Q1, using the same reference
word Y for every face. No reference copy is reflected. Native side j runs
from corner j to corner j+1 modulo 5. Pair the following ten sides, always
reversing boundary endpoint order:

| first side | second side | length |
| --- | --- | --- |
| (0,0) | (2,4) | x5 |
| (0,2) | (2,1) | x3 |
| (1,0) | (3,4) | x5 |
| (1,2) | (3,1) | x3 |
| (2,0) | (1,4) | x2 |
| (2,2) | (1,1) | x0 |
| (3,0) | (0,4) | x2 |
| (3,2) | (0,1) | x0 |
| (0,3) | (1,3) | t |
| (2,3) | (3,3) | s |

All twenty sides occur exactly once, with equal actual lengths on both
sides of every seam. Reversed-endpoint identification yields exactly:

    {(0,0),(1,0),(2,0),(3,0)},
    {(0,2),(1,2),(2,2),(3,2)},
    {(0,1),(2,4),(3,3)},
    {(0,3),(1,4),(2,1)},
    {(0,4),(1,3),(3,1)},
    {(1,1),(2,3),(3,4)}.

Each right class has a four-sector cyclic link and sum 360. Each other
class has a three-sector cyclic link and angles105,105,150, again sum 360.
The exact certificate records all twenty individual seam endpoint pairs,
not merely these desired stars. Face adjacency is connected, boundary
orientations are reversed, and V-E+F=6-10+4=0. Therefore this is a connected
orientable torus, with the intrinsic Euclidean metric of its polygon faces
and no cone singularities.

Its compact flat metric is complete. The universal cover is a complete
simply connected flat surface and hence the Euclidean plane; developing
its cells gives a genuine full plane tiling with disjoint interiors by the
original P and Q. Every deck transformation preserves orientation and acts
freely, so each nonidentity one is a translation, since nontrivial Euclidean
rotations have fixed points. The discrete cocompact deck group is rank-two,
giving two independent periods. There are two copies of each prototile per
fundamental torus. This verifies global extendability and periodicity,
without a substitution conjecture or inference from local stars alone.

## Exact failure of the proposed forcing step

The attempted new mechanism used the three-angle language to separate
four-right nodes from three-sector nodes, then gave the two otherwise
compatible metric species irrationally related private edges. Those
private edges force equal-type seams; the four distinct shared lengths
force the indicated mixed matches. The candidate forcing step was that
these private seams would force incompatible irrational spacings around
any finite translational domain.

The displayed exact four-face torus falsifies that step for this explicit
metric ansatz, even with both species occurring. Irrational private lengths
need not be commensurate: the planar lattice generators can themselves
contain both irrational contributions. This particular candidate is
therefore not aperiodic. The same105 construction closes for every t,s>0,
so replacing sqrt(5) by another positive irrational parameter within this
ansatz cannot repair the attempted forcing.

## The distinct-word four-face trial and its narrow obstruction

Before the Y/Y metric construction, I tried two copies of X=(90,150,90,105,105)
and two copies of Y=(90,105,90,105,150), with independently reflected copies.
For this trial, every edge connects right/nonright or nonright/nonright;
there are eight edges of each right/nonright orientation and four
nonright/nonright edges. A full-star seam must match a right endpoint to a
right endpoint. Hence all four-face ETE endpoint matchings are covered by
8 reflection assignments *3 nonright-edge pairings *8! right-edge bijections
=967,680 cases. Fixing one P reference orientation loses no model because
global reflection is allowed.

There are eight flat angle models, with four stored native-side partition
labelings representing three distinct equality relations. Two labelings
represent the same relation by interchanging their class labels0 and1;
their matrices are column permutations. That relation has zero-dimensional
closure nullspace. The other two relations each have a one-dimensional
nullspace with the common native side3 length forced zero. Thus no positive metric realization
exists for this four-face X/Y ansatz. The retained matrices/nullspaces and
model tables are in the certificates below.

This bounded statement eliminates only the declared four-face ETE ansatz.
It does not exclude larger quotients, a nonperiodic plane tiling, or tilings
with permitted right-corner T contacts for any general X/Y pair. No absence
of a bounded torus is promoted to aperiodicity. The X/Y ansatz is blocked;
reopening needs a concrete different global gluing or a different geometry,
not merely an increase in search bounds. The Y/Y change above produces a
fully global counterexample and ends its irrational private-length route.

## Irrational-angle extension of the same global seam mechanism

The 105-degree witness is not dependent on rational angles. For any real
90<theta<135, put k=-cos(theta)>0 and h=sin(theta)>0, and define

    a=h, b=(1-2k^2)/(2k), c=h/(2k).

Since k^2<1/2, all three coefficients are positive. With the same formulas
for P,Q and arbitrary t,s>0, the consecutive unit vectors become

    (1,0), (k,h), (-h,k), (-2kh,2k^2-1), (0,-1).

Their directions are0,180-theta,270-theta,450-2theta,270 degrees; the
strict positive turns give exactly Y=(90,theta,90,theta,360-2theta).
Write x0,...,x5 as before. The two closure pairs are exactly

    x5+k*x0-h*x3-2k*h*t=0,
    h*x0+k*x3+(2k^2-1)*t-x2=0,
    x2+k*x3-h*x0-2k*h*s=0,
    h*x3+k*x0+(2k^2-1)*s-x5=0.

They follow by substitution and k^2+h^2=1. Every edge length is positive.
A positive closed edge chain with strictly cyclic directions and all turns
between 0 and 180 is a genuine convex polygon: for each fixed directed side,
perpendicular vertex heights increase through the following open semicircle
of directions and decrease thereafter to the zero height at closure. All
nonincident vertices therefore have strictly positive height. Thus the
metric pair exists throughout this continuum.

The ten seams and six corner classes above remain valid: actual paired
lengths are equal and each nonright star has theta+theta+(360-2theta)=360.
The flat torus gives a doubly periodic tiling for every t,s>0. No rational
angle or orientation-group assumption enters that global construction.

In particular choose

    theta=arccos(-2/5), gamma=2pi-2theta,
    a=sqrt(21)/5, b=17/20, c=sqrt(21)/4,
    t=1, s=sqrt(5).

Here the angle formula is in radians. Since0<2/5<sqrt(2)/2, theta lies
strictly between pi/2 and 3pi/4. It is not 2pi/3 because its cosine is not
-1/2. It is not 5pi/8 (112.5 degrees): the exact cosine formula gives
cos(4theta)=8(2/5)^4-8(2/5)^2+1=-47/625, whereas cos(4*5pi/8)=0.
Thus this is in the three-angle two-star family above.

The angle theta/pi is irrational, by an elementary monic argument. If
zeta=exp(i*theta) were a root of unity, then x=zeta+zeta^(-1)=2cos(theta)
would satisfy a monic integer polynomial. Indeed the recursively defined
C0=2,C1=x,Cn=x*C(n-1)-C(n-2) have integer coefficients, Cn is monic for
n>=1, and for a root of unity of ordern the valueCn(x)=2. A rational root
of a monic integer polynomial is an integer. Here x=-4/5 is rational and
nonintegral, a contradiction. Therefore theta/pi is irrational, and so is
gamma/pi=2-2theta/pi.

The exact native unit vectors for this instance are

    (1,0), (2/5,sqrt(21)/5), (-sqrt(21)/5,2/5),
    (-4sqrt(21)/25,-17/25), (0,-1).

The separate exact verifier computes in Q(sqrt(5),sqrt(21)), checks all
closure coordinates, actual native angle cosines, strict convex support,
six distinct positive length labels, equal seams and the full vertex links.
The native angle cosines are0,-2/5,0,-2/5,-17/25, consistent with the
specified angle word. The references remain unreflected.

This second exact pair also has private lengths 1 and sqrt(5), both species
occur in its periodic tiling, and now two of its three native angle values
are irrational multiples ofpi. Its polygon areas are

    area(P)=101sqrt(21)/100+861sqrt(5)/400,
    area(Q)=151sqrt(21)/100+861sqrt(5)/400.

Their ratio is irrational: a rational ratio r would separately force
101-151r=0 and1-r=0, since sqrt(21)/sqrt(5) is irrational, which is
impossible. Thus neither irrational angles, irrational private side ratio,
nor irrational area ratio supplies a period obstruction for this explicit
family. The conclusion is a counterexample to those forcing shortcuts;
it does not assert that other irrational-angle pairs are periodic.

## Both private lengths individually irrational

The displayed normalization has private lengths 1 and sqrt(5), with an
irrational ratio. If both private lengths themselves are required to be
irrational, take the exact uniformly scaled polygons

    P*=sqrt(2) P, Q*=sqrt(2) Q.

Their private lengths are sqrt(2) and sqrt(10), respectively, both
irrational, with ratio sqrt(5). Their native angles are unchanged, including
theta/pi and gamma/pi irrational. Uniform scaling preserves strict
convexity, the two distinct congruence classes, every seam, interior
disjointness and full-plane covering. The private lengths remain absent
from the other shape. The polygon-area ratio also remains irrational.

For this literal both-lengths-irrational version, an exact period basis is

    u=(4sqrt(42)/25, sqrt(210)/2+42sqrt(2)/25),
    v=(17sqrt(42)/50+42sqrt(10)/25, -33sqrt(210)/50-42sqrt(2)/25).

Its determinant has absolute value

    252sqrt(21)/25+861sqrt(5)/50=2 area(P*)+2 area(Q*).

The [independent coordinate-and-overlap verifier](../reviews/verify_three_angle_pentagon_periodic_independent.py)
now develops and checks both scaled prototypes directly, checks the whole
complete 48-comparison overlap domain again, and verifies that the lattice,
motif coordinates and areas are exactly the uniform scalings of the
unscaled data. The [fresh dated replay audit](../reviews/new-angle-three-pentagon-periodic-review.md)
records these checks. This supplies a periodic counterexample even with
both private lengths individually irrational; it does not classify other
three-angle pairs.

## Replay and remaining scope

Primary witness verifier and certificate:

    research/searches/new-angle-three-pentagon-counterexample-verify.py
    research/certificates/new-angle-three-pentagon-counterexample.json

The irrational-angle extension has its separate replay artifacts:

    research/searches/new-angle-three-pentagon-irrational-angle-verify.py
    research/certificates/new-angle-three-pentagon-irrational-angle.json

The 105-degree verifier uses exact arithmetic in Q(sqrt(2),sqrt(3),sqrt(5)), and strict
rational radical intervals for positivity and convexity. It also verifies
the entire analytic affine-star system, actual length matches, vertex links,
face connectivity and Euler characteristic. The global flat-cover argument
is proved in the text rather than certified by numerical coordinates alone.

The mixed-word trial has replayable exhaustive generator and exact closure
certificates at:

    research/searches/new-angle-three-pentagon-explore.py
    research/certificates/new-angle-three-pentagon-mixed-word-angle-models.json
    research/certificates/new-angle-three-pentagon-mixed-word-closure.json

The additional small exact rank checker and its retained certificate are:

    research/searches/new-angle-three-pentagon-mixed-word-verify.py
    research/certificates/new-angle-three-pentagon-mixed-word-rank.json

Its floating-point linear programming was only an initial screen. The
retained radical nullspaces, not solver infeasibility, establish the stated
finite-ansatz obstruction. See the accompanying subject-specific search
record for the exact domains, versions, runtimes and replay commands.

These new results do not classify arbitrary three-angle pentagon pairs and
do not supply an aperiodic pair. The general metric/gluing branch outside
the explicit failed ansatz remains unresolved.
