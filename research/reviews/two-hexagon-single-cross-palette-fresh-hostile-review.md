# Fresh hostile review: one adjacent cross-palette equality

Date: 2026-10-13. Reviewer: independent sol agent, not the result author or
root auditor. **Verdict: VALID** under the theorem's exact hypotheses.

## Claim and assumptions

The reviewed claim is the full length stratum: actual strictly convex A with
native colours 012012 and lengths (L,L,M,P,Q,V), with five pairwise distinct
positive lengths; B has two copies of each generic complementary colour.
There is no defect-free field containing A. Any originally admitted plane
tiling therefore supplies a pure-B defect-free limit and an admitted
monohedral periodic escape. Reflections, partial original contacts and
omission remain admitted. No arbitrary-metric classification of A012012 is
claimed. Extra equalities and additional angle stars are excluded.

The generic star language, B-B propagation, defect-free-limit theorem and
unrestricted monohedral convex-hexagon theorem are previously independently
reviewed dependencies. This review checks their application and does not
re-audit their settled proofs or imported literature.

## Independent spatial reconstruction

A native corner has the unordered arm sets
colour 0: {V,L}, {M,P}; colour 1: {L,L}, {P,Q}; colour 2: {L,M}, {Q,V}.
A pure star is a three-cycle with one native corner of each colour and one
length on each cycle edge. Choosing colour-1 corner {L,L} forces colour-0
{V,L} and colour-2 {L,M}; their third edge requires V=M. Choosing {P,Q}
forces {M,P} and {Q,V}, again requiring V=M. This proves AAA emptiness
without closure, circular-order assumptions or fixture arithmetic.

At any AAB corner, both A colours agree. The arm sets of the two native
slots at that colour are disjoint. Equality along their common AA ray thus
requires the same native slot. Their other two arms then agree, so the
incident B sides agree. With no B-B edge in a genuinely mixed field, every
B corner is mixed; cycling around a B tile makes all its sides one length.
The possible remaining-arm palettes intersect in {L}, forcing that length.
Every incident A side is therefore native side 0 or 1, with endpoint colours
01 or 12. Because mixed stars identify B colour with its two A colours, B
cannot have a same-colour side, nor a 02 side. But six B corners containing
two copies of each colour cannot have all edges 01/12: each colour-0 and
colour-2 corner would require two colour-1 neighbours, giving eight required
incidences against the four available at colour 1. Contradiction.

This arm-cycle proof admits both cyclic orientations and arbitrary reflected
native placements. Pure A also requires the eliminated AAA stars. A pure
BBB star includes a B-B edge and propagates to a pure B field. These three
possibilities exhaust every connected defect-free field. The original tiling
is never assumed defect-free or pure, and the translated limit need not
retain A. This is precisely why a monohedral omission escape is valid.

## Attacks and computational check

Attacks checked: alternative AAA arm pairings; reflected same-colour fans;
nonconstant B metrics; adjacent equal B colours; loss of A in the limit;
noncentral B bracelets; and specializations of the five length classes.
No surviving counterexample exists under the hypotheses. Further length
specializations cannot be inferred from this result and must be analyzed
separately; the hypothesis pairwise distinct is consequential.

The existing no-author-import exact checker was independently replayed against
the retained certificate. It checks 1728 native triples, all reflected AAB
fans, all 90 labelled cyclic B words, and the stated fixture closure domain.
The core spatial proof does not depend on those fixture closures.

One evidence-scope issue was found: the original cyclotomic constant-B
closure test uses the single angle triple (134,118,108), so by itself it is
not a symbolic all-angle closure certificate. The obstruction theorem does
not require that claim. Nevertheless the all-generic-angle closure claim
has the following independent analytic proof, removing any ambiguity.

## All-generic-angle constant B closure

Let a,b,c be the three B exterior turns. They lie in (0,180) and sum to 180.
Set u=exp(ia), v=exp(ib), w=exp(ic)=-1/(uv). Unit-edge closure for a bracelet
is the sum of the six successive products of its turns. Among all eleven
bracelets, 012012 has identically zero residue. Six others factor using
u+1, v+1, uv-1, u-v, u^2 v+1 or uv^2+1. The first three cannot vanish in
the positive-turn domain; the latter three require respectively a=b, a=c
or b=c, since a+b+c=180. Equal colours are nongeneric because they create
additional mixed native-colour triples.

For the four remaining bracelets, clear denominators to obtain P(u,v).
Unit modulus makes the reciprocal polynomial P(1/u,1/v) vanish whenever
P does. Their exact resultants in v are:

- 001122: (u+1)^6 (u^2-u+1).
- 001212: -(u+1)^2 (u^2-u+1).
- 010122: 2u^2 (u+1)^2 (u^2-u+1).
- 011202: 2(u+1)^2 (u^2-u+1).

In 0<a<180 these imply a=60, hence B colour-0 angle 120 and its
complementary A angle 120. The latter permits an extra AAA same-colour
star and is nongeneric. Thus only 012012 can close at generic angles.
This algebra is verified independently by the retained symbolic checker
(SymPy 1.14.0; no solver, seed, symmetry of angle names, or timeout).
Its finite domain is exactly the eleven dihedral bracelets; elimination is
exact and complete. Possible outcomes were a noncentral generic closure
(which would refute the ancillary closure classification) or its exclusion.
The latter occurred. This permits the classification to be retained as an
all-angle necessary gate; it adds no mixed-extension mechanism.
It proves a necessary closure classification, not joint A/B realizability
or any mixed infinite extension. The unit 012012 polygon is centrally
symmetric, and its standard central-hexagon carrier is an omission escape.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_single_cross_palette_generic_constant_closure.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_single_cross_palette_independent.py research/certificates/two-hexagon-single-cross-palette-interface.json

No consequential defect remains in the reviewed theorem. The original
research problem, other native words, extra side equalities and nongeneric
angle strata remain unresolved.
