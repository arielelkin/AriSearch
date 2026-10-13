# A single adjacent cross-palette equality cannot carry the ternary interface

Date: 2026-10-13. Status: independently adversarially reviewed VALID;
[fresh hostile review](../reviews/two-hexagon-single-cross-palette-fresh-hostile-review.md).
The earlier [root audit](../reviews/two-hexagon-single-cross-palette-review.md)
is retained separately.
This is a family obstruction, not a sample exclusion or a global classification.

## Statement

Use the generic complementary ternary star language from the reviewed
[star lemma](two-hexagon-ternary-angle-star-balance.md). Let actual strictly
convex A have native angle word012012 and side classes

    (L,L,M,P,Q,V), with L,M,P,Q,V pairwise distinct.

B has two corners of each complementary colour, in any of its11 bracelets,
and arbitrary actual lengths. Reflected copies and original partial contacts
are admitted. There is no connected genuinely mixed defect-free field.
Indeed A cannot occur in any defect-free field. The pair tiles the plane
if and only if B tiles monohedrally, and every tileable pair admits a periodic
escape with A omitted. This conclusion uses the reviewed defect-free-limit
and unrestricted monohedral convex-hexagon dependencies; it does not assert
purity of every original tiling.

The statement holds throughout this length stratum at every generic angle
triple. In particular it includes every actual member of the checkpoint family
(L,L,M,L-lambda*sin54,L+lambda*sin113,M-lambda*sin59), with the stated five
distinct classes. Neither rational parameters nor the fixture(4,6,1) are
hypotheses. Extra coincidences and nongeneric angle lines are excluded.

## Forced seam neighbourhood, including reflections

Side0 has endpoint colours0/1; side1 has1/2. Up to exchanging the two tiles
and the spatial endpoints there are exactly two endpoint bijections.

* Pair corners(0,2) and(1,1): the former needs an A colour1 corner, while the
  latter needs a B colour1 corner. At the pure endpoint the remaining rays
  have lengths V,M. A corner1 offers L,L and corner4 offers P,Q. Neither
  matches V,M, in either order. The mixed endpoint would force B arms L,L.
* Pair corners(0,1) and(1,2): both endpoints would be pure. The first needs
  colour2 with arms V,L; its available native pairs are L,M and Q,V. The
  second needs colour0 with arms L,M; its available pairs are V,L and M,P.
  Neither endpoint can be completed.

These bijections cover direct and reflected copies; each exposed arm pair
is tested in both orders. There is no legal transition state, hence no
interface successor and no interface cycle to develop into an infinite field.

## Reusable spatial gates

The six A corner arm pairs are

    colour0: (V,L), (M,P)
    colour1: (L,L), (P,Q)
    colour2: (L,M), (Q,V).

An AAA star must use one corner of each colour. If its colour1 corner is
(L,L), the other corners must be(V,L) and(L,M); their remaining rays V,M
cannot match. If it is(P,Q), the other corners must be(M,P) and(Q,V), with
the same mismatch. These cases exhaust all native choices, circular orders
and reflections. Thus no AAA star exists even without a mixed-field premise.

The two native arm sets of any fixed colour are disjoint. At an AAB star
the two same-colour A corners therefore use the same native slot. Matching
their AA arm forces their two remaining arms equal, including the repeated
L,L corner. Consequently the two B sides at EVERY mixed B corner are equal.
The B-B propagation gate removes BBB in a genuinely mixed connected field,
so all B sides have a common length. Allowed classes by B colour are

    colour0: {L,M,P,V}; colour1: {L,P,Q}; colour2: {L,M,Q,V}.

Their intersection is{L}: mixed B must be equilateral with side L.
Every B side matches an A side, whose distinct endpoint colours prohibit
adjacent equal B colours. In a six-cycle with two occurrences of each colour
and no same-colour edge, incidence counting gives exactly two edges of each
pair01,12,02. But the only A sides of length L have pairs01 and12. A B02 edge
has no possible A neighbour. This proves mixed-field impossibility for all
B orders, without a closure or torus search.

Finally pure A is also impossible because its required AAA stars are empty.
The defect-free limit of any admitted original tiling is therefore pure B.
The monohedral theorem supplies an admitted periodic tiling. Conversely a
monohedral B tiling is already an admitted tiling of the pair.

## Early exact B closure and its scope

The spatial gate reduces the entire mixed-family B closure query from5^6
side words per bracelet to constant words. At the fixed fixture angles, the exact checker tests all11
bracelets and all five positive constant classes: closure is length times
a fixed cyclotomic residue. Only012012 closes in that angle fixture.
The independent [all-generic-angle proof](../reviews/two-hexagon-single-cross-palette-fresh-hostile-review.md)
uses symbolic unit-turn factors and reciprocal resultants to prove the same
constant-length classification at every generic angle triple. The fixture
residues alone do not prove that all-angle statement. The subsequent class
intersection retains only length L.
This covers every spatially permitted family candidate; untested nonconstant
family assignments were already removed by a proven local necessity.

Separately, an intentionally relaxed exact fixture query at(4,6,1) tests all
11*5^6=171875 assignments. Only012012 closes, with125 assignments: precisely
its5^3 opposite-equal length words. The other ten fixture exclusions are
SAMPLE ONLY for unrestricted nonconstant B assignments. They are not elevated
to all-parameter closure theorems. The actual author fixture verifies exact
A closure, positivity and every strict nonincident support determinant.

Equilateral B012012 is centrally symmetric. The audit verifies a single-cell
translation carrier: all six vertex links have angle sum360, opposite sides
match with reversed endpoints, and two translation generators have exact
positive determinant equal to polygon area. The standard central-hexagon
translation construction therefore covers the plane. This is a pure-B
periodic escape, never a mixed interface carrier or evidence of an infinite
extension of one of the125 relaxed polygon closures.

[Producer](../searches/two-hexagon-single-cross-palette-interface.py),
[certificate](../certificates/two-hexagon-single-cross-palette-interface.json),
[separate checker](../reviews/verify_two_hexagon_single_cross_palette_independent.py).
