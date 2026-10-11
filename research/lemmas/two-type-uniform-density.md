# Uniform occurrence and positive lower density of an unavoidable tile set

**Status:** proved and independently adversarially reviewed VALID on
2026-10-10; see [the hostile review](../reviews/two-type-uniform-density-review.md). This is not a
resolution of the two-tile problem.

## Statement and definitions

Let P be a finite set of fixed compact convex polygons with nonempty
interiors. All isometries, including reflections, and arbitrary partial-edge
contacts are permitted. A P-tiling covers the plane with interior-disjoint
copies; it may omit prototile classes. Assume at least one P-tiling exists.
Partition P into disjoint sets S and M, and assume that S admits **no** plane
tiling under these same conventions. An empty S has no plane tiling.

Then there is a finite number L > 0, depending only on P and S, such that in
**every** P-tiling, every closed disk B(x,L), for every x in the plane,
intersects a tile whose type belongs to M.

Let D > 0 bound the diameters of all members of P, let a_M > 0 be the minimum
area of a member of M, and put r=L+D. For every P-tiling, every square
Q_R(x)=x+[-R,R]^2, and every R>r, the number N_M(Q_R(x)) of M-tiles whose
interiors meet the interior of this square satisfies

    N_M(Q_R(x)) >= 4(R-r)^2 / (pi r^2).

Writing U_M for the union of all M-tiles, the following uniform area bound
also holds:

    area(U_M intersect Q_R(x)) >= a_M 4 max(R-D-r,0)^2 / (pi r^2).

In particular the lower limits of the tile count divided by 4R^2 and the
M-covered area divided by 4R^2 are at least 1/(pi r^2) and
respectively a_M/(pi r^2), uniformly in the tiling and square center. These
are lower-density bounds, not assertions that frequencies exist.

## Uniform compactness of unrestricted tilings

Choose an anchor c_T in the interior of each reference polygon T in P.
Choose rho>0 so that B(c_T,rho) is contained in the interior of T for every
T; finiteness of P permits this common rho. Relative to its anchor, a tile
occurrence is specified by a type T, an anchor position p, and an orthogonal
matrix O in O(2); its point set is p+O(T-c_T). There may be several such
representations if the reference polygon has symmetries; choose one per
occurrence. Every occurrence is contained in B(p,D) and contains the open
disk B(p,rho). Consequently distinct anchors in a tiling have distance at
least 2rho.

For anchors in any disk B(0,b), their interior-disjoint radius-rho disks are
contained in B(0,b+rho). Hence their number is at most
(b+rho)^2/rho^2, independently of the tiling. The same argument bounds all
tiles meeting any compact set, since their anchors lie within distance D of
that set. In particular all the tilings are locally finite.

Here is an explicit sequential extraction, requiring no finite local
complexity and no discrete set of orientations. Enumerate the tile
occurrences of each tiling in order of increasing anchor distance from the
origin; break ties in any fashion. There are infinitely many tiles, and
only finitely many within any bounded anchor distance, so such an
enumeration exists. Let A be the maximum reference polygon area. Tiles
covering B(0,b) have anchors in B(0,b+D), and there must be at least
pi b^2/A of them. Therefore for every fixed index j there is a universal
finite radius b_j+D containing the jth anchor, by choosing pi b_j^2/A>j.
Its position has a compact bounding disk; its type lies in a finite set;
its orthogonal part lies in compact O(2). Successive subsequences and a
diagonal extraction make the placements at every fixed index converge.
Different limit anchors retain their distance at least 2rho, so indices do
not merge into duplicate occurrences. The limit collection is locally
finite by the same disk packing estimate.

It is a plane tiling. An overlap of interiors of two limit tiles would
contain a point at positive distance from both boundaries; by convergence
of the two isometries that point belongs to both approximating interiors
for sufficiently large indices, a contradiction. To check coverage fix a
point y. An approximating tile covering y has anchor in B(0,|y|+D).
The packing bound gives a universal finite upper bound on the enumeration
index of every anchor in that disk. Among this finite prefix, one fixed
index covers y infinitely often. Membership in its closed polygon passes
to its limiting occurrence, so the limit collection covers y. Since y was
arbitrary it covers the plane. This verifies compactness of the whole
space of admitted placements, not merely of finite edge-to-edge patches.

## Proof of uniform occurrence

Suppose no common L works. For each positive integer k choose a P-tiling
and a disk B(x_k,k) which intersects no M-tile. Translate x_k to the origin.
The translated tilings have a convergent diagonal subsequence by the
preceding compactness argument. A limit tile of type in M would have its
finite anchor position approached by the corresponding occurrence's
anchor positions. For sufficiently large k that occurrence lies inside
B(0,k) (in particular its anchor does), contrary to the clean-disk choice.
Every limit tile therefore has type in S, yielding a plane S-tiling. This
contradicts the hypothesis. Some finite L>0 consequently works for all
P-tilings and all centers simultaneously.

Notice the distinction between a uniform bound over all tilings, proved
here, and a bound inferred from a single favored tiling. The compactness
contradiction permits the tiling to vary with k.

## Proof of the quantitative bounds

Use the fixed anchor convention above in any one admitted tiling. Every
point y lies within distance r=L+D of an M-anchor: the occurrence conclusion
provides an M-tile intersecting B(y,L), and its anchor has distance at most
D from any point in that tile. Thus disks of radius r centered on
M-anchors cover the plane.

Fix Q_R(x), with R>r. Every point of Q_(R-r)(x) lies in the radius-r disk
of some M-anchor in Q_R(x), since Euclidean distance at most r bounds each
coordinate difference by r. There are finitely many such anchors. Area
subadditivity gives

    4(R-r)^2 <= (# M-anchors in Q_R(x)) pi r^2.

Every anchor is interior to its tile. Even when an anchor lies on the
square boundary, its tile's interior disk intersects the square interior.
Thus all occurrences counted on the right contribute to N_M(Q_R(x)),
which proves the count bound.

For the area bound, use the inner square Q_(R-D)(x). If R-D>r,
the same covering argument gives at least 4(R-D-r)^2/(pi r^2)
M-anchors there. Every tile anchored in this inner square is entirely
contained in Q_R(x), because its diameter is at most D. Their interiors
are disjoint and their areas are at least a_M, proving the claimed area
bound. When R-D<=r the displayed estimate is zero and follows from area
nonnegativity. Dividing these count and area estimates by 4R^2 and taking
lower limits proves the stated positive uniform constants.

## Corollary for a hypothetical aperiodic pair of hexagons

Suppose two fixed genuine convex hexagons form an aperiodic pair under
research-problem.md. Neither member can admit a monohedral plane tiling:
by the imported unrestricted monohedral hexagon classification and the
classical periodic constructions of its three families, such a member
would admit a periodic monohedral tiling, which is also admitted by the
pair and violates aperiodicity. Apply the theorem with S equal to either
single member. Both types must occur within a common uniformly bounded
distance of every point in every admitted tiling, and both have positive
lower area and tile densities. The same holds in any defect-free limit
tilings obtained from the pair.

The classification enters only this corollary. The general compactness and
density theorem has no monohedral-classification dependency. Its conclusion
does not constrain the geometric neighbor map to be deterministic and does
not supply a periodic tiling for a branching two-hexagon language.

## Dependencies and review boundary

The compactness and quantitative statements are proved in this file without
external theorems. The hexagon application imports Zhu, Wang, Yan,
*Hexagonal Tiling of the Plane*, arXiv:2508.01404v2, Main Theorem, as recorded
in [hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md).
The general statement and its quantitative bounds passed the independent
[hostile review](../reviews/two-type-uniform-density-review.md). No novelty
claim is made.
