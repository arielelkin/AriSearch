# Periodic escape for a hexagon pair with six and at least five distinct lengths

Date: 2026-10-15. Status: proved from three independently reviewed new case
theorems and the previously reviewed six-distinct/six-distinct theorem.
This is a restricted structural theorem, not a solution of research-problem.md.

## Exact statement

Let A and B be compact convex hexagons with six genuine corners and nonempty
interiors. Assume A's six native side lengths are pairwise distinct and B
has at least five distinct native side lengths. If copies of A and B tile
the entire Euclidean plane, with arbitrary isometries, reflections, and
partial contacts permitted, then copies of the same shapes admit a doubly
periodic plane tiling. In particular, this pair cannot be aperiodic under
the original unrestricted definitions.

No restriction is placed on numerical side-length coincidences between A
and B. No orientation rule, adjacency marking, or edge-to-edge convention
is imposed on the hypothesis. The conclusion asserts existence of a periodic
escape, rather than periodicity of every admitted original tiling.

## Proof and exact dependencies

The reviewed [defect-free limit theorem](hexagon-limit-and-periodicity.md)
produces an edge-to-edge, trivalent tiling admitted by any tileable pair of
convex hexagons. Thus the new cases can use full native-side endpoint
constraints without silently strengthening the original definition.

If B has six distinct lengths, apply the previously reviewed
[distinct-length theorem](hexagon-holonomy-distinct-lengths.md).
If B has exactly five, precisely one length occurs twice and the other
four occur once. The two repeated slots have cyclic separation one, two,
or three, exhausting all possibilities. Apply respectively:

1. [Adjacent-repeat theorem](hexagon-six-five-adjacent-periodicity-2026-10-15.md):
   complete 3780-word numerical domain, twelve surviving corner-word orbits,
   eleven native-arm-consistent corner supports; every support contains a
   formal four-triangle ring, giving a four-face flat-torus witness.
2. [Separation-two theorem](hexagon-six-five-separation-two-periodicity-2026-10-15.md):
   complete 3780-word domain, eight surviving orbits, sixteen endpoint-closed
   supports; fourteen admit four-face tori and two give unique intrinsic
   neighbor isometries and hence a discrete cocompact symmetry group with
   a rank-two translation lattice.
3. [Opposite-repeat theorem](hexagon-six-five-opposite-repeat-periodicity-2026-10-15.md):
   complete 1890-word domain with pure-B stars separately handled by an
   explicit two-B-face torus. The mixed branch has eight orbits and twelve
   endpoint-closed supports, ten with four-face tori and two with intrinsic
   neighbor determinism.

Each theorem proves periodic escape for all positive geometric metrics
realizing its numerical length word, without a bounded period search.
The graphs and supports alone do not assert tilability: they supply
necessary conditions extracted from an existing defect-free tiling; the
flat-torus or intrinsic-isometry argument supplies the actual periodic
witness. This proves the statement. QED.

The three new domains sum to9450 normalized word records. They are separate
repeat-position domains, with deliberately retained private-label redundancy
for small shared alphabets. No claim of9450 geometric congruence classes is
made. All finite arithmetic is integer combinatorics; no solver UNSAT result,
angle approximation, or finite-patch extension assumption is trusted.

## Consequence for the remaining research frontier

This theorem alone excludes a six-distinct member paired with a member having five or six lengths. Later reviewed results strengthen the remaining frontier: no member of a hypothetical aperiodic hexagon pair may have six distinct lengths, and at least one member must have at most four. The [unified statement and proof map](hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md#unified-statement-and-proof-map) distinguishes the one-period arbitrary-partner theorem from the doubly periodic each-at-least-five theorem. Neither result resolves the remaining lower-multiplicity hexagon pairs or pentagon-containing pairs.

This necessary structural restriction is a new partial result relative to
[the documented literature boundary](../literature/hexagon-six-five-boundary-2026-10-15.md).
No universal priority or complete two-hexagon classification is claimed.

## Independent audits and deterministic replay

Separate fresh hostile reviews are retained for
[separation two](../reviews/hexagon-six-five-hostile-2026-10-15.md),
[opposite repeats](../reviews/hexagon-six-five-separation-three-hostile-2026-10-15.md),
and [adjacent repeats](../reviews/hexagon-six-five-adjacent-hostile-2026-10-15.md).
The independent verifiers import no producer and additionally construct
actual side-pairing tori rather than trusting the formal-ring enumeration.

Run the registered three certificate producers and three independent
verifiers with:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/verify.py --only hexagon-six-five-ring-selection-2026-10-15.py --only hexagon-six-five-separation-three-gate-2026-10-15.py --only hexagon-six-five-adjacent-gate-2026-10-15.py --only hexagon-six-five-independent-2026-10-15.py --only hexagon-six-five-separation-three-independent-2026-10-15.py --only hexagon-six-five-adjacent-independent-2026-10-15.py

Default producers print deterministic JSON without changing retained
certificates. For a full repository replay use the prescribed `mise run replay`;
that includes other historical registered research and is not a new search.
