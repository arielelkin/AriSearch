# Exact Hat four-spoke junction obstruction

Date: 2026-10-19. Status: independently Sol-reviewed within its stated topology.
[Hostile review](../reviews/hat-four-spoke-junction-sol-hostile-review-2026-10-19.md).

## Domain and result

Fix the reviewed 13-vertex Hat outline from
`research/certificates/hat-eight-kite-convex-cluster-gate.json`. Introduce one
interior point O and four straight spokes from O to all four reflex vertices,
indices 0,4,8,11. Require a partition into four convex polygons. There is
**no dissection in this topology whose four pieces all have five or six
genuine sides**, over any real coordinate field. Consequently there is no
requested two-class cover with both classes present, even allowing reflections.

A stronger target-specific obstruction applies: one piece has at most four
sides. Every nondegenerate convex triangle or quadrilateral admits a periodic
monohedral plane tiling. Its congruence class alone therefore defeats the
original problem's aperiodicity quantifier, irrespective of the other pieces.
For a quadrilateral, halfturn copies across side midpoints give the standard
periodic quadrilateral tiling; opposite side-pair compositions yield nonzero
translation vectors. Triangles pair into parallelograms.

## Coordinates and exact convexity regions

Write each source vertex as (X/2,sqrt(3)Y/2), and similarly
O=(u/2,sqrt(3)v/2). The integer (X,Y) list is

```
(0,0),(-3,-1),(-2,-2),(2,-2),(3,-1),(6,-2),(9,-1),
(8,0),(6,0),(6,2),(3,3),(2,2),(0,2).
```

This positive linear coordinate transformation preserves turns, convexity,
and incidences. The four faces have the following counterclockwise vertex
words. A row gives the determinant at each vertex in that word, in order.
Its nonnegative inequalities give the closed convexity region for that face;
strict inequalities give its full side-count region.

| Face word | Turns | Maximum genuine sides |
| --- | --- | --- |
| 0,1,2,3,4,O | u-3v,4,4,4,-u+v+4,u+3v | 6 |
| 4,5,6,7,8,O | u+3v,6,4,2,-2v,-u+3v+6 | 6 |
| 8,9,10,11,O | 12-2u,6,4,u-v,-2u-4v+12 | 5 |
| 11,12,0,O | 4-2v,4,2u,2u-2v | 4 |

In the common feasible region, the genuine count for a face equals the
number of its strictly positive listed turns: zero turns remove collinear
subdivision vertices. Nondegeneracy is implicit throughout.

The common closed region is exactly

```
v <= 0,  u >= -3v,  u <= v+4,
```

a triangle with vertices (0,0),(4,0),(3,-1). Necessity follows from the
second face's fifth turn, its first turn, and the first face's fifth turn.
These imply -1<=v<=0. Sufficiency follows by evaluating each affine turn
at the three vertices of this triangle; all values are nonnegative.
The source points (0,0) and (3,-1) are excluded by the interior-junction
hypothesis. The remaining triangle is inside the source visibility kernel:
each original oriented boundary-edge halfplane contains it, as also follows
from the endpoint turn rows and the positive fixed boundary turns. Thus all
spokes are contained in the Hat and the indicated cyclic faces are the
actual partition faces. Boundary cases can only reduce side counts.

## Short certificate and scope

There are precisely two original boundary edges from vertex 11 to vertex 0,
through vertex 12. The face on this arc is necessarily
[11,12,0,O]. Two spokes close it, giving at most four genuine sides.
An interior Steiner junction does not add another corner to this face.
This elementary count already excludes the topology without using the
convexity-region calculation, congruence equations, numerical sampling, or
any restriction to Q(sqrt(3)). It covers arbitrary real O, hence algebraic
extensions as well. There is no candidate for a source-existence or decoder
audit. This does not exclude other dissection topologies or resolve the
main two-convex-tile problem. Do not enlarge the junction count or grid on
the basis of this result.

## Replay

No enumeration or solver is used. The finite checker checks the fixed 13
coordinates, four reflex indices, four symbolic determinant rows, affine
inequalities at three triangle vertices, and side counts. Dependencies are
Python standard library and environment-pinned SymPy. No randomness or timeout.

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/check-hat-four-spoke-junction.py
```
