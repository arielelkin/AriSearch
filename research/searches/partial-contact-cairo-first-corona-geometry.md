# Bounded Cairo cycle: exact first-corona geometry

**Status: VALID for the exact finite relaxed-collar witnesses after [fresh independent hostile review](../reviews/partial-contact-cairo-first-corona-geometry-review.md). No plane extension, parent-family closure or new global forcing mechanism was found.** The separate ray459 periodic witness has a fresh VALID
whole-geometry review and removes that whole ray from the seven-target inventory.

## Mathematical question and finite object

The seam balance relaxation ignores geometric interactions between different
neighbors of the same original tile. Does exact interior-disjointness of a
first ring already eliminate any of the complete optional-cut variants in
the remaining Cairo domains?

Fix one retained native metric with exact side forms over Q(sqrt3), and let V
be the complete optional-cut variant inventory in the reviewed necessary
residual-color model. An element of V is one original convex P or Q, with
zero or one allowed geometric contact cut on each of its five native sides.
Subdividing a side does not create another tile. Its atomic boundary pieces
carry formal length vectors, number of native120 endpoints, native direction,
and actual endpoint angles. Formal lengths are compared before specializing
to the exact metric; coincident lengths at a fixture are not substituted for
identities of the full kernel forms.

For a central v in V, the finite collar relaxation assigns to every atomic
boundary interval an actual isometric copy of original P or Q. The copy is
obtained by aligning a same-color whole atom of some u in V, allowing both
endpoint maps and every reflection. Its CCW boundary orientation opposes that
of the central tile. The native edge directions differ by multiples of30
degrees, so the finite exact frame/sign enumeration is exhaustive for such
an atomic contact. At both endpoints the two corner angles must fit some
Cairo star: both120 or both non120, with sum at most360. Two selected original
neighbors must have disjoint interiors unless they are the identical original
occurrence. Native rotational/reflective encodings of an identical occurrence
are merged by its exact original polygon vertex set. Equal occurrences may
cover several atomic intervals of the central tile.

The collar **ignores** vertex-only neighbors, any extension beyond this ring,
full angle coverage around vertices and consistency of different optional
subdivision choices for repeated selection of the same original neighbor.
These omissions enlarge the actual tiling possibilities. Therefore a complete
failure could be a necessary geometric obstruction after independently
auditing the underlying contact inventory. A positive assignment proves only
feasibility of this finite relaxation, even if all central variants have one.

## Complete bounded pass

Each variant's assignment CSP has at most100,000 recursive nodes. At every
step the smallest remaining candidate domain is selected. Pair compatibility
is decided by exact separating axes from all original pentagon edges; touching
is allowed, but intersecting interiors are excluded. Every decision is over
Q(sqrt3). Candidate placement domains contain every same-form/color neighbor
atom with both endpoint maps; no fixed motif frequency, topology, periodic
quotient size, symmetry reduction or original tiling periodicity is assumed.
No seed, numeric geometry, numerical equality or extra prototile is used.

| Metric tested | Central variants | Distinct possible neighbor placements | Exact pair tests | Recursive nodes | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| orbit1 flat759, chamber0 |22|49|141|169|22 witnesses |
| orbit6 flat906, chamber0 |50|58|223|417|50 witnesses |
| orbit7 flat575, chamber0 |42|49|189|343|42 witnesses |
| low orbit6 flat239, chamber7 fixture |10|34|98|73|10 witnesses |
| separated flat46, chamber0 fixture |88|77|352|808|88 witnesses |
| separated flat49, chamber0 fixture |152|84|354|1368|152 witnesses |
| accepted periodic ray459, chamber0 control |27|61|227|210|27 witnesses |

All391 tested variants have exact mutually nonoverlapping edge-neighbor
assignments, with3,388 total recursive nodes and no node cap reached. The
experiment yields **zero new exclusions**. It is a completed finite positive
result, not an UNSAT computation and not evidence that the unknown metrics
tile. The control passes as required; this prevents an immediate inconsistency
with the accepted sixteen-original-face ray459 periodic tiling.

The fixed-ray results scale throughout their respective positive rays:
every coordinate is homogeneous, formal piece equality is unchanged, and
all separating inequalities scale by a positive square. The dimension2
results apply only to the retained exact chamber fixture, whose entire kernel
point is in its certificate. For low239 the checker explicitly verifies
sqrt3*Pa/4<Pb<Pa/sqrt3. No overlap-sign arrangement in the entire dimension2
domain was enumerated, so no chamber-wide or whole-stratum result is claimed.

## Retained evidence and replay

The producer is `partial-contact-cairo-first-corona-geometry.py`. Its input
is `research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json`.
The source inventory is reconstructed from the established optional-cut model;
the complicated model is **not** trusted by the separate assignment checker.

Seven certificates named
`research/certificates/partial-contact-cairo-first-corona-PATTERN-flatID.json`
retain all native forms, exact metric point, full formal atomic variant
inventory, original native polygons, every candidate geometric placement,
complete candidate domains, successful assignments and recursion counts.
The independent-style standalone checker imports no producer/model module.
It rebuilds all optional cuts from original bank sums, requires exact exhaustive
variant equality, verifies positive lengths/native closure and all chosen
atom endpoint alignments, and tests all neighbor interior intersections with
an independently stated exact projection-interval separating-axis predicate.

Replay the read-only retained witnesses:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_first_corona_independent.py

Observed: PASS all391 complete finite assignments. This checker was written by
the experiment author; the [fresh independent review](../reviews/partial-contact-cairo-first-corona-geometry-review.md) audits its exact predicates and witnesses. An additional fresh-reviewer checker, `research/reviews/verify_partial_contact_cairo_first_corona_geometry_extra.py`, checks strict native supports, positive pieces, actual/formal length equivalence and the finite count/scope metadata.

Reproduce one case, replacing the pattern/flat/chamber with the rows above:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-first-corona-geometry.py --pattern orbit6 --flat 239 --chamber 7 --max-nodes 100000 --output research/certificates/partial-contact-cairo-first-corona-orbit6-flat239.json

The other rows use chamber0. Python3.12.13/SageMath10.9, exact quadratic
field arithmetic. All computation files and witnesses are retained. No
long-running search remains.

## Earlier quotient records remain strictly bounded

The strongest retained original quotient negatives were checked for their
actual status; no negative search was enlarged in this cycle:

| Selected original-face multiset | Completion | Visited nodes | Completed pairings |
| --- | --- | ---: | ---: |
| ray759,10 faces |1,000,000-node resource limit|1,000,004|0|
| ray906,10 faces |entire selected multiset exhausted|8,995|0|
| ray575,8 faces |entire selected multiset exhausted|909,775|0|
| low239,20 faces |2,000,000-node resource limit|2,000,008|0|
| separated46,6 faces |entire selected multiset exhausted|65|0|
| separated49,6 faces |entire selected multiset exhausted|286|0|

The exact native variants and pairing domain are in the corresponding
`partial-contact-cairo-mixed-quotient-*-faces.json` certificates. The tiny
overrun in counted nodes is the recorded recursive cutoff behavior; it does
not change the resource-limit outcome. Exhaustion excludes only the selected
copied variant multiset, not a different frequency vector, larger quotient,
rank-one periodic tiling or nonperiodic plane tiling. These records are not
unrestricted untileability results.

## Assumption ledger and bounded-cycle blocker

Part of the mathematical problem: original unmarked convex P/Q, reflections,
all contacts, omission allowed. Imported finite model: reviewed exhaustive
native bank-sum/optional-cut contact reduction on these strata. Derived inside
the checker: exact positivity/closure, original polygons, complete finite cut
inventory, legal selected edge alignments and mutually disjoint interiors.
Deliberately unproved/ignored: complete vertex neighborhoods, neighbor cut
consistency, extension, topology and existence of an infinite tiling.

The actual remaining Cairo necessity targets are six after the fresh VALID
ray459 periodic review: separated46/49, low239 and fixed rays759/906/575.
No full selected Cairo family was closed. The new geometric gate still permits
every native variant, so it supplies no global forcing argument. Increasing
old motif node limits or reusing marginal balance would not address the exact
missing obligations. Retain all accepted classifications and stop this bounded
pass; reopening requires a materially different geometric/global mechanism.
