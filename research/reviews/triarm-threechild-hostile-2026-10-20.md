# Hostile audit of the radial three-child boundary gate (2026-10-20)

**Status: the initial corner rejection was false; the author's corrected native-side inventory and placement argument addresses that gap.** This review gives an exact counterexample to the initial implication, then independently checks the support patterns that kill the first three vertical metrics. It does **not** supply a `sqrt(3)P=2P+H` dissection or establish plane tilability.

## Scope and finite arithmetic

The proposed inventory is `tH=3P`, `tP=2P+H`, with `t=sqrt(3)`, P side word `(1,a,b,a,1)`, and H side word `(b/t,2a/t)` repeated three times. Each parent side may meet at most one full side of each convex child, so the script's 30 scalar words per parent side are a valid overinclusive necessary list. Requiring one word each for the three parent side lengths gives three linear equations in `(a,b)` over `Q(t)`. The script rejects common rank-one equations by normalized coefficient-row intersection; any consistent triple then has a rank-two pair. Enumerating all pairs of row classes is therefore complete at the scalar level. Circle feasibility includes equality, so the `x=0` tangent branches are retained. Strict convexity is checked in the real algebraic field, not from the displayed decimals. The replay reports 57 circle-feasible scalar pairs and nine strictly convex metrics, six with `x=0` and three with `x≠0`.

The missing check is at the parent corner. At `x=0`, the exact P angle word is `(120,90,120,120,90)` degrees. Its 120-degree corners are **vertices 0, 2, and 3**. Vertex 0 has incident sides `(1,1)`, while vertices 2 and 3 each have incident sides `(a,b)`. Every one of the six `x=0` metrics satisfies `a+b=t` and has the scalar unit-parent-side word `(0,1,1,'none')`. A copy of P can therefore occupy the parent's 120-degree vertex with an `a` side along one unit-parent edge and a `b` side along the other. The script's assertion that a 120-degree P child requires a native unit side applies only to vertex 0. Its eight printed `KILLED` lines cannot be accepted as a dissection obstruction.

For example, take `a=t/3`, `b=2t/3`, and `v=(0,t/3)`. Then

    P=((0,0),(1,0),(1,t/3),(0,2t/3),(-1/2,t/2)).

Direct vector products give strict convexity and angle word `(120,90,120,120,90)`. At P vertex 2, the two incident side lengths are `a,b`. They fit the two parent unit sides because `a+b=t`. The other scalar parent-side equations also hold: `ta=1` and `tb=2`. Thus this is a complete exact counterexample to the *corner-aware scalar rejection*, although no child packing has been claimed. The same corner issue affects the other five vertical metrics. For the three nonvertical metrics, the replay's exact cosine tests show only P vertex 0 has angle 120, H has none, all corners exceed 60, and their unit boundary words omit native P unit sides; that restricted corner rejection remains plausible.

## Audit of the corrected placement obstructions

The three earliest vertical cases can be closed directly from their exact scalar rows, without relying on the author's larger native-side assignment count.

* At `(a,b)=(t/3,2t/3)`, every exact parent-edge row has `h='none'`. Hence H has no side on the parent boundary. H cannot touch a parent side only at an H vertex: that 120-degree corner leaves at most 60 degrees, while every P corner is at least 90 degrees; a P side continuing through the point would occupy the whole parent half-plane. H cannot touch a parent corner without its incident sides lying on the parent boundary. Thus H lies strictly inside the parent. Choose an interior point of H. Each disjoint convex P child is seen from that point in an angular interval of width strictly below 180 degrees. Both P children together cover less than a full turn, but every ray from the point through the interior H must continue through a child before it exits the parent. Contradiction. This metric already has periodic P-only Type 3 and regular H-only tilings, but the geometric obstruction is independent of those omissions.
* At `(a,b)=((3-t)/2,(3t-3)/2)`, each of the two parent `a` edges uniquely requires a native P `b` side. The two P children have only two such sides between them. The remaining unit-parent-edge rows requiring a P `b` side are unavailable, so both unit edges require a native P unit side and a **long** H side of length `2a/t`. Traversing the parent boundary counterclockwise, those unit edges have directions 0 and 300 degrees, 60 degrees apart modulo a full turn. The three long H edges have directions 120 degrees apart. The same H cannot support both edges. Reflection changes the labeling but not this spacing.
* At `(a,b)=(t/2,t/2)`, the unit-parent-edge rows contain no H side, while each of the three middle parent edges requires a native P unit side and a **short** H side of length `b/t=1/2`. The middle parent-edge directions are 90, 150, and 210 degrees. H is equiangular, and its three short edges have directions 120 degrees apart. Thus one H cannot support all three middle edges.

The other three vertical metrics admit simpler global side-budget contradictions using the exact rows printed by the replay:

* At `(a,b)=(4t-6,6-3t)`, each parent `a` edge uniquely requires **two** native P `b` sides. There are two such parent edges but only two P `b` sides total, so four required sides cannot be supplied.
* At `(a,b)=((3t-3)/2,(3-t)/2)`, each parent `a` edge requires one native P `b` side and an H long side, exhausting both P `b` sides. Each unit-parent edge requires `a+b`, including another P `b` side, so the allocation is impossible.
* At `(a,b)=(2t/3,t/3)`, each parent `a` edge requires two native P unit sides and the parent `b` edge requires one more. Five are required, while two P children have only four unit sides in total.

For the three nonvertical metrics, the exact angle check gives P vertex 0 as the sole 120-degree P corner and no 120-degree H corner; all angles exceed 60 degrees, so exactly one child corner must occupy the parent's 120-degree vertex. That P corner has incident native unit sides. The unit-parent rows at each nonvertical metric contain no native P unit side: respectively `2b`, `2b`, and `2b+b/t`. This rejects each case even where `a=1`, because the native `a` and native unit sides remain distinct in the inventory.

I also inspected the corrected script's native-side allocator. It chooses at most one complete native side per child and per parent support line, and it tracks each side by `(child,index)` across all five parent edges. This preserves native identities when numerical lengths coincide (`a=b` or `a=1`), excludes using a side twice, and deliberately overincludes many impossible spatial orders and orientations. Its corner filter likewise checks all P and H 120-degree vertices and both orders of their incident sides. The exact replay runs to completion with 57 scalar metrics, nine convex metrics, and the stated final zero-survivor result. The direct contradictions above independently cover the nine cases and make the **restricted** conclusion replay-safe: no strictly convex radial metric admits this specified `tP=2P+H` parent dissection. No conclusion about other inventories or unrestricted tilings follows.

## Monohedral omission checks for the six vertical metrics

The independent [Sage replay](../searches/triarm-threechild-vertical-omission-2026-10-20.sage) transcribes the fifteen Rao families already source-audited in this repository, checks all ten dihedral angle/side relabelings exactly over `Q(sqrt(3))`, and compares full homogeneous side equations. Every metric has the same eight angle-only Rao labels (Types 2, 3, 4, 13 with two labels each). Exactly one metric passes a complete family:

| `a` | `b` | P-only exact Rao | H-only |
|---|---|---|---|
| `t/3` | `2t/3` | Type 3, `(sign,off)=(+1,4),(-1,1)` | regular H; periodic honeycomb |
| `(3-t)/2` | `(3t-3)/2` | none | no monohedral tiling |
| `t/2` | `t/2` | none | no monohedral tiling |
| `4t-6` | `6-3t` | none | no monohedral tiling |
| `(3t-3)/2` | `(3-t)/2` | none | no monohedral tiling |
| `2t/3` | `t/3` | none | no monohedral tiling |

The Rao Type 3 construction is periodic, as is a regular-hexagon honeycomb, so the first pair is falsified for unrestricted aperiodicity. The other H shapes have all angles 120 degrees and alternating side lengths `b/t,2a/t` with `b≠2a`. An H-only tiling would be edge-to-edge: a T junction leaves a 60-degree gap at a 120-degree native corner, and four corners cannot meet. At every trivalent vertex, matching edge lengths would have to alternate short and long around a three-cycle, impossible. This excludes H-only tilings even with initially unrestricted contacts. The P-only exclusions rely on the imported completeness of Rao's fifteen-family classification.

These omission results do not decide mixed tilings. The corrected placement obstructions concern only the proposed second-parent `tP=2P+H` dissection and do not imply that the pair is plane-nontilable or aperiodic. No such global claim follows from this gate.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/triarm-threechild-vertical-omission-2026-10-20.sage
