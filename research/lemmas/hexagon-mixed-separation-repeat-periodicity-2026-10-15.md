# Common five side colors, with repeat separations two and three

Date:2026-10-15. Status: independently hostile-reviewed VALID and exactly
certified; [fresh review](../reviews/hexagon-mixed-separation-repeat-hostile-2026-10-15.md). This is a restricted periodic-escape
theorem. The original unrestricted two-polygon problem remains unresolved.

## Statement and geometric reduction

Let A,B be genuine convex hexagons having the same set of exactly five
numerical side lengths. Each has one doubled length. Suppose the doubled
slots of A have cyclic separation two, and those of B separation three.
The doubled values may agree or differ. If the pair admits any plane tiling,
including reflections and partial contacts, it admits a tiling with a nonzero
translation. In fact the witnesses below are doubly periodic.

A stronger source version holds: assign the same five formal side colors
to these slots, with equal physical lengths for sides of the same color.
Different colors need not have different physical lengths. If there exists
an indexed full-side, everywhere-trivalent plane tiling matching these
colors, the unmarked shapes admit a periodic escape. The periodic witness
need not preserve every source seam type or color. Auxiliary colors are a
proof device, not placement restrictions on the target shapes.

For the numerical statement, apply the independently reviewed
[defect-free limit theorem](hexagon-limit-and-periodicity.md) to obtain such
a full-side trivalent tiling. Adjacent colors differ. At each trivalent
vertex its three ray colors are distinct: equality of two would give an
adjacent equal pair on one incident hexagon. Thus a vertex is a color
triangle with one actual native corner on each edge of that triangle.
The source version uses this same combinatorial condition directly.

Normalize A=(0,1,0,2,3,4), numbering its corner i between sides i and i+1,
and B=(p,q0,q1,p,q2,q3), where p ranges over0..4 and q is a permutation
of the other four values. This is a complete120-word domain; no dihedral
quotient is needed for exhaustiveness. If the source uses only B, the
monohedral escape below applies. It cannot use only A: its corner-color
graph has no triangle. Otherwise all twelve native corners occur.

## Complete necessary endpoint and contact gate

The [standalone producer](../searches/hexagon-mixed-separation-repeat-gate-2026-10-15.py)
and [retained certificate](../certificates/hexagon-mixed-separation-repeat-gate-2026-10-15.json)
contain the full finite argument. Its implementation uses only integers
and Python Fraction arithmetic, no metric solver. For each word it lists
all actual triples among the twelve corners whose unordered color pairs
are the three distinct edges of a triangle. For each star and each of its
three rays, the two adjoining tiles prescribe actual native corners at the
far end of that full side. Delete a star if any such pair occurs in no
remaining star; iterate to the greatest fixed atlas. Every actual star
survives by induction. All three far-end demands, including both actual
occurrences of repeated color pairs, are used.

For each remaining star, connect the two native SIDE SLOTS meeting along
each ray. The graph on twelve side slots contains every seam type possible
in that atlas. An actual occurring-seam graph is a subgraph. Consequently
its connected-component partition REFINES the atlas graph partition.
If the repeated pair of either shape is disconnected in the atlas graph,
all six slots of that shape lie in different actual components: components
cannot mix different formal colors, and all its other colors are single.
Color the actual components separately. The reviewed
[six-formal-colors/arbitrary-partner theorem](hexagon-six-colors-arbitrary-partner-2026-10-15.md)
then gives an unmarked periodic escape for the original metrics. Moreover
the other shape retains at least its original five formal colors, because
actual components refine the original color partition. The reviewed
[six/five formal-color theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md)
therefore applies directly and supplies rank two in this branch. No metric
deformation is needed.

The120 records give96 words lacking a complete twelve-corner cover,16
with such a contact-component escape, and8 remaining words. Every one of
these8 has a retained explicit dihedral reading of each shape and a common
color bijection carrying it to the SINGLE representative

    A=(0,1,0,2,3,4), B=(2,0,3,2,4,1).

The certificate checks the bijection pointwise on both six-cycles. Neither
existence nor uniqueness of a metric realization is inferred from this gate.

## All actual supports of the exceptional representative

Its fixed atlas consists of the twelve actual native triples

    (0,2,11), (0,5,10), (1,2,11), (1,5,10),
    (1,6,11), (2,3,7), (2,7,8), (3,4,9),
    (3,6,7), (4,8,9), (6,7,8), (9,10,11).

Here0..5 are A corners and6..11 B corners. Enumerate all4096 subsets,
retaining exactly those covering all twelve actual corners and satisfying
each of their three far-end endpoint demands internally. Exactly30 survive.
The actual occurring-star SET equals one of these30; merely containing
an inclusion-minimal support would not suffice for the final argument.

Construct positive periodic witnesses with two indexed A and two indexed
B faces. Choose all8 relative boundary orientations modulo global reversal.
Their side-color classes have sizes6,4,6,4,4. Enumerate all perfect matchings
inside each color, hence15*3*15*3*3 pairings per orientation,48600 total.
Identify paired sides by opposite boundary endpoints. Keep connected
orientable closed surfaces whose corner links are circular triples and
whose Euler characteristic is zero. The atlas retains6 actual torus
gluings, realizing3 distinct angle-equation patterns. Completeness over
larger quotients is neither asserted nor needed.

For any such positive gluing, its edges have matching physical lengths.
If each of its vertex triples sums to2pi, the glued surface is a compact
oriented flat torus: cone points are absent and the circular links give
ordinary surface neighborhoods. Its complete universal cover develops
isometrically to the Euclidean plane, so lifted faces cover the plane with
disjoint interiors. The deck lattice supplies two independent translations.
This applies to the actual original hexagon metrics, including reflections
and noninjective physical realization of the auxiliary colors.

Normalize angles by pi. Source equations are total4 for each hexagon
and total2 for each occurring source star. For28 of the30 supports the
certificate chooses one retained actual torus and supplies a complete
exact rational combination of source rows for each target star row.
There are112 such identities. Their direct Fraction verification proves
that the original angles make the chosen positive torus flat. This is a
sufficient witness comparison, not an inference from bounded search failure.

## The two remaining exact supports

The uncovered supports are precisely

    S={(0,2,11),(1,5,10),(3,6,7),(4,8,9)},
    Splus=S union {(6,7,8),(9,10,11)}.

If actual S equals Splus, an actual B-only star occurs. In native B indices
it is {0,1,2} or {3,4,5}. Either angle sum2pi forces the other, since B's
six angles sum4pi. The explicit monohedral two-face torus from
[the opposite-repeat lemma](hexagon-six-five-opposite-repeat-periodicity-2026-10-15.md)
then gives an escape: within EACH of two equally oriented B faces pair
side0 to side3; pair each remaining side1,2,4,5 to the same side of the
other face, with opposite boundary endpoints. Its four circular vertex
links are twice each of {0,1,2} and {3,4,5}; V4,E6,F2. All lengths match,
the cone sums are2pi, and the flat-torus bridge applies. This also handles
a source using B alone.

If actual S equals S, its four stars partition ALL twelve native corners.
For any indexed host tile, side and endpoint corner, there is a unique
star containing that native corner. The host side color selects exactly
one of the other two guest corners, because all three ray colors differ.
At that corner it selects a unique native guest side, because adjacent
colors differ. Matching the full side then prescribes both ordered native
endpoints. Of the two plane isometries mapping these endpoints, exactly one
places the guest interior opposite the host. Thus the complete indexed
relative isometry of the neighbor depends only on host type and side.
Repeated lengths and physical symmetries do not change this determination:
it uses the given indexed source frames.

The full-side adjacency graph is connected, by local finiteness and a
compact path between tile interiors crossing finitely many sides while
avoiding vertices. An isometry carrying any indexed occurrence of a type
to another propagates its fixed relative neighbor maps throughout this
graph, and hence preserves the complete framed tiling. These symmetries
have at most two tile orbits, form a discrete group, and act cocompactly.
The elementary planar crystallographic argument used in the reviewed
[intrinsic frame proof](hexagon-shared-repeat-changed-family-periodicity-2026-10-15.md)
gives a rank-two translation lattice. In this last case the actual source
itself is periodic. This proves both statements. QED.

## Replay, review and precise limits

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-mixed-separation-repeat-gate-2026-10-15.py

The default prints the complete deterministic certificate. An explicit
--output PATH retains it. The domain is120 words, the representative's4096
star subsets, and48600 fixed-four-face matchings; there is no randomness,
timeout or unbounded negative search. Source legality is necessary only.
The finite certificate plus the positive flat-torus and intrinsic-isometry
bridges establish the stated restricted unbounded theorem.

The [independent no-import verifier](../reviews/hexagon-mixed-separation-repeat-independent-2026-10-15.py)
reconstructs the native endpoint demands,
word equivalences, all30 actual supports, complete target surface links,
all112 weighted identities, and the12 indexed deterministic neighbor maps.
It also independently checks the monohedral two-face torus links. All checks passed.
This does not classify common-five adjacent repeats, both-opposite repeats,
other length sets, fewer distinct lengths, or pentagon-containing pairs.
It does not resolve the original two-unmarked-convex-polygon problem.
