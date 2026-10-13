# A010212 on B5+1: empty boundary interface gives all-metric periodic escape

Date: 2026-10-13. Status: [independent hostile review VALID](../reviews/terra-five-one-010212-012021-fresh-hostile-review.md); exact native checks PASS. The [full-interval scope review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md) extends this coverage mechanism to 108 < x < 126, x != 120. Restricted-family result, not the original research problem.

## Statement and finite question

Let 112.5<x<126, x!=120, and y=720-5x, z=4x-360, r=360-2x, s=360-2y. Actual strictly convex hexagons A,B have native angle words A010212 in colours x,y,z, and B(s,r,r,r,r,r). Every side metric is allowed, provided it defines the actual positive closed convex polygon. If the pair tiles with unrestricted isometries, partial contacts and omissions, it has a periodic monohedral A escape. No such pair is aperiodic.

Before metric or closure enumeration, the finite question was whether any boundary A row can border a B row on one side and an A row on the other. Domain: all twelve native direct/reflected A placements, four eligible placements for each of two boundary orientations, sixteen adjacent pairs per orientation. Outcomes: an empty graph excludes wide A strips at every actual metric; recurrent edges would require a further AAB-resource or actual length/closure attack. The graph is empty, so no 203-partition geometry search or longer B-chain search is justified.

## Settled reductions used

The reviewed [capacity theorem](terra-five-one-b-saturated-chain-reduction.md) takes any original tiling to an actual defect-free field and a saturated limit. If B disappears, the pure-A field and imported unrestricted convex-hexagon classification give the periodic omission escape. Pure B is impossible in the exact four-star language

    AAA xyz, AAB xxr, AAB yys, ABB zrr.

Otherwise every B has exactly two B neighbours. For A010212 the reviewed endpoint palette forces native BB mask {1,4}. The reviewed [parallel-row theorem](five-one-middle-mask-b-rows-and-bounded-a-strips.md) gives complete parallel B rows separated by one or more whole A rows, without assuming AAA unused. These dependencies are already independently reviewed and are not re-audited here.

## New angle-only boundary contradiction

Choose a boundary A row with B immediately above and A immediately below. In the reviewed global neighbour indexing, neighbour slots 1,2 are B and slots 0,3,4,5 are A. Vertex slot k meets neighbour slots k,k+1. Thus global A corner 1 is ABB and must be z; corners 0,2 are AAB; corners 3,4,5 are AAA.

For a native placement (rho,epsilon), global corner k has native index rho+epsilon*k mod6. The native word is (0,1,0,2,1,2). Exactly these four placements put z at global slot 1:

    (0,-),(2,+),(4,+),(4,-).

Their complete colour profiles are precisely

    X=(0,2,1,2,0,1), Y=(1,2,0,1,0,2),

each repeated twice. The horizontal seam joins left global side 5 to right global side 2. Its B-facing endpoint has A colours (left slot0,right slot2); its inward endpoint has (left slot5,right slot3). In either profile, both copies obey the SAME endpoint map

    outer0 -> inner1, outer1 -> inner2.

At the outer endpoint AAB requires equal A colours, either x/x or y/y. Applying that same map to both copies gives equal inner A colours, either y/y or z/z. At the inward endpoint all three tiles are A, and the only legal AAA star is the rainbow xyz. Two equal colours cannot occur. Therefore no adjacent boundary pair is legal.

The opposite boundary orientation is obtained by reflection. Direct enumeration with z at global slot4 gives the same endpoint map: outer corners (left5,right3), inner corners (left0,right2). All local native reflections are independently included. No side equality, metric inequality or actual closure formula is used; matching lengths can only remove pairs from this already empty angle-compatible set.

## Global consequence and every original tiling

Every A row adjacent to any B row must therefore have B on its other side. Propagating from one B row forces exactly alternating B/A rows throughout the full integer lattice; isolated B rows, one-sided B sets and wider gaps are all excluded directly.

An alternating row field has no AAA vertex. But native A010212 has two private AA sides 0 and 1 incident at its native corner1 (colour y). Both endpoint pairs avoid z, while every AB side in the middle-mask field has endpoint pair 02 or12. Thus both sides are AA. This gives two A neighbours at that corner and forces a USED AAA star. This contradicts the alternating species field; equivalently it is exactly the independently reviewed A010212 no-AAA private-corner obstruction in [seven-word coverage](five-one-middle-mask-no-aaa-coverage.md).

Hence the saturated mixed alternative is impossible. Every original tileable pair must take the pure-A saturation alternative and has a periodic A-only tiling. The conclusion permits omission of B, as required by the original problem; it does not claim all admitted pair tilings are periodic. All equality coarsenings are covered directly by the angle-only proof, not extrapolated from low-rank success. If A is independently nonmonohedral, the same argument proves the pair untileable.

## Exact certificate, replay and remaining work

[Finite producer](../searches/five-one-010212-boundary-interface.py), [certificate](../certificates/five-one-010212-boundary-interface.json). The producer derives side indices from native endpoint sets and retains all twelve placements plus every pair in both orientations. Counts: 32 boundary pairs, 16 outer-AAB legal, zero compatible inner-AAA. There is no solver, approximate geometry, random seed, timeout, patch bound or infinite-existence inference.

Nondestructive replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/five-one-010212-boundary-interface.py --check research/certificates/five-one-010212-boundary-interface.json

Result: PASS. Fresh hostile review must reconstruct the shared-seam endpoint mapping, actual whole-row consequence and pure-A alternative; the author's replay is computational evidence, not independent review.

This settles one additional native word on this fixed B5+1 family. It does not classify other B multiplicities or angle strata. Other native words remain assigned to independent structural attacks; this result is not a reason to search more A010212 metrics. The original research problem remains unresolved.
