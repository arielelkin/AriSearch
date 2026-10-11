# Fresh original-geometry review of the isolated-cross Cairo ray459

**Verdict: VALID.** The reviewer did not author the witness, native proposal,
development routine, or retained certificates. This review covers the complete
positive scaling ray in the [scoped lemma](../lemmas/partial-contact-cairo-mixed-quotient-fixed-ray459-periodic.md).

The exact claim is existence of a doubly periodic plane tiling by the two
original unmarked convex pentagons at orbit7 flat459, for every common positive
scale. It makes no claim about the other necessary Cairo strata or unrestricted
two-polygon target.

The standalone checker imports no producer, seam-balance model, quotient
search, or development module. It treats both certificates as untrusted input.
It defines the native P/Q sides from the lemma, independently compares all ten
normalized side rows with the raw one-dimensional event-flat kernel, and checks
both native closures, all positive sides, exact side lengths and all thirty
strict nonincident support inequalities. The original five angles are
120,90,120,90,120; these also follow from the independently fixed native edge
directions. Reflection is permitted and contributes a negative frame sign,
without changing the original shapes.

For every original face it removes subdivision vertices and requires the five
remaining vertices to equal the original native coordinates exactly. Each
actual atomic piece has positive length, lies on the correct original side,
has the correct direction, and all pieces sum to that original side. Thus no
negative residual, artificial tile, or interior segment is used.

The checker rebuilds the full endpoint-flag gluing, including preservation and
reversal separately. Every flag has exactly one partner; all sixteen vertex
links are individual circular cycles, with angle inventory either 120 cubed or
90+90+180. Angle totals alone are not used as a surface certificate.

It audits the supplied sixteen original placements directly, rather than
calling the author's development algorithm. Each exact frame is orthogonal
with determinant +1 or -1. Each of the ninety-six directed atomic transitions
has both endpoints at identical exact coordinates modulo the displayed lattice,
opposite CCW boundary direction, a unique inverse transition and integer period
coordinates. The lifted face graph is connected. The period determinant is
nonzero and the transition shift coordinates generate all Z², including the
two signed coordinate basis vectors. Twelve original P areas plus four Q areas
equal the positive lattice covolume exactly.

The finite proposal and circular links do not alone prove plane existence.
The decisive additional calculation is cancellation of all original CCW
boundary atoms, combined with exact area/covolume=1. For the locally finite
lattice translates of the sixteen bounded convex faces, the sum of interior
indicators has zero distributional derivative: opposite atomic boundaries
cancel, including reflected occurrences. Hence its multiplicity is constant
almost everywhere on the connected plane. Integration over a fundamental
parallelogram gives that constant as one. Any overlap of interiors has an open
subset of multiplicity at least two. Local finiteness makes the closed-face
union closed; an uncovered point has an open uncovered neighborhood. Both
contradict the almost-everywhere value one. This proves unrestricted plane
coverage and disjoint interiors, with the displayed nonzero translations.

The same argument can be stated using generic paths: after accounting for
coincident atoms, every boundary crossing has net jump zero, and paths can
avoid the locally finite exceptional endpoints/intersections. No unexplained
finite-to-infinite inference, imposed matching rule, or original-tiling
periodicity assumption is involved. Common positive scaling multiplies every
coordinate and period by the same number and every area by its square, so
the entire ray follows without fixture extrapolation in a larger domain.

No mathematical defect was found. The sixteen-face witness is used directly;
the earlier four-face parity obstruction and capped matching exploration are
irrelevant to existence. The raw source really is one-dimensional, so the
normalized metric exhausts the positive ray. The checker does not certify
that every tiling on this ray is periodic; one explicit periodic tiling already
excludes aperiodicity. Other metrics/rays remain outside its scope.

Replay, with no certificate writes:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_ray459_independent.py

Observed result: PASS exact native ray, thirty strict supports, every positive
cut, sixteen circular links, sixteen original faces, ninety-six endpoint
transitions/forty-eight inverse seams, primitive rank-two periods and exact
area/covolume. SageMath exact arithmetic over Q(sqrt3); no numerical geometry.

The conservative seven-target inventory may therefore remove the whole
ray459, leaving six targets. This update requires only this scoped existence
result; no surviving target is asserted tileable or untileable.
