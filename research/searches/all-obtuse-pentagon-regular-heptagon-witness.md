# Exact periodic escape for the all-obtuse pentagon/regular-heptagon family

**Completion:** fixed witness verification complete. The final producer replay
matches the retained certificate exactly. A fresh independently structured
checker has passed. The [analytic classification review](../reviews/all-obtuse-pentagon-regular-heptagon-review.md)
is valid separately.

## Mathematical question and domain

Do the exact four polygons Q0,Q1,P0,P1 and two periods u,v in the
[classification lemma](../lemmas/all-obtuse-pentagon-regular-heptagon-classification.md)
form a whole-plane tiling by one regular unit heptagon congruence class and
one genuine all-obtuse pentagon congruence class?

This is a single fixed algebraic construction, not a parameter search or
a bounded test of plane tilability. Its finite overlap domain is the
complete set of integer shifts derived from lattice-coordinate bounding
boxes, not a radius chosen experimentally. All 4*4 ordered motif pairs
are considered. For each pair and each lattice coordinate, the shift lies
between the exact ceiling of the first polygon's minimum minus the second
polygon's maximum and the exact floor of its maximum minus the second's
minimum. Only an identical motif at shift (0,0) is omitted. This yields 26
nontrivial ordered comparisons. Any other shift is excluded by disjoint
one-dimensional projection intervals, so completeness is proved.

The general classification uses actual infinite tilings and a translated
limit argument; it is analytic and is not inferred from this finite domain.

## Encoding, transformations, and constraints

Coordinates use AA/QQbar algebraic arithmetic with zeta=QQbar.zeta(14).
The retained JSON encodes a rational value exactly as a rational string;
each nonrational real value has its rational minimal polynomial and a
rational interval isolating precisely one real root. The producer checks
that every isolation interval actually has that property. Floating-point
approximations make no proof-relevant decision: converting the algebraic
value to RIF is used only to obtain candidate exact binary rational
interval endpoints, followed by exact root-isolation verification.

There are no solver variables, heuristic seeds, symmetry quotients, or
external matching rules. Q1 is the specified half-turn of Q0 and P1 the
specified half-turn of P0. The infinite witness uses all integer translations
of these four fixed copies. These placements are permitted isometries in
the unrestricted problem; no restriction is placed on other tilings.

The exact constraints checked are:

* Strict positive side-support inequalities for every motif polygon, which
  prove genuine strict convexity and counterclockwise orientation.
* Seven unit Q sides and native Q angle cosine cos(5pi/7).
* Four unit P sides, one private side of length
  L=sin(pi/7)/sin(3pi/14) in (0,1), and native P angle cosines for
  (9pi/14,4pi/7,4pi/7,4pi/7,9pi/14).
* Positive determinant of the two period vectors.
* Zero intersection area in all 26 complete translated-pair comparisons.
* Exact equality of the total motif area and the lattice covolume.

The producer uses exact convex polygon clipping. The fresh checker imports
no producer code and uses exact separating-axis tests for interior
overlap, then independently checks the full shift bounds, coordinate
encoding, side and angle data, congruences, and area equality.

Zero interior overlap plus exact area equality gives plane coverage by the
locally finite closed periodic union, as proved in the lemma. No generic
carrier packing or hole-filling assertion is trusted in that step.

## Software, resources, and reproducibility

Producer: [all_obtuse_pentagon_regular_heptagon_witness.py](all_obtuse_pentagon_regular_heptagon_witness.py).
Certificate: [all-obtuse-pentagon-regular-heptagon-witness.json](../certificates/all-obtuse-pentagon-regular-heptagon-witness.json).
Independent checker: [verify_all_obtuse_regular_heptagon_independent.py](../reviews/verify_all_obtuse_regular_heptagon_independent.py).

The final replay used Python 3.12.13 and SageMath 10.9 in the repository's
arisearch Conda environment. No other package or solver is required beyond
Sage and the standard library. There is no random seed, timeout, iteration
cap, or resource cutoff in the producer or checker. Both finite domains
completed normally; no timeout or failed run is described as an exclusion.
Assertions are proof relevant, so Python optimization must remain disabled.

Replay the producer (its stdout is the JSON certificate):

```text
conda run --no-capture-output -n arisearch python research/searches/all_obtuse_pentagon_regular_heptagon_witness.py
```

Replay the independent checker:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_all_obtuse_regular_heptagon_independent.py
```

A final producer replay was parsed as JSON and compared to the retained
certificate; they agree exactly, including the 26-comparison domain.

## Result and logical limits

The four motifs form an exact doubly periodic plane tiling by P*,Q. This is
a whole-plane witness, not bounded supportive evidence for extension. The
analytic lemma additionally proves that any strictly obtuse pentagon that
tiles with the regular unit heptagon must be congruent to P*.

This computation does not classify nonregular heptagons, acute/right-angle
pentagons, or other convex polygon pairs. It proves existence of one
periodic escape and makes no claim that every tiling of P*,Q is periodic.
It supplies no aperiodic protoset and resolves no global impossibility
question. No specific primary-literature novelty search has been completed
for this exact family, so no priority or novelty claim is attached.
