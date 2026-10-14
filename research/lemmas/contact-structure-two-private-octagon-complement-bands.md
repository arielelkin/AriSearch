# The periodic two-private octagon core has invariant complementary bands

Date: 2026-10-13. Status: independently reviewed VALID; [bands and synthesis review](../reviews/contact-structure-two-private-octagon-core-complement-synthesis-review.md).
Depends on [common periodic Q core](contact-structure-two-private-octagon-periodic-core.md)
and the reviewed [native reduction](contact-right-angle-unrestricted-native-reduction.md).
This supplies scaffold geometry only; periodic P completion is separate.

## Statement

Under the periodic-core theorem hypotheses, assume an actual plane tiling
exists. Let K be the union of its Q tiles and v0 the common period of K.
Every connected component of R2 minus K is an open band bounded by two
simple proper polygonal curves, the facing boundaries of two adjacent Q
chains. Each component is invariant under v0. These bands have uniformly
bounded width in the direction perpendicular to v0, with a bound depending
only on the two prototiles. No bounded holes, permuted component or outside
half-plane occurs.

## Each chain is a closed topological strip

The core theorem gives a bi-infinite sequence of convex Q disks glued across
two distinct nonadjacent full native edges. Nonconsecutive Q tiles cannot
even touch. Send each disk homeomorphically to a rectangle, its two shared
edges to the two opposite crosscuts and its two remaining boundary arcs to
the longitudinal rectangle edges. Boundary parametrizations can be chosen
consistently on each shared edge. Gluing these maps yields a homeomorphism
of the chain union with R times [0,1]. The map and inverse are continuous
locally by finite gluing; properness of the periodic chain removes any end
accumulation. Local finiteness of the tiling makes its union closed.

Its two boundaries are consequently simple proper polygonal curves. Both
are within bounded distance of the core line, since all points of a tile
are within the tile diameter of its centroid. The common translation v0
preserves each chain and its longitudinal orientation. It cannot exchange
its upper and lower sides, since it preserves the far halfplanes normal to
v0. Thus it preserves each boundary separately.

## Order, adjacency and absence of outermost chains

Orient the common period horizontally and orient every core to positive
horizontal infinity. A core separates the plane into upper and lower
components containing the respective far halfplanes. Every other disjoint
core lies wholly in one component. This gives a total transverse order;
upper components are nested, which proves transitivity. It is the usual
order of disjoint proper parallel lines and does not require each core to
be the graph of a function.

Only finitely many chains lie between two specified chains. Their core
centroids must lie in a bounded transverse band between those two curves.
Translate each by an integer multiple of v0 to put one centroid in a fixed
longitudinal fundamental interval. The resulting representative Q tiles
meet a compact rectangle. Positive minimum area and bounded diameter permit
only finitely many such tiles in the actual tiling. Therefore the order has
adjacent chains above and below whenever chains exist on those sides.
This argument uses the common period and area packing, not an unsupported
claim that local finiteness alone prevents infinitely many chains far away.

Every P has at least two Q-neighbor native sides by its alternating native
species word, and those contacts are whole. If DP is its diameter, each
point of each P is within DP of K. Coverage therefore implies

    R2 is contained in the closed DP-neighborhood of K.       (1)

An outermost core would bound all other cores on one side. Since that core
stays in a bounded horizontal slab and every Q tile is within a fixed
Q diameter of its core, K would be bounded in the opposite normal direction.
A far halfplane would violate (1). Thus the chain order has no outermost
member. Packing in a periodic fundamental interval also rules out infinitely
many chains in any bounded transverse region. Hence the chains extend to
both transverse infinities and every chain has immediate neighbors.

The region between the upper boundary of a chain and the lower boundary of
its immediate successor is connected, is an open band, and contains no Q.
The proper strip boundaries separate it from every other such region. These
regions exhaust the complement: the chain order is discrete and unbounded
in both directions. Each band is bounded by two individually v0-invariant
curves, so it is itself v0-invariant. No bounded component can be hidden
inside one chain, because that chain is a topological strip.

## Uniform transverse width

Let DQ bound Q diameter. In each chain there are two centroid positions
modulo v0. Their normal coordinates differ by at most 2DQ, because the
corresponding adjacent tiles share an edge. Let h be the average of those
two normal coordinates. Every Q tile in that chain, and its core, lies in

    h-2DQ <= normal_coordinate <= h+2DQ.                   (2)

Consider adjacent ordered chains with averages h1,h2. If h1-h2>4DQ,
(2) would put the second entirely below the first, contrary to the order.
Thus h2-h1>=-4DQ. All cores below the first are in its lower component and
have normal coordinates at most h1+2DQ; their Q tiles are at most another
DQ away. Likewise all cores above the second and their tiles have normal
coordinate at least h2-3DQ. There are no intermediate chains. If
h2-h1>6DQ+2DP, a point on the intervening middle horizontal line would be
at distance greater than DP from all Q tiles, contradicting (1). Hence

    -4DQ <= h2-h1 <= 6DQ+2DP.

The open band is trapped between the two boundary slabs (2), so its total
normal width is at most |h2-h1|+4DQ <= 10DQ+2DP. This coarse bound is enough
for a uniform finite-placement alphabet in a later strip-completion theorem;
no metric sharpness is claimed.

## Scope

No FLC, finite orientation set, frequency, substitution or original edge-to-edge
restriction is assumed. The fixed two-tile motif and whole contacts involving
Q come from the prior reductions. P-P T contacts are still permitted in the
bands. Existence of these invariant scaffold bands does not itself periodize
an arbitrary P filling. That separate finite-state extension argument is proved and reviewed in the
[anchored-strip theorem](periodic-scaffold-anchored-strip-completion.md) and
[all-metric synthesis](contact-right-angle-two-private-all-metric-periodic-escape.md).
No computation or novelty claim is made.
