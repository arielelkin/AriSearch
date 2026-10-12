# Same-colour AAB hexagon transport: exact finite record

Status: [independently reviewed VALID](../reviews/two-hexagon-rank-nine-colour-transport-review.md)
for the finite colour census and the stated metric specializations. The later
[whole complementary-angle theorem](../lemmas/two-hexagon-complementary-angle-native-word-reduction.md)
separately covers every actual metric in this angle family.

The [producer](two-hexagon-rank-nine-colour-transport.py) and
[certificate](../certificates/two-hexagon-rank-nine-colour-transport.json) reduce
the two-angle-per-species family to its binary corner-colour projection. The
complete [statement and proof](../lemmas/two-hexagon-rank-nine-colour-transport.md)
distinguish angle witnesses from metric sufficiency.

Run:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-rank-nine-colour-transport.py research/certificates/two-hexagon-rank-nine-colour-transport.json

The exact outcomes are C/C:96 rings→6 core, C/I:48→empty, C/ALT:2→empty,
ALT/C:0, ALT/I:0, ALT/ALT:2→2. Five explicit stripe tori establish all surviving
colour pairs, including all three I cases without enumerating their native rings.
Each witness retains its native labels and required side equality closure.

C/C's core has three orbits of size two and all directions functional. Its
native colour fibres have size two, so metric equalities reduce to periodic
binary signed equalities and unary pins. The separately proved periodic binary
equality lifting lemma turns any actual metric realization into a periodic one.
ALT/ALT has native fibres of size six and is not covered by that argument.
For ALT/ALT with native A side period two, a local ray argument forces B
equilateral; explicit index-three native reflected witnesses cover both choices
of B length. Arbitrary ALT metrics and the three I metric fibres remain open.

No global claim follows merely from angle-only torus existence, and no inference
of native period from colour period is used.
