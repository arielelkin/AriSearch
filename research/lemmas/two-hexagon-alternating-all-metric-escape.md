# Alternating/alternating angle hexagons are untileable or periodic for every metric

Date: 2026-10-12. Status: [complete exact chain independently reviewed VALID](../reviews/two-hexagon-alternating-all-metric-chain-review.md).
This closes the specified continuous angle family. It does not establish the
unrestricted two-convex-polygon impossibility theorem.

Fix two genuine strictly convex hexagons with native angle words

    A=(p,q,p,q,p,q), B=(r,s,r,s,r,s),
    q=240-p, r=360-2p, s=2p-120, 90<p<150, p!=120.

**Claim:** if the pair admits any plane tiling, it admits a periodic plane
tiling. Reflections, partial contacts, omission of a type, arbitrary positive
side values and coincidences, and every exceptional admitted angle are included.

## Complete necessary metric reduction

The reviewed defect-free hexagon limit and global encoding supply a trivalent
edge-to-edge tiling whose stars are exactly same-colour AAB. Its B cells have
only A neighbours and its A cells have alternating AA/AB neighbours. The
[complete side alphabet ledger](two-hexagon-alternating-metric-ledger.md)
enumerates all203 native A side equality partitions and all39628 necessary
native B words. It uses invariant averaging, not assumed empirical frequencies.

If A has native side period two, the already reviewed metric gate forces B
equilateral and supplies an exact index-three periodic witness. The
[A-side closure stratum filter](two-hexagon-alternating-a-side-strata.md)
excludes137 actual native partitions at every admitted angle. The three
remaining three-value partitions and all270 B words are excluded by
[joint polygon closure](two-hexagon-alternating-three-length-joint-obstruction.md).
The necessary domain remaining at this stage is61 partitions and20970 B words.

Canonicalizing unmarked metric pairs by native colour-preserving D3 on each
polygon, with a single shared class-label permutation, gives685 geometry
orbits. The [exact joint closure reduction](two-hexagon-alternating-joint-metric-orbits.md)
excludes628 universally, retains45 generic-kernel orbits and12 isolated-angle
orbits. None of those exceptions is silently omitted. The local
[six-distinct-side obstruction](two-hexagon-alternating-distinct-a-sides-obstruction.md)
then excludes every six-value A case. This leaves exactly37 necessary
four-/five-value metric orbits, carrying828 original native word cases:
25 generic orbits plus12 isolated-angle orbits.

These reductions are necessary conditions. A positive polygon closure kernel
is never assumed to produce an infinite placement field.

## Direct side-matched native ring domain

For each of the37 metric pairs, let a[0..5],b[0..5] be its actual side-class
labels and let native placements be(r,s), r=0,...,5, s=+1,-1. At native side
slot k use index r+k when s=+1 and r-k-1 when s=-1. At corner slot k use
r+s*k. Equal class labels mean equal actual lengths, and different class
labels denote distinct actual values of A's partition; a class may be absent
from B.

For each of twelve B placements, its corner colours at slots k and k-1
fix the required A neighbour corner colours at slots k+2 and k+3. Filter its
A choices immediately by the actual AB length equality at side slot k+2
against B side slot k-1. Choose one remaining native A symbol for each of six
neighbours, and keep the ring exactly when all six consecutive AA seams match
actual side classes at slots k+1 and k+4. This is the complete local whole-side
domain: no candidate is discarded by angle sampling, no generic angle assumption
is used, and no unconstrained559872-state angle-ring generator is called.

The [producer](../searches/two-hexagon-alternating-residual-metric-transport.py)
and [certificate](../certificates/two-hexagon-alternating-residual-metric-transport.json)
retain every raw full native ring before any intrinsic shape-alias reduction.

## Shape aliases preserve the actual unmarked geometry

For each native placement retain its complete six-slot corner-colour profile
and six-slot actual side-class profile. If two placements have identical
profiles, the ordered boundary angles and lengths in all slots agree. Polygon
reconstruction gives a self-isometry of the fixed convex polygon taking one
native parametrization to the other. Replacing a tile representation by the
least-index such alias does not change its actual placed region, any corner
angle or any matched length. This is permitted because the final polygons
are unmarked.

Canonicalize every A and B symbol by that exact profile equivalence and
deduplicate full rings. Every actual tiling consequently has a legal canonical
representation. This is a full metric-profile identity, not a projection that
forgets lengths or chirality. The certificate retains every alias map and
all twelve full profiles for both species. For all seven eventual positive
cores the A alias map is the identity; the only relevant aliases are two
representations of B's intrinsic mirror symmetry.

## Exhaustive transport and the period gate

Across coarse B direction k, two canonical rings are compatible exactly when
their full native A symbols agree at shared neighbours k,k+1 and k+4,k+3.
Repeated necessary triangle-support deletion gives

| Metric orbit outcome | Count |
|---|---:|
| Empty native core | 30 |
| Six-state native core, all directions functional | 7 |

All twelve exceptional-angle metric orbits have empty cores. The seven
surviving joint geometry IDs are27,78,132,270,322,347,446. Their raw native
ring counts are12 except78 and347, which have24. After intrinsic B mirror
alias canonicalization and pruning, each has six states. The maximum outgoing
degree is1 in **every** one of its six directions.

The seven positive cases also have direct finite certificates, rather than
relying solely on functional periodicity. The
[finite-action producer](../searches/two-hexagon-alternating-residual-periodic-actions.py)
and [seven exact tori](../certificates/two-hexagon-alternating-residual-periodic-actions.json)
check all six successor maps, inverse directions, commutation and the triangular
relation. In fact all six maps are the identity in each surviving core. Choosing
its state0 gives an index-three torus with cell-lattice generators(3,0),(1,1),
HNF(3,1,1), one B cell and two A cells. Native labels at cells(0,0),(1,0),(2,0)
are:

| Joint metric orbit | Native labels |
|---|---|
| 27 | 12,8,4 |
| 78 | 12,4,10 |
| 132 | 12,6,4 |
| 270 | 12,8,4 |
| 322 | 12,8,4 |
| 347 | 12,10,2 |
| 446 | 12,8,4 |

Here0..11 are the twelve native A placements and12..23 the corresponding B
placements, with exactly the side/corner indexing already specified above.
The certificate retains all six vertex stars and eighteen directed seams for
each torus. Every star consists of two A corners and one B corner of the same
colour, hence sums to360 for every admitted p. Every seam matches equal actual
side-class labels. The seam-equivalence closure is checked to be contained in
the supplied metric partition: no extra side equality is imposed. Thus these
are positive witnesses for every actual convex metric in the seven cases,
including its exceptional admitted angles.

The reviewed global encoding/development theorem develops each labelled torus
into a periodic Euclidean tiling by the fixed polygons. The index-three
certificate is combinatorial cell index; the geometric period lattice follows
from that theorem, rather than from treating cell coordinates as Euclidean
coordinates. Independently, the reviewed
[functional-direction period theorem](two-hexagon-one-b-ring-spatial-reduction.md)
shows that any actual canonical field remaining in these cores has a nonzero
period. The direct witnesses suffice for the periodic-escape claim.

The geometric reductions cover every admitted actual metric. Thirty retained
cases cannot have a native field; every other retained case has a periodic
escape by its direct index-three native torus. All earlier excluded metric cases are
untileable or already have the explicit period-two metric witness. This proves
the claim after the indicated fresh finite reviews.
