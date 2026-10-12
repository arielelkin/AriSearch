# Independent review: horizontal two-junction hat congruence obstruction

Date: 2026-10-12. Verdict: **VALID**, within the stated fixed-word scope.

## Claim and independence

Reviewed [the horizontal two-junction lemma](../lemmas/hat-horizontal-two-junction-congruence-obstruction.md).
For normalized Tile(1,b), b>0, its four fixed cyclic words comprise two strict
hexagons and two strict pentagons, with V horizontal and strictly left of h8,
and the flat h8 suppressed on P1. No genuine partition of these words has
only two congruence classes. This is an obstruction to this compiler, not to
other hat partitions, relaxed convexity, or arbitrary two convex tile pairs.

The [fresh exact checker](check_hat_horizontal_two_junction_independent.py)
reconstructs the13 outline coordinates over Q(sqrt3), uses a symbolic b, and
imports no producer or congruence certificate. Its real embedding is exact.

## Necessary side inventories and exceptional equalities

The source edge lengths around h0..h4 are b,1,2,1; around h4..h7 are b,b,1;
around h8..h11 are b,b,1; around h11..h0 are1,b. The horizontal displacement
h7-h8 is(1,0), so a V strictly left of h8 has distances K and K+1 to h8,h7.
Adding the cut-side lengths gives precisely both multiset equalities stated
in the lemma. Since strict hexagons and strict pentagons cannot be congruent,
a two-class realization must make the respective hexagons congruent and the
respective pentagons congruent. Consequently their side multisets must agree.

Cancellation in these multisets does not require unequal values. The pentagon
residual{K,b}={F,D} has exactly the two named assignments, which overlap at
coincidences. In F=b,D=K, cancellation in the hexagon residual forces
{1,2}={K+1,K}, and positivity forces K=1. In F=K,D=b the residual is
{1,2,K}={b,b,K+1}. Its repeated b requires K in{1,2}; K=2 leaves an unmatched3,
while K=1 gives b=1. Thus every assignment, including repeated values, has
K=D=1,F=b. The derived V coordinate is exactly h8-(1,0).

## P2 convex branch and complete pentagon angle test

At K=1 the P2 consecutive turns in order V,h8,h9,h10,h11 are

    (3b-sqrt3)/2, b, sqrt3*b²/2, b, (3b-sqrt3)/2.

The positive h8 turn fixes counterclockwise orientation. Strict convexity
therefore requires b>1/sqrt3. Equality collapses the h11-V side; the lower
branch has negative turns and cannot be rescued by changing word orientation.
On the admitted upper branch, normalized edge directions give interior-angle
cosines(-1/2,0,-1/2,0,-1/2), hence the exact120,90,120,90,120 angle word.

At h0 of P3, the incoming direction is270 degrees. Its inherited h12 turn is
positive, so strict P3 has counterclockwise orientation. Any congruence with
P2, whether cyclic or reflected, makes its h0 angle90 or120. The outgoing
h0-W direction must therefore be0 or330 degrees. F=b fixes its length and
gives exactly W=(b,0) or W=(sqrt3*b/2,-b/2). No length uniqueness or chosen
vertex correspondence is assumed in this angle argument.

## Both directions fail over their complete parameter branches

For W=(sqrt3*b/2,-b/2), the exact P0 turns at W and h4 are
(sqrt3*b-3)b/2 and -sqrt3*(sqrt3*b-3)/2. Their signs are opposite for every
positive b except b=sqrt3, where W=h4. Thus no strict P0 exists at any b.
The D=1 constraint happens to hold identically for this W and supplies no
missing exceptional rescue.

For W=(b,0), D²-1=b((2-sqrt3)b-1). Since b>0, its sole positive root is
2+sqrt3. Substitution gives the h4 turn exactly-5/2. The discarded root b=0
is outside the normalized source hypothesis. These two cases exhaust the
angle-imposed directions, so full congruence enumeration is unnecessary.

## Positive partition example and audit limits

The checker independently verifies the stated b=sqrt3,V=(2,0),
W=(7/6,-sqrt3/6) example. Every nonincident vertex is strictly left of every
piece's directed edge, each pair of convex pieces is separated by a supporting
line, and their total area equals the source area. Splitting the P1 h7-V edge
at its suppressed h8, all internal directed seams cancel exactly and leave
the13 source boundary edges. Thus this is a strict disjoint partition of the
hat, rather than only four individually convex polygons.

No defect or required producer repair found. The theorem is an exact local
congruence obstruction for the specified words and horizontal V. It neither
asserts all hat decompositions are obstructed nor imports any infinite tiling
recognition claim.

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_hat_horizontal_two_junction_independent.py
