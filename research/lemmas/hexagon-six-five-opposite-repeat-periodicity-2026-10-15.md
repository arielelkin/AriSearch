# Six-distinct/five-distinct hexagons with an opposite repeat

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-six-five-separation-three-hostile-2026-10-15.md). This is a partial theorem.

## Theorem

Let A,B be genuine compact convex hexagons with nonempty interiors. Suppose
A has six distinct native side lengths and B has exactly five, its two equal
sides being opposite (cyclic separation three). If they admit any plane tiling
by isometries, including reflections and partial contacts, then they admit a
doubly periodic tiling. They therefore cannot form an aperiodic pair under
research-problem.md. Equal-length numerical coincidences between A and B
are unrestricted. This does not cover adjacent repeats in B or fewer than
five distinct lengths in B.

The proof uses the reviewed defect-free limit theorem in
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md).
The four-ring and intrinsic-isometry mechanisms are proved in Sections3-5 of
[the separation-two theorem](hexagon-six-five-separation-two-periodicity-2026-10-15.md),
and originally in the independently reviewed
[distinct-length torus](hexagon-holonomy-distinct-lengths.md) and
[intrinsic determinism](hexagon-five-length-intrinsic-determinism.md) lemmas.
We state their exact applicability below; no separation-two word census is
assumed to hold for this new domain.

## 1. The defect-free limit and a new monohedral escape

Pass to an edge-to-edge, everywhere-trivalent tiling. Number side slots
0,...,5 and corner i after side i, so side i has endpoints i-1,i.
Normalize the side word of B as

    B=(p,q,r,p,s,t),

with five distinct numerical lengths. Its corner graph is two triangles,
pqr and pst, meeting at p; every graph edge is one actual B corner. Since
adjacent side lengths differ in both shapes, every trivalent star has
three distinct ray lengths and is a numerical graph triangle with one
actual corner chosen on each graph edge.

If a star using B alone occurs, its corner triple is either {0,1,2} or
{3,4,5}, in B's native indices. If the first has angle sum 2pi, the other
does too because the six angles of B sum to 4pi. The converse is identical.
These two equations give an explicit periodic monohedral escape:

Take two counterclockwise B faces B0,B1. WITHIN each face identify its
side0 with side3 by reversed boundary endpoints. For each other native side
1,2,4,5 identify that side in B0 with the same side in B1, again reversing
boundary endpoints. All lengths agree. The quotient is connected since the
four cross-face edges connect the faces, and is a closed orientable polygonal
surface. Its four vertices have circular three-corner links with labels
{0,1,2},{0,1,2},{3,4,5},{3,4,5}. For example, the corner0 of B0 is identified
across its side0 with corner2 of B0, and the side1 cross-pair brings corner1
of B1 into the same link. All twelve face corners are accounted for. Thus
V=4,E=6,F=2 and Euler characteristic zero. Every cone angle is 2pi by the
two equations, so this is a flat torus. Its universal cover is the Euclidean
plane, tiled by the lifted B faces; its rank-two deck lattice gives two
independent translational periods. The self-identifications are between
different boundary edges, and are valid surface gluings; the plane lift
uses whole disjoint copies of the original polygon.

We may therefore assume that no B-only star occurs. The A corner graph is
a six-cycle and has no triangle, so there is no A-only star either. Both
types occur, every actual native corner slot occurs, and every occurring
star is mixed.

## 2. Complete numerical-word domain

Normalize A=(0,1,2,3,4,5). Let k be the number of shared numerical lengths.
Choose its k shared A values and append private B values 6,7,..., obtaining
five distinct role values p,q,r,s,t. Include every assignment of these roles
to (p,q,r,p,s,t), modulo the four readings starting at either occurrence of p
in either boundary direction. Select the lexicographically least reading.
There are choose(6,k)*30 words, for k=0,...,5:

    30,180,450,600,450,180; total 1890.

For every word, form all numerical triangles. On each edge choose every
actual A or B corner occurrence having that numerical length pair. Remove
all B-only triples. A-only triples never arise. Discard a word if the mixed
triples do not cover all twelve actual corner slots. This is a necessary
test, not a sufficiency assumption. There are no survivors for k<4, thirty
for k=4, and thirty-six for k=5.

Quotient by dihedral relabelings of A and independent dihedral readings of B.
Private numerical labels have no further ambiguity in the surviving domain,
which has at most one private B length. The eight resulting classes are:

| Class | k | B | Raw words | Mixed triples | Endpoint-closed supports |
|---|---|---|---:|---:|---:|
| 1 | 4 | (0,1,3,5,1,6) | 12 | 5 | 0 |
| 2 | 4 | (0,1,5,3,1,6) | 12 | 5 | 1 |
| 3 | 4 | (0,2,6,5,3,6) | 3 | 4 | 1 |
| 4 | 4 | (0,2,6,3,5,6) | 3 | 4 | 1 |
| 5 | 5 | (0,1,3,0,2,4) | 12 | 8 | 0 |
| 6 | 5 | (0,1,3,0,4,2) | 12 | 8 | 1 |
| 7 | 5 | (0,1,3,5,1,2) | 6 | 8 | 1 |
| 8 | 5 | (0,1,5,0,4,2) | 6 | 8 | 7 |

Hereafter actual corner indices0..5 denote A, and6..11 denote B.

## 3. Actual full-side consistency and exhaustive finite dichotomy

Let S be the set of mixed actual-corner triples that occur in the chosen
defect-free tiling. It covers all twelve corner indices. For any two corners
c,d in a triple, their shared numerical length x specifies one side at each
corner, because adjacent lengths differ. Follow these two full matched sides
to their other endpoints, c',d'. They must belong together to a triple in S.
If they have the same native corner index, no numerical triangle can contain
these two copies of the same corner, so the starting triple cannot occur.
This is exactly the full-side endpoint-closure condition used in the
separation-two theorem, now applied to the new mixed atlases.

Enumerate all subsets of each mixed atlas, retaining exactly corner covers
with this endpoint-closure property. There are twelve retained supports,
distributed 0,1,1,1,0,1,1,7. Every support either directly contains a formal
four-triangle ring or partitions the twelve actual corners into four triples.
No linear algebra, solver, metric feasibility assumption, or extension of
locally legal patches is used. The only supports without a ring are:

    class3: {(0,1,6),(2,7,10),(3,4,9),(5,8,11)},
    class7: {(0,1,11),(2,7,10),(3,4,8),(5,6,9)}.

Each is a disjoint partition. In the ring definition choose four equal-length
A/B side-slot matches; give those pairs common formal symbols, and every
other side slot its own private formal symbol. Require the formal union
corner graph to be four edge-disjoint triangles covering all actual corners.
Different formal symbols can have the same numerical length. This only
selects allowed matches for a periodic witness; it does not restrict the
original tilings.

## 4. Why the finite dichotomy proves periodic escape

If the occurring support contains a formal ring, its four actual corner
triples each have total angle 2pi. Use two copies of each polygon, pair
same-index private sides between the two copies of that species, and pair
common sides across species with alternating copy parity around the common
four-cycle. Reflect the B reference if needed so the common cyclic orders
are opposite. All side matches have equal numerical lengths. Every quotient
vertex consists of one of the four triples, each appearing twice. The
result is a connected orientable surface with eight vertices, twelve edges,
four faces and circular vertex links. Angle sums make it a compact flat
torus. Developing its simply connected complete flat cover gives a doubly
periodic tiling by the original shapes. Section4 of the cited separation-two
theorem supplies the explicit pairing proof; it applies to formal rings
regardless of the original location of the repeated numerical length.

Otherwise every actual corner has precisely one occurring star. The host
side length at one endpoint selects the neighbor corner uniquely, because
the star's three ray lengths differ. That neighbor corner has two distinct
arms, so this also selects its native side uniquely. Full-side matching
fixes the other endpoint. Ordered endpoint images together with opposite
interior half-planes determine the complete relative isometry uniquely,
including the choice between reflected and unreflected placement. Thus
across every native side, neighbor type, side slot, endpoint correspondence,
and complete relative isometry depend only on the indexed host type.
Both prototypes have enough unique lengths to eliminate indexing ambiguity.
The full-side adjacency graph is connected by local finiteness and a path
avoiding vertices. The reviewed intrinsic-determinism theorem therefore
applies and makes this tiling itself doubly periodic. Equivalently, equal
types determine global tiling isometries, yielding a discrete cocompact
plane-isometry group and hence a rank-two translation lattice.

These arguments prove the theorem in all branches.

## Computation, scope and remaining questions

The complete finite domain is1890 words, the eight mixed atlases of sizes
5,5,4,4,8,8,8,8, and every subset of each atlas. No numerical angles or
coordinates, random seeds, solver calls, timeouts, or period-size bounds
occur. All decisions use finite sets and integers.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-five-separation-three-gate-2026-10-15.py

The default command prints JSON without changing retained evidence; explicit
`--output` writes a certificate. The retained record is
`research/certificates/hexagon-six-five-separation-three-2026-10-15.json`.
The producer imports only the pure combinatorial atlas/ring/endpoint
functions of the separation-two producer. A fresh independent verifier reconstructs this new domain and the two-B
torus without producer imports:
`research/reviews/hexagon-six-five-separation-three-independent-2026-10-15.py`.
Its complete artifact-specific hostile review is VALID.

The theorem is specific to A six distinct lengths and B exactly five with
an opposite repeat. The adjacent-repeat case remains separate, as do all
pairs with four or fewer distinct side lengths in B and all pentagon pairs.
No claim that every original unrestricted tiling is periodic is needed:
one admitted periodic witness suffices to refute aperiodicity.
