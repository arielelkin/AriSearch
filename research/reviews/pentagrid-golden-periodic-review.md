# Fresh review of the golden-length pentagon periodic escape

Reviewer: root,2026-10-10. The metric agent developed the shapes and witness;
root did not develop those artifacts. **Verdict: valid** for the exact
U/regular-W pair and its whole-plane periodic witness. This is not a
classification of arbitrary pentagrid pairs.

The [counterexample](../counterexamples/pentagrid-golden-metric-periodic-pair.md)
specifies two complex-coordinate pentagons, four placements, two periods
and a complete coverage argument. Root's independently written
[checker](verify_pentagrid_golden_periodic_independent.py) imports no search
implementation. It reconstructs z from positive radicals in exact
AA/QQbar arithmetic and verifies the defining polynomial and root isolation.
All coordinates, period vectors and certificate values are compared with
these independently constructed algebraic numbers.

The checker re-enumerates all2343 normalized golden-power metric vectors
in the stated three-word domain. It recovers exactly1 U,6 V and6 W records,
matches every retained vertex, checks actual angle cosines and strict
supporting-side convexity. In particular the binary alphabet yields only
regular W. This checks the finite closure domain, not arbitrary golden
lengths or plane tilability of every fixture.

For the positive witness, the primitive proposed period matrix has nonzero
determinant, and the four motif areas sum exactly to its covolume. Root
computes the complete overlap bounds with an inverse AA lattice matrix.
All38 nonidentity ordered translates in those bounds have intersection
area zero by exact polygon clipping, rather than the author's separating
axis routine. The complete shift set agrees with the placement certificate.
No fixed or numerical shift cutoff enters the proof.

The coverage proof is sound: disjoint interiors and area equality imply
coverage almost everywhere in a lattice cell; the periodic union of a
finite compact motif is closed and locally finite, so an uncovered point
would create an open uncovered set of positive area. There are therefore
no holes, including isolated boundary holes.

Root also reconstructs the side-twin corner permutation. It has exactly
six circular links, each with actual angle sum2pi, and connected face
adjacency. All ten reversed endpoint seams match by integer combinations
of the two proposed periods. The stored corner classes agree with these
permutation cycles. Arbitrary local angle legality is not used as an
extension claim: the explicit periodic placement already proves coverage.

Attempted attacks included a wrong complex root, omitted mirror classes,
indexing angles before instead of after sides, incomplete overlap bounds,
positive-area intersections, area counted with the wrong sine factor,
zero-area holes, noncircular native links and nonintegral seam translations.
No mathematical defect was found. The first root checker execution called
an unavailable denominator method on an AA number; explicit coercion to QQ
after proving rationality fixed the checker. This changed no geometric data
or decision.

The claim about U's monohedral untileability is a separate imported
classification application, undergoing its own fresh review. W's
monohedral angle obstruction is elementary and valid. Neither is needed
for the periodic witness. The eleven negative four-face fixture domains
are not independently exhaustively re-enumerated in this review and have
only their stated bounded computational scope.

Replay with assertions enabled:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_golden_periodic_independent.py
```

The checker passes2343 metric tests,38 complete overlap comparisons and
six links. The original unrestricted two-convex-polygon target remains open.
