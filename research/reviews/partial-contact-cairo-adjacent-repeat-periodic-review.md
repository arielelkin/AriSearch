# Fresh hostile review of the r=1 adjacent-repeat periodic witness

**Reviewer:** branching_hexagons, freshly assigned by root. This reviewer did not construct the witness or develop the numerical proposal search. Before reading the extracted author proof, the reviewer built an independent raw-native-geometry verifier using the motif supplied by root. The actual extracted lemma, producer and retained certificate were then freshly inspected. No author code was executed or imported.

**Artifact:** [adjacent-repeat periodic witness](../lemmas/partial-contact-cairo-adjacent-repeat-periodic.md).
**Verdict:** **VALID.** The exact construction is a full admitted doubly periodic monohedral tiling, not a finite patch or existence inference from the earlier conditional cluster reduction. No substantive defect or required repair was found.

## Geometry and native congruence

In the positive Q(sqrt3) embedding the reviewer independently reconstructs native P=(1,1,c,d,2), Q=(d,c,1,1,2), with c=(3sqrt3-1)/2,d=(sqrt3-1)/2, from their original directed-edge convention. Closure, positive lengths and strict support determinants hold. The raw quadrant pentagon has area9/4 and is strictly convex.

Its native congruence is checked in both directions: rotation240 followed by translation P3 sends the quadrant vertices to P3,P4,P0,P1,P2; a reflection with translation Q1 sends them to Q1,Q0,Q4,Q3,Q2. The actual author's Q reflection formula F30*(P_i-P4), with i=4,3,2,1,0, was separately checked directly against the independently reconstructed Q vertices. Thus P,Q are the same unmarked congruence class, and every primitive motif face is an allowed P copy. All reflected quadrants and the second quarter-turned cluster are allowed isometries. No classification theorem or forced-cluster theorem is needed for this positive construction.

The author uses rotationminus90 for the second cluster, while the independent checker initially uses plus90. These give exactly the same cluster and same four primitive polygon point sets: S(1) has central180 symmetry, so the two quarter turns differ by an intrinsic symmetry. The retained certificate's eight actual polygon point sets are compared exactly to the independent eight-face motif and match. The periods and native side words also match the certificate exactly.

## Complete independent lattice audit

The lattice generators are u=(sqrt3,-sqrt3), v=(3sqrt3,3sqrt3); their determinant is18. All eight motif pentagons have area9/4, giving total area18.

To avoid inheriting the author's84-pair pruning logic, the reviewer uses a larger, independently proved complete domain. Across the entire motif the x-coordinate span is3sqrt3 and the y span is5sqrt3+1/2<6sqrt3. If any motif faces overlap after translation m*u+n*v, their coordinate intervals must meet, so

    |m+3n|<=3, |-m+3n|<6.

Adding/subtracting bounds gives |6n|<9 and |2m|<9. Integer indices therefore obey |n|<=1 and |m|<=4. Every omitted lattice translate is excluded rigorously by these coordinate inequalities, irrespective of its species or face index.

The independent checker enumerates all27 lattice indices in this rectangle and all64 ordered original-pentagon pairs, excluding only the eight identical zero-shift occurrences. This gives1720 complete comparisons. Exact half-plane clipping constructs every convex intersection polygon. Each has area zero, proving no pair has overlapping interiors. This includes motif pairs, self translations and all lattice copies. The author's narrower inverse-lattice interval bound is also correct: an invertible affine map preserves intersection, transformed extrema of a convex polygon occur at its vertices, and the stated integer interval formulas exhaust every candidate translate. Its84 relevant comparisons are contained in the independently tested domain. The larger checker does not trust the author's separating-axis answers.

## Whole-plane coverage and actual periods

Interior disjointness gives periodic multiplicity at most1 almost everywhere. Unfolding the finite motif over a fundamental cell gives mean multiplicity equal to total polygon area divided by lattice covolume, namely1. Hence multiplicity is1 almost everywhere. The union of all translated closed faces is locally finite because the lattice is discrete and faces are fixed and bounded; it is therefore closed. An uncovered point would have an uncovered open neighborhood of positive area, contradicting full almost-everywhere multiplicity. Thus the construction covers the entire plane with disjoint interiors.

Both lattice vectors translate every primitive motif occurrence to another occurrence, so they are actual nonzero independent periods of the original pentagon tiling. No canonical subdivision needs to be inferred at r=1, where private-arm assumptions have changed. The subdivision is directly part of the explicit construction.

The normalized closure uniquely fixes c,d when a=b=1,e=2, so scaling gives the stated sufficiency for a=b,e=2a. This does not assert anything about arbitrary Cairo metrics or arbitrary convex-polygon pairs.

## Independent replay

[Independent checker](verify_partial_contact_cairo_single_shared_r1_periodic_independent.py) imports no author module. It uses exact Q(sqrt3), an explicit positive algebraic embedding, native vertex/isometry identities, convex half-plane clipping, exact complete lattice bounds, and certificate coordinate comparisons. It uses no solver, random proposal, numerical tolerance or bounded-extension inference.

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_single_shared_r1_periodic_independent.py

Completed output: PASS, with1720 exact nonidentical lattice-pair comparisons and motif area18 equal to covolume18. The numerical MILP proposal record is not a logical dependency of the verification or this review.

## Scope

This establishes the positive periodic escape at the r=1 metric and its scalings. Together with separately reviewed negative arguments for the other metrics, it can close the sole-shared family; those negative arguments remain separate dependencies. This positive witness alone does not resolve the original two-convex-polygon problem.
