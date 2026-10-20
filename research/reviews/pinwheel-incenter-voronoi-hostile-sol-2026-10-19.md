# Independent hostile review: fixed incenter Voronoi rule

Verdict: **PASS for the stated finite certificate and conditional exclusion.** No classification or outside-clearance flaw found. This review establishes no infinite-source existence or occurrence theorem.

Reviewed the sibling search `.md`, `.py`, and `.json` named `pinwheel-incenter-voronoi-sol-2026-10-19`, and its imported source geometry in `pinwheel-barycentric-crossboundary-2026-10-19.py`.

## Replay and independent checks

Executed the exact search using the mandated environment:

```sh
mise exec -- conda run --no-capture-output -n arisearch python research/searches/pinwheel-incenter-voronoi-sol-2026-10-19.py
```

It reproduced 125 distinct source sites, 76 retained cells, 49 boundary cells, 20 quadrilaterals, 32 hexagons, 24 heptagons, 11 congruence classes, and 65 clearance-certified cells spanning all 11 classes.

A separate temporary Sage audit reconstructed the three subdivision rounds and checked all 125 source triangles have squared short leg 1/125 and squared long leg 4/125. All are contained in T; the exact sum of absolute areas is 1, and every triangle pair has separating projections on some triangle edge normal. Thus interiors are disjoint and these triangles cover T. The five displayed children and similarity normalization agree with the standard 1:2 right-triangle pinwheel dissection used by this source. I did not infer substitution-language membership of an infinite tiling from the finite partition.

The independent audit computed each incenter using side-length vertex weights `(sqrt(5) O + L + 2 S)/(sqrt(5)+3)`. These exactly matched every retained JSON site and the formula in the search. The coefficients are valid for reflected triangles as well: the local right vertex and unequal leg lengths determine the frame intrinsically.

For every retained polygon, the audit checked every vertex against all 125 site inequalities and strictly against all three boundary sides. Every polygon edge lies on an actual site bisector. Together with the replayed positive-turn check, these conditions certify equality with the full finite Voronoi cell: the polygon is feasible, and all its supporting edge halfplanes belong to the defining system. No hidden enlargement or clipping artifact survives this check.

## Congruence and clipping

The canonical signature contains all labeled pair distances and minimizes over the dihedral vertex orderings. A Euclidean isometry between strict convex polygons preserves or reverses cyclic vertex order, so this gives a complete congruence invariant including reflections. Different polygons cannot collapse into the same signature through omitted diagonal information.

As an independent check, I compared every pair of the 76 polygons by direct rigid coordinates. For each candidate cyclic/reversed correspondence with equal first-edge length, I compared all vertex projections and cross products relative to that edge, allowing sign reversal of the perpendicular coordinate. This test agreed with the reported class equality for every pair, without invoking the search signature implementation.

The clipping routine includes vertices on a halfplane and inserts crossings only for strict sign changes. Endpoint intersections are already retained by the inclusion case; this does not omit boundary points. Removing duplicate and collinear vertices is appropriate here. The interior criterion is exact: because all clipped vertices lie inside the convex triangle, touching any supporting line is equivalent to touching its corresponding triangle side. A full Voronoi cell that crosses the boundary cannot have its clipped intersection strictly inside T, by convexity and the fact that its site is inside T.

## Outside-source certificate

Independently recomputed the exact minimum over all vertex/side pairs of

`cross(b-a,v-a)^2 / |b-a|^2 - |v-p|^2`.

Its strict positivity agreed with every reported clearance flag. Exactly 65 cells passed, with every one of the 11 classes represented. Site 31 supplies a passing quadrilateral.

The proof extending vertex inequalities to each whole cell is valid. Within T the signed distance to a supporting line is positive affine, and `|x-p| - d_line(x)` is convex. Strict negativity at the finite set of polygon vertices implies strict negativity on their convex hull. The distance to the complement of a triangle is the minimum distance to its supporting lines. Consequently every point of a passing cell is closer to its own site than to any site outside T, including a boundary site. Additional outside sites cannot shrink a passing cell; adding inequalities cannot enlarge it either. The nonpassing cells are simply uncertified by this sufficient test, not proven unstable.

## Scope

The fixed unweighted incenter rule fails the proposed two-class gate on this exact patch: all eleven classes have witnesses immune to arbitrary outside additions, and a quadrilateral witness persists. For an infinite triangular tiling containing this exact complete tile patch, all other triangle incenters lie outside T, so these witnesses persist conditionally. The finite audit proves neither that such a global tiling exists nor that every pinwheel source contains this patch. It does not assess weights, other site choices, or other dualizations.

No Git or discovery-log changes were made. The replay regenerated its existing JSON artifact; this review is the only new repository file authored by this reviewer.
