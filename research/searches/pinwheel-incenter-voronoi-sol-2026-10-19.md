# Exact incenter Voronoi gate on the fixed pinwheel patch

Status: **finite exact exclusion of this fixed unweighted site rule**. Not independently hostile-reviewed. The unrestricted two-convex-polygon problem remains unresolved. Stop this rule: there are eleven intrinsic congruence classes, and a complete quadrilateral class. No symbolic weight, parameter scan, numerical sampling, or larger patch was attempted.

## Exact source and site rule

Start with T=((0,0),(2,0),(0,1)). Use the five inflated triangles

((0,0),(2,0),(2,1)), ((2,0),(4,0),(4,1)),
((4,0),(5,0),(4,2)), ((2,1),(4,1),(4,2)),
((2,0),(4,1),(2,1)).

Apply N(x,y)=(2-(2x+y)/5,(x-2y)/5). For each parent identify its right vertex O, long-leg endpoint L, and short-leg endpoint S, and transport normalized children by (x,y) -> O+x(L-O)/2+y(S-O). Exactly three rounds give the established 125-triangle patch, all with rational coordinates. The script imports only these existing geometry functions; it does not import the earlier corner-star cells or seam decisions.

Put r=sqrt(5)>0. The single site of each triangle is its Euclidean incenter

c=O+(3-r)(L-O)/4+(3-r)(S-O)/2.

The rule commutes with every isometry, including reflection. All calculations are in the exactly ordered Sage number field Q(r), r²=5, with its positive real embedding. All 125 sites are distinct. This is a site-based Voronoi construction, distinct from the excluded center/seam corner-star recompositions: cell vertices here are intersections of actual perpendicular bisectors, with no prescribed source seam crossings.

For each site p, form V_p={x:2(q-p)·x<=|q|²-|p|² for every other site q}. The script clips T against all 124 inequalities and rejects a clipped polygon if it touches any side of T. Thus the retained list comprises exactly the full finite-site Voronoi cells contained strictly inside T; cells crossing or touching its boundary are outside this census. It removes every redundant collinear boundary vertex and verifies positive turns at every genuine vertex.

## Complete finite census

There are 76 fully interior cells and 49 boundary-touching clipped cells. All 76 are strictly convex. Their genuine side counts are 20 quadrilaterals, 32 hexagons, and 24 heptagons. There are eleven congruence classes under translations, rotations, and reflections:

| Class | Genuine sides | Multiplicity | Outside-complete witness site index |
| --- | --- | --- | --- |
| 0 | 4 | 20 | 31 |
| 1 | 6 | 5 | 7 |
| 2 | 6 | 7 | 10 |
| 3 | 7 | 7 | 14 |
| 4 | 7 | 7 | 18 |
| 5 | 6 | 8 | 20 |
| 6 | 7 | 8 | 24 |
| 7 | 6 | 4 | 28 |
| 8 | 6 | 5 | 37 |
| 9 | 7 | 2 | 47 |
| 10 | 6 | 3 | 73 |

For a cyclic polygon, the canonical signature is the lexicographically least full list of pairwise squared vertex distances over every cyclic starting point and both traversal directions. Full distances determine a finite point configuration up to Euclidean isometry; an isometry of strict convex polygons induces one of precisely these cyclic/reversed correspondences. Hence signature equality is equivalent to intrinsic congruence, including reflections. No numerical tolerance or edge-length-only heuristic is used.

## Completeness against sites outside the source triangle

Finite-site cells alone need not persist in a plane source. Here a stronger exact certificate is available: 65 of the 76 retained cells, representing **all eleven classes**, pass an outside-source clearance test.

For every cell vertex v of a site p and every oriented boundary edge ab of T, the certificate verifies

cross(b-a,v-a)² > |b-a|² |v-p|².

All v lie strictly inside T, so this says |v-p| is strictly less than the distance from v to each boundary supporting line. For each such line, the function |x-p|-d_line(x), with d_line the positive affine signed distance, is convex. Its strict negativity at all polygon vertices implies negativity throughout the polygon. Consequently |x-p|<dist(x,complement(T)) for all x in the cell. Any additional site q outside T is therefore farther from x than p. Such sites cannot change that cell. The finite Voronoi inequalities already exclude every other inside site. Thus every passing cell is unchanged by **any** set of sites outside T, without a tail estimate or additional patch.

In particular, any infinite triangle source containing this exact patch as a tile patch has its remaining incenters outside T, and therefore contains all eleven certified classes. This implication is conditional on occurrence of the patch; no infinite-source extension or recognizability is assumed or proved. The eleven certified persistent classes already kill this rule for the two-class gate. The quadrilateral is an additional failure of the >=5-side requirement; no periodicity theorem is needed for the exclusion.

For example site 31 is p=((27-r)/50,(19+3r)/50), from triangle ((16/25,12/25),(12/25,14/25),(11/25,12/25)). Its four vertices, in positive cyclic order, are

((95+r)/200,(55+r)/100),
((20+r)/50,(10+r)/25),
((17+4r)/50,(43+r)/100),
((25r-28)/50,(5r+14)/50).

This cell passes strict outside clearance. The JSON retains all 76 exact cells, all full-distance signatures, source triangle coordinates, and witness flags.

## Replay and scope

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pinwheel-incenter-voronoi-sol-2026-10-19.py

Artifacts: sibling `.py` and `.json` files. Sage is imported from the locked Python environment; the CLI in this environment does not accept `sage -python`, so replay uses Python directly. No git or discovery-log edits were made. This is a bounded first gate, not a classification of all pinwheel dualizations or power diagrams. A handedness-dependent power weight would change the rule and requires a separately justified construction mechanism; it was not used to rescue an already failed fixed gate. Under protocol §§5 and 19, close this fixed rule and move to a genuinely different mechanism.
