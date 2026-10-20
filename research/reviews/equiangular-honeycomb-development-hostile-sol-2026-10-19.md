# Hostile review: legal equiangular honeycomb development

2026-10-19. Reviewer: independent Sol agent, not author of the lemma.
Reviewed: `research/lemmas/equiangular-hexagon-honeycomb-development-2026-10-19.md`.

## Claim and hypotheses checked

The claim is a transfer for one entire legal labeling of the ordinary complete
hexagonal honeycomb by two fixed positive strictly convex 120-degree hexagons,
with native rotations and reflections allowed and equality across every paired
full side. It claims global plane realization, uniqueness of development,
and transfer of rank-two symbolic translation periods to independent physical
translations. It does not claim a legal labeling exists for arbitrary shapes,
or establish unrestricted geometric-to-symbolic equivalence.

## Attempted failures and findings

1. **Incomplete flat surface.** A simply connected locally flat plane need not
   be complete in general, so angle sums alone are insufficient. Here the global
   piecewise affine comparison repairs precisely that issue. The six fan
   triangles of each strictly convex target have positive area because the
   vertex mean is strictly interior. With two fixed polygons and finitely many
   native frames, the finitely many affine triangle maps and inverses have
   uniformly bounded norms. Target translations or rotations do not alter
   those norms. Sidewise affine maps agree in the glued quotient. The resulting
   global homeomorphism is bi-Lipschitz for intrinsic length metrics. This
   rules out finite-length escape through infinitely many cells.

2. **Hidden assumption in path subdivision.** The argument can be made direct:
   a continuous path with compact parameter domain has compact image in the
   locally Euclidean topology of S. A locally finite cell complex has finitely
   many cells meeting that compact image. On that finite union, the finite
   piecewise affine comparison is a usual length comparison, including paths
   which touch or run along cell boundaries. Apply this to arbitrary
   rectifiable paths in either direction and take infima. Thus no unproved
   bound on the number of edge crossings is needed. The draft's finite-path
   density sentence is adequate, but this observation is an optional
   clarification.

3. **Local singularity or reflected orientation.** Each vertex has exactly three
   incident sectors, each of angle 120 degrees; edge gluings reverse boundary
   orientation and make the topological plane an oriented surface. Native
   reflection choices change the cyclic side assignment, not the sector angle.
   Full matching sides supply Euclidean neighborhoods at edges and vertices.
   No cone or boundary singularity remains.

4. **Overlapping or non-surjective development.** Completeness plus local
   Euclidean structure permits the complete local-isometry covering theorem.
   Since S is a simply connected plane and the target is R^2, the developing
   map is a global isometry. Face interiors are consequently disjoint and
   every point is covered. Properness and the bi-Lipschitz cell comparison also
   imply local finiteness. No finite-patch-to-infinite-tiling inference is used:
   the hypothesis already supplies the full infinite labeling.

5. **Nonunique attachment.** Fixing an oriented first tile fixes the across-edge
   placement of each neighbor in the opposite half-plane, because the native
   side and its two endpoints are fixed. Connectedness propagates the choice;
   flat simple connectivity ensures consistency. Accordingly uniqueness up to
   a global isometry is valid. Once the complete first tile placement is fixed,
   that remaining global freedom is of course fixed as well.

6. **Symbolic period becomes a rotation.** A state-preserving abstract
   translation acts by intrinsic isometries: each face has an identical
   species/native state at its translate, so the vertex correspondence extends
   by a Euclidean isometry and agrees across shared edges. The intrinsic action
   is orientation preserving and fixed-point free, including on edges and
   vertices. Conjugacy under the global development preserves that fact. A
   nonidentity orientation-preserving Euclidean isometry is a translation or
   a rotation, and every rotation has a fixed point. Hence the conjugate is a
   nonzero translation, regardless of whether its angle would have infinite
   order.

7. **Two symbolic periods collapse to one geometric direction.** Injectivity
   of the abstract action alone would not suffice: Z^2 embeds densely in a line
   by an irrational ratio. The draft correctly uses metric comparison.
   Explicitly choose one reference point in a face and its images under the
   rank-two period lattice. The facewise affine comparison is equivariant
   under those periods (the target center is the vertex mean). Its lower
   bound compares physical displacement with the corresponding standard
   honeycomb lattice displacement. Collinear images of two independent
   generators would yield integer combinations with unbounded standard
   displacement but bounded physical displacement, by rounding one multiple
   against the other. This contradicts the lower bound. Thus the physical
   period vectors really are linearly independent.

8. **Native symmetry and unproved period converse.** Repeated side lengths and
   polygon symmetries can make different native labels physically identical.
   This creates extra geometric symmetries and can invalidate an unqualified
   converse from unmarked periods to literal native-state periods. It does not
   affect the sufficient direction proved here: a literal state-preserving
   period always induces the isometry above. The draft explicitly does not
   identify all physical periods and requires a separate structural and
   symmetry argument for the converse. No converse is silently used in the
   theorem. Distinct species need not be assumed for the forward transfer;
   congruent or symmetric instances still obey it.

## Defects, repairs and remaining uncertainty

No blocking defect found. No root-file change or mathematical repair was made.
The optional compact-path elaboration above can replace the path-density
sentence for readers seeking every length-metric detail. The uniqueness wording
can be simplified, but does not change its mathematical content.

The full-edge/trivalent structural theorem and the geometric-period converse
were not proved by this review. They are outside this lemma's forward transfer.
In particular this result alone cannot certify aperiodicity of a symbolic
system interpreted as unmarked polygons.

## Verdict

**Valid** for the exact forward-transfer statement and its rank-two periodic
escape consequence, under the stated whole infinite honeycomb labeling
hypothesis. This is a proof review, not a computational certificate or an
existence result for a particular pair of native words. No discovery-log or Git
operation was performed by the reviewer.
