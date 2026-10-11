# Three-angle pentagon trial: exact search and witness record

**Status:** exact periodic witnesses freshly independently reviewed valid;
bounded X/Y four-face ansatz exhausted and metrically obstructed, with its
partition-count repair awaiting independent re-review.
Neither result resolves the unrestricted problem.

## Mathematical questions and exact domains

The analytic family has angles R=90, B=theta, G=360-2theta with
90<theta<135. Both pentagons have multiplicities (2,2,1), and avoid adjacent
right corners. Theta=112.5 and120 are excluded when asserting the precise
two-full-star language. All unrestricted contacts obey the full/half-sector
dichotomy. Minimum angle90 bounds a full star to3 or4 native corners and a
half star to1 or2; convexity excludes full valence1 or2. The exact affine
check enumerates all category multisets in these justified ranges. It finds
permanent full stars RRRR andBBG, a permanent half star RR, and exceptional
parameters112.5 and120. This covers a continuum, not a bounded denominator
or a sampled parameter grid.

The direct mixed-word trial fixes theta105 and native angle words
X=(90,150,90,105,105),Y=(90,105,90,105,150), with two faces of each type.
All native sides are full seams; T contacts are outside this finite ansatz,
not excluded from the original pair problem. Sides run from cornerj to
cornerj+1 modulo5 and all seam maps reverse endpoint order. Each face has
one nonright/nonright side and two sides of each right/nonright orientation.
At a full legal star a right endpoint can be identified only with a right
endpoint. Thus every possible model in this ansatz is represented by:

    8 independent reflection choices after fixing one global reference,
    3 pairings of the four nonright/nonright sides,
    8! bijections of the right/nonright to nonright/right sides.

The exact finite domain is967,680 complete matchings. Cyclic labels remain
native labels; all side pairings are considered. Fixing face0 unreflected
loses no possibility because reflecting the whole quotient toggles all
face reference choices. Reflected native sidej maps to original side
(-j-1) mod5. Reversed-endpoint union-find constructs the actual vertex
classes. Six classes, each with angle total360, are required. Every such
model has six vertices, ten edges and four faces; the retained models have
the necessary connected flat torus structure. There are eight angle models
and four stored native-side partition labelings representing three distinct
equality relations.

For each partition the generator forms the exact4-row linear closure matrix
for the two unreflected native pentagons, using their direction lists
X:0,30,120,195,270 andY:0,75,165,240,270. Equal matched lengths share one
column. Exact radical nullspaces establish that one equality relation, represented
by two column-permuted stored labelings, permits only the zero length vector;
the other two relations force both native side3 lengths zero.
This eliminates the declared four-face X/Y ETE ansatz only.

The Y/Y trial changes both words to(90,105,90,105,150) with the same four-face
count and same candidate reflection domain. It terminates at its first
positive numerical model after28,800 candidate pairings. It is a witness
search, not a complete classification. Exact reconstruction gives the
six-label formulas in the lemma and a full mixed periodic tiling.

## Discovery screens and exact proof arithmetic

The reconnaissance LP assigns one variable per native-side equality class,
uses four floating closure equations plus sum(lengths)=1, and bounds each
variable below by1e-6. Objective is0. SciPy HiGHS is used only to find or
reject exploratory candidates. Those answers do not decide any promoted
mathematical equality, convexity, or infeasibility conclusion.

The105-degree witness is reconstructed with exact fraction arithmetic in
Q(sqrt(2),sqrt(3),sqrt(5)). Its radical basis is
1,sqrt(2),sqrt(3),sqrt(6),sqrt(5),sqrt(10),sqrt(15),sqrt(30). The irrational-
angle witness uses Q(sqrt(5),sqrt(21)), basis1,sqrt(5),sqrt(21),sqrt(105).
Both small witness verifiers independently check all native side vectors,
closure, strict supporting-half-plane determinants, positive/distinct side
labels, actual seam length equality, reversed endpoints, vertex links,
connectivity, Euler characteristic and the affine-star equations.

Strict inequalities use rational intervals with denominator2^20: for each
squarefree radicand n, integer square root bounds prove
floor(sqrt(n)*2^20)/2^20 < sqrt(n) < (floor+1)/2^20. These are certified
isolating intervals, not numerical tolerances or angle denominator bounds.
All closure/equality tests are exact coefficient tests in the radical field.

For the mixed-word obstruction, SymPy computes exact radical nullspaces.
A separate stdlib checker imports only the small exact radical arithmetic
from the105 witness checker, reconstructs every retained angle model and
raw partition labeling, and verifies ranks by exact determinant minors. For the
five-column cases it checks rank4 together with zero determinant on columns
0..3; the cofactor kernel then has coordinate4 zero. That coordinate is
native side3 of both types. This checker validates the retained models and
all four stored metric calculations (three distinct equality relations), while enumeration completeness comes from
the declared generator domain and its exhaustive loops.

The infinite plane tilings are justified by the stated compact flat-torus
universal-cover proof. Local angle classes alone are not used as an
existence certificate. The irrationality of theta/pi at cos(theta)=-2/5
is proved by the monic integer root-of-unity recursion, not a numerical
angle estimate or an imported rational-cosine classification.

## Replay commands and retained artifacts

Run from repository root, in the existing arisearch environment:

    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-three-pentagon-explore.py
    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-three-pentagon-same-word-explore.py
    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-three-pentagon-counterexample-verify.py
    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-three-pentagon-irrational-angle-verify.py
    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-three-pentagon-mixed-word-verify.py

The generators write their retained discovery/model outputs. The three
small verifiers print exact JSON, retained respectively as:

    research/certificates/new-angle-three-pentagon-counterexample.json
    research/certificates/new-angle-three-pentagon-irrational-angle.json
    research/certificates/new-angle-three-pentagon-mixed-word-rank.json

Additional discovery and exact closure records:

    research/certificates/new-angle-three-pentagon-preliminary.json
    research/certificates/new-angle-three-pentagon-mixed-word-angle-models.json
    research/certificates/new-angle-three-pentagon-mixed-word-closure.json

The preliminary JSON contains numerical reconnaissance only. The retained
exact105 and irrational-angle certificates establish the main counterexamples.
The main mathematical artifact is
`research/lemmas/new-angle-three-pentagon-private-length-counterexample.md`.

## Environment, limits, and completion

Date2026-10-09. Python3.12.13, NumPy2.5.2, SciPy1.18.0, SymPy1.14.0,
Linux6.8.0-142-generic-x86_64 withglibc2.41. The NumPy/SciPy/SymPy packages
were already installed; no dependencies or environment files were changed.
No randomness or seed is used. No search cap, internal timeout, memory cap,
solver node cap or truncation was imposed. The X/Y enumerator fully exhausted
its declared967,680 domain; its last enumeration elapsed timer was
17.747822461002215s before exact nullspace postprocessing. The Y/Y witness
search terminated successfully after0.3242662460033898s and28,800 cases.

The captured exact verifiers all exited with status0:

    105-degree witness: 0.04970329099887749s,
    irrational-angle witness: 0.05831566900451435s,
    mixed-word retained-model/rank checker: 0.2278130240010796s.

These are observed elapsed subprocess times, not complexity estimates.
Memory usage was not separately measured. No timeout or interruption was
reported as infeasibility.

## Consequences, failure scope, and restart state

The exact Y/Y family admits a mixed doubly periodic plane tiling for every
positive t,s and every90<theta<135, via one explicit four-face torus.
Consequently irrational private edge ratio within this family cannot force
aperiodicity. The concrete cos(theta)=-2/5,t=1,s=sqrt(5) pair additionally
has irrational angles and irrational area ratio, with the same periodic
escape. It is a negative control for the combined angle/metric shortcut,
not a classification of all three-angle pentagons.

The distinct-word X/Y ansatz is blocked at its specific four-face ETE
metric closure. It supplies no global obstruction to arbitrary plane
tilings, larger quotients or right-corner T contacts. Reopening that route
requires a concrete different infinite gluing mechanism or different
geometry; increasing the bounded torus size alone does not meet the
construction task. Root owns discovery-log integration and fresh hostile
review. No novelty or universal literature-priority claim is made.

The count repair retained all four stored labelings and all matrix evidence.
First-occurrence canonicalization identifies the two rank-three records as
one equality relation. The metadata now records four raw labelings and three
distinct relations, and the exact retained-model checker asserts both counts.
No metric conclusion changed. Independent count re-review is requested.

Exact retained versions (SHA-256):

    c8dc46e7cda9c3783eb4745e683f921a38cdb0eb1964628e19f638f50c0f7ac6  research/searches/new-angle-three-pentagon-explore.py
    2aa355aaf99a7b625df9b62aef8e643944ae1acbd71bece70715e2680b968c58  research/searches/new-angle-three-pentagon-same-word-explore.py
    214c349b79fde19799821e4ee560f3741a5058b16c537598c2ab9ae15ed9fd0a  research/searches/new-angle-three-pentagon-counterexample-verify.py
    f9ab5389bb9945660a2db153f2571700e3da53851118cedd98374472a90d64c3  research/searches/new-angle-three-pentagon-irrational-angle-verify.py
    e175b782479b513dfd9e224eb22f12141181f51e932797bc3dfe6c2f465ffff8  research/searches/new-angle-three-pentagon-mixed-word-verify.py
    ced0a6c3d53d0812e429717159dab433faacb5653209107f1807bc52c67d7f2a  research/certificates/new-angle-three-pentagon-counterexample.json
    9706c29238e2ede03ef248b6693ab79723cc7d5b69592550f93fac58102a3a9c  research/certificates/new-angle-three-pentagon-irrational-angle.json
    dba1d4a45be06b02841b8af64d2bfa0f76dbf04ac34bbe69714751721ffe57b7  research/certificates/new-angle-three-pentagon-mixed-word-angle-models.json
    b76251663bb51b289373c663ab9c5c5b180aa83a2faf43e115e295ccbd429305  research/certificates/new-angle-three-pentagon-mixed-word-closure.json
    57601707bc46bf73eb94a07b2d615436a56b0ff8cacfca3c8cc9b08400788b81  research/certificates/new-angle-three-pentagon-mixed-word-rank.json
