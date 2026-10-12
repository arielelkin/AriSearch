# The b=c=1 golden U/V pair admits no homothetic substitution

**Status:** proved internally by exact finite computation plus the
[wedge lemma](convex-substitution-wedge-obstruction.md) (2026-10-11); not
independently reviewed. This covers homothetic substitutions only. It is not
a statement about plane tilings by U and V.

## Statement

Let U have lengths (phi^3,phi^3,1,1,1) and V have lengths
(1,3phi+1,1,2phi,2phi), with angles after sides (1,3,4,4,3) and (2,2,4,3,4) in
units pi/5. This is the b=c=1 member of the
[area-compatible family](../searches/pentagrid-golden-metric-area-compatible.md).
For every lambda > 1, lambda U has no partition into isometric copies of U and V
(reflections, partial contacts and any counts allowed). Hence there is no
homothetic substitution for this pair. Together with the
[generic-parameter lemma](pentagrid-generic-metric-substitution-obstruction.md)
(case c/b not in Q(sqrt5)), the only open members of the family are those
with c/b in Q(sqrt5) and c ≠ b.

The exact phi^3 thirteen-piece question that timed out in Z3 in
[the phi^3 macro search](../searches/pentagrid-golden-metric-phi3-macro.md)
is answered negatively. The search is complete and exhausts after 5 nodes for
the U parent (5U+8V); a scratch run, not retained, also exhausted the V parent (8U+13V) after 6 nodes.
Only the U parent is needed.

## Proof

1. **Large lambda.** The wedge test with shapes {U,V} at the 36-degree angle
   is `dead` (5 nodes, maxd = 10.0902, R* = 15.9443). The U tip has chord
   distance h = 4.02874, so lambda U is impossible for lambda > 3.95763.
   The wedges at 72, 108 and 144 degrees are also `dead` (57, 187 and 1886
   nodes, R* <= 16.95).
2. **Small lambda.** Side sums force lambda in Q(sqrt5). lambda^2 is the root
   of an integer matrix, so lambda lies in Z[phi]. With lambda = p + q*phi,
   area forces counts (a,d) = (p^2+q^2, 2pq+q^2) and d > 0, and
   |lambda'| < lambda. The values with lambda <= 3.958 are phi, 2phi, 1+phi,
   2+phi and -1+3phi. For each, the complete exact search finds no
   partition of lambda U.
   [`convex-substitution-uv-golden.py`](../searches/convex-substitution-uv-golden.py)
   runs every p+q*phi with a+d <= 80, and every U parent dies within 5 nodes.

Certificates: [wedge](../certificates/convex-substitution-uv-golden-wedge.json),
[explicit runs](../certificates/convex-substitution-uv-golden.json).
