# Independent hostile review: fixed parent-corner branching maps

Date: 2026-10-19. Verdict: **PASS within the exact fixed-map scope** (protocol verdict: valid). This is an independent encoding/replay of a solver decision, not a solver-independent UNSAT certificate. The unrestricted two-convex-tile problem remains unresolved.

## Claim and assumptions

Reviewed the substitution report, generator and retained JSON, angle solver, preserved P diagnostic, and interrupted combined diagnostic. Read AGENTS.md, research-problem.md, research-protocol.md and the current discovery-log entry. The objects under review are precisely the P-parent 11P+2Q and Q-parent 9P+3Q disks with one split parent corner each and no flat incidences. No alternative map or enlarged inventory was searched.

## Independent reconstruction and attacks

The companion checker imports neither construction nor angle script. It reconstructs the sixteen oriented core/annulus triangles as an explicit list, appends the P ear, and compares them to retained faces. From raw faces it independently reconstructs dual edges, checks oriented cancellation, boundary edges, connected path/cycle vertex links and Euler characteristic. It obtains P (V,E,F)=(13,29,17), Q=(12,27,16), six interior degree-five P vertices each, and the advertised species inventories.

It checks every native word for distinct node entries and five/seven entries as appropriate. From each dual edge it reconstructs the two primal endpoints and verifies that the seam is consecutive in both incident native words with opposite traversal. The reconstructed seam table equals the retained table. Thus the positive object is a full oriented abstract primal incidence map. These checks do not establish a metric dissection.

The boundary-word subarcs recover untouched parent-corner counts P=(0,2,0,0,1,1,0), Q=(1,3,0,1,1,0). Their ordered singleton roles are u1,...,u4 and u1,...,u6 respectively, with the last boundary transition t6 or t5 assigned parent native corner 0. Each other transition is ordinary. Every singleton has one child incidence, every transition two, and every interior node three. Native ledgers consequently are 69=51+14+4 and 66=48+12+6. No seam endpoint or parent role mismatch was found.

The source angle encoding admits each phase and both reflection signs independently for every child. Since child native words are fixed cyclic words, these are exactly all ten or fourteen dihedral identifications, including repeated-angle cases. No normalizing constraint omits a branch. All twelve native variables have exact strict bounds 0<a<1 and the correct sums 3 or 5 in units pi. Junction equations target 2 internally, 1 at ordinary transitions, and the correct ordered parent native angle at singleton or exceptional roles. Reflections are permitted by the problem definition. No rational denominator restriction or angle-distinctness assumption is present. The angle system is only a necessary geometric condition, which is sufficient for rejection when UNSAT.

## Independent angle result

An independently written model uses one bounded integer phase and one Boolean reflection per child, with nested If expressions selecting the associated native real angle at each corner. It reuses only the audited JSON incidence, not the source solve function or its permutation-disjunction implementation. Its P-only system returned **UNSAT**, Z3 4.16.0, seed 0, 180000 ms timeout, elapsed 65.078914321 seconds. Input SHA256 agrees with the preserved diagnostic: 534241a47421d787898aecea6a3a3b4c983e9e24c702b45e5016b1c200cd8839. The result is retained in corner-branching-independent-sol-2026-10-19.json.

The complete P-only domain is 10^11 * 14^2 dihedral assignments with strict real native angles, each branch an exact linear system. This independently upholds the fixed-map exclusion subject to Z3 and the two audited encodings. The original tracked core is nonminimal, not a proof certificate. No short analytic obstruction or small core was obtained. In particular, this review does not identify all six interior children being P as the cause. Replacing an interior vertex by degree-seven Q changes the map and lies outside the reviewed exclusion; no repair is implied.

The combined retained run remains **UNKNOWN (interrupted)**. No UNSAT conclusion is attributed to that execution. P-only UNSAT logically excludes simultaneous realization of the pair.

## Defects, repairs and limits

No defect requiring a repair was found. No search artifact, discovery-log or Git change was made by this reviewer. The only added files are the independent checker, its results and this report under research/reviews/. The broader J=1 topology, other species assignments, other corner allocations, metric realization, plane extension and shape-only forcing remain unresolved. Stop this exact design; do not interpret its failure as an obstruction to every branching map.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/corner-branching-independent-sol-2026-10-19.py

The optional --orbit mode supplies a second implementation using explicitly rotated/reversed native-angle lists. This also returned UNSAT in 20.806820110 seconds, with the same solver, timeout, seed and input hash; its result is retained separately in corner-branching-independent-sol-2026-10-19.orbit.json.
