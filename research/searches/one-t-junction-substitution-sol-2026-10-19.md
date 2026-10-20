# One genuine interior T-junction: one complete-map design cycle

2026-10-19. Status: **complete abstract oriented primal maps; shared-angle gate UNKNOWN (timeout)**. This is restricted construction research and does not resolve the two-polygon problem.

## Fixed domain and genuinely changed primal maps

Read the governing problem and protocol, the 20:52 assessment, the earlier native-only seven-boundary angle gate, J=1 construction, and reviewed six-interior ten-edge lemma. Retain exactly the latter construction's two oriented triangulated contact disks, species and ear placement. The saved source is `corner-branching-substitution-sol-2026-10-19.json`. No alternative ear, extra T, inventory increase, interior Q, or repeated contact is introduced.

This reuses the abstract dual but constructs different primal/native maps. The old exceptional boundary transition t_last becomes an ordinary parent-side seam endpoint. Its former parent corner is moved to a position inside one boundary child's arc. At an interior junction f incident to that host, replace the host's native corner by a flat incidence. Both adjacent vertices in the expanded host word must themselves be interior f nodes. Thus the host's subdivided native side is wholly internal, and f lies strictly inside that side if positive seam lengths can eventually be realized. All seam edges are retained, without a collapsed edge. Suppressing f only in the native host word gives the proper five/seven sides. The other two children at f retain genuine native corners.

The single finite analytic design domain contains eight P-parent variants and six Q-parent variants, hence 48 candidate pairs. These are every allowed host/flat placement on these fixed disks under the interior-endpoint condition and the stated placement of the additional boundary corner (first position inside the host arc). This is not an exhaustive enumeration of all maps in the assessment's inventory. Parent corner indices are reassigned consecutively along the actual oriented boundary, so every parent corner is unsplit and no obsolete J=1 corner identity survives.

Every generated variant retains full oriented dual triangles, species, expanded child incidence words, native words, boundary cycle, parent corner roles, host side endpoints, and exact seam endpoints. Each seam is checked consecutive in both expanded words with opposite traversal directions; distinct seams have distinct child pairs. Native side counts are five or seven. Every interior child is P. The source's disk embedding and vertex links are inherited because neither triangulated dual nor expanded cyclic incidence order is changed (only a boundary corner is inserted).

## Budgets and equations

P parent: F=13, I=17, B=7, E=29, seven distinct single-arc boundary children, six interior P, inventory 11P+2Q. Q parent: F=12, I=16, B=6, E=27, six distinct single-arc boundary children, six interior P, inventory 9P+3Q. Native corner ledger is respectively 69=3*17-1+2*7+5 and 66=3*16-1+2*6+7. There is exactly one flat host incidence H=1, and J=D=0.

Angles use units pi. Shared P entries lie in (0,1) and sum3; shared Q entries lie in (0,1) and sum5. Independently for each child, allow every native cyclic phase and both reflections: 10 choices for P and 14 for Q. No angle denominator restriction or child phase normalization is imposed. Each ordinary interior node has sum2; at the T the explicit host flat angle1 plus the opposite pair has sum2, making that pair supplementary. Every ordinary boundary transition has sum1. Every unsplit parent corner has its native parent angle. These are necessary conditions only, before coordinates or lengths.

A parent map selector chooses one of its explicitly retained variants. Each branch is exact rational linear arithmetic with finite dihedral disjunctions. The combined discrete domain has 48*10^20*14^5 assignments before coincidences. Conditional constraints impose the full equations of the selected variant. Z3 seed0 and a fixed timeout decide only this domain. Timeout means UNKNOWN, never UNSAT. A SAT witness receives a separate Fraction check of all native assignments and node equations.

## Result and stopping condition

The complete combined gate returned **UNKNOWN: timeout**, after 180.02262870000413 seconds, Z3 4.16.0, random_seed0, timeout180000ms. Input SHA256 is 534241a47421d787898aecea6a3a3b4c983e9e24c702b45e5016b1c200cd8839; formula SHA256 is ee76429594888bac39cd18ee0751efe50c2f5ec3811db1bb6c97d6659e6f1186. All 14 complete maps are retained in the JSON. No simultaneous exact rational witness and no UNSAT certificate was obtained. This is a computational limit, not a mathematical obstruction to these maps or to the broader H=1 family.

Stop this single design cycle at the assessment's explicit angle-witness gate. The exact remaining obligation is to decide the preserved finite disjunctive rational-linear system, or supply a simultaneous strict native angle witness for an explicitly stated map pair. The metric and recognition obligations remain subsequent independent gates. No extra map family or timeout escalation was attempted.

No exact additive host-side or edge-vector/similarity gate is justified before simultaneous angles survive. The required metric equations would include positive seam lengths and l_host=l_left+l_right at each T, consistent common native P/Q lengths and angles, parent inflation sqrt(7+sqrt(34)), every child phase/reflection, positive convex coordinates, and disjoint child interiors covering each parent. None is inferred from this topological certificate. There is no claim of plane tiling, hierarchy recognition or aperiodicity.

## Replay and trust boundary

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/one-t-junction-substitution-sol-2026-10-19.py --timeout-ms 180000

The adjacent JSON retains all generated maps, source and formula SHA256, software version, finite domain counts, timeout and completed solver status. The exact solver is within the trust boundary; no independent UNSAT proof trace is asserted. The [independent Sol hostile review](../reviews/one-t-junction-primal-hostile-sol-2026-10-19.md) passed the complete primal maps and faithful UNKNOWN reporting. It found that the saved post-check `solver.sexpr()` hash is not directly reproducible from the pre-check formula; this is a reproducibility limit of that hash, not evidence of a different mathematical formula. No Git or discovery-log edits were made by the delegated implementer.
