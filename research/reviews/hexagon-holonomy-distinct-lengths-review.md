# Hostile review: two hexagons with internally distinct side lengths

**Date:** 2026-10-09. **Verdict:** valid. The reviewer independently
attempted to invalidate the full argument and did not develop the theorem.
The defect-free-limit dependency received a separate repaired re-review.
No novelty claim or solution of the entire two-tile problem follows.

## Exact claim reviewed

[The theorem](../lemmas/hexagon-holonomy-distinct-lengths.md) states:
if two genuine compact convex hexagons, **each separately having six
pairwise distinct numerical side lengths**, tile the plane under arbitrary
isometries and unrestricted contacts, the same shapes admit a doubly
periodic tiling. Equal lengths across types remain possible. This does not
say that one internally distinct hexagon suffices and does not exclude
pairs with repeated side lengths within either polygon.

## Whole-proof checks and attempted counterexamples

1. **Unrestricted contacts and a disappearing type:** the freshly reviewed
   [defect-free limit proof](hexagon-defect-limit-rereview.md) gives a
   trivalent full-edge tiling. A monochromatic limit is impossible here:
   a single six-cycle of distinct length labels contains no triangle.
   This proof uses no deep monohedral hexagon classification. Consequently
   both types occur and bring every native corner into an actual star.
2. **Length graph:** three incident ray labels are pairwise distinct;
   equality of any two would give equal adjacent sides in one sector's
   tile. Every star is a graph triangle, using actual A/B corner
   occurrences. Duplicated corner pairs across A and B are explicitly
   distinguished, so possible equal unordered adjacent lengths do not
   silently identify unequal corner angles.
3. **k>=4:** a private symbol can participate in a triangle only when its
   two neighbours are common and their shortcut is an edge of the other
   polygon's cycle. Three private symbols would alternate with the three
   common symbols and require a triangle as a subgraph of the other
   six-cycle. This is impossible. Thus k=0,...,3 are genuinely excluded,
   including both monohedral cases.
4. **k=4 ring:** private symbols are isolated. Each of A's two private
   shortcuts consumes one of B's only two common-common edges, and vice
   versa. The projected common four-cycles coincide; on every edge one
   polygon inserts a private symbol and the other uses a direct edge.
   The twelve actual corners partition into four unique triangles.
   Actual tiling occurrence forces each triangle's total angle to 2pi.
5. **Finite cyclic-word domain:** fixing A labels cyclically and fixing
   the least B label as its first position loses only rotations. Taking
   one direction per reversed B word loses only reflection; unordered
   corner labels and their angle slots are transported consistently.
   The six k=5 common subsets give 360 words, and k=6 gives 60. The four
   listed orbit classes and all thirty survivors match the exact retained
   certificate; numeric coincidences beyond k are impossible because each
   polygon's six lengths are internally distinct.
6. **Angle legality, not just side legality:** this was the main attempted
   attack. For the duplicated-corner cases, both actual A/B versions must
   occur in nonempty availability sets at the two relevant triangle kinds.
   A two-set perfect matching assigns each corner version once. In the
   k=5 zero-duplication representative, the selected triangles are forced
   by unique corners. In the k=6 octahedron, a length-graph edge cover
   alone can fail to contain a full four-face partition: six legal faces
   could omit opposite cube nodes of different parity. The proof repairs
   that potential shortcut correctly using the total corner angle 8pi:
   any partition with three legal triangles has its fourth legal too.
   A legal cover with at most four triangles is one entire cube bipartition.
   Thus an actual legal ring follows in every class.
7. **Formal splitting:** treating an equal A/B numerical length as two
   type-private formal symbols only chooses a smaller collection of
   permissible contacts for the *new periodic witness*. It does not
   impose a rule on all admitted tilings. Every selected formal match
   still has equal numerical full-side lengths, so this construction is
   permitted by the original shapes.
8. **Both endpoints of edges:** reflect the B reference so projected
   common cyclic orders reverse, and alternate the bit h on the common
   four-cycle. A private-side crossing switches the copy index; h(x)
   differs from h(y) at the two ends of each inserted private symbol.
   The same B copy therefore meets the paired two A corners. The converse
   B-private case is identical. These are actual reversed endpoint
   identifications, not independently chosen vertex chiralities.
9. **Surface and geometry:** all twenty-four corners split into eight
   three-sector links; every edge is paired with a side of a different
   face. The link at each quotient vertex is circular, not a pinched
   collection of stars. The connected orientable quotient has V=8,E=12,
   F=4 and is a torus. Metric edge gluing is exact and all corner totals
   are 2pi. Its complete simply connected flat universal cover develops
   isometrically onto the plane. The lifted polygons therefore tile with
   disjoint interiors; no unproved patch-extension step is used.
10. **Periods:** the faithful torus deck group is Z^2. Its free,
    orientation-preserving Euclidean isometries are translations, since
    a nonidentity rotation has a fixed point. Proper discontinuity makes
    this translation subgroup discrete. A discrete injective rank-two
    subgroup cannot be collinear, so the witness has two independent
    nonzero periods. Reflected copies of B are allowed by the original
    definition.

## Independent computation audit

The [independent verifier](hexagon-holonomy-verify.py) was read in full and
run under Conda arisearch / Python 3.12.13:

    conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-holonomy-verify.py

It passed: 5,040 raw permutation words / 420 normalized words; thirty
survivors; fifty-four four-face torus gluings; ninety-five corner-covering
angle-support cases. It does not import the generator. Its reversed
endpoint union-find checks the actual vertex classes for every retained
splitting, and exact rational row spans independently establish the
selected-star angle consequences from every possible covering support.

The Gaussian span computation allows even abstract supports that are
inconsistent with positive polygon angles, which is harmless: it proves
an implication for a superset of actual supports. It does not infer
geometric closure or plane existence from a numerical solver. Both are
provided by the whole original polygons and flat torus construction.

## Defects, repairs, uncertainty, and verdict

No defect was found in the completed theorem. The suspected side-graph
versus angle-legal selection shortcut was explicitly resolved in the
written proof and independent span audit. The compactness dependency's
previous terse side-length sentence was strengthened by root and then
independently re-reviewed; this reviewer did not author that repair.

The full result is a restricted-family periodic-witness theorem. It leaves
repeated-length hexagon pairs and pentagon-containing pairs unresolved.
The literature novelty boundary is a separate obligation, and the theorem
makes no newness claim. The finite audit checks its complete stated domains;
it is not a bounded search for a periodic witness in an arbitrary family.

**Final verdict:** valid with the independently re-reviewed defect-free
limit dependency and the exact finite classification retained above.
