# Fresh independent review of the nonsymmetric equal-private Q3 witness

**Verdict: VALID.** Root did not derive the candidate or its fixed-quotient
metric search. The [exact periodic escape](../counterexamples/new-octagon-q3-equal-private-periodic.md)
has been independently reconstructed and checked by
[an exact clipping verifier](verify_octagon_q3_equal_private_independent.py),
which imports no author code.

The checker builds P and Q from their native lengths and direction words
in Q(zeta10), using the explicitly isolated embedding. Positive closure,
all strict supporting-side inequalities and each exact angle cosine pass.
Its six actual placed walks agree coefficientwise with the retained
certificate. The two equal phi^2 sides are absent from P and occur exactly
twice in Q. Direct cyclic rotation/reflection tests show Q has only the
identity symmetry. Thus this example really belongs to the nonsymmetric
equal-private branch, even though P has its permitted reflection symmetry.

All36 reversed seam endpoint equations pass; all36 native slots occur once.
The face adjacency graph is connected. The actual corner successor cycles
are twelve circular triple links, with angle sum2pi and accumulated integer
lattice shift zero for each. No abstract sector-count substitution hides
an incorrectly ordered or multivalued vertex identification. The quotient
is an orientable compact nonsingular flat torus. The nonzero displayed
covolume equals the total area of four P and two Q motifs. Consequently
the coordinate local isometry onto the ordinary lattice torus has degree1
and its lift is a full-plane tiling with disjoint interiors.

The independent checker also derives every possible ordered face/lattice
intersection from exact inverse-lattice vertex extrema. All36 candidate
pairs have intersection area zero under exact convex clipping, independent
of the author's separating-axis check. Omitted integer translates have
disjoint coordinate projections, so this covers every infinite translate.
Density1 and closed locally finite periodic union independently exclude
holes. Replay passed:

    conda run --no-capture-output -n arisearch python research/reviews/verify_octagon_q3_equal_private_independent.py

The search stopped at a witness after304 of1000 native assignments; neither
review nor theorem treats that prefix as exhaustive. Its search domain,
reflection assignments and endpoint equations are recorded. The final exact
fixture is verified independently of any cone solver or search procedure.

This proves one periodic admitted tiling. It refutes equal private lengths
plus no Q symmetry as a sufficient aperiodicity condition. It does not
prove every tiling of these shapes periodic or classify all equal-private
metrics; local cross-native mates and arbitrary mixed branches remain
unclassified. Further searches in that family are inactive under the
current two-mechanism portfolio. No defect remains in the scoped witness.
