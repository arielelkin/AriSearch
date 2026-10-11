# Independent re-review: defect-free limit for two convex hexagons

**Date:** 2026-10-09. **Verdict:** valid after the October 9 uniform
sector-disk strengthening. This re-review covers the defect-free limit
claim, not all other claims in its shared source file.

## Exact claim and independence

[The source theorem](../lemmas/hexagon-limit-and-periodicity.md), under
"Defect-free limit for two hexagons", states that every tileable pair of
fixed genuine compact convex hexagons admits an edge-to-edge,
everywhere-trivalent plane tiling, possibly omitting one type. Root authored
the October 9 strengthening. This reviewer did not write that repair and
independently checked the full proof and the uniform separation step.
No monohedral hexagon classification is needed for this theorem.

## Earlier defect and precise repair

The previous final compactness paragraph relied on the sentence that a
positive minimum side length prevents vertex coalescence. That sentence
alone did not explain why *nonadjacent* native vertices stay separated or
why new vertex-to-side contacts cannot appear in a limit. It was a proof
exposition gap, not an established counterexample to the theorem.

The replacement chooses r>0 smaller than every prototile vertex's distance
to every other vertex and to every nonincident native side. These distances
are positive for a finite set of fixed genuine convex polygons. At a clean
edge-to-edge vertex, each incident tile fills exactly its corner sector
inside B(v,r). The three sectors cover the disk. Any other native vertex
there would lie either in a tile interior, contradicting disjoint interiors,
or on a native side ray. The latter possibility contradicts full-edge
matching and the choice of r. Thus r uniformly separates all native vertices
in clean interior patches, even nonadjacent ones.

## Adversarial checks of the whole proof

1. Local finiteness and bounded incidence follow from the finite positive
   minimum tile area and bounded diameters. Tiles touching any fixed tile
   lie in a uniformly bounded region, so contact subdivisions per tile
   are uniformly bounded.
2. The selected-window planar graph has exact face-side incidence
   2E=6N+delta+B. Euler's formula with H holes and degree counting give
   delta+2Dv=6Vb-2q-B-6+6H. Recomputing the algebra yields exactly the
   displayed identity. Delta and Dv are nonnegative. The uniform boundary
   estimates therefore bound both by O(R); no cancellation of positive
   defects is assumed.
3. Every interior vertex-to-side contact contributes a native-side
   subdivision, and every interior valence greater than three contributes
   at least one to Dv. Hence the number of actual defect locations is O(R).
   Boundary subdivisions and holes are covered by the boundary estimates,
   rather than silently discarded.
4. For fixed L, separated radius-L candidate disks inside the selected
   square have quadratic-in-R count. Each defect excludes only a uniformly
   bounded number of candidates. Taking R sufficiently large compared with
   (L+D)^2 gives a defect-free disk, with a boundary margin for every tile
   meeting its inner window. Arbitrary large clean patches arise in one
   actual tiling, not as unrelated independently solved finite instances.
5. After translating clean disks to the origin and taking L to infinity,
   compactness of locally finite tile placements gives a plane tiling.
   A gap or an interior overlap would persist in nearby configurations and
   is therefore impossible. Tile types are not rescaled, deformed, or
   restricted in orientation.
6. Uniform separation prevents native vertices from merging in every fixed
   clean limit window. A limit native corner is the limit of that fixed
   corner slot in an approximating tile occurrence. Its finite three-tile
   star can be frozen on a subsequence. Native full-side endpoint equalities
   and the three incident corner sectors pass to the limit. An additional
   tile with an interior sector at this point would overlap the disk already
   covered by those sectors. Thus no T-junction or higher-valence vertex can
   be created at the compactness step.
7. All clean native sides have full-edge neighbours; freezing the finite
   neighbour slots passes their full-segment matches to the limit. Every
   limit vertex has exactly three genuine corners. The conclusion is
   therefore the claimed unrestricted edge-to-edge trivalent tiling,
   although one prototile type can disappear.

## Repairs, remaining uncertainty, and scope

The root's strengthening resolves the compactness exposition gap. This
review found no remaining defect in the defect-free limit proof. It does
not prove periodicity, force both types to remain, classify hexagons, or
extend the result to pentagon-containing pairs. The higher-side exclusion
and conditional deterministic-state claims in the shared source retain
whatever separate review status their own records state.

**Final verdict:** valid for the exact theorem above; the repaired
compactness step has now received an independent hostile re-review.
