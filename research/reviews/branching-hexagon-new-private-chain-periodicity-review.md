# Independent hostile review: fixed-B private-chain periodicity

Date2026-10-10. Reviewer partial_contacts; independent of the construction.

**Verdict: VALID after the seam-tangent repair, subject to root's separately
recorded fresh independent check of that repair.** The root's fresh valid
repair verdict was communicated to the author during this audit; retain that
verdict in the global checkpoint. This reviewer proposed the repair and is
not its sole reviewer.

## Claim and assumptions

Reviewed every step of
[branching-hexagon-new-private-chain-periodicity.md](../lemmas/branching-hexagon-new-private-chain-periodicity.md).
A has alternating unequal p,q, threefold symmetry and alternating angles
120+delta,120-delta with0<delta<60. B has exactly(r,p,q,q,q,q), all3 values
distinct; all10 three-qq angle multisets are forbidden. The primary theorem
quantifies over every ETE trivalent plane tiling. The unrestricted-pair
corollary uses the reviewed defect-free hexagon limit, and claims existence
of some periodic admitted tiling, not periodicity of every original tiling.
The all-original corollary separately assumes all B angles>90.

## Contact and orientation attacks

The unique r seam's reflection gives two rp sectors and missing pp, absent
from both shapes. Its half-turn gives rq/rp sectors and pq third. A B2
third would force beta0+beta1+beta2=360, hence a forbidden qq triple sum.
Both seam endpoints therefore use A with fixed angle kappa. Chirality is
physically fixed because an A p or q endpoint can carry only one of its
distinct alternating angles, and native equal-length slots are intrinsically
threefold-equivalent. The no-reflection statement correctly excludes
p=q,delta0,delta60.

For Bside2 the entire second endpoint is crucial. A Bside3/4 mate gives
three qq corners at its other endpoint, forbidden under all10 constraints.
Side5 globally already meets A; native2 reflected matching requires pp.
Thus same-slot half-turn2 is exhaustive. This fixes side3's A. Side4's B
mates2,3,5 are ruled out by their already forced neighbors, while4/4 would
again yield three qq. Angles at side4's two endpoints force beta4+beta5=240.
The equal120 option contradicts triple beta4, leaving120±2delta and therefore
delta<30. No assumption about finite tile frequencies occurs.

## Straight chains and the discovered defect

The midpoint segment has strictly positive length and interior strictly
inside each convex B. Same-slot half-turns on0 and2 continue it straight
at both ends. Degree2 components advance by a fixed distance, so cannot
cycle; two steps translate by the physical image of V2+V3-V0-V1.

The first proof said any distinct line through a seam midpoint immediately
enters one of the original B interiors. This fails for a line tangent to
that seam. The author repaired the argument: two incident B interiors fill
the local neighborhood off the seam; choose a nearby point on the second
chain line away from its discrete midpoint set, hence inside its own B tile.
Its open interior neighborhood must overlap an original B interior.
The same argument covers an intersection inside a first-chain segment.
This establishes pairwise disjoint infinite chain lines without a tangent
exception. Root independently checked the repaired step; no new defect
was found in the revised text.

Parallelism follows because infinite nonparallel lines intersect. All chain
period lengths equal the fixed nonzero magnitude L, hence their vectors
agree up to sign. Every B physical polygon set is invariant under one t.
B's unique adjacent r,p slots also eliminate intrinsic ambiguity about its
native indexing. Every A q side must meet B because A/A would require pp.
The uniquely forced A neighbors of all B tiles therefore comprise exactly
the entire A set, an isometry-equivariant function. Thus the period transports
to every A tile without a density or connectivity assumption on A contacts.

## Scope and dependencies

Species omission is excluded within ETE by the r-dimer argument and A's
pq-only corner graph. The unrestricted-pair conclusion obtains a periodic
ETE limit from a hypothetical arbitrary original tiling; it does not impose
ETE on that original. With all B angles>90, existence forces delta<30,
so all A angles>90 and the reviewed obtuse theorem applies directly.
No remaining gap in the stated claims was found. Resonant qq triples remain
outside the theorem. There is no claim of plane existence under nonresonance.
No finite computation is needed for the chain theorem.
