# Equal odd A lengths: direct index-nine metric witness

Status: [independently reviewed VALID positive construction](../reviews/two-hexagon-interleaved-alternating-equal-odd-torus-review.md).
This is a direct index-nine witness, with no bounded-search absence inference.

Run:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-interleaved-alternating-equal-odd-torus.py research/certificates/two-hexagon-interleaved-alternating-private-transport.json research/certificates/two-hexagon-interleaved-alternating-equal-odd-torus.json

The all-AA-reflection subset has36 native rings and six full A-ring signatures.
Its order-three commuting action gives HNF(3,0,3), nine native labels. The
certificate directly checks18 canonical stars and54 directed whole-side seams
with all three even A lengths independent, all odd A and B lengths equal.
This covers every actual metric of the equal-odd I/ALT residue, through the
reviewed periodic-label development theorem. No new carrier-geometry trust is
needed for this finite route.

The [full I/ALT metric statement](../lemmas/two-hexagon-interleaved-alternating-all-metric-escape.md)
combines this witness with twelve index-six nonconstant metric witnesses and
the complete necessary136-word AB alphabet. General ALT/ALT metrics remain
outside the proof.
