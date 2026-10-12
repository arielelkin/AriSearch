# Fresh hostile review of the one-B ring spatial reduction

Date: 2026-10-12. **Verdict: VALID within the stated all-2A+1B domain.**
Reviewer independent of `two-hexagon-one-b-ring-spatial-reduction.md`.
This is a second mathematical review of the corrected deterministic
propagation bound, with separate scrutiny of the one-direction argument.
No new solver outcome is asserted.

## Exact encoding and phase

Opposite third cells of two elementary triangles sharing an A/A edge are
separated by Delta_k=D_k+D_(k+1). Subtracting their one-B equations forces
B occupancy constant on the index-three lattice L. Each elementary
triangle represents all three cosets, so exactly one entire coset is B.
Species periodicity alone does not determine orientation labels.

The ring state carries full placement symbols. Its twelve checked seams
are exactly the six B/A and six A/A edges in the seven-cell patch.
Adjacent B centers share two A cells, with neighbor indices k+4,k+3
relative to the second center; relation (1) identifies their full symbols.
Each A cell belongs to three B rings whose centers form an L triangle,
and pair overlaps enforce equality of all three assignments. Every star
is centered at its unique B and every seam is checked in such a ring.
Thus the inverse construction has neither missing stars nor missing
metric seams. Side restrictions only shrink the state and relation sets.

## One direction requires no indegree hypothesis

Restrict any actual field to a complete row in the tested direction.
Its state sequence is indexed by all integers and follows a partial
function on a finite set C. For an arbitrary chosen index n, two indices
in its infinite past have equal states. Forward uniqueness then gives a
directed cycle. Such a cycle cannot exit, so the chosen state lies on it.
This argument applies at every index, excluding transient tails even
though the abstract partial function can have many predecessors.

Every row therefore consists of a cycle of length at most |C|. The
common multiple lcm(1,...,|C|) is a period of every row simultaneously.
Transverse neighbors may branch arbitrarily; they cannot destroy this
uniform period because translating by that multiple preserves every
individual site's full state. Exact ring lifting carries the period to
all original placement labels. No predecessor uniqueness was assumed or
needed. If C is empty, emptiness is already proved and the periodicity
claim is vacuous; the period formula can simply be read for nonempty C.

## Corrected two-direction bound

Let f,g be the two forward partial functions on C, and fix an actual
field and its origin state q0. Every occurring state belongs to a cycle
of f and a cycle of g by the row argument. Although abstract transient
predecessors can branch, a cyclic state has a **unique cyclic predecessor**
under f: the forward cycle through it is fixed by the function, and any
predecessor that is itself cyclic lies on that same cycle. The same holds
for g. Thus backward moves of the actual field depend only on its full
current state, as do forward moves.

On the occurring orbit, f and g commute because their two compositions
reach the same lattice site. Their cyclic inverse maps are likewise
well-defined and commute on this orbit. Every site is reached from q0
by these basis moves. Consequently a return f^n0(q0)=q0 propagates to
all sites: apply the same deterministic word of forward or cyclic inverse
basis moves to both q0 and its returned copy. It yields a period
n0*Delta0 everywhere, where n0 is the origin's f-cycle length and is at
most |C|. The corresponding g return yields n1*Delta1.

These two independent vectors generate a placement-period subgroup of
index 3*n0*n1 in Z^2, because |det(Delta0,Delta1)|=3. The full period
lattice can contain additional periods, so its index is **at most** that
quantity, not necessarily equal. The repaired text states this correctly.
The resulting finite torus bound is a combinatorial SFT bound; periodic
development supplies the admitted polygon tiling under the reviewed global
encoding assumptions.

## Logical limits

A nonempty locally pruned core need not extend to the plane. Failure of
the deterministic tests is not evidence of aperiodicity. In the metric
library gate, the torus must use side pairs already in the equivalence
closure of the specific witnessed ring's seam pairs. An angle-only torus
with arbitrary extra equalities would not suffice; the text imposes the
correct containment.

For an actual tileable polygon pair, the defect-free-limit reduction gives
a legal full-plane SFT point. The theorem then constructs a periodic
admitted tiling of that pair. It does not claim that the original tiling
with partial contacts, nor every such original tiling, is periodic. Both
reflections are present throughout the ring alphabet. No extension to
other star compositions or to arbitrary higher-rank hexagon types is
licensed by this review.

## Added complete-wheel corollary: fresh review

The necessary-function part is valid: every actual field supplies a full
six-neighbor wheel, so entries common to all possible wheels restrict the
actual successor relation without removing an actual field. No extension
from raw edge/triangle consistency is assumed.

The constructive version now explicitly checks all six refined maps are
permutations, opposite maps are inverses, W0 and W1 commute, and
W2=W1*W0^(-1). These are the needed triangular-lattice identities; mere
commutation of six unrelated permutations would not suffice. The field
W0^n*W1^m(q) therefore has exactly the required displacement maps in all
six directions. Every selected map edge came from an allowed full wheel,
so the constructed field satisfies the original overlap relations. The
corrected construction criterion is VALID and covers the independently
checked twelve-residue action certificate.
# Fresh review of the full A-tuple quotient

The corollary projecting `(b;a0,...,a5)` to the complete ordered six-A
placement tuple is valid. All inter-ring relations compare shared A
placements only; hence they are complete between the retained fibres.
Choosing one full representative in each nonempty fibre preserves ring
membership, and thus every central angle and AB/AA seam, while preserving
every overlap relation. Theorem1 then gives a legal full placement field.
The choice can be made once per tuple, so every period of the projected
field lifts. This applies after actual metric restrictions by selecting
representatives from those restricted fibres. Functional quotient
propagation supplies a periodic full escape; it does not force the
original arbitrary B-choice field itself to be periodic. No gap found.
