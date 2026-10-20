# Direct three-arm convex dissection: exact metric compatibility gate

Date: 2026-10-20. Status: **falsified for the stated four-\(P\), one-\(H\) dissection**. This is a restricted dissection obstruction, not a result about arbitrary convex pairs or plane tilings.

## Object and exact field

Let \(R\) rotate by \(120^\circ\), \(O=(0,0)\), \(S=(1,0)\), \(T=RS\), \(V=S+v\), \(W=T-Rv\), and \(P=(O,S,V,W,T)\). Let \(G=(V,W,RV,RW,R^2V,R^2W)\). The intended construction has \(G=P\cup RP\cup R^2P\), and \(H=G/t\), where \(t=\sqrt{2+\sqrt7}\), the positive root of \(t^4-4t^2-3=0\). The area equation for \(tP=4P+H\) is therefore exact. Write \(a=|v|\) and \(b=|W-V|\). The cyclic side lengths are \(P:(1,a,b,a,1)\) and \(H:(b/t,2a/t,b/t,2a/t,b/t,2a/t)\).

## Exhaustive necessary boundary equations

If four strictly convex copies of \(P\) and one strictly convex copy of \(H\) cover \(tP\), a given straight parent edge can contain at most one whole side from each child. Its length must have the form

\[
  n_1+n_a a+n_b b+h,
  \quad n_1,n_a,n_b\in\mathbb Z_{\ge0},\quad
  n_1+n_a+n_b\le4,\quad
  h\in\{0,b/t,2a/t\}.
\]

There are \(35\cdot3=105\) equations for each target length \(t,ta,tb\). This is deliberately an enlarged necessary domain: it does not enforce per-tile side inventories, edge order, or interior packing. Exact linear algebra over \(\mathbb Q(t)\) intersects two target equations, tests the third, and separately checks for common rank-one lines. The latter set is empty. Positivity and the circle-intersection condition \(|a-b|\le\sqrt3\le a+b\), with the strict inequalities used for noncollinear branches, leave precisely eight isolated pairs:

| \(a\) | \(b\) | Convexity of both \(P,G\) |
| --- | --- | --- |
| \((5t-t^3)/2\) | \((t^3-3t)/2\) | fails; \(v_y=0\) |
| \(t/3\) | \(t^3/3-t\) | passes for both signs of \(v_x\) |
| \(5t-t^3\) | \(t^3-4t\) | fails; a negative native turn |
| \((t^3-2t)/7\) | \((3t^2-6)/7\) | passes for both signs of \(v_x\) |
| \((t^3-t)/6\) | \((t^2-1)/2\) | fails; a negative native turn |
| \(t^3-4t\) | \(t^2-3\) | fails; a negative native turn |
| \((t^3-3t)/2\) | \((t^2-3)/2\) | fails; a negative native turn |
| \(t\) | \(t^3-4t\) | fails; a negative native turn |

For each pair, \(b=|v-i\sqrt3|\), so \(v_y=(a^2+3-b^2)/(2\sqrt3)\) and \(v_x=\pm\sqrt{a^2-v_y^2}\). Circle tangencies are included in the enumeration. Exact algebraic-real comparisons test the consecutive cross products of both polygonal words. The two signs exchange the angle order but have the same outcome.

## Parent-corner obstruction for both convex metrics

For both surviving metrics and either sign of \(v_x\), exact algebraic-cosine comparisons place the native angles of \(P\) and \(H\) in the disjoint bins \((57^\circ,59^\circ)\), \((64^\circ,70^\circ)\), exactly \(120^\circ\), \((121^\circ,123^\circ)\), and \((170^\circ,176^\circ)\). Exactly one \(P\) corner has angle \(120^\circ\), namely \(O\); \(H\) has none. No sum of two or more child angles is \(120^\circ\): two angles in the smallest bin sum to less than \(118^\circ\); replacing either with the next bin makes the sum exceed \(121^\circ\); three smallest angles exceed \(171^\circ\). Thus a dissection of \(tP\) must place a single \(P\) corner at the parent \(O\). Both incident sides of that child have length \(1\), and, since \(1<t\), each lies wholly along a parent edge of length \(t\).

The exact length equations for either parent unit edge are unique at each surviving metric:

| Metric | Only representation of \(t\) |
| --- | --- |
| \(a=t/3,\ b=t^3/3-t\) | \(t=3a\) |
| \(a=(t^3-2t)/7,\ b=(3t^2-6)/7\) | \(t=2a+b/t\) |

Neither representation contains a length-\(1\) child side. This contradicts the forced \(P\) at \(O\). **No positive strictly convex member of this direct three-arm family admits the proposed \(tP=4P+H\) dissection.** The two convex metrics survive scalar length equations but fail the corner-aware boundary gate. Species-omission and packing gates are unnecessary after this contradiction.

## Scope, replay, and deduplication

Run `mise exec -- conda run --no-capture-output -n arisearch sage research/searches/triarm-metric-compatibility-gate-2026-10-20.sage`. The script states all 105 equations per target, verifies no common rank-one line, prints all eight metric pairs, checks both geometric branches with exact algebraic-real order, certifies angle intervals using exact cyclotomic cosines, and asserts the length-1 boundary contradiction. Printed decimal coordinates and turns are diagnostics only.

This pair is a direct threefold pentagon/hexagon geometry rather than a relabeling of the Cairo, equiangular-hexagon, P5/Q7 obtuse, or source-derived candidates listed in [the shape-first deduplication audit](shape-first-dedup-audit-2026-10-20.md). The obstruction is specific to this substitution inventory and geometry; it does not exclude another placement count, inflation, or unrelated two-polygon construction.
