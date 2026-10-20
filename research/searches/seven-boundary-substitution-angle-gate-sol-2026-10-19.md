# Exact angle gate for the reviewed two-parent substitution incidence

Date: 2026-10-19. Status: **UNSAT over the complete stated finite phase/reflection domain; independently hostile-reviewed valid within this scope.**

## Claim and finite scope

The exact native corner words in `six-boundary-substitution-2026-10-19.json` cannot satisfy the simultaneous strictly convex angle equations. This excludes metric realization of this retained incidence pair by common pentagon P and heptagon Q. It excludes no other incidence, species allocation, parent-corner allocation, or substitution inventory. It does not resolve the two-convex-polygon problem.

Normalize angles by pi. P has five real angles in (0,1) summing to 3; Q has seven in (0,1) summing to 5. Independently for each child v with word length n, choose phase s in {0,...,n-1} and epsilon in {+1,-1}; corner k has native angle a[(s+epsilon*k) mod n]. These are exactly all cyclic shifts and reflections, including assignments with repeated angle values. There are 20 P children and 5 Q children across the two disks, hence 10^20 * 14^5 = 53,782,400,000,000,000,000,000,000 discrete assignments. The continuous angles are unrestricted real numbers within the stated strict bounds. Each branch is a rational linear feasibility problem, so SAT would have a rational witness. There is no coordinate grid or floating-point decision.

At every f node require its three incident angles to sum to 2. At every t require its two angles to sum to 1. At u_j require its sole child angle to equal native angle j of the correct parent species. All parent indices remain fixed exactly as in the source JSON. The program validates word lengths, species labels, node multiplicities, f-face incidence, t-boundary adjacency, and complete parent-corner roles before solving. Node counts are P:16 f,8 t,5 u; Q:15 f,7 t,7 u.

## Derivation and encoding

Before enumeration, the exterior deficit transformation b=1-a gives sum(b_P)=sum(b_Q)=2, f-triple deficit sum 1, t-pair deficit sum 1, and unchanged u equalities. The complete scalar ledgers hold, so they provide no immediate contradiction. The finite dihedral equations are the necessary next gate. No symmetry reduction was imposed: in particular, fixing a selected child's phase without also respecting the fixed parent roles would not be justified. The solver handles the exact native equations directly rather than attempting geometry.

Each child is encoded by one finite disjunction of 2n constant permutations of its native real-angle variables. A selector integer labels each disjunct; all arithmetic after selecting a disjunct is linear. This encoding contains every allowed phase and reflection. Native bounds are strict, excluding zero and flat angles. Equalities allow repeated native angles. Shared P and Q variables enforce the same angle words in every child and in the parents.

## Result, reproduction, and trust boundary

Z3 4.16.0, random_seed=0, timeout 600000 ms: the complete simultaneous system returned **unsat**, initially in 43.2578 seconds. The adjacent JSON retains the input SHA-256, formula SHA-256, scope, software version, limit, and completed status. The script reconstructs the formula from the retained source; it does not trust a stored status. Its optional SAT verifier uses Python Fraction and independently checks every native bound, sum, phase/reflection, f/t/u equation, and assignment completeness.

Replay the complete gate:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/seven-boundary-substitution-angle-gate-sol-2026-10-19.py

A narrower sufficient obstruction was also found: **the P disk alone is UNSAT**, with the same common P/Q native angle sums and bounds. Initial untracked replay completed in 9.6294 seconds; tracked replay in 17.1186 seconds. The tracked core, retained inside the JSON, contains essentially the full P equations and is not claimed minimal or a short analytic proof. Replay this scope with:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/seven-boundary-substitution-angle-gate-sol-2026-10-19.py --parent P --core --timeout-ms 60000

The CLI writes its current run to the adjacent JSON; copy that file first if preserving the combined record. A Q-only diagnostic returned **unknown (timeout)** at 60000 ms and establishes no Q-only conclusion. A denominator-12 CP-SAT witness reconnaissance returned infeasible on its restricted grid; it is discarded and is not evidence for the unrestricted real-angle UNSAT claim.

This is a reproducible exact solver result, not a retained independently checked formal proof trace. Its trust boundary includes the source encoding and Z3's exact SMT decision. The independent hostile review reconstructed the mathematical constraints using nested If expressions and reflection-major selectors, obtaining UNSAT in 107.5874 seconds; its direct replay also returned UNSAT in 51.4709 seconds. Its verdict is VALID within the exact retained incidence scope. The stronger P-only localization is a production diagnostic, not independently reviewed. Solver timeout is never interpreted as UNSAT.

## Consequence and stop

Any straight convex realization with these exact words and common native shapes would satisfy this necessary angle system. Its UNSAT therefore kills this fixed abstract incidence pair before lengths or coordinates. Seam lengths, coordinate realization, parent similarity, nonoverlap, plane extension, recognition, and aperiodicity were not established. No metric search was performed. Stop this fixed seed under protocol section 5; the unrestricted problem remains unresolved. No git or discovery-log edits.

Dependencies: the source incidence certificate, its independent incidence hostile review, research-problem.md, and research-protocol.md sections 5,11,19. Independent review: `research/reviews/seven-boundary-substitution-angle-gate-hostile-sol-2026-10-19.md`.
