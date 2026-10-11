# A generic Cairo dichotomy:155 arm-pattern obstructions and32 periodic patterns

**Status:** independently hostile-reviewed **VALID** with exact finite
reconstruction of both209 classifications and all32 sufficient maps; see
[review](../reviews/partial-contact-cairo-generic-arm-patterns-review.md).
The new swapped-arm full-cone review is also VALID.
The already used private-arm/two-T and Y dependencies have their recorded
independent reviews. No unrestricted target or novelty claim is made.

## Exact statement and genericity

Let P,Q be strictly convex Cairo-angle pentagons, with angles after successive
sides(a,b,c,d,e) equal(90,120,90,120,120) degrees. Suppose the four arms
a,b,c,d of each separately are pairwise distinct. Their cross-arm equality
pattern is a partial bijection M between indices0,1,2,3 of the two shapes.
There are exactly209 such partial bijections.

Set w=sqrt3. Let H_M be the real linear subspace defined by each shape's
closure b-c=w(d-a) and exactly the indicated cross-arm equations. Its fifth
length is e=w*c+d-2a for each shape. A metric is **generic in H_M** if:

1. no undeclared arm equality holds;
2. two right-corner event sums are equal only if their difference vanishes
   identically on H_M;
3. no e length equals any event sum;
4. e_P=e_Q only when that equality is an identity on H_M.

Events pair equal perpendicular arms of native90 corners; their sums are
the two opposite collinear arm lengths r+s. Their finite definitions and
two-T geometric necessity are in the self-contained
[two-T lemma](partial-contact-cairo-two-t-switch.md).
The genericity exclusions are proper hyperplanes whenever their defining
form is nonzero. They are relative to each actual shared-arm stratum,
not a claim that shared-arm equality is generic in the full6D metric cone.

**Theorem.** Every pair satisfying these hypotheses is either untileable or
admits a doubly periodic plane tiling. Of209 arm patterns,22 force additional
arm equalities,155 are untileable on their generic positive strata and32
have periodic escapes from two sufficient cones. Thus no such generic
internally-distinct-arm Cairo pair can be aperiodic. Exceptional proper
hyperplanes and internal arm repetitions remain outside the theorem.

## The necessary contact computation

For each209 pattern form the exact QQ(sqrt3) closure matrix and its nullspace.
Zero quotient coordinates decide identity of any linear form.22 patterns
force extra undeclared/internal arm equalities and have no metric satisfying
the stated pattern. All187 others have positive open metric cones.

For each actual native arm slot i, let other(i) be its incident90-corner
other arm. Define the anchored event sum set

    S_i={length(i)+length(j): length(other(i))=length(other(j))}.

Here j ranges over actual native arm slots of either species, including i.
The two-T switch at a ray opposing slots i,j requires an event containing
that actual original bank slot on each end, not only its numerical length.
Thus unequal slots i,j can oppose only if S_i and S_j share an identical
quotient sum form. Equal lengths can whole-match directly. These tests
exclude the nonidentical event-sum equalities by genericity and still drop
the strict switch offset inequalities, a safe overapproximation. No
transitive closure of slot compatibility is taken.

The initial unanchored bank-label overapproximation had147 obstructions
and40 local survivors. Refining to actual original slots kills8 additional
patterns, giving155 obstructions and32 survivors. Both computations are
retained explicitly; old status fields are not relabeled as stronger ones.

Both fifth sides are unsplit by condition3. They whole-match to an e side;
condition4 determines the allowed species of that mate. For any possible
H/G e mate, both endpoint identifications are tested. The exposed arm pairs
are(d_H,d_G),(a_H,a_G) for preserved labels or(d_H,a_G),(a_H,d_G) for reversed
labels. Each endpoint needs a third isolated120 corner(b,c) of some species
with both rays compatible. The third corner cannot be e-adjacent because
its unsplit e could not oppose a90-to120 arm.

155 patterns cannot provide an e mate for at least one species under this
safe contact overapproximation. That species cannot occur. The reviewed
[private-arm theorem](partial-contact-cairo-private-arms.md) applied to a
single species excludes a monohedral tiling with four distinct arms, so
both species must occur in any admitted tiling. Thus all155 patterns are
untileable throughout their generic positive stratum.

The remaining32 are only necessary local survivors at this stage. Their
actual global periodic tilings come from the following separate proof.

## Actual native symmetry and the eight sufficient patterns

The Cairo native angle word is preserved by reflection reversing arm
indices i->3-i and fixing the e slot. Either species can be reflected
independently; species may also be exchanged. These operations are actual
isometries/relabelings of the unmarked shapes, not an imposed chirality rule.

All32 final survivor patterns contain one of the following8 two-equality patterns
(in each tuple the first index belongs to P and the second to Q):

| Family | Sufficient patterns |
| --- | --- |
| Swapped-arm cone | {(0,2),(2,0)}, {(0,1),(2,3)}, {(1,0),(3,2)}, {(1,3),(3,1)} |
| Existing Y cone | {(1,3),(2,0)}, {(0,1),(3,2)}, {(0,2),(3,1)}, {(1,0),(2,3)} |

The first row is exactly the reflection/species orbit of{(0,2),(2,0)}.
Those equalities normalize the side words to

    P=(a,b,c,d,e), Q=(c,B,a,D,f).

Their vector closure forces exactly
b=c+w(d-a), B=a+w(D-c), e=w*c+d-2a, f=w*a+D-2c.
All forms are positive because the actual polygons are genuine. Therefore
these actual shapes lie in the full
[swapped-arm periodic cone](partial-contact-cairo-swapped-arms-periodic.md),
whose whole-plane boundary/area construction supplies their periodic tiling.
It does not replace either of the user's given shapes with a chosen partner.

The second row is exactly the orbit of{(1,3),(2,0)}. To match the already
reviewed
[Y compatibility theorem](general-y-pentagon-periodic-partner.md), put
its native vertex0 at our first90 corner. The Y normalized side words are
P_Y=(b,c,d,e,a), Q_Y=(b_Q,c_Q,d_Q,e_Q,a_Q), with theta=120 degrees. Its exact
criterion Q_Y(2)=P_Y(0), Q_Y(4)=P_Y(1) becomes d_Q=b_P,a_Q=c_P, precisely
{(1,3),(2,0)}. The Y proof supplies a convex central-hexagon carrier and
periodic four-face tiling for every actual positive metric satisfying these
equalities. That theorem does not require its separate large-lambda partner
selection when applied as a given-pair compatibility criterion.

All8 k=2 necessary survivors are exactly these8 patterns.24 of the32 k=3
survivors contain one as a subset. The retained certificate records for each
of these32 covered survivors the selected sufficient subset, family and
exact independent-native reflection/species-swap map. A third equality merely
restricts the same already proved cone; it does not change its positive
coverage proof.

The8 initial unanchored k=3 survivors without such a subset form the orbit
of{(0,3),(1,0),(2,1)}. They are all excluded by the anchored native-slot
filter. In a normalized representative the words are

    P=(a,b,c,d,e), Q=(b,c,X,a,f),

with distinct declared arms. An apparent P a/P c ray match in the old
bank-label compatibility used a shared perpendicular b event with banks a,c.
But the P c slot's actual perpendicular d is private, so its event has banks
c,c. Their sums cannot agree without an extra excluded event equality or
a=c. Anchoring exposes this defect in the local overapproximation. The
complete209 computation applies the correct slot test at every endpoint.
No plane existence was inferred from the initial40 local outcomes.

An initial claim that all40 mapped to sufficient cones failed an exact subset
assertion before any all40 certificate was produced. It was corrected to32
periodic/8 unclassified, then the independently verified anchored contact
invariant resolved those8 negatively. The final theorem uses only the
155/32 anchored result and the exact32 valid cone maps.

## Exact evidence and limits

The exhaustive209 computation is
[partial-contact-cairo-generic-arm-patterns.py](../searches/partial-contact-cairo-generic-arm-patterns.py),
with [full finite search record](../searches/partial-contact-cairo-generic-arm-patterns.md)
and [certificate](../certificates/partial-contact-cairo-generic-arm-patterns.json).
The independent root checker
[verify_cairo_generic_arm_patterns_independent.py](../reviews/verify_cairo_generic_arm_patterns_independent.py)
uses a different reduced label basis and independently returns155/32,
while retaining the original147/40 comparison. It has no author imports.
It has no symmetry reduction, floating decisions, randomness or timeout.
The finite counts, anchored actual-slot/e-seam tests and32 subset-map checks are
computer-assisted components; every retained result and map has passed the
independent reconstruction. Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-generic-arm-patterns.py

The exact proof of the new full metric cone is separate and is not replaced
by one fixture or the40 local results. The classification does not cover
internal arm repetitions or exceptional proper hyperplanes where new event
sums or e-hosted subdivisions become possible. It also does not assert that
every tiling of the periodic families is periodic. Those scope distinctions
are essential to the main problem's quantifiers.
