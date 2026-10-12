# Fixed hat scaffold: every convex whole-kite cluster has a periodic escape

Date: 2026-10-12. **Exact narrow gate independently reviewed VALID.**
The [extracted theorem](../lemmas/hat-eight-kite-convex-cluster-obstruction.md)
records its complete proof and [hostile review](../reviews/hat-eight-kite-convex-cluster-review.md).
No construction candidate survives this gate. The broader hat
source-decoration route has not been reopened.

## Mechanism and primary source

The proposed compiler groups whole cells of the reference hat's eight-kite
scaffold into convex final tiles. Unlike an everywhere-trivalent source,
this scaffold has vertices of degree four and six, so the earlier trivalent
fusion obstruction does not automatically exclude it. Grouping could in
principle preserve a hat-supported source partition; unrestricted recognition
would still need proof.

Smith, Myers, Kaplan and Goodman-Strauss define the hat as eight kites of
the [3.4.6.4] Laves tiling and prove it aperiodic. Their Section6 defines
the direction-preserving Tile(a,b) family. These source facts are taken from
their primary paper, [An aperiodic monotile](https://arxiv.org/html/2303.10798v3),
Theorem1.1 and Section6. The new calculations below concern only the
fixed reference Tile(1,sqrt3), not that entire family.

The source geometry is independently retained in
`research/searches/source-decoration-hat-patch.py`. Its exact `ref_kites()`
returns the eight whole cells. No unfinished 154-segment decoration search,
new patch solver or larger decoration enumeration is used here.

## Exact finite gate

Examine all 255 nonempty subsets of these eight kites. Because they are
interior-disjoint grid cells, their union is convex precisely when its area
equals the area of the convex hull of its vertices. Both hull and areas
are decided exactly in Q(sqrt3), with the positive real embedding. Collinear
boundary subdivisions are removed by the hull computation.

There are **16 convex subsets**:

* eight singleton kites, each a quadrilateral;
* one three-kite triangle, mask168;
* five adjacent two-kite pentagons, masks6,9,12,48,192;
* two adjacent three-kite pentagons, masks13,14.

The bit convention is mask=sum_(i in cluster)2^i, with kite indices defined
by the exact certificate. There are no other convex subsets, including
none with six or more intrinsic corners.

The only partition of the eight cells into clusters with at least five
corners is

    {9,6,48,192}.

All four pieces are congruent; this produces one final class, not two.
More decisively, **every one of the sixteen convex clusters tiles periodically
by itself**, so no finite protoset consisting of such shapes can be aperiodic.

## Explicit periodic escapes

Let H be the regular hexagon with radius2 centred at0. Its six standard
kites are bounded by a centre, two successive edge midpoints and the
intervening hexagon vertex. All rotations below are Euclidean rotations.

A representative two-kite pentagon, counter-clockwise, is

    P=[(0,0),(3/2,-sqrt3/2),(2,0),(1,sqrt3),(0,sqrt3)].

It has angles (120,90,120,120,90). Its two kites are consecutive around
the centre. The three sets P,R_(120)P,R_(240)P have disjoint interiors
and union H. Translating this three-piece dissection over the regular
hexagon lattice gives a periodic monohedral P tiling. Lattice generators
may be taken as (3,sqrt3) and (0,2sqrt3).

A representative three-kite pentagon is

    Q=[(0,-sqrt3),(1,-sqrt3),(2,0),(1,sqrt3),(0,sqrt3)].

It is the right half of H. Q and R_(180)Q cover H with disjoint interiors.
The same lattice gives a periodic monohedral Q tiling.

Singleton kites periodically tile by the standard six-kite subdivision of
each H. The three-kite triangle has a periodic tiling because every triangle
and its half-turn across a side form a parallelogram. Thus all four shape
classes among the sixteen subsets have explicit periodic escapes. Using
both members of a two-shape protoset is not required by the target definition.

## Why the deformation is a separate problem

The positive two-parameter Tile(a,b) family changes the outline's two edge
length classes while preserving its outline angles. The fixed standard kite
has angles (60,90,120,90), which fix its short/long side ratio to1/sqrt3.
Scaling these eight congruent standard kites therefore supplies only the
similarity line b=sqrt3*a. A claim that the same eight congruent standard
kites provide a source decomposition for arbitrary a,b would need a new
argument and cannot be inferred from the published outline deformation.

Unequal/nonstandard internal quadrilaterals, changed interior seams,
cuts through kites, and clusters extending across multiple hats are outside
this gate. They need exact geometry and a new periodic-escape check before
any enumeration. Neither a hat-supported partition nor the source's
aperiodicity implies unrestricted final-shape forcing.

## Artifacts and replay

Producer:
`research/searches/hat-eight-kite-convex-cluster-gate.py`.
Certificate:
`research/certificates/hat-eight-kite-convex-cluster-gate.json`.

The certificate records the defining field, all eight cells, the hat outline,
all convex hulls, exact masks and all eligible whole-cell partitions. Congruence
is checked using complete pairwise squared-distance matrices under every
cyclic shift and both orientations. The source point and domain are fixed;
no numerical threshold, random seed or timeout is involved.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/hat-eight-kite-convex-cluster-gate.py TEMP_CERTIFICATE.json

The computation passed on2026-10-12. An independent reviewer checked the
exact cell geometry, convexity exhaustiveness and periodic witnesses. This
record is a failed compiler mechanism, not a construction or impossibility
theorem for arbitrary two convex polygons.
