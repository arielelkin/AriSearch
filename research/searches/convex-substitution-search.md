# Convex two-tile self-similar substitution: inverse search

**Status:** completed bounded exact searches plus three internal lemmas; not
independently reviewed. **No candidate passed the first gate** (an exact
homothetic dissection of both lambda*A and lambda*B into copies of A, B), so
kill tests (1)-(3) on a surviving substitution were never reached. Nothing here
is an aperiodicity claim, and the negative results are restricted to the exact
domains stated below.

## Question

Find convex A, B (neither tiling alone; pair types (5,5), (5,6), (5,n>=7)) and
lambda>1 with lambda*A, lambda*B each partitioned into isometric copies of A, B
(reflections, partial contacts, T-junctions allowed), substitution matrix M
nonnegative integer with Perron root lambda^2 irrational. Earlier repo work
excluded homothetic substitution for the area-compatible golden U/V family with
c/b not in Q(sqrt5) ([lemma](../lemmas/pentagrid-generic-metric-substitution-obstruction.md));
this record does not repeat that.

## Tools (all exact)

* [`convex-substitution-core.py`](convex-substitution-core.py): angles in units
  pi/N (N = 4, 5, 6), sides in Z[w] (w = sqrt2, phi, sqrt3); points stored as
  integer 4-tuples (2Re, Im/sin(pi/5)) or (2Re, 2Im); every sign is an exact
  sign of a+b*w. No float enters a decision (floats only print and, in the
  wedge test, order choices and record radii).
* **Complete corner-filling dissection search** (`Dissector`). All child sides
  lie in 2N directions, so each point has 2N basic sectors; masks record
  coverage exactly (corner sectors, half-planes at side interiors, parent
  exterior). The uncovered part of the parent, if nonempty, has a convex
  corner at a tracked point whose free sector is a run of m<N zero bits starting
  at direction a; the child covering the region just counterclockwise of ray a
  contains that point, cannot use the covered bits a-1, a+m, hence has a
  corner there with outgoing side direction a and angle <= m. Branching over
  these children is therefore exhaustive. Interior-disjointness: exact
  separating-axis test over the N side normals; containment: exact half-planes.
  With counts fixed by the area eigen-relation, a leaf with all counts used is
  a full partition. A node limit is reported as UNKNOWN, never as negative.
  Controls: Robinson phi*T = 2T+G (4 placements found), phi*G = T+G, the
  pentaflake phi^2*P = 6P+5T (found), a 3x2 brick parallelogram with T-junctions
  (11 found), equilateral 2x, square 2x, sqrt3 30-60-90 and sqrt2 isosceles
  rep-tiles (found). An alternative branching rule (`choose_mode="max"`) is
  provided for cross-checks; its sampled re-run was interrupted and is not
  claimed.
* **Local wedge obstruction** (`wedge_test`, new): parent = huge
  parallelogram with apex angle alpha, unlimited child counts, points chosen
  nearest the apex. If the finite search tree dies with every placed vertex
  within maxd of the apex, then **every** convex parent whose corner of angle
  alpha agrees with the wedge inside radius R* = maxd + max diameter(A,B) has no
  partition into copies of A, B: the same exact choices, options and prunings
  occur (fewer options with finite counts). For lambda*X the corner agrees with
  the wedge inside radius lambda*h, h = distance from the corner to the chord of
  its two neighbours; so lambda*X is impossible for lambda > R*/h, for **all**
  such lambda at once. Controls: Penrose rhombs fill a 36-degree wedge
  (status "radius" in 46 nodes); Robinson T,G never report "dead"
  (node limit). Small lambda: lambda is forced into Z[w] (side sums, integrality
  of lambda^2), |lambda'| < lambda (Perron), and lambda^2*area(X) =
  m_self*area(X) + m_other*area(O); finitely many, each run exactly.

## Killed families and witnesses

| # | Family | Kill | Witness |
|---|---|---|---|
| K1 | (hexagon, hexagon) and (hexagon, n>=7), any angles/lengths | no homothetic substitution | Euler identity sum(6-n_T) = 6-p+V_b+V_T+2X ([lemma](../lemmas/convex-substitution-dissection-euler.md) items 1-2): a hexagon is not a union of >=2 convex polygons with >=6 sides |
| K2 | lambda = phi (lambda^2 = phi^2), any (5,5) or (5,6) pair | impossible | M in {[[1,1],[1,2]],[[2,1],[1,1]]} gives a pentagon parent 2 or 3 children; lemma item 3: a convex pentagon needs >=5 pieces with 5 or 6 sides |
| K3 | all angles in multiples of pi/4 (Ammann-Beenker angle family) | every convex pentagon tiles alone (type 1); only (6,6) left, dead by K1 | lemma item 4; driver prints empty word list |
| K4 | pi/5 pentagon words other than U=(1,3,4,4,3), V=(2,2,4,3,4), W=(3^5) | tile alone (adjacent supplementary pair => Rao type 1) | 13 cyclic words enumerated, 3 survive (matches the reviewed angular reduction) |
| K5 | hexagon B = union of two copies of A/lambda (one straight cut) | requires two distinct equal sides of A whose endpoint angles are complementary (same side => adjacent supplementary or two right angles => type 1); no U, V, W side pair qualifies | side endpoint pairs U:(1,3),(3,4),(4,4),(4,3),(3,1); V:(2,2),(2,4),(4,3),(3,4),(4,2); W:(3,3) |
| K6 | **golden U/V b=c=1** (U=(phi^3,phi^3,1,1,1), V=(1,3phi+1,1,2phi,2phi)) | **no homothetic substitution for any lambda** | wedge tests at 36,72,108,144 degrees all "dead" (5, 57, 187, 1886 nodes; R* <= 16.95); U tip h = 4.0287, so lambda*U impossible for lambda > 3.958; the five remaining lambda (phi, 2phi, 1+phi, 2+phi, -1+3phi) fail by the complete search ([certificate](../certificates/convex-substitution-uv-golden-wedge.json), [runs](../certificates/convex-substitution-uv-golden.json)) |
| K7 | same pair, the repo's open 13-piece phi^3 question (Z3 timeout in [phi3-macro](pentagrid-golden-metric-phi3-macro.md)) | U parent: **no partition** (5 nodes, exhausted); V parent (8U+13V): none (6 nodes) | uv-golden runs list every p+q*phi with a+d <= 80: all U parents die in <=5 nodes |
| K8 | pi/5 U/V/W pentagon pairs, free sides from {1,phi,phi^2,2,1/phi} (x2), 137 shapes, 4692 pairs meeting the area condition | **all lambda excluded** | [wedge-domain certificate](../certificates/convex-substitution-wedge-domain-small.json) |
| K9 | pi/5 U/V/W pentagon pairs, free sides from the 10-value alphabet {1,phi,phi^2,2,phi^3,2+phi,2phi,2phi^2,1/phi,1/phi^2} (x2): 1032 shapes, 262,535 pairs meeting the area condition | **all lambda excluded** (every pair: a dead wedge in some parent and every small lambda exhausted, no node limit) | [certificate](../certificates/convex-substitution-wedge-domain-big.json) (domain shapes + the empty list of non-excluded pairs) |
| K10 | bounded lambda lists (exhaustive per record, node limit never hit) | no lambda*A partition for any record | N=5 pentagons: 4431 records; N=5 heptagon partners: 171,456; N=6 pentagons: 15,048; N=5 hexagon partners: 288,751 of 512,042 records processed before an interruption, all negative ([certificates](../certificates/)) |

Area condition used in K8/K9 (exact, new observation): for an irrational area
ratio r = area(B)/area(A) in a real quadratic field, some nonnegative integer M
with eigenvector (1, r) exists iff r > 0 and its conjugate r' < 0
(r is a root of m21 x^2 + (m11-m22) x - m12 with m21, m12 >= 1).

## What the bounded lambda-list runs cover (K10)

Driver [`convex-substitution-pentagrid.py`](convex-substitution-pentagrid.py)
(N=5) and [`convex-substitution-cyclotomic.py`](convex-substitution-cyclotomic.py)
(N=4,5,6): A pentagon with a non-type-1 word, B a pentagon / hexagon /
heptagon; free sides from fixed Z[w] alphabets (listed in the scripts),
sides 0,1 solved exactly; filters: Rao Table 2 (copied from the reviewed
filter), Reinhardt types (conservative: type 2 tested under two side-label
conventions, which can only remove extra hexagons), exact area eigen-relation,
whole-side boundary knapsack, angle fill; lambda in {phi, phi^2, 2phi, 2+phi,
phi^3} (N=5) or {1+r3, 2+r3, 3+r3, 2+2r3, 1+2r3} (N=6); all M with <= 20
children per parent. Every record died at the lambda*A parent, mostly within
2-30 nodes (histograms in the certificates). The N=6 pentagon+hexagon run
(174,663 records after filters) was interrupted before any record was
processed and is **not** claimed.

## Big-alphabet wedge run

`CS_ALPHABET=big` finished: 262,535 of 262,535 pairs excluded for all lambda
(1248 s, 7 processes). For each pair, each parent is tried in turn. Wedge tests
start at the smallest corner angle and stop at the first `dead` one (node limit
20,000). Then every small lambda allowed by the area relation gets an exact
search (node limit 200,000). A pair counts as excluded only when, for one
parent, a wedge is `dead` and every small-lambda run exhausts with no partition.
The certificate keeps only the non-excluded pairs, and there are none.

**Interrupted, not claimed:** the same classifier with (pentagon, hexagon)
partners (`CS_HEX=tiny`, 1739 shapes, 114,583 pairs) was stopped on the root's
instruction before it finished. Its status is UNKNOWN. The N=6 wedge
classification was never started.

## Angle-incidence relaxation (recorded as too weak)

[`convex-substitution-angle-ilp.py`](convex-substitution-angle-ilp.py) encodes
corner counts and Euler (F) for a dissection as a CP-SAT model. It admits,
e.g., V -> 2V, so it is not used as a filter.

## What is proved and what is not

Proved (internal, unreviewed; lemmas: [Euler](../lemmas/convex-substitution-dissection-euler.md), [wedge](../lemmas/convex-substitution-wedge-obstruction.md), [golden U/V all-lambda](../lemmas/convex-substitution-golden-uv-all-lambda.md)): K1-K5; K6 (all lambda) and K8 as exact
finite computations plus the wedge-localisation argument above; K7 and K10 as
exact complete searches within their stated domains. Not proved: anything
about lengths outside the alphabets (rigid solutions with large coefficients
are not sampled), lambda outside the lists in K10, non-homothetic or compound
substitutions, angle systems other than pi/4, pi/5, pi/6, or any plane-tiling
statement. The wedge "dead" results say U,V-type shapes cannot fill large
convex corners; they do not exclude plane tilings.

## Route status and the one proposed mechanism (not run)

On the root's decision the route is **closed**: no further enlargement of the
alphabet, angle unit or length ring. Every exact computation started here is
either complete (K6-K10, with K10's hexagon run counted only for its 288,751
processed records) or recorded above as interrupted/UNKNOWN.

Proposed non-alphabet mechanism, with a concrete first gate (not executed):
a **length-parametric wedge test**. Fix the angle words of A and B. Treat all
free side lengths as positive unknowns; vertex positions are then linear in
them over Z[w]. Run the corner-filling search near a single corner. At each
placement, branch on the order of the new child's side endpoints along the two
rays bounding the gap (<, =, >) and on the separating axis for each nearby
child. Keep feasibility with an exact LP over Q(w).
First gate: for the U/V words (where the alphabet results above all die at a
corner), decide whether the 36-degree U-tip wedge is `dead` for **all**
positive U/V lengths simultaneously. If it is, then together with the
small-lambda bound this would exclude homothetic U/V substitutions for every
metric, including the open c/b in Q(sqrt5) members. If some length region
survives, its defining equalities give exact rigid candidates for the ordinary
exact search.

## Replay

```text
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-uv-golden.py --maxc 80
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-uv-golden-wedge.py
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-wedge-domain.py
CS_ALPHABET=big conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-wedge-domain.py
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-pentagrid.py --nodes 20000
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-pentagrid.py --hexagons --nodes 20000
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-cyclotomic.py --N 6 --nodes 20000
conda run --no-capture-output -n arisearch python3 research/searches/convex-substitution-cyclotomic.py --N 5 --heptagons --nodes 20000
```

The hexagon-partner variant is `CS_HEX=tiny ...wedge-domain.py` (interrupted). Add `--output FILE` to save; `--compact` keeps only found/limit records. No
random seeds; CP-SAT is used only in the discarded relaxation.
