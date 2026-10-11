# Fresh hostile review: explicit private-repeat hexagon pair

Reviewer: `primary_literature`, 2026-10-09. The reviewer did not develop or
modify either proof. Reviewed
[the shape-specific theorem](../lemmas/hexagon-five-length-private-repeat-periodicity.md),
[its intrinsic determinism dependency](../lemmas/hexagon-five-length-intrinsic-determinism.md),
[the two gluing certificates](../certificates/hexagon-five-length-private-repeat-tori.json),
and the author's endpoint/torus verifier. This is a new application audit,
not a reuse of the former finite-absolute-orientation review.

## Exact claim and hypotheses

Six symbols 0,1,2,3,4,5 denote six distinct **positive numerical lengths**.
The two fixed convex hexagons have cyclic side-length orders

    A=(0,1,0,2,3,4), B=(5,3,5,2,1,4),

up to independent reversal of their references. Reflections and unrestricted
contacts are allowed in the initial tiling. If the pair tiles, it has some
doubly periodic tiling. Additionally, if a_0!=a_1 and b_0!=b_1, every
edge-to-edge trivalent tiling of this pair is itself doubly periodic.
Here a_i,b_i are the actual corners **after** native side slot i. The first
assertion uses the previously reviewed defect-free two-hexagon limit; the
second does not assert that every unrestricted-contact original tiling is
periodic. This is only the two displayed cyclic side orders.

## Angle-star and completeness attacks

At a trivalent full-side vertex the three ray lengths must be distinct:
if two were equal, one of its three incident corners would have adjacent
equal lengths, which neither displayed word has. Its corner pairs thus form
a triangle in the union length graph. Independently listing the native
corner pairs gives

    A: 01,10,02,23,34,40;
    B: 53,35,52,21,14,45.

The only triangles are 012,014,235,345. Each single-type graph is triangle
free, so a trivalent tiling cannot omit one prototype. Every actual corner
slot occurs, because each occurring copy has all its corners. Each of the
four triangle types is forced to occur by one of its unduplicated edges.
The duplicated edge01 has slots a_0,a_1; edge35 has slots b_0,b_1.

For each pair of triangle types, their available duplicated slots form two
nonempty subsets of {0,1} whose union is {0,1}. A matching selecting one
different slot from each subset therefore exists. This justifies the
complementary source stars

    (a_x,a_2,b_3), (a_(1-x),a_5,b_4),
    (a_3,b_y,b_2), (a_4,b_(1-y),b_5).

If a_0!=a_1, a fixed triangle type can have only one angle-legal choice,
since the other two angles are fixed. Corner coverage then forces the two
choices to be complementary. Equality gives both choices, since their
angle sums coincide. The same reasoning applies to b_0,b_1. There is no
unstated assumption that symbolic availability alone proves a plane tiling.

## Endpoint uniqueness, reflections, and state transport

An independent verifier, written for this review without importing author
code, exhausts every same-length neighbor slot of either type and both
endpoint bijections. A candidate survives only if its two incident corner
pairs are each a multiplicity-preserving two-element subset of a legal
star. The domain is 192 candidates across the four (x,y) supports; exactly
48 survive, one for each of the twelve native source slots in each support.
The survivors agree with the following manually derived complete slot table.
“Swap” exchanges the before/after roles of the matched sides; “preserve”
matches before to before and after to after.

| Source side | Neighbor slot | Endpoint rule |
|---|---|---|
| A0,A2 | same A slot if x=1; opposite A repeated slot if x=0 | swap if x=1; preserve if x=0 |
| B0,B2 | same B slot if y=1; opposite B repeated slot if y=0 | swap if y=1; preserve if y=0 |
| A1 | B4 | swap if x=1; preserve if x=0 |
| A3 | B3 | swap |
| A4 | B1 | swap if y=1; preserve if y=0 |
| A5 | B5 | swap |

The B-to-A rules on shared lengths are precisely the inverse rules. This
exhaustion includes same-type attempts on the shared lengths. No such
attempt survives both endpoint tests. In particular, the proof is not
silently excluding reflected matches or retaining only a preferred
orientation of one polygon.

For x=0, the repeated A matches have corner correspondences
a_5<->a_1 and a_0<->a_2, and the repeated B matches are b_5<->b_1 and
b_0<->b_2 when y=0. For x=1 or y=1, the corresponding repeated slots match
themselves with endpoints exchanged. The common-side correspondences in
the proof agree with the table. The angle-pair tests are only necessary
conditions for a geometric contact, which is sufficient for this uniqueness
argument: the existing actual tiling supplies one realized neighbor, and
all other possible index/endpoint candidates have been excluded.

Two distinct endpoint images admit two orthogonal isometries before the
side-interior condition is imposed. The condition that the two convex
polygons lie on opposite sides of their common supporting line selects
exactly one. Thus the table fixes the **whole** relative isometry, rather
than only its angle or endpoint permutation. If a tile frame g_U is
reflected, applying g_U carries the fixed endpoint images and both
halfplanes with it. The same intrinsic h_(s,i) still describes its neighbor;
no absolute-orientation or reflection-parity alphabet is required.

Each polygon has four length symbols occurring only once. Any polygon
self-isometry must fix those four native edge segments individually. A
nonidentity rotation cannot fix two different edge midpoints. A reflection
fixing a supporting edge as a set cannot have its axis along that supporting
line, since the polygon has an interior on one side; the edge must instead
cross the reflection axis perpendicularly. A line meets the boundary of a
full-area convex polygon in at most two such crossing edges. Four fixed
edges therefore also exclude a reflection. The reference indexing is
unambiguous. Local finiteness and a compact generic path avoiding vertices
give connected full-side adjacency. The two shape types supply the finite
intrinsic states required by the separately reviewed determinism lemma.

## Nongeneric supports and the surface attack

When at least one duplicated angle pair is equal, its choice can be set
freely. Select x=y, agreeing with the forced choice of the other pair when
that pair is unequal. The four angle equations then all hold. No argument
from a failed search for the uncoupled supports is used.

Both certificates were independently checked by a **corner-successor
permutation**, rather than the author's corner union-find. For an incoming
edge at corner (f,i), the reversed whole-edge gluing maps it to the
predecessor corner of the matched edge. Iterating this permutation gives
eight cycles of length three in each model. Consequently each identified
vertex has one circular three-corner link; the vertex classes are not
merely triples hiding a nonmanifold link. The four source-star types each
occur twice. Every one of the 24 native sides is used exactly once, giving
12 equal-length edges; all paired faces are different; the face adjacency
graph is connected. All edge identifications reverse the chosen oriented
face-boundary orders. Thus the quotient is a connected closed orientable
surface, with V-E+F=8-12+4=0.

For the reflected words, new corner i maps to original corner (4-i) mod6.
This was independently checked against both corner cycles and their source
star multisets. Reversal by (5-i) would have been an off-by-one error;
the retained certificates and both checkers use the correct (4-i) rule.
Each source star has angle sum2pi, so there are no cone points. With the
given polygon metrics this is a compact flat torus. Its complete flat
universal cover is the Euclidean plane; deck transformations are a rank-two
translation lattice, developing whole original faces into a doubly periodic
tiling. Actual side lengths and angles belong to the given original
polygons, so no new polygon-closure claim is inferred from the integer
certificate. This uses the reviewed flat-torus development dependency.

## Reproduction, defects, and verdict

Commands actually executed with assertions enabled:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-private-repeat-verify.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_private_repeat_independent.py
```

The independent checker returned:

```text
PASS independent audit: 192 endpoint candidates, 48 unique prescribed maps; both quotients have eight circular three-corner links, connected faces, reversed edge orientations and chi=0.
```

Certificate SHA-256:
`dba8222715575ad8f98890db37ddd21f78b9d292eb872f0ebba18cba259ed645`.

No counterexample or proof defect was found under the stated hypotheses.
No proof repair was made by this reviewer. The newly retained independent
checker provides explicit endpoint-table and circular-link verification,
which strengthen the evidence for the proof's geometric and manifold steps.
The claim for initial unrestricted contacts still depends on the separately
reviewed defect-free limit; this review does not replace that dependency.
Other five-length words, nonprivate repeated lengths, and branching endpoint
languages remain outside the theorem. No claim of novelty is made.

**Verdict: VALID for the displayed restricted pair**, including arbitrary
initial contacts for the existence of a periodic alternative and the stronger
all-trivalent-tilings conclusion when both duplicated angle pairs differ.
