# Local obstruction for the two branching obtuse P5/Q8 representatives

**Status: exact computational proof for two fixed metrics, [independently hostile-reviewed](../reviews/branching-p5q8-hostile-2026-10-20.md).** The two branching representatives `k=1, reverse=False` and `k=7, reverse=True` in [the six-template gate](astra-obtuse-p5q8-six-template-gate-2026-10-20.md) admit no tiling of the plane by their unmarked convex P and Q tiles. The extra P0/P0 and P3/P3 seam options do not produce a repeatable strip or periodic carrier: a complete one-P neighborhood is already impossible. This does not exclude other metrics in either continuous template family.

## Exact metrics

Use the angle words `P=(100,110,100,120,110)` and `Q=(150,130,140,130,140,120,140,130)` in degrees, with counterclockwise side directions advanced by the exterior angles. Normalize `P4=Q0=Q7=1` and put `P0=P3=t`, where the unique algebraic solution of P closure and `P1=1` is `t=0.5976724774602396...?`. P closure gives `P2=0.6879027419128390...?`. These are exact elements of Sage's real algebraic field `AA`, defined by the vector closure equations in the script.

For the first metric set `Q1=P2`, `Q2=Q3=Q6=1/5`; solve `Q4,Q5` by vector closure. Its remaining approximate lengths are `Q4=2.098176825672934...`, `Q5=0.1830893683841313...`. For the second metric set `Q1=Q2=1/5`, `Q3=3/2`, `Q6=P2`; solve `Q4,Q5` by closure. Its remaining approximate lengths are `Q4=0.884175874777315...`, `Q5=0.1615868876224290...`. All lengths are exactly positive; both polygons are strictly convex by their positive side lengths, closure, and listed turns. Neither Q has a side of length `t` (exact comparisons in the script).

## Obstruction

In any tiling by these polygons, there are no side-interior T junctions: a straight angle plus two polygon corners already exceeds 360 degrees, since every corner is at least 100 degrees. Four corners also exceed 360 degrees, so every vertex has exactly three corners and every contact is full edge to full edge. Each P side of length `t` (sides 0 and 3) must meet another P side 0 or 3; Q has no side of that length. Thus every P has a P neighbor across each of these sides.

Fix a P tile and independently choose the neighbor's side (0 or 3) and reflection parity at each of its two `t` sides. This gives 16 local combinations. For any reflected neighbor, one or both seam endpoints have no Q corner whose exact angle and two adjacent side lengths complete the trivalent star. The four unreflected combinations have the following exhaustive exact result. The entries for Q options list the numbers of nonoverlapping reflected/unreflected Q placements at the four seam endpoints: central P vertices `(0,1,3,4)`. Every Q choice at vertex 1 overlaps every Q choice at vertex 3, and none of these choices is the same Q tile.

| Neighbor side across P0 | Neighbor side across P3 | Q options at vertices 0,1,3,4 | Universal Q conflict |
|---:|---:|---|---|
| 0 | 0 | 2,2,1,2 | vertices 1 and 3 |
| 0 | 3 | 2,2,1,1 | vertices 1 and 3 |
| 3 | 0 | 2,1,1,2 | vertices 1 and 3 |
| 3 | 3 | 2,1,1,1 | vertices 1 and 3 |

The exact checker constructs all placements from both Q reflection parities and both adjacent-ray orders, matches both incident Q side lengths, and applies the convex separating-axis test to every option pair. It permits a single Q tile to serve two endpoint stars by comparing equal image polygons before the overlap test. For both metrics it asserts the universal vertex-1/vertex-3 conflict in each of the four unreflected cases.

Finally, a tiling cannot omit P: Q's 130-degree corners cannot belong to any all-Q vertex, since the other two Q corners are at least 120 degrees. It cannot omit Q: P's 100-degree corners cannot belong to any all-P vertex, since the other two P corners are at most 120 degrees. Thus neither monohedral omission evades the local contradiction. Both fixed pairs are plane-nontilable.

Replay from repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/branching-p5q8-seam-transitions-2026-10-20.sage
```

The script prints every local branch and exact finite count. The conclusion is specific to these exact Q metrics and rests on the elementary edge-to-edge reduction above; it does not prove aperiodicity for any pair.
