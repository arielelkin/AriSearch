# One-B stars: exact ring reduction and deterministic-strip periodicity

**Status: adversarially reviewed.** [First hostile review](../reviews/two-hexagon-one-b-ring-spatial-reduction-review.md) and [independent repaired-statement review](../reviews/two-hexagon-one-b-ring-spatial-independent-review.md). Date2026-10-12.
This generalizes the balanced-root spatial obstruction. It applies whenever
all admitted corner triples contain exactly two A corners and one B corner.
It does not assume unique corner stars or a predetermined side-equality pattern.

## Hypotheses and notation

Use the reviewed [global hexagon SFT encoding](two-hexagon-global-sft-encoding.md).
Native A corners are0..5 and B corners6..11. Let T be any set of corner
multisets all of composition2A+1B. Let e be any equivalence relation on the
12 native sides. The placement symbols of either species are (r,s), where
r in Z/6 and s in {+1,-1}; both reflections are included.

Write D_k=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)) cyclically and
Delta_k=D_k+D_(k+1). Let

    L = span_Z{Delta_0=(1,1), Delta_1=(-1,2)}
      = {(x,y):x-y=0 mod3}.

A ring state is q=(b;a_0,...,a_5), with one B placement b and the A
placements at the six cells D_0,...,D_5. Let Q(T,e) consist of exactly
those rings satisfying all six central vertex stars and all native side
matches on the six B/A seams and six A/A seams of that seven-cell patch.
In particular the star at central slot k has native corners

    B(b,k), A(a_k,k+2), A(a_(k+1),k+4).

For a placement (r,s), native corner at slot j is r+s*j modulo6;
native side at side-slot j is r+j for s=+1 and r-j-1 for s=-1.
The B/A seam in direction D_k compares B side-slot k-1 with A side-slot
k+2. The A/A seam between D_k and D_(k+1) compares their side-slots k+1
and k+4. Apply e to those native side labels.

For q,q' in Q define q R_k q' precisely when

    a_k = a'_(k+4), a_(k+1) = a'_(k+3),           (1)

with indices modulo6. These are equality of full placement symbols,
not equality of just species, angles or physical orientation classes.

## Theorem1: species phase and exact ring encoding

Every legal full-plane configuration of X(T,e) has its B cells on exactly
one coset c+L, and its A cells on the other two cosets. For a fixed coset,
restriction to the B-centered rings is a bijection with fields

    q_z in Q(T,e), z in c+L,
    q_z R_k q_(z+Delta_k) for every z,k.          (2)

The bijection preserves every translation belonging to L.

### Proof of the species phase

Let b_z in {0,1} indicate species B. Every elementary triangle of the
cell lattice is one honeycomb vertex and has exactly one B cell. The
two triangles sharing the edge from z+D_k to z+D_(k+1) have opposite
third cells z and z+Delta_k. Subtracting their species equations yields
b_z=b_(z+Delta_k). Therefore b is invariant under L. The quotient Z^2/L
has three cosets; an elementary triangle has one site from each coset.
Its indicator sum1 means exactly one coset is B. This proves the phase
claim and includes every possible translation of that phase.

### Proof of the ring encoding

A B cell has six A neighbours. Its seven-cell patch supplies a state in
Q. Two B centers separated by Delta_k share exactly the A cells D_k and
D_(k+1) relative to the first center. Relative to the second, these are
D_(k+4) and D_(k+3), since subtraction of Delta_k gives those coordinates.
Their full placement labels consequently satisfy(1).

Conversely assign a B placement at each B center and A placements from
its state. Every A cell neighbours exactly three B centers. Those three
centers form an elementary triangle of the L-lattice, and every two share
that A cell. Relations(1) make the three assignments identical. Thus all
placements are well-defined. Every honeycomb vertex contains exactly one
B and is one of that B's six central stars, so its angle constraint is
satisfied. Every seam is B/A or A/A. B/A seams are checked in their B ring;
an A/A seam is checked in the rings of the B cells at its two endpoints.
Thus every side constraint is satisfied as well. The two constructions
are inverses, and all definitions commute with translations in L. QED.

## Theorem2: finite spatial exclusions and monotonicity

Repeatedly remove any ring state lacking an R_k neighbour in the current
state set for some k. Optionally also remove states that have no compatible
completion around a specified elementary triangle of the L-lattice; such
a completion must satisfy all three pair relations of that triangle.
Every full-plane field(2) uses only states surviving every such removal.

Thus a finite deletion record ending with the empty set proves X(T,e)
empty. Its scope is infinite configurations, not merely a chosen torus.
All deletions are independently checkable by finite label membership.

Moreover an exclusion computed with all native sides declared equal also
excludes every actual side equivalence: Q(T,e) is a subset of that angle-only
ring set and the overlap relations are restrictions of the same relations.
Neither successful local pruning nor a nonempty core establishes extension.

### Proof

Induct on the deletion steps. An actual state has all actual neighbours,
which survive by the induction hypothesis. Its actual elementary triangles
provide all required compatible completions. It cannot be removed. Side
constraints only remove states, and never introduce a new relation pair. QED.

## Theorem3: one deterministic direction gives a genuine period

Let C be any finite surviving state set containing every state of every
full-plane field, with the true relations restricted to C. Suppose that
for some direction k every q in C has at most one R_k successor in C.
Then every full-plane field(2) is periodic under

    P*Delta_k, P=lcm(1,2,...,|C|).               (3)

No uniqueness in transverse directions or of predecessors is required.
Consequently, for actual convex hexagons with this exact triple type,
the pair is untileable or has an admitted nonzero translational symmetry.
It cannot be aperiodic under the unrestricted problem definition.

### Proof of strip periodicity

On a full bi-infinite row z+n*Delta_k, q_n follows the partial function f
specified by R_k. Fix q_0. In its infinite past some state repeats, by
finiteness of C. Deterministic forward propagation makes that repetition
a directed cycle, and a directed cycle cannot exit under a function.
Thus q_0, and indeed every occurring row state, lies on a cycle of length
at most |C|. P is a multiple of every such cycle length. For every row and
every n, q_(n+P)=q_n. The same P works for all rows regardless of transverse
branching, proving(3). Theorem1 transfers the period to full placement labels.

If an actual polygon pair tiles, the reviewed defect-free-limit theorem gives
a legal X configuration even when the original tiling has partial contacts
or T-junctions. The periodic X configuration develops into a polygon tiling
with a nonzero translation (possibly after squaring a glide reflection),
by the reviewed global encoding. This proves existence of a periodic escape,
not periodicity of every original admitted tiling. QED.

A conditional converse is not asserted: failure of this deterministic test
does not establish aperiodicity or rule out other periodic constructions.

## Corollary: quotient away the central B choice when overlaps ignore it

Project a full ring q=(b;a_0,...,a_5) to its entire ordered A-neighbor tuple
p=(a_0,...,a_5). For every fixed surviving state set C, the overlap relation
q R_k q' depends only on p,p'. Thus its induced quotient relation S_k is
complete between the two fibres whenever those tuples satisfy the shared
A equalities in(1). Every quotient field lifts to a full ring field by
choosing ANY available representative q(p) in C once for each tuple p.
The resulting field retains every angle and native seam constraint, since
those were checked in membership of C; R_k is independent of the omitted
B placements. This lift commutes with translations and preserves periods.

If a quotient direction is functional, theorem3 applied to the quotient
states yields a period of every quotient field. Canonical representatives
then give a periodic FULL placement field. This proves that every actual
metric field has a periodic escape, even when its original central B
choices vary nonperiodically. It does not claim those original full fields
are all periodic. For a subset imposed by actual side equalities, restrict
to its nonempty fibres and choose representatives there; restriction cannot
introduce new quotient successors. The same method applies to the two-basis
bound and complete-wheel refinements on the quotient relations.

This is an exact overlap-signature quotient, not a projection to species
or angles: all SIX neighboring A native placements remain. Forgetting any
of those requires a separate proof that relations are independent of the
forgotten data. No uniqueness of the central B placement is assumed.

## Corollary: complete wheels can force propagation despite pairwise branching

A possible complete neighbor wheel at q consists of six states q_0,...,q_5
with q R_k q_k and q_k R_(k+2) q_(k+1) for all k cyclically. Every actual
field provides such a wheel: the displacement from Delta_k to Delta_(k+1)
is Delta_(k+2). Consequently if all possible wheels at each retained q
have the same kth entry for one fixed direction k, that direction is a
necessary partial function on actual fields. Theorem3 applies to this
refined relation, even if the original R_k had several successors.

In particular a unique complete wheel at every state forces all six actual
successors. The two-basis finite-index bound below then applies. If one also
checks that the maps W_k are permutations satisfying
W_(k+3)=W_k^(-1), W_0 W_1=W_1 W_0 and W_2=W_1 W_0^(-1)
on the entire refined finite state set, the resulting finite group action
constructs an actual periodic ring field. Indeed assign at
z=n*Delta_0+m*Delta_1 the state W_0^n W_1^m(q); these identities
verify all six neighbor directions, including Delta_2=Delta_1-Delta_0.
This proves existence rather than only periodicity conditional on existence.
No assertion that edge or triangle consistency alone guarantees extension
is used. This corollary is a direct application of theorem3 to a necessary
restriction containing every globally occurring neighbor pair.

## Corollary: finite index bound when both basis directions are deterministic

If R_0 and R_1 are both functions on C, any actual field has periods
n_0*Delta_0 and n_1*Delta_1 with1<=n_0,n_1<=|C|. At the chosen center,
forward/backward finite functional rows are cycles. A return to the same
central state propagates to all sites by deterministic moves in the two
basis directions; opposite moves are uniquely determined on occurring
cycles. Equivalently the two translations commute on the occurring orbit.
The subgroup generated by those two periods has index3*n_0*n_1.
The full placement period lattice can be larger and has index at most
3*n_0*n_1<=3*|C|^2.

This gives a proved finite torus bound for this deterministic class,
rather than a bound inferred from repeated solver failures. The broader
one-direction theorem needs no claim of such a small two-dimensional bound.

## Metric witnesses for the branching residue

An angle-only torus is not by itself a periodic escape for arbitrary metrics.
For an angle-ring q, let E(q) be its twelve actual matched native side pairs.
If a retained torus uses only T triples and side pairs in the equivalence
closure of E(q), then any e admitting q also admits that torus.
A finite library covering every surviving q proves that every nonempty
X(T,e) has a periodic point, even if the ring relations branch.

This is the precise metric gate used after local exclusions/deterministic
propagation. Each torus must be independently checked from its labeling;
absence of a bounded torus is not an impossibility result.

## Scope and dependencies

This reduction includes arbitrary2A+1B triple sets, repeated corner labels,
all rotations/reflections and every side-equivalence relation. A unique
native B corner star is not enough to imply a unique full ring. Periodicity
of the species cosets alone is also insufficient; theorem3 uses full states.

Types with pure A or B stars or1A+2B stars are outside these hypotheses.
The broader target still includes those hexagon types and all pentagon pairs.
Dependencies: [global encoding](two-hexagon-global-sft-encoding.md), its
reviewed unrestricted defect-free limit and periodic-development corollary.
No geometric-realizability assumption is supplied for arbitrary abstract T,e.
