# Complementary pp angles: a new periodic cone and exact fixed-carrier classification

Status: **independently adversarially reviewed VALID**; see [the fresh review](../reviews/branching-hexagon-new-complementary-pp-periodic-cone-review.md). This is a constructive periodic escape, not a solution of the unrestricted two-prototile target. The necessity statement below applies only to the explicitly indexed eight-face carrier, not to all two-run tilings or to every tiling satisfying a chain-transport condition.

Angles and directions below are in degrees. Native angle B_i is the interior angle immediately before native side i. Reflections and rotations of tiles are permitted.

## 1. New positive periodic family

For every real pair

    0 < delta < 30,       60-delta < alpha < 120-delta,

set q=1 and p=2 cos(delta). Define A with side lengths (p,q,p,q,p,q) and directed edge angles

    (0, 60+delta, 120, 180+delta, 240, 300+delta).

Define B with side lengths (p,p,p,q,q,q) and directed edge angles

    (0, 180-alpha, 180, 300-alpha-delta, 360-alpha+delta, 420-alpha-delta).

Then A and B are strictly convex closed hexagons, and their congruent copies admit an edge-to-edge doubly periodic plane tiling with a quotient containing four copies of each species. Every positive common scale also admits such a tiling.

A has angles (120+delta,120-delta) repeated three times. B has angles

    (240-alpha-delta, alpha, 180-alpha, 60+alpha+delta,
     120-2delta, 120+2delta).

In particular B_1+B_2=180. Except at alpha=90 these pp angles differ, so this extends beyond the previously constructed equal-pp-angle cone. At alpha=90 it meets that cone's gamma=90 slice, p=2 cos(delta).

### Exact closure and convexity on the entire open domain

A closes because its p edges form one equally spaced threefold orbit and its q edges form another. In B the first and third p edges cancel, so its p-chain is

    p exp(i(180-alpha)) = -p exp(-i alpha).

The q-chain is

    exp(-i alpha) [exp(i(300-delta))+exp(i delta)+exp(i(60-delta))]
      = 2 cos(delta) exp(-i alpha),

since exp(i300)+exp(i60)=1. Thus B closes exactly for the stated p. All six native lengths are positive.

A's consecutive turns alternate 60+delta and 60-delta. B's consecutive turns, including the last-to-first turn, are

    (180-alpha, alpha, 120-alpha-delta, 60+2delta, 60-2delta,
     alpha+delta-60).

Every turn is strictly between 0 and 180 on the given domain. They sum to 360. These assertions are direct inequalities; they do not rely on the exact fixture or on continuity from it.

For completeness, closed positive edge vectors with cyclically increasing directions, total turn 360, and each turn strictly less than 180 give strict convexity here. Fix one edge. The subsequent edge vectors' cross products with that edge have a positive block followed by a negative block, with possible zeros at the antipodal direction. The first product is strictly positive because the next turn lies in (0,180); the last is strictly negative because the last-to-first turn lies there. The products sum to zero by closure. Every proper partial sum after at least one subsequent edge and before the last is therefore strictly positive: before the negative block it has a strictly positive term; in the negative block it equals the negative of the remaining nonpositive terms, which include the strictly negative final term. Every nonincident vertex lies strictly to the left of each side. This proves simplicity, nonzero area, and strict convexity.

### Fixed carrier and actual links

The native side-pair carrier is the retained raw certificate

- `research/certificates/branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json`.

Its old fixture's `quad`, `lift_bits`, and search-domain metadata play no role here. Only its `faces`, `paired_edges`, and `vertex_classes` are reused. Faces 0,1 are A, faces 2,3 reflected A, faces 4,5 B, and faces 6,7 reflected B. A reflected face maps actual vertex i to native vertex (-i) mod 6 and reverses its side-label word. The reflection is conjugation together with reverse traversal, so each actual face retains positive orientation.

The new symbolic certificate repeats these face data and all 24 side pairs. Every one of the 48 face-side occurrences appears exactly once and every pair has equal p/q labels. Glue each paired side by the isometry reversing its boundary direction. This glues positively oriented polygons to an orientable surface. The dual face graph is connected.

The endpoint equivalence graph is checked directly: all 48 corner occurrences occur once, each occurrence has degree two, and each retained class is exactly one connected three-node cycle. Thus these are actual circular links, not merely multisets of corner angles. There are 16 links, four of each native type:

| Native link type | Angle sum |
| --- | --- |
| A_high, B_0, B_1 | (120+delta)+(240-alpha-delta)+alpha = 360 |
| A_low, B_2, B_3 | (120-delta)+(180-alpha)+(60+alpha+delta) = 360 |
| A_high, A_high, B_4 | 2(120+delta)+(120-2delta) = 360 |
| A_low, A_low, B_5 | 2(120-delta)+(120+2delta) = 360 |

The producer independently recomputes all 16 raw link sums as affine coefficient triples (360,0,0), in constant/delta/alpha order. It also checks the turn bounds on the vertices of the closed parameter polygon, (0,60),(0,120),(30,90),(30,30); every affine turn has minimum at least zero, maximum less than 180, and is nonzero. The displayed direct inequalities ensure strict positivity throughout the open polygon.

### Why the quotient proves a periodic plane tiling

Each side interior has a Euclidean neighborhood after the two halves are glued. Each vertex link is a single circle of total angle 360, so each vertex also has a Euclidean neighborhood. The quotient is a compact connected orientable flat surface with eight faces, 24 edges, and 16 vertices, hence Euler characteristic zero. It is a flat torus.

Its complete simply connected Euclidean universal cover is the plane. The lifted polygons have disjoint interiors and cover the plane because they are lifts of the actual cell structure. An orientation-preserving deck isometry with a nontrivial rotation has a fixed point, so the fixed-point-free deck group consists of translations. Compactness of the quotient makes these translations a rank-two lattice. Therefore the lifted tiling is doubly periodic. This argument holds independently at every parameter in the open domain; it uses no persistence inference from a sample or a local balance vector.

### Exact noncentral fixture

At delta=15 and alpha=75, p=2 cos15=sqrt(2+sqrt3). The native data are

    A directions (0,75,120,195,240,315), angles (135,105) repeated;
    B directions (0,105,180,210,300,330), angles (150,75,105,150,90,150).

The exact fixture is developed in Q(zeta24), zeta24=exp(i*pi/12). Its NEW development certificate verifies native closure, all strict side supports, exact native angle units, all paired squared lengths, all actual circular links, connected direct-isometry development, translational holonomies, the full integral rank-two period lattice, and covolume equal to the sum of all eight positive face areas. This fixture is additional exact evidence; the full-domain proof is the preceding quotient argument.

## 2. Necessity and sufficiency for this fixed indexed carrier

Fix 0<delta<30, q=1 and p>0. Let A be the preceding threefold hexagon with that p. Let B be an arbitrary strictly convex closed hexagon with native side word (p,p,p,q,q,q), and normalize its first directed edge to direction zero. Suppose these native A and B shapes, with the specified reflection indexing, make **this fixed eight-face side-pair carrier** a nonsingular flat quotient. Then its link equations force

    B_0+B_1=240-delta,   B_2+B_3=240+delta,
    B_4=120-2delta,      B_5=120+2delta.

These conditions are necessary because all four listed actual link types occur. They are sufficient for the carrier's 16 links, once native positivity and closure hold. Set alpha=B_1 and beta=B_2. Strict convexity gives 0<alpha,beta<180. The forced B angles are

    (240-delta-alpha, alpha, beta, 240+delta-beta,
     120-2delta, 120+2delta).

The native p directions are 0,180-alpha,360-alpha-beta. The q directions, obtained by adding the remaining turns, are

    (300-alpha-delta, 360-alpha+delta, 420-alpha-delta).

After multiplying the native closure equation by exp(i alpha), closure is exactly

    p [exp(i alpha)-1+exp(-i beta)] + 2 cos(delta) = 0.

Its imaginary part gives sin(alpha)=sin(beta). For alpha,beta in (0,180),

    sin(alpha)-sin(beta)
      = 2 cos((alpha+beta)/2) sin((alpha-beta)/2) = 0,

so either beta=alpha or beta=180-alpha. There are no other branches.

**Equal branch.** If beta=alpha, the real closure equation is

    p(2 cos(alpha)-1)+2 cos(delta)=0.

Writing gamma=180-alpha gives p=2 cos(delta)/(1+2 cos(gamma)). Positivity of B_3 requires alpha>60+delta; together with alpha<180 this gives exactly 0<gamma<120-delta. Conversely every such gamma has positive denominator, since gamma<120, and all six B angles lie in (0,180). Its directions and angles are exactly those of the earlier two-parameter cone

- `research/lemmas/branching-hexagon-new-two-run-two-parameter-periodic-cone.md`.

**Complementary branch.** If beta=180-alpha, the exponential sum exp(i alpha)+exp(-i beta) vanishes. The real equation gives p=2 cos(delta). The strict upper bounds B_0<180 and B_3<180 give respectively alpha>60-delta and alpha<120-delta; all other strict angle inequalities follow. Conversely exactly this open interval gives the new family in Section 1.

The branches intersect only at alpha=beta=90, corresponding to gamma=90. The preceding convexity and flat-quotient proofs establish sufficiency on both complete parameter domains. Thus the two branches are an exact classification of positive strictly convex geometry compatible with this native-indexed carrier. This statement does not assert that arbitrary tilings must contain this carrier, that chain transport forces its link types, or that all other binary two-run geometries are untileable.

## 3. Retained verification artifacts and scope

NEW producer, normal replay read-only; an explicit `--output` is required to write:

- `research/searches/branching-hexagon-new-two-run-complementary-pp-periodic-cone.py`;
- `research/searches/branching-hexagon-new-two-run-complementary-pp-periodic-develop.py`.

NEW retained certificates:

- `research/certificates/branching-hexagon-new-two-run-complementary-pp-periodic-cone.json`;
- `research/certificates/branching-hexagon-new-two-run-complementary-pp-eight-face-development.json`.

Both replayed successfully in the `arisearch` environment. No earlier certificate or lemma was changed. The cone certificate checks combinatorial topology and every exact affine angle identity. The development certificate checks a single noncentral exact fixture. The trigonometric necessity argument and the all-real flat-cover argument have passed the fresh independent review. The larger unrestricted two-prototile aperiodicity problem remains unresolved.
