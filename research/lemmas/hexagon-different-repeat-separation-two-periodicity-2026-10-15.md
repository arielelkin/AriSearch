# Different doubled colors force a disconnected native seam class

Date: 2026-10-15. Status: independently hostile-reviewed VALID for genuine hexagons;
[review](../reviews/hexagon-different-repeat-separation-two-hostile-2026-10-15.md). This is a restricted periodic
escape theorem, not a solution of the unrestricted two-polygon problem.

## Statement

Let A and B be indexed genuine convex hexagons, each with six actual corners. Each side has one of the same five
formal colors. On each polygon one color occurs twice, in slots of cyclic
separation two; the other four colors occur once. The doubled colors of A
and B are DIFFERENT. Each color has a positive geometric length, but different
colors may have the same length. Suppose there exists an indexed,
color-matching, full-side, everywhere-trivalent plane tiling by these shapes,
with reflections allowed. Then the underlying unmarked shapes admit a
rank-two periodic tiling.

Consequently, two convex hexagons having the same five distinct numerical
side lengths, with different doubled values and both repetitions at
separation two, either are untileable with unrestricted contacts or admit
a doubly periodic plane tiling. Together with the independently reviewed
[same-repeat theorem](hexagon-shared-repeat-separation-two-periodicity-2026-10-15.md),
this closes all pairs sharing the same five numerical lengths with both
repetitions at separation two. This does not include four shared lengths,
other repeat positions, or more heavily repeated side-length words.

## Native indexing and the exhaustive finite domain

Normalize A=(0,1,0,2,3,4). Its corners i lie between side i and side i+1,
modulo six; B's corners and side slots have offset six. A side i has corners
i-1 and i. Normalize B=(p,q,p,r,s,t), where p belongs to {1,2,3,4} and
(q,r,s,t) permutes the other four colors. There are exactly 96 words before
reflection and 48 after identifying (q,r,s,t) with (q,t,s,r). No symmetry
of A or species exchange is used. Thus this is an exhaustive domain without
a potentially ambiguous further orbit reduction.

Each color graph is a four-cycle with a pendant edge; it has no triangle.
Adjacent colors differ, so the three ray colors at a trivalent vertex are
pairwise distinct. Its three native corners therefore form the three
edges of a color triangle. No triangle uses only one species. Both species
must occur, and all twelve native corner slots occur somewhere.

For each normalized B, enumerate every unordered three-element subset of
the twelve native corners. Retain exactly those whose unordered adjacent
color pairs are the three distinct edges of a triangle. This is the full
native star atlas. There are no multiplicity omissions: three ray colors
are distinct, so no native corner can be repeated within one star.

For a star {c,d,e} and its corner pair c,d, their shared ray has a unique
color z. That ray identifies a UNIQUE native side at each corner, since
adjacent colors differ. Follow the two identified sides to their other
endpoints c',d'. A full-side trivalent tiling must have another star
containing c',d'. If c'=d', no such triangle star exists. Remove a star
whenever one of its three ray demands has no remaining far-end star.
Iterate simultaneously to a fixed point. By induction every actual star
survives every pruning round. This is a necessary condition only; no
locally consistent atlas is asserted to extend to a plane tiling.

## The computed contact split

The [producer](../searches/hexagon-different-repeat-separation-two-gate-2026-10-15.py)
uses integers and native indices only; it imports no earlier research code.
The [certificate](../certificates/hexagon-different-repeat-separation-two-gate-2026-10-15.json)
retains all 96 raw words, all 48 normalized words, every initial atlas,
every removal with its failed ray demand, and every surviving fixed point.
Forty words prune to the empty set. The following eight survive, and each
covers all twelve corners. For each surviving star, every corner pair gives
the two native side slots across its common ray. Make an undirected graph
on the twelve native side slots with all these pairs as edges, including
loops. The table lists the connected components containing the two repeated
slots, computed from the ENTIRE fixed-point atlas.

| B | Fixed-point stars | A repeated-slot components | B repeated-slot components | Closed corner covers |
| --- | ---: | --- | --- | ---: |
| (1,2,1,3,0,4) | 8 | {0,2,10} | {1,6}; {8} | 7 |
| (1,4,1,2,0,3) | 8 | {0,2,10} | {6}; {1,8} | 7 |
| (2,1,2,0,3,4) | 6 | {0,9}; {2} | {3,6}; {8} | 3 |
| (2,4,2,0,3,1) | 4 | {0,9}; {2} | {3,6}; {8} | 1 |
| (3,0,3,1,2,4) | 8 | {0,7}; {2} | {4,6,8} | 7 |
| (3,0,3,1,4,2) | 8 | {0}; {2,7} | {4,6,8} | 7 |
| (4,1,4,0,3,2) | 6 | {0}; {2,9} | {5,6}; {8} | 3 |
| (4,2,4,0,3,1) | 4 | {0}; {2,9} | {5,6}; {8} | 1 |

For additional audit the producer exhausts all subsets of each fixed point,
retaining exactly corner-covering subsets satisfying all three far-end
requirements of every included star. It finds 36 supports total. Their
native seam graphs and connected components are retained individually.
This subset enumeration is NOT needed for the strongest contact split:
the full fixed point already disconnects at least one repeated pair in
every row. Deleting possible seams cannot reconnect disconnected slots.

## Source-to-periodicity proof

In an actual indexed source tiling define E on the twelve native side slots:
join two slots if they occur across some full seam anywhere in that tiling,
and take connected components. Every actual seam occurs at an actual star,
which survived pruning. Thus the actual seam graph is a subgraph of its
row's full fixed-point seam graph, and the E-component partition refines
the fixed-point component partition. At least one species therefore has
its repeated slots in different E-components. Every E-component lies within a single original color, since
all source seams match colors. Each E-component consequently has one
well-defined physical length, even when the original color-to-length map
was noninjective.

Recolor each native slot by its E-component. The species whose repeated
slots are disconnected now has SIX distinct formal colors. The other has
at least five. The same indexed source still matches colors on every seam.
Apply the reviewed
[formal six-color source theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md),
exchanging species if required: its six/five-or-six branches give an
unmarked rank-two periodic escape. No new geometric realization, metric
perturbation, finite-model property or bounded quotient assumption is used.

For the numerical-length corollary, begin with any unrestricted tiling.
The reviewed [hexagon defect-free limit theorem](hexagon-limit-and-periodicity.md)
supplies a full-side trivalent tiling. Give every tile a fixed indexed
reference placement and color its sides by their five numerical lengths.
This is the source required above. Colors are auxiliary proof data, and
no extra rule is imposed on the final admitted unmarked tilings. QED.

## Combined same-five-color corollary

Let two indexed genuine convex hexagons, each with six actual corners, use
the SAME five formal colors, each
using exactly one color twice at cyclic separation two and each of the
other colors once. The doubled colors may be equal OR different. Suppose
that each color determines one positive physical side length, with a
possibly noninjective color-to-length map, and that there is an indexed,
color-compatible full-side trivalent plane tiling by the two hexagons.
Then their underlying unmarked shapes admit a doubly periodic tiling.

Proof: if the doubled colors differ, apply the theorem above. If they
coincide, apply the independently reviewed formal-source version of the
[same-repeat separation-two theorem](hexagon-shared-repeat-separation-two-periodicity-2026-10-15.md).
The equal/different split is exhaustive and both source results permit
noninjective physical length maps. No identification of different formal
colors is needed in either branch.

In particular, if two unmarked convex hexagons have the SAME five distinct
numerical side-length values and both repeats have separation two, then
unrestricted tileability implies an admitted rank-two periodic tiling,
REGARDLESS OF WHICH VALUE IS DOUBLED ON EITHER SHAPE. Apply the defect-free
limit theorem, index the source tiles, color by numerical length, and use
the source corollary. Thus this entire numerical family cannot be an
aperiodic pair under the original unrestricted-contact definition.

## Replay and review gate

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-different-repeat-separation-two-gate-2026-10-15.py --output research/certificates/hexagon-different-repeat-separation-two-gate-2026-10-15.json
```

Expected summary: 96 raw words, 48 normalized words, 40 empty fixed points,
8 covering fixed points, 36 endpoint-closed corner-cover supports.

Fresh review should independently regenerate the domain and both endpoint
maps, check all star multiplicities and reflections, verify the eight
fixed-point contact graphs, and attack the actual-E recoloring argument.
Independent replay without proof review is insufficient for the theorem.
No novelty or unrestricted impossibility claim is made here.
