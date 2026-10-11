# Complete periodic escape when no homogeneous trivalent star is legal

Status: **VALID after fresh independent hostile review.** This new corollary removes the A–A q exclusion from the independently reviewed double-end theorem. It closes the no-homogeneous-star branch, not the homogeneous resonance strata or the unrestricted target.

## Exact statement

Fix0<delta<30, positive distinct side lengths p,q, and common scale q=1. A has word(p,q,p,q,p,q) and directions(0,60+delta,120,180+delta,240,300+delta). B is any strictly convex closed hexagon with word(p,p,p,q,q,q). Write its pp angles(alpha,beta) and qq angles(chi,psi).

Suppose no multiset of three pp corner angles from{alpha,beta}, with repetitions allowed, sums360, and no multiset of three qq corner angles from{chi,psi} does. Then the pair is tileable **if and only if** it is, up to native rotations/reflections and common positive scale, a member of either of the two known periodic cones **or of a common side-length-swapped image of either cone**. In particular every tileable pair satisfying these hypotheses admits an actual doubly periodic tiling.

The positive cones are the equal-pp cone and complementary-pp cone in `branching-hexagon-two-run-double-end-periodic-reduction.md`; their periodic constructions have separate independent reviews. The conclusion is an existence of a periodic escape, not an assertion that all tilings of these pairs are periodic.

## 1. Exhaust the A–A q possibility

If an A–A q seam were possible in a trivalent edge-to-edge tiling, its two endpoint fillers are B pp corners. Each A q side has endpoints A_H=120+delta and A_L=120-delta. The possible two-ended filler patterns are either two120 corners, or one120-2delta and one120+2delta corner. Thus a necessary condition is alpha=120, beta=120, or

    {alpha,beta}={120-2delta,120+2delta}.

The first two are impossible under the no-homogeneous-star hypothesis, since three repeated copies of that120 pp corner sum360. Hence either A–A q seams are impossible and the reviewed double-end theorem applies directly, or the pp pair is exactly the displayed low/high pair.

In the latter case the qq pair cannot also equal this unordered low/high pair. Indeed the unit three-edge arc with internal angles x,y has squared resultant length

    F(x,y)=3-2cos(x)-2cos(y)+2cos(x+y).

This is symmetric in x,y. The binary B closure gives p^2 F(alpha,beta)=q^2 F(chi,psi). At the low/high pair x+y=240 and

    F(120-2delta,120+2delta)=2+2cos(2delta)=4cos^2(delta)>0.

Equal pp and qq unordered pairs therefore force p=q, contradicting the distinct binary domain. Thus{chi,psi} differs from the low/high pair. Also neither chi nor psi can be120, by the no-homogeneous qq hypothesis.

## 2. Exact length-swap symmetry preserving A(delta)

Apply a common scale1/p to both shapes and exchange the names of the two lengths. The new p-length is old q/p=1/p, and the new q-length is old p/p=1. This is only a change of common scale and native presentation, so actual plane tilings transfer in both directions.

A needs a reflection to restore the specified delta presentation. If its native vertices are v_j, take the new ordered vertices

    v'_j = exp(i(120+delta)) conjugate(v_{(-j) mod6})/p.

The six new directed edge vectors are

    -exp(i(120+delta)) conjugate(e_{(-j-1) mod6})/p.

They have successive new lengths(1/p,1,1/p,1,1/p,1) and directions

    (0,60+delta,120,180+delta,240,300+delta).

This is the same native A(delta), with new p=1/p,q=1. Its native H/L angles remain(120+delta,120-delta) alternating. The reflection and its reverse boundary traversal are legitimate congruent copies; independent native isometries of the two prototypes do not alter the set of allowed congruent tiles.

For B, merely start the native side list at old side3, followed by the same common scale and a rotation making its first side direction0. The new first three sides are the old q block, now called p, and the new last three are the old p block, now called q. Its new pp angles are(chi,psi) and its new qq angles are(alpha,beta). Native strict convexity and closure persist.

The absence of homogeneous stars is preserved because the two arc-angle sets are exchanged. As established above, the new pp pair(chi,psi) has neither120 corner and does not contain both120±2delta. The sufficient two-ended filler test therefore excludes A–A **new-q** seams. Equivalently, it excludes A–A old-p seams in the original geometry.

## 3. Apply the reviewed necessity and the actual positive constructions

If the original pair tiles, so does its transformed pair: common scaling and replacement of each prototype by a congruent presentation preserve the admitted tiling set. The transformed pair satisfies every hypothesis of the reviewed double-end theorem: same A(delta), distinct binary lengths, no homogeneous stars, and A–A new-q impossible. It therefore belongs to one of the two constructive periodic cones.

Apply the inverse common scaling and native congruences to that cone's actual periodic tiling. The resulting tiles are congruent to the original two shapes. The lattice translations scale by p and remain nonzero and independent, so the original pair has a doubly periodic tiling. This proves necessity of the direct-or-swapped cone list and a periodic escape for each admitted pair. Sufficiency follows from the two reviewed positive constructions and their inverse common-scale transfer. If a point of a positive cone has a legal homogeneous star, it simply falls outside this theorem's stipulated subdomain; no negative claim about that point is made.

## 4. Consequence for the ongoing broader search

The paired A–A q exception in the resonance inventory is now closed in the no-homogeneous branch, by exact symmetry rather than by additional bounded patch search. Any distinct binary pair in this A-threefold/B-two-run branch that could satisfy the aperiodicity target must therefore lie on one of the eight homogeneous-star hyperplanes

    alpha=120, 2alpha+beta=360, alpha+2beta=360, beta=120,
    chi=120, 2chi+psi=360, chi+2psi=360, psi=120.

The separately pending72 mixed-cover hyperplane obstruction further restricts these resonant shapes if reviewed valid. None of this settles the resonance strata, the equal-length domain p=q, or the unrestricted two-prototile target.

## Review obligations

Dependencies are the independently reviewed double-end reduction and both positive cones. Fresh review must verify the A reflection/indexing formula, the B rotation of native blocks, exact arc magnitude formula and its nonzero low/high value, invariance of the no-homogeneous hypothesis, and the transfer's common scale for both prototypes. The source lemmas and certificates remain unchanged.
