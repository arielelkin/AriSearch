# Twelve branching pair-graph residues: exact four-state wheel actions

Date: 2026-10-12. Status: [constructive wheel implication reviewed VALID](../reviews/two-hexagon-unique-b-star-impossibility-review.md#new-complete-wheel-corollary).
The twelve retained branching residues belong only to the stated unique-B-pair
metric domain. Their periodic escapes are also covered by the [complete family audit](../reviews/two-hexagon-odd-pair-graph-orders-review.md).

## The new spatial mechanism

A B-ring state q has one B placement and six full A placement symbols.
Write R_k for overlap in direction Delta_k, as in the
[exact ring reduction](two-hexagon-one-b-ring-spatial-reduction.md).
Although each residue has some R_k outdegrees two, a full wheel around
q is a tuple (v_0,...,v_5) satisfying

    q R_k v_k;
    v_k R_(k+2) v_(k+1),  k modulo six.

The second relation follows from Delta_(k+1)-Delta_k=Delta_(k+2).
Every actual full-plane field supplies such a wheel. Each origin has at
most 2^6 possible tuples in these residues.

Exact reconstruction finds **one wheel per state** in every residue.
Call its six entries W_k(q). All W_k are permutations of the twelve
states, and independently checked identities are

    W_(k+3)=W_k^(-1),
    W_0 W_1 = W_1 W_0,
    W_2 = W_1 W_0^(-1).

Thus they are a genuine action of the B lattice rather than merely
locally compatible transition proposals. For any chosen origin q0,

    q_(a*Delta0+b*Delta1) = W_0^a W_1^b(q0)

is an actual full-plane ring field: the identities give all six overlap
relations. Each of the twelve states belongs to one of three orbits of
size four. Its stabilizer therefore has index four in the B lattice,
or index twelve in the original cell lattice. The exact ring lifting
produces an original twelve-cell torus.

This also supplies a structural conclusion about arbitrary actual
fields: their wheels force the same deterministic action, so they belong
to these finite four-state orbits. It is not necessary to infer extension
from a nonempty pruned core, nor to trust a solver's positive result.

## Stripe and skew cases

For six residues, each four-state orbit has a lattice direction fixed
by W_k. They are stripes with period one in that direction and four in
an adjacent direction. For example row374 has the common R1/R2 cycle

    0 -> 6 -> 9 -> 3 -> 0

and R0 self-loops on those four states, giving periods Delta0 and
4*Delta1. Its other two orbits give rotated stripe directions.

The other six residues have four-state actions with skew stabilizers.
For row418, W0 has the cycle 0->11->8->3->0 while W1=W0^2 on that orbit.
Its periods include 4*Delta0 and Delta1-2*Delta0. Both situations have
exact four-state quotients; neither is restricted to index-three or
index-six tori. This explains why the earlier index-at-most-eight metric
gate left them unresolved.

## Universal metric transfer

For each residue, the equivalence closure of the twelve seam equalities
in **every** surviving ring is the same side relation e0. The verifier
reconstructs those equalities from native labels, instead of trusting
stored length classes. Every constructed torus uses side pairs whose
closure is exactly e0.

If X(T,e) is nonempty, any occurring ring forces e0 contained in e.
Consequently the retained torus is legal for that e. By the reviewed
global development theorem, any actual convex pair with this exact type
is untileable or admits a periodic tiling. No simultaneous polygon
realisability test is necessary for this escape implication.

The twelve residue IDs are

    374,418,923,1155,3627,4148,
    5482,5757,5998,8614,9887,10940.

## Independent exact artifact and replay

The [standalone verifier](../reviews/verify_two_hexagon_residue_wheel_action.py)
imports no pruning producer, SFT implementation, CP-SAT or geometric
solver. It independently reconstructs every native central star, each
ring seam's equality closure, full-symbol overlap relations, and all
wheel tuples. It then verifies the permutation identities and constructs
one native torus for each of the three four-state orbits per residue.

For all 36 tori it checks every corner star, every full-side match,
period wrapping, the exact used-triple set, and equality closure of every
used side pair. The [retained certificate](../certificates/two-hexagon-residue-wheel-action.json)
records source digests, wheels, orbits, Hermite period lattices and full
24-symbol native labels. All 36 have index twelve. This artifact proves
the residue escapes independently of any retained negative solver verdict.
Its identification of the twelve residues relies on the separately
reviewed full domain/pruning census; it does not regenerate that census.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_hexagon_residue_wheel_action.py --check research/certificates/two-hexagon-residue-wheel-action.json
