# A012021 on B5+1: an empty interface excludes all saturated mixed fields

Date: 2026-10-13. Status: [independent hostile review VALID](../reviews/terra-five-one-010212-012021-fresh-hostile-review.md); exact native checks PASS. The [full-interval scope review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md) extends this coverage mechanism to 108 < x < 126, x != 120. Restricted-family result, not the original research problem.

## Statement and exact question

Use 112.5<x<126, x!=120, y=720-5x,z=4x-360,r=360-2x,s=360-2y. Let actual strictly convex A,B have native words A012021 in colours x,y,z and B(s,r,r,r,r,r), at arbitrary positive actual closed polygon metrics. Every tileable pair under unrestricted contacts/isometries/omissions has a periodic A-only tiling.

The finite obligation before geometry search was the directed graph of adjacent A boundary placements: all twelve direct/reflected placements, four eligible top and four bottom placements, sixteen pairs each. An empty graph rules out a wider A strip; surviving recurrent transitions would require resource or exact metric constraints. Both graphs are empty. No further metric-partition or patch search is warranted for this native word.

## Necessary row interface

The independently reviewed capacity theorem extracts a saturated field or a pure-A periodic omission escape. Pure B is impossible in the exact four-star language AAAxyz,AABxxr,AAByys,ABBzrr. A012021 forces the middle BB mask {1,4}; the independently reviewed opposite-B-side theorem then gives complete parallel B rows separated by one or more whole A rows, even if AAA is used.

Assume a boundary A row has B above and A below. Its two upper B neighbours meet at global A vertex1, an ABB star, so that corner is z. Outer vertices0,2 are AAB; inward vertices3,4,5 are AAA. The shared horizontal seam of adjacent boundary A cells is left side5/right side2; its outer A colours are left corner0/right corner2, and its inner colours left corner5/right corner3.

For native word (0,1,2,0,2,1), the four placements putting z at global corner1 are

    (1,+),(3,+),(3,-),(5,-).

Their two full colour profiles, each with two states, are

    X=(1,2,0,2,1,0), Y=(0,2,1,0,1,2).

For either incident copy the shared-side endpoint map is exactly

    outer0 -> inner2, outer1 -> inner0.

The exact AAB language demands equal outer A colours. Both inner colours are then equal as well, either z/z or x/x, contradicting the only AAA star xyz. All angles are distinct in the stated interval except the expressly excluded x=120. No metric assumption enters. With B below, eligible states are (0,+),(0,-),(2,-),(4,+); outer corners5/3 and inner corners0/2 obey the same map. This is a full reflected/native placement check, not just the two profile representatives.

Thus no boundary A row can have A on its other side. Propagating from any B row gives exactly alternating A/B rows, with no AAA vertex anywhere. But A012021 has two private AA native sides5 and0 meeting at colour0 corner0: both pairs are 01, whereas an AB side in the middle mask requires 02 or12. Both are AA and force an AAA vertex. This is the already independently reviewed no-AAA private-corner exclusion. The saturated mixed field is therefore impossible.

Consequently an original tileable pair must give the pure-A alternative. The actual pure field develops to an A-only plane tiling, and the imported unrestricted convex-hexagon theorem supplies a periodic monohedral tiling. B may be omitted under the original acceptance criteria. If A independently fails every monohedral family, the pair is untileable. No claim that every original pair tiling is periodic is made.

## Certificate and honest scope

[Producer](../searches/five-one-012021-boundary-interface.py), [certificate](../certificates/five-one-012021-boundary-interface.json). Native sides are derived from endpoint sets. All twelve placements and all32 pairs across both orientations are retained;16 outer-AAB compatible pairs, zero inner-AAA compatible pairs. Side-length equality can only delete candidates, so every metric coarsening is covered without minimal-pattern extrapolation. No solver, timeout, numerical geometry or infinite-existence inference is used.

Nondestructive replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/five-one-012021-boundary-interface.py --check research/certificates/five-one-012021-boundary-interface.json

Result: PASS. Fresh independent hostile review must check shared endpoints, both boundary orientations, global propagation and the original-tiling pure alternative. The author replay alone is computational evidence.

Only the settled capacity, parallel-row, no-AAA local obstruction, actual development and monohedral escape dependencies are used. The binary periodic-fibre theorem is not needed: mixed fields are impossible. Other native words remain separate assigned branches; the original research problem remains unresolved. More A012021 metrics or longer chains would not change this angle-only exclusion.
