# Every metric in the area-compatible U/V family needs partial contacts

**Status:** adversarially reviewed; [fresh hostile audit](../reviews/pentagrid-area-family-edge-obstruction-review.md) is valid without repair, with a separately structured exact native-link checker.
This excludes edge-to-edge tilings only. The unrestricted target remains open.

## Statement and conventions

For arbitrary positive real b,c, let U,V be the genuine convex pentagons in
[the area-compatible family](../searches/pentagrid-golden-metric-area-compatible.md).
Write phi=(1+sqrt(5))/2 and

    A=phi^2*b+phi*c, D=2phi*b+phi^2*c, E=phi*(b+c).

U has consecutive side lengths (A,A,b,c,b) and angles after the corresponding
sides (1,3,4,4,3)*pi/5. V has lengths (b,D,b,E,E) and after-side angles
(2,2,4,3,4)*pi/5. Then {U,V} has no edge-to-edge plane tiling, even allowing
all isometries and omission of either type. This theorem requires neither
Rao's monohedral classification nor an assumption that c/b is algebraic.
It does not exclude tilings with partial-edge contacts.

## Exact length and corner graph

The following strict identities settle all possible coincidences:

    D-A=(phi-1)b+c >0, A-E=b>0,
    E-b=(phi-1)b+phi*c>0, E-c=phi*b+(phi-1)c>0.

Thus D>A>E>max(b,c), and b=c is the only possible equality of named lengths.
Use an undirected graph whose nodes are lengths and whose edges are native
corners; the edge weight is the corner angle in units pi/5. A graph loop is
a corner with equal incident side lengths. Multiplicities below count native
corners on each reference tile:

| Tile corner | Length nodes | Weight | Multiplicity |
| --- | --- | --- | --- |
| U36 | A,A | 1 | 1 |
| U108 | A,b | 3 | 2 |
| U144 | b,c | 4 | 2 |
| V72 | b,D | 2 | 2 |
| V144 | b,E | 4 | 2 |
| V108 | E,E | 3 | 1 |

In an edge-to-edge tiling the genuine native corners around any vertex form
a closed walk in this graph, with total weight10. Whole-side matching gives
equality of the successive length nodes. Reflections change only the walk
direction and are included. There is no straight native-side sector at an
edge-to-edge vertex of genuine convex polygons. Full vertex valence need
not be three; weight10 handles every possible valence up to10.

## A V144 corner cannot occur

Suppose a weight10 closed walk uses a b--E edge. Removing this bridge
separates the E node, with its weight3 loop, from all other nodes.
The walk must therefore use b--E at least twice, costing at least8; four
uses already cost16. There are exactly two uses and residual weight2.
No E-loop fits. On the other side, a nonempty walk from b back to b has
weight at least4: its shortest possibility uses b--D twice, of weight4;
if b=c the U144 loop has weight4 as well. Reaching A and returning costs6,
and reaching distinct c and returning costs8. Although A has a weight1
loop, reaching A already exceeds the residual budget. Therefore no nonempty
residual excursion is possible, and the total cannot be10.
Every V copy has two such V144 corners. Consequently no V copy can occur
in any edge-to-edge tiling by these shapes.

## No U-only exception

If b differs from c, c has only the weight4 edge to b. A closed walk using
it requires at least two uses, costing8, and a remaining weight2 excursion
at b is impossible by the preceding argument. Thus U144 corners cannot
occur either, excluding a U-only tiling pointwise.

If b=c, the only U-only full star containing U144 is one U144 and two
U108 corners. Indeed a second U144 would cost8 and leave an unavailable
weight2 excursion at b. With one U144, the remaining weight6 walk from b
to b must go b--A--b using two weight3 corners; A-loops would exceed10.
U's middle b-side joins its two144 corners. Its side neighbor would have
to contribute108 at both endpoints, by the forced star at each endpoint.
No U side has108 at both ends: the five endpoint pairs are108/36,36/108,
108/144,144/144,144/108. The required whole-side neighbor does not exist.
This excludes U-only tilings in the remaining metric case and proves the
statement without a density argument or imported classification.

## Finite replay, scope and reopening condition

[The exact graph enumeration](../searches/pentagrid-area-family-edge-stars.py)
retains both complete graph cases and all rooted directed closed walks of
weight10. There are11 walks for b!=c and14 for b=c, after equal parallel
corner types are identified; their distinct signature counts are3 and4.
The retained [certificate](../certificates/pentagrid-area-family-edge-stars.json)
states the corner convention and complete signatures. This finite computation
checks the analytic graph facts; it is not a search over bounded plane patches.

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-area-family-edge-stars.py

The area ratio phi and the absence of monohedral tilings do not establish
mixed plane existence. Any whole-plane realization of this family must have
partial contacts. A genuine source-triangle recomposition may have partial
macro boundaries even if its underlying triangles meet edge-to-edge; this
lemma alone does not rule out such a recomposition. A new mechanism must
construct or exclude those admitted partial contacts, rather than impose
edge-to-edge placement on the final shapes.
