# Complementary two-angle hexagons cannot force aperiodicity

Date: 2026-10-12. Status: [fresh whole-statement review VALID](../reviews/two-hexagon-complementary-angle-native-word-reduction-review.md).

Let A,B be fixed compact strictly convex hexagons, with all rotations,
reflections and arbitrary partial contacts admitted. Assume A has three
angles p and three q=240-p degrees, and B has three angles r=360-2p and
three s=2p-120 degrees, where90<p<150 andp!=120. Their native cyclic
orders are unrestricted. If the pair admits any tiling of the plane, it
admits a periodic tiling. Thus no pair in this entire complementary-angle
family is aperiodic under the target definition.

This imposes no rationality on p, lengths or coordinates and permits omission
of either tile species. Each of the nine native-order cases is covered at
all actual side metrics; there is no remaining alternating metric residue.

## Exact angle and native-word domain

Label the p/r corners0 and q/s corners1. Every admitted three-corner star
has two A corners and one B corner, all of the same colour. There are36
native unordered triples, including repeated corner labels. Every other
three-corner equation specializes to p=120, excluded here. Some parameters
allow higher-valence stars in an original tiling; the reviewed unrestricted
hexagon defect-free limit supplies a trivalent whole-side field without
assuming those stars absent in the original tiling.

The20 binary words with three zeros and three ones have exactly three
native dihedral orbits: C=000111, I=001011 and ALT=010101, of sizes6,12,2.
All nine ordered A,B combinations are thus included, with native side
indices transported along the same rotations/reflections. The species
phase forces B onto one index-three coset of the triangular cell lattice.

## Completed cases and their proof mechanisms

| A word | B word | Result for all actual metrics | Retained mechanism |
|---|---|---|---|
| C | C | Untileable or periodic escape | Functional colour backbone; periodic binary native-placement fibre |
| C | I | Untileable | Empty colour-ring triangle core |
| C | ALT | Untileable | Empty colour-ring triangle core |
| I | C | Untileable | Corrected geometric closure/sign exclusions; empty96-ring residual core |
| I | I | Untileable | All12288 native rings geometrically impossible |
| I | ALT | Untileable or periodic escape | Complete136 AB metric words:123 empty;12 index-six tori;1 index-nine torus |
| ALT | C | Untileable | No legal colour ring |
| ALT | I | Untileable | No legal colour ring |
| ALT | ALT | Untileable or periodic escape | Complete exact metric stratification;30 empty residual cores and7 direct index-three tori |

The four direct colour exclusions, C/C metric lifting and alternating
side-period-two gate are proved in the independently reviewed
[colour transport theorem](two-hexagon-rank-nine-colour-transport.md).
C/C retains two full native placements per colour word. Its metric edges
are equality tables between binary side-length maps; the separately reviewed
[binary fibre lifting lemma](periodic-binary-equality-fibre-lifting.md)
gives a finite-cover periodic point whenever an infinite point exists.
Colour periodicity alone is not used as full-placement periodicity.

The corrected [interleaved geometric/spatial exclusion](two-hexagon-interleaved-symbolic-closure-obstruction.md)
handles I/C and I/I. It uses exact rationalized direction matrices over
Q(sqrt(3))(t), t=tan((p-120)/2), the entire admissible real interval and
all exceptional rank values. An initial B=C direction error was caught
and its certificate withdrawn. The accepted corrected I/C proof additionally
needs a sound spatial deletion of96 residual states; the withdrawn local-only
argument supplies no premise. The independent review verifies all matrices,
minor gcds, sign partitions and spatial deletions.

The [all-metric I/ALT theorem](two-hexagon-interleaved-alternating-all-metric-escape.md)
first proves AA native self-indexing and the complete odd-A AB alphabet,
then handles every merged-length partition and B native word. Periodic
witnesses leave even A lengths independent. The equal-odd residue also has
an independently reviewed whole-plane [triangular carrier proof](two-hexagon-interleaved-alternating-equal-odd-carrier.md).

The [all-metric ALT/ALT theorem](two-hexagon-alternating-all-metric-escape.md)
uses the necessary side-class ledger to cover203 A-side partitions and39628
B words. Exact closure matrices, including all exceptional real rank strata,
exclude137 A-only partitions and all270 joint three-length cases. The
remaining20970 words form685 coupled native symmetry orbits;628 are excluded
by actual-class kernel equalities. The separately reviewed six-distinct-A-side
local obstruction removes the all-distinct cases. The remaining37 cases have
30 empty full-native transport cores and7 functional cores. All seven have
direct index-three native tori, with every star, seam and required equality
independently checked and no extra metric equality imposed. The entire
finite reduction and positive witness chain has passed independent replay.
ALT-specific closure matrices use t=tan((120-p)/2); this reverses the parameter
used in the interleaved calculation, and each family's convention is explicit.

In each periodic case a checked FULL native labeling matches the actual
polygon angles and lengths. The reviewed global encoding develops it into
an admitted periodic Euclidean tiling. In each empty case the same reviewed
limit would give a forbidden ring if an original partial-contact tiling
existed. These transfers establish the stated actual-polygon conclusion,
not just conclusions for rational angles or chosen bounded tori. QED.

## Remaining scope

Other hexagon angle types, extra admitted three-corner compositions, and
pentagons remain outside this complementary-angle family. Together with the
separate [unique-B-star theorem](two-hexagon-unique-b-star-impossibility.md),
this is a broader obstruction, not a complete two-convex-polygon
impossibility proof.
