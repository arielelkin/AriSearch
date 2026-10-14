# Exact adversarial checks inside the construction loop

Date: 2026-10-14. This is an applied counterexample workflow, not a solution or a comprehensive polygon classifier. The [exact tool](construction-adversary-2026-10-14.py) accepts indexed cyclic polygons in Sage algebraic real coordinates. Its [control/application certificate](../certificates/construction-adversary-2026-10-14.json) is reconstructed by the command below.

## Checks before downstream construction

Native full-side attachment enumeration retains every equal-length source side, both determinant signs and both endpoint identifications before rejecting same-side interiors. Source vertex indexing is preserved; reflections may reverse winding. Exact clipping normalizes winding internally, and a separate separating-axis predicate checks convex interior overlap independently. Congruence includes both cyclic orientations.

For an explicit periodic motif, the verifier reconstructs every reversed native edge partner by solving exact lattice coordinates without a translation-radius cutoff. It checks shape congruence, genuine convexity, an involutive complete edge pairing, a nonsingular lattice and total representative area equal to absolute covolume. Complete oriented-boundary cancellation makes periodic integer multiplicity constant almost everywhere; its mean one excludes overlap and open gaps, and local finiteness of closed polygons excludes boundary gaps. An accepted witness is therefore a genuine periodic escape. The current interface handles full native edges, not general atomic subdivisions; existing separately reviewed partial-contact carriers remain available for their exact stated domains.

The finite omission search constructs triangle/quadrilateral motifs directly. For larger polygons it tries two copies related by native-side midpoint halfturn, taking each pair of native midpoint-translation gains as candidate lattice generators. This is a small sufficient witness domain: failed attempts return NO_WITNESS_IN_DOMAIN. It is neither complete pentagon recognition nor all torus sizes, and it does not establish aperiodicity or untileability. No quotient enlargement is authorized by a negative outcome.

An angle-palette obstruction is conclusive only when every full native star and every possible flat-host star has been exhausted and none exists. The perimeter prefilter for nonconvex all-hexagon parents is separately proved in the [root lemma](../lemmas/nonconvex-parent-hexagon-perimeter-bound.md) and [independent sector-count review](../reviews/construction-adversary-2026-10-14-hexagon-parent-review.md). It killed the actual all-hexagon iterable construction route before another packing search, causing a change to pentagonal atoms.

## Meaningful controls

The tool reconstructs the previously reviewed right-angle pentagon / regular-octagon three-representative carrier independently from its exact coordinates. Its full edge and area checks return PERIODIC_ESCAPE. A square omission motif is accepted, while a damaged lattice witness is rejected. A regular pentagon plus regular octagon is an analytically untileable control: their angles are 3pi/5 and 3pi/4, and neither a full nor a flat-host star can sum to 2pi or pi. Exact regular polygon construction verifies convexity. These controls distinguish witnessed periodicity, a genuine exhaustive angle obstruction, and an invalid proposed witness.

All four subject/clip winding combinations of the same actual square return its exact positive area. Overlapping and boundary-tangent squares are distinguished. The square's four equal native sides give eight opposite-side attachments, retaining both reflection hands. Thus aliases, winding and reflection are exercised by actual geometry rather than symbolic labels.

## Applied new pentagon/hexagon repair

The construction agent supplied exact P vertices
(0,0),(3,0),(4,sqrt3),(7/2,3sqrt3/2),(0,1/sqrt3),
and Q vertices
(0,0),(3,0),(3+1/sqrt6,1/sqrt6),(3+1/sqrt6,7/sqrt3+1/sqrt6),(sqrt2,7/sqrt3+1/sqrt6),(0,7/sqrt3+1/sqrt6-sqrt2).

Both are genuinely convex. The restricted omission search exhausts 30 P and 60 Q lattice-generator cases without a witness. These are inconclusive finite-domain negatives.

All eight indexed equal-length P/Q full-side attachments, including reflections, fail at a native endpoint. The palette is 90,120,135 degrees; every full star containing a P120 corner must be PPP120^3. Every P side has a P120 endpoint, so an entire native P side cannot match an entire native Q side in any admitted plane tiling. The certificate records each failure explicitly. This excludes those full seams and hence a construction using an actual mixed full-native two-child parent occurrence. It does not exclude partial P/Q contacts, the original pair as a whole, or changed parent seams. A geometrically disjoint two-tile union alone is not a candidate infinite covering.

## Applied P5/Q14 track

The separate [independent checker](../reviews/construction-adversary-2026-10-14-p5q14-independent.py) reconstructs the exact P, all binary Q14 words, native endpoint cycles and mandatory alpha dimers. It also attacks the fixed one-Q translation-orbit periodic cell using mandatory u-to-v bridges. Its final counts and verdict are preserved in the [independent review](../reviews/contact-pentagon-5pi7-q14-independent-hostile-review.md), rather than inferred from the author's producer output. All364 geometrically disjoint completions fail a necessary translated-Q bridge in that one-Q model; no lattice stage is reached. A separate [same-patch palette audit](../reviews/construction-adversary-2026-10-14-p5q14-palette.py) rejects336 for forbidden T contacts, leaving28 with no T or native-multiset obstruction. The28 pass states remain finite necessary local data, not a plane cover. Other periodic cells and plane existence remain unresolved.

## Replay

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/construction-adversary-2026-10-14.py --check research/certificates/construction-adversary-2026-10-14.json
```

No random seed, solver timeout, sampled metric grid, larger patch depth or unrestricted impossibility claim is used. The tool was applied to both live construction tracks; it is not merely new infrastructure.
