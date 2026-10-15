# A shared-repeat five-length hexagon family has a periodic escape

Date:2026-10-15. Status: independently hostile-reviewed VALID;
[full review](../reviews/hexagon-changed-word-connected-support-hostile-2026-10-15.md). This is one complete numerical-word family,
not a classification of two hexagons or the original problem's solution.

## Theorem and stronger source variant

Let A,B be genuine convex hexagons with cyclic native side-length words

    A=(r,x,r,y,z,t), B=(r,z,r,y,x,t),

where r,x,y,z,t are five pairwise distinct positive numbers. If these
unmarked shapes tile the plane with arbitrary isometries and partial
contacts, they admit a full-side tiling with TWO independent translations.

A stronger SOURCE statement also holds. Give the native slots the displayed
words as five DISTINCT AUXILIARY COLORS. Same-colored sides must have equal
physical lengths, but different colors may have the same physical length.
If an indexed, color-matching, full-side everywhere-trivalent source tiling
exists, the underlying unmarked pair has a doubly periodic full-side tiling.
This source statement imposes no extra rule on the final unmarked problem.
Physical polygon symmetries are permitted; indexed placements belong to the
source data. The numerical unrestricted theorem follows by taking the
reviewed uncolored defect-free limit and then using lengths as colors.

## 1. Complete native source domain

Number native sides0,...,5; native corner i is after side i, between i and
i+1. Use A corner indices0,...,5 and B indices6,...,11. Interpret the five
labels as colors throughout; numerical equality is only the special case.
Neither polygon has equal adjacent colors. At a trivalent vertex all
three ray colors therefore differ. The three native corner arm pairs
are the three edges of a triangle in the union color graph.

Each individual color graph is a four-cycle with a pendant edge, hence
triangle-free. Neither type can supply the source alone, so both occur and
all twelve native corners occur. The full possible actual star atlas is

    (0,2,9), (0,5,10), (0,8,9), (0,10,11),
    (1,2,9), (1,5,10), (1,8,9), (1,10,11),
    (2,3,6), (2,3,7), (3,6,8), (3,7,8),
    (4,5,6), (4,5,7), (4,6,11), (4,7,11).

For its actual occurring subset S, every native corner occurs. Each star
also satisfies FULL-SIDE far-endpoint closure: for each ray, its incident
two actual native side slots meet again at their other endpoints, so S
contains a star covering the two far corner indices. Adjacent colors differ,
so ray color uniquely selects the side at each corner; no unrecorded arm
mode choice remains. Duplicate far corner indices cannot occur together in
a three-distinct-ray star.

Enumerate all2^16=65536 atlas subsets, retaining precisely corner coverage
and this necessary far-end closure. Exactly171 subsets remain. This is a
complete finite NECESSITY domain; no surviving subset is asserted to extend
to a plane tiling. Its exact enumeration and independent reconstruction are
linked below. The earlier connected-four-slot-r subdomain has144 subsets;
that restriction is NOT assumed by the theorem.

## 2. Six explicit flat-torus witnesses

Take exactly two indexed A faces and two indexed B faces. Allow all eight
face-orientation assignments modulo a global reversal. The r sides give
eight occurrences with105perfect matchings; each other color gives four
occurrences with3perfect matchings. The complete fixed domain is therefore

    8 * 105 * 3^4 = 68040 side pairings.

Every paired boundary edge is identified with REVERSED oriented endpoints.
Retain connected pairings whose24corner occurrences form eight circular
three-sector links. There are12such oriented pairings, with six distinct
native angle supports. One explicit pairing and its signs for each support
are retained. All pairings use same-colored whole native sides, so lengths
agree for every allowed physical metric, including noninjective color lengths.

Each pairing is a connected orientable closed surface. Its corner-link
cycles are genuine circles, with V=8,E=12,F=4, hence it is a torus. If its
four native star-angle equations hold, each of its eight vertices has
angle2pi. Giving it the original polygon metrics makes it a compact flat
torus. Its complete simply connected cover develops isometrically onto
the Euclidean plane. The lifted faces cover without interior overlap,
and its rank-two deck lattice gives two independent translations. This
is an actual positive witness, not an inference from a failed bounded search.

## 3. Exact angle implications for169 source supports

For each of the171 necessary actual supports S, use its native star-angle
equations (sum2pi) and both polygon-angle totals (sum4pi). In pi units these
are rational augmented rows on twelve native angle variables. For169 of
the supports, the retained coverage certificate chooses one of the six
actual torus witnesses and gives an EXACT RATIONAL COMBINATION of these
source rows for each of its four target star rows. Every one of the676row
identities is directly verified by Fraction arithmetic.

Thus if the actual S is one of these169, its true geometric angles satisfy
all equations of the chosen torus. Section2 constructs a periodic escape
for those very shapes. The source need not contain a geometric copy of the
torus patch and the periodic witness need not retain all source seam types.

Exactly TWO supports are not covered by this torus comparison:

    S1={(0,2,9),(1,5,10),(3,7,8),(4,6,11)},
    S2={(0,5,10),(1,2,9),(3,6,8),(4,7,11)}.

The enumeration here compares ALL171 actual-support possibilities, not just
eight inclusion-minimal supports. Therefore in the remaining case actual S
EQUALS S1 or S2. Containing one of these partitions would be insufficient
for the next argument; equality is what the finite domain comparison gives.

## 4. The two exact remaining supports force indexed neighbors

Each S1,S2 partitions the twelve actual native corners into four triples.
Fix an indexed placed tile U, one native side i, and one endpoint corner c.
Its unique occurring star gives the other native corners d,e. Its three
ray colors differ, so the color of side i selects exactly one neighbor
corner among d,e. That neighbor corner's two colors differ, so it selects
one native guest side. One endpoint correspondence is fixed, and the other
endpoint follows from matching the full side. The ordered segment map has
two plane-isometric extensions; precisely one places the guest interior
opposite the host interior. Hence the complete indexed relative map h
is determined by host TYPE and NATIVE SIDE.

This holds even with extra physical symmetries: the source gives its actual
indexed reference placements, and ordered native endpoints plus interior
half-plane determine their whole isometries. It does not assume that
unmarked geometry canonically chooses an index or that different colors
have different metric lengths. The independent check explicitly tests all
host sides, guest slots and endpoint maps for both exact supports.

The full-side adjacency graph of the source tiling is connected: finite
shape types with positive inradii give local finiteness, and a generic
compact path between tile interiors crosses finitely many whole sides and
avoids vertices. For two indexed occurrences U,W of one type, the map
I=g_W g_U^(-1) transports U to W. The fixed relative h maps propagate I
across every neighbor in this connected graph, so I is a symmetry of the
whole framed tiling. Its image covers the plane and therefore is the whole
tile collection. The framed symmetry group has at most two tile orbits,
is discrete (a polygon has finitely many physical symmetries), and acts
cocompactly. The reviewed elementary planar group argument then supplies
a rank-two translation lattice. The source itself is doubly periodic.
This closes both remaining supports and proves both statements. QED.

## Exact artifacts and independent review obligations

The source domain is retained in
[the native-support certificate](../certificates/hexagon-changed-word-connected-support-gate-2026-10-15.json),
whose ALL171domain and original144connected subset coexist explicitly.
Its [producer](../searches/hexagon-changed-word-connected-support-gate-2026-10-15.py)
and [independent checker](../reviews/hexagon-changed-word-support-independent-2026-10-15.py)
reconstruct the full atlas, native far ends and every one of65536subsets.
The connected-tree angle-flat records are optional additional information;
the theorem needs no angle-feasibility solver or flat quotienting.

The [fixed-four-face atlas](../certificates/hexagon-shared-repeat-four-face-atlas-2026-10-15.json)
contains all six actual witness gluings. Its
[producer](../searches/hexagon-shared-repeat-four-face-atlas-2026-10-15.py)
and [independent gluing checker](../reviews/hexagon-shared-repeat-four-face-independent-2026-10-15.py)
check complete endpoint pairings, circular links, connectivity and orientation.
The positive witnesses suffice; no completeness claim about arbitrary
periodic tilings is made.

The [weighted-row certificate](../certificates/hexagon-changed-word-torus-coverage-2026-10-15.json)
and [producer](../searches/hexagon-changed-word-torus-coverage-2026-10-15.py)
retain all169chosen witnesses and676exact rational identities, and explicitly
retain the two uncovered supports rather than interpreting them as negative
periodicity evidence. The
[independent two-partition checker](../reviews/hexagon-changed-word-two-partition-determinism-2026-10-15.py)
checks their complete native endpoint maps without importing a producer.
The flat-surface and framed-group bridges are reproduced above and use the
reviewed arguments in
[the formal-color theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md).
Fresh full synthesis and all676weighted-row identities have passed independent review, linked above.

No larger torus size was searched or assumed sufficient. Neither residual
repeated-side families nor pentagon-containing pairs are classified. The
original unrestricted two-convex-polygon objective remains unresolved.
