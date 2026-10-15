# Fresh research direction: 11:30 UTC, 2026-10-15

The unrestricted two-convex-polygon problem remains **unresolved**. This cycle proposed new interior-cycle construction gates, executed their strict-geometry and necessary-angle tests, and rejected every tested two-class incidence before metric search. No discovery-log, registry, or Git edits were made. The new computations below are internally checked reconnaissance, not independently reviewed theorems.

## Tested central-cycle hat partition: strict precursor exists, angle gate fails

Use the thirteen genuine vertices h0,...,h12 of Tile(1,2), in the indexing of [the existing exact hat producer](source-decoration-hat-patch.py). More explicitly, start from its Tile(1,sqrt3) outline, replace each edge of squared length3 by2/sqrt3 times that vector, retain the other edge vectors, and cumulatively sum starting at h0=(0,0). The source polygon closes exactly over Q(sqrt3). Its positive source parameters are fixed; this is not a search over source ratios.

Put

    W=(h1+h2)/2, U=(h5+h6)/2.

Choose six interior vertices z0,...,z5, cyclically ordered. The CENTRAL hexagon is

    Qc=[z0,z1,z2,z3,z4,z5].

Join its vertices to the six boundary points h0,W,h4,U,h8,h11 respectively. The six outer pieces, in cyclic order, are

    P0=[h0,h1,W,z1,z0],
    Q1=[W,h2,h3,h4,z2,z1],
    P2=[h4,h5,U,z3,z2],
    Q3=[U,h6,h7,h8,z4,z3],
    Q4=[h8,h9,h10,h11,z5,z4],
    P5=[h11,h12,h0,z0,z5].

The requested class conditions are exactly

    P0 congruent P2 congruent P5,
    Qc congruent Q1 congruent Q3 congruent Q4.

This would be a **3P+4Q** dissection of one hat into two genuine convex shapes, a pentagon and a hexagon. The interior graph contains a cycle bounding Qc. All earlier four-piece hat constructions in the repository use a tree of cuts; the source-free all-hexagon parent obstruction does not apply because P is a pentagon. The donor and power-diagram structures are absent. W and U are genuine partial-contact points on the eventual source boundary, not extra collinear corners counted as corners of a piece.

### Exact strict precursor established

The following rational ring points give seven strictly convex pieces with disjoint interiors and exactly the prescribed hat boundary:

    z0=(764,271)/1000,
    z1=(637,-161)/1000,
    z2=(1228,-479)/1000,
    z3=(3095,-985)/1000,
    z4=(2838,-429)/1000,
    z5=(1655,973)/1000.

The [exact checker](astra-hat-edge-ring-exact-2026-10-15.py) verifies every nonincident supporting determinant, all21 pairwise separating-axis conditions, exact oriented internal-edge cancellation, and exact area equality. Every support determinant is positive; the minimum over all seven polygons is approximately0.294614. Arithmetic is exact in Q(sqrt3), with its positive real embedding. The numerical value is explanatory only. Oppositely directed internal edges cancel, leaving precisely the subdivided source boundary; equality of winding functions proves coverage, rather than inferring it just from area.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-hat-edge-ring-exact-2026-10-15.py

The fixture is a **convex partition precursor, not a two-class point**. No equality of its seven shapes is asserted. The numerical discovery script [astra-hat-ring-precursor-2026-10-15.py](astra-hat-ring-precursor-2026-10-15.py), with flags `--edge-spokes --b2`, is exploratory and unnecessary to the exact checker.

### Proposed metric gate, now SUPERSEDED by angle UNSAT

**Do not execute this metric gate:** the complete necessary-angle test below returned UNSAT. Its original finite definition is retained for audit. Keep b=2 and W,U at their specified midpoints. Let ONLY the twelve coordinates of z0,...,z5 vary. Impose all seven strict supporting-halfplane systems and the prescribed incidence. First attack the common-P requirement using the three anchored source corners:

* P0 contains a90-degree corner with adjacent side lengths2 and1/2;
* P2 contains a120-degree corner with adjacent side lengths2 and1;
* P5 contains a90-degree corner with adjacent side lengths1 and2.

These facts sharply restrict native corner correspondences. In particular the two90 corners of P are distinct because their unordered arm lengths differ. Do not impose a right-angle palette on its other two corners, and do not assume all source right corners correspond to one native index.

For an exact algebraic implementation, for each allowed cyclic/reflected correspondence equate the complete squared vertex-distance matrices. P0/P2/P5 have at most10^2 correspondence combinations; the four Q occurrences have at most12^3 combinations relative to Qc, before angle/side filters. These are explicit quadratic equations over Q(sqrt3) in twelve coordinates, with exact strict convex inequalities. A numerical optimizer may find candidate roots, but root isolation or an exact feasible construction must decide any promoted point. A sampled failure is not an exclusion.

The useful first return is an exact common-P realization with the residual Q equations stated, or an exact necessary-condition exclusion of this fixed gate. A successful full return must give TWO exact prototype coordinate lists and the complete7-piece dissection. Plane existence then follows by applying this same dissection to a known Tile(1,2) source tiling; universal reconstruction is a separate obligation. Before decoder work, attack P-only/Q-only tilings and mixed periodic carriers. A new seven-piece source partition does not show that arbitrary admitted P/Q tilings reassemble into hats.

There is no justification for extending source ratios, midpoint parameters, or the number of central vertices if this fixed gate fails. Any such change must remove its actual obstruction, not merely add variables. If a pentagon-only obstruction closes it, stop before the Q congruence enumeration.

## Why the first ring proposal was rejected

A slightly simpler ring connects the central hexagon to h0,h2,h4,h6,h8,h11. It gives five outer pentagons and one outer hexagon, hence a proposed5P+2Q partition. A strict precursor exists numerically, but common-P geometry fails for every source ratio b!=1 by an elementary corner argument.

The same P would contain the following native corners, inherited from different source arcs:

    angle90,  arms {b,1};
    angle120, arms {2,1};
    angle120, arms {b,b};
    angle120, arms {1,1}.

For b!=1 the three120 corners are pairwise distinct. The90 corner is distinct by angle, even at b=2 where one unordered arm pair coincides. A pentagon's angle sum forces its fifth angle to90. Thus P has no acute corner. But h6 has source angle90 and is split between two P pieces, each with a strictly positive angle, forcing both of these corners below90. Contradiction.

At b=1 the source Tile(1,1) itself has periodic tilings when reflections are allowed; any uniform dissection of that polygon propagates such a periodic escape to its pieces. The authors' [primary project page](https://cs.uwaterloo.ca/~csk/spectre/) states this fact explicitly, and links [A chiral aperiodic monotile](https://arxiv.org/abs/2305.17743). This is an inherited source fact, not a new theorem. The fresh query was `Smith Myers Kaplan Goodman Strauss Tile(1,1) periodic tilings reflections equilateral hat`.

The edge-spoke gate above changes precisely the incidence causing this obstruction: h6 is now an unsplit native90 corner in Q3, while U is a flat boundary point split between P2 and Q3. The common-P family has only THREE occurrences, with no mandatory three distinct120 corners. This is an actual escape from the proved obstruction, not a new coordinate sample in the same killed topology.

## Cheap fixed-frame deformation test: do not pursue

Before the ring construction, I tested a completely free geometric deformation of the old four-pentagon plane complex, with two prototype coordinate lists and a binary assignment to the four positions inside each hat. The old parent boundary shape was not prescribed, and occurrence translations were free. I fixed inherited occurrence linear frames, using the lexicographically first preserving dihedral correspondence to the reference P6 pentagon.

The [diagnostic](astra-hat-pentagon-linear-diagnostic-2026-10-15.py) uses the first genuine H-supertile:25 hats,100 pentagons,205 nodes. It eliminates per-occurrence translations by a shared-node spanning tree and computes the exact remaining linear kernel over Q(sqrt3). Every one of the seven nonconstant positional colorings has rank15 on20 prototype coordinates. The kernel is precisely four prototype-origin gauges plus the original uniform scale. Dropping ALL T-incidence constraints still gives the same result, so merely freeing T ratios cannot rescue these fixed-frame assignments.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-hat-pentagon-linear-diagnostic-2026-10-15.py --native-only

If all four position templates are free, the same necessary native-vertex system has rank28 on40 coordinates, leaving four shape parameters after eight origin gauges:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-hat-pentagon-linear-diagnostic-2026-10-15.py --native-only --four-free

Those parameters appear to recover source(a,b) and the existing free junction(Vx,Vy); this identification has NOT been proved. The fixed-frame computation is exact but unreviewed, and other correspondences/occurrence frames are not exhausted. It suffices as an information-gain test against endorsing this deformation idea. No new broad rigidity theorem or independent forcing result is claimed.

## Executed necessary-angle gate and final construction status

Root correctly recommended an angle-correspondence gate before metric equations. [The retained script](astra-hat-edge-ring-angle-gate-2026-10-15.py) uses five prototype P angles and six prototype Q angles, all strictly between0 and180, with sums540 and720. Every occurrence is an independent cyclic or reflected correspondence; no repeated corner value is silently assigned a unique index. The constraints impose every original source vertex angle, every native boundary T pair summing180, and every interior native corner sum360. Thus the initial3P+4Q domain includes all10^2*12^3=172800 correspondences simultaneously. The solver uses exact rational linear arithmetic with disjunctions, not floating geometry.

All EIGHT named finite angle domains returned **UNSAT**, before their60000ms caps:

| Invocation suffix | Explicit incidence |
|---|---|
| `1 5` | Six-spoke ring, W in h1h2 and U in h5h6;3P+4Q |
| `1 6` | W in h1h2, U in h6h7;3P+4Q |
| `2 5` | W in h2h3, U in h5h6;3P+4Q |
| `2 6` | W in h2h3, U in h6h7;3P+4Q |
| `--mixed` | Replace W by native h2, retain U in h5h6;4P+3Q |
| `--split-center` | In case1,5, replace Qc by two pentagons across a chord joining interiors of z0z1 and z3z4;5P+3Q |
| `--split-outer1` | In case1,5, replace Q1 by two pentagons across a chord joining interiors of h2h3 and z2z1;5P+3Q |
| `--mixed-center7` | Seven-spoke variant specified below;6P+3Q |

Replay each with

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-hat-edge-ring-angle-gate-2026-10-15.py SUFFIX

These are **finite solver evidence** with a retained producer. No independent reimplementation, Farkas-certificate family, or hostile review has yet been completed. They are not promoted to stable impossibility theorems. The angle budgets are independent of positive source length ratio and of the positions of proper edge-interior attachment points, so changing these metrics does not change the tested angle formulas. This observation is not permission to extend the negative conclusion to different incidences.

The central split has an additional exact strict precursor. In the rational fixture above put r=(z0+z1)/2 and s=(z3+z4)/2, and replace Qc by

    [r,z1,z2,z3,s], [s,z4,z5,z0,r].

Both are strict pentagons. The exact checker with `--split-center` PASSES all28 pairwise separation tests, the subdivided boundary-chain cancellation, and area equality. The minimum support determinant is147849/1000000>0. This is a second exact source partition, not a two-class point. The unsplit outer polygons retain their genuine side counts; r and s are host-side interior points, not added native corners on their outer neighbors.

The last7-spoke variant deliberately changes BOTH central species and the old h8-to-h11 outer arc. Add V inside h9h10 and use ring z0,...,z6. Its nine words are

    P0=[h0,h1,W,z1,z0],
    Q1=[W,h2,h3,h4,z2,z1],
    P2=[h4,h5,U,z3,z2],
    Q3=[U,h6,h7,h8,z4,z3],
    P4=[h8,h9,V,z5,z4],
    P5=[V,h10,h11,z6,z5],
    P6=[h11,h12,h0,z0,z6],
    Pc=[r,z1,z2,z3,s],
    Qc=[s,z4,z5,z6,z0,r].

Here r lies inside z0z1 and s inside z3z4. Its angle model includes V's180-degree boundary budget, z6's360-degree budget, and r/s native-pair budgets180. It too is UNSAT. No metric precursor was claimed or needed for that rejection.

**Direction decision:** none of this cycle's tested positive gates survives to a common-metric problem. Do not allocate work to congruence ideals, larger source patches, source-ratio scans, or hierarchy recognition for them. The useful return is the changed-topology experiment and its decisive necessary-condition failure. I have not obtained a viable new two-shape candidate and do not describe one as promising merely because its unmarked decoder is still absent. The next source-based positive proposal must change the fixed source corner-budget incidence itself, for example by explicitly erasing and crossing source boundaries, and must first specify a finite angle-feasible two-class cell complex. Merely adding another central chord to these failed named incidences has not earned a new metric search.

## Separate negative portfolio update

While this direction cycle ran, root completed the adjacent-repeat common-five classification and reported a fresh VALID whole-proof audit. Thus its earlier4-class/41-support reconnaissance is superseded by the root's reviewed result; this note does not re-prove it. All common-five numerical hexagon pairs, at every repeated-slot separation, are now excluded from aperiodicity in that reported theorem's scope. The earlier noncommon both-nonadjacent theorem and six-distinct arbitrary-partner theorem remain distinct scope claims. No unrestricted impossibility result follows.

The current negative portfolio therefore does not need another unmotivated finite word census. Preserve the positive portfolio, but record its failures accurately: the reviewed mean-site power box and arbitrary-split mark-local donor topology remain closed, and this new ring exploration supplies no surviving two-class geometry. Fresh strategy work should start from the listed exact failures rather than replaying these incidences.

## Retained wrap-up artifacts

- [Seven-piece exact precursor output](../certificates/astra-hat-edge-ring-precursor-2026-10-15.json).
- [Eight-piece exact precursor output](../certificates/astra-hat-split-ring-precursor-2026-10-15.json).
- [Eight angle-gate outputs](../certificates/astra-hat-ring-angle-recon-2026-10-15.json), explicitly labelled unreviewed finite solver evidence, not a proof certificate.

Both exact precursor checks and all eight named angle gates were replayed together during wrap-up and returned PASS/UNSAT as recorded. All four diagnostic programs passed Python syntax compilation. No task process remains running. No verification-registry, discovery-log, staging, or Git changes were made by this adviser.
