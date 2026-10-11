# Complete center-pp / pure-homogeneous-qq periodic escape

Status: **VALID after fresh independent whole-proof hostile review.** See [the complete audit](../reviews/two-homogeneous-center-pure-qq-classification-review.md). This
closes one exact slice of the binary two-run hexagon family, not its parent
family. Both imported positive carriers already have independent VALID reviews.

## Exact theorem and normalization

Angles are in degrees. Fix distinct positive lengths p,q and 0<delta<30.
A(delta) has native side lengths (p,q,p,q,p,q), directions
(0,60+delta,120,180+delta,240,300+delta), and native angles
(H,L,H,L,H,L), H=120+delta,L=120-delta. B is a strictly convex
hexagon with native side lengths (p,p,p,q,q,q), pp angles alpha=beta=120,
and qq angles containing a pure homogeneous slot: one qq native angle is
120 and the other t differs from120. All translations, rotations,
reflections and unrestricted contacts are permitted; species omission is
permitted.

Common scale q to1. Reflection and native reindexing of B normalize its
native angle list to (u,120,120,v,120,t). Rotate B so its first three edge
directions are (0,60,120). Define

    P(t)=1+exp(i60)+exp(i(240-t)),
    rho(t)=arg(P(t)) in(0,90), p=|P(t)|/2.

Actual closure and strict convexity force precisely

    60<t<180, t!=120,
    u=300-rho-t, v=60+rho.

**Theorem. In this exact normalized domain the pair tiles the plane if and
only if**

    rho=60-delta or rho=60+delta
    or rho+t=180-delta or rho+t=180+delta.

**Every tileable pair in this entire center-pp/pure-qq slice admits a doubly
periodic plane tiling.** Equivalently, its shape parameters satisfy

    delta=|60-rho(t)| or delta=|180-rho(t)-t|,
    0<delta<30.

This is an implicit exact trigonometric classification, including all
intersections. It does not assert that a prescribed admitted tiling is
periodic or uses a particular finite carrier.

## Actual native metric, phase and strict convexity

The p unit-chain is 1+exp(i60)+exp(i120)=2exp(i60). Relative to its first
edge, the q unit-chain has directions (0,60,240-t). Thus exact closure
requires its first direction to be 240-rho and requires 2p=|P(t)|.
The actual q directions are

    (240-rho,300-rho,480-rho-t).

For 0<t<180, set phi=240-t in(60,240). Then

    Re P=3/2+cos(phi)>0,
    Im P=sqrt(3)/2+sin(phi)>0.

Therefore P never vanishes and its unique principal phase is in(0,90).
The native side3 direction must follow side2=120 with a strict turn less180;
the displayed 240-rho is in(150,240), and no other lift by360 meets this
constraint. The remaining angles and directions are consequently forced.
There is no independent phase or p branch left to choose.

Direct exact identities give

    p^2=1-(sqrt(3)/2)cos(t-30),
    Im[exp(i(t-120))P(t)]=sqrt(3)(1/2-cos t).

The latter is |P|sin(rho+t-120). Since
-120<rho+t-120<150, its sine has the same sign as its argument.
On 0<t<180, 1/2-cos t has the sign of t-60. Hence the native mixed
angle u is less180 precisely when t>60. All other strict angle constraints
are automatic there: v in(60,150),u>30 and 0<t<180. The six positive
native turns are

    (60,60,120-rho,60,180-t,rho+t-120),

and they sum360. Positive side lengths, exact closure and strictly ordered
once-around edge directions imply strict convexity by the support projection
argument in the independently reviewed same-slot family. Conversely every
parameter in this domain gives that closed strictly convex native B.
The squared-length identity gives p=1 iff cos(t-30)=0, hence iff t=120
on this interval. Thus excluding t120 enforces precisely distinct lengths.
Both pp120 and qq120 pure stars are allowed by the model; neither must
occur. Both AA seam lengths are retained throughout.

## Complete native-star angle arrangement

A trivalent binary star contains either zero or two mixed corners: an odd
number of changes between the two distinct length labels around its three
rays is impossible. Its mixed native angle types are H,L,u,v. Its
homogeneous native types are alpha,beta (pp) and chi=120,psi=t (qq).
Consequently its abstract possible angle multisets are exactly

* a multiset of two mixed types and one homogeneous type: 10*4=40;
* a triple from the pp pair, or from the qq pair: 4+4=8.

This is an overinclusive angle list; the indexed cyclic length tests below
remove incompatible entries. Using coordinate order (constant,delta,t,rho),
the native angle rows are

    H=(120,1,0,0), L=(120,-1,0,0),
    u=(300,0,-1,-1), v=(60,0,0,1),
    alpha=beta=chi=(120,0,0,0), psi=(0,0,1,0).

Subtract360 from each triple sum and divide a nonzero integer row by its
gcd, choosing positive first nonzero entry. The48 types give nine permanent
identities: H+L+alpha/beta/chi, u+v+psi, all four pp triples, and3chi.
There are eleven nonidentity planes. The planes delta0 and t120 are
excluded by hypotheses. The remaining nine are exactly

| Index | Plane |
|---|---|
| 0 | rho=60-delta |
| 1 | rho=60 |
| 2 | rho=60+delta |
| 3 | t=120-2delta |
| 4 | t=120+2delta |
| 5 | rho+t=180-delta |
| 6 | rho+t=180 |
| 7 | rho+t=180+delta |
| 8 | t+2rho=240 |

Every actual point has an active subset of these planes. Its consistent
intersection has rank at most3: an affine system on three variables has
no independent constant-only row when it has a solution. Thus all
130 subsets of size0..3 exhaust the intersections, including every
nongeneric intersection. Rational row-space canonicalization gives31
distinct consistent affine flats. Seven force either delta0 or t120, so
are inadmissible without any metric or numerical filtering. The other24
have exact rational samples in the deliberately larger envelope

    0<delta<30, 0<t<180, t!=120,
    0<rho<90, rho+t>120,

and outside every nonactive plane. A sample is never claimed to satisfy
the nonlinear native phase. Completeness is established in this larger
space; the exact phase is only used for genuine shapes and carrier
transfer, so no metric branch can escape the negative cases.

## Full indexed seam model and exact exclusions

There are twelve indexed native corners: six per species. Both mirror
states of every corner are retained. At positive native corner i, the
outgoing ray is side i at its reference endpoint0, and the incoming ray
is side i-1 at endpoint1. Reflection exchanges these two rays and their
flags. All24 oriented states and their ordered triples are tested.
Retain precisely triples whose angle-sum row belongs to the active flat
row space and whose three cyclic radial length labels match. Identify
only cyclic rotation of the complete oriented star. A point in the exact
active stratum has no further legal angle triple, since its remaining
nonidentity planes are inactive. Native repeated slots, homogeneous stars,
AA seams, both mirrors and arbitrary species ratios are all included.

For each ray shared by native slots x=(species,side) and y, order x,y
lexicographically and retain their endpoint parity px xor py. Its signed
feature is +1 at endpoint0 of the smaller slot and -1 at endpoint1.
For x=y, equal flags give the same unambiguous sign; opposite flags give
feature0 since the two copies are indistinguishable. On moving to the
other end of an actual whole seam, both flags toggle, so the feature
cancels. Let C_s be a star's twelve corner counts and S_s its complete
signed seam vector. Each species tile contributes one of each of its
six indexed corners.

The retained original certificate supplies ten strong rational duals
(W,Y). The read-only synthesis checker independently reconstructs all
4416 indexed star columns across24 strata, every signed seam key and
coefficient, and checks exactly all1548 inequalities in the ten dual
strata:

    W.C_s+Y.S_s >=0 for every legal star,
    sum(W[0:6])<=-1, sum(W[6:12])<=-1.

The excluded record indices are
0,2,7,9,11,12,15,17,19,21. The other14 records have active sets

    {5}, {0}, {0,3}, {4,5}, {3,7}, {0,6}, {2,6},
    {0,4,7,8}, {2,3,5,8}, {1,7}, {1,5}, {7}, {2}, {2,4}.

Each intersects {0,2,5,7}. Exact rational primals in those records are
also checked for reproducibility, but no positive or global conclusion
uses them. This finite classification establishes only the necessary
union of the four displayed planes.

To justify the infinite negative consequence, suppose a shape in one
of the ten dual strata tiled with arbitrary contacts. The independently
reviewed [defect-free hexagon limit](hexagon-limit-and-periodicity.md)
produces an actual admitted trivalent ETE tiling. Either species can
vanish; both per-tile charges remain negative. Select tiles meeting a
square Q_R. Every complete selected star has nonnegative augmented
charge. The signed Y charges cancel between opposite ends of every
interior whole seam. Incomplete stars and unpaired endpoints lie in a
fixed-width boundary band containing O(R) tiles by fixed diameter,
minimum positive area and disjoint interiors. Bounded incidence and
finite rational weights give total selected corner charge at least
-O(R). But the per-tile bounds give charge at most -N, and covering
Q_R requires N=Omega(R^2). This contradiction excludes all unrestricted
tilings in each dual stratum. No actual limiting frequency is assumed.
This is the independently reviewed signed-seam boundary argument in
[the native catalog theorem](branching-hexagon-new-two-run-catalog-slot-classification.md).

Every tileable actual shape therefore lies on a plane with index
0,2,5 or7, as claimed.

## Full positive transfer, with reflections and all domain checks

Use the independently VALID whole-domain
[same-slot](branching-hexagon-two-run-pp-center-periodic-family.md) and
[cross-slot](branching-hexagon-two-run-pp-center-cross-periodic-family.md)
periodic families. Their definitions allow homogeneous qq stars; they
supply actual closed strictly convex faces and flat-torus covers throughout
their strict domains, not just numerical fixtures or rational seam primals.

Reflecting and reindexing B by native side map (2,1,0,5,4,3) and vertex
map (3,2,1,0,5,4) exchanges u/v and chi/psi while preserving pp120/120,
length wordpppqqq and p/q. Rotating its first p side back to0 gives the
same standard native orientation. This is an allowed isometry of B.

| Active plane | Carrier | B normalization | Resulting native angle list |
|---|---|---|---|
| rho=60-delta | same | original chi120,psit | (240+delta-t,120,120,120-delta,120,t) |
| rho=60+delta | same | reflected chit,psi120 | (120+delta,120,120,240-delta-t,t,120) |
| rho+t=180-delta | cross | original chi120,psit | (120+delta,120,120,240-delta-t,120,t) |
| rho+t=180+delta | cross | reflected chit,psi120 | (240+delta-t,120,120,120-delta,t,120) |

The same-slot strict bounds are chi>60-delta,psi>60+delta,
chi,psi<180. In the first row, chi120 automatically satisfies its
bound and u<180 gives t>60+delta. In the second row, psi120 satisfies
its bound and v<180 gives t>60-delta. The cross-slot bounds are
chi>60+delta,psi>60-delta,chi,psi<180. In the third row, chi120
satisfies its bound and v<180 gives t>60-delta. In the fourth row,
psi120 satisfies its bound and u<180 gives t>60+delta. These deductions
use actual strict mixed angles; no additional parameter assumption is
inserted. All upper bounds come from0<t<180 and120<180.

For completeness, the transfer matches the full native edge geometry.
A center-pp B with angles (u,120,120,v,chi,psi), rotated to p directions
(0,60,120), has q directions

    (300-v,480-v-chi,660-v-chi-psi).

Substitution in each row gives exactly the imported carrier's directions:

    same: (60+delta+chi,240+delta,420+delta-psi),
    cross: (60+delta+psi,240+delta+psi-chi,420+delta-chi).

Therefore the actual q unit-chain equals exp(i60) times respectively

    exp(i delta)(exp(i chi)-1+exp(-i psi)),
    exp(i delta)(exp(i psi)-exp(i(psi-chi))+exp(-i chi)).

Actual B closure gives either expression=-2p, which is the imported
family's full complex metric equation. No root is inferred from an angle
multiset, no quadratic branch is selected, and no nonlinear phase domain
is dropped. Because p>0, the carriers' remaining positivity hypothesis
is automatic. A is exactly their A(delta) throughout, so there is no
independent species rescaling or change of delta.

Every actual shape on the four necessary planes thus belongs, after an
allowed B reflection if needed, to an exact periodic carrier domain.
Its four-face or eight-face flat torus supplies a rank2 lattice plane
tiling. Scaling back by q and prototype isometries transfers the complete
tilings. If multiple planes hold, either applicable carrier suffices;
the necessity inventory already included all active intersections.
This proves both directions of the classification.

## Certificates, replay and precise limits

The retained producer/certificate prefix is
`branching-hexagon-two-run-center-pp-pure-qq-strata-slot-balance`, under
`research/searches/` and `research/certificates/`. The source certificate
is unchanged. It enumerates all130 subsets, emits31 flats, seven rejected
flats and24 exact active strata, ten strong rational duals and14 exact
necessary-only primals, with no UNKNOWN. The producer's default solver
limit is10,000ms per call; replay is read-only unless --output is supplied.
The proof relies on the retained rational duals and their exact replay,
not on trusting a solver's UNSAT answer.

The independent-of-producer author synthesis checker is
`research/searches/branching-hexagon-two-run-center-pp-pure-qq-classification-check.py`.
It imports no producer, invokes no solver, performs no floating-point
proof decision and writes no file. It constructs all48 abstract types,
all130 subsets and31 exact row spaces, verifies all seven inadmissible
flats via direct excluded-row membership and each remaining rational
sample's precise active set, exhausts all24^3 indexed oriented triples
per stratum, reconstructs every corner/seam column, verifies the ten
strong duals and14 rational ledgers, verifies every allowed seam's
endpoint cancellation, and checks all four symbolic full direction
transfers and exact phase identities.

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-two-run-center-pp-pure-qq-classification-check.py

Observed deterministic result: PASS48 types;130 subsets/31 flats/24 strata;
4416 oriented stars;1548 strong-dual inequalities;10 exclusions/14
necessary-only primals; seam cancellation; four full native transfers;
exact phase identities. The computation is finite over the stated symbolic
arrangement, not a finite patch search. Sage rational linear algebra and
Python Fraction arithmetic make all proof-relevant tests exact.
Replay environment: Python3.12.13, Sage10.9; retained producer Z34.16.0.
No randomness or symmetry reduction beyond whole-star cyclic rotation is
used. The synthesis replay completed without a timeout; its exhaustive
loops have no per-case time cap.

Dependencies: reviewed fixed-hexagon ETE limit and fixed-shape boundary
estimate; reviewed signed-seam boundary principle; independently VALID
full same/cross periodic carrier theorems. No literature theorem is newly
imported by this synthesis. Its finite arrangement is a new exact slice
classification within the existing repository's narrow candidate family;
no unrestricted impossibility or novelty-priority claim is made.

Other pure homogeneous categories, including noncentral pure pp with
mixed qq or pure qq, remain outside this theorem. Both central arcs force
p=q and are excluded by the distinct-length hypothesis. Closure of this
slice does not close the full A(delta)/Bpppqqq parent family or the
unrestricted two-convex-prototile problem. Fresh hostile review must audit
inventory completeness, row-space/active-stratum completeness, every
retained dual/model row, actual phase lift and strict domain, per-tile
boundary charge with species omission, reflection map, full positive
metric transfer and every exceptional intersection before promotion.
