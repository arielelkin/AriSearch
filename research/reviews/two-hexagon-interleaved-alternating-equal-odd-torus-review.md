# I/ALT equal-odd metric torus and completed metric coverage

Verdict: VALID. This direct index-nine torus resolves the equal-odd residue of the separately reviewed 136-word metric gate.

The independent checker `check_two_hexagon_interleaved_alternating_equal_odd_torus.py` imports no producer. It checks the 36 reflected native rings against the independently verified 216-state domain, recomputes every local native seam closure and shared-cell overlap relation, and verifies the six full A-ring signatures with six central-B representatives each. The quotient successor maps have order three. This construction does not require an infinite-field existence assumption or a solver.

More importantly, the full nine-face native torus is checked directly from its stored cell labels on HNF `(3,0,3)`. All eighteen canonical vertex stars have exactly two A corners and one B corner of the same colour. All fifty-four directed seams match the prescribed actual length classes; all eighteen directed AA seams are reflected, native-self-index matches. Native reflected side indices are obtained from their corner endpoints.

Independently computing the exact side equality closure gives `(0,1,2,1,3,1;1,1,1,1,1,1)`. Thus precisely the three odd A sides and all six B sides share a length, while A's three even sides remain independent. Further equalities in actual metrics are allowed. The torus consequently works for any fixed genuine polygons with the stated angle words and these side lengths. Periodic Euclidean development uses the reviewed global encoding theorem; neither colour periodicity nor an unproved geometric carrier substitutes for it.

Combined with the independently checked twelve index-six witnesses for the nonconstant surviving words and the 123 empty transport cores, this completes every actual metric in the I/ALT rank-nine family: the pair is untileable or has a periodic escape. The original tiling may have reflections, partial contacts, and omitted types, because the reviewed defect-free limit supplies the necessary trivalent phase and metric-word ledger. Periodicity of every original admitted tiling is not asserted.

The retained check is `two-hexagon-interleaved-alternating-equal-odd-torus-check.json`. The checker has optional `--output PATH` and otherwise modifies no artifact.
