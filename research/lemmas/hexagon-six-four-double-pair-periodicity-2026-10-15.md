# Six-distinct versus four-distinct double-pair hexagons

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-six-four-double-pair-hostile-2026-10-15.md). No novelty claim and no general two-polygon resolution.

## Theorem and dependencies

Let A and B be compact convex hexagons with nonempty interiors and six actual
corners each. Suppose A has six distinct numerical native side lengths,
and B has exactly four distinct numerical native side lengths with
multiplicities (2,2,1,1). Suppose all four B lengths also occur among A's
side lengths.

If copies of A and B tile the Euclidean plane, with rotations, reflections,
and unrestricted partial contacts permitted, then these shapes admit a
doubly periodic tiling. If an everywhere-trivalent whole-side limit is mixed,
the periodic witness can be chosen to have a four-face flat-torus quotient
with two faces of each type.

Dependencies are the reviewed
[defect-free limit and monohedral hexagon periodicity facts](hexagon-limit-and-periodicity.md)
and the reviewed [formal four-triangle flat-torus construction](hexagon-holonomy-distinct-lengths.md).
The new ingredient is a finite actual-slot endpoint classification, followed
in twenty-two cases by explicit rational combinations of angle equations.
No trusted solver UNSAT assertion is needed.

## 1. Native slots and finite word normalization

Apply the defect-free limit theorem. A-only trivalent tiling is impossible:
its three ray lengths at a vertex would be distinct and give a triangle
in A's simple six-cycle of corner length pairs. If the limit uses only B,
the monohedral convex-hexagon result supplies a periodic escape. Hence it
suffices to treat a mixed everywhere-trivalent whole-native-edge tiling.
Both types then occur and all twelve actual corner slots occur.

Normalize A's numerical side word to (0,1,2,3,4,5). Two of these lengths
are private to A. They cannot be adjacent: at their corner both neighboring
tiles across the private sides would be A, giving an impossible AAA vertex
with a triangle in A's six-cycle. Up to dihedral relabeling of A, the private
pair is therefore {0,2} or {0,3}. The B alphabet is the corresponding four
other A labels.

For each private pair, enumerate all linear six-words on that four-symbol
alphabet whose multiplicities are exactly (2,2,1,1). Choose the two repeated
symbols in six ways and arrange their six occurrences in 6!/(2!2!)=180
ways, giving 1,080 words per alphabet and 2,160 total. Quotient only cyclic
rotation and reflection of B. This leaves 96 words for each private pair,
192 total; no unproved geometric or angle equivalence is used.

Side i has endpoint corners i-1 and i modulo 6. Corner i is AFTER side i,
between sides i and i+1. Use actual corner indices 0,...,5 for A and
6,...,11 for B. Repeated numerical lengths do not merge actual side or
corner slots.

## 2. Complete local encoding with repeated rays

For each numerical word, enumerate all multisets of three ray lengths,
including repeats. For each ray multiset choose one actual corner slot for
each of its three adjacent ray pairs. This produces the complete atlas
of possible unordered actual corner triples, with repeated corner indices
allowed. For example a p,p,p ray multiset may use three copies of one
actual p,p corner; such cases must not be discarded as non-triangular.

For each potential triple fix its sorted cyclic order and independently
flip the two native arms at each of its three corner occurrences. Keep
only flips matching numerical lengths along all three shared rays. These
are simultaneous native-arm microstates, distinguishing equal-length side
slots. For three corners, every permutation is a cyclic permutation of
that sorted order or its reversal; reversing every arm choice captures
the same native pairing data in the reversed order. Thus both cyclic
orders and every reflected tile possibility are included.

For each microstate and each of its three rays, follow the two matched
native sides to their actual opposite endpoint corners. Record that pair
as a multiset, preserving multiplicity. If S is the set of triples actually
used in a tiling, then every member of S has at least one microstate whose
THREE far-end pairs are each contained in some member of S. The same two
actual tile copies remain adjacent at the other end of their full side;
this is why the implication is valid. It does not assert any converse
extension from local data.

Starting with the full atlas, repeatedly discard triples having no such
microstate supported by the current atlas. Every actual support S survives
every deletion. Enumerate all subsets of the final atlas and retain exactly
those covering the twelve actual corner slots and satisfying the same
simultaneous-microstate endpoint condition.

The complete calculation retains twenty-four numerical words, twelve per
private-pair normalization. Their ninety-three endpoint-closed corner covers
are listed by count below. Every other one of the 192 numerical words lacks
a closed corner cover. No atlas relevant to this theorem exceeds twelve
stars after pruning; no subset domain was skipped.

| A private | B cyclic word | Closed covers | Direct-ring covers | Angle-span covers |
|---|---|---:|---:|---:|
| 0,2 | (1,3,1,4,3,5) | 4 | 4 | 0 |
| 0,2 | (1,3,1,4,4,5) | 1 | 1 | 0 |
| 0,2 | (1,3,1,4,5,5) | 1 | 1 | 0 |
| 0,2 | (1,3,3,4,1,5) | 1 | 1 | 0 |
| 0,2 | (1,3,3,4,4,5) | 1 | 1 | 0 |
| 0,2 | (1,3,3,4,5,5) | 3 | 3 | 0 |
| 0,2 | (1,3,4,4,1,5) | 1 | 1 | 0 |
| 0,2 | (1,3,4,4,3,5) | 3 | 3 | 0 |
| 0,2 | (1,3,4,4,5,5) | 1 | 1 | 0 |
| 0,2 | (1,3,5,4,1,5) | 4 | 4 | 0 |
| 0,2 | (1,3,5,4,3,5) | 4 | 4 | 0 |
| 0,2 | (1,3,5,4,4,5) | 3 | 3 | 0 |
| 0,3 | (1,1,2,4,2,5) | 1 | 1 | 0 |
| 0,3 | (1,1,2,4,4,5) | 2 | 2 | 0 |
| 0,3 | (1,1,2,4,5,5) | 1 | 1 | 0 |
| 0,3 | (1,2,2,4,1,5) | 1 | 1 | 0 |
| 0,3 | (1,2,2,4,4,5) | 1 | 1 | 0 |
| 0,3 | (1,2,2,4,5,5) | 2 | 2 | 0 |
| 0,3 | (1,4,2,4,1,5) | 27 | 16 | 11 |
| 0,3 | (1,4,2,4,2,5) | 1 | 1 | 0 |
| 0,3 | (1,4,2,4,5,5) | 1 | 1 | 0 |
| 0,3 | (1,4,2,5,1,5) | 1 | 1 | 0 |
| 0,3 | (1,5,2,4,2,5) | 27 | 16 | 11 |
| 0,3 | (1,5,2,4,4,5) | 1 | 1 | 0 |

## 3. Legal rings, including the twenty-two angle consequences

A formal ring is obtained by choosing four B side slots, one for each of
its four numerical values, and matching them with A's corresponding four
shared slots. Give each pair a common formal symbol and give every remaining
slot a separate private formal symbol. Both formal words have six distinct
symbols, four common and two private. Distinct private symbols may denote
equal numerical lengths. Retain the choice precisely when its formal graph
has four triangles partitioning all twelve actual corner slots. Its graph
is then the four-triangle ring of the dependency, with one private insertion
on each edge of a common four-cycle.

For seventy-one of the ninety-three closed covers, a ring's four actual
triples belong to the support directly, so all four angle sums equal 2pi.
In each of the other twenty-two covers a legal ring follows from exact
angle equations, even though not every ring star occurs in that support.
Here are the precise certificate semantics.

Measure angles in units pi and put X=(alpha_0,...,alpha_11,1). For an actual
star s, including multiplicities, let

    E_s=(multiplicity of 0 in s,...,multiplicity of 11 in s,-2).

Then E_s dot X=0 when that star occurs. The two polygon angle rows are

    H_A=(1,1,1,1,1,1,0,0,0,0,0,0,-4),
    H_B=(0,0,0,0,0,0,1,1,1,1,1,1,-4).

The retained certificate specifies a formal ring and, for each of its four
triples t, exact rational coefficients expressing E_t as a combination of
H_A,H_B and the occurring support-star rows E_s. The separate small checker
multiplies those coefficients and compares all thirteen entries exactly,
using Python Fraction arithmetic. Thus E_t dot X=0 follows for the ACTUAL
polygon angles, with no inference of real geometry from an abstract angle
model. These twenty-two verified row certificates establish four legal
ring sums for every remaining support.

## 4. Unbounded periodic witness

For a legal formal ring, choose opposite common cyclic orders for A and B,
reflecting B if needed. Give its common four-cycle alternating bits h.
Take four faces A0,A1,B0,B1, pair private same-native-slot sides between the
two copies of their type, and pair each common x side of A_i to B_(i xor h(x)),
always reversing boundary endpoints. All paired numerical lengths agree.
The four triangle types each become two circular trivalent vertices,
accounting for all twenty-four native face corners. The quotient is a
connected orientable surface with 4 faces, 12 edges and 8 vertices, hence
a torus. Its vertices have total angle 2pi by Section 3, so its original
polygon metrics define a compact flat torus without singularities.

Its complete simply connected flat universal cover develops isometrically
onto the Euclidean plane. The lifted original whole polygons cover that
plane with disjoint interiors. The torus deck group acts by a discrete
rank-two translation lattice. This supplies the claimed periodic witness.
The construction does not presume that the original tiling already obeys
the formal-symbol selection, or that any merely locally allowed patch
extends. It constructs a separate complete flat quotient from proved angle
identities. This completes the theorem.

## 5. Replay, finite scope and review

The standalone standard-library-only producer and its retained narrow record are
[hexagon-six-four-double-pair-certificate-2026-10-15.py](../searches/hexagon-six-four-double-pair-certificate-2026-10-15.py)
and [the certificate](../certificates/hexagon-six-four-double-pair-certificate-2026-10-15.json).
The exact proof domain is the 2,160 linear words and 192 cyclic words
specified in Section 1, the complete native-arm endpoint pruning, and all
subsets of the resulting atlases. Every one of the ninety-three retained
covers is listed with its support and a direct ring or rational row
certificate. Seventy-one direct rings and twenty-two angle combinations
account for every case. No exploratory triple-repeat model is executed,
imported, or needed by this producer.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-four-double-pair-certificate-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-four-row-certificate-check-2026-10-15.py

The [small row-certificate checker](../searches/hexagon-six-four-row-certificate-check-2026-10-15.py)
independently reconstructs the target formal rings, checks all seventy-one
direct support inclusions, and verifies every one of the twenty-two weighted
row identities without importing the producer or trusting its elimination
routine. The producer prints JSON to stdout and writes only with explicit
--output PATH, so proof replay does not overwrite retained evidence.

The proof-relevant computation uses only integers, finite multisets and
exact rational arithmetic; it has no random seed, geometry tolerance,
period-size bound, or solver resource assumptions. The historical all-shared exploration also retained Z3 angle
models, but neither that exploration nor those models is a proof dependency. A fresh independent verifier has audited the complete normalized domain,
simultaneous arm assignments, endpoint pruning, support enumeration and
actual torus gluings without importing the producer. Its replay passed:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-four-double-pair-independent-2026-10-15.py

This does not classify B multiplicities (3,1,1,1), two hexagons both with
repeated lengths, non-hexagons, or arbitrary convex pairs. Neither the
finite classification nor this restricted periodic escape resolves the
main problem.
