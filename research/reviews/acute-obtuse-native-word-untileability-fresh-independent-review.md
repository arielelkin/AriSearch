# Fresh independent review of all-metric acute/obtuse native-word untileability

Date: 2026-10-12. Verdict: **VALID**.
Reviewer: fresh delegated hexagon/ternary agent, without construction history.

## Exact reviewed claim and assumptions

Reviewed [the native-word theorem](../lemmas/acute-obtuse-native-word-untileability.md):
any fixed genuine strictly convex pentagons with native angles
A=(65,140.5,147.5,75,112), B=(40,144.5,136,47,172.5) admit no plane tiling,
for arbitrary positive realizable side metrics, rotations, reflections,
partial contacts, valences and omission. The proof does not require the
normalized sample metrics, an invariant density, finite local complexity,
or any pentagon defect-free limit.

The [independent checker](check_acute_obtuse_native_word_capacity_independent.py)
imports no producer module or retained certificate. It reconstructs the entire
native180/360 language directly from the doubled-integer angles, including
all valences through9, and examines every one of20 native partner/end orders
for A1. All asserted angular tables pass exactly.

## Hostile local geometry checks

The sole flat fan is(alpha,beta,gamma). Consequently z,x,delta,u,w cannot
lie on the interior of another tile edge. For two positive collinear seam
rays starting at a common vertex, unequal far distances would put the shorter
ray's native endpoint inside the other's edge. If both far corners are
non-flat-eligible, this is impossible. Thus their distances coincide.
When their two native angles exceed180, their coincident far vertex cannot
have an additional flat host sector and must use a complete native360 star.
These facts apply without reflected-orientation restrictions.

In(alpha,x,x), an x-to-alpha seam using A1 has far pair z/z or z/y;
no complete star contains either pair. Both x copies must therefore face
alpha with A2, leaving their mutual seam as A1/A1 with far z/z, impossible.
This eliminates the whole star independently of any metric equality.

Every x then lies in P=(x,gamma,w), and every delta in D=(z,beta,delta).
Every w lies in P or Q=(z,v,w). The complete A1 partner census is exactly
A2,B0,B3,B4 with the endpoint orders in the theorem. The A2 partner forces
the forbidden(alpha,x,x), while B3/B4 consume Q at the source A tile's unique z.
No reversed endpoint order or coincident side-class alternative is missing.

For B0, the third beta corner at D can meet the source A0 with A2 or A3.
The A3 branch creates an A2/B1 seam with far pair x/u; both far corners are
non-flat, and their residual76.5 is absent from the full census. The A2 branch
has far alpha/x. A0>A2 would place non-flat x inside A0; equality would give
the forbidden(alpha,x,x). Hence A0<A2, and alpha lies in the A2 host interior,
necessarily at T. An individual B0 patch is not ruled out pointwise: its T
is the precise bounded-distance resource required for the final counting.

## Injection, sparse-defect and boundary audits

For a fixed pair of actual polygons, anchors in a fixed-width annulus number
O(R): tile interiors are disjoint, tile areas have a positive minimum and
all their regions lie in a bounded expansion of that annulus. Starred vertices
number O(R) there as well, since each is a native corner of one of finitely
many nearby tiles. Uniform vertex separation is unnecessary. Every corner,
side and tile association in this proof has bounded displacement depending
only on the fixed pair, so shifting a counting disk changes counts by O(R).

P uses distinct gamma corners; T uses an additional distinct gamma corner.
D uses distinct beta corners; T uses an additional distinct beta corner.
Thus b>=a+T-O(R) and a>=b+T-O(R), giving T=O(R), |a-b|=O(R).
Counting w with its sole supports P/Q gives Q=O(R). No positive species
density is assumed in these deductions.

Each whole A1/B0 side injects into T through its source A tile's unique alpha;
T contains exactly one alpha. Each whole A1/B3 or B4 side injects into Q
through its source A tile's unique z; Q contains exactly one z. A partial A1
has an interior junction whose flat host is A1 and whose corner fan is T.
Choosing one such junction per partial A1 is injective because two positive
flat host sectors cannot coexist with positive native corners at a vertex.
If A1 had no interior junction, a single opposite native side must contain
it; its two non-flat-eligible source endpoints force whole equality, so no
unclassified partial-side case remains.

The two T injections need not be disjoint from each other, and the proof
correctly counts them separately as2T. Therefore a<=2T+Q+O(R)=O(R), then
b=O(R), contradicting the Omega(R²) tile count necessary to cover the plane.
The estimates include configurations with sparse defects or a vanishing
species density. Monohedral omission cannot escape the same contradiction.

## Defects, repairs and remaining uncertainty

No defect found and no producer repair required. The scalar angle census,
endpoint ordering and all named resource supports have an exact independent
check. The geometric continuation and injectivity arguments were checked
analytically; they are not numerical solver claims. Different native corner
orders and different angle values are explicitly outside scope. The theorem
does not exclude the author's separate rearranged-word construction family.

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_acute_obtuse_native_word_capacity_independent.py
