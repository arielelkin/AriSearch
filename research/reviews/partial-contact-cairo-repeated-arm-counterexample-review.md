# Independent hostile review: repeated-arm Cairo counterexample

Reviewer: root, independently of the construction author. Verdict **VALID**.
[Counterexample](../counterexamples/partial-contact-cairo-repeated-arm-not-monotile.md).

The native angle word gives only90^4/120^3 full stars and90^2 half stars.
At every T the perpendicular native arm seam is whole. Both possible
slots of the repeated length1 have complement1; the private c,d slots
have complements d,c respectively. Thus every event has identical banks.
The reviewed two-T invariant excludes every unequal arm-ray match, and
e avoids every doubled bank length, excluding hosted e seams. Any remaining
T-hosted arm would oppose an unequal native arm at its120 endpoint and is
likewise excluded. A hypothetical tiling must therefore be edge-to-edge.

Every e seam needs an isolated(b,c) third sector; both physical e partner
orientations give exposed arm pairs(1,1),(d,d),or(1,d), none equal{1,c}.
This excludes all admitted tilings by that one shape, not merely a selected
orientation or monohedral periodic tiling.

[Independent exact checker](verify_cairo_repeated_arm_counterexample_independent.py)
reconstructs the vertices from the five directed edges; it verifies closure,
all15 strict supporting determinants, all five squared lengths, all five
same-perpendicular event pairings, all doubled exclusions and every e-seam
endpoint obstruction. It imports no producer, solver or classification.
Replay PASS. The general argument applies under the artifact's explicit
three-distinct-arm and nonhosted-e hypotheses. Repeated-arm pairs remain
outside the generic two-Cairo dichotomy. No Rao theorem is a dependency.
