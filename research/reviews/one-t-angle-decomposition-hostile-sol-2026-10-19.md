# One-T angle decomposition hostile review (Sol)

Date: 2026-10-19. Independently reviewed the adjacent angle-decomposition Python, Markdown, JSON and SMT-LIB against the preserved one-T source and prior primal hostile review. No solver check was run, no timeout was extended, and no Git or discovery-log file was edited.

## Verdict

**PASS for exact algebraic reformulation of the declared fixed-map necessary-angle problem and honest UNKNOWN reporting.** No angle feasibility, infeasibility, geometric realization, or aperiodicity result is certified. Two verifier/replay qualifications below should accompany reuse of these artifacts.

## Domain and equivalence attack

Regenerated the original source maps from the preserved corner-branching input using the original one-T conversion. Full structural equality holds for all eight P and six Q variants. The prior topology review therefore applies to these identical maps; this review does not independently repeat its manifold checks. Each P parent has 11 P and 2 Q children; each Q parent has 9 P and 3 Q children. Independent map choices cover exactly 48 pairs and the raw dihedral domain is correctly 48*10^20*14^5.

Each native incidence belongs to exactly one node. Eliminating the last incidence at a node substitutes its required total minus its other incidences. Those pivots are disjoint, so simultaneous substitution is reversible. At the T there are exactly two native incidences and the omitted host sector contributes 1, giving total 1 for the two genuine angles. Private parent corners have one native incidence, hence the substituted value is exactly the fixed indexed parent angle. Other transitions have total 1 and ordinary interior nodes total 2, matching the original equations.

Exactly-one Boolean choices enumerate phase 0 through n-1 and eps in {1,-1} for each child. Their implications force every surviving or substituted slot to its shared angle coordinate. Inactive map clauses impose nothing. Moving from selectors shared across variants to selectors private to each variant does not restrict the selected map. Both parents use the same twelve angle coordinates; their parent word orders stay fixed. Coincident angles merely produce duplicate branches. Strict 0<a<1 bounds remain on all shared coordinates, and all selected slot values equal those coordinates, so eliminating explicit slot bounds loses no condition.

For a fixed branch, the integer incidence rows are exactly the original node equations after those identifications. Supplementary-coordinate elimination is ordinary affine pivot substitution with a positive integer coefficient 1 or 2. Keeping the omitted coordinate's strict affine bounds makes projection and extension inverse, including repeated coordinates. Joining original twelve-column rows implements intersection without allowing independent reindexing. RREF is only equation reduction and supplies no strict-feasibility decision.

Checked exact rational row-substitution identities on 392 deterministic branch assignments across every saved map, varying phases and alternating reflections. This is a finite implementation check; the general equivalence follows from the incidence and pivot argument, not from exhaustive enumeration of the enormous branch domain.

Both pruning lemmas are sound with their stated hypotheses. Two disjoint pairs of four distinct P coordinates summing to 1 each force the remaining P coordinate to 1, contradicting the strict upper bound. An ordinary triple containing a supplementary pair as a multiset forces its remaining coordinate to 1, also with multiplicities. Neither argument applies without its specified node/pair conditions, and neither decides the remaining union. The solver does not claim to have applied these lemmas to exhaust branches.

## Serialization and outcome

The source-input SHA256 independently matches `33d0b6da814916e886daa93daee3b095519749120e42b0eaabfe6e84e550a47b`. The retained SMT2 file hash independently matches `b7bbe5da6d852d703b8f420fa1d3cae62296ef18b8af909fdc6a4e6d78ab4aa4`. Removing exactly the appended newline/check-sat suffix reproduces precheck hash `410501398f4478e0a77f066c0950afd618b5aa1dec9e4579cc52db5ae0a82265`.

Reconstructed the complete formula from the current script while intercepting all artifact writes and replacing Solver.check with an immediate exception. Its captured precheck SMT2 text is byte-for-byte identical to the retained file. Thus the prior post-check hash caveat is resolved for this artifact without repeating a solve.

JSON reports UNKNOWN/timeout, seed 0, timeout 180000 ms, elapsed 180.01853186800145 seconds. The 48-entry ledger is exactly the Cartesian map-pair product, without duplicates, and every entry is unresolved. The slight elapsed overhead does not imply a timeout escalation. The script contains one aggregate check and no retry path. The historical permission/scheduling narrative cannot be independently established from these artifacts alone; it is explicitly disclosed as an aggregate-check deviation from the later per-branch schedule. No individual pair exclusion follows from timeout.

## Corrections and practical limits

1. The prospective SAT `--check` verifier verifies rational bounds and incidence equations but does not validate that assignment phases are in range and eps is exactly +1 or -1, or that chosen-map indices are nonnegative and in range. Python negative indexing and unrestricted modular expressions can accept inputs outside the declared certificate schema. Before relying on this as a standalone SAT certificate checker, require exactly the P/Q keys and native child keys, integer map indices in range, integer phases in range, eps in {1,-1}, and angle lists of the required lengths. Generated solver witnesses do have valid domains by construction. This latent checker issue does not alter the current UNKNOWN result, which contains no witness.
2. The SMT2 assertion dump includes check-sat but omits solver timeout/seed options. It reproduces the formula, not the bounded solver configuration. Use the documented Python replay for the 180000 ms cap, or explicitly set equivalent options when invoking the raw SMT2. The recorded configuration and assertion hashes are separate evidence. Replaying the Python script also overwrites its output artifacts; this review intercepted writes and did not do that.

No mathematical correction to the projection lemma, map coverage, strict inequalities, phase/reflection handling, or pruning lemmas is required. All simultaneous strict angle feasibility remains open for all 48 map pairs.
