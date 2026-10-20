# Intrinsic Penrose vertex-site dual: three-class obstruction

Status: exact bounded exclusion of one changed site rule; not independently reviewed.

## Rule and source

Take the unit-edge thick/thin Penrose rhomb source used in the retained
`penrose-center-voronoi-quadrilateral-2026-10-19.py` source generator. Place
one site at each distinct geometric source vertex, with zero weights, and
form ordinary Voronoi cells. Shared vertices contribute one site, not one
site per incident rhomb. This is intrinsic under every source isometry and
uses no tile labels, source means, chirality selection, or whole-cell fusion.
The output cells are bounded convex polygons: the source has finite local
complexity and separated vertices, and every point in a unit rhomb lies
within distance less than 2 of one of its vertices. This gives a covering
radius 2, without asserting a two-shape output.

The exact source field is Q(zeta_10), with the specified embedding
zeta_10=exp(2*pi*i/10). The imported generator builds five deflations of the
Robinson sun and pairs compatible triangles into 430 complete unit rhombs.
Its exact checks establish the unit edges, paired interiors, exposed
boundary and containment of its level-one seed. The source occurrence and
infinite extension have the same primary recurrence dependency and scope
as the retained reviewed Penrose-center gate. No new source-extension
claim is inferred from finite growth.

## Finite question and result

Question: does this fixed dual rule already exhibit three incongruent cells
in the retained actual source neighborhood? The domain consists of the 476
distinct vertices of those 430 rhombs. Deterministically order vertices by
their rational cyclotomic coefficient vectors. SciPy proposes the first
three distinct side counts among sites of distance at most 3 from the
origin. Floating computation only proposes witnesses.

For each proposed site c, the script exactly clips its relative plane by
all inequalities 2(q-c) dot x <= |q-c|^2 from patch sites q within distance
3. The initial rectangle has vertices (+/-2)+i sin(36 degrees)(+/-2).
After removing collinear subdivisions it checks every turn is positive,
every vertex satisfies all retained inequalities, and every radius is
strictly less than 1. The resulting polygons have respectively **5, 6 and
7 genuine sides**. Isometries including reflections preserve side count,
so these are three congruence classes.

The squared distances of the three sites to the actual rhomb-union
boundary are respectively 49+30(zeta^2-zeta^3),
40+23(zeta^2-zeta^3), and 43+26(zeta^2-zeta^3), all strictly greater than 9.
An exterior source vertex cannot lie inside that source union: its incident
positive-angle source tiles would overlap the patch interiors. Thus every
omitted vertex is at least distance 3 from c. Likewise every retained but
unprocessed vertex is farther than 3. Since the exact cells lie strictly
inside radius 1, none of these omitted sites can cut them, by the triangle
inequality. The three witnesses therefore persist in any source completion.
The cutoff is a local witness certificate; no infinite neighbor census is
needed.

The fixed rule fails the two-class gate. A periodic omission search is
unnecessary after this failure and was not performed. No output decoder,
full congruence census, shape-only aperiodicity, or impossibility result for
other site rules is claimed. Stop this fixed rule under protocol section 5.

## Replay

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-vertex-dual-gate-sol-2026-10-19.py --check
```

Producer and verifier are the same narrow script. It reads only the source
prefix (before its center-site construction) of the retained Penrose-center
script; it does not execute that script's output-writing portion. Exact
witnesses and coefficient vectors are retained in the adjacent JSON file.
No solver, random seed, symmetry reduction, or timeout was used. The
computation completed. Sage exact field arithmetic and real algebraic
comparison discharge the final claims; SciPy only selects witness indices.
The environment versions are retained below by the producer's environment
record. No novelty claim is made.

Environment: Python 3.12.13, SageMath 10.9, SciPy 1.18.0.
