# A two-angle pentagon pair must pass through the Cairo angle family

**Status:** adversarially reviewed; [fresh hostile review](../reviews/two-angle-pentagon-cairo-review.md) found no unresolved defect. This is a necessary-condition reduction, not a solution of the original problem.

## Theorem

Let P and Q be genuine compact convex pentagons with nonempty interiors. Suppose their combined set of interior angle values has cardinality at most two. If the pair is aperiodic under unrestricted isometries and contacts, then both polygons have, up to cyclic rotation and reflection, the angle word

    (pi/2, 2pi/3, pi/2, 2pi/3, 2pi/3).

In particular the two right corners are nonadjacent. No assertion that these angle words can be closed with prescribed lengths or that they force aperiodicity follows. Side lengths and partial-edge contacts remain unrestricted in this surviving family.

## Local and boundary facts

At any point which is a genuine tile corner, local finiteness and convexity give one of two cases: all incident sectors are genuine corners, with total 2pi, or one tile contributes a straight sector and all genuine corner sectors on the other side have total pi. Two straight sectors would fill the disk and leave no genuine corner. This applies to isolated vertex-to-side touches as well as T-junctions.

For fixed polygon prototiles the native corner counts in a square have O(R) boundary error: tiles meeting a width-D boundary strip number O(R), by bounded diameters and minimum positive area. Vertex incidences have uniformly bounded valence, by the positive minimum angle. Thus summing any inequality between native corner types over vertices gives the same inequality on total native corner counts up to O(R). This does not assume edge-to-edge contact. Tile count N(R) is Theta(R^2).

If there is only one angle value, both pentagons are equiangular with angle 3pi/5. No positive integer multiple of this equals pi or 2pi, so no native corner can occur in a plane tiling. The pair is untileable.

Hence let alpha<beta be the two values. Let k count alpha corners in P. Subtracting P's and Q's angle sums shows Q has exactly the same k, since (kP-kQ)(alpha-beta)=0. The sum is

    k alpha + (5-k) beta = 3pi.                       (1)

If k=0 or5, both pentagons are the equiangular case just excluded. Assume k=1,2,3,4. At a vertex write p,q for the numbers of alpha,beta corner sectors. The sum p alpha+q beta is pi or2pi. We need only vertices with q>=1 when deriving exclusions. In all cases below beta>3pi/5, so q<=3 in a full vertex and q<=1 in a half vertex.

## k=1

Here beta=(3pi-alpha)/4 and 0<alpha<3pi/5. If q=3 in a full vertex, adding even one alpha exceeds 2pi because 3beta+alpha=9pi/4+alpha/4>2pi. Therefore p=0, forcing beta=2pi/3 and alpha=pi/3.

Unless alpha=pi/3, no such vertex exists. For q=2 at a full vertex, p alpha=(pi+alpha)/2>alpha, so p>=2. For q=1 at a full vertex p>=1; at a half vertex likewise p>=1 because pi-beta>0. Thus at every vertex containing beta, p>=q. At alpha-only vertices the same inequality holds. Summation would give N(R)>=4N(R)+O(R), contradicting quadratic growth. Hence the only tileable k=1 data are alpha=pi/3,beta=2pi/3.

Each such pentagon has a pi/3 corner adjacent to a 2pi/3 corner. Their sum is pi, so the half-turn construction below gives that member a periodic monohedral tiling. This excludes aperiodicity of the pair.

## k=2

Now beta=pi-2alpha/3, with 0<alpha<3pi/5. A full vertex with q=3 satisfies (2-p)alpha=pi, selecting alpha=pi/2,p=0; p=1 would give alpha=pi, and p>=2 gives no positive solution. For q=2 the full sum requires p=4/3, impossible. For q=1 the full sum requires alpha=pi/(p-2/3); its allowed range forces integer p>=3. A half vertex with q=1 requires p=2/3, impossible.

Unless alpha=pi/2, every beta vertex therefore uses at least three alpha sectors per beta sector. Summation would give 2N(R)>=9N(R)+O(R), impossible. Hence the only surviving data are alpha=pi/2,beta=2pi/3.

If either pentagon's right corners are adjacent, their sum is pi and the same half-turn construction gives a periodic monohedral escape. If neither has adjacent right corners, the unique cyclic arrangement of two nonadjacent right corners and three 2pi/3 corners is the angle word stated in the theorem.

## k=3

Here beta=3(pi-alpha)/2 and pi/3<alpha<3pi/5. Inspect q=1,2,3 in the full sum:

    q=1: alpha=pi/(2p-3), no value in the strict interval;
    q=2: alpha=pi/(3-p), only alpha=pi/2,p=1;
    q=3: alpha=5pi/(9-2p), only alpha=5pi/9,p=0.

In a half sum only q=1 is possible, giving alpha=pi/(3-2p), with no value in the strict interval. These conclusions handle every integer p>=0 analytically, without a valence cutoff.

At alpha=5pi/9,beta=2pi/3, every beta vertex consists only of three beta sectors. No positive multiple of alpha equals pi or2pi, and no mixed alpha/beta vertex was admitted by the preceding enumeration. Thus the native alpha corners cannot occur, excluding tilability.

At alpha=pi/2,beta=3pi/4, each pentagon has three right corners among five positions, so at least two are adjacent. The half-turn construction gives a periodic monohedral escape. No aperiodic case remains.

## k=4

Equation (1) gives beta=3pi-4alpha, and convexity/order force pi/2<alpha<3pi/5. All angles are strictly obtuse. The reviewed all-obtuse theorem forces edge-to-edge trivalence, which is impossible for two pentagons by the square-window side-count/curvature identity. The pair is untileable.

## Half-turn periodic escape

For any genuine convex pentagon having consecutive angles whose sum is pi, glue it to its half-turn about the midpoint of the side between those angles. Interiors lie in opposite half-planes and are disjoint. At both seam endpoints the new boundary is straight, and all other corners remain strictly convex. The union is a convex centrally symmetric hexagon with six genuine sides. Its lattice translates tile the plane by the elementary cut-and-translate proof in [the reviewed equilateral obstruction](new-angle-equilateral-rational-obstruction.md). Retaining the two pentagons inside each translated hexagon gives a doubly periodic monohedral tiling. No edge-length equality beyond the matched copy is needed.

## Dependencies and remaining gap

The local full/half-sector dichotomy and native-corner counting proof above are elementary and valid for unrestricted contacts. The k=4 exclusion uses [all-obtuse forcing](obtuse-edge-forcing.md) and [the window side-count bound](side-count-and-monohedral-obstructions.md). Half-turn lattice escape uses the stated elementary centrally symmetric hexagon lemma. No pentagon-family completeness theorem, rational-angle hypothesis, or source matching rule is imported.

The finite p,q equations were handled symbolically for unbounded p. No search, numerical equality, finite denominator assumption, or computational witness supports this theorem. The two pentagons need not both occur; both have identical angle multiplicities, so the incidence contradictions also cover a tiling using one type alone.

The surviving Cairo-angle pair leaves a concrete unresolved metric problem: which positive Q(sqrt3)-linear side lengths admit a mixed plane tiling, and can any two such pentagons exclude all translational periods? Partial contacts at the right corners are permitted and must be handled. The newly found Cairo trial family has a periodic four-face torus witness; it kills only that family. A genuine new candidate needs a different length mechanism or more than two angle values.
