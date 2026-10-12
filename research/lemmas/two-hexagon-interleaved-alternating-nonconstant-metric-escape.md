# Nonconstant odd lengths in the interleaved/alternating family have a periodic escape

Date: 2026-10-12. Status: [independently reviewed VALID](../reviews/two-hexagon-interleaved-alternating-private-transport-review.md)
for the complete metric-word gate and twelve nonconstant periodic witnesses.
The equal-odd residue is covered separately by the [index-nine torus review](../reviews/two-hexagon-interleaved-alternating-equal-odd-torus-review.md).

Fix strictly convex hexagons A,B in the same-colour AAB angle family, with
native A word I=(p,p,q,p,q,q), B word ALT=(r,s,r,s,r,s), p+q=240,
r=360-2p, s=2p-120, 90<p<150, p!=120. If A's odd native lengths A1,A3,A5
are not all equal, the pair is untileable or admits a periodic tiling.
The original problem permits reflections, partial contacts, and omission of
a type. No unmarked source inheritance is invoked.

The independently reviewed [private-seam domain
lemma](two-hexagon-interleaved-alternating-private-seams.md) supplies the full
necessary domain in the admitted trivalent limit: all odd A sides meet B,
all even A sides meet the same native A side index, and every B side has a
length from the odd A alphabet. If a block U of equal odd-native A lengths
has size |U|, precisely2|U| B sides have that length. Coincidences with even
A lengths do not change these restrictions.

## Exact constrained finite domain

Use the five restricted-growth partitions of A1,A3,A5,

    000, 001, 010, 011, 012.

These yield1,15,15,15,90 native B side words, respectively:136 in total,
without quotienting by native rotations or reflections. The all-equal case
000 is retained in the computation but excluded from this theorem's metric
assumption. All full native B rings are first enumerated by same-colour corner
stars, including every reflected placement:49152. Requiring odd AB sides
leaves8748. Requiring all six local AA seams to use the same native A side
index leaves216. The root domain lemma proves these filters necessary,
independently of side coincidences.

For each metric word, retain precisely the216-domain states whose six AB
seams match that partition and B word. Across coarse direction k, compatibility
is equality of shared full native A placements k,k+1 and k+4,k+3. Necessary
triangle-support deletion uses supported j,l in directions k,k+1 with j to l
in direction k+2. The [producer](../searches/two-hexagon-interleaved-alternating-private-transport.py)
retains all domain states, words, relations and deletion rounds in
[the certificate](../certificates/two-hexagon-interleaved-alternating-private-transport.json).
Exactly123 metric words have empty cores. The13 nonempty words consist of the
one all-equal word and these twelve nonconstant cases:

| Odd A partition | Nonempty B native words |
|---|---|
| 001 | 001001, 010010, 100100 |
| 010 | 000110, 011000, 100001 |
| 011 | 001111, 110011, 111100 |
| 012 | 002112, 120021, 211200 |

Each nonconstant case has12 full native ring states with maximum outdegree2
in all six directions. Branching does not by itself establish aperiodicity.

## Full-native overlap quotient and direct metric witnesses

Group each of these12-state cores by its entire six-entry native A ring,
retaining six signatures with two B choices per signature. This is a full
native overlap signature, not a binary corner-colour projection. Compatibility
depends only on the A ring, so choosing any representative B centre for each
signature preserves all overlap relations.

Order the six signatures lexicographically. All twelve quotient systems have
the same successor permutations

    F0=(1 4)(2 3), F1=(0 5)(2 3), F2=(0 5)(1 4), F(k+3)=Fk.

In particular the orbit {0,5} has F0 identity and F1,F2 exchanging its two
states. Choose signature0 at B cells h=x-y=0 modulo6 and signature5 at B
cells h=3 modulo6. At each centre select the first retained native B
representative and its native A ring. Shared A placements agree, giving a
full native torus of HNF(6,1,1).

For each of the twelve cases the certificate retains the resulting six
full labels, twelve canonical vertex stars,36 directed matched seams and
the required native side equality closure. Its side classes are

    A=(e0,o[0],e2,o[1],e4,o[2]), B=the retained odd-class word,

with e0,e2,e4 treated as three independent classes distinct from the odd
alphabet. Every AA seam is self-indexed, and every AB seam already matches
the word exactly. Thus the witness requires **no equality between different
even A sides** and no additional odd-length identification. Extra coincidences
in an actual fixed metric preserve all matches.

The native angle stars are checked exactly using the r+s*k corner map;
reflected side indices use r-k-1. The reviewed periodic-label development
theorem converts each legal torus to a periodic Euclidean tiling for any
actual strictly convex pair with those angles and side classes. The side
lengths may otherwise be arbitrary positive values satisfying the two
polygons' own closure equations. Hence an admitted tiling can only lie in
one of the twelve retained nonconstant metric words, and in every such case
the explicit torus gives a periodic escape. This proves the stated theorem.

The all-equal odd case retains216 rings and36 overlap signatures; its quotient
is not functional. It needs a separate geometric argument and is not covered
by the present theorem. Neither a periodic corner-colour projection nor a
failure of bounded periodic search is used in this proof.
