# One noncentral homogeneous arc: pairing or untileability

Status: **VALID after fresh independent adversarial review.** This is a new actual-contact and boundary-count mechanism; no finite quotient search or positive linear balance is used. It isolates the remaining one-arc center and two-arc homogeneous cases.

## Scope and result

Fix two strictly convex hexagons A(delta),B with distinct positive lengths p,q,0<delta<30. A's lengths are(p,q,p,q,p,q), directions(0,60+delta,120,180+delta,240,300+delta), with native corners H=120+delta and L=120-delta, three each. B has length word(p,p,p,q,q,q), pp angles alpha,beta, qq angles chi,psi, and two mixed corners. Reflections are permitted. Each arc's four possible homogeneous triple angle sums use repetition of its two native corners.

Assume exactly one B arc admits a homogeneous triple, the other admits none, and the homogeneous arc is **noncentral**: its two angles are not both120. Call an arc *paired* if its unordered angles are{120-2delta,120+2delta}.

**Theorem. If the nonhomogeneous arc is not paired, the pair is untileable even with unrestricted contacts. If it is paired, the reviewed paired-qq theorem after an exact length swap when required gives a complete classification into its two periodic cones. Consequently every tileable pair under the stated one-arc noncentral hypotheses has a doubly periodic tiling.**

This does not treat a homogeneous arc with both native angles120, two homogeneous arcs, equal lengths, or arbitrary A. The center exclusion is essential to the seam-count proof below.

By the reviewed length-swap/reflected A normalization, it suffices to treat homogeneous pp and nonhomogeneous qq. The transformation applies common scaling1/p, swaps the B length blocks by beginning at old side3, and turns the reflected/reindexed A back to the displayed A(delta); it swaps the ordered pp/qq arc data but preserves unordered pairing, noncentrality and homogeneous-star legality. The exact transformation is recorded in the independently VALID no-homogeneous-star classification lemma. When qq is paired, the independently VALID paired-qq classification already supplies the result. The remainder therefore assumes qq has no homogeneous triple and is not paired.

## Common finite boundary counts

Use the reviewed actual defect-free trivalent edge-to-edge limit of any alleged unrestricted plane tiling by the two fixed hexagons. Omission of either species is allowed. Fixed positive side lengths, finite diameters/areas and reviewed native vertex separation give O(R) boundary discrepancies when counting tiles, vertices or whole seams in a square of side2R. Let N_A,N_B denote selected tile counts and Y_p,Y_q counts of homogeneous ppp and qqq stars; every equation below has a fixed O(R) discrepancy independent ofR.

Every trivalent binary-length star has zero or two mixed pq corners. A contributes six mixed corners; B contributes two mixed and four homogeneous corners. If V_m counts two-mixed stars, then

    2V_m=6N_A+2N_B+O(R),
    4N_B=V_m+3(Y_p+Y_q)+O(R).

Hence

    N_A=N_B-Y_p-Y_q+O(R).

Noqq homogeneous triple is legal, so Y_q=0 exactly. Total selected tiles satisfy N_A+N_B=Omega(R^2). No limiting frequencies or uniform species density are presumed.

An AA seam along either length has a third native B homogeneous corner at each endpoint. The two endpoint A angle-pair sums are either H+L at both ends, or2H at one end and2L at the other. Thus an AAp seam requires a native qq angle120, or the unordered qq pair{120-2delta,120+2delta}. The former permits a forbidden threefold repetition homogeneous qq star, and the latter is excluded by hypothesis. Therefore **AAp seams are impossible**. The same test will exclude AAq where the pp angle data have neither a120 member nor the paired unordered set.

## Mixed homogeneous pp multiset

Away from the center, a mixed homogeneous pp multiset has either2alpha+beta360 oralpha+2beta360. It cannot contain a native120 angle: substituting such an angle forces both120. Nor can its pp arc be paired: that pair sums240, and either homogeneous mixed equation would again force both120, impossible fordelta>0.

Thus both AAp and AAq seams are impossible. Every pair of tiles in a trivalent star are neighbors along a ray, so a star can contain at most one A. A mixed A corner forces one other mixed corner and one homogeneous corner by cyclic binary labels; the other mixed corner must be B's and the homogeneous corner also B's. Thus each of A's six native corners consumes one B mixed corner, yielding

    6N_A<=2N_B+O(R), so N_A<=N_B/3+O(R).

Only that one mixed homogeneous pp multiset is legal: the four pp resonance planes meet only at the excluded center. Every such star consumes at least two occurrences of the repeated native pp slot. Each B supplies one occurrence of that slot, hence

    Y_p<=N_B/2+O(R).

The common count gives N_A=N_B-Y_p+O(R)>=N_B/2+O(R). Combining with the previous upper bound implies N_B=O(R) and then N_A=O(R), contradicting quadratic tile count. This excludes both mixed-multiset branches. It uses no hypothetical actual occurrence of the legal homogeneous star; zero occurrences are included.

## Pure homogeneous pp slot: exact middle-side contact and seam bound

It remains to treat one native pp angle120 with the other different from120. Reflect/reindex B if necessary so alpha120 and beta unequal to120. Reflection swaps both pp and qq orders; the unordered assumptions on qq persist. The only legal homogeneous pp star is three alpha corners, so write Y=Y_p.

Let E count B/B whole p seams. Since AAp is impossible, every A p side meets a B p side, giving

    3N_A=3N_B-2E+O(R).

The common count also gives N_A=N_B-Y+O(R), therefore

    3Y=2E+O(R).

We now prove the stronger bound E>=3Y+O(R), without assuming that a legal pure star occurs everywhere.

B's middle p side1 has pp endpoints alpha,beta. It cannot meet another B side1: either beta faces beta, or beta faces alpha; the third corner at that endpoint would be pp, but no homogeneous pp triple containing beta is legal. At any actual pure-alpha star the three incident B alpha corners each expose one side0 and one side1. There are three incident side1 halfedges. Since side1/side1 matching is impossible, all three must mate the three side0 halfedges. Thus all three radial seams are side0/side1 and all three B occurrences have the same chirality around the star. This is an actual whole-side constraint, not angle coverage alone.

At the opposite endpoint of every such side0/side1 seam the native corners are B0 mixed and beta pp, so it cannot be a pure-pp star. Consequently the three seams charged by a pure-alpha star are distinct, and no seam can be charged by a second pure-alpha star. Up to square-boundary discrepancies E>=3Y-O(R). Combined with3Y=2E+O(R), this proves

    Y=O(R), E=O(R), N_A=N_B+O(R).

No compactness step or pointwise disappearance of defects is inferred from these bounds. The final contradiction is also a boundary count.

## Remaining-corner capacity contradicts the whole middle q side

Only O(R) B pp vertices can have an incident B/B p seam, since E=O(R). At every other B pp vertex both neighboring tiles are A. The alpha120 vertex has one H and one L A corner. At the beta vertex, two A corners can fill the angle only if beta is120,120-2delta or120+2delta. The first is excluded. If beta is neither of the latter, every B beta vertex must be among the O(R) bad vertices, forcing N_B=O(R) and already contradicting N_A=N_B+O(R) and quadratic tile count.

Suppose beta120-2delta. Every good beta vertex then has two H corners. Let X_H count stars with one A H corner, one B mixed corner and one B qq corner. The good alpha vertices supply N_B-O(R) H corners and good beta vertices supply2N_B-O(R). These stars are distinct from the X_H stars. Since A supplies3N_A H corners,

    3N_A>=3N_B+X_H-O(R), so X_H=O(R).

For beta120+2delta, the identical argument with L gives X_L=O(R).

B's whole middle q side4 has two qq endpoints. It cannot meet any B q side: every B q side has at least one qq endpoint, so one endpoint of their whole shared seam would contain two qq corners and a third qq corner, a forbidden homogeneous qq star. Thus side4 always meets a whole A q side, whose two endpoints are one H and one L.

Every B qq corner is an endpoint of its middle q side4, already proved to meet A, so it has at least one A neighbor. Two A neighbors would share an A p seam, impossible. Thus it has exactly one A neighbor and one other B neighbor; cyclic binary parity forces that other B corner to be mixed. Therefore each such vertex has exactly one A mixed corner, one B qq corner and one B mixed corner. In particular the H endpoint of each B middle-q seam is an X_H star, and the L endpoint an X_L star. Such a star has only one B qq corner, so it can be charged by at most one B middle-q side. This is the required actual one-side endpoint capacity, not an assumed global frequency balance. It yields

    X_H>=N_B-O(R), X_L>=N_B-O(R).

Either beta branch consequently forces N_B=O(R), and again N_A=N_B+O(R) contradicts quadratic total tile count. This completes the pure-120 noncentral case.

The beta120 center cannot be added to this argument: a B middle p side can then connect pure pp stars at both endpoints, invalidating E>=3Y. Such center geometries are explicitly left unresolved by this lemma.

## Exact positive reduction and scope of the remaining target

If the nonhomogeneous arc is paired, common scaling and the reviewed length-swap when necessary put it in the complete paired-qq family. That theorem's two cones give both necessity and exact periodic sufficiency. The current argument adds the negative statement for all other nonhomogeneous arc data, including possible absence of actual homogeneous stars in an alleged tiling.

Together with the independently VALID all-no-homogeneous classification, a tileable A(delta)/binary-two-run pair can escape these reductions only if both arcs permit homogeneous stars, or exactly one arc permits homogeneous stars and both of that arc's native angles are120. This is a reduction of the stated hexagon family, not a resolution of those remaining cases or of the unrestricted two-prototile target.

Fresh review must check the actual-AA endpoint test, every incidence/boundary inequality, the side1/side1 impossibility with reflections, the unique charging of pure stars and middle-q endpoints, the essential center exclusion, omission of species, the exact length-swap transfer and composition with the paired-qq periodic theorem. This proof uses no finite solver decision and needs no new large star arrangement.

Fresh whole-proof review: [VALID review](../reviews/branching-hexagon-two-run-one-noncentral-homogeneous-arc-review.md). Its no-author-import checker audits 1,664 oriented native stars, seam bijections, all mirror assignments, resonance intersections, exact count elimination and the six length-swap edge identities.
