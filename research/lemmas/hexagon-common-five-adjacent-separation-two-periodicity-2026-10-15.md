# Common-five hexagons: adjacent and separation-two repeats

Date: 2026-10-15. **Status: independently reconstructed and hostile-reviewed VALID**; [review](../reviews/hexagon-five-adjacent-microstate-hostile-2026-10-15.md). Restricted periodic escape only.

Let A,B be genuine convex hexagons with the same five distinct numerical side lengths, each occurring once except for one doubled value in each hexagon. Suppose A's doubled sides are adjacent and B's doubled sides have cyclic separation two. If these shapes tile the plane with arbitrary isometries, reflections and partial contacts allowed, they admit a doubly periodic tiling.

The repeated values need not be the same. No claim is made here for two adjacent repeats, adjacent/opposite repeats, fewer numerical lengths, or pentagon-containing pairs.

## Defect-free source and complete native states

Apply the separately reviewed [hexagon defect-free limit theorem](hexagon-limit-and-periodicity.md), obtaining an everywhere-trivalent full-side source. Index each copy by its reference placement. Normalize A=(0,0,1,2,3,4). After rotating and choosing a boundary reading of B, its word is (p,q,p,r,s,t), where p is any of the five length values and (q,r,s,t) is any permutation of the other four. All 120 words are retained, with no dihedral quotient.

Unlike the nonadjacent-repeat case, a vertex may have repeated ray lengths and repeated native corner indices. Corner i lies between native sides i and i+1. Enumerate three ordered native corner occurrences, allowing repetitions, and independently select which of each corner's two native sides is its left and right ray. Retain choices whose consecutive ray lengths agree cyclically. Every physical vertex has one such reading: its three sectors can be read in plane order, and each reflected or unreflected tile determines its native arm order. No angle equation is assumed for a merely possible state.

For each state retain all three simultaneous full-side seams. Each seam carries its unordered pair of native SIDE slots, its multiset of the two near-end native corners, and its multiset of the two far-end native corners. These data retain both arms of the adjacent-equal corner. Unordered data forget some geometric information but do not remove an actual state.

Prune a state if any of its three seams has no remaining far-end state containing that SAME native side-slot pair with the required opposite-end corner multiset. Iterate to a fixed point. An actual state survives inductively because the physical full side has an actual far vertex whose slot and endpoint data agree. Thus the set of actual states is contained in the fixed atlas. There is no assertion that every retained state or support extends to a plane tiling.

## Exact finite gate

The independent [standalone checker](../reviews/hexagon-five-adjacent-microstate-independent-2026-10-15.py) enumerates directed native sectors directly, including all ordered triples, reflections and repeated occurrences. The retained [complete certificate](../certificates/hexagon-five-adjacent-microstate-gate-2026-10-15.json) records all initial and fixed states for 360 words across all three B separations; only the separation-two slice is needed here. Its 120 words split into:

- 96 fixed atlases which fail to cover all twelve native corners;
- 24 atlases which cover all corners but disconnect at least one species' doubled side slots in the possible native seam graph;
- zero remaining words.

The other separations have counts (88,24,8) and (92,24,4), respectively, in the same three categories. Those residual cases are not closed by this theorem.

Both species occur in the chosen source. A separation-two hexagon has no pure star, because it has distinct adjacent lengths and its corner graph is triangle-free. An adjacent-repeat hexagon alone also cannot supply all its native corners: its five-cycle-plus-loop corner graph has no three-distinct-ray triangle, and its only possible pure repeated-ray states use the loop corner 0 together with two copies of corner 1 or of corner 5, or three copies of corner 0. Its native corners 2,3,4 therefore cannot appear in a pure-A source. This handles sources that might otherwise omit a species, and ensures all twelve corners occur.

Consequently none of the 96 noncovering atlases can contain the actual source. In every remaining case connect native side slots whenever they meet across a seam of any fixed state. The actual seam graph is a subgraph, so its component partition refines this upper graph's component partition. At least one shape's doubled slots are disconnected in the upper graph and hence in the actual graph. Color native slots by actual seam component. Unequal numerical lengths cannot lie in the same component. That shape now has six different formal colors and its partner has at least five. Each actual source seam matches colors, and each color has a well-defined physical length.

The reviewed [six/five formal-color source theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md) applies and supplies a doubly periodic tiling by the original unmarked shapes. Different auxiliary colors may have equal physical lengths, as allowed by that theorem. No color restrictions are added to admitted target tilings. This proves the stated restricted theorem.

## Replay

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-adjacent-microstate-independent-2026-10-15.py
```

This independently reconstructs and checks the complete certificate. It imports no author modules, performs no geometric sampling, and uses no bounded negative tiling search. Exact finite counts supply only the necessary source gate; the positive periodic conclusion comes from the separately reviewed formal-color theorem. The unrestricted main problem remains unresolved.
