# Interleaved/alternating: private seams and all AB metric words

Date: 2026-10-12. Status: [independently reviewed VALID](../reviews/two-hexagon-interleaved-alternating-private-transport-review.md)
for the complete metric-word gate and twelve nonconstant periodic witnesses.
The equal-odd residue is covered separately by the [index-nine torus review](../reviews/two-hexagon-interleaved-alternating-equal-odd-torus-review.md).

Run:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-interleaved-alternating-private-transport.py research/certificates/two-hexagon-interleaved-alternating-private-transport.json

Native-ring restrictions give49152→8748→216. The complete five-partition,
136-word AB alphabet gives123 empty cores and13 nonempty cores. Twelve have
nonconstant odd A lengths and admit an exact index-six native metric torus
covering every actual side metric of their word; all three even A lengths
remain independent. Full-native A-ring quotients are six-state involution
systems, with two interchangeable B representatives per signature.

The [proof](../lemmas/two-hexagon-interleaved-alternating-nonconstant-metric-escape.md)
distinguishes this full-native overlap quotient from corner colours. The one
all-equal odd case remains a separate geometric residue; its overlap quotient
has36 states and maximum outdegree5. No further generic ring enumeration or
solver extension is proposed by this record.
