# Independent review of the interleaved/alternating private-seam domain

Reviewed: [root lemma](../lemmas/two-hexagon-interleaved-alternating-private-seams.md).
Verdict: valid within its explicitly stated defect-free trivalent limit.

For I=(p,p,q,p,q,q), the even native side endpoint types are pp,qp,qq,
and all odd sides are mixed. ALT has mixed endpoints on every side.
The same-colour AAB star therefore forbids an AB seam on side0 or4.
Alternating species neighbours force the entire even parity class to be
AA and the odd class to be AB. A dihedral native placement preserves
the parity partition; reflections do not add a third possibility.

Within the even class each unordered colour pair occurs on precisely
one native side. Since p!=q, equality of the two A corner colours at
each endpoint forces equal native seam indices, even if actual lengths
coincide. On side2 the unequal endpoint colours force each endpoint to
map to the identical native endpoint. The physical neighbour is then
the reflection in the seam line. On the homogeneous sides both endpoint
orders survive locally; eliminating the half-turn would need a new
argument. The root retains both and makes no such elimination.

The AB ledger is independent of state-orientation distribution. Every
A contributes |U| occurrences of a chosen odd-side length block U, and
every B contributes the fixed native multiplicity n_U. Translation
averaging supplies an invariant measure on the finite-state lattice
field; the one-B coset fixes species densities 2/3 and1/3 in every phase.
Double counting gives n_U=2|U|. This argument permits zero frequencies
of particular orientations and mixtures of species phases.

Thus five set partitions of the three odd native indices are complete,
with multiplicities 2,2,2; 4,2; or6. The90 labelled distinct-length B
words are counted correctly. This does not require odd lengths to be
distinct from even lengths and those coincidences do not create new
AA endpoint-colour choices.

Scope is essential: these conclusions apply to the reviewed limit,
not automatically to every partial-contact seam in the original tiling.
They are necessary conditions only and prove neither geometric closure,
full-plane extension nor periodicity. No correction needed.
