# Independent hostile review: one off-normal angle fixture

Date: 2026-10-15. **Verdict: VALID for the relaxed angle witness and for its exact coordinate-fixture rejection.** The rejected object is precisely the retained base6/head42, half-apex120/12 fixture. This review does not close the off-normal construction component.

I read [the relaxed H-angle gate and witness](../searches/offnormal-cap-h-angle-gate-2026-10-15.md), its Fraction checker and JSON, and [the exact geometry rejection](../searches/offnormal-one-fixture-geometry-2026-10-15.md), producer and JSON. I wrote a separate [independent verifier](offnormal-one-fixture-independent-2026-10-15.py) that imports no producer and calls no solver. It independently reconstructs all actual arrow contexts and the geometry in exact complex QQbar coordinates.

## Relaxed angle witness is valid within its stated scope

The retained prototype angles are (36,156,144,156,72,156), summing to 720, all strict. Both marks have donor base angles 6/42 and half-apex angles 120/12. Each mark's half-apex sum is 132=180-6-42. The ordered external cut pairs are (156,144) at tails and (156,36) at heads. Their sums are 180 plus the corresponding original half-apex angle, and each cut angle is strictly larger than that original angle and smaller than 180.

For both source species, both donor parities, both receiving edges and both endpoints, I independently reconstruct the source angle plus incoming base minus outgoing base using actual arrow endpoint roles. The verifier checks all sixteen declared contexts exactly once, computes the supplied dihedral alias, and verifies its first three angles, its split-point angle 156, and the positive original internal donor angle. It checks the last two cut angles individually and their required sum. All sixteen pass exact Fraction arithmetic. No geometric closure or common ray-fraction realization is implied by this positive relaxed gate.

## Actual arrows and off-normal reconstruction

Let z=exp(pi*i/30), exactly the sixtieth root of unity. All points use QQbar, with real comparisons in AA. Set h=1/(cot6+cot42), u=h*cot6 and m=u+h*cot54. Exact inequalities give 0<u<m<1 and h>0. On the standard unit edge from 0 to 1, the apex is u+i*h and the split is m. Exact dot/cross cotangents verify the donor base at its tail is 6, the tail half-apex is 120, and the complementary head half-apex is 12. Thus this fixture realizes the intended off-normal split angles rather than accidentally retaining the old normal foot.

For rhomb angle sigma=36 or72, use complex vertices (0,1,1+exp(i*sigma),exp(i*sigma)). The boundary orientation is counterclockwise. For boundary edge vector e and ACTUAL arrow vector a, an internal donor node is tail+u*a+i*h*e, whereas an incoming external node is tail+u*a-i*h*e. The normal uses the boundary edge e, not the arrow vector a. This distinction is essential on reversed arrows. The split is tail+m*a.

The source arrows are checked as thin (0->1,X),(2->1,X),(2->3,Y),(0->3,Y), and thick (0->1,X),(1->2,Y),(3->2,Y),(0->3,X). Both marks use the same numerical fixture parameters. All internal and external nodes are therefore determined consistently from their actual source edges; the verifier does not independently adjust the adjacent internal nodes to fit a receiving quad.

## Source partition and receiving outputs

For each of the four species/parity cases the independent checker constructs the two internal donor triangles and two complementary receiving quadrilaterals. It verifies strict supporting-line inequalities for every cell, that all vertices lie in the closed source rhomb, pairwise non-overlap using exact separating axes, and equality of the sum of cell shoelace areas to the rhomb area. These finite closed convex cells consequently cover the source: an omitted interior open set would have positive area, and closedness then covers the boundary too. All four source partitions pass. The central receiving triangles (M,q,p) are also strict.

The assembled endpoint quads are reconstructed in native order as (endpoint, external apex, split M, adjacent internal node). Exact supporting-line checks give eight strict convex and eight nonconvex quads. Every retained geometry record, turn-sign list, minor-angle grid value, required internal angle, and strict-quad internal-angle comparison is checked independently. The sixteen geometry context keys are verified complete and unique.

## Small exact rejection certificate

For thin sigma36, donor parity0, receiver BC, endpoint B, the actual arrow on BC points C->B. With c=cos36,s=sin36 the internal donor on AB is p=(u,h), and the external point and split are

    t=B+(1-u)(c,s)+h(s,-c),
    M=B+(1-m)(c,s).

The quad is (B,t,M,p). Direct independent complex-coordinate determinants give its consecutive turn signs (+,-,+,+). Specifically the turn at t equals h*(1-m)>0, while the turn at M equals

    Delta=h*(1-m)*(1+c)+s*((u-m)*(1-u)-h*h).

I verify equality of this written expression to the actual determinant and the strict algebraic isolating interval

    -3254/1000000 < Delta < -3253/1000000 < 0.

Opposite turn signs exclude convexity. This one failed receiving quad already rejects the fixture before later cap cuts or congruence aliases. Its M corner is retained by the prescribed receiving output words, so subsequent truncations at donor-node corners do not remove the failed corner.

A separate strict-convex mismatch also holds. For thick parity0, receiver DA, endpoint A, the exact interior angle at M is 108, while the abstract H-angle assignment requires 156. The independent checker confirms this quad is strict and compares exact cotangents. Cotangent is injective on (0,180), so this is a genuine angle mismatch. For nonconvex quads the calculation deliberately refers only to the minor angle between rays and does not confuse it with a reflex interior angle.

## Replay, defects sought and scope

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/offnormal-one-fixture-independent-2026-10-15.py

Result: PASS sixteen relaxed Fraction angle contexts; four exact valid source partitions; eight strict and eight nonconvex receiving quads; explicit negative-turn isolating interval; strict M=108 mismatch. No numerical tolerance, sampled angle decision, solver UNSAT inference or parameter search enters this verification. The complex-coordinate implementation is independent of the producer's Cartesian-coordinate functions and compares all retained records.

I attacked reversed-arrow normals, tail/head swaps, improper reflection handling, confusing the split with the normal foot, source overlaps, invalid source cells, a mistaken determinant formula, and treating minor ray angles as reflex polygon angles. The exact reconstruction and scope survive these attacks. No author files or certificates were changed.

Both conclusions coexist without contradiction: the necessary H-angle system has its stated SAT witness, and the selected consistent coordinate reconstruction fails strict output convexity and further angle matching. Only this fixture is falsified. Other off-normal angles, changed source-local rules or context-dependent cuts remain outside the rejection. No two-class geometric candidate or unrestricted impossibility theorem follows.
