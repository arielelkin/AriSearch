# Periodic tiling for the isolated AAABBABB octagon

**Theorem (single exact pair).** Put `w=exp(2*pi*i/20)` and `L=2cos(18°)=-w^7+w^5-w^3+2w`. Let `P` be the regular unit pentagon with vertices `p_i=sum_{j<i}w^(4j)`, `i=0,...,4`. Let `Q` be the convex octagon starting at 0 with consecutive edge vectors `l_i w^(e_i)`, where

`(e_0,...,e_7)=(0,2,4,7,10,12,15,18)`,

`l_3=l_6=L` and all other `l_i=1`.

Then `Q` closes, has interior-angle word `AAABBABB` with `A=144°` and `B=126°`, and `{P,Q}` admits a doubly periodic tiling of the Euclidean plane. The unmarked pair is therefore **not aperiodic** under the [research problem](../../research-problem.md). This theorem concerns this one exact pair, not arbitrary P/Q shapes.

## Four-pentagon / two-octagon carrier

Use six direct placements, listing each as `rT+c` for native polygon `T`:

| Face | T | r | c |
|---|---|---|---|
| P0 | P | `w^6` | `0` |
| P1 | P | `w^8` | `w^4+1` |
| P2 | P | `w^16` | `2w^6-w^4-2` |
| P3 | P | `w^18` | `w^6+w^2` |
| Q0 | Q | `1` | `w^6-1` |
| Q1 | Q | `-1` | `w^6-w^4-1` |

Let the lattice generators be

`L1=w^6-2w^4-w^2-3`, `L2=-3w^6-2w^2+2`.

The [exact certificate](../searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.json) lists all eighteen opposed edge pairs, their integer shifts in this lattice, and all twelve trivalent vertex links. The [producer replay](../searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.sage) verifies both endpoint equations for each pair. The [independent hostile checker](../reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.sage) reconstructs the six polygons and discovers all eighteen unique lattice mates independently of the producer pairing table. Thus every boundary edge is glued once, with coincident whole segments and opposite face sectors. The links are all single three-corner cycles, each of types `P,P,A` or `P,B,B`, so every vertex has total angle 360°.

The exact oriented lattice area is

`cross(L1,L2)=-13w^7+8w^5-3w^3+16w>0`.

Exact shoelace arithmetic gives this same number as `4 area(P)+2 area(Q)`. The polygons are strictly convex: P is regular, and the Q supporting-half-plane checks use exact cyclotomic arithmetic. The independent checker also rules out all 36 possible nonidentity ordered translate intersections by exact polyhedron tests, but the following topological argument already proves global coverage and nonoverlap.

Glue the six closed face disks along their eighteen orientation-reversed edge pairs. The face adjacency graph is connected; every vertex link is one complete 360° cycle. The resulting compact oriented surface has 6 faces, 18 edges and 12 vertices, hence Euler characteristic zero and a flat Euclidean chart at every point. The edge-shift identities define a continuous facewise local isometry from this surface to the lattice torus `R²/(ZL1+ZL2)`. At a paired edge the sectors lie on opposite sides, and around each vertex the cyclic positive sectors make exactly one full turn; thus the map is a local homeomorphism even at boundaries and vertices. Compactness makes it a finite surjective covering of the connected target torus. Its degree is total face area divided by lattice covolume, exactly one. It is therefore a homeomorphism. Lifting the faces gives a covering of the whole plane with pairwise disjoint interiors and periods `L1,L2`.

The other retained carrier encoding uses a reflected native index order for the second Q. It describes the same geometric Q1 polygon: the [hostile review](../reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.md) verifies the exact Q reflection symmetry. The displayed direct placement already suffices for the theorem; no reflection restriction is imposed on admitted tilings.

## Reproduction and limits

Replay from repository root in SageMath 10.9:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.sage
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.sage
```

The [self-contained search report](../searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.md) derives this 4P+2Q inventory after the reviewed one-Q obstruction, treats both Q parities, and stops there. The [independent Sol hostile review](../reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.md) is **PASS** for the whole-plane periodic witness. All geometry is exact in `Q(w)`; there is no solver, numerical tolerance, random seed or cutoff in the positive proof. The original unrestricted two-convex-polygon objective remains unresolved.
