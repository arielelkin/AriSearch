# Three actual A lengths: joint ALT/ALT closure

Date: 2026-10-12. Status: [independently reviewed VALID as part of the complete ALT/ALT chain](../reviews/two-hexagon-alternating-all-metric-chain-review.md).
This component retains its stated restricted domain; the full family conclusion
is in [the all-metric theorem](../lemmas/two-hexagon-alternating-all-metric-escape.md).

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-alternating-three-length-joint-closure.py research/certificates/two-hexagon-alternating-a-side-strata.json research/certificates/two-hexagon-alternating-three-length-joint-closure.json

The [theorem](../lemmas/two-hexagon-alternating-three-length-joint-obstruction.md)
uses three A mirror partitions and90 B words per partition. All270 joint
matrices have rank2, kernel(1,1,1), and no admitted rank-drop root, contradicting
three ACTUAL distinct shared lengths. This eliminates the complete three-value
metric subfamily without native-ring enumeration. Remaining necessary domain
after prior gates is61 native A partitions and20970 B words.
