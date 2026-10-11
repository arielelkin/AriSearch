# Six residual Cairo targets after the ray459 periodic escape

Status: **VALID after fresh independent synthesis review.** This is a
necessary-domain reduction, not a tilability assertion for any residual metric.

## Statement and exact scope

Retain the four-distinct-arm, exactly-two-cross-arm-equality Cairo domain of
[the reviewed native reduction](partial-contact-cairo-two-cross-native-reduction.md).
All isometries, partial contacts and omission of a type remain allowed. The
[reviewed seven-target synthesis](partial-contact-cairo-mixed-quotient-seven-stratum-reduction.md)
and its complete signed native carrier map reduce a hypothetical aperiodic
pair in that domain to three dimension2 and four dimension1 targets.

The fresh independently VALID [ray459 theorem](partial-contact-cairo-mixed-quotient-fixed-ray459-periodic.md)
removes exactly the dimension1 target orbit7 flat459. Therefore any hypothetical
aperiodic pair in this precise domain must lie in one of the following six
necessary targets:

- dimension2: separated flat46, separated flat49, and orbit6 flat239 only on
  `sqrt(3)*a/4 < b < a/sqrt(3)` with native `a=Pa`, `b=Pb`;
- dimension1: orbit1 flat759, orbit6 flat906, and orbit7 flat575.

The separated flats retain their original full positive/private active-event
and actual-order domains. Nothing here extends those domains, excludes any
residual target, treats solver feasibility as existence, or covers internal
arm repetitions or three/four shared-arm patterns.

## Complete proof

The seven-target theorem is an independently reviewed necessity implication
covering every metric of the stated domain, not a sample enumeration. Its
seven named targets include orbit7 flat459. That stratum has kernel dimension1
and positive native Pa, so every one of its positive original-native metrics
is a common positive scale of its Pa=1 metric. The ray459 independent checker
reconstructs the raw native kernel and verifies all ten native side rows
coincide with the explicit P/Q sidewords of the sixteen-face theorem at that
normalization. It therefore identifies the entire positive ray, rather than
merely one representative chosen within a higher-dimensional cone.

The sixteen-face theorem proves a tiling by actual original convex P/Q copies
with nonzero rank2 lattice periods. Every common positive scale inherits both
periods, disjoint interiors and whole-plane coverage. Thus no metric of that
ray can be aperiodic under the original shape-only convention. Removing it
from the seven necessary targets gives precisely the displayed six. All
signed restrictions on the partially covered flat239 are unchanged. No
bounded failure or new contact relaxation enters the proof.

## Verification and dependencies

- [Seven-target whole-native map review](../reviews/partial-contact-cairo-mixed-quotient-seven-stratum-reduction-review.md).
- [Ray459 whole-native geometry and coverage review](../reviews/partial-contact-cairo-mixed-quotient-fixed-ray459-periodic-review.md).
- Independent ray identity/geometry checker:
  `conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_ray459_independent.py`.
- Independent preceding signed-map checker:
  `conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_lower_carriers_independent.py`.

The underlying exact certificates remain preserved without rewriting the
historical seven-target certificate. The original two-convex-polygon problem
and both parent mechanisms remain unresolved.

[Fresh independent six-target synthesis audit](../reviews/partial-contact-cairo-mixed-quotient-six-stratum-reduction-review.md) found no unresolved scope, native-map or whole-ray coverage defect.
