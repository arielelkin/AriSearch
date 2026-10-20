# Hostile review: binary hexagon and bipartite partner

Date: 2026-10-19. Verdict: **VALID** for the stated equiangular 120-degree hexagons and unrestricted plane-tiling definition. No counterexample found; the proof below establishes the claims over arbitrary positive real side lengths. This is an independent mathematical review, not a literature or novelty review, and does not resolve the unrestricted two-convex-polygon problem.

Reviewed artifact: [binary partner obstruction](../searches/hexagon-binary-partner-bipartite-charge-sol-2026-10-19.md). Definitions read in [research-problem.md](../../research-problem.md). Structural reference read: [hexagon limits and conditional periodicity](../lemmas/hexagon-limit-and-periodicity.md), together with [the repaired reduction rereview](two-hexagon-global-repaired-reduction-rereview.md). The present angle hypothesis gives a direct full-edge proof and requires neither defect-free extraction nor the honeycomb theorem.

## Independent geometric and graph checks

At an interior point of a native side, its tile occupies a half-disk. A second tile corner there would require the remaining half-disk to be partitioned into native 120-degree sectors, which is impossible. A second tile side would consume the entire half-disk and leave no corner sector. Local finiteness follows from positive minimum tile area and bounded diameter. Thus native corners cannot lie strictly inside other sides. Any positive side overlap with unequal endpoints would give precisely such an incidence; all positive contacts are consequently full sides. Exactly three 120-degree native corners occur at each vertex.

Let the three outgoing full-side lengths be x,y,z. The incident corner pairs are (x,y), (y,z), (z,x), even when some labels coincide. They form a closed walk of length three in the numerical corner graph union. A bipartite graph has no such odd closed walk; numerical loops are forbidden as well. This checks arbitrary numerical identifications rather than formal side symbols.

A-only vertices would require an odd walk in the single edge a--b, so A alone cannot tile. B alone cannot tile under the bipartite hypothesis by the same argument. Hence neither omission allowed by the research definition evades assertion 1. If one public length is missing from B, an A corner cannot be completed. If both occur and adding a--b preserves bipartiteness, no vertex exists. Otherwise a and b occupy the same part of a B component. This exhausts the partition cases: components can be independently flipped if a and b occupy different components. In fact the graph of a single cyclic side word is always connected, since that word itself traverses all its numerical vertices; the artifact's disconnected discussion is harmless additional generality.

AAA and BBB stars are excluded. An AAB star would require a B corner (a,a) or (b,b), hence a forbidden loop. Every vertex is ABB. Its ray labels must be a,b,x, and its B corners must be (a,x) and (b,x). Here x is outside {a,b}, since otherwise a loop occurs. Every native corner of every actually occurring B tile therefore has exactly one incident side in {a,b}. This forces the cyclic alternation (p,x,q,y,r,z) with p,q,r public and x,y,z private. Overlapping A/B palettes have thus been explicitly considered; disjointness of public and private values is a conclusion of an assumed tiling.

## Independent closure and final contradiction

Choose successive side directions u0,u1,u2,-u0,-u1,-u2, with u1=u0+u2 and u0,u2 independent. Closure is equivalent to

    (l0-l3)+(l1-l4)=0,
    (l2-l5)+(l1-l4)=0.

Therefore l0-l3=l2-l5=l4-l1=delta. Substitution of (p,x,q,y,r,z) gives x=r-delta, y=p-delta, z=q-delta. This uses exact real equations and no rationality, genericity, or arithmetic assumption.

If all three public positions have one value, the other public value is absent from B, so no ABB star exists. Otherwise the binary public word has a majority value. Rename it a and cyclically rotate the three public positions to obtain p=q=a,r=b. Then x=b-delta differs from y=z=a-delta. The unique private x side is flanked by a on both ends. Its native (a,x) corners require (b,x) partners, absent from B. A cannot supply either corner involving private x. This is an immediate local contradiction, proving assertion 1 without infinite counting.

The optional charge proof is also sound: all B corners have one public side, each a side contributes two positive corners, each b side two negative corners, and their three public sides give nonzero total charge. ABB stars cancel charge. Boundary terms are O(R) for fixed positive areas and bounded diameters. Counting ABB corners gives N_B=2N_A+O(R), forcing quadratic B population by coverage and contradicting the charge identity. Its scope is no stronger than the closure proof.

## Corollary, reflections, and scope

A centrally symmetric equiangular hexagon has equal opposite lengths. Conversely equal opposite lengths give a halfturn symmetry by the displayed direction sequence. Thus noncentral means delta is nonzero. Equality at opposite positions is then impossible. If adjacent equalities are also forbidden, a repeated numerical value can occur only at cyclic distance two or four. Every even-position value is consequently different from every odd-position value. The even and odd palettes bipartition the numerical corner graph, proving assertion 2 for arbitrary real equalities, including repeated same-parity values. The intended no-equal-adjacent corollary is valid.

Reflection reverses the cyclic word and the direction order, possibly changing the sign convention for delta, but preserves closure, centrality, numerical graph bipartiteness, native adjacent pairs, and the final absence of (b,x). Arbitrary rigid placements therefore create no exception.

For a central B, the usual translation tiling by a centrally symmetric convex hexagon is a monohedral periodic escape allowed by the problem definitions. Assertion 3 is consequently a necessary condition for a potentially aperiodic pair. No assertion excludes noncentral B with adjacent equal lengths, and no classification or new aperiodic construction follows. The explicit example (1,5/2,1,3/2,2,3/2) has all three opposite differences -1/2 and positive lengths, as claimed.

No computational enumeration was necessary. The review independently checked all partition, parity, reflection, and omission cases symbolically; its verdict does not depend on a bounded solver domain.
