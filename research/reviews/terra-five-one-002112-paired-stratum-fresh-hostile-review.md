# Fresh hostile review: paired A002112 B-closure separator

Date: 2026-10-13. Reviewer: sol. Verdict: **VALID** on the exact native side stratum (a,a,b,b,c,c), at every angle in the stated open interval except x=120. This is not arbitrary-metric A002112 coverage.

## Analytic reconstruction

With u=180-x, the listed native edge directions follow from the A word 002112 by cumulatively turning through (u,w,v,v,u,w); grouping yields (1+U, -(1+U^5), U^-1-U^-5). Their positive magnitude arguments are u/2,5u/2,450-3u. All three cyclic gaps lie strictly below 180 and above zero on 54<u<67.5, so these three nonparallel vectors have a unique positive real closure relation up to scale.

I independently checked in Q(U) that the displayed rational-function forms

    c/a=U^5(1+U)/(1+U^11),
    b/a=U^4(1+U)(1+U^7)/((1+U^5)(1+U^11))

annihilate the grouped closure exactly. On the unit circle they give precisely the displayed cosine ratios. Their denominators do not vanish in the interval. The signs of c-a and c-b follow from the cosine-difference identities with the negative cos(5u/2) factor retained. Thus a>c>b for u>60 and b>c>a for u<60. Equality specializations inside this positive stratum do not remain open: every such equality would require u=60, outside the statement.

## All native fan choices and BB signs

The independently reviewed capacity theorem supplies a saturated B field or a pure-A escape. Native A002112 has no 22 side, eliminating masks {1,3} and {2,4}; the remaining mask {1,4} has AB endpoint pairs 12 on sides 0,5 and 02 on sides 2,3. Direct native-index enumeration gives A0 AB/AA arm pairs (a,a),(c,a), and A1 pairs (b,b),(c,b). Thus the two central AAB fans allow all sixteen independent assignments advertised in the lemma. No distinct-length assumption precedes closure; distinctness was proved from the positive A relation.

For B direction E=exp(iR), R=180-2u, the unknown columns are E,E^4. Cross-product Cramer's rule gives D=sin(3R)=sin(6u), and exactly the two numerators in the lemma. The coefficient signs are essential: -sin(4R),sin(R),sin(2R),cos(R) are positive throughout 45<R<72. For u>60 both positive-coefficient AB lengths are at most c and both negative-coefficient lengths at least c; for u<60 the order reverses. The common numerator bound is -c(sin(4R)+sin(2R))=-2cDcos(R). Dividing by D with its correct sign gives both p,q<=-2c cos(R)<0. This rules out even positive B closure, before convexity or B-chain extension is considered. Reflections reverse the developed directions by a global isometry and preserve this obstruction; B can always be indexed from its unique s corner with one of the two cyclic orientations.

## Rational fixture and scope

I read and replayed the retained no-producer-import checker:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_002112_rational_geometry.py

PASS. The independent rational reconstruction uses U=(8+15i)/17, exact angular interval bounds, grouped closure formulas, all strict nonincident supports, all twelve cyclic/reflected H1/H2 tests, and all sixteen BB closure equations. The three selected corners 0,4,2 have consecutive outgoing/incoming arms (a,c),(c,b),(b,a). Three rotated whole convex copies can therefore be placed in consecutive interior sectors summing 360, with matching common radial side endpoints and disjoint interiors. This supplies an actual AAA patch, not only a metric-star signature. H3 is excluded since no angle is 120. The imported unrestricted monohedral classification is an already settled dependency; it was not re-audited here.

What is proved: the whole positive paired-side stratum cannot support the saturated mixed field, despite genuine nonmonohedral AAA geometry. If an original pair in this stratum tiles, the reviewed saturation reduction must instead give a pure-A limit and hence a periodic omission escape; for the distinct-angle paired stratum the H-family tests actually forbid that pure-A alternative too, so such pairs are untileable. The latter follows only with the imported monohedral theorem and is not needed for the separator.

What remains open: other AAA length-equality patterns, including four-class and non-paired metrics, and the distinct no-AAA branch until separately reviewed. No AAA-implies-monohedral claim or all-A002112 theorem follows. A new native equality pattern whose closure changes the fan-order premise is a justified next test; another angle sample of this eliminated stratum is not.
