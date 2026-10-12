# Interleaved A: corrected exact closure and transport

Date: 2026-10-12. Status: [independently reviewed VALID for I/I and corrected I/C](../reviews/two-hexagon-interleaved-symbolic-closure-review.md),
including the corrected matrices, positivity exclusions and spatial gate.
The earlier I/C local-only proof is withdrawn; its [erroneous C-direction certificate](../certificates/two-hexagon-interleaved-symbolic-closure-withdrawn-C-direction.json)
is retained solely as historical evidence and is not a proof dependency.

Run the symbolic calculation, then constrained transport:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-interleaved-symbolic-closure.py research/certificates/two-hexagon-interleaved-local-side-gate.json research/certificates/two-hexagon-interleaved-symbolic-closure.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-interleaved-contiguous-transport.py research/certificates/two-hexagon-interleaved-symbolic-closure.json research/certificates/two-hexagon-interleaved-contiguous-transport.json

The [corrected proof](../lemmas/two-hexagon-interleaved-symbolic-closure-obstruction.md)
excludes all I/I rings geometrically: 12240 by rank and 48 by positive-kernel
signs. Correct I/C has 2688 rank exclusions, 288 further positivity exclusions,
and 96 locally possible rings. Their native compatibility triangle core is
empty. Certificates retain matrices, exact minor gcds, algebraic sign partitions,
a nullity-two opposed-coordinate relation, native states and deletion rounds.

The corrected I/C proof uses spatial transport. It does not reuse the withdrawn
assertion that every I/C ring is locally impossible. I/ALT and general ALT/ALT
remain outside this gate.
