# One-chirality Hat sites: both fixed ordinary Voronoi rules excluded

2026-10-19. **Exact finite witness obstruction, independently Sol-reviewed PASS**; see [review](../reviews/hat-single-chirality-sol-hostile-2026-10-19.md).
This implements priority 2 of `progress-assessment-2026-10-19-1852.md`.
Keep only one determinant sign of the genuine Hat site set at the fixed
intrinsic site p0=(5/8,5sqrt(3)/8), and take ordinary Voronoi cells.
Each sign separately forces at least three incongruent cells. No weights,
site displacement, or enlarged patch search is used.

## Source and uniform covering proof before dualizing

Use retained `source-decoration-hat-patch.py` and the primary viewer source
and provenance retained for the reviewed
[existence gate](hat-voronoi-existence-gate-2026-10-19.md).
The imported theorem input is existence of infinite Hat tilings carrying
this genuine H/T/P/F hierarchy and occurrence of the expanded genuine
supertile patches. The discarded overlapping construction patch is never
used as a tiling. As before, generated coordinates are multiplied by two
so that Hats have the full native `hat_outline` size.

The finite occurrence table is established before any Voronoi calculation:

| Level-one type | Positive frame sites | Negative frame sites |
|---|---:|---:|
| H | 22 | 3 |
| T | 3 | 1 |
| P | 12 | 2 |
| F | 14 | 2 |

For a reflected parent the two columns interchange. The certificate
explicitly enumerates both parent determinant signs and both retained
signs. Rotations and translations preserve these counts and distances.
Thus every legal level-one parent contains both chirality choices, also
under reflected placements; relative density is not inferred from a patch.

For each constituent Hat in each level-one parent and each retained sign,
the script selects ONE retained site in that same parent. It computes
exactly over Q(sqrt(3)) the maximum squared distance from that fixed site
to all thirteen vertices of that Hat and verifies it is strictly below
100. The certificate records every assignment and bound. Since the radius
10 disk is convex, it contains the entire convex hull of those vertices,
and hence that entire possibly concave Hat. This is a uniform finite ball
cover of the actual parent cluster, not a vertex-wise nearest-site claim.
Every plane point belongs to a Hat in one of these level-one clusters.
Consequently either retained site set has the global covering radius R=10.
The argument handles reflected parents by isometry, with sign reversal.

Uniform separation is inherited from the full site set: the already
reviewed positive separation lower bound 15/16 applies at p0, and deleting
sites cannot decrease it. Therefore either retained site set is Delone;
its ordinary Voronoi cells form a plane tiling by bounded convex polygons.
Every such cell lies in its closed radius-10 site disk. A site farther
than 2R=20 cannot cut this disk, by the triangle inequality. This supplies
the exact justified neighbor cutoff before examining cell shapes.

## Genuine source neighborhoods and exact cell verification

The source is the same depth-three genuine H supertile with 1,156 Hats.
Every actual Hat is decomposed into eight primitive kites. Exact checks
place all kites on one common grid, verify their standard sector shapes,
exclude repeated kite interiors, and bound edge multiplicities by two.
Cancelling matching primitive edges gives every exposed boundary segment,
including any hole boundary. No idealized metatile outline is used.

Each target site is interior to its own Hat. Its exact squared distance
to every exposed boundary segment is greater than 400. Hence its entire
closed radius-20 disk lies in the union of actual source Hats: otherwise
a segment from the center to an uncovered point would cross an exposed
boundary. Any omitted source site's intrinsic point is interior to its
own omitted Hat and therefore cannot be inside this covered disk.
The retained source sites at squared distance at most 400 are consequently
the complete list relevant to the infinite-source cell.

SciPy only proposes a cyclic facet order. Every bisector intersection is
then reconstructed exactly over Q(sqrt(3)); every retained neighbor
halfplane is checked, incident equalities are checked, every vertex has
squared radius strictly below 100, and every consecutive exact corner
has positive cross product. Thus all recorded sides are nonzero intrinsic
sides and the cycle is strictly convex. The halfplane inequalities are
2(s_j-s_i) dot z <= |s_j-s_i|^2 in site-relative coordinates.
Completeness and the vertex radius bound show that omitted sites cannot
trim these exact polygons. Areas use the exact shoelace formula.

## Cheapest resulting obstruction

| Retained determinant | Hat index | Sides | Area / sqrt(3) |
|---|---:|---:|---|
| -1 | 510 | 6 | 4233954347/81711360 |
| -1 | 518 | 6 | 596323597/9467064 |
| -1 | 514 | 6 | 99383642899633/1726465308288 |
| +1 | 519 | 5 | 23484642059/3199878312 |
| +1 | 508 | 7 | 1359041891/158138064 |
| +1 | 516 | 7 | 3064090381/282983904 |

Within each sign these are three pairwise incongruent cells: unequal
areas distinguish the three negative-sign hexagons; side counts separate
the positive-sign pentagon from the two heptagons, whose areas differ.
Congruence with reflection also preserves area and intrinsic side count.
Thus both fixed rules fail the two-class gate. The gate stops after these
witnesses, without a global palette census, omission classification, or
intrinsic decoder. Source aperiodicity is never transferred to arbitrary
output tilings. This restricted construction failure does not settle the
main research problem.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hat-single-chirality-voronoi-gate-2026-10-19.py

The script is both producer and exact replay verifier. Certificate:
`research/certificates/hat-single-chirality-voronoi-gate-2026-10-19.json`.
It includes the full oriented occurrence table, individual covering
assignments, genuine source frames, complete neighbor lists, exact
vertices, exact areas, and boundary clearance witnesses. The independent
checker in the linked review reconstructs all six cells without importing
the producer or using SciPy. No novelty claim is made. Under protocol
section 5 this fixed rule is closed; reopening requires a materially new
construction or invariant. Section 19 continues the wider programme.
