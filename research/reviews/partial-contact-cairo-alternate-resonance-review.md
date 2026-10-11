# Fresh hostile review: alternate Cairo resonance reduction

Reviewer: root agent, independently of the structural-audit author.
Verdict: **VALID** for the exact family and four-ratio necessary conclusion.
No tileability, periodicity or unrestricted target resolution is established
at the four surviving ratios.

The reviewed artifact is
[the reduction](../lemmas/partial-contact-cairo-alternate-resonance-reduction.md).
The finite-to-infinite step uses a bounded rational charge on actual
augmented native tiles. Complete interior stars have nonnegative charge,
every native tile has charge at most minus one, and incomplete stars lie
on O(R) selected boundary tiles. A bounded-diameter/minimum-area argument
gives the boundary estimate, whereas coverage needs Omega(R squared)
tiles. This does not assume existence of asymptotic frequencies or positive
density of both species.

The complete contact ledger permits every individual resonant fifth side
to remain whole or host its possible T, in both bank orders when distinct.
It also permits independent cuts of long arms a,b at their unique allowed
short-arm endpoint coordinates. The reviewed two-T invariant supplies the
finite exhaustive cut locations, and at most one T per native side.
The proof excludes omitted species via the same charges/private-arm
argument, and permits reflections by treating corner edges as unoriented.
A whole matched augmented piece has the same number of120 endpoints on
both sides because120 cannot meet90 or180. Cyclic ray matching is necessary;
it is not promoted to patch extension. Coincident numeric lengths remain
separate when their endpoint roles differ.

[The independent checker](verify_cairo_alternate_endpoint_marginals_independent.py)
imports neither producer nor solver. It reconstructs the six ratio roots,
all12 strictly convex polygons and native cuts from numeric lengths; it
builds circular stars by direct backtracking rather than the author's
Eulerian graph criterion. It agrees on all variants, corner kinds, tile
vectors and stars, and checks every rational primal/dual inequality:

| Ratio | Variants | Corner kinds | Stars | Certificate |
|---|---:|---:|---:|---|
| f2c |12|23|59|infeasible dual|
| fac |16|24|63|feasible primal|
| f2a |12|23|57|feasible primal|
| e2c |12|23|59|feasible primal|
| eac |16|25|67|feasible primal|
| e2a |12|24|61|infeasible dual|

Replay in arisearch returns PASS. The earlier forced-host experiments
exclude legitimate whole-side occurrences and are explicitly superseded.
In particular no unconditional f2a exclusion survives this audit.
The four feasible systems are only necessary marginals. The absence of
restricted four-face quotients is not an impossibility proof.
