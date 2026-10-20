# Periodic escape for a binary power-cell pentagon/heptagon family

For any real `0<d<1/4`, set `h=1/2`, `a=(1+d)/2`, `b=(1−d)/2`, and take the polygons with counterclockwise vertices

```text
P: (h,−b), (h,b), (b,h), (−b,h), (−b,−b)
Q: (a,−b), (a,h), (h,a), (−b,a), (−h,h), (−h,−h), (h,−h).
```

They are distinct strictly convex pentagon and heptagon shapes: P has three 90° and two 135° corners, Q one 90° and six 135° corners, with positive side lengths throughout the interval. **This entire pair family admits a rank-two periodic tiling**, so no member is an aperiodic pair under the original definition.

Assign square-lattice site `z=(i,j)` weight `d` if `i+j mod 4` is 0 or 3, otherwise weight zero, and take its Euclidean power cell

```text
C_z={z+x: 2 x·v ≤ |v|²+w(z)−w(z+v) for every v∈Z²}.
```

The eight nearest-site inequalities give, for the four residues, `z+Q`, `z+P`, `z−P`, `z−Q`. All farther lattice inequalities are redundant: nearest cardinal bounds imply each coordinate magnitude at most `(1+d)/2<5/8`, and any integer offset with an absolute coordinate at least two satisfies the strict bound derived in the [full construction proof](../searches/fresh-convex-pair-construction-sol-2026-10-19.md). Bounded weights ensure every point has a nearest power site, so the cells cover the plane with disjoint interiors. The weight field is invariant under independent translations `(1,−1)` and `(4,0)`, giving a rank-two period lattice of determinant four.

The producer's exact [Python replay and JSON certificate](../searches/fresh-convex-pair-construction-sol-2026-10-19.md) independently enumerate the finite 4×4 binary-field gate at `d=1/5`; that census is not needed for the analytic periodic escape. An [independent Sol hostile review](../reviews/fresh-power-cell-hostile-sol-2026-10-19.md) passed the symbolic polygons, full power-cell realization and period claim. This construction is a counterexample to any claim that a two-class convex output from a binary square-lattice power diagram is automatically aperiodic. It does not classify other fields, contrasts or site sets.
