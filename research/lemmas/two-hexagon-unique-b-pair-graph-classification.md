# Unique-B-pair hexagon stars: a complete necessary graph family and loop obstruction

Date: 2026-10-12. **Status: independently reviewed as part of the [whole-theorem audit](../reviews/two-hexagon-unique-b-star-impossibility-review.md).**
This generalizes the graph mechanism behind the two-disjoint-three-cycle
balanced root. It gives a complete necessary graph family for one narrow
star domain, plus a universal spatial exclusion for a subfamily. It does
not claim that every remaining case tiles or has a periodic escape.

## Domain and theorem

Use the global hexagon SFT conventions, including reflected placements.
Assume every allowed vertex star has exactly two A corners and one B
corner. For each native B corner j=0,...,5, assume its allowed unordered
pair of native A corners is unique, written E_j={u_j,v_j}; repetition
u_j=v_j is permitted. Thus the six allowed triples are

    T = {(u_j,v_j,6+j): j=0,...,5}.

Each B corner is a distinct native label even if two of its pairs agree.
The pair multigraph G has vertices 0,...,5 and six B-labeled edges E_j.
A repeated A corner gives a loop, counted twice in the degree. Repeated
pairs give parallel edges.

**Theorem.**

1. If X(T,e) is nonempty for any side-equivalence e, every vertex of G
   has degree two. Failure of this condition excludes every e.
2. For a degree-two G, T has rank five modulo the two polygon sums. Its
   rational closure consists of T and precisely the pure-B triples
   corresponding to perfect matchings of G. Therefore T is an exact
   mixed-only closed type precisely when G has an odd component cycle.
3. Every such mixed-only closed type is a minimal covering rank-five
   root: it has no proper covering rationally closed ancestor.
4. If G consists of six loops, then X(T,e) is empty for every e and
   every permutation of native B corners.

Statements 1 and 4 are combinatorial SFT obstructions, so they do not
require actual polygon realisability. The reviewed global reduction
transfers their emptiness to non-tileability for actual convex pairs.

## 1. Corner balance forces a degree-two graph

Take any invariant probability measure on a nonempty X, obtained by
averaging translates over growing lattice squares. Let a,b be the A,B
cell probabilities. Each tile contributes all six of its native corner
labels exactly once. There are two vertex stars per cell, each containing
one B corner, so 6b=2 and b=1/3, a=2/3.

Let w_j be the expected number per cell of stars using B corner j.
Because this corner has one allowed triple, its native-corner ledger is
w_j=b=1/3. An A corner i occurs deg_G(i) times in these six triples,
counting multiplicity. Its ledger therefore gives

    deg_G(i)/3 = a = 2/3,

so deg_G(i)=2 for every i. This argument excludes nonregular graphs
without assuming that any individual configuration has convergent
frequencies or without solving length equalities. Conversely, degree
two gives the positive necessary balance w_j=1/3; it proves no tiling.

## 2. Exact closure and the eight mixed-only component types

Write x_c=angle_c-120 degrees. The six equations give

    x_(6+j) = -x_(u_j)-x_(v_j),

including the doubled term at a loop. The B sum equation follows from
the A sum because every A vertex has degree two. The six triple rows are
independent before polygon sums: each has its own B column. A linear
combination lies in the span of the polygon rows only when its six
coefficients are all equal. The single relation is

    sum_j m_j = 2*1_A + 1_B.

Thus the additional rank is five.

For an implied triple, let h be its number of B corners, with
multiplicities n_B(j) and A incidences n_A(i). Substitution of the B
variables leaves a form that must be a multiple c of the sole A-sum row:

    n_A(i) - sum_j n_B(j)*m_(E_j)(i) = c.

Summing over the six A indices yields 3-h-2h=6c, hence c=(1-h)/2.
For h=0 or h=2 this is a half-integer, impossible for the integer left
side. For h=1, c=0 and the A pair is exactly its assigned E_j, giving
one of the six existing triples. For h=3, all A entries vanish and c=-1:
the selected three B edges cover every A vertex exactly once. This is
precisely a perfect matching, with distinct nonloop edge occurrences.
Loops cannot occur, and repeating a labeled edge cannot occur.

A finite degree-two multigraph is a disjoint union of cycles: a loop has
length one, a parallel-edge component has length two, and longer cycles
are simple. It has a perfect matching if and only if every component
cycle is even. The eight remaining partitions of six are therefore the
complete mixed-only closed family:

| Component lengths | Graphs on the six labeled A corners | B-dihedral edge words | Universal six-loop exclusions |
|---|---:|---:|---:|
| 5+1 | 72 | 4320 | 0 |
| 4+1+1 | 45 | 2700 | 0 |
| 3+3 | 10 | 600 | 0 |
| 3+2+1 | 60 | 1800 | 0 |
| 3+1+1+1 | 20 | 1200 | 0 |
| 2+2+1+1 | 45 | 720 | 0 |
| 2+1+1+1+1 | 15 | 450 | 0 |
| 1+1+1+1+1+1 | 1 | 60 | 60 |
| **Total** | **268** | **11850** | **60** |

There are 388 degree-two labeled graphs in total. The three excluded
all-even partitions are 6 (60 graphs), 4+2 (45), and 2+2+2 (15).
Their closures add respectively 2,4,8 pure-B triples, since every even
component supplies two choices of labeled matching edges. Such larger
exact types lie outside the all-2A+1B domain; no monohedral geometric
escape is inferred merely from their pure-B angle triples.

The B-word counts quotient the ordered six pairs by native B rotations
and reflection. They keep parallel B-corner labels distinct in the star
set; duplicate pair words are merged only as native B relabellings.
No A-dihedral quotient is taken, so the table is a complete finite domain
with harmless duplicate symmetry classes, not a count of distinct SFTs.
The previous two-three-cycle investigation is the 600-word row of this
domain. The other seven rows are separate obligations.

Every B label occurs in just one triple. A covering subset must contain
all six triples, so no proper closed subset can cover all twelve native
corners. This proves the minimal-covering-root assertion for the entire
268-graph family, rather than just the original example. Generic exact
angles exist arbitrarily close to all-120 degrees, by avoiding the
finitely many additional proper triple hyperplanes. This imposes no
compatible side-length or polygon-closure conditions.

## 3. At most 64 endpoint assignments determine a B-neighbor ring

Fix a placed B cell at zero. Every one of its six neighbors A_k at D_k
is A, since each of its vertex stars has exactly one B. At central slot k,
assign the two endpoints of E_j to A_k and A_(k+1). A nonloop pair has two
choices and a loop has one, so there are at most 2^6 choices overall.

Consecutive central vertices meet the same A neighbor at two consecutive
slots. Their assigned native A indices must differ by +1 or -1 modulo
six. If they do, they determine that neighbor's rotation and chirality
uniquely. Hence these endpoint assignments reconstruct exactly the
angle-legal B-neighbor rings; there is no need to search 12^6 independent
A placements. Length constraints can then remove assignments.

There is also a useful seam inventory. The six reconstructed A sides
facing B are edges of the native six-cycle. Let n_i count the occurrences
of native A side i. Every A corner occurs twice among the assigned pair
endpoints because G has degree two, so

    n_(i-1)+n_i=2 for each i.

Thus n_even=t and n_odd=2-t, where t is one of 0,1,2. Every ring uses
one of three A-side multisets: each side once, the three even sides
twice, or the three odd sides twice. The six native B side lengths must
match the corresponding multiset. This is a necessary local metric gate,
not a periodicity certificate. The general overlap-SFT and deterministic
row criterion are separate spatial tools.

## 4. The universal six-loop spatial exclusion

Suppose all six edges of G are loops. Degree two forces them to be
exactly one loop at each A native corner. Write i_k for the loop index at
central B slot k, and A_k=(r_k,s_k) for its neighbor at D_k. Put

    a_k(h)=r_k+s_k*h modulo six.

The central loop forces

    a_k(k+2)=a_(k+1)(k+4)=i_k.

The two A neighbors share an edge. At its opposite endpoint the third
cell is B, because both adjacent cells are A. All allowed triples are
loops, so the two A native indices there must agree. They are

    a_k(k+1)=i_k-s_k,
    a_(k+1)(k+5)=i_k+s_(k+1).

Their equality gives s_(k+1)=-s_k. The same A_k neighbor occurs at the
preceding central B vertex, giving

    i_(k-1)=a_k(k+3)=i_k+s_k.

Thus the A-neighbor chiralities alternate and i_(k+1)=i_(k-1). The six
central labels therefore use at most two A indices. But a placed B tile
uses all six native B corners, and their assigned six loop indices are
all distinct. This contradiction proves X(T,e) empty for every e and
every native B order. It does not rely on a torus bound or solver result.

A useful additional **necessary local loop condition** applies to mixed
loop/nonloop graphs. At a loop indexed i, the opposite A/A endpoint pair
can only be a loop at i-1, a loop at i+1, or the nonloop edge {i-1,i+1}.
Indeed opposite neighbor chiralities give the first two possibilities;
equal chiralities give the third. Therefore if none of these three
edges is present in G, X(T,e) is empty for every e. This condition can
remove entire graphs independently of the native B ordering.

For a mixed graph, a central loop need not force opposite neighbor
chiralities: the opposite star can be a nonloop {i-1,i+1}. Consequently
three consecutive central loops alone have not been proved impossible.
No such stronger exclusion is used in the table or domain certificate.
The 60 all-loop orders leave 11790 domain words requiring other tests;
local loop conditions or the separate full-ring census can further
exclude them, but those outcomes are not counted here.

## Exact domain replay

The [solver-free domain verifier](../reviews/verify_two_hexagon_unique_b_pair_graph.py)
generates all degree-two graphs from the cycle decompositions of all
permutations of six vertices, deduplicates their edge multisets, and
counts their B-dihedral words. Every degree-two graph has such a cycle
orientation, so the generation is complete. It independently checks
representative rank and all 364 closure memberships for all eleven
component partitions using exact rational nullspaces.

The [retained domain certificate](../certificates/two-hexagon-unique-b-pair-graph-domain.json)
contains the ledger and the representative triples/closure extras.
This is a domain certificate, not a complete angle-spatial census or a
metric-side-equivalence enumeration.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_hexagon_unique_b_pair_graph.py --check research/certificates/two-hexagon-unique-b-pair-graph-domain.json
