# Fresh hostile review of the all-obtuse regular-heptagon classification

**Verdict: valid**, with the explicitly reviewed all-obtuse forcing and
one-beta heptagon obstruction as dependencies. The general necessity proof
and the direct rank-two periodic witness both pass fresh review. This is
a classification of the stated restricted family, not a solution of the
unrestricted main research problem.

The reviewer did not develop the saturation proof or the witness. Artifacts
examined are the [classification lemma](../lemmas/all-obtuse-pentagon-regular-heptagon-classification.md),
[producer](../searches/all_obtuse_pentagon_regular_heptagon_witness.py), and
[certificate](../certificates/all-obtuse-pentagon-regular-heptagon-witness.json).
The independent exact checker is
[verify_all_obtuse_regular_heptagon_independent.py](verify_all_obtuse_regular_heptagon_independent.py).
It imports no producer and uses separating axes instead of the producer's
polygon clipping. The analytic necessity proof is audited separately below.

## Boundary counts and an independent attack on the angle gate

Strict obtuseness permits application of the reviewed full-edge/trivalent
forcing theorem to the original unrestricted tiling. Hence neither partial
contacts nor reflected copies add another local sector type. With fixed
positive-area prototiles and bounded diameter, all changes between centroid,
side, and vertex window conventions affect only O(R) incidences. These
estimates are uniform in translation of the square. The displayed corner
and angle counts eliminate V to give N_P=N_Q+O(R), and total area gives
N_P+N_Q=Theta(R^2). Both types consequently have uniform positive quadratic
counts. Omission of either type and a subquadratic sparse type are excluded
at this step, without assuming a limiting frequency.

The author's star equations are correct. Write X,Y,Z for QQP, QPP, PPP
stars; QQQ is impossible because 3*(5pi/7)!=2pi. Direct elimination from

    7N_Q=2X+Y+O(R),   5N_P=X+2Y+3Z+O(R)

gives X=3N_Q+Z+O(R). Every QQP star uses a P corner of
alpha=4pi/7, so kN_P>=X+O(R), where k is the number of native alpha
corners. This forces k>=3. The O(R) notation in this inequality expresses
a signed boundary error; after bounding its absolute value, it cannot
compensate for a missing quadratic supply of alpha corners.

A cheap independent counterexample attack gives the same gate through
side incidences. Each non-alpha P corner requires an incident PP side,
because two Q neighbors would force its angle to be alpha. If there are
at least three such corners, at least two PP sides are required on every
P, so P has at most three PQ sides. QQ side positions around a regular
heptagon cannot be adjacent: three Q sectors would then occur at the
shared corner. Thus Q has at most three QQ sides and at least four PQ
sides. Counting PQ contacts would give 4N_Q<=3N_P+O(R), contradicting
N_P=N_Q+O(R). This rules out k<=2 without reproducing the star-count gate.
No contrary local or window-count configuration was found.

The k=5 case violates the pentagon angle sum. In the k=4 case the remaining
angle is beta=5pi/7, exactly the scope of the independently reviewed
[one-beta obstruction](regular-heptagon-one-beta-pentagon-review.md).
Its proof allows arbitrary P lengths and all isometries. Thus k=3, and
the other two native angles theta,psi sum to9pi/7.

## Nonnegative defects and persistence in the limit

B_alpha is an actual count of alpha incidences at stars other than QQP,
not a signed curvature residual. Since each QQP star has precisely one
P-alpha corner, B_alpha=3N_P-X+O(R). Substituting the checked X equation
gives

    B_alpha+Z=3(N_P-N_Q)+O(R)=O(R).

Both terms are nonnegative. In particular PPP stars cannot cancel wrong
alpha incidences. A bad P centroid is charged to a wrong alpha incidence
or one of the three P incidences at a PPP star; the boundary convention
adds only O(R). The bad-centroid count is therefore uniformly O(R).

The growing bad-free disk argument is valid even if defects are dense
along lines or have unbounded gaps between good components. If every
radius-H disk contained a bad centroid, then their radius-H disks would
cover a large square. Only O(R+H) bad centroids lie in its H-enlargement,
so this cover has area at most C(R+H)H^2, below 4R^2 for sufficiently
large R. H is fixed during this comparison and may then tend to infinity.
This establishes arbitrarily large good disks without a bounded search
or a claim that the original tiling is everywhere good.

The local compactness argument uses only fixed compact shapes, bounded
positions, positive area, and compact O(2). It allows continuous absolute
orientations and reflections. A finite number of placements in each
bounded enlargement may be stabilized and extracted on a diagonal
subsequence. A chosen covering tile near any point remains within a fixed
centroid distance and has a closed limiting polygon containing that point.
An interior overlap, or two retained tiles collapsing to the same positive
area polygon, would persist as an open overlap in approximating tilings.
Thus the collection is a locally finite admitted tiling.

The stated uniform vertex separation is sufficient for native-star
persistence. Choose r below the minimum reference-vertex distances to
other native vertices and nonincident sides. The three corner wedges at
any original tiling vertex cover its radius-r disk. Another vertex cannot
enter a wedge interior and cannot subdivide a full native side on a wedge
ray. Distinct stars therefore cannot merge in the limit. Whole-side
neighbors and all incident corner tiles are extracted together with each
selected tile; fixed positive side lengths prevent collapse. Their three
angle sectors still exhaust 2pi. Every relevant P centroid lies in the
growing good disk once its radius exceeds the fixed local neighborhood
size. Consequently all limit alpha corners are QQP and no limit PPP star
occurs. No such pointwise conclusion is imposed on the original tiling.

## Forced P shape and closure

In the admitted limit, each non-alpha corner is PPQ, while each alpha
corner is QQP. A PP side can therefore have only the two non-alpha
vertices as its endpoints. Each of those vertices needs exactly one PP
neighbor, forcing their adjacency and their connecting side as the unique
PP side. The other four sides meet Q and are unit. This uses full native
contacts; none of the four equal-length claims is inferred from a partial
overlap.

The four unit side directions along the opposite chain are
0,t,2t,3t with t=3pi/7. Their sum is

    exp(3it/2)*sin(2t)/sin(t/2)
      = L*exp(9pi*i/14),   L=sin(pi/7)/sin(3pi/14)>0.

The closing vector is directed at23pi/14. The preceding unit vector is
at18pi/14, so the final exterior turn is5pi/14; the return to the first
unit vector has the same turn. Thus both non-alpha angles are9pi/14.
There is no additional branch from a negative resultant: sin(2t) and
sin(t/2) are both positive. Four known consecutive unit vectors and their
closing vector determine the vertex list uniquely up to isometry. This
forces the original fixed prototile to be P*, since the limiting tiling
uses that same P. It does not force the original tiling's placement to be
periodic.

## Independent exact witness and whole-plane existence

The checker decodes every retained coordinate used in the witness from its
irreducible minimal polynomial and rational isolating interval, using exact
AA/QQbar arithmetic. It verifies the selected cyclotomic embedding and the
lemma's complete explicit Q0 and P0 coordinate formulas. Strict supporting
inequalities check global convexity of all four polygons. Side lengths and
angle cosines verify a regular unit heptagon and exactly P*. Pointwise
vertex sums verify that Q1 and P1 are their half-turn copies, so exactly
two congruence classes are used.

The source's formulas for u,v,C are independently checked. Their determinant
is positive. Lattice-coordinate bounds are derived afresh for every ordered
motif pair, and every integer shift pair within those bounds is tested by
separating axes. The derived complete domain is exactly the retained list
of 26 nontrivial comparisons. Each passes with disjoint interiors. Shifts
outside the domain have a disjoint coordinate projection, so no geometric
neighborhood cutoff is hidden in this finite certificate.

The checker also verifies the exact identity

    2area(Q0)+2area(P0)=det(u,v)>0.

Since the independent periods form a discrete lattice and the four motifs
are bounded, the periodic union is locally finite and closed. Interior
disjointness and the area identity give full measure in a fundamental
parallelogram. Any uncovered point would have an uncovered open disk and
would give positive missing area in a fundamental domain. Hence the union
covers the plane. This proves existence directly and does not rely on an
unproved carrier packing or finite-patch extension.

## Replay and scope

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_all_obtuse_regular_heptagon_independent.py
```

The checker passed, including the final lemma's explicit coordinate and
embedding formulas. Its overlap backend differs from the producer and it
imports none of that producer. No solver, stochastic seed, search cutoff,
timeout, or finite orientation alphabet is used. Separate numerical tests
of the analytic saturation proof would not add proof evidence and were
not written.

The result establishes precisely an if-and-only-if metric classification
for an all-obtuse pentagon paired with a regular heptagon, together with a
periodic escape for its sole tileable metric class. Right or acute P angles
and nonregular heptagons are excluded by the hypotheses. The proof does
not assert that all P*,Q tilings are periodic. No novelty or priority claim
is audited or made. No substantive defect was found.
