# Strictly obtuse convex atoms admit no nontrivial convex fusion

Date: 2026-10-19. Status: proved and [independently Sol-reviewed](../reviews/strictly-obtuse-convex-fusion-sol-review-2026-10-19.md). The review identified an initial loose `covers K` hypothesis, repaired below to `union exactly K`.
This is a restricted construction obstruction, not a solution of the two-tile problem. No novelty or priority claim is made.

## Theorem

Let K be a compact convex polygon with nonempty interior. Suppose a finite collection C1,...,CN of compact convex polygons with nonempty interiors has union exactly K and has pairwise disjoint interiors. If every genuine interior angle of every Ci is strictly greater than pi/2, then N=1.

The pieces may differ arbitrarily, and their contacts need not be edge-to-edge. No tiling of the whole plane is assumed. Genuine vertices exclude artificial collinear subdivision vertices.

## Proof

Subdivide the boundary of K at its vertices and at every point on it which is a vertex of any Ci. There are finitely many resulting open boundary intervals. Each interval belongs to exactly one piece on its interior side: two different pieces occupying that side would overlap in positive area. This label is constant on the interval. Every boundary interval has such a label because the pieces cover K.

If all intervals have the same label i, closedness gives boundary(K) contained in Ci. Convexity gives K=conv(boundary(K)) contained in Ci, so Ci=K. Disjoint positive-area interiors then exclude every other piece.

Otherwise, two consecutive boundary intervals have different labels i,j. Let x be their common endpoint. Both Ci and Cj contain x. At x, each piece has a positive angular sector: it is a genuine corner sector, of angle strictly greater than pi/2, or x lies in the relative interior of one of its sides and its sector has angle pi. These sectors have disjoint interiors, lie inside the sector of K, and therefore have total angle at most pi. But their sum is strictly greater than pi. This contradiction proves the theorem.

This also handles an outer vertex of K: its containing sector has angle less than pi. A T-junction is not excluded by convention; if one piece meets x in the middle of its side, its pi sector only strengthens the contradiction. Extra pieces meeting only at x cannot remove the two sectors already used.

## Applied construction obstruction

In any plane tiling whose tiles are strictly obtuse convex polygons, a finite union of whole tiles is convex only when it consists of one tile. Consequently a construction which starts with such a source tiling and replaces finite clusters of whole source tiles by convex prototiles cannot fuse any source tiles at all. In particular it cannot reduce three or more distinct source congruence classes to two by whole-tile convex fusions.

This quantifies over every finite cluster, with no cluster-size cutoff. It does not exclude partitions which cut through source tiles, source tiles having a right or acute angle, or arbitrary constructions of two convex polygons.

## Hostile checks and source boundary

The strict threshold is necessary: two unit squares form a convex 2-by-1 rectangle. Partial-side contacts and boundary vertex transitions are included in the proof, rather than suppressed by an edge-to-edge assumption. Pieces meeting the outer boundary only at isolated points do not affect the positive boundary-interval labels.

The reconstructed Sugimoto Method 3 source has angles as small as 75 degrees and right angles, so this theorem does not apply to that source; its separate source-specific saturation result remains necessary. Penrose rhombs and Robinson triangles also have acute corners. No assertion is made that a presently retained aperiodic source satisfies this theorem. The result prunes the general all-obtuse whole-cell-fusion mechanism, not those source families.

## Dependencies and computation

Only elementary convexity and the finiteness of a polygonal dissection are used. There is no enumeration, solver, coordinate fixture, or numerical dependency. The finite dissection hypothesis is essential to the stated boundary-label argument; no claim about arbitrary infinite dissections is made.
