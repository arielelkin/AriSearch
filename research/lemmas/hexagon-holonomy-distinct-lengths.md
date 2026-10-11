# Periodic witnesses for two hexagons with internally distinct side lengths

**Status:** adversarially reviewed; [fresh whole-claim review](../reviews/hexagon-holonomy-distinct-lengths-review.md) valid. The finite side-order classification and all proposed torus
vertex identifications have an exact certificate and separate implementation.
See the [whole-claim review](../reviews/hexagon-holonomy-distinct-lengths-review.md)
and the [defect-free dependency re-review](../reviews/hexagon-defect-limit-rereview.md).
No novelty claim is made: a literature audit is still required.

## The theorem and scope

Let A and B be two compact convex hexagons with nonempty interiors and six
actual corners. Suppose **each polygon separately has six pairwise distinct
side lengths**. Lengths of an A-side and a B-side may coincide. If isometric
copies of A and B tile the plane, then copies of these polygons admit a doubly
periodic plane tiling. Reflections and unrestricted contacts are permitted
both in the hypothesis and in the conclusion.

In particular, no such pair is aperiodic under `research-problem.md`.
This does not exclude a pair having repeated side lengths in either member.
There is no claim that just one member having distinct lengths is enough.

**Dependency:** the defect-free limit theorem in
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md): a tileable
pair of convex hexagons admits an edge-to-edge, everywhere-trivalent tiling.
The present argument does not import a monohedral hexagon classification.

## 1. The length graph

Give every distinct numerical side length a symbol. The six symbols around A
are all different, as are those around B. Each cyclic word defines a simple
six-cycle: its vertices are side-length symbols, and an edge {x,y} represents
the corner between consecutive sides of lengths x and y. Let G be the union
of these two cycles. If both cycles contain the same edge, G is simple but
that edge has two actual corner occurrences, with potentially different
angles. Write a_xy and b_xy for the A- and B-corner angles when they exist.

At a trivalent vertex, the three rays must have three different length
symbols: a repeated pair of ray symbols would be the two adjacent sides of
one tile, contradicting internal distinctness. Therefore the three corner
occurrences form a triangle in G. They cannot all be A, or all be B, because
a six-cycle has no triangle. Every actual corner of each type that occurs
must belong to at least one occurring angle-legal triangle.

Neither type can tile alone in the defect-free limit: its length graph would
be a single triangle-free six-cycle. Thus both types occur, and every one of
the twelve actual corner occurrences must occur in some vertex star. Every
edge of G consequently belongs to a triangle.

Let k be the number of shared numerical side lengths. A symbol private to A
has exactly two neighbors in G. Its two incident corner edges can belong to
a triangle only if its neighbors are both shared and the shortcut between
them is a B-cycle edge. Thus private A symbols are nonadjacent around A;
the corresponding statement holds for B. There are at most three private
symbols per cycle. If there were three, the A word would alternate private
and shared symbols. Its three required shortcuts would be a triangle on the
three shared symbols inside the B six-cycle, impossible. Consequently

    k >= 4.                                               (1)

## 2. The four-triangle ring and its explicit flat torus

For this construction symbols may be **formal**: equal numerical lengths
on the two types may receive different private symbols. A formal symbol
always prescribes one specific numerical side length, so matching formal
symbols still matches equal full sides.

Assume four symbols are common, and each type has two private symbols.
Assume every corner-cycle edge belongs to a triangle in the union graph.
The private symbols are isolated in their own cyclic word. Deleting the two
private symbols from A gives a four-cycle Q on the common symbols. Its two
shortcut edges must be B common-to-common edges. B has exactly two such
edges, so these are all its common-to-common edges. The same argument with
A and B interchanged shows that deleting B's private symbols gives the same
four-cycle Q. Thus each edge xy of Q has exactly one private symbol p inserted
on it in exactly one type, while the other type uses xy directly. The union
length graph is four triangles, one on each edge of Q, with disjoint edge
sets. Every actual corner occurs in exactly one of these triangles.

Suppose the three actual angles on each of these four triangles sum to 2pi.
We now construct a periodic witness using four whole tiles.

Choose A's reference orientation. Choose B's reference, reflecting it if
necessary, so that its common symbols appear in the reverse cyclic order
around Q. This reflection is allowed by the problem. Give the vertices of Q
alternating bits h(x)=0,1,0,1.

Take four oriented polygonal faces A_0,A_1,B_0,B_1, with their boundaries
oriented counterclockwise in their respective reference placements. Pair
all sides as follows, always reversing boundary endpoint order:

* A private side is paired between A_0 and A_1, matching the same side slot.
* B private sides are paired between B_0 and B_1 in the same way.
* For each common symbol x, pair its side of A_i with its side of
  B_(i xor h(x)), for i=0,1.

These pairings identify equal complete sides. They are fixed-point-free on
the 24 side occurrences, so there are twelve quotient edges. The quotient
is connected: private edges connect the two copies of either type, and
common edges connect the types. Reversed boundary identifications give a
closed orientable surface.

Check the vertices explicitly. Suppose p is an A-private symbol inserted
between common x and y. At a corner (p,x) of A_i, crossing its p-side leads
to corner (p,y) of A_(1-i). The B face reached across x is B_(i xor h(x));
the B face reached across y from A_(1-i) is
B_((1-i) xor h(y)). These are the same face because h(x) differs from h(y).
The opposite projected common boundary orders identify the remaining B
corner (x,y) with these two A corners. Hence this quotient vertex has exactly
these three corners. The argument for a B-private symbol is identical.
Each of the four triangle kinds gives two such quotient vertices. All 24
corners are accounted for, so there are eight vertices, each with a circular
three-sector link. The Euler characteristic is 8-12+4=0. The connected closed
orientable quotient is therefore a torus.

Put on it the intrinsic Euclidean polygon metrics. Along edges these metrics
match, and every quotient vertex has total angle 2pi by hypothesis. This is a
compact flat torus without cone singularities. Its universal cover is complete,
flat, and simply connected; developing its local Euclidean charts gives a
global isometry with the Euclidean plane. One standard justification is that
completeness makes the developing local isometry a covering onto the complete
Euclidean plane; that plane is simply connected, so the covering is one-sheeted.
The lifted faces consequently cover the plane with disjoint interiors and are
isometric copies of the original whole convex polygons.

The deck group is Z^2. Its Euclidean isometries preserve orientation and act
freely, so every nonidentity deck transformation is a translation (a nontrivial
orientation-preserving rotation has a fixed point). The translation subgroup
is discrete, and its rank-two image has two linearly independent generators.
This gives a doubly periodic tiling with a four-face torus quotient.

This construction proves existence from the four specified angle equations;
it does not presume that a locally legal patch extends.

## 3. Four shared lengths

When k=4, Section 2 applies without any splitting. All four triangles are
angle-legal because each actual corner occurs in the given trivalent tiling
and has only its unique graph triangle available. Its four-face flat torus
provides the periodic witness.

## 4. The finite cyclic-word classification for k=5 and k=6

Normalize A's cyclic word to (0,1,2,3,4,5). The private B symbols, when present,
are 6,7,... . A reference corner is indexed by its unordered pair of neighboring
side symbols; this survives rotating or reflecting either cyclic word.

For k=5 there are six choices for A's private symbol and 60 unoriented cyclic
B words for each choice, totaling 360. For k=6 there are 60 B words. Enumerate
all of these 420 words and discard a word exactly when an edge of G belongs
to no triangle. Up to the dihedral relabelings of A, rotation/reflection of B,
and relabeling of private B symbols, the surviving words have four classes:

| k | Representative B word | Common corner edges | Number of normalized words |
|---|---|---|---|
| 5 | (0,2,1,3,6,4) | {1,2} | 12 |
| 5 | (0,2,6,3,1,4) | none | 12 |
| 6 | (0,1,5,3,4,2) | {0,1}, {3,4} | 3 |
| 6 | (0,2,4,1,5,3) | none | 3 |

The complete finite classification is independently replayed below. It is
small integer computation, not a geometric search or a periodicity bound.
The certificate retains all thirty survivors, their graph triangles, and every
four-common-symbol splitting that gives the ring of Section 2.

## 5. Five shared lengths: choosing a legal ring

### 5.1 B=(0,2,1,3,6,4)

The four graph triangles are 012,123,045,346. Here and below a string such as
012 means the set {0,1,2}. The private-symbol triangles 045 and 346 have unique
corner assignments, so they are angle-legal.

Triangle 012 consists of a_01, b_02, and either a_12 or b_12.
Triangle 123 consists of a_23, b_13, and either a_12 or b_12.
Both triangle kinds occur: a_01 can occur only in 012 and a_23 only in 123.
Both actual corners a_12 and b_12 occur somewhere, and these are their only
two available triangle kinds. Thus the nonempty availability sets for 012 and
123 collectively contain both choices A and B. A perfect matching of these
two sets chooses A for one triangle and B for the other. This elementary
matching claim follows directly by checking whether either set is a singleton.

If 012 uses a_12 and 123 uses b_12, treat numerical length 1 as separate
A-private and B-private symbols. If the choices are reversed, split length 2
instead. Together with the original private lengths 5 and 6, the resulting
formal words have four common symbols and exactly the four selected legal
triangles. Section 2 gives a periodic tiling. The splitting selects permitted
contacts; it does not assert that all original tilings obey this selection.

### 5.2 B=(0,2,6,3,1,4)

The graph triangles are 012,014,045,123,134,236, all with unique corner
assignments. Triangles 045 and 236 are forced by the private symbols. Triangle
012 is forced because the actual B corner {0,2} belongs to no other graph
triangle. Triangle 134 is forced because the actual A corner {3,4} belongs
to no other graph triangle. These four angle-legal triangles are

    012, 045, 134, 236.

Split numerical length 1 into A-private and B-private copies. In 012 the two
A corners meet at 1; in 134 the two B corners meet at 1. These four triangles
are exactly the ring for the resulting four-common-symbol words. Section 2
again provides the periodic witness.

## 6. Six shared lengths: choosing a legal ring

### 6.1 B=(0,1,5,3,4,2)

The graph triangles are 012,015,234,345. The shared corner edge {0,1} belongs
to the first two triangles; the shared corner edge {3,4} belongs to the last
two. Each of these triangle kinds occurs because of one of its corner edges
that is not duplicated and belongs to no other triangle. Each of a_01,b_01
must occur in the first pair, and each of a_34,b_34 must occur in the second.
The two independent two-set matching arguments of Section 5.1 choose each
actual duplicated corner once. In the first pair this splits either numerical
length 0 or 1; in the second it splits either 3 or 4. The resulting four formal
triangles form a ring, and all four selected sums are 2pi. Section 2 applies.

### 6.2 B=(0,2,4,1,5,3)

G is the octahedron graph, with nonedge pairs {0,4},{1,3},{2,5}. Its eight
triangles divide into two sets:

    F = {012,035,145,234},
    H = {015,023,124,345}.

Each set partitions all twelve graph edges, hence all twelve actual corners,
once. There are no duplicated corners. Let L be the graph triangles whose
actual corner sums equal 2pi. Every graph edge lies in at least one triangle
of L, because the corresponding corner occurs in the given tiling.

The only four-triangle edge covers of the octahedron are F and H. Here is a
short verification: its face-adjacency graph is the cube, bipartitioned into
F,H; every node is adjacent to three of the four nodes in the other part.
A four-node vertex cover with r nodes in F leaves 4-r nodes of F and r nodes
of H uncovered. For r=1,2,3 these cannot be independent: a node has only one
nonneighbor in the opposite part. Only r=0 or r=4 works. Fewer than four
triangles cannot cover twelve edges since each triangle covers only three.

Consequently, if |L|<=4, it contains F or H. If |L|>=5, one of F,H contains
at least three triangles of L. The sum of all twelve actual corner angles is
8pi; three legal triangles from that partition sum to 6pi. The fourth therefore
also sums to 2pi. In all cases every triangle in one of F,H is angle-legal.

For F, split numerical lengths 1 and 3 into type-specific private copies.
Its four selected triangles become the four-triangle ring with the other
four symbols common. For H, split lengths 0 and 4 instead. Section 2 supplies
a periodic witness in either case.

This finishes every value of k permitted by (1) and proves the theorem.

## 7. Exact replay, certificate, and limitations

From the repository root:

```text
conda run --no-capture-output -n arisearch python3 research/searches/hexagon-holonomy-classify.py
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-holonomy-verify.py
```

The generator prints JSON; it does not overwrite the retained
[certificate](../certificates/hexagon-holonomy-classification.json). The separate verifier
reconstructs the full cyclic-word domain, checks the retained survivors and
splittings, and audits every four-face gluing without importing the generator.
The complete domain, execution conditions, and narrow literature check are in
[the search record](../searches/hexagon-holonomy-classification.md).
There are no stochastic seeds, solver calls, timeouts, or floating-point steps.
The finite arithmetic is integer/rational. The verifier additionally checks
all possible angle-legal star subsets in these four finite classes using exact
linear-span consequences and actual-corner coverage; this validates the
selection argument separately from the geometric torus construction.

The polygons in the torus are the original exact shapes; this proof introduces
no new approximate geometry or polygon closure assumption. The source cyclic
words merely organize their existing side lengths and existing corner angles.
A tiling with unrestricted contacts is handled by the named defect-free limit
lemma before applying this argument. A type disappearing in that limit would
produce a triangle-free monochromatic length graph and is impossible here.

The main problem remains unresolved for pairs with a repeated side length in
at least one hexagon, and for all other surviving side-count classes. This
partial theorem does not establish a general two-hexagon impossibility theorem.
