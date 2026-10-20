# Sugimoto Method 3 first gate: independent hostile review

Date: 2026-10-19. Verdict: PASS for the two stated restricted exclusions. This does not settle the unrestricted two convex polygon problem. No discovery log was edited.

Reviewed `research/searches/sugimoto-method3-two-class-first-gate-2026-10-19.md` and its matching `.py` exact arithmetic audit. Replayed the script under the required mise/conda environment: PASS. The script is an executable certificate for the rational fixture, not a separate independent proof of every parameter value. No separately named Sugimoto JSON certificate was present at review time.

## Primary source and reconstruction

Checked [Sugimoto, arXiv:2404.00534v5, 15 January 2025](https://arxiv.org/html/2404.00534v5), especially Sections 1, 2, 2.2, 3 and the actual Figure 15 image. Its boundary labels and child vertex words agree with the reconstruction. Figure 15 explicitly gives equal moving distances X6Q=X8R=X10S=X12T, resolving the apparent X10T typo in the surrounding HTML prose. The 3:2 source ratio is exactly t=3/5, since X5X6=1. The listed 14 unit directions close exactly, give the pictured parent up to rigid motion, and retain X13 only as a collinear subdivision of the two-unit vertical boundary segment.

Independently inspected the resulting coordinates and every exposed edge endpoint angle. The rational audit verifies strict positive turns, angle cosines, the six exact shared edge pairs, equal complete squared distance matrices for B/C/D, and signed area equality. These are meaningful exact checks, not measurements from the source image. Its incidence dictionary alone would not prove a dissection, but the written oriented-boundary cancellation and positive winding argument supplies that missing logical step.

The all-parameter claim also checks out. Put f(t)=1-(sqrt(3)-1)t/2; then f(t)>0 on [0,1]. RS=f(t)(1,-1), QR=f(t)((sqrt(3)-1)/2,-(sqrt(3)+1)/2), and ST is the quarter-turn of QR. All other moving boundary vectors scale by t, 1-t or 2-t, while fixed vectors stay fixed. Thus every listed genuine child angle is constant and strict on 0<t<1. This independently supports extension beyond the rational replay. At t=1 the heptagon loses a straight vertex, so the open-interval scope matters.

## Convex two-child fusion attack

The geometric seam lemma is valid for polygons whose genuine vertex angles are strictly below 180 degrees. Separation of the disjoint convex interiors confines their intersection to a line. A convex union with interior cannot have only point contact. If either endpoint of the common segment lies in the relative interior of a side, its straight sector plus the other positive sector violates local convexity. Consequently the seam must be a complete genuine side of both children. This addresses partial contacts without an edge-to-edge hypothesis.

The exposed sides have endpoint angle pairs among (90,120), (120,105), (120,165), (165,75), and (75,120), including reversals. Every exposed side therefore has a vertex of at least 120 degrees; every possible partner vertex has at least 75 degrees. Their sum is at least 195 degrees. Hence two children lying in different disjoint source parents cannot fuse convexly, under arbitrary orientations or mirror placements. Their common segment must be exposed in each parent; an internal child seam cannot become a cross-parent contact along a positive segment because it lies in the parent interior. A parent boundary subdivision or a partial parent contact does not evade the seam lemma.

All six within-parent seams fail: A/H at X1 gives 270 degrees; B/H at R gives 255; C/H at R or S gives 255; D/H at S gives 255; B/C at X8 and C/D at X10 give 240. Nonadjacent children lack a common segment. No missing orientation or reflection case changes these sector sums.

## Inherited periodic escape

The parent-contained proposition is correct with reflections admitted. Select representatives of parent orbits modulo a nonzero translation period and transport the same finite dissection to each translated copy. This constructs a child tiling with that period. For a doubly periodic parent tiling, a lattice fundamental domain gives a doubly periodic child tiling. Parent stabilizers cause no obstruction: a bounded parent cannot be invariant under a nonzero translation, and a coherent representative choice is sufficient even for a symmetric parent. Partial contacts between parents are harmless.

Section 2 and Figure 2 of the primary source explicitly supply the reflected periodic parent escape. Thus every fixed parent-contained two-class repartition fails the unrestricted target, regardless of whether its chiral realization was designed around substitution. Both output classes occur whenever both occur in the fixed dissection; omission or monohedral tiling is unnecessary for this counterargument. A rule only defined on chiral collars is outside this proposition, as the artifact correctly states.

## Source caveat and scope

The source treats reflected pieces as different types and prohibits their use. Section 3 further explicitly leaves actual ASP status unconfirmed under its source assumption; Section 1 also flags an unconfirmed extracted two-type obstruction. The artifact correctly avoids using those positive claims as a forcing theorem. Its two negative proofs need only source geometry and the reflected periodic parent tiling.

No finding requires revision of the stated first gate. Larger fusions, boundary-moving exchanges across parents, and other source methods remain outside this review. A later saturation or propagation theorem would require its own review and is not certified here.
