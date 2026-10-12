# Interleaved A: exact local whole-side gate

Date: 2026-10-12. Status: [independently reviewed VALID local necessary gate](../reviews/two-hexagon-interleaved-local-side-gate-review.md).
The later geometric and transport theorems separately handle the surviving rings.

Run:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-interleaved-local-side-gate.py research/certificates/two-hexagon-interleaved-local-side-gate.json

The [lemma](../lemmas/two-hexagon-interleaved-local-side-obstruction.md) proves
that native I angles away from p=120 cannot close with positive side lengths
of period two. The exact twelve-seam closure rejects 384/3072 I,C rings,
6264/12288 I,I rings, and 0/49152 I,ALT rings. Counts include all native B
placements and reflected side indices. The certificate contains closure
multiplicities and exact native representatives, rather than large solver logs.

The 2688,6024,49152 respective remaining local rings still require global
transport and polygon closure analysis; this record does not assert that any
of them extends to a full plane tiling.
