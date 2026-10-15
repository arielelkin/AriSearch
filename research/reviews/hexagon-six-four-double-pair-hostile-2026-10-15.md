# Independent hostile review: A-six/B-four double-pair periodic escape

Date: 2026-10-15. Component verdict: **VALID**. No unresolved mathematical
or computational defect found within the stated hypotheses.

Reviewed claim:
[hexagon-six-four-double-pair-periodicity-2026-10-15.md](../lemmas/hexagon-six-four-double-pair-periodicity-2026-10-15.md).
A has six different native side lengths; B has four, with multiplicities
(2,2,1,1), all shared with A. Tileability with unrestricted contacts and
all isometries implies a doubly periodic escape. If a mixed defect-free
limit exists, a four-face torus using two copies of each shape suffices.

This reviewer did not develop the double-pair proof, its search, its row
certificates, or its torus selection. The reviewer earlier developed the
separate three-shared-length theorem; that theorem is not used in this
component audit. Its independent review is cited only in the later synthesis
check, not replaced by self-review.

## Independent exact replay

A new standalone standard-library verifier was written without importing
any producer or earlier verifier:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-four-double-pair-independent-2026-10-15.py

Result: **PASS**. It reads the new narrow proof-only certificate
[hexagon-six-four-double-pair-certificate-2026-10-15.json](../certificates/hexagon-six-four-double-pair-certificate-2026-10-15.json).
It independently obtains:

- 2,160 linear words and 192 B-dihedral representatives;
- 24 words retaining a closed twelve-corner cover;
- 93 complete endpoint-closed covers, including 71 direct-ring covers;
- 22 remaining covers certified by 88 exact rational row equalities;
- maximum pruned atlas size 12, with every subset examined;
- 26 formal side-slot selections, each explicitly verified to give the
  claimed four-face orientable torus and its eight trivalent vertices.

The two private-pair cases have respectively 27 and 66 covers. Their
71/22 split is respectively 27/0 and 44/22. All 24 table rows in the written
proof agree with the independent output, including the two 27-cover words
with eleven rational-span cases each. No relevant domain is skipped.

The narrow producer was rerun and its parsed JSON compared exactly with the
retained certificate: **PASS**. The updated small row checker also passed:
24 words, 71 direct inclusions, 22 rational certificates. That extra replay
is supplementary; the independent verifier checks those obligations itself.
No Z3, Sage, symbolic elimination package, numerical angle model, stochastic
seed, or period-size bound is part of this audit's computational trust base.
Python integer arithmetic, Fraction arithmetic, and the written geometry are.

## Domain completeness and all reflected native contacts

In a mixed defect-free limit, an A corner between two private lengths would
have A neighbors across both sides and hence be an AAA vertex. At such a
vertex no ray lengths can repeat, since A has no equal adjacent sides; its
three pairs would form a triangle in A's numerical corner graph C6, which
is impossible. Thus its two private slots are nonadjacent. The only distances
up to A's dihedral relabeling are two and three, represented by {0,2} and
{0,3}. This normalization uses abstract numerical labels, not an unproved
Euclidean symmetry of A or a change to its actual corner angles.

For each resulting four-symbol B alphabet, the independent verifier chooses
the two doubled symbols and takes every permutation of the resulting
multiset. It obtains 1,080 distinct linear words and 96 dihedral classes.
Its coverage does not rely on the producer's surjective-word generator.
Both polygon orientations and arbitrary reflected placements are included.
No order relation between actual numerical lengths is assumed by relabeling.

The independent local encoding differs materially from the producer. It
forms all 24 directed native corner ports, retaining left/right side slots
and the actual far endpoint of each arm. It then enumerates EVERY ordered
cyclic triple of ports whose ray lengths match. It does not begin with
numerical ray triangles and does not assume that sorted corner order plus
eight flips is complete. Its resulting stars and simultaneous far-pair
microstates agree exactly with the narrow certificate, including the full
initial atlas before pruning. This checks the producer's three-corner
ordering quotient and repeated-ray handling independently.

Repeated native corner indices remain separate occurrences. In particular,
the far pair (c,c) is supported only when the target star contains c at least
twice. The independent verifier computes pair supports by selecting actual
positions in each star; it never tests plain set inclusion for multisets.

## Endpoint pruning, actual supports, and angle implications

For an actually occurring star choose its actual native-arm cyclic order.
Its three full matched rays lead to actual far-end stars containing the
specified endpoint pairs. Thus every actual support survives the iterative
pruning. Each surviving star needs ONE microstate satisfying all THREE
far-pair requirements simultaneously; allowing a separate microstate per
ray would be weaker and was not substituted. The independent program
reconstructs this condition and exhausts every subset of every retained
atlas. Every actual support covers all twelve native corner slots because
both whole prototile types occur. No extension of a locally admissible
support is assumed.

For each of the 93 independently found supports, the narrow certificate
lists exactly that support once. Seventy-one have an explicit certified
ring contained in the support. For every other support, its certificate
uses exactly its own occurring-star rows plus the two hexagon angle rows.
The verifier multiplies all coefficients as Fraction values and checks all
thirteen entries for each target ring row. It does not trust the producer's
Gaussian-elimination implementation or a SAT/UNSAT status.

The constant entries -2 and -4 correctly express angles in units of pi;
repeated corners contribute their full multiplicities. Negative rational
coefficients are legitimate because these are equality consequences.
A target ring star need not occur in the given tiling: its angle sum follows
for the ACTUAL existing polygon angles, and the separate flat torus uses
that newly proved legal angle sum. This is the central quantifier point.
No abstract angle solution is promoted to a realizable convex polygon.
An algebraically inconsistent support cannot harm the implication, since
an actual tiling already supplies a consistent angle vector.

## Formal ring geometry and explicit torus audit

For each B word choose one actual B slot for each shared numerical value.
The unchosen slots get different private formal symbols. A's two private
lengths likewise remain private. Formal equality always implies numerical
length equality; splitting an equal numerical value into distinct formal
symbols selects allowed matches and never adds a forbidden match.

The independent program reconstructs all formal corner graphs and requires
four triangles partitioning all twelve actual corner slots. For EVERY
retained slot selection, not merely one visually chosen pattern, it then
constructs all twelve complete side pairings on A0,A1,B0,B1. It chooses B's
reference orientation from its common cyclic order, reverses paired boundary
endpoints, and checks numerical length equality and use of each of the
24 side occurrences exactly once.

It explicitly forms the corner-link graph on all 24 face corners. Each
corner has degree two; every connected link has three corners; there are
eight links; and each of the four target actual-corner triples appears
twice. It also checks connectedness of the face adjacency graph and
8-12+4=0. Boundary-reversing pairings and circular links give a connected
closed orientable surface, hence a torus. Repeated numerical lengths do not
identify additional native corners or sides beyond the specified pairing.

The actual polygon metrics match on paired edges. The certified ring rows
make every quotient cone angle 2pi. The compact quotient is therefore a
complete flat torus. Its complete simply connected flat universal cover
develops isometrically to the plane, producing whole original polygon
copies with disjoint interiors and complete coverage. Its deck group is a
rank-two translation lattice. This unbounded step uses the reviewed flat-
torus construction, not a bounded patch-extension inference. Reflected B
references are allowed by the problem's original definition.

## Unrestricted contacts, omissions, and limitations

The defect-free theorem is correctly invoked only to obtain some trivalent
whole-edge tiling from an arbitrary unrestricted one. It need not preserve
the original tiling's type frequencies. An A-only limit is ruled out by C6;
a B-only limit invokes the reviewed monohedral hexagon periodicity theorem.
The mixed case uses all twelve actual corners and the finite classification.
Thus the theorem covers omissions, partial initial contacts, arbitrary
rotations, and reflections, while asserting existence of a periodic escape
rather than periodicity of every admitted original tiling.

No substantive mathematical repair was needed. During review the author
isolated the proof-only (2,2,1,1) producer and certificate from the earlier
broader exploratory file. The independent verifier was switched to this
narrow record, rechecked all its explicit supports, and passed. This removes
irrelevant exploratory solver calls from the replay path without changing
the theorem or the finite proof data.

Novelty is outside this validity verdict. The theorem alone does not cover
B multiplicities (3,1,1,1), two repeated-side hexagons, pentagons, or arbitrary
pairs of convex polygons.

## Additional audit of the one-distinct-hexagon synthesis

The root requested an audit of
[hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md](../lemmas/hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md).
The case union and original quantifiers are **VALID**, using the independently
reviewed components named there. This is a synthesis audit, not a fresh
independent review of this reviewer's own three-shared component.

For b distinct lengths in B and k common lengths, 1<=b<=6 and k<=b.
The b>=5 branch invokes the reviewed six/five-or-more theorem. The k<=3
branch invokes the separately reviewed three-shared theorem, covering every
b<=3. Everything left has b=k=4, whose positive multiplicities partition six
as exactly (2,2,1,1) or (3,1,1,1). The first is the component fully audited
above. In the second B has loops at no more than one numerical length,
exactly the hypothesis of the independently reviewed private-AA-chain
escape theorem. All component hypotheses match and all cases are exhausted.

The union correctly asserts a NONZERO translational period, since the
private-chain strip-filling component does not assert two independent
periods. It allows all original contacts and isometries and needs only one
periodic escape. Consequently a hypothetical aperiodic two-hexagon pair
must have a repeated native side length in each member; this says nothing
conclusive about arbitrary such repeated-side pairs or pentagon pairs.

One small wording clarification was sent to the root and repaired. The
final synthesis explicitly qualifies nonadjacency of the A-private slots as
a statement about a MIXED defect-free limit, and explicitly handles a B-only
limit by its monohedral periodic escape. The repaired passage was reread.
No broader necessity for an unused A in a monohedral B tiling is asserted.

Final synthesis verdict: **VALID**, with no unresolved qualification within
its stated one-distinct-hexagon scope. This is still not a resolution of the
full two-convex-polygon problem.
