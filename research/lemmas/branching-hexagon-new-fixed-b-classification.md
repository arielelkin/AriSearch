# Complete periodic-escape theorem for a threefold hexagon and a four-q-side partner

**Status:** proved and independently hostile-reviewed VALID on 2026-10-10; see [the fresh review](../reviews/branching-hexagon-new-fixed-b-classification-review.md). No novelty claim. This classifies the specified fixed-B side-word family, including its qq-resonant contacts; it is not an unrestricted two-convex-tile theorem.

## Exact family and theorem

Let A be a genuine strictly convex hexagon with directed edges of alternating lengths p,q,p,q,p,q in directions

    0,60+delta,120,180+delta,240,300+delta,
    p,q>0, p!=q, 0<delta<60 degrees.

Equivalently A has threefold rotational symmetry and alternating corner angles alpha_plus=120+delta, alpha_minus=120-delta. Its opposite-parity three-edge orbits separately sum to zero.

Let B be any given genuine strictly convex hexagon with native side word

    (r,p,q,q,q,q),  r,p,q pairwise distinct.

Its angles are beta0,...,beta5. Corners0,1,2 have incoming/outgoing pairs rq,rp,pq; corners3,4,5 have qq. Reflections and unrestricted contacts are permitted in the original tiling problem. No orientation, chirality or matching rule is added.

**Theorem.** Every such pair either has no plane tiling or admits a tiling with a nonzero translational symmetry. In particular no pair in this family is aperiodic under the problem definitions.

The proof does not assert every original tiling is periodic. Its only imported geometric dependency is the independently reviewed defect-free-limit theorem for two fixed genuine convex hexagons. This supplies an admitted edge-to-edge trivalent tiling whenever an unrestricted tiling exists. The new saturation limit below is proved directly.

## Two prior elementary mechanisms, with their precise scope

1. If beta3+beta4+beta5=360, B edges2 and5 are equal and oppositely directed. B has a periodic monohedral witness: with V0=0, u=V2 and v=V3+V4-V1, use faces B,V1-B and reversed-edge pairs

       (0,0)/(1,0):0; (0,1)/(1,1):u;
       (0,3)/(1,3):v; (0,4)/(1,4):v-u;
       (0,2)/(0,5):u; (1,2)/(1,5):-u.

   Their four corner links have angle sums beta0+beta1+beta2=360 or beta3+beta4+beta5=360. They form a flat torus, and det(u,v)=2area(B)>0. The complete direct proof is in [the chirality-collapse lemma](branching-hexagon-new-chirality-collapse.md). This requires no monohedral classification.
2. If no multiset of three B qq angles sums to360, every trivalent edge-to-edge A,B tiling has a period. The complete proof is in [the private-chain theorem](branching-hexagon-new-private-chain-periodicity.md): B sides0 and2 must half-turn-match their own native slots, yielding disjoint infinite straight midpoint chains of a common translation length; all A placements are physically determined by the B set. This prior theorem is used only in the repeated-required-angle case below. It covers all ten three-corner qq multisets and does not assume local-to-global extension.

We now handle the genuinely resonant cases left by mechanism2.

## The required qq angle and local r-dimer ledger

Assume a plane tiling exists. Pass to an admitted trivalent edge-to-edge tiling by the reviewed hexagon limit theorem. This limit cannot omit B: every A corner has pair pq, so a monohedral three-ray vertex would require an odd three-cycle whose every consecutive length pair is pq, impossible for p!=q. If the limit omits A, the r-dimer argument below forces S=360; thus under the standing S!=360 assumption both types occur. Put

    S=beta3+beta4+beta5.

If S=360, mechanism1 settles the pair. Hence assume S!=360.

Every B r side is its unique native side0. A reflected same-slot mate puts two rp corners at one endpoint, requiring a nonexistent pp corner. Therefore every r seam pairs B by the half-turn about its midpoint. At both endpoints the two B corners are corners0 and1, and the third corner must be pq. If it were B corner2, beta0+beta1+beta2=360 would imply S=360. Hence it is always A, with the fixed angle

    kappa=360-beta0-beta1 in {alpha_plus,alpha_minus}.

Define kappa'=240-kappa, the other A angle. The r-dimer stars force B sides1 and5 to meet A, and fix those A placements: at B corner1 the A angle is kappa; at B corner0 the A angle is kappa. A's three intrinsic rotations identify its corresponding length slots, while its two physical chirality options exchange alpha_plus and alpha_minus at a selected endpoint. Thus a specified endpoint angle fixes the whole A placement.

At B corner2, its p-side A neighbor has angle kappa', and the third corner has lengths qq. It is a B qq corner with the required angle

    mu=360-beta2-kappa'=120+kappa-beta2.                (1)

Every B copy has such a source corner2, and each source is completed by one B qq target of angle mu. Therefore mu occurs among beta3,beta4,beta5. The target is incident across the source's q side2. A qq target cannot be used by two source corners2: that would put two B pq corners at a vertex and make their p sides neighbors, although those p sides already meet A by the r-dimer ledger.

The hexagon angle sum and the definition of kappa give

    beta2+S=360+kappa, hence S=240+mu.                  (2)

This numerical identity is the decisive restriction on repeated required angles.

## Repeated required angles reduce to the already closed nonresonant case

Let m be the number of native qq corners of angle mu.

* If m=3, equation(2) gives3mu=240+mu, hence mu=120 and S=360. This contradicts the standing assumption and was already settled monohedrally.
* If m=2, write nu for the third qq angle. Equation(2) gives mu+nu=240. Since S!=360, mu!=120 and nu!=mu. Every three-qq multiset has k copies of mu and3-k copies of nu, so its sum minus360 is

       (2k-3)(mu-120),  k=0,1,2,3.

  This is never zero. Thus mechanism2 applies: the admitted tiling has a nonzero period.

It remains only m=1. Let j in {3,4,5} be its unique target slot.

## A proved saturation limit for the unique target slot

Map each placed B source corner2 to the B copy carrying its mu target. This is an injection on the set of B copies, because every copy has exactly one source and, when m=1, exactly one target. This is not presumed surjective on an infinite set.

Choose B centers to be their vertex averages. Let D bound all tile diameters. Source and target copies share a corner, so their centers have distance at most2D. Let N_B(R) count B centers in a disk of radius R, and let U(R) count unused target-owner centers in that disk. All sources in the radius R-2D disk map to distinct target owners in the radius R disk. Consequently

    U(R) <= N_B(R)-N_B(R-2D)=O(R).                      (3)

The annular bound is rigorous: each B tile whose center lies in this annulus has positive fixed area and is contained in the annulus enlarged by D on both boundaries. Its area is O(R); pairwise disjoint interiors bound the number of such tiles by that area divided by area(B). All constants depend only on the two fixed shapes. Centers and their native target corners differ by at most D.

For each integer n choose R sufficiently large compared with n^2. The disks of radius n+3D around the O(R) unused target centers cover area O(n^2 R), less than the area of an inner disk of radius proportional to R. Thus there is a point surrounded by a radius n+3D disk containing no unused target centers. Every A q side meets B: an A/A q seam would require a pp third corner. Therefore a B tile center lies within2D of this point. Root at that B and move it by an isometry to its fixed native placement. The resulting tiling has no unused target near any point in a disk of radius tending to infinity around the fixed root.

Here is a direct compactness proof preserving this property. Across a complete native side of a fixed root polygon there are only finitely many possible neighboring placements: choose one of the two types, one of its finitely many equal-length side slots, and an orientation sign. The isometry matching that side is then determined. A face-adjacency ball of any fixed graph radius has finitely many geometric possibilities. Repeated subsequence selection stabilizes every such finite ball exactly.

These stabilized balls cover the plane. For each Euclidean radius t, the number of tiles meeting its disk is uniformly bounded by area of a disk enlarged by2D divided by the minimum tile area. For a dense set of target points in that disk, a straight segment from the root tile center avoids every vertex and crosses boundaries transversely. Each convex tile meets that segment in at most one interval, so it crosses at most that uniform number of distinct tiles. A uniformly bounded finite adjacency ball therefore covers a dense subset of the disk. Its union of closed tiles is closed and covers the entire disk. The stabilized ball still does. Disjoint interiors are inherited by every finite collection. Thus the union of the stabilized adjacency balls is an actual admitted plane tiling, with full-edge trivalent contacts and the same fixed root B.

Whether a mu target is used is determined by its three incident corners, a finite adjacency neighborhood. Every such neighborhood stabilizes while remaining inside a growing disk free of unused targets. Therefore every target in the limit is used. We have obtained an admitted **saturated** tiling with all native corner-j targets used by B corner2 stars. No zero-density-to-absence assertion about the original tiling was made.

## Unique target j3: a periodic saturation limit

Every B corner3 in the saturated tiling belongs to a B2/B3/A star. Source side2 cannot meet B side5, already A. A mate on side3 or4 would put B3 and a qq mate at the other seam endpoint, requiring a third qq corner and hence a three-B-qq star. This is impossible because the original B3 target is saturated with an A and B2. A same-slot side2 reflection requires pp at one endpoint. Thus every B side2 half-turn-matches native side2.

The corner3 B2/B3/A star forces side3 to meet A, with its angle kappa'. Side5 already meets A with angle kappa at corner0. Side4 must meet A as well: B mates on slots2,3,5 are already unavailable, and a B4/B4 seam would have two qq corners at corner4 although the known A across side3 has pq there. The three length pairs qq,qq,pq cannot form a three-ray star. This excludes that mate even when a numerical qq-angle triple is legal.

All A placements around B sides1,3,5 are fixed by the known kappa or kappa' endpoint. The placement across side4 is fixed at corner4 by the known A across side3, with its required endpoint angle360-beta4-kappa. Every A q side meets B and hence one of the uniquely filled B sides3,4,5. Therefore the entire A set is determined by the B set.

Inside B connect the midpoints of native sides0 and2. The matched half-turn neighbors continue this segment as an exact straight line through a bi-infinite B chain. Its two-step translation vector is

    T=V2+V3-V0-V1 !=0.

Distinct chain lines cannot cross: at any point of one line its one or two incident B tiles contain a full neighborhood; a nearby non-seam point of the other line lies in a B interior whose open interior ball would overlap an incident first-chain B interior. They therefore share a B and are the same chain. All chains are parallel, and all physical T images have the same length, so all B chains share one translation vector up to sign. The whole B set and its uniquely determined A set are periodic. This is exactly the global straight-chain mechanism, now established without a qq nonresonance hypothesis.

## Unique target j5: impossible native incidence parity

Every B corner5 is saturated with B2 and A. Its q side5 already meets the A fixed by the r-dimer star. Hence its other incident side4 meets the B2 source. Thus every B side4 pairs with a B side2, and conversely every B side2 pairs with native side4.

At the other endpoint of such a side2/side4 seam, the two corners are B3 and B4, both qq. Their third corner must be B qq. It cannot be corner5, since all corner5 targets have an A in their saturated star. Thus all three native corners at this vertex belong to {3,4}.

Count their incident native side slots. Each corner3 has one side2 halfedge; each corner4 has one side4 halfedge. Every side2 is paired with side4, so at this vertex the number of corner3 sectors equals the number of corner4 sectors. But their total is3, an odd number. This is impossible. Equivalently the third sector's native side2 or4 would have to pair with one of the other sectors' side3 halfedges, contradicting the global side2/side4 matching. No angular estimate or frequency extrapolation enters this local contradiction.

## Unique target j4: an odd q-edge cycle in A

Every saturated corner4 has B2 and A. Therefore every B source side2 meets native side3 or4. If it met side4, the other seam endpoint would contain B3 and B5 with qq third corner. This would be a three-B-qq star involving B5, although side5 of that B already meets A. Hence side2 cannot meet4. It pairs with native side3; every side3 therefore pairs with side2, while side4 meets A.

At the other endpoint of the side2/side3 seam, the two corners are B3,B3. The qq third cannot be B4, saturated with an A, or B5, already adjacent to its side5 A. Thus it is another B3, and beta3=120.

The A across side4 has angle kappa' at B corner4, hence kappa at B corner5. The A across side5 has angle kappa at B corner0, hence kappa' at B corner5. Thus beta5+kappa+kappa'=360, so beta5=120. The A q-side neighbors are only B sides4 or5 because B sides2,3 are already B/B.

Call such an A q side tag4 or tag5 according to the B slot it meets. The exact native incidence ledger is:

| A q-neighbor tag | B corner at A's kappa endpoint | Adjacent A p neighbor there | B corner at A's kappa' endpoint | Adjacent A p neighbor there |
| --- | --- | --- | --- | --- |
| 4 | B5, angle120 | A | B4, saturated B2/A star | B |
| 5 | B0, r-dimer star | B | B5, angle120 | A |

For tag4 this follows from the fixed A across B side4 just described; for tag5 it follows from the fixed A across B side5. At a B5 star the other two sectors are A with angles kappa and kappa', and their shared ray is p, so the corresponding A p neighbor is A. At a B4 or B0 star the corresponding p neighbor is B.

Each A p side has one kappa endpoint and one kappa' endpoint. Its neighbor type must agree at its two endpoints. The ledger therefore forces the q tags on the two sides of each A p side to be different. But A has three q sides joined cyclically by its three p sides. They would have to be two-colored by tags4,5 with adjacent tags different on a3-cycle, impossible. This argument is unchanged for reflected A copies, which reverse the cyclic order but retain the odd cycle.

Thus j4 is impossible.

## Completion, quantifiers and exact remaining scope

The required angle mu either does not occur (no tiling), occurs once (j3 gives an admitted periodic limit; j4,j5 are impossible), occurs twice (the nonresonant chain theorem gives a period), or occurs three times (the monohedral case). These exhaust all cases, proving the stated theorem.

There is no computation-assisted component in this classification. The finite ten-qq-multiset parity computation is written explicitly. The saturation argument proves an actual plane limit by finite side-neighbor stabilization, and the periodic construction is the complete chain tiling in that limit. No bounded failure-to-find claim, irrational-frequency inference, imposed edge rule or forced use of both species is introduced.

The original target remains unresolved outside the exact family. Reopening this mechanism requires changing the A threefold alternating-angle/length assumption, the B word(r,p,q,q,q,q), the distinctness of r,p,q, or another stated hypothesis. The former qq-resonant subfamily within these hypotheses is no longer an unclassified global gap if this proof survives independent review.
