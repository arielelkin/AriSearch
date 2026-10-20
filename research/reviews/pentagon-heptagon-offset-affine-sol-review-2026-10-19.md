# Independent Sol hostile review: offset-affine pairwise gate

Verdict: **valid**, for the explicitly declared independent-side product relaxation, conservative scalar transfers, and equivariance under all plane isometries including reflection. The gate is infeasible. This verdict establishes neither mixed plane nontilability nor failure of discharging on jointly realizable geometric states. The author clarified the excluded point-contact convention during review; the revised text has been checked.

## Claim and sources checked

Reviewed `research/searches/pentagon-heptagon-offset-affine-gate-2026-10-19.md` and its adjacent Python script; the original `pentagon-heptagon-astra-first-gate-2026-10-19.md` and `pentagon-heptagon-corner-transport-blocker-2026-10-19.md`; and `research-protocol.md`, especially sections 5, 8, 11, 16 and 19. The fixed sources specify strictly convex unit-incircle P with angles (60,105,115,125,135), Q with angles (150,150,120,120,120,120,120), and allowed reflected copies. The conclusion below does not depend on exact cyclotomic side lengths beyond their positivity.

## Attacks on completeness and labels

For disjoint strictly convex polygon interiors, positive-length intersection lies on a common supporting line, and each polygon exposes exactly one native side there. Once the reference side is [0,L] with interior above, a chosen partner side has interval [t,t+M] below it; determinant and native endpoint labels determine its orientation. Hence -M<t<L is exactly the positive-contact domain. Splitting at 0 and L-M, with equality cells, accounts for containment, stagger, equal endpoints and full coincidence. Neither a second continuous rotation parameter nor a hidden reflected endpoint identification is missing. Some nominal endpoint-order choices can be redundant or incompatible with a specified determinant; they must be understood as actual realizable label placements, not independent arbitrary permutations. The reflected witness is an actual placement under either description.

This is completeness only for two tiles. It supplies no simultaneous nonoverlap of neighbors, corner completion, side partition compatibility, or extendibility. Those omissions are explicit in the declared product relaxation and cannot be silently removed during its falsification.

## Independent exchange-fixed contact proof

Let X be any labeled copy of either polygon and e any native side. Let r be reflection in the supporting line of e. The pair (X,rX) has disjoint interiors, identical full seam, relative determinant -1 and the same native side index on both copies. The two endpoint labels occupy identical spatial positions because r fixes the seam pointwise. Reflection maps the ordered receiver/partner pair (X,rX) to (rX,X). Thus an incoming scalar transfer F obeys

    F(rX,X)=F(X,rX)    by reflection equivariance,
    F(rX,X)=-F(X,rX)   by conservativity.

Over the rationals or reals this gives F=0. Exchanging roots does not switch to an unrelated coefficient table: the same indexed rooted geometry is recovered by the reflection. A pseudoscalar, an absolute chirality dependent rule, an absolute-position rule, or an externally marked orientation could evade this equality, but each changes the stated isometry-equivariant scalar gate. Merely permitting reflected tile copies does not alone imply reflection equivariance; the latter hypothesis is essential and is explicitly used by the source proof.

At this seam t=0, M=L and h=L, giving a+cL=0 exactly. No rationality of L is required. Allowing independent coefficients on endpoint cells, or increasing their polynomial degree, does not evade the fixed-contact argument.

## Independent-side contradiction and geometry attack

Choose the above full reflected seam independently for each native side of a root tile. Every side is covered and every incoming contribution is zero. This is an admitted formal product state, giving net 0 against the required lower bound 1 for P and also Q. Either species alone suffices to falsify universal feasibility. No LP, endpoint limit calculation or complete enumeration is required once this single state is admitted.

This is deliberately not a corona. At a reflected seam endpoint carrying P's 115-degree corner, the two copies leave 130 degrees. No nonnegative sum of the native angle palette fills 130: one corner cannot equal 130; two corners of minimum 60 either give 120 or at least 165; three exceed 130. A flat sector also exceeds the remainder. Consequently even that individual seam cannot appear with such an endpoint in a completed tiling. This spuriousness strengthens the scope warning: an infeasible sufficient relaxation does not imply infeasibility of the smaller geometric state set.

## Defects and verifier limits

The original endpoint sentence could suggest that zero point-contact flux follows from the displayed formula. It does not: h=0 there gives affine limits a-bM and a+bL. The author repaired this by explicitly declaring zero point-contact transfers separately and disclaiming vanishing one-sided limits. I reread the revised lines 34–37 and accept the clarification. The full-contact contradiction at t=0 was unaffected.

The Python program replays exact arithmetic for 2F=0 and sums five or seven zeros. It does not mechanically verify geometric completeness, label action, coefficient identities or global tiling compatibility. Its claims are justified by the written proof, not independent discovery of those hypotheses by the program. Replay completed successfully with assertions enabled:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-heptagon-offset-affine-gate-2026-10-19.py

I did not edit author artifacts. The author made the endpoint clarification described above, which I independently checked.

## Boundary argument and final scope

The conditional boundary-versus-area argument is sound for a finite collection of positive-area compact prototiles, bounded conservative local flux and a true positive uniform surplus on every jointly realizable tile state. Contact neighbors fit in a uniformly bounded neighborhood; disjoint positive-area interiors bound their number. Tiles meeting the disk boundary fit in a fixed-width annulus, giving O(R) uncancelled flux versus order R squared demanded surplus. The product gate never supplies that positive surplus, so this conditional argument yields no plane contradiction here.

The exact verdict is valid scoped falsification of the declared product relaxation, with the endpoint clarification independently rechecked and no unresolved defect. Mixed tiling existence remains unresolved. Rules exploiting simultaneous angular/contact constraints, different initial charges, extra corner terms or other discharging constructions are not excluded. Under protocol section 5 this particular relaxation should stop unless a materially different joint domain or mechanism is supplied; protocol section 19 does not turn this local failure into a solution or authorize a global stop.
