# Fresh hostile review: universal Ammann areas and the algebraic rank3 source

Date:2026-10-13. Reviewer:luna, independent of sol area author and producer.
**Verdict: VALID** for the symbolic area formulas/rank criterion, exact N1000 generic source certificate, area-rigid content theorem and their stated source-fusion scope. The stronger uniform-resection theorem makes rank3 unnecessary for singleton exclusion, but this area result remains independently reusable.

## Claims and dependency policy

Reviewed [the artifact](../lemmas/ammann-area-rigidity-and-whole-tile-fusion.md) and [no-producer-import checker](verify_ammann_area_rank_three_independent.py). Exact indexed source vertex formulas and G* forcing hypotheses were checked for applicability; their settled reconstruction/forcing proofs were not repeated. The universal source frequency result has a separate independent VALID review. Here the new obligations are area normalization, rational-rank quantifiers, exact geometric sample, phase/prime certificate and congruent whole-patch content uniqueness.

## Universal shoelace formulas and pointwise rank

With w=exp(i*pi/5), sigma=Im(w)>0, complex shoelace area divided bysigma is

    sum(conjugate(p_i)*p_(i+1)-p_i*conjugate(p_(i+1)))/(2*(w-conjugate(w))).

The factor is correct: ordinary area uses denominator4i and w-conjugate(w)=2i*sigma. Conjugation fixes the real symbols s,t. Independent polynomial substitution overQ(w)[s,t] returns

    H:1, P1:phi-f, P2:f,
    f=(s^2+phi*s*t+t^2+(phi-2)t)/2.

These are oriented identities for arbitrary real parameters; unsigned positive-area applications are restricted to actual positive convex polygons inD. Reflection preserves unsigned area. Multiplication by the common nonzero scalar sigma preserves rational rank even though sigma need not lie in the smaller coordinate field used for normalized areas.

The three coefficient rows at constant1,constantphi,s^2 have determinant1/2. Thus there is no universal homogeneous rational area relation. At a fixed parameter, a relation isqH+q1*phi+(q2-q1)f=0. If f is outsideQ(phi), rational coefficients forceq2=q1 and thenqH=q1=q2=0. If f=A+Bphi, the span is exactlyQ(phi), because1 andphi already lie in it, and its kernel generator(-A,-B,1-B) is correct. At(9/20,3/4), clearing denominators indeed yields primitive(294,-435,365).

The level-curve/full-measure statement follows from countability ofQ(phi) andpartialf/partials=s+(phi/2)t>0 on0<s,t<1. It is not an open area-rank3 condition. Rational s,t necessarily give rank2, so no rational sample is incorrectly promoted to area independence.

## Explicit sample and exact field

For s=9/20,t=3/4+sqrt2/N, the displayed f_N follows by direct expansion. The basis1,phi,sqrt2,phi*sqrt2 is rationally independent inQ(sqrt5,sqrt2), and the three area rows have minor-1/(4N). This proves normalized and actual area rank3 for each nonzeroN, but onlyN1000 is claimed to meet the geometric/source forcing domain.

The checker constructs w as the canonical positive-imaginary tenth root of unity and uses the positive real square root of2. It verifies the degree8 polynomial ofw+sqrt2 exactly, its irreducibility and its specified QQbar embedding. It reconstructs all three polygons, verifies0<s,t<1 and all54 strict global support inequalities, and computes the normalized areas independently. The four label lengths are distinct; positivity follows from genuine nonzero source sides proved by the strict supporting determinants. ThusD andG1 hold. Six versus five source corners and the distinct source edge-label multisets keep the three congruence classes distinct under reflections.

No floating angle or visual containment check is load-bearing. Normalized area conversion into the degree8 field is justified by the exact identities and independently confirmed coefficient vectors; it is not a claim that the common area factor sigma must belong to that field.

## Prime valuations imply full genericity

The native phase ratios are reconstructed at exactly the reviewed H-J',H-J'' andP1-K corners. Strict positive source orientation gives their arguments in(0,pi). Each q=rho/conjugate(rho) isexp(2i*angle) in the exact degree8 field.

The retained small prime ideal bases are reconstructed directly in that field. For norms281,3391,401, the checker proves primality/norm and recomputes the actual valuation rows(0,0,-1),(1,0,0),(1,-1,-1). Their determinant is1. It does not need to trust the other retained factorization supports or perform a larger principal-ideal factorization.

Any rational relation involvingpi,chi,psi,kappa can be cleared to integer coefficients and exponentiated at2i. The resulting multiplicative relation among q values has zero valuation at every prime; the nonsingular three-row matrix therefore forces all angle coefficients zero, after which the pi coefficient is zero. This provesG2, hence reviewedG2', for the exact sample. Norm coincidence or a wrong field embedding would be caught by the independently reconstructed q values and ideal valuations, not accepted merely from claimed certificate rows.

The independent checker was run successfully: PASS universal polynomials/rank3,54 exact supports,G1 and the three small-prime rows, givingG* and area independence.

## Congruent supports and source-fusion quantifiers

For finite patches of whole source tiles with disjoint interiors, unsigned support area is the sum of source areas with integer counts; polygon boundaries have measure zero. Congruent supports preserve it under any isometry, including reflection. Rank3 therefore forces their source count vectors equal, without recognizability or unique spatial dissection. Fixed macro support area bounds all possible dissection tile counts, and its compact diameter bounds anchor displacement.

At such a source, a support congruent to sourceP1/P2 inherits its singleton content automatically. Combining with independently reviewed universal source ratios excludes the fixed-content singleton compiler. The claimed rank3-domain conclusion is valid, but the separately reviewed uniform unmarked resection theorem strengthens it to allG* parameters and all dissections of a tileable macro pair. Rank2 algebraic equal-area content differences alone do not establish congruent geometry or justify reopening variable-content rescue.

For two nontrivial whole-source macros, balance/rank/cone conditions remain necessary only. They do not imply convexity, tilability or forcing. The subsequently reviewed balanced-macro parity theorem now excludes pentagonal supports throughoutG*, independently of area rank; this does not invalidate the reusable area theorem.

## Attacks, repairs and scope

Checked normalization errors, oriented-versus-unsigned area, reflected supports, rational parameter rank confusion, wrong embedding/square-root branch, area-only genericity assumptions, omitted support constraints, prime-row reliance and variable dissection quantifiers. No consequential defect was found; no repair is needed.

The theorem does not assert allN are admissible, area independence implies angle genericity, rank2 kernels realize congruent patches, or any final two-tile construction exists. Final verdict: **VALID on the stated pointwise/universal area and source-fusion scope**. No novelty or unrestricted solution is implied.
