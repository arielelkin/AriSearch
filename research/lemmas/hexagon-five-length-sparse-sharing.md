# Two repeated-side hexagons with at most three shared lengths

**Status:** adversarially reviewed; [fresh whole-claim review](../reviews/hexagon-five-length-sparse-sharing-review.md) valid.

## Statement

Let A and B be compact convex hexagons. Suppose each has exactly five distinct
side lengths: one length occurs twice, and its two side slots have cyclic
separation two. Suppose the sets of numerical side lengths of A and B share
at most three values. If the pair tiles the plane with arbitrary rotations,
reflections, and unrestricted contacts, then it admits a doubly periodic
plane tiling with a four-face torus quotient, containing two tiles of each type.
With at most two shared numerical lengths the pair cannot tile at all.

This statement concerns **both** members with the specified repeated-side
pattern. It does not cover a (6-distinct,5-distinct) pair, repeat separation
one or three, or four or five shared numerical lengths.

**Dependencies:** the [defect-free limit theorem](hexagon-limit-and-periodicity.md)
and the explicit four-triangle flat-torus construction in Section 2 of
[the distinct-length theorem](hexagon-holonomy-distinct-lengths.md). The latter
construction applies to formal side symbols even if some different symbols
have equal numerical lengths.

## Exact finite reduction

Number A's side slots cyclically as

    A = (0,1,0,2,3,4).

Its simple corner graph is the four-cycle 0-2-3-4-0 with a pendant edge 0-1.
The pendant edge represents two actual corner occurrences. This graph has no
triangle. The same is true for B. Adjacent sides always have different
lengths, so three rays at a trivalent vertex have three distinct numerical
lengths. Their three corners form a graph triangle in the union of the two
corner graphs. Neither type can tile monohedrally in a defect-free limit.
Thus both types occur, all twelve actual corner slots occur, and every edge
of the union graph belongs to a triangle.

The complete side-order search for k=0,1,2,3 shared values has respectively
60,300,600,600 normalized B words. It retains zero words for k<3 and one for
k=3, namely

    B = (0,3,0,5,1,6).

Private B labels are 5,6,... . A normalized B word is (p,q,p,r,s,t), where p
is its repeated length, q its pendant symbol, and r<t resolves reversal.
All choices of the k shared A values and all assignments of B's five distinct
symbols to these roles are included. The exact retained certificate and a
separate implementation verify this complete 1,560-word domain; this is not a
bounded search for periodic tilings. In the sole survivor the shared lengths
are 0,1,3. Its graph triangles are

    015, 016, 023, 034.

Write a_i and b_i for the corner after side slot i of the displayed A and B
words, respectively. The available corner triples for these four graph
triangles are:

| Triangle | Two fixed corners | Choice |
|---|---|---|
| 015 | b_2,b_3 | a_0 or a_1 |
| 016 | b_4,b_5 | a_0 or a_1 |
| 023 | a_2,a_3 | b_0 or b_1 |
| 034 | a_4,a_5 | b_0 or b_1 |

Every triangle kind occurs, because its private length has only that triangle
available. Both a_0,a_1 occur in the first two rows; both b_0,b_1 occur in the
last two. For each pair of rows, one can select one actual repeated corner
in either row and the other in the other row. This two-by-two matching fact
alone does not ensure consistent repeated-side slots. The other endpoint of
a full side supplies the missing relation.

## The endpoint relation

Choose an actual occurrence of triangle 015. There are two cases.

**Case I: it uses a_0.** The ray of numerical length 0 is the full shared
side between A's slot 0 and B's slot 2. At this endpoint their corners are
a_0 and b_2. At the other endpoint those *same tile copies* have corners
a_5 and b_1. The graph contains only triangle 034 at this endpoint, and its
third corner is a_4. Thus

    a_4 + a_5 + b_1 = 2pi.                              (2)

We can choose a_1 for row 016. Indeed, a_1 must occur in 015 or 016; if it
occurs only in 015 then both a_0,a_1 make 015 legal, so a_0=a_1, and the
nonempty row 016 also permits a_1. Similarly we can choose b_0 for row 023:
if b_0 occurs only in 034, (2) and that occurrence give b_0=b_1, and the
nonempty row 023 also permits b_0. We therefore have four legal sums with
actual corner triples

    (a_0,b_2,b_3), (a_1,b_4,b_5),
    (a_2,a_3,b_0), (a_4,a_5,b_1).                       (3)

**Case II: it uses a_1.** The same ray of length 0 is now the full side
between A's slot 2 and B's slot 2. At the other endpoint those tile copies
have corners a_2 and b_1; the third corner is a_3. Thus row 023 permits b_1.
The same actual-corner coverage/equal-angle argument selects the opposite
corner in the companion rows, giving

    (a_1,b_2,b_3), (a_0,b_4,b_5),
    (a_2,a_3,b_1), (a_4,a_5,b_0).                       (4)

All statements above follow from full sides in the defect-free tiling and
from actual corner slots; a graph triangle alone does not prove them.

## Four-face periodic realization

Assign distinct formal symbols u,v to A's numerical-length-0 slots 0,2.
A's formal word is (u,1,v,2,3,4), with four common symbols u,v,1,3.

For (3), give B's numerical-length-0 slots 0,2 the symbols v,u, respectively.
Its formal word is (v,3,u,5,1,6). Its four graph triangles are exactly (3).
For (4), use B's formal word (u,3,v,5,1,6); its graph triangles are exactly (4).
In either case the two A-private symbols are 2,4 and the two B-private
symbols are 5,6. The formal union graph is the four-triangle ring. The
formal distinction u!=v introduces no unequal matching lengths: both stand
for the same original numerical length 0. Their use merely specifies which
whole native side slots to pair in a selected witness.

The explicit four-face construction of the dependency pairs whole sides,
has eight three-corner vertices, and is a connected orientable torus. Its
four cone-angle equations are (3) or (4), now proved. Its universal cover is
a doubly periodic tiling by the original polygons. This proves the theorem.

## Replay, scope, and remaining obligation

```text
conda run --no-capture-output -n arisearch python3 research/searches/hexagon-five-length-classify.py
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-verify.py
```

The [certificate](../certificates/hexagon-five-length-classification.json)
retains the unique survivor. The separate verifier visits all 93,600 raw
multiset permutations, recovers the same 1,560 normalized patterns, checks
both four-face gluings by explicit reversed endpoint unions, and verifies
[the abstract-angle counterexample](../counterexamples/hexagon-five-length-angle-support.md).
See [the search record](../searches/hexagon-five-length-classification.md)
for complete conditions. All finite decisions use integer or rational arithmetic.

An aperiodic pair in this five-length/separation-two family must therefore
share at least four distinct numerical lengths. No theorem for that remaining
family is established here. Side-slot ambiguity can defeat angle-only
four-star selection; endpoint compatibility must be established before any
new flat-torus witness is asserted. No novelty claim is made for this result.
