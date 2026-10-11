# Fresh independent review: optional Cairo subdivisions and rational seam obstructions

**Verdict: VALID for the sole Pa=Qd obstruction theorem, its original102 chamber models and weaker16 order-free models. The other17 order-free models also pass; completeness of their separate two-orbit flat reduction is independently audited by root.**

Reviewer: branching_hexagons, freshly assigned by root. Root developed the optional seam model, so this is a separate hostile audit. Reviewed the actual [sole e-adjacent shared-arm theorem](../lemmas/partial-contact-cairo-sole-adjacent-shared-arm-obstruction.md), native model producer, original102 dual certificate, separate16 order-free certificate, other17 driver/certificate, and the reviewed complete sole-Pa=Qd flat reduction. The [independent checker](verify_partial_contact_cairo_optional_seams_independent.py) imports no author module and executes no producer or solver.

## Every actual subdivision is included

The reviewed Cairo angle inventory permits only120^3,90^4 and90+90+180 at vertices, and at most one interior T on each native side. At a T its perpendicular90-to120 seam is whole. These facts apply to the original unrestricted tiling; no edge-to-edge limit is inserted.

Every whole arm and every whole fifth side remains a possible variant. A T-hosted fifth side has its length equal to a legal actual bank-event sum, so both ordered bank partitions are included. For an arm of length M, view it from its120 endpoint: its first opposing bank has a strictly shorter native arm length m. The two-T invariant gives equal event totals containing that actual bank and host slot. Hence m is among the model's shorter native bank candidates. The120-adjacent piece is length m and the residual piece has length M-m. Native arms0,2 have their120 endpoint at the start and arms1,3 at the end, so the recorded partition reversals are correct. All independent five-side choices are retained; impossible combinations only enlarge the model.

In the weaker order-free model every different native bank with a shared actual event total is included regardless of length order. Some resulting residuals are abstractly negative. Their lengths are never used as colors, so these extra states impose no asserted polygon geometry and only relax the necessary system. Every actual positive cut is still included. The abstract model remains finite on the whole relative flat and eliminates any need for arm-order chamber restrictions.

## Safe piece colors and reflected endpoints

At a genuine refined seam endpoint, a120 sector forces the other incident sectors to be120. It cannot meet a90 or180 sector, or occur inside an original side. Both copies of an actual shared piece therefore have the same number of120 endpoints. A piece with such an endpoint has length equal to a native bank arm or a whole fifth side; equality of those forms is fixed throughout the reviewed relative stratum. Residual pieces with zero120 endpoints deliberately discard length. This enlarges admissible pairings, including any accidental residual coincidences, rather than excluding them.

A piece's complete native partition and segment index identify both reference endpoints. Other cuts do not change that local signature. A corner uses its actual angle and adjacent piece IDs. Merging equal such corner states across tile variants is safe because each full variant retains its multiset of all corners. Original and reflected sector orientations reverse rays and reference endpoint flags as stated; rotations require no further states. The special90/90 shared-ray condition is necessary: its perpendicular seam is a whole native90-to120 arm on both tiles, having exactly one120 endpoint.

The independent checker derives native cut choices from normalized affine words for the original102 models and raw exact kernel forms for order-free models. It checks the16 original bases agree with the normalized parameter convention. All whole choices and ordered fifth-event banks are preserved. Instead of copying the author's angular DFS, it enumerates adjacency cycles for the three exact angular compositions120^3,90^4,90^2+180, with all cyclic placements and both orientations. Every retained model size and every rational dual inequality agrees.

## Actual two-ended cancellation and unrestricted global contradiction

At a physical shared piece the reference endpoint flags on both sides flip at its opposite endpoint. The sorted native-piece pair and flag parity remain identical, while the sign reverses. For identical IDs with opposite flags, the omitted feature is0 at both ends. Thus every actual interior segment cancels exactly; no chirality or unordered endpoint ambiguity remains.

The independently reconstructed dual gives nonnegative total corner-plus-seam charge on every permitted oriented star and corner charge at most-1 on every full optional variant of each species. All actual tiles and stars are included, so these inequalities apply to any original tiling. Either species can be absent; negative charge holds on each surviving tile variant individually.

Select original tiles contained in a radius-R disk. Fixed positive original areas and bounded diameters give Omega(R^2) selected tiles and only O(R) boundary tiles, hence O(R) incomplete refined corners and uncanceled piece endpoints. Each tile has at most ten refined corners and all finitely many rational charges are bounded. Summed tile charge is at most-Omega(R^2). Reorganizing by complete stars and canceling both ends of interior seams bounds that same charge below by-O(R), a contradiction. This argument requires neither frequency limits nor a periodicity hypothesis, and the abstract order-free phantom variants cause no difficulty: only actual variants are used in this sum.

## Completed independent certificate checks

The original102 records exactly cover every reviewed chamber of the16 surviving sole-Pa=Qd strata. Independent reconstruction verifies9146 star inequalities and2064 negative variant inequalities with Fraction arithmetic. The separate16 order-free records cover all16 relative flats;3532 star inequalities and624 negative variants pass. Thus either certificate route completes the actual scoped sole e-adjacent/e-adjacent shared-arm obstruction after the already reviewed complete event-flat reduction.

For the other two sole-shared-arm cases, all17 order-free records also pass, including their dimension3 flat. The checker verifies exact kernel rank and constraints, native closure, sole declared arm equality, positive kernel witnesses, complete abstract subdivision/star reconstruction,6819 rational star inequalities and730 negative variant inequalities. This validates the model and obstruction certificate on each supplied relative flat. It does not replace root's independent proof that those seventeen flats exhaust the other two cases; their eventual complete geometric classification must import that separate valid audit explicitly.

Completed readonly replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_optional_seams_independent.py

No substantive defect was found. No floating-point optimizer status is trusted, no finite patch failure is used, and no proposed geometric family kill is imported. The original adjacent-arm theorem is accepted within its exact four-distinct-arm sole Pa=Qd scope. Additional shared arm lengths, internal repeats, other angle families and the unrestricted two-convex-polygon problem remain outside this theorem.
