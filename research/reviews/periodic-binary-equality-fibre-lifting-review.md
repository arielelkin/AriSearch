# Fresh review of periodic binary equality fibre lifting

Date: 2026-10-12. Reviewer: independent sub-agent `/root/ammann_audit`.
Author of the reviewed general lemma: root agent. Scope: the complete proof in
[periodic-binary-equality-fibre-lifting.md](../lemmas/periodic-binary-equality-fibre-lifting.md).
Verdict: **VALID** under its stated periodic finite-quotient assumptions.

I checked the proof algebraically, independently of a polygon producer or a
finite torus search. The following are the material gates.

1. An equality relation of two maps from a two-element set can only have the
   eight structural table types listed in the lemma (with choices of row,
   column, or singleton). A missing fourth corner after three equalities is
   impossible by transitivity in the value set. A row/column fixes one variable;
   a singleton fixes both. Thus the reduction loses no constraints, including
   repeated side values, and is substantially more restrictive than an arbitrary
   binary SFT.
2. For each finite signed-graph quotient component, root-based closed walks
   form a group. The gain/sign map to Z^2 x Z/2 is a homomorphism. The spanning
   tree and each non-tree edge generate all root-based walks, so their finitely
   many gain/sign pairs generate its exact image Gamma. Although the walk group
   can be nonabelian, the image is abelian; no commutativity of walks is assumed.
   Reversing a signed edge negates its translation and retains its XOR sign.
3. Every element of Gamma is represented by an actual closed quotient walk.
   An element (0,1) would lift to a sign-odd closed walk in the infinite graph,
   contradicting feasibility. The kernel of projection to translation is
   therefore trivial, and Gamma is the graph of a homomorphism chi on its
   projected subgroup L. This does not assert that every quotient component has
   a connected infinite lift.
4. The three cover formulas are correct. In rank one use the genuine subgroup
   generator (a,b), rather than its primitive direction; Bezout proves that
   membership in (2gcd(a,b))Z^2 forces an even multiple of that generator. In
   rank two the index d obeys dZ^2 subset L, so 2dZ^2 subset 2L. Rank zero has
   no nonzero translation gains. Common multiples preserve these properties
   over all finitely many quotient components.
5. A finite-cover closed walk may start away from the chosen root. Conjugating
   by a tree path puts it at the root without changing gain or XOR sign.
   Consequently every such walk has gain in K intersect L and sign zero.
   This justifies propagation on every finite-cover component, including
   self-edges and parallel edges.
6. Pin compatibility uses the assumed infinite solution, not a choice of free
   signs on infinite components. A path between two finite-cover pins lifts to
   a path whose endpoints have the same prescribed pin values as their native
   vertex types. Periodic pins give those values at every translate, so all
   pairs of pins in each finite component obey the path parity. The finite
   assignment then lifts to a genuinely K-periodic assignment.

The warning that twice the original lattice need not suffice is necessary:
one vertex type with the constraint b(x+2,y)=1-b(x,y) is feasible with period
four in x, but not period two. Here L=2Z x {0}, chi(2,0)=1, and the rank-one
formula selects N=4 exactly. An odd zero-gain cycle instead excludes every
solution; a sign-odd nonzero gain is not by itself an obstruction.

No claim about Euclidean polygon realization is part of this review. The
polygon application still needs an independently established periodic angle
backbone, exactly two native choices per tile, and the separate legal-label
development theorem. Fibres of size six in the alternating-colour family do
not satisfy this lemma merely because their colour projection is periodic.
