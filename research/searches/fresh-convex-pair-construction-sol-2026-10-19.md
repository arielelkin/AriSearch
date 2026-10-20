# Binary square-lattice power cells: one bounded construction cycle

Date: 2026-10-19. Status: **explicit exact convex P5/Q7 family constructed, killed by a rank-two periodic escape**. The unrestricted aperiodic-pair problem is unresolved. No novelty claim is made. This record owns only the adjacent uniquely prefixed Python/JSON files; no global log or registry was edited.

## Changed mechanism and first gate

Use a binary field on the square lattice as a prospective symbolic carrier, and take its weighted Euclidean power cells. This changes both source and mechanism from the Hat/Penrose/Pinwheel and regular-P5 routes: the binary field itself would have to be constrained by the two resulting unmarked convex shapes. The first falsifiable gate is whether two congruence classes with at least five sides can occur, and whether those same shapes already occur periodically.

An initial proposed shortcut, that a maximal- or minimal-weight site necessarily has a quadrilateral cell at small contrast, is **false**. For example, give the origin and its northeast diagonal neighbor weight d>0, and its east/north neighbors weight zero. The east/north bounds meet at ((1+d)/2,(1+d)/2), beyond the diagonal bound x+y<=1. Thus the diagonal clips the maximal-weight site's cardinal rectangle even for arbitrarily small positive d. The actual exact gate below replaces that discarded argument.

## Exact two-class family

Put h=1/2, a=(1+d)/2 and b=(1-d)/2, where 0<d<1/4. Define convex polygons, in counterclockwise order,

P=[(h,-b),(h,b),(b,h),(-b,h),(-b,-b)],

Q=[(a,-b),(a,h),(h,a),(-b,a),(-h,h),(-h,-h),(h,-h)].

All side lengths are positive. P has three 90-degree and two 135-degree corners; Q has one 90-degree and six 135-degree corners. Thus both are strictly convex, and they are distinct congruence classes. At d=1/5, their exact rational coordinates are also retained in the adjacent JSON. Their areas at that parameter are 161/200 and 239/200.

For z=(i,j) in Z^2 let r=i+j modulo 4 and assign

w(z)=d if r is 0 or 3, and w(z)=0 if r is 1 or 2.

The power cell at z is

C_z={z+x: 2 x dot v <= |v|^2+w(z)-w(z+v) for every v in Z^2}.

The four residue classes give, respectively, z+Q, z+P, z-P and z-Q. This follows directly from the eight inequalities for v in {-1,0,1}^2 excluding zero. The four cardinal bounds and clipping diagonal bounds produce exactly the vertices displayed above; the other diagonals are redundant.

For completeness, no farther lattice site supplies an omitted facet. The cardinal inequalities place every cell in |x_1|,|x_2| <= (1+d)/2 <5/8. For an integer v=(u,v_2) with max(|u|,|v_2|)>=2, it suffices to check

u^2+v_2^2 -(5/4)(|u|+|v_2|)-1/4 >0.

For integer n>=0, n^2-5n/4 has minimum -1/4 at n=1; for n>=2 it is at least 3/2. The displayed expression is therefore at least 1. This proves strict redundancy of all farther inequalities.

Power cells cover the plane with disjoint interiors: at each point the minimum of |x-z|^2-w(z) is attained because weights are bounded and |z| tends to infinity; ties lie on straight bisectors, and strict interiors cannot overlap. Hence this supplies full plane existence without compactness or a finite-patch inference.

But the field, and therefore this tiling, is invariant under (1,-1) and (4,0). Their determinant is 4. Its fundamental cell contains two copies of each polygon. Thus **every pair in this displayed one-parameter family has an explicit rank-two periodic tiling**, and is excluded for the original objective regardless of any other aperiodic power-cell realization it might possess. In particular an aperiodic binary carrier would not rescue these same two shapes.

## Bounded exact computation

Replay:

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/fresh-convex-pair-construction-sol-2026-10-19.py`

The dependency-free Python script uses Fraction arithmetic throughout. It constructs all 512 binary 3x3 local cells at contrast 1/5, removes collinear vertices, and computes an intrinsic congruence signature: the complete squared-distance matrix in cyclic vertex order, minimized over cyclic shifts and reversal. This is complete for congruence of strictly convex cyclically ordered polygons, including arbitrary rotations and reflections; it does not assume that congruences preserve the lattice axes.

It then enumerates all 65,536 labelled binary 4x4 tori, without symmetry reduction. Exactly 24 fields have no cell with fewer than five sides. Sixteen have three congruence classes with side counts {5,8}; eight have exactly two congruence classes with side counts {5,7}. One two-class witness is integer bit mask 14025, with rows

```
1001
0011
0110
1100
```

This is the d=1/5 member proved analytically above. The eight-site-neighbor reduction is justified by the preceding exact farther-site bound. The exhaustive computation completed, with no solver, timeout, randomness, or floating-point predicate. It establishes only its finite torus census, not a classification of binary fields or all power-cell pairs. The analytic periodic family does not depend on trusting that census.

## Stop rule and remaining gap

Stop this cycle under protocol section 5: the one concrete two-class family produced by the exact gate is killed by its own explicit periodic realization. The {5,8} fields fail the two-class gate. No construction candidate survives, and no larger torus or patch search follows.

Reopening needs an explicit changed field/weight/site mechanism yielding a *different* two-class convex pair and a new intrinsic shape-only forcing argument. Merely selecting an aperiodic binary field, or asserting that the chosen field is recognizable from its power cells, does not exclude the periodic tiling of the same shapes. The present record makes no theorem about other contrasts, other fields, other site sets, or the unrestricted two-convex-polygon problem. No literature theorem is used; no novelty assertion is supported or intended.
