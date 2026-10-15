# Periodic escapes for convex hexagon pairs: unified scope and proof map

Date:2026-10-15. Status: independently hostile-reviewed VALID, including the exhaustive
case synthesis; see
[review](../reviews/hexagon-six-four-double-pair-hostile-2026-10-15.md). This is a structural partial result, not a full
solution of research-problem.md.

## Unified statement and proof map

This account combines two already reviewed results. It introduces no new
case classification or stronger periodicity claim. A genuine convex hexagon
has six actual corners, is compact, and has nonempty interior. Write d(P)
for the number of distinct numerical lengths among its six sides.

In both statements, the hypothesis is the existence of a plane tiling by
isometric copies of the two unmarked shapes. Arbitrary orientations,
reflections, partial contacts, and omission of a species are allowed. The
conclusion constructs an admitted tiling of the same shapes; it does not
assert that every original tiling is periodic or uses both species.

| Result | Numerical side-length hypothesis | Guaranteed periodic escape |
|---|---|---|
| A: six-distinct member, arbitrary partner | d(A)=6; 1<=d(B)<=6, with species interchangeable | At least one nonzero translation |
| B: both members have at least five lengths | d(A)>=5 and d(B)>=5 | Two linearly independent translations |

A single nonzero translation already contradicts the original definition
of an aperiodic pair. In Result A the proof guarantees a rank-one subgroup
of translations, but does **not** say the full translation subgroup has
exactly rank one: a second period may exist. Result B guarantees a rank-two
translation lattice. No upgrade of Result A's entire scope to rank two is
proved here.

### Proof of Result A

The theorem and exhaustive proof below establish Result A. After the
[defect-free limit reduction](hexagon-limit-and-periodicity.md), the
partner's numerical multiplicities give the following proof map. A limit
omitting a species is handled by the named monohedral escape, rather than
assuming that both species persist.

| Partner branch | Reviewed proof | Strength supplied |
|---|---|---|
| d(B)>=5 | [Six/five general theorem](hexagon-six-five-general-periodic-escape-2026-10-15.md) | Rank two |
| At most three lengths shared with A | [Three-shared-length theorem](hexagon-six-distinct-three-shared-periodicity-2026-10-15.md) | Rank two |
| Remaining d(B)=4, four shared lengths, multiplicities (2,2,1,1) | [Double-pair theorem](hexagon-six-four-double-pair-periodicity-2026-10-15.md) | Rank two |
| Remaining d(B)=4, four shared lengths, multiplicities (3,1,1,1) | [Private-AA-chain theorem](periodic-private-aa-chain-escape-2026-10-15.md) | At least one nonzero period |

These branches exhaust every partner. The last branch synchronizes periodic
A chains and finite-width B fillings using a common multiple of bounded
filling periods. That is the reason Result A is stated with one guaranteed
period. The other branches construct flat tori or use connected intrinsic
neighbor propagation, giving rank two. The detailed proof below retains
the exact hypotheses and links to their independent reviews.

### Proof of Result B

If either member has six distinct lengths, the [six/five general theorem](hexagon-six-five-general-periodic-escape-2026-10-15.md)
applies directly and supplies rank two. This uses the stronger theorem
for this branch, rather than inferring a second period from Result A.
Otherwise both members have exactly five lengths, so exactly one value is
repeated in each member. The following alternatives are exhaustive:

| Five-length palettes and repeat positions | Reviewed proof |
|---|---|
| Equal palettes, at least one adjacent repeat | [Common-five adjacent theorem](hexagon-common-five-adjacent-periodicity-2026-10-15.md) |
| Equal palettes, both repeats nonadjacent | [Complete nonadjacent common-five synthesis](hexagon-both-opposite-repeat-periodicity-2026-10-15.md) |
| Unequal palettes, both repeats nonadjacent | [Unequal nonadjacent theorem](hexagon-five-noncommon-nonadjacent-periodicity-2026-10-15.md) |
| Unequal palettes, at least one adjacent repeat | [Unequal adjacent theorem](hexagon-five-unequal-adjacent-periodicity-2026-10-15.md) |

Each branch supplies a doubly periodic escape. The [final independent
whole-claim review](../reviews/hexagon-five-unequal-adjacent-hostile-2026-10-15.md)
also audits this complete synthesis. Numerical palettes and actual contact
colors must not be conflated: any auxiliary colors are introduced only in
an existing source and discarded in the unmarked periodic conclusion.

### Combined consequence and publication boundary

For a hypothetical aperiodic pair of convex hexagons, Result A implies
that each member has an internally repeated length; Result B implies that
at least one member has at most four distinct lengths. Equivalently,

    d(A)<=5, d(B)<=5, and min(d(A),d(B))<=4.

This is a necessary restriction, not an existence theorem or a complete
classification of the remaining family. Pentagon-containing pairs remain
outside these two results. The original problem is unresolved.

The proof dependencies distinguish necessary finite support enumeration
from positive periodic witnesses and global strip filling. The component
proofs retain their exact domains, certificates, independent checkers,
external theorems, and review records. The [bounded literature record](../literature/hexagon-six-five-boundary-2026-10-15.md)
is the limit of the novelty assessment. A focused paper would still need
an external mathematical audit, a broader novelty check, and a minimal
reproducible supplement; this synthesis is not a priority claim or a
submission-ready manuscript.

## Theorem A: six-distinct member and arbitrary partner

Let A,B be any two genuine compact convex hexagons with nonempty interiors.
Assume A's six native side lengths are pairwise distinct. If the pair admits
any tiling of the Euclidean plane by isometric copies, including reflections
and unrestricted partial contacts, then it admits a tiling invariant under
a nonzero translation. Therefore it is not an aperiodic pair under the
original problem definition.

There is no restriction on B's side-length multiplicities, on numerical
length coincidences between the types, or on the original tiling's contacts
or absolute orientations. The conclusion is existence of one translational
escape, which is exactly sufficient to exclude aperiodicity. We do not
assert that every original tiling is periodic or that the final escape
always has two independent periods.

## Exhaustive proof by B's numerical multiplicities

Let b be the number of distinct numerical side lengths of B, and k the
number shared by A and B. Necessarily1<=b<=6 and k<=b.

If b is5or6, the reviewed
[six-distinct/five-or-more-distinct theorem](hexagon-six-five-general-periodic-escape-2026-10-15.md)
gives a doubly periodic escape. Its exactly-five branch exhausts adjacent,
separation-two and opposite repeats with exact finite actual-corner and
native-arm classifications.

If k<=3, the reviewed
[three-shared-length theorem](hexagon-six-distinct-three-shared-periodicity-2026-10-15.md)
gives a doubly periodic escape. This includes every b<=3 case. Its new
mechanism forces an alternating shared/private A word in any mixed
trivalent limit, every vertex AAB, a complete two-word B corona, and
connected deterministic private-AA contacts. If the limit contains only B,
the named unrestricted monohedral hexagon theorem gives its escape.

The only remaining case is b=k=4: all four numerical B lengths are shared
with A. Two A lengths are private. In a MIXED defect-free limit they cannot be
adjacent, since that would force a trivalent AAA vertex with a triangle
in A's six-cycle of corner length pairs. A B-only limit already gives the
monohedral periodic escape. Thus the two following mixed-case mechanisms
apply after handling that separate escape. A six-slot word on exactly four numerical lengths
has multiplicities either(2,2,1,1) or(3,1,1,1), exhausting the integer
partitions of six into four positive parts.

For(2,2,1,1), apply
[the double-pair theorem](hexagon-six-four-double-pair-periodicity-2026-10-15.md).
Its complete2160-linear-word/192-cyclic-word native-arm classification
retains93 possible actual supports. Seventy-one give direct four-triangle
rings; twenty-two give rings by retained rational combinations of actual
angle equations. Every ring constructs a compact flat torus with the
original polygon metrics and hence a doubly periodic plane tiling.
No solver UNSAT assertion or unproved finite-model property is used.

For(3,1,1,1), the B boundary can have adjacent equal sides at only its
tripled numerical value. It cannot have loops at two different lengths.
The reviewed
[private-AA-chain escape theorem](periodic-private-aa-chain-escape-2026-10-15.md)
applies: both A-private side mates are forced midpoint half-turns;
noncrossing periodic A chains have a common nonzero period; uniformly
finite-width separating bands admit finite-state periodic B fillings with
a synchronized common multiple of their periods. This constructs an
admitted tiling with a nonzero translation. It does not silently replace
partial contacts by an edge-to-edge hypothesis: the original unrestricted
pair first supplies a defect-free limit by the previously reviewed theorem.

These cases exhaust every B, proving the statement. QED.

## What remains for the main research problem

A hypothetical aperiodic pair of two convex hexagons must therefore have
an internally repeated side length in EACH member. By Result B above,
at least one member must additionally have at most four distinct numerical
side lengths. The remaining repeated-side branching is unclassified. The other globally surviving class still
contains a pentagon. No implication to unrestricted impossibility for all
pairs, or to an explicit aperiodic pair, follows from this theorem.

The new result is relative to the
[documented bounded novelty search](../literature/hexagon-six-five-boundary-2026-10-15.md).
It strengthens the earlier two-distinct-sided theorem by imposing distinct
sides on only ONE hexagon. No universal priority is claimed.

## Exact computations and proof dependencies

The geometric defect-free, monohedral, uniform-occurrence and planar-group
facts are named in the linked component proofs. The new mathematical
periodic-chain proof has no computational dependency. The finite numerical
word domains for the exactly-five cases sum9450 normalized records, and
B-double-pair adds2160 linear records. These are word encodings with stated
symmetry conventions, not a count of noncongruent geometric tile pairs.
All proof-relevant finite decisions are integer combinatorics or explicit
rational row identities, replayed against retained certificates with
separate independently written verifiers. Default producer commands do not
overwrite retained evidence. See the component proofs for complete commands,
finite bounds, trust boundaries, and hostile review paths.

The standalone synthesis has no additional search or hidden geometric
realization assumption: a given plane tiling supplies all actual-corner
angle equations, and each invoked result either constructs its periodic
escape or produces it by the stated uniform strip-filling argument.
