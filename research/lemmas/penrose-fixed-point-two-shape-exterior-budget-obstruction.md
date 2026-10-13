# Fixed marked-Penrose points require more exterior-angle budget than two convex polygons possess

Date: 2026-10-13. Status: **proved by exact finite certificate and internally checked; fresh hostile review pending**. This supersedes the side-count restriction of the [14-value palette gate](penrose-dual-single-fusion-deformation-gate.md) on exactly the same fixed point-preserving compiler domain. It excludes all partner side counts in that domain, not arbitrary two convex shapes.

## General reusable angle-budget lemma

Let C be any set of distinct native interior angles which two genuine convex polygons A,B must collectively possess. Polygon vertex lists are written after deleting collinear subdivisions, so all native angles lie strictly between0 andpi. Then

    sum_(alpha in C) (pi-alpha) <=4pi.

Proof. The exterior angles pi-alpha at all native vertices of one convex polygon sum to2pi and are positive. For each distinct required value alpha select one native occurrence among A,B. Distinct values select distinct occurrences. Their positive exterior-angle sum is at most the sum over all native occurrences of both polygons, namely4pi. Repeated angles, arbitrary rotations/reflections, unused corners and omission of a tile type cannot increase this budget. QED.

A flat sector pi at a contact is not a native angle and contributes zero, so allowing and ignoring such sectors is a valid relaxation. The lemma has no bound on polygon side counts.

## Exact fixed compiler domain

Use [the retained source fixture](../certificates/penrose-centered-dual-single-fusion-source.json), an exact three-deflation marked Robinson/Penrose rhomb patch. Put one point inside each rhomb: thick points are rhomb centers, thin points are center+(1/100)*w^a, where w=exp(i*pi/5) and a is its marked frame rotation. Original network edges connect points across common source edges. All internal connections cross that source edge strictly inside both segments; every point is strictly inside its rhomb.

Consider any final polygon tiling obtainable by deleting original network edges, with these hypotheses:

* all35 rhomb points surrounded by all four rhomb neighbors in the fixture remain network vertices of degree3 or4;
* no extra edges, new graph nodes or fractional cuts change their incident rays;
* the final face closures are genuine convex polygons drawn from two unmarked congruence classes.

Flat pi sectors are allowed and need not be polygon corners. Source-point degree2 collapse/elimination is outside the claim; the recorded point data have some exactly opposite rays, so this exception must not be silently discarded. No global matching or pairwise-cluster condition is assumed: arbitrarily many original dual faces may be joined by deleted edges.

## Finite question and outcomes

At each of the35 points, enumerate every subset of3 or4 original rays. Their cyclic order is the order of the source rhomb edges, because point placement and crossings are strict. Reject a subset with a consecutive sector exceedingpi. For each surviving subset record its distinct sector values in(0,pi), ignoring pi sectors.

Any proposed two-shape compiler must select one such local option at every point. Let C be the union of required nonflat angle values. The exact finite question is whether every possible C has exterior budget exceeding720 degrees. A negative budget certificate excludes the fixed compiler for all side counts. A surviving union would be only a local necessary condition and would not justify increasing the source patch.

There are26 distinct exact algebraic unit values z_alpha=exp(i*alpha) and six distinct local-choice signatures among the35 points. Their numbers of choices are4,3,3,3,4,3. Consequently exactly1296 products suffice; repeated point signatures cannot improve the optimum, because every repeated point must satisfy the same local constraint.

## Exact integer budget certificate

For each of the26 native angle values, the retained certificate gives the integer d=floor(180-alpha) in degrees. The26 values, in retained angle-ID order, are

    71,108,54,53,126,125,72,18,35,17,107,89,16,
    72,90,18,15,56,106,107,54,53,72,51,20,109.

These are certified algebraically. Since alpha lies in(0,pi), delta=pi-alpha lies in(0,pi); cosine is strictly decreasing on that interval and cos(delta)=-Re(z_alpha). Thus

    d <= delta_degrees < d+1

is equivalent to

    -Re(z_alpha) <= cos(d*pi/180),
    -Re(z_alpha) >  cos((d+1)*pi/180).

The thresholds are exact real parts of powers of exp(i*pi/180), a360th root of unity. Both comparisons use exact algebraic-real arithmetic. Floating values only propose the producer's integer candidates; the independent budget verifier reads those candidates and checks them without floating arithmetic.

For each of the1296 products form the set C of required angle IDs and sum its integer lower bounds d. The smallest such sum is **837 degrees**, attained by

    C={0,2,3,5,7,8,10,12,13,14,16,17,20,23,24}.

The certificate retains the entire histogram of1296 integer costs; the independent checker reproduces it. Every actual sum of exterior angles is at least its certified integer lower bound, so every C needs at least837 degrees, strictly more than the720 degrees available from any two convex polygons. The general budget lemma therefore contradicts the existence of every two-shape final compiler satisfying the fixed-domain hypotheses.

This bound uses neither CP-SAT nor a numerical angle estimate as a proof. It also uses no inference that matching deletions can fuse only two cells.

## Proposition: an open thin-point deformation interval is excluded

The same degree3/4 point-preserving two-shape compiler is impossible not just at tau0=1/100 but throughout some open real interval I containing tau0, within the symbolic family

    thin p_r(tau)=center_r+tau*w^a,
    thick p_r(tau)=center_r.

This is an existential open-interval statement, not coverage of the entire thin-point family. No additional parameter sample or enlarged source patch is used. Status: **internally proved continuity consequence of the finite certificate; fresh hostile review pending**.

Proof. Only finitely many rhomb points, connections, retained-ray subsets and their sector functions occur in the fixed fixture. Strict point-interior and source-edge-crossing inequalities hold at tau0 and persist on a common open interval around tau0. Thus all local radial orders remain the source-edge orders. Any size3/4 ray subset rejected at tau0 has a gap strictly larger thanpi, or a degenerate zero sector. Distinct adjacent rays hold at tau0 by strict source-edge crossings; the rejected positive reflex gaps therefore persist. After shrinking the common interval, every subset admissible at a nearby tau was already included in the tau0 relaxed admissible list. A gap equal topi at tau0 was allowed in that list, so its possible opening into an admissible corner nearby creates no omitted choice.

For each positive sector at tau0, label its value by one of the26 distinct exact angle classesj. Its angle and exterior deficit vary continuously while the endpoints remain distinct. At tau0 its deficit is at least the certified integerd_j; hence, after shrinking the interval, every sector with that label has deficit strictly greater than d_j-1 degrees. Angles belonging to different tau0 classes are unequal at tau0. Their finitely many continuous representatives stay in pairwise disjoint small neighborhoods after another common shrinking. Thus distinct old class labels cannot become one new native angle value; an old class may split, which can only increase the native-angle budget requirement.

Choose any actual admissible local choices in the nearby compiler. Regard those same choices at tau0, and let C be the old positive-sector class union. For each j inC, at least one actual native corner value carries that label. Values selected for distinct labels remain distinct. Their exterior sum is therefore strictly greater than

    sum_(j in C)(d_j-1)
    =sum_(j in C)d_j-|C|
    >=837-26=811 degrees.

New positive sectors arising from formerly flatpi gaps can be ignored: their exterior deficits are nonnegative and ignoring them only weakens the lower bound. The811-degree bound exceeds the720-degree exterior budget of any two convex polygons. Contradiction. QED.

One can define a concrete algebraic endpoint bound by isolating the finite critical roots where a point reaches a source side, a crossing reaches an edge endpoint, a rejected gap reachespi, an old class representative leaves its chosen separating neighborhood, or an exterior deficit reaches d_j-1. The present proposition only asserts existence of the common positive interval; it does not supply a numerical epsilon or classify parameter values outside I. Collapse of degree2 rhomb points remains outside this proposition's degree3/4 hypothesis. The subsequent [straight-collapse shared-edge obstruction](penrose-dual-straight-collapse-shared-edge-obstruction.md) includes that changed hypothesis and proves a750-degree contradiction, also on an open interval.

## Scope and programme consequence

The previously surviving local pentagon remains a genuine exact convex polygon outside the known monohedral pentagon families. The exterior-budget result explains why that local success cannot extend through the fixed point-preserving compiler even with an arbitrarily high-sided second shape. It closes that concrete compiler, rather than the entire pentagon-containing construction track.

Material ways to change the used hypotheses include degree2 collapse/elimination of rhomb points, new graph nodes or cuts, changed exact interior points, or a different source/derivation. A new proposal must identify which exact local constraints or angle deficits it changes. Merely collecting larger patches or more center-fusion examples does not evade this obstruction.

## Artifacts and nondestructive replay

* [Palette certificate](../certificates/penrose-dual-fusion-angle-palette.json): all35 local point choices and26 exact unit-angle representatives.
* [Exterior-budget certificate](../certificates/penrose-dual-fusion-exterior-budget.json):26 exact integer floors,1296 cost histogram and minimum witness.
* [Budget producer](../searches/penrose-dual-fusion-exterior-budget.py): no source enlargement; floats guide candidates only.
* [Independent geometry/palette checker](../reviews/check_penrose_dual_fusion_angle_palette.py): reconstructs coordinates, point interior, edge crossings, exact angle values and all local choices without producer imports or solver calls.
* [Independent budget checker](../reviews/check_penrose_dual_fusion_exterior_budget.py): uses that geometric reconstruction, certifies all cosine inequalities without floats and replays1296 integer-cost products.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_fusion_exterior_budget.py

External hostile review of the geometric model, degree3/4 scope, exact phase comparisons, integer bounds and budget lemma is still required. No novelty claim or global two-tile result is asserted.
