# Independent hostile review: resonant purification and periodic carrier

Date: 2026-10-19. Verdict: **PASS for the stated implication: tileability implies existence of a tiling with a nonzero translation.** Independently reviewed `research/searches/resonance-purification-sol-2026-10-19.md` against the already reviewed complementary-angle necessary theorem. No counterexample or substantive gap found. This review certifies neither existence for a particular metric Q nor periodicity of the original, possibly defective tiling.

## Purification

Both defect types really are nonnegative integers. The heptagon has one AA side, every such side faces P, and the pentagon has capacity at most one; hence AA incidence counting and p=q+O(R+1) yield the pentagon deficit bound. The independent resonant gate supplies t in {1,3} and total t=3q+O(R+1), giving the other bound. There is no cancellation between positive and negative defects.

The disk-avoidance argument is valid: for each fixed L the excluded area grows at most linearly in R, while eligible centers have quadratic area. Anchors outside the enlarged window cannot contribute a tile meeting the desired disk. Taking R after L produces arbitrarily large completely defect-free neighborhoods. Compactness uses fixed shapes, bounded diameter and positive minimum area, and permits reflected placements. Incidences can be included in diagonal extraction; fixed positive side lengths prevent the selected full-edge neighbors disappearing or collapsing. Thus every limit tile has its complete, defect-free neighborhood. This avoids the invalid inference that boundary-order many defects means no defects in the original tiling.

## Anchors and chain geometry

A saturated Q has precisely the three asserted PQ edges. At its A corners the stars are PPA. Each P receives exactly one AA edge, so pairing along AA is a genuine bijection. A Q cannot be assigned to two P tiles, and no Q is omitted. The remaining two PQ edges of that Q lead to the PP neighbors of its paired pentagon, by the actual three-tile stars at the two A corners. Thus the three-P/three-Q carrier incidence is forced, rather than an assumed continuation.

The opposite-endpoint argument across PP is sound. If both pentagons selected the same physical endpoint, the single Q there would have two distinct edges both serving as its AA edge. They cannot coincide since they are the two rays of its strictly convex A corner. At most one selection at an endpoint therefore forces opposite selections. This argument does not distinguish orientation-preserving from orientation-reversing copies.

I independently checked the turns in coordinates. Take one pentagon's incoming and outgoing PP normals as 144 and 0 degrees, with AA normal 72 degrees. The next pentagon has shared normal 180, AA normal 252, and outgoing normal 324 degrees. The following pentagon has shared normal 144, AA normal 72, and outgoing normal 0 degrees. Thus traversal directions alternate 0,324,0,324 degrees, with turns -36,+36. Reflecting reverses both signs. The two-step center displacement has length 4r cos(18 degrees), and also preserves the distinguished AA side.

No finite PP cycle is possible: the locally propagated center displacements alternate two fixed vectors whose sum is nonzero. A cycle would sum a positive multiple of that sum to zero; an odd cycle would additionally violate the alternating turns. Distinct pentagons cannot share two different full edges: disjoint convex interiors preclude two noncollinear common boundary segments. Thus the degree-two graph components are actual doubly infinite chains. The alternating vectors have positive projection on their sum, so each center path is an embedded proper graph over its axis.

## Q placement and reflections

The possible concern is an independent binary Q decoration on each pentagon. This concern is resolved by the PBC stars. A prescribed AA segment and half-plane admit at most two isometric placements of the fixed Q, according to the assignment of its two A endpoints. The other two PQ sides are forced rays and have unit lengths, since they face unit pentagon sides. Their outer endpoints therefore coincide geometrically for the two choices, with labels B and C interchanged. Those labels have unequal angles, so specifying one fixes the entire Q placement.

For each index j, let F_j be the label on Q_j's flanking edge toward P_(j+1), and H_j its label toward P_(j-1). Each Q has exactly one B and one C at those endpoints, so H_j is the complement of F_j under every reflection choice. At the sole PBC corner of P_n the incident Q labels are F_(n-1) and H_(n+1); they must be complements. Consequently F_(n-1)=F_(n+1). This holds for all four binary choices and is independent of the chirality of the tiles. Two-step translation preserves the forward AA endpoint geometry, so it preserves the selected full Q placement. There is no unproved control of the remaining QQ edges in this deduction, and none is needed.

## Common translation

The center segments lie in the interiors of their pentagons except at the shared side midpoint. Two distinct carrier paths therefore cannot intersect: an interior intersection would overlap tile interiors, while a midpoint intersection would force the same PP adjacency. Each path stays within bounded distance of its axis and is a proper graph over that axis. A graph separates the plane into its two sides; the two ends of a path with a nonparallel axis eventually lie on different sides. Such a second path must intersect the first. Hence all carrier axes are parallel.

Every return has the same fixed nonzero length. Parallel axes therefore give the same vector up to sign; invariance under either sign gives invariance under the common vector. Because the AA pairing assigns every P and Q to exactly one decorated carrier, the whole saturated tiling inherits that translation. Arbitrary phase offsets or choices between distinct carriers cannot destroy this particular common period.

## Scope

The proof establishes a singly periodic tiling whenever this exact fixed-shape pair tiles. It does not assert a second independent period, construct a tiling for every heptagon with the angle word, prove metric realizability, or remove sparse defects in an arbitrary original tiling. Under the standard meaning of an aperiodic prototile set as one admitting tilings but no tiling with a nonzero translational symmetry, this implication excludes the specified resonant branch.
