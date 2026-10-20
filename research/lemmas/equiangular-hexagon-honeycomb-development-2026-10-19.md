# Development of a legal equiangular-hexagon honeycomb

Status: independently hostile-reviewed VALID on 2026-10-19; see
`../reviews/equiangular-honeycomb-development-hostile-sol-2026-10-19.md`.
This is an existence and periodic-escape transfer for a specified symbolic
labeling. It asserts neither that such a labeling exists for a given pair nor
that every labeling is aperiodic.

## Statement

Let `A,B` be positive, strictly convex, equiangular 120-degree hexagons.
Take the ordinary abstract face-to-face hexagonal honeycomb, with its fixed
cyclic order at every face and three faces at every vertex. At each face
place one isometric copy of `A` or `B`, with any of its six rotations in the
common edge-direction frame and either reflection parity. Require the two
native sides identified across each abstract edge to have exactly equal
length. Then these copies realize a locally finite edge-to-edge tiling of
the whole Euclidean plane, unique up to a global Euclidean isometry after
the combinatorial labeling and the first tile placement are fixed.

If the labeling is invariant under a rank-two sublattice of orientation-
preserving translations of the abstract honeycomb, the developed tiling
has two independent Euclidean translation periods. In particular, one
explicit legal periodic symbolic carrier kills the pair's aperiodicity.

## Proof of plane development

Glue the assigned polygon copies along each paired full edge by the unique
length-preserving identification that reverses boundary direction. Edge
equality makes this well-defined. The quotient surface `S` is topologically
the ordinary honeycomb cell complex, hence is a plane. Its intrinsic path
metric is locally Euclidean: in face interiors this is immediate, across
edges two Euclidean half disks meet, and at vertices the three 120-degree
sectors total 360 degrees. There are no cone singularities or boundary.

To prove metric completeness rather than assume it, use the standard
regular-hexagon realization `H` of the same abstract honeycomb. On each
regular face, send its six boundary vertices to the six assigned target
vertices in cyclic order, and send its center to any fixed interior target
point, for example the mean of those six vertices. Triangulate by the six
center-to-side triangles and extend affinely on each. The map is a
homeomorphism of each face because the target is strictly convex. Adjacent
face maps agree on their common side: both linearly parameterize the same
geometric segment from the same abstract endpoint to the same identified
endpoint. Therefore they glue to a homeomorphism `F:H→S`.

There are only finitely many target shapes and native orientations. Every
triangle map has positive finite singular values. Thus one constant `L≥1`
bounds all piecewise affine maps and inverses. Subdividing rectifiable paths
at cell boundaries gives, for all `x,y∈H`,

    L^{-1}|x-y| ≤ d_S(F(x),F(y)) ≤ L|x-y|.

One can equivalently apply the bounds first to finite cell-crossing polygonal
paths and then use density. Continuous compact paths meet only finitely many
cells by local finiteness; they need not cross edges only finitely often.
Hence `S` is complete and proper because `H` is.

A complete simply connected flat Euclidean surface is globally isometric
to `R²`: the developing map from a chosen tangent frame extends along all
paths, path independence follows from simple connectivity and zero
curvature, and completeness makes the resulting local isometry a covering
of `R²`; both surfaces are simply connected, so it is an isometry. The
images of the glued faces consequently cover `R²` with disjoint interiors,
including every seam and vertex. The fixed first tile and frame determine
the development uniquely up to a Euclidean isometry.

## Symbolic period transfer

The chosen target center is the vertex mean, so the piecewise affine map is
equivariant under any translation preserving the full symbolic assignment.
An orientation-preserving abstract honeycomb translation preserving every
face's assigned species and native state acts as an orientation-preserving
isometry of `S`, so development conjugates it to an orientation-preserving
Euclidean isometry. It acts freely on cells and has infinite order. It
therefore cannot become the identity or a finite-order rotation. An
infinite-order plane rotation has a fixed point, whereas the abstract
translation has none; fixed points are preserved by conjugacy. Thus the
conjugate is a nonzero Euclidean translation.

For two independent abstract translation generators, their Euclidean
translation vectors must be independent. Otherwise a nontrivial integer
combination might still fail to vanish if collinear incommensurable; the
stronger reason is the global bi-Lipschitz comparison above. If a sequence
of independent abstract lattice vectors tended to infinity while their
developed displacement stayed bounded, the lower bound would fail. A
linear homomorphism from `Z²` to `R²` with collinear image and a periodic
cell labeling produces such a sequence by integer approximation (or an
exact kernel when the ratio is rational). Hence the two vectors are linearly
independent and give a rank-two Euclidean period lattice.

The theorem does not identify all geometric periods of a development.
For an aperiodicity proof one also needs the converse: a nonzero geometric
translation of the unmarked tiling induces a nontrivial abstract honeycomb
translation preserving the symbolic species/native-length assignment, after
quotienting native states that are the same physical polygon. That converse
uses the separate full-edge/trivalent structural theorem and must include
shape symmetries and reflections.
