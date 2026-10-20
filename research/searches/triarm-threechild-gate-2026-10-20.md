# Direct radial three-child substitution gate

Date: 2026-10-20. Status: **the specified second-parent dissection is obstructed and independently reviewed**. This is a restricted statement about one substitution inventory, not a theorem on arbitrary plane tilings by the shapes.

**Preflight deduplication:** the previously reviewed [forest gate](../lemmas/six-child-topology-substitution-consequences.md) already forbids any nontrivial convex pentagon parent partitioned into fewer than six children with at least five sides. Hence the proposed three-child P parent is impossible before metric enumeration. The calculation below is retained as a redundant exact boundary check and as a record of its corrected corner error. The [independent hostile review](../reviews/triarm-threechild-hostile-2026-10-20.md) now validates the restricted conclusion.

## Geometry and area

Let R rotate counterclockwise by 120 degrees, O=(0,0), S=(1,0), T=RS, V=S+v, W=T−Rv, P=(O,S,V,W,T), G=(V,W,RV,RW,R²V,R²W), and H=G/t. Require P and G strictly convex. Set a=|v| and b=|v−i√3|. The side words are P=(1,a,b,a,1) and H=(b/t,2a/t,b/t,2a/t,b/t,2a/t).

The exact radial first parent is tH=G=P∪RP∪R²P. The new second-parent inventory is tP=2P+H. Its area equation is t²=2+3/t², hence **t=√3**. This differs from the prior 4P+H inventory, though it reuses the radial geometry and first parent.

## Exhaustive scalar boundary screen

Each straight parent side must be covered by whole child sides. A strictly convex child can place at most one of its sides on one parent support line. Therefore each target tL, L in {1,a,b}, must equal i+j a+k b+h, where i,j,k are nonnegative integers with i+j+k≤2 and h is one of 0,b/t,2a/t. There are 30 deliberately enlarged possibilities per target. Exact linear algebra over Q(√3) intersects equations for all three targets and checks that no common rank-one metric line is omitted.

Positivity and the circle-intersection conditions |a−b|≤√3≤a+b leave 57 isolated pairs. Reconstructing y=(a²+3−b²)/(2√3) and x=±√(a²−y²), then testing all consecutive cross products of P and G exactly, leaves nine strictly convex metrics:

| a | b | x branch | Unit-edge scalar words |
| --- | --- | --- | --- |
| t/3 | 2t/3 | 0 | a+b |
| (3−t)/2 | (3t−3)/2 | 0 | b+b/t; a+b; 1+2a/t |
| t/2 | t/2 | 0 | 2b; a+b; 2a |
| 4t−6 | 6−3t | 0 | a+b |
| 1 | t/2 | ± | 2b |
| 1/2+t/3 | t/2 | ± | 2b |
| (3t−3)/2 | (3−t)/2 | 0 | a+b |
| 2t/3 | t/3 | 0 | a+b |
| (18−3t)/11 | (6t−3)/11 | ± | 2b+b/t |

Here ± means both nonzero signs of x. Native side identities remain distinct even when numerical lengths coincide, such as a=1. Scalar words are only necessary conditions.

## Corrected native-side corner and boundary enumeration

The parent O angle is 120 degrees. Every child angle exceeds 60 degrees, so one child occupies it. For the six x=0 metrics, P has angle word (120,90,120,120,90), and H is equiangular 120 degrees. In particular, **P has three 120-degree vertices**: vertex 0 has incident lengths (1,1), while vertices 2 and 3 each have incident lengths (a,b). For the three nonvertical metrics, only P vertex 0 has angle 120 degrees, and H has no such angle. The replay certifies these comparisons using exact algebraic cosines.

The initial version of this report incorrectly rejected the two (a,b) corners and numerical label collisions. The corrected replay enumerates each native side index separately for two named P children and one H. It chooses at most one side per child on each of the five parent edges, requires exact edge-length sums, never reuses a side, and requires the two sides incident at the parent O corner to belong to an actual 120-degree child corner. This remains an enlarged necessary combinatorial model, since it does not assert that the selected sides can be placed or packed.

Six convex metrics have **zero** assignments in this corrected model. The first three metrics in the table survive it:

| (a,b) | Assignments | Forced H boundary support in every assignment |
| --- | ---: | --- |
| (t/3,2t/3) | 128 | No H side on any parent edge |
| ((3−t)/2,(3t−3)/2) | 576 | Long H sides on both parent unit edges |
| (t/2,t/2) | 6912 | Short H sides on the three consecutive middle parent edges |

These counts retain child labels, native side indices, and corner orientation. They count necessary boundary allocations, not dissections.

## Placement obstructions for the three surviving allocations

At (a,b)=(t/3,2t/3), H has no boundary side, though it might touch the parent boundary at isolated points. Choose h inside H. Every ray from h must encounter one of the two convex P children after leaving H and before leaving the parent, except possibly finitely many isolated contact directions. Each P child is disjoint from h and subtends an angular interval strictly shorter than 180 degrees. Two such intervals cannot cover all ray directions. Thus two convex P children cannot surround H. Independently, b=2a makes H a regular hexagon with a periodic monohedral tiling.

At (a,b)=((3−t)/2,(3t−3)/2), the two parent unit edges, traversed counterclockwise, have directions 0 and 300 degrees. Both require long H sides. The three long sides of an equiangular H have oriented directions spaced by 120 degrees under any isometry, including reflections. They cannot occupy parent edges with a 60-degree direction gap.

At (a,b)=(t/2,t/2), the consecutive middle parent edges have directions 90,150,210 degrees. All three require short H sides. The three short H sides likewise have directions spaced by 120 degrees; they cannot occupy these three parent edges.

Thus no strictly convex member of this direct radial family admits the specified **tP=2P+H** dissection. The result does not exclude unrestricted tilings by any of the nine pairs, another substitution inventory, or aperiodicity in another family. No H-only or P-only omission classification was needed to reject this dissection.

## Replay and deduplication

Run:

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/triarm-threechild-gate-2026-10-20.sage
```

The script checks the scalar equations, all real geometric branches, strict convexity, exact angle comparisons, and all native-side boundary allocations. It asserts the three compulsory H support patterns; the final placement arguments are given above. Printed decimals are diagnostics only. This is a changed child inventory from [the preceding four-P gate](triarm-metric-compatibility-gate-2026-10-20.md), rather than a new shape-first pair mechanism. No literature novelty claim is made.
