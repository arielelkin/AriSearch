# Complete pp-center / no-homogeneous-qq classification by actual contacts

Status: **VALID after fresh independent necessity and synthesis review.** The same-slot positive family is independently VALID; the cross-slot positive family has an independently VALID exact eight-face construction. The proof below derives shape conditions from actual tilings and whole-side endpoint roles, not from either fixed carrier's link equations.

## Exact scope and result

Fix0<delta<30, distinct positive lengths p,q, and A(delta) with lengths(p,q,p,q,p,q) and directions(0,60+delta,120,180+delta,240,300+delta). Its native angles are H=120+delta and L=120-delta. B is any strictly convex hexagon with lengths(p,p,p,q,q,q), pp native angles alpha=beta120 and qq native angles chi,psi in(0,180). Assume no multiset of three qq native angles, with repetition, sums360. Reflections are allowed.

Normalize q1 by common scaling. **Theorem. This pair is tileable if and only if, after optionally reflecting and reindexing B, it belongs to either the same-slot pp-center periodic family or the cross-slot pp-center periodic family. Consequently every tileable pair in this whole no-qq-homogeneous center-pp class has a doubly periodic tiling.**

The same-slot family has native angles

    (240+delta-psi,120,120,240-delta-chi,chi,psi),
    60-delta<chi<180, 60+delta<psi<180,
    exp(i delta)(exp(i chi)-1+exp(-i psi))=-2p.

The cross-slot family has native angles

    (240+delta-chi,120,120,240-delta-psi,chi,psi),
    60+delta<chi<180, 60-delta<psi<180,
    exp(i delta)(exp(i psi)-exp(i(psi-chi))+exp(-i chi))=-2p.

In both p>0, and retain p unequal to1 for the current negative-classification scope. Positive constructions themselves allow p1. The two family theorems supply actual periodic quotients for every retained parameter. The statement does not classify qq-homogeneous center-pp pairs, two noncentral homogeneous arcs, equal lengths or arbitrary A.

## Paired qq is already covered

If the unordered qq pair is{120-2delta,120+2delta}, the independently VALID complete paired-qq theorem gives the canonical center-pp first curve, p=cos(delta),chi120-2delta,psi120+2delta, up to B reflection. Its mixed angles are120-delta,120+delta and it belongs to the displayed same-slot family. Thus no further necessity argument is required for this branch.

For the remainder assume qq is not paired. No native qq angle120 is possible, because its threefold repetition would be a legal homogeneous qq star. Therefore actual AAp seams are impossible: the third qq filler angles at both endpoints of a whole shared A p side must either both be120 or form the paired low/high unordered set. This is the reviewed exact whole-side A endpoint test, including reflections.

## Actual q-middle contact and simultaneous mixed-corner saturation

Pass from any alleged unrestricted tiling to an actual defect-free trivalent ETE tiling using the independently reviewed hexagon limit theorem. Species omission is allowed. B's middle q side4 has qq endpoints chi,psi. It cannot meet any B q side, because every B q side has at least one qq endpoint. At that endpoint the whole seam would have two qq corners, and cyclic binary parity forces the third corner qq, yielding a forbidden homogeneous qq star. Hence **every B side4 meets a whole A q side**.

Every B qq corner is an endpoint of side4 and therefore has at least one A neighbor. Two A neighbors would share an A p seam, impossible. It has exactly one A neighbor and another B neighbor; binary parity forces that latter B corner mixed. Thus every B qq corner lies at a star with one A, one B qq and one B mixed corner.

In a square patch let N_B be the selected B count. Its qq corners number2N_B and its mixed corners also2N_B. The preceding qq stars consume one distinct B mixed corner each. Finite diameters, areas, native vertices and the reviewed uniform vertex separation give only O(R) boundary discrepancies. Consequently the number of B mixed corners in any other star is O(R). No limiting frequencies are invoked.

This sparse-defect statement produces a **new actual admitted tiling** where every B mixed corner lies at an A+Bqq+Bmixed star. For completeness, for each fixed radius n choose a sufficiently large square: O(R) bad mixed vertices have n-neighborhoods with area at most C(n+D)^2R, while the interior square has area Omega(R^2). Select a center outside those neighborhoods and away from the square boundary. Let n tend to infinity, translate these centers to the origin, and use compactness for the two fixed strictly convex shapes. The reviewed native vertex separation and whole-edge contact compactness preserve actual ETE trivalent stars; no side degenerates and no partial-contact defect is created. Every bounded disk in the limit avoids all bad mixed corners. This is simultaneous actual saturation, not an O(R)-to-pointwise assertion about the original tiling.

The limit cannot omit B: an A-only trivalent star has three mixed corners, impossible with distinct binary lengths. It cannot omit A when B occurs, because every B middle q side must meet A. Thus actual B tiles exist for the endpoint argument below.

## All p seams and the two endpoint roles of a whole middle p side

In the saturated tiling every B mixed corner has an A mixed and a B qq neighbor. The qq corner has only q rays; the p ray is therefore between A and B mixed corners. Hence B outer p sides0 and2 always meet A.

B middle p side1 must also meet A. If it met B, it could not meet that tile's outer p sides0 or2, already proved to meet A. It would meet side1. At either endpoint the A across the incident outer p side is still present, so the actual star would have one A mixed corner and two B pp corners. Such a star has exactly one mixed corner and is impossible by binary cyclic parity. Thus **all B p sides meet A**, and every B pp120 star consists of that B corner and one H and one L A corner. The two A neighbors share a q seam there.

Let T0 and T3 be the A corner angles at B's two mixed native vertices. The whole A p side across B middle p side1 has H and L at its two endpoints. At each pp120 endpoint the other A neighbor has the opposite type. Moving along B outer p sides0 and2 reverses the endpoint type once more, because every A p side also has one H and one L. Therefore

    (T0,T3)=(L,H) or(H,L).

This conclusion uses the same actual A across the complete middle p side, followed by the actual whole outer p sides. It does not assign independent endpoint fillers.

Write T3=120+sigma delta, T0=120-sigma delta with sigma in{+1,-1}. Every B outer q side3 or5 meets B: at its mixed endpoint the q ray is the ray to the B qq neighbor. Side4 meets A as already proved. Therefore choose any actual B q3 seam; its B mate is q3 or q5. Endpoint qq-to-qq matching would force a forbidden homogeneous qq star, so the two native endpoint roles must exchange mixed and qq. This exhausts the possible actual native-slot mates.

## Same-slot versus cross-slot geometry, without presupposing a carrier

**Same slot q3/q3.** At its mixed/qq endpoint the actual A filler is T3, giving

    B3+chi=240-sigma delta.

The total B angle sum with alpha=beta120 is B0+B3+chi+psi480, so

    B0+psi=240+sigma delta.

For sigma+ this is exactly the displayed same-slot angle list. Strict convexity yields its strict bounds on chi,psi. Rotate B so its p directions are0,60,120. The q directions forced by these native angles are

    60+delta+chi,240+delta,420+delta-psi.

Their chain sum and the actual closure of B give the same-slot complex relation stated in the theorem. This derives geometry from the actual q3 seam and whole-side A roles, not from quotient link equations.

**Cross slot q3/q5.** At the endpoint with B3 mixed and the other tile's psi qq corner, the actual filler is T3. Thus

    B3+psi=240-sigma delta,
    B0+chi=240+sigma delta

by total angle sum. For sigma+ this is the displayed cross-slot angle list. Its q directions are

    60+delta+psi,240+delta+psi-chi,420+delta-chi.

Actual B closure gives the cross-slot complex relation exactly. Strict mixed-angle bounds are chi>60+delta and psi>60-delta. A cross-slot seam uses opposite B chiralities to exchange mixed/qq endpoints; a same-slot seam uses equal chiralities. Neither possibility was discarded on an assumed mirror preference.

If sigma- occurs, reflect B and reindex native sides(2,1,0,5,4,3), native vertices(3,2,1,0,5,4). This swaps B0/B3 and chi/psi while leaving pp120/120 unchanged. The reflected geometry has sigma+ and falls into the corresponding displayed same or cross family. Reflected B is an allowed copy of the same prototile, so this prototype normalization leaves tileability unchanged. No reflection of the A prototype or delta sign change is needed.

For completeness, the other endpoint of a same-slot seam forces the neighboring B's sigma equal; the other endpoint of a cross-slot seam gives B0+chi240+sigma' delta, and total B angle sum forces sigma'=sigma. This is endpoint-role propagation along actual q chains. The shape-necessity proof needs only one actual seam and does not assert a global common translation, a unique chain axis, or that every tiling itself is periodic.

## Exact periodic sufficiency and remaining scope

Both derived sigma+ families have actual closed strictly convex polygons and independently checked fixed flat-torus quotients: four faces for same slots and eight faces with alternating B chirality for cross slots. Their deck lattices give a periodic tiling regardless of additional legal star types. Replacing B by its reflected copy preserves the protoset's admitted tilings. This proves sufficiency for all displayed shape conditions and closes the center-pp/no-qq-homogeneous case with both positive theorems and this necessity argument freshly independently reviewed.

Combining the reviewed no-homogeneous and one-noncentral-homogeneous reductions with this theorem, every tileable distinct-binary A(delta)/two-run B pair for which at least one B arc has no legal homogeneous triple has a periodic escape. Only the two-arc-homogeneous angle strata remain outside those reductions. This conclusion is limited to the displayed threefold A(delta) and binary B word; it is not a theorem about arbitrary two hexagons or the unrestricted target.

Fresh review must independently check square-boundary mixed-corner saturation and actual compactness, species omission, middle-q exclusion, every whole-side A endpoint role, the middle-p parity argument, same/cross slot exhaustiveness including reflections, native closure phases, B reflection normalization, and composition with both positive flat-cover theorems. The earlier fixed-carrier classification alone does not supply any of this necessity.

Fresh complete necessity and synthesis [review](../reviews/branching-hexagon-two-run-pp-center-no-qq-homogeneous-classification-review.md) is VALID. Its independent native checker also passes actual endpoint roles, all mirror cases and symbolic closure phases.
