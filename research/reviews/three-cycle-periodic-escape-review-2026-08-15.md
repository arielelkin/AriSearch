# Hostile review: three-cycle periodic escape

**Reviewer:** independent subagent `review_three_cycle`

**Artifact reviewed:**
`research/counterexamples/three-simple-cycle-hexagon-periodic-escape.md` as
initially extracted on 2026-08-15.

## Exact claim reviewed

Every tileable three-simple-cycle hexagon carrier satisfying the stated
edge-to-edge, trivalence, unique-length, and common-endpoint hypotheses has a
doubly periodic tiling.

## Assumptions checked and attacks attempted

The review attacked repeated incident labels, repeated cycle types, two
sectors of one cycle type at a vertex, extra active graph edges, the
`K_3,3` conclusion, the periodic honeycomb cover, rotational or glide
holonomy, overlap after development, and reflection compatibility.

## Defects found

No invalidating counterexample was found. The phrase “conventional incidence
coordinates” left the decisive cover unverifiable from the artifact alone.
The flat-torus development was also too compressed: orientability,
completeness, absence of cone singularities, and translational deck holonomy
needed to be stated.

## Repair proposed

Define faces `F(m,n)` and vertices `U(m,n),D(m,n)` with all three incidences,
then check the three matching directions explicitly. State that the periodic
quotient is an orientable compact flat torus and develop its universal cover.

## Remaining uncertainty

The theorem remains conditional on its carrier hypotheses; it does not show
that an arbitrary geometric construction forces them. The repaired
coordinate and development argument requires fresh independent review.

## Verdict

**Valid with minor exposition repairs**, but not yet eligible for the status
**Adversarially reviewed** until those repairs receive fresh review.
