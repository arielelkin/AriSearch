# Two convex hexagons with unique one-B corner stars cannot be aperiodic

**Status: independently reviewed VALID within the stated exact angle-star domain.**
See the [whole-theorem review](../reviews/two-hexagon-unique-b-star-impossibility-review.md).
Date2026-10-12. This is a complete restricted-family impossibility theorem.
It does not settle the unrestricted two-hexagon case or pairs with pentagons.

## Statement in polygon geometry

Let A,B be convex hexagons, with six intrinsic corners each. Let alpha_i
and beta_j be their native counterclockwise angles, i,j in0..5. Allow
translations, rotations, reflections, unrestricted partial contacts and
omission of either species, as in [the problem](../../research-problem.md).
Suppose the following exact angle conditions hold:

1. Every three-corner multiset with sum2pi contains exactly two A corners
   and one B corner.
2. For each B corner j, there is exactly one unordered A-corner pair
   {u_j,v_j}, with repetition allowed, whose sum with beta_j is2pi.

**Theorem.** The pair is either untileable or admits a plane tiling with a
nonzero translational symmetry. It is not aperiodic. No restrictions on
side equalities, rationality of angles or geometric parameters are imposed.

The theorem covers all native cyclic orders of both shapes and every metric
coincidence pattern. Equal B angles and repeated A pair labels are allowed
when they satisfy the stated exact-star conditions. Additional angle stars
outside these conditions define other cases and are not excluded here.

## Dependencies and precise computation boundary

The reviewed [global SFT encoding](two-hexagon-global-sft-encoding.md) says
that tileability of actual convex hexagons gives an edge-to-edge trivalent
limit and a legal full honeycomb placement labeling. A periodic labeling
develops into an admitted polygon tiling with nonzero translation, possibly
after squaring a glide reflection. This uses no added matching rules for
the final polygons: the local rules are exactly their angle and side data.

The [one-B ring theorem](two-hexagon-one-b-ring-spatial-reduction.md) reduces
these labels to full B-centered ring states on an index-three triangular
lattice. Finite spatial deletions prove emptiness; a functional relation in
one direction forces a genuine common period of every bi-infinite field.

The [pair-graph classification](two-hexagon-unique-b-pair-graph-classification.md)
reduces the six unique stars, necessarily, to degree-two pseudographs on
six native A corners. Its exact closure and counting proof is recalled below.
The retained census consists of11850 rooted native orders, with duplicate
A-dihedral classes kept harmlessly. It includes every side equivalence by
functional propagation or exact forced-side periodic witness coverage.

This finite classification uses no computational UNSAT verdict as a theorem
premise: spatial deletions and periodic labels are verified directly. Solver
SAT searches produced some torus labels, whose integer incidence checks are
independent. No bounded failure to find a torus enters the final proof.

## Proof: complete necessary pair-graph domain

Set T={(u_j,v_j,6+j):j=0..5}. If the pair tiles, the reviewed limit gives a
nonempty X(T,e), where e is its actual equivalence of twelve native sides.

Every honeycomb vertex contains one B tile. The ring theorem forces B cells
onto one of the three index-three lattice cosets. Alternatively an invariant
translate-average has species probabilities b=1/3,a=2/3. Each native B corner
occurs once per B tile and in one unique star, so that star has frequency1/3.
Each native A corner occurs once per A tile. Its pair-graph degree must be2:
its star-incidence ledger is deg(i)/3=2/3. Loops count twice. Nonregular graphs
therefore give empty SFTs for every metric.

For a regular graph, write x_i=alpha_i-2pi/3 and y_j=beta_j-2pi/3. The six
star equations give y_j=-x_(u_j)-x_(v_j); the A sum gives sum x_i=0, and the
B sum follows because each A degree is2. The additional rank is5. A further
three-corner equation can only be one of the original AAB equations or a
BBB equation selecting three nonloop graph edges covering each A corner once.
The latter selections are perfect matchings. The complete algebraic proof
by B multiplicity is in the pair-graph lemma and includes repeated corners.

An actual exact T is rationally closed. Thus the graph must contain an odd
component cycle, or its perfect matching would add a forbidden BBB star.
Degree-two pseudographs decompose into loops, parallel-edge2cycles and longer
simple cycles. The eight possible odd-containing component partitions are
5+1,4+1+1,3+3,3+2+1,3+1+1+1,2+2+1+1,2+1+1+1+1,1+1+1+1+1+1.
There are268 such graphs on the native A labels. For each, enumerate all
six-edge multiset native B words modulo B rotations and reflections. This
gives11850 rooted orders. Fixing the A native order0..5 loses no actual
assignment because every graph on those labels is included. Repeated pair
entries yield identical T at fixed B positions and are not omitted metric
cases; arbitrary e is still included. No A-dihedral reduction is necessary.

## Proof: spatial and metric classification of the complete domain

For every rooted order, retain every B placement and every full A-neighbor
ring satisfying all six exact angle stars. Adjacent B centers must agree on
their shared A placements. Remove states lacking a neighbor, or lacking a
compatible elementary neighbor triangle; repeat the recorded finite deletions.
No actual infinite field loses a state under these necessary constraints.
The independent checker reconstructs the entire domain and every full ring
from native corner constraints, including loops and parallel edges, and
verifies every deletion and surviving degree. The separate pair-graph lemma
proves the alternative at-most64 endpoint-assignment bound.

The exhaustive results are:

| Component partition | Rooted orders | Empty cores | Functional cores | Branching cores |
|---|---:|---:|---:|---:|
| 5+1 |4320|4272|48|0|
| 4+1+1 |2700|2676|6|18|
| 3+3 |600|581|15|4|
| 3+2+1 |1800|1794|6|0|
| 3+1+1+1 |1200|1198|2|0|
| 2+2+1+1 |720|708|0|12|
| 2+1+1+1+1 |450|450|0|0|
| 1+1+1+1+1+1 |60|60|0|0|
| **Total** |**11850**|**11739**|**77**|**34**|

Empty cores give empty X(T,e) for every e. In the77 functional cores at least
one full-state neighbor relation has outdegree at most1. The one-direction
ring theorem proves an actual periodic labeling whenever X(T,e) is nonempty.
Length constraints only delete states and cannot undo that periodicity.

For the34 branching cores, a ring q forces twelve actual matched side pairs:
six B/A seams and six surrounding A/A seams. Let E(q) be their equivalence
closure. Any actual e admitting q contains E(q). The finite certificate
covers every surviving ring by a torus whose angle triples lie in T and whose
matched side pairs are contained in E(q). Hence that same torus is legal for
e. The34 cases use49 distinct local forced metric closures. All49 have exact
periodic witnesses, with original lattice indices3,6 or12. In particular the
twelve initially unresolved cases have explicit index12 witnesses; their
absence at indices<=8 is not used as a global negative conclusion.

The unique-wheel/commuting-action record supplies an independent structural
explanation of those twelve cases. Their pairwise relations have degree2,
but each state has exactly one complete six-neighbor wheel. The resulting
maps commute and have four-state orbits, constructing index12 torus fields.
The full family proof only needs the checked periodic witness coverage; this
stronger local mechanism has a separate proof and replay.

Thus every possible exact T,e in the stated family has either an empty SFT or
a periodic point. The reviewed unrestricted global reduction proves the
polygon theorem. QED.

## Artifacts and replay

- [Full exact ring/pruning census](../certificates/two-hexagon-odd-pair-graph-orders.json).
- [New branching forced metric records](../certificates/two-hexagon-odd-pair-graph-ring-metrics.json).
- [Twelve positive residue tori](../certificates/two-hexagon-odd-pair-residue-tori.json).
- [Two-triangle branching source tori](../certificates/two-hexagon-balanced-root-ring-metrics.json).
- [Search record](../searches/two-hexagon-odd-pair-graph-orders.md).
- [Independent complete checker](../reviews/check_two_hexagon_odd_pair_graph_orders.py).

The checker verifies the explicit dihedral B-corner maps, endpoint-derived
side maps (including reflection's minus-one offset), and full placement
transformations when reusing the earlier two-triangle torus data. It does
not confuse two different B-word representative conventions.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_two_hexagon_odd_pair_graph_orders.py --metrics research/certificates/two-hexagon-odd-pair-graph-ring-metrics.json --residue research/certificates/two-hexagon-odd-pair-residue-tori.json

Scope remaining outside this theorem: multiple A-pair options for a native
B corner, any additional AAA/ABB/BBB stars, every general pentagon family,
and the unrestricted two-hexagon impossibility question. Neither the finite
ring counts nor a selected source substitution resolves those cases.
