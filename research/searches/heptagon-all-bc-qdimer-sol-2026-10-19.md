# All-BC complementary-angle Q7: universal four-face carrier

Date: 2026-10-19. Exact symbolic certificate; no angle samples.

## Result and quantifiers

Let P be a regular unit pentagon. Let Q be any closed strictly convex heptagon with angle word A plus three adjacent BC/CB pairs, where A=144°, B=alpha, C=252°−alpha and 108°<alpha<126°. Require its sides 0,2,4,6 to have length one; its sides 1,3,5 may have arbitrary positive lengths satisfying closure.

**Every such actual metric Q admits an orientable translational torus carrier with exactly two P and two Q faces.** The two Q orientations differ by 180°, and corresponding QQ sides are glued. This holds throughout the angle interval, including alpha=120°, without needing a generic-angle hypothesis or the prior existence of a tiling. For an arbitrary tiling by the fixed Q and unit P, the passage to this unit-public hypothesis requires the purification argument below, especially at alpha=120°. An arbitrary positive closed Q metric whose four public sides are not unit is outside the explicit construction theorem. It does not claim that every alpha has a positive closing metric for every word.

The four rooted reversal classes are exactly:

| Representative | Three pair choices |
|---|---|
| ABCBCBC | BC, BC, BC |
| ABCBCCB | BC, BC, CB |
| ABCCBBC | BC, CB, BC |
| ACBBCBC | CB, BC, BC |

Reversing the rooted word reverses pair order and exchanges BC with CB; its action on the eight choices has four two-element orbits. The remaining six rooted reversal classes with three B and three C lie outside this all-BC domain.

## From an arbitrary tiling to the unit-public metric hypothesis

This implication uses the [complementary-angle flow gate](complementary-angle-flow-sol-2026-10-19.md) and its [independent hostile review](../reviews/complementary-angle-flow-hostile-sol-2026-10-19.md). Off alpha=120°, the only vertex stars are PPA and PBC. At alpha=120°, BBB is also allowed. In particular, the original tiling may contain BBB defects: among the four words here, ABCCBBC and ACBBCBC admit local t=2 assignments, where t counts B corners of a Q at BBB vertices. Therefore it would be incorrect to infer that the four public sides of every Q copy in the original tiling directly face P.

For balanced Q7, the reviewed branch budget gives sum of t over copies meeting a radius-R region bounded by O(R+1). Each defective Q has t at least 2. For any fixed radius r, the union of radius-r neighborhoods of those defect tiles inside a radius-R region has area O_r(R), whereas the region has area of order R squared. For sufficiently large R there is consequently a defect-free radius-r disk. Taking r tending to infinity, translate those disks to the origin and pass to a locally convergent subsequence of tilings by the same fixed compact polygons. Finite prototile shapes, bounded diameters, and positive minimum area give the needed local compactness; edge-to-edge matching and the absence of BBB in each fixed disk pass to the limit. This produces a defect-free plane tiling by the identical metric polygons.

In that purified tiling, A has QQ degree zero and each B/C has QQ degree one. The six-vertex path away from A has the unique perfect matching (1,2),(3,4),(5,6). Thus precisely sides 1,3,5 of every Q meet Q, while sides 0,2,4,6 meet P. Those four sides therefore have unit length. Q necessarily occurs: a tiling by P alone is excluded by the vertex-star inventory. Since the metric Q is fixed, these are equalities of its intrinsic side lengths, valid independently of which copies were defective in the original tiling. The explicit four-face construction now applies to that fixed metric.

Hence every fixed metric Q in the four-word all-BC family that tiles together with unit P has a doubly periodic tiling with that same P,Q, including alpha=120°. This conclusion uses the reviewed branch budget and translated compactness; it does not assert that the original tiling is defect-free or periodic.

## Explicit contact map

Darts 0–4 are P0; 5–9 are P1; 10–16 are Q0; 17–23 are Q1. Each dart starts at its indexed vertex. Glue the following pairs reversing boundary orientation:

```
QQ: (11,18), (13,20), (15,22)
PQ: (0,10), (5,12), (3,14), (8,16),
    (6,17), (4,19), (9,21), (2,23)
PP: (1,7)
```

The eight vertex cycles under next-after-mate are:

```
(0,11,19) (1,8,10) (2,17,7) (3,15,23)
(4,20,14) (5,13,21) (6,18,12) (9,22,16).
```

The second and third cycles are PPA, with angle sum 108+108+144=360°. Each remaining cycle is PBC because each specified QQ edge joins opposite B/C corners. Their sums are identically 108+alpha+(252−alpha)=360°. This verification uses the actual variable alpha, not a fixed numerical substitution. Edge lengths match: PP/PQ are unit; each QQ pair matches the same indexed length of congruent Q copies.

The symbolic direction verification fixes P0 side0 at heading 0°. It finds P1 at 108°, Q0 at 180°, and Q1 at 0°, independent of alpha and of the four words. Thus the requested Q half-turn is established, as are consistent phases for both pentagons. Reflection of a regular pentagon supplies no additional metric shape. These phases already supply a positive solution, so exhausting other phases/reflections is unnecessary.

## Why this is a degree-one plane tiling

Glue the four actual Euclidean polygons by this map. The face adjacency graph is connected. Edge interiors have ordinary disk neighborhoods. The listed vertex cycles are single circular links of total angle 360°, so every vertex also has an ordinary flat disk neighborhood. The quotient is therefore a compact connected oriented flat surface without cone points or boundary, with Euler characteristic 8−12+4=0, hence a flat torus.

Its complete simply connected flat universal cover is isometric to the Euclidean plane. The lifted polygon decomposition is a genuine decomposition of that plane: each open face is embedded, distinct open faces are disjoint, and all faces cover it. Thus this establishes degree-one coverage; a locally flat but overlapping placement in a chosen picture is not being used as evidence. Deck transformations are free orientation-preserving Euclidean isometries, hence translations, and compactness gives a rank-two lattice. The quotient has precisely the four specified faces.

This argument also prevents a hidden degeneracy of the lattice for any allowed positive closed metric. No explicit determinant estimate for seam vectors is needed: such a degeneracy would contradict the complete compact flat torus just constructed.

## Exact metric parameterization

The closure condition itself has an elementary exact one-parameter description. Set the side0 heading of Q to 0°, and write e(theta)=(cos(theta),sin(theta)). The four unit side headings are always 0°,108°,216°,324°, since the exterior turns across each BC/CB pair sum to 108°. Write a1,a3,a5 for the first angle of each ordered pair. The QQ unit directions are

```
u1=e(180−a1), u3=e(288−a3), u5=e(396−a5),
S=e(0)+e(108)+e(216)+e(324).
```

For cross(x,y)=x_x y_y−x_y y_x, let D=cross(u1,u3). Their heading difference is 108+a1−a3, which lies strictly between 72° and 144°, so D>0 throughout the stated alpha interval. Every closing metric is uniquely parameterized by t=length(side5) through

```
T=−S−t*u5,
length(side1)=cross(T,u3)/D,
length(side3)=cross(u1,T)/D,
length(side5)=t.
```

The exact feasible parameter set is the intersection of the three strict affine inequalities

```
t>0, cross(−S−t*u5,u3)>0, cross(u1,−S−t*u5)>0.
```

For any parameter in that set the polygon closes with strictly positive sides and positive exterior turns totaling 360°; it is strictly convex. The carrier above works for every such t. No equalities among the three QQ lengths are required.

## Replay and provenance

The map is the same as the four all-BC positive maps in the earlier [fixed-angle four-face certificate](../certificates/regular-pentagon-heptagon-fourface-carrier-sol-2026-10-19.json). The new verifier independently constructs all eight bit choices, reduces by rooted reversal, computes the vertex permutation, checks angle sums as exact affine expressions in alpha, and solves all face heading constraints as exact affine expressions modulo 360°.

[Verifier](heptagon-all-bc-qdimer-sol-2026-10-19.py); [certificate](../certificates/heptagon-all-bc-qdimer-sol-2026-10-19.json).

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/heptagon-all-bc-qdimer-sol-2026-10-19.py
```

Replay passed. There is no negative enumeration claim: all four domain words have the universal positive carrier.
