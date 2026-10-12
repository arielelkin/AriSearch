# Same-colour AAB hexagon transport and metric fibres

**Status:** [independently reviewed VALID](../reviews/two-hexagon-rank-nine-colour-transport-review.md). The
finite record is [the colour certificate](../certificates/two-hexagon-rank-nine-colour-transport.json),
reproduced by [this solver-free script](../searches/two-hexagon-rank-nine-colour-transport.py).
The signed-graph metric step cites the independently reviewed binary lifting lemma
and has a [separate cross-review](../reviews/two-hexagon-rank-nine-cc-metric-proof-review.md).

## Scope and statements

Let A have three angles p and three angles q=240-p degrees. Let B have three
angles r=360-2p and three angles s=2p-120 degrees, where 90<p<150 and p!=120.
Give the p and r corners colour 0 and the q and s corners colour 1. Both polygons
are fixed strictly convex hexagons, and reflections are admitted.

The complete list of three-corner angle stars consists of two A corners and one
B corner, all of the same colour. There are 36 native unordered stars, allowing
repetition of an A corner: each colour has six unordered A pairs with repetition
and three B corners. Substitution in the angle sums checks that every other
three-corner species/colour composition would require p=120. This is a statement
about three-corner stars. Some special parameters admit higher-valence stars in
an original tiling; for example p=135 permits four 90-degree B corners.

The reviewed [defect-free hexagon limit](hexagon-limit-and-periodicity.md) and
[global encoding](two-hexagon-global-sft-encoding.md) reduce any original tiling
to a trivalent edge-to-edge tiling for these fixed shapes. The species field then
has exactly one B and two A at each vertex. We apply the following classification
only to that admitted trivalent field; we do not assume the original tiling is
trivalent.

There are exactly three binary native cyclic bracelets with three corners of
each colour, represented by

| Name | Native corner word |
|---|---|
| C | 000111 |
| I | 001011 |
| ALT | 010101 |

The possible angle-only bracelet pairs are exactly
(C,C), (I,C), (I,I), (I,ALT), and (ALT,ALT).
The other four pairs are impossible, irrespective of side lengths.

Furthermore:

1. For (C,C), every metric pair that admits a plane tiling admits a periodic
   plane tiling. This conclusion uses the periodic binary equality fibre lemma
   below; a periodic colour pattern alone would not imply it.
2. For (ALT,ALT), if the native A side lengths have period two, say
   E,O,E,O,E,O with E,O>0, any plane tiling forces B to be equilateral with side
   length E or O. Either such metric admits an explicit periodic tiling.

No claim is made for the unrestricted metric fibres of the three I cases or
for general side lengths in the (ALT,ALT) case.

## Complete small colour-ring census

Use native honeycomb cell directions
D0=(1,0), D1=(0,1), D2=(-1,1), D3=(-1,0), D4=(0,-1), D5=(1,-1).
B cells occupy x-y=0 modulo 3. The six surrounding A cells of a B centre are
z+Dk. A neighbour at Dk has colours b[k] and b[k-1] at slots k+2 and k+3,
respectively. This follows from the two vertices of its shared B edge and is
both necessary and sufficient for a full colour-legal B ring.

Distinct placed colour words are obtained by r+s*k modulo 6, for r=0,...,5 and
s=+1,-1; they number 6,12,2 for C,I,ALT. A ring is precisely a B word together
with one compatible placed A word for each of its six neighbours. The script
enumerates their Cartesian product, without choosing native orientations inside
each colour fibre. It retains every ring, including colour-degenerate native
placements implicitly.

Across coarse B direction Delta_k=Dk+D(k+1), two rings share A neighbours k,k+1
of the first ring and k+4,k+3 of the second. Their compatibility is equality of
these two complete placed A words. For each state i and each k, triangle support
requires compatible states j,l in directions k,k+1 with j compatible with l
in direction k+2. Repeated deletion without such support is necessary for an
infinite field. The certificate retains every deletion round, all starting
states, and all compatibility pairs.

| A | B | Full colour rings | Triangle-pruned core |
|---|---|---:|---:|
| C | C | 96 | 6 |
| C | I | 48 | 0 |
| C | ALT | 2 | 0 |
| ALT | C | 0 | 0 |
| ALT | I | 0 | 0 |
| ALT | ALT | 2 | 2 |

The two zero starting counts for ALT follow directly because every adjacent
pair of B corner colours must be distinct. The small positive starting counts
for C/I and C/ALT are not sufficient: their triangle cores are empty. No native
I ring census is needed, because each of its three B cases has the constructive
witness below.

## Positive angle-only witnesses and their limit

Let f be a periodic binary sequence and h=x-y. Colour the six slots of the cell
at (x,y) by

    (f_h, 1-f_(h-1), f_(h-1), 1-f_h, f_(h+1), 1-f_(h+1)).

Both canonical types of honeycomb vertex then have one common colour. Every
cell has exactly three corners of each colour. A cell's bracelet is ALT when
the three consecutive f values agree, C when the neighbours agree and differ
from the central value, and I when the neighbours differ. B cells have h=0 mod3.
The following sequences therefore produce the five pairs stated above:

| A,B | Repeating f | Torus HNF |
|---|---|---|
| C,C | 01 | (6,1,1) |
| I,C | 011 | (3,1,1) |
| I,I | 0011 | (12,1,1) |
| I,ALT | 001110 | (6,1,1) |
| ALT,ALT | 0 | (3,1,1) |

For each cell the certificate gives an actual native placement, not just its
colour. It independently checks both canonical vertex stars and every seam.
It records the exact side equality closure required by each torus. Thus these
are angle-only existence witnesses and conditional metric witnesses. They do
not show that every actual side metric extends one of these particular tori.
In particular an ALT colour word has six native placements: independent choices
inside that fibre need not have the colour field's periods.

## The C,C metric conclusion

Index the six surviving C,C ring states increasingly by their retained census
indices 15,26,37,58,69,80. Their coarse successor maps are

    F0=(0 5)(2 3),  F1=(1 4)(2 3),  F2=(0 5)(1 4),
    F(k+3)=Fk.

All six states have exactly one successor in every direction. The maps commute,
satisfy F2=F1 F0^-1, and have three two-state orbits. Consequently every infinite
colour field is a translated, rotated, or colour-complemented index-six stripe
field. Shared A word equality gives the corresponding entire cell colour field.

Each placed C word has exactly two native placements, for A and also for B.
On this fixed periodic colour backbone choose a binary variable at each cell
to specify its native placement. Across a fixed seam, each endpoint's native
side length is a function from that one binary variable to two fixed numbers.
Metric matching is equality of these two functions. If both functions are
injective, its relation is empty, a singleton, equality, or disequality. If one
function is constant, it gives no constraint, an impossibility, or a unary pin
on the other endpoint. If both are constant it gives no constraint or an
impossibility. In particular it cannot give a three-pair binary relation.

Thus the entire metric fibre is exactly a periodic collection of binary
equalities, disequalities, and pins. An actual tiling supplies a feasible
infinite assignment. The [periodic binary equality fibre lifting
lemma](periodic-binary-equality-fibre-lifting.md) supplies a periodic assignment,
possibly on a larger finite cover. All angle stars are still legal because the
placements stay inside their original colour fibres. All whole-side matches
are legal by the retained binary constraints. The reviewed global encoding's
periodic development therefore realizes a periodic Euclidean tiling by the
original fixed shapes. Reflected placements are one of the two choices, and
were never omitted or forced to share a colour period.

## Alternating A with side period two

Assume (ALT,ALT) and native A sides E,O,E,O,E,O. If E!=O, every A corner has
unordered incident side pair EO. At a trivalent vertex there are exactly two
A sectors and one B sector. The ray shared by the two A sectors has one length;
each of their other rays has the other length. The two rays bounding the B
sector thus agree. This holds at every B corner, so all consecutive B sides
agree and B is equilateral, of length E or O. If E=O the same conclusion is
immediate. This local ray argument is unaffected by reflections. The underlying
homogeneous-corner observation also occurs in the previously reviewed
[alternating-species corner-budget lemma](branching-hexagon-new-alternating-species-elimination.md);
the new step here is the explicit sufficient metric witness for these angles.

The index-three torus has HNF (3,1,1), whose cell representatives are (0,0),
(1,0),(2,0), with B at the first. Set corner phase zero globally. For B length E,
give the placements

    (B,r=0,s=+1), (A,r=0,s=+1), (A,r=0,s=-1).

For B length O exchange the two A placements. The certificate checks all six
canonical vertex stars and all eighteen directed side seams for each witness,
using native side indices r+k for s=+1 and r-k-1 for s=-1. Native A side classes
are (0,1,0,1,0,1), with all six B classes 0 or 1 respectively. Their angle stars
are exactly the prescribed same-colour AAB triples. Periodic development gives
the claimed Euclidean tilings for any fixed strictly convex shapes having these
angles and side lengths. With E=O the two witnesses merge without difficulty.

## Review boundary

The producer uses only integer words, exact side indices, Cartesian products,
and finite graph pruning; no solver timeout or numerical geometric test enters.
The infinite C,C metric conclusion additionally depends on the separately
proved signed-graph lifting lemma and the reviewed hexagon reduction and
development theorems. Independent verification passed for the finite
census and both metric specializations. No larger native-ring search is
proposed by this record.
