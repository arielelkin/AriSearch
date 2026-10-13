# Two-target source-by-source cuts obey an exact area module

Date:2026-10-13. Author:luna, incorporating root's modular obstruction.
Status: **[fresh independent hostile review VALID](../reviews/ammann-source-by-source-two-area-module-fresh-hostile-review.md)**. This is a compiler exclusion, not unrestricted two-convex-tile impossibility.

## Compiler definition and finite question

Fix three actual source shapes H6,P1,P2 of positive areas aH,a1,a2. A source-by-source two-target compiler gives a finite exact dissection of EACH source shape into isometric copies of only two target shapes P,Q, with disjoint interiors and exact source support. Reflections and partial contacts are allowed. The source boundary is retained as a union of target boundaries: target pieces do not cross source boundaries. The counts may differ arbitrarily among source classes; no matching, periodicity, recognizability, substitution scale or source density is assumed.

Before geometric search, ask whether the three source areas belong to the nonnegative integer span of the two target areas. Failure excludes every such dissection, independent of exact cut positions or target angle words. Success is necessary only, and supplies no convex pieces, plane extension or shape-only forcing. Cross-boundary recomposition changes this used hypothesis and requires an explicit new proposal.

## General area-rank and integer-kernel gate

Let bP,bQ be the target areas, and let n_iP,n_iQ be the nonnegative integer piece counts in sourcei. Then

    a_i=n_iP*bP+n_iQ*bQ.

Thus the rational rank of the three source areas is at most2. If it is3, NO source-by-source two-target compiler exists, regardless of source/target convexity or piece number.

If the source area rank is2, the two target areas must be rationally independent: otherwise their rational span would have dimension at most1. Their rational span consequently equals the source area span. Let kappa=(kH,k1,k2) be a primitive integer generator of the one-dimensional source area relation space, so

    kH*aH+k1*a1+k2*a2=0.

Substitute the dissection counts. Rational independence of bP,bQ forces separately

    kH*n_HP+k1*n_1P+k2*n_2P=0,
    kH*n_HQ+k1*n_1Q+k2*n_2Q=0.

Hence, for sourcei and either targetj, n_ij is divisible by

    d_i=gcd(|k_l|,|k_m|)/gcd(|k_i|,gcd(|k_l|,|k_m|)),

where l,m are the other two source indices. The gcd in the numerator is positive because a nonzero relation among positive areas has at least two nonzero coefficients. This is only an arithmetic necessary condition; it does not provide an actual dissection.

The proof covers arbitrary real target areas and does not assume they are predeclared algebraic. Rank2 forces them into the rational source-area span. It also excludes a compiler using only one target class, because that span has rank1.

## Generic Ammann area-rank3 coverage

For reviewed Ammann coordinates, normalized by sigma=sin36>0,

    aH/sigma=1,
    a1/sigma=phi-f(s,t), a2/sigma=f(s,t),
    f=(s^2+phi*s*t+t^2+(phi-2)t)/2.

The [area-rank theorem](ammann-area-rigidity-and-whole-tile-fusion.md) gives rank3 exactly when f is outside Q(phi). Thus EVERY source-by-source two-target cut compiler is excluded at every such actual parameter. This covers the explicitly checked N1000 parameter and the area-rank3 part ofG*, without any new dissection enumeration. The area-rank artifact has its separate fresh-review gate; the general linear-algebra statement here does not depend on its prime certificate.

Parameters with area rank2 remain subject to the exact integer-kernel gate. They are not silently excluded by success at rank3.

## Complete H two-piece-cut exclusion at the reviewed rational sample

At the existing reviewed source sampleJ0=1/2+(4/5)w,

    aH/sigma=1,
    a1/sigma=71/200+(2/5)phi,
    a2/sigma=-71/200+(3/5)phi.

Their rational rank is2 and their primitive integer relation is

    -71*aH+120*a1-80*a2=0.

For either target shape, source dissection counts consequently satisfy

    -71*n_H+120*n_1-80*n_2=0.

Reduce modulo40. Since gcd(71,40)=1, EVERY target-type count in H is divisible by40. A nonempty H dissection into P,Q must therefore have at least40 pieces. In particular **no two-piece dissection of H into the two final target classes can be completed by source-by-source dissections of P1 andP2**, irrespective of cut/chord position, convexity, angle choices or reflections. This excludes the whole H two-piece-cut family atJ0, not merely the midpoint choice. No40/80-piece enumeration is justified by this necessary divisibility result.

## Concrete retained-boundary midpoint seed and its stronger local failure

A changed-hypothesis seed cut H by the chord joining the midpointsq of native side0 andr of native side3, while retaining the original source boundary. The two boundary words are

    P=(q,H1,H2,H3,r), Q=(r,H4,H5,H0,q).

Their exact coordinates, supporting half-plane checks and source containment are retained in [the local certificate](../certificates/ammann-h-midpoint-two-pentagon-cut.json). Each is a genuine convex pentagon. Atq,r, two opposite boundary rays plus the noncollinear chord give degree3; an uncut exterior source neighbor contributes a flatpi sector. This genuinely escapes the old erased-boundary degree2 attachment hypothesis and the whole-source balanced parity theorem.

Both pieces passed all150 known pentagon-family relabelings each (300 tests), so they avoid the imported monohedral pentagon families at this exact sample. This is retained finite computational evidence about local shapes, not infinite tilability or a credible aperiodic pair. Those inexpensive tests were run before the root's area-first steering arrived; the following cheaper area rejection is decisive and should precede any future such census.

The normalized piece areas are

    bP/sigma=559/800-(9/80)phi,
    bQ/sigma=241/800+(9/80)phi.

Their rational coefficient determinant is9/80, so each source area has a unique rational P/Q count expression. For sourceP1 it is

    (nP,nQ)=(-1289/1800,5111/1800),

and for sourceP2,

    (nP,nQ)=(-1177/600,2023/600).

Both require negative P counts. Hence this fixed midpoint compiler fails even the nonnegative rational area gate, independently of the stronger family-wide modulo40 exclusion. There is no compatible retained-boundary completion of the two local words across all three source classes.

## Status, exact residuals and restart rule

The local pentagons remain exact geometric features with genuine degree3 boundary endpoints. The retained-source-boundary compiler is **falsified** at the fixed midpoint seed, and the entire H two-piece-cut source-by-source family is **excluded** atJ0 by the integer kernel. Rank3 parameters exclude all source-by-source two-target cuts. No target aperiodicity follows from having local nonmonohedral pentagons.

Residual mechanisms require an explicit changed hypothesis: a rank2 source parameter with arithmetic-compatible higher-piece dissections; source cuts followed by specified cross-boundary reassembly; or a different source/forcing mechanism. The modulo40 lower bound is not a reason to enumerate40 or80 pieces. Without an actual compatible geometric reassembly, treating the arbitrary P/Q infinite covering as the next unexplained lemma would replace the original problem by an equally difficult obligation, so that local route is blocked and effort should redirect.

Source-by-source cuts alone also do not transfer source aperiodicity to every target tiling: target recognizability or a different shape-only forcing argument would still be required. The whole-source uniform-resection theorem runs in the opposite direction and must not be applied to fractional target pieces as if they were whole-source-supported macros.

## Artifacts and nondestructive replay

* [Local cut producer](../searches/ammann-h-midpoint-two-pentagon-cut.py) and [certificate](../certificates/ammann-h-midpoint-two-pentagon-cut.json): one source sample, one chord, two pentagons,300 known-family tests; no source enumeration.
* [Fixed-seed area certificate](../certificates/ammann-h-midpoint-cut-area-gate.json) and [independent exact geometry/area checker](../reviews/check_ammann_h_midpoint_cut_area_gate.py): reconstructs the affine source vertices and target cut, checks convexity/degree3 endpoints/area partition and the unique negative rational counts, with no producer import or solver.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_ammann_h_midpoint_cut_area_gate.py --check research/certificates/ammann-h-midpoint-cut-area-gate.json

The family-wide rank/modular arguments are exact linear algebra, not a bounded search. Fresh hostile review should check the primitive integer kernel, rational independence of target areas and source-by-source versus cross-boundary quantifiers. No novelty or unrestricted solution is claimed.
