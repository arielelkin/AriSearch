# Broad trivalent pair structural sprint: duplicate criterion, stopped

Date: 2026-10-19. Status: **rediscovery; blocked under protocol §5**. No claim of resolving the original problem. No enumeration or new computation was performed.

## Exact proposed condition

For arbitrary two strictly convex polygons whose native angles exceed 90 degrees, construct the finite reflection-aware relation of full-side neighbor placements allowed by equal side lengths and the two endpoint trivalent stars. Root a tile by its species and an indexed native frame. Identify choices that place exactly the same polygon support (intrinsic tile automorphisms do not create distinct choices). The proposed sufficient predicate was that every side of every occurring rooted tile has at most one allowed neighbor support.

Given an actual full-edge trivalent tiling satisfying this predicate, any frame-preserving map between two same-species tiles extends to the entire tiling: induction along finite dual paths fixes every tile. The dual graph is connected. Hence the tiling symmetry group has at most two tile orbits, including the case where one species is omitted. Bounded polygon sizes make this action cocompact. Local finiteness and finite polygon stabilizers make the group discrete. The elementary classification/argument for discrete cocompact plane isometry groups then provides translations. Reflections must be included in the neighbor relation; suppressing them invalidates the premise. Arbitrarily many finite propagation steps suffice, since each individual tile lies at finite dual distance from the root; no uniform propagation bound or limit argument is required.

## Existing result subsumes this proposal

The reviewed repository theorem [hexagon-five-unequal-adjacent-periodicity-2026-10-15.md](../lemmas/hexagon-five-unequal-adjacent-periodicity-2026-10-15.md), especially its paragraph beginning “A transition is certain,” already gives the stronger mechanism: finitely many indexed corona states, transitions unique only on a certain-edge subgraph, and connectivity of that actual subgraph imply finitely many symmetry orbits and periodicity. The proposed all-side unique-neighbor predicate is a strict special case. The existing artifact explicitly distinguishes this from the invalid assertion that finite local state count alone implies periodicity. Therefore this sprint adds no new structural theorem and does not warrant another proof or verification cycle.

## Exact gap and termination

No proof was found that arbitrary trivalent obtuse two-polygon tilings satisfy the proposed deterministic predicate, the stronger existing certain-transition connectivity predicate, or any newly weaker sufficient predicate. Tileability alone does not supply unique local neighbor choices; finite incidence balances supply neither unique continuation nor a global return map. Promoting those balances to a finite periodic quotient would simply insert the main unresolved global periodicity obligation.

The cycle is stopped under §5. No regular-P5 palette enumeration, seam atlas, torus growth, Euler ledger, or new candidate was launched. Root was informed of the duplicate before further polishing. Reopening requires a genuinely new, independently testable global invariant or a weaker continuation hypothesis together with a concrete application outside the reviewed class. No such hypothesis is claimed here.
