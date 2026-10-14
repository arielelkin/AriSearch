# Independent hostile review: two-parent wheel/seam incidence

Date: 2026-10-14. Reviewer: fresh independent adversarial reviewer. Claim reviewed: the four explicit oriented dissections in [the design artifact](../searches/two-parent-wheel-seam-incidence-2026-10-14.md) might implement `H=2P+Q`, `K=P+2Q`, `φH=2H+K`, `φK=H+K` with convex pentagonal atoms and simple nonconvex parents. Verdict: **INVALID for this exact incidence**. The artifact's corner-count obstruction is correct. This review does not classify other incidence schemes or prove global impossibility.

## Independent necessary checks

Let `p,q,h,k` be areas. The two base decompositions give `h=2p+q`, `k=p+2q`; the two inflation equations give `φ²h=2h+k`, `φ²k=h+k`. Thus `h/k=φ` and `p/q=(2φ-1)/(2-φ)=3φ+1`. Substitution into atoms gives `φH=5P+4Q`, `φK=3P+3Q`. These necessary equations agree with the artifact but provide no embedding.

For a whole-native-edge disk made of three pentagons in a central wheel, the three paired seams remove six edge occurrences from the fifteen atomic edges, leaving nine boundary edges. For the proposed macro H wheel, three nine-sided parents and three paired seams leave `27−6=21` exposed edges. The macro K one-edge join leaves `18−2=16`. These counts are independent of coordinates and do not assume a preferred source tiling.

## Oriented incidence and endpoint audit

I checked the corrected cyclic wheel order directly. The pairings `b0↔rev(a4)`, `c0↔rev(b4)`, `a0↔rev(c4)` identify central vertices and yield the boundary arcs `a1 a2 a3 | b1 b2 b3 | c1 c2 c3`. Their three far endpoints are `a4=b1`, `b4=c1`, `c4=a1` at the vertex level. Thus the far angle sums are, respectively, `A(a4)+B(b1)`, `B(b4)+C(c1)`, and `C(c4)+A(a1)`. The H and K atom orders give the recorded P/P, P/Q, Q/Q distinctions. The central angle equations imply both atom central angles are `2π/3`; the three seam length equations in both wheels force `p0=p4=q0=q4`. I found no remaining orientation or endpoint mismatch in these specified words.

The macro H wheel repeats the same cyclic pairing on nine-edge parents. Its exposed arcs are `h1..h7 | h1..h7 | k1..k7`, with far endpoints `H1(v8)=H2(v1)`, `H2(v8)=K1(v1)`, `K1(v8)=H1(v1)`. The macro K join has boundary `H3(h1..h8) | K2(k0..k7)`, with seam endpoints `H3(v0)=K2(v0)` and `H3(v1)=K2(v8)`. Both words close and give the stated far angle correlations. These checks are conditional on the intended simple disjoint-interior embedding; the artifact does not claim such an embedding exists.

## Fatal genuine-corner count

In each base wheel, six native atom corners occur strictly inside its three exposed three-edge arcs. Each is a genuine convex pentagon corner. The three far seam endpoints are stipulated genuine, so each base parent has exactly nine genuine corners. Scaling or applying an isometry preserves that number.

In the macro H wheel, each exposed seven-edge parent arc has six internal boundary vertices. Each is a genuine corner of that parent; the declared incidence gives no other child sector along the exposed arc, so none is flattened by gluing. The macro H boundary therefore has at least `3·6=18` genuine corners even if all three macro far endpoints flatten. It cannot be similar to nine-corner H.

In the macro K join, each exposed eight-edge parent arc has seven persistent internal genuine corners. The union has at least `2·7=14` even if both seam endpoints flatten. It cannot be similar to nine-corner K. Failure follows before coordinate solving, edge-length matching, overlap testing, or recursive extension.

I also audited the later flat-inclusive endpoint budget. If any base wheel far endpoints flatten, its six internal exposed-arc atom corners remain genuine, hence each parent has `p_H,p_K≥6` genuine corners. Under the explicit additional hypothesis that each macro seam consumes one whole *genuine* parent edge and there are no other positive-length contacts, the H,H,K wheel removes two genuine corner endpoints per seam from the sum of child corner counts and may flatten at most three far joins. Thus it has at least `2p_H+p_K−9` genuine corners. Equality with the scaled H count `p_H` would require `p_H+p_K≤9`, contradicting the lower bound 12. The H,K whole-edge join similarly has at least `p_H+p_K−4` corners; equality with `p_K` would require `p_H≤4`. These inequalities are valid only for the stated whole-genuine-edge incidence. If base flattening merges a selected seam segment into a longer maximal parent edge, the proposed whole-edge rule no longer applies as written; treating that segment as a partial contact would be a new template, not a repair of this one.

The artifact correctly leaves geometric feasibility of the base wheels unproved. That uncertainty does not weaken the contradiction: if the stipulated simple embedded disks exist, their macro output has too many corners; if they do not, the proposed construction fails earlier. Partial contacts, internal children, multiple seams, or parent boundary words with different corner counts are outside this template and need a new complete incidence before another metric search. No repaired claim is presented, so no re-review of a repair is pending here.

The [small independent checker](verify_new_interface_stopping_gates_2026_10_14.py) asserts all four fixed boundary traversals, endpoint identifications, and every flat-inclusive integer corner budget. Read-only replay: `mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_new_interface_stopping_gates_2026_10_14.py`. Result: PASS.
