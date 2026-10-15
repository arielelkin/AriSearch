# A six-distinct/five-distinct hexagon pair has a periodic escape

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[independent review](../reviews/hexagon-six-five-hostile-2026-10-15.md).
This is a restricted family theorem, not the full two-convex-polygon result.
Novelty is assessed only against the [documented bounded primary-source search](../literature/hexagon-six-five-boundary-2026-10-15.md); no universal priority claim is made.

## Theorem and conventions

Let A and B be compact convex hexagons with nonempty interiors and six
actual corners each. Suppose A has six pairwise distinct native side lengths,
and B has exactly five distinct native side lengths. Suppose B's repeated
length occupies two side slots of cyclic separation two: one slot lies
between them in one of the two directions around the boundary.

**Theorem.** If isometric copies of A and B tile the Euclidean plane, with
reflections and unrestricted partial contacts permitted, then A and B admit
a tiling with two linearly independent translational periods. In particular
such a pair is not aperiodic in the sense of research-problem.md.

This covers one internally distinct and one repeated-side hexagon. It does
not assume both polygons have five distinct side lengths, and it does not
cover repeat separation one or three in B.

The dependency for removing partial contacts is the reviewed
[defect-free limit theorem](hexagon-limit-and-periodicity.md): a tileable pair
of convex hexagons has a whole-native-edge, everywhere-trivalent tiling.
We also explain both periodic-witness mechanisms below. They agree with
the reviewed [four-triangle torus construction](hexagon-holonomy-distinct-lengths.md)
and [intrinsic determinism theorem](hexagon-five-length-intrinsic-determinism.md).

Number a polygon's sides cyclically 0,...,5. Its corner i is the corner
**after side i**, between sides i and i+1 modulo 6. For A use actual corner
indices 0,...,5 and for B use 6,...,11. Side i has endpoints corners i-1,i.
All corner and side indices refer to actual native slots, including the
two different B slots having equal length.

## 1. Reduction to eight numerical side words

Apply the defect-free limit theorem. Adjacent native side lengths differ
in either polygon: A has no repeat, and B's only repeat is not adjacent.
Therefore the three rays at a trivalent whole-edge vertex have three
distinct numerical lengths. Its three corner slots form a triangle in
the union of the two numerical corner graphs, where the vertices are
length values and a corner gives an edge between its two side lengths.

The A corner graph is a six-cycle. The B word can be normalized to
(p,q,p,r,s,t), with p,q,r,s,t distinct. Its simple corner graph is the
four-cycle p-r-s-t-p with pendant edge p-q. The pendant edge represents
two actual corners. Both graphs are triangle-free. Thus neither type can
occur alone in the trivalent limit, and both occur. Consequently all twelve
actual corners occur in the tiling, and every edge of the union graph
belongs to a triangle.

Let k be the number of distinct numerical lengths shared by A and B.
A length private to A has just its two A-cycle neighbors in the union
graph. Both neighbors must be shared: otherwise the shortcut needed to
close a triangle would involve a private A value in B, which is impossible,
and A's own six-cycle has no triangle. Hence private A slots are isolated
and there are at most three. If there were three, A would alternate private
and shared values. Its three required shortcuts would give a triangle on
the three shared values inside B's triangle-free graph. This is impossible.
Thus k>=4, and since B has five distinct lengths, k is 4 or 5.

Here is the complete finite numerical-word domain, including the excluded
smaller values for an independent check. Normalize A=(0,1,2,3,4,5).
Choose its k shared values, append private B values 6,7,..., and permute
these five distinct values into roles p,q,r,s,t subject to r<t. The B word
is (p,q,p,r,s,t). This gives exactly choose(6,k)*60 words, respectively

    k:       0    1    2     3    4    5
    words:  60  360  900  1200  900  360

for 3,780 words total. The constraint r<t removes reversal and no other
numerical-word choice. Discard a word precisely when a union-graph edge
belongs to no triangle. There are zero survivors for k<4, thirty for k=4,
and sixty for k=5. Quotient by dihedral relabelings of A and by cyclic
rotation/reflection of B. The eight resulting classes are listed below.
The finite computation here is graph enumeration, not a placement or
period-size search.

| Class | k | Representative cyclic B | Normalized words | Formal rings | Endpoint-closed corner covers |
|---|---|---|---:|---:|---:|
| 1 | 4 | (0,2,0,3,6,4) | 12 | 1 | 1 |
| 2 | 4 | (0,2,4,6,5,6) | 6 | 1 | 3 |
| 3 | 4 | (0,2,0,3,5,6) | 12 | 1 | 1 |
| 4 | 5 | (0,2,0,3,1,4) | 12 | 1 | 1 |
| 5 | 5 | (0,1,4,2,5,2) | 12 | 0 | 0 |
| 6 | 5 | (0,1,5,2,4,2) | 12 | 2 | 3 |
| 7 | 5 | (0,1,0,2,5,3) | 12 | 0 | 0 |
| 8 | 5 | (0,1,5,1,4,2) | 12 | 2 | 7 |

## 2. Actual stars and the full-side endpoint constraint

For each numerical graph triangle {x,y,z}, independently choose one ACTUAL
corner slot on each of its three edges xy,xz,yz. List all the resulting
unordered triples of actual corner indices. This is the complete possible
star atlas for the word; duplicated corner edges are kept as separate slot
choices. A genuine star cannot use one actual corner index twice, since
that would give two identical ray-length pairs instead of three distinct
pairs of a numerical triangle.

Let S be the subset of atlas triples that actually occur in the chosen
trivalent tiling. It covers all twelve actual corner slots. It has a
necessary endpoint closure property. Take a triple in S and one of its
three rays of length x. The two corner slots c,d touching that ray determine
one incident side each: adjacent lengths at either corner are distinct,
so the numerical length x chooses that side uniquely. Follow the two
actual sides to their other endpoints, obtaining slots c',d'. These same
tile copies are adjacent at that other endpoint of their full matched side.
Therefore some triple in S contains c' and d'. If c'=d', two copies of the
same slot would meet there, which no numerical triangle star allows; such
a triple cannot occur. This closure concerns actual tile copies and both
endpoints of a native side. It is stronger than angle-sum compatibility.

The following finite statement is the computational ingredient.

**Finite support lemma.** For each of the eight words, enumerate every subset
of its complete actual-corner star atlas. Retain it exactly when it covers
all twelve indices and has the endpoint closure property above. There are
sixteen retained subsets, distributed as the last table column. Every one
contains a formal four-triangle ring as defined in Section 3, except for
exactly these two subsets:

    class 2: {(0,1,6), (2,3,7), (4,8,10), (5,9,11)},
    class 8: {(0,1,11), (2,3,10), (4,7,9), (5,6,8)}.

Each exception partitions the twelve actual corners into four triples.
The atlases have respectively 7,6,7,10,8,10,8,10 triples, so this is a
complete enumeration of at most 2^10 subsets per representative. It uses
only finite sets, native side indexing, and equality of length symbols.
No angle feasibility, solver UNSAT claim, or geometric extension assumption
is needed. The retained support record and independent verification are
specified in Section 6.

## 3. Meaning of a formal four-triangle ring

Choose four injective side-slot matches between A and B, each matching an
equal numerical length. The four A slots have distinct lengths, so the
four B matches have distinct numerical lengths too. Give each matched pair
one common formal symbol. Give all remaining slots private formal symbols,
different in the two types and different for different slots of one type.
Each resulting formal word has six distinct symbols, four common and two
private. Different formal symbols may still denote equal numerical lengths.
In particular B's two numerically equal slots may become different private
symbols, or one private and one common. This merely selects a permissible
witness matching; it imposes no extra rule on the original polygons.

Retain the matching as a formal ring if its union corner graph has exactly
four triangles, each actual corner occurring exactly once. These are the
rings counted in the table. They are four-triangle rings in the following
concrete sense. Delete the two private symbols from either word. Every
private symbol's two neighbors must be common and joined by an edge of
the other type. The common symbols form one four-cycle Q. On each edge
of Q, exactly one type inserts a private symbol, and the other uses the
direct common-common edge. Thus the union is four triangles, one on each
edge of Q, whose edges are disjoint. Actual corner slot identities, not
only numerical graph edges, define the four triples.

If a retained actual support contains a ring, all four ring triple-angle
sums are 2pi, since those stars actually occur. Section 4 then constructs
a periodic witness without needing that witness to be a subpatch of the
original tiling.

## 4. Four-face periodic realization of a legal ring

Take two copies A0,A1 and two copies B0,B1. Orient A's reference boundary
counterclockwise and choose B's reference, reflecting it if necessary, so
their projected common four-cycle orders are opposite. On the four common
symbols choose alternating bits h(x)=0,1,0,1. Pair whole native sides with
reversed boundary endpoints as follows:

* Pair each A-private slot of A0 to that same slot of A1.
* Pair each B-private slot of B0 to that same slot of B1.
* At each common symbol x, pair the x-side of A_i to B_(i xor h(x)).

Formal matches always have equal numerical lengths. This is a fixed-point-free
pairing of twenty-four side occurrences, giving twelve quotient edges and
a connected orientable closed surface. Connectivity follows from private
sides connecting each type's two copies and common sides connecting the types.

For a triangle obtained by an A-private symbol p inserted between common
x,y, crossing p takes its first A corner to the second corner in the other
A copy. The B faces reached across x and y agree because h(x) and h(y)
are opposite. These two A corners and the direct B corner xy are therefore
one circular three-corner link. The same argument holds for B-private
triangles. Each of the four triangle kinds appears twice. All twenty-four
corners are accounted for in eight circular trivalent vertices. Thus the
surface has Euler characteristic 8-12+4=0 and is a torus.

Use the original polygon metrics on its faces. Whole-side lengths agree,
and every vertex has angle 2pi, so it is a compact flat torus. Its universal
cover is complete, simply connected, and flat. Developing Euclidean charts
gives a global isometry onto the Euclidean plane: completeness makes the
developing local isometry a covering onto the plane, and simple connectivity
makes that covering one-sheeted. The lifted original polygons therefore
cover the plane with disjoint interiors. Nonidentity deck transformations
preserve orientation and act freely, hence are translations rather than
rotations with fixed centers. The torus deck group is a rank-two discrete
translation lattice. This is the required periodic witness.

## 5. The exceptional supports force intrinsic neighbors

Suppose the actual support is one of the two exceptions. Every actual
corner belongs to precisely one possible occurring star. Fix a placed,
indexed tile U and one of its native sides i, and inspect either endpoint
corner c. Its unique star specifies the other two actual corners d,e.
The two ray lengths incident to c are distinct, and the three rays of the
star have distinct numerical lengths. Therefore the chosen side i selects
exactly one of d,e as the neighbor corner across i. That corner has two
distinct incident lengths too, so it selects a unique native side j of
the neighbor polygon. The endpoint correspondence is fixed: c goes to
the chosen neighbor corner. The other endpoints correspond along the
full side. An actual neighbor exists in the original tiling, so these
requirements are consistent. There is exactly one complete relative plane
isometry h sending the neighbor reference polygon to that side with its
interior opposite the host interior. Indeed the endpoint-ordered segment
map has two isometric extensions, and precisely one puts the reference
interior in that half-plane.

This h depends only on the host type and side index, not its absolute
position or orientation. The reference indexing is unambiguous: A has six
distinct lengths and hence no nontrivial polygon symmetry; a nontrivial
symmetry of B cannot fix its four unique numerical-length side slots either.
Both reflections and rotations are covered by composing the relative map
with the placement of U. Thus the two intrinsic tile types, with their
fixed native indices, satisfy the full relative-isometry hypothesis of the
reviewed intrinsic determinism theorem.

For completeness, the periodicity argument needs no finite absolute
orientation set. The full-side adjacency graph is connected: a generic
compact path between interior points crosses finitely many sides and can
avoid vertices, using local finiteness of a fixed finite prototile set.
If U,W have the same intrinsic state and indexed placements g_U,g_W,
then g_W g_U^(-1) maps their neighbors to corresponding neighbors because
the same h applies across each corresponding side. Propagating through
the connected graph makes it a symmetry of the entire framed tiling.
The framed symmetry group consequently has finitely many tile orbits and
acts cocompactly. It is discrete: a symmetry sufficiently close to the
identity fixes a selected tile, and an indexed nondegenerate polygon has
only finitely many symmetries.

A discrete cocompact plane-isometry group contains a rank-two translation
lattice. Here is the elementary argument. Its translation subgroup N is
a discrete additive subgroup of the plane. If N were trivial, the
orientation-preserving subgroup would inject into the abelian group SO(2).
Its nonidentity elements would be commuting rotations with one common
center, hence would form a discrete subgroup of a compact circle group
and be finite. The whole group, of index at most two over that subgroup,
would be finite, contradicting cocompactness. If N had rank one, conjugation
would preserve its primitive vector up to sign. Only four orthogonal maps
preserve that axis; the whole group would be at most four cosets of N,
whose translates of a compact set cannot cover the plane. Thus N has rank
two. Its two generators are independent periods of this actual tiling.

We have proved periodicity in either branch of the finite support lemma.
Classes 5 and 7 admit no endpoint-closed cover and therefore cannot occur
in any defect-free tiling at all. The theorem follows for every class and
hence every pair in its original unrestricted-contact hypotheses.

## 6. Exact artifacts, replay and remaining qualifications

The finite support record is
[hexagon-six-five-ring-support-2026-10-15.json](../certificates/hexagon-six-five-ring-support-2026-10-15.json).
Its producer is
[hexagon-six-five-ring-selection-2026-10-15.py](../searches/hexagon-six-five-ring-selection-2026-10-15.py).
The producer enumerates all atlas subsets for the eight representatives;
the complete 3,780-word classification and both geometric bridges are
independently checked by [the separate verifier](../reviews/hexagon-six-five-independent-2026-10-15.py). The proof uses the direct-contained-ring
property, not algebraic consequences of hypothetical angle equations.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-five-ring-selection-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-independent-2026-10-15.py

The independent exploratory
[angle/endpoint gate](../searches/hexagon-six-five-2026-10-15.md) uses Z3 and
finds exactly the same two no-ring partition models. It is corroboration
only, not a proof dependency. It must not be cited as a substitute for the
finite exhaustive set checks.

All proof-relevant finite decisions are equality of integers, set operations,
and native indices. There are no random seeds, solver resource assumptions,
period-size bounds, or numerical geometry tests in the support lemma.
The unbounded conclusion rests on the reviewed defect-free limit theorem
and the complete geometric bridges in Sections 4 and 5. The [independent whole-claim review](../reviews/hexagon-six-five-hostile-2026-10-15.md) checked those bridges and the complete enumeration and returned VALID.

This theorem excludes a new side-multiplicity class from the aperiodic-pair
search. It does not classify pairs with more repeated sides, different
repeat separation, pentagons, or arbitrary two convex polygons. In particular
it is not a final report satisfying research-problem.md's global target.
