# Hostile audit: fixed deep-P-wheel J=1 map

Date: 2026-10-19. Verdict: **PASS within the exact fixed-map scope** (protocol verdict: valid). The unrestricted problem remains unresolved.

## Claim and reconstruction

Read AGENTS.md, research-problem.md, research-protocol.md, the deep-P-wheel report, both source scripts and retained incidence JSON, and the preceding corner-branching map and independent review. Scope is exactly the displayed W6 one-advance annulus, nested P ears, Q ear, species and ordered parent roles. No alternate disk or corner allocation was searched.

The checker imports neither source generator nor angle solver. It reconstructs all oriented faces from an explicit list, including center z, five rim vertices, five outer vertices, the common ear and P's additional nested ear. It checks cancellation on every shared oriented edge, a single boundary cycle, connected cycle/path vertex links, and Euler characteristic one. These establish the specified abstract oriented disks. It checks exact boundary order and exact Q species locations, not merely inventories.

P has (V,E,F)=(13,29,17), inventory 11P+2Q; Q has (12,27,16), inventory 9P+3Q. The six interior vertices are degree-five P in each disk. Every boundary child occupies one connected arc. The independently recovered untouched-corner lists are P=(0,2,1,1,0,0,0), Q=(1,2,1,0,2,0). Native words have exactly five or seven distinct corner nodes; ledgers are 69=51+14+4 and 66=48+12+6. The sole split parent corner is respectively t6 or t5, assigned parent index zero; ordered singleton roles are u1,...,u4 or u1,...,u6. Every other transition is ordinary. There are no flat child incidences.

For each dual edge the checker reconstructs both primal seam endpoints, requires consecutive endpoints in both native words with opposite traversal, and matches the entire retained seam table. Boundary words consist of the incoming transition, the ordered singletons, the outgoing transition, and the interior seam chain. Thus the outer cycle has exactly the expected five or seven parent corner roles in cyclic order, with intervening ordinary straight transitions. This is convex-boundary compatibility at the combinatorial level only: it makes no claim of angles, lengths, straight sides, or a metric convex embedding. The disk has no omitted boundary component or extra corner role.

## Necessary angle encoding and hostile attacks

The independent encoding shares only the audited incidence data with the source angle solver. It uses bounded integer phases and Boolean reflection choices, with nested If lookup of native real angles; the source instead uses disjunctions of constant permutations with explicit corner variables. For each P child all ten dihedral identifications occur, and for each Q all fourteen occur, independently. No phase normalization, distinctness assumption, or rational denominator bound is used. Repeated native angles therefore cannot invalidate coverage.

All twelve real native angles satisfy strict bounds 0<a<1, P sum three and Q sum five, in units pi. Every trivalent interior junction sums to two, every ordinary transition to one, each singleton to the actual ordered parent native angle, and the two angles at the unique split corner to parent angle zero. These are necessary for any geometric realization of this fixed map. The independent P-only subsystem covers 10^11*14^2 assignments, with exact rational linear equations on every branch. P-only infeasibility suffices to exclude the simultaneous pair; it does not justify any claim about other maps.

## Result, defects and trust boundary

The independent P-only system returned **UNSAT**, Z3 4.16.0, seed zero, timeout 180000 ms, elapsed 36.86149561499769 seconds. Input SHA256 is `412bdd5ae5ae25714fa3c927d0fe6d63f75f93a4d06b172d26af59b28c491b93`, agreeing with the retained source result. The review JSON retains this decision and topology counts. Thus the fixed-pair angle exclusion is independently reproduced, with Z3 and the two encodings in the trust boundary. This is an independently encoded solver decision, not a solver-independent UNSAT certificate.

No incidence defect was found and no repair was proposed. This audit adds only review artifacts. Neither Git nor discovery-log was edited. No metric solve or enlarged enumeration was performed. The original tracked core is not a solver-independent proof certificate. Other annuli, corner assignments, species, split positions, J=1 maps, metric polygon pairs, plane existence, and shape-only aperiodicity remain outside this exclusion.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/deep-p-wheel-hostile-sol-2026-10-19.py
