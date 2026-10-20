# One parent-corner branching design cycle

Date: 2026-10-19. Status: **exact oriented incidence pair constructed; this fixed pair fails its necessary angle gate (P-only UNSAT), pending independent review**. The unrestricted problem and other J=1 maps remain unresolved. This is not a polygon dissection or plane tiling.

## Scope and analytic construction

One cycle at precisely P-parent 11P+2Q and Q-parent 9P+3Q; J=1,D=H=0. No larger inventory or extra exceptional corner was tried. Both disks use six interior P children. Start with the triangulated inner hexagon whose oriented faces are the reversals of (012),(023),(035),(345). Its inner vertex degrees are (4,2,3,4,2,3). Add an annulus with six outer vertices a0,...,a5 and outer advances (0,2,1,0,2,1) at consecutive inner vertices. Each inner degree becomes five. The outer degrees are (5,3,4,5,3,4).

For Q retain this disk, labeling a0,a1,a3 as Q and all others P. For P attach the oriented ear (a0,a1,e0), labeling only a0,a3 as Q. The resulting counts are:

|Parent|children|dual edges|dual triangles = I|boundary children|interior children|ordinary transitions B|split corners J|
|---|---:|---:|---:|---:|---:|---:|---:|
|P|13|29|17|7|6|6|1|
|Q|12|27|16|6|6|5|1|

The P boundary is (a0,e0,a1,a2,a3,a4,a5). Untouched parent-corner counts along these arcs are (0,2,0,0,1,1,0). The Q boundary is (a0,a1,a2,a3,a4,a5), with counts (1,3,0,1,1,0). In each disk the last boundary transition (a5,a0) is the unique exceptional corner, native parent corner 0. Traverse the remaining boundary assigning untouched corners u1,... in order. These are actual corner roles rather than a degree-only ledger. Every child native count is degree+1+untouched corners at boundary, degree inside, giving exactly five or seven according to species. Native ledgers are 69=3*17+2*7+4 and 66=3*16+2*6+6.

The generator checks oriented cancellation on shared dual edges, exact boundary edges, disk Euler characteristic, connected cycle/path vertex links, species inventory, native word sizes, and primal seam endpoints. Every dual triangle becomes a trivalent primal seam junction f; each dual edge becomes one seam; each boundary dual edge receives its transition endpoint t. Reversed oriented links give child corner words. Each seam is consecutive in its two child words and traversed in opposite directions. The adjacent JSON retains every oriented triangle, native word, species, corner role and seam endpoint. Thus the output is a full abstract primal map, not merely scalar budgets or a proposed graph.

## Complete necessary strict angle system

Angles are real numbers in units pi: P has five entries in (0,1), sum3; Q has seven entries in (0,1), sum5. For each child independently, every phase 0,...,n-1 and sign +/-1 is represented, mapping its native word position k to native index (phase+sign*k) modulo n. There is no phase normalization, angle distinctness assumption, rational denominator restriction, or reflection omission.

Every interior f junction has angle sum2. Every ordinary t transition has sum1. At the exceptional last t transition, the two child angles sum to parent native angle0. At u_j the sole child angle equals native parent angle j. Parent labels follow the actual ordered outer cycle. Both disks use the same twelve native angle variables; parent inflation does not change angles.

The simultaneous finite discrete domain has 20 P children and five Q children, hence 10^20*14^5 assignments before repeated-angle coincidences; each assignment leaves a rational strict linear feasibility system. The P-only necessary subsystem has 11 P and two Q children, hence 10^11*14^2 assignments. The solver encodes these assignments by finite disjunctions of constant permutations and exact linear real arithmetic.

## Result and limits

The P-only tracked system returned **UNSAT in 25.921399129 seconds**, Z3 4.16.0, seed0, timeout60000ms. The P diagnostic JSON records its complete nonminimal tracked core, input SHA256 and formula SHA256. This necessary subsystem already excludes simultaneous strict angles and hence geometric realization of this exact incidence pair. It does not exclude other corner allocations, exceptional seam placements, species assignments, dual disks, or any unrestricted polygon family. No short independent structural contradiction was obtained: the current obstruction is the retained exact finite solver decision, with Z3 and encoding in its trust boundary. Independent hostile review is pending.

The combined solver was interrupted after 104.114086095 seconds once the sufficient P-only result was available. Its status is UNKNOWN (interrupted), retained separately in the angle JSON, and supplies no additional result. No metric solve was attempted. There is no rational angle witness because this particular map fails the necessary system. The positive construction accomplished in this cycle is the complete topological/native incidence pair only.

## Replay and retained evidence

All files are under research/searches:

- corner-branching-substitution-sol-2026-10-19.py and .json: analytic disk construction, validation and full primal maps.
- corner-branching-angle-sol-2026-10-19.py: all-dihedral exact necessary equations; optional Fraction verifier for SAT witnesses.
- corner-branching-P-diagnostic-sol-2026-10-19.json: completed P-only UNSAT and tracked core.
- corner-branching-angle-sol-2026-10-19.json: interrupted combined run.

Replay the incidence generator, then the sufficient P gate (the latter overwrites only the angle script adjacent result, not the preserved P diagnostic):

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/corner-branching-substitution-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/corner-branching-angle-sol-2026-10-19.py --parent P --core --timeout-ms 60000

Stop this design cycle under the assessment direction2 stop rule. This specific map is rejected pending review; the broader J=1 parent-corner construction mechanism is blocked at the unsolved obligation of finding a different complete pair with simultaneous strict angles. No inventory increase, second corner, Git edit, or discovery-log edit was performed. A new allocation requires a materially new incidence/angle mechanism rather than coordinate work on these rejected words.
