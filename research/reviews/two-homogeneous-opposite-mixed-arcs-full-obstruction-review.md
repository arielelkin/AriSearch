# Fresh whole-proof audit: opposite mixed homogeneous arcs

**Verdict: VALID for the complete scoped untileability theorem.**

Reviewer `consolidate` did not develop the manuscript, its H/L exceptional-curve reduction or the root-proposed native count cancellation. This review audits the complete [theorem](../lemmas/two-homogeneous-opposite-mixed-arcs-full-obstruction.md), including both formerly unresolved curves. It imports the independently accepted [phase audit](two-homogeneous-opposite-mixed-arcs-phase-review.md) and [off-curve audit](two-homogeneous-opposite-mixed-arcs-off-curve-obstruction-review.md), but independently rederives their raw native phase and count premises. It does not certify central arcs, pure three-copy homogeneous arcs, equal lengths or arbitrary convex pairs.

## Claim, assumptions and imported gates

The domain is exactly fixed threefold alternating A(delta), distinct positive lengths p,q, 0<delta<30, and strictly convex closed B of native word pppqqq with angles (u,alpha,360-2alpha,v,360-2eta,eta), alpha,eta in (90,180), neither equal120. All isometries, arbitrary contacts and species omission are allowed.

The reviewed unrestricted-contact [hexagon limit theorem](../lemmas/hexagon-limit-and-periodicity.md) supplies an actual trivalent edge-to-edge admitted tiling if any admitted tiling exists. This is an existence implication for the same two shapes; it does not claim every original tiling is edge-to-edge. The [binary monohexagonal exclusion](../lemmas/branching-hexagon-two-run-resonance-inventory.md) imports the full Zhu-Wang-Yan convex monohexagon classification: every opposite pair in pppqqq is unequal, and either adjacent-pair partition crosses a p/q boundary. Thus B alone has no tiling, even with unrestricted contacts. Consequently the actual limit contains A and the independently reviewed [uniform-density theorem](../lemmas/two-type-uniform-density.md) applies to it. No assumed frequencies or ergodicity are needed.

The native p-chain is 1+2i sin(alpha); the q-chain is the rotated conjugate of 1+2i sin(eta). Positive closure gives u=rho(alpha)+rho(eta), v=alpha+eta-u and p/q=|P_eta|/|P_alpha|. Correctly differentiating rho=atan(2 sin) gives rho'<0 and rho''<0 on (90,180). The strict turn lift is the one in the accepted phase lemma. A noncentral mixed homogeneous arc contains neither120 nor the paired opposite fillers120±2delta, so both AA whole-side tests fail. Every A star therefore contains one A, one B mixed corner and one B homogeneous corner.

The off-curve proof reduces all possible admitted geometries to u=alpha or u=eta. Its singleton lower-density premise is invoked only off these curves. The three necessary off-curve loci do not intersect in the distinct metric domain: any intersection forces alpha+eta240 and u=v120, contradicted by strict rho concavity about120. The accepted off-curve native counts then exclude all three loci, including the exceptional y=2x repeated-slot case.

## Attempted omitted-case attacks on the curves

The genuine B reflection displaying old corners (0,5,4,3,2,1) and old sides (5,4,3,2,1,0), followed by swapping length names, interchanges alpha/eta while retaining opposite relative ordering. The corresponding A reflection displays old sides (1,0,5,4,3,2) and old corners (2,1,0,5,4,3), preserving H-even indexing and delta. Thus it legitimately exchanges the two curves; it is not a fictitious symmetry of a single native B.

On u=alpha, f(alpha)=rho(eta), where f=x-rho is strictly increasing and rho strictly decreasing, puts alpha/eta on opposite sides of120. Write their deviations x,y>0. If alpha120-x, comparing eta120+x gives u120-epsilon with 0<epsilon<x/2, larger than the required120-x; strict rho decrease forces y>x. If alpha120+x, its equality u<2atan2<150 yields x<30; the same comparison at eta120-x gives u<120<alpha, forcing y>x. This retains the complete curve, including its inverse-sine and rational-halfangle pole boundary behavior already audited separately.

For low alpha the eight actual cover offsets are (2x,x-y,-x,-2x-y,x+2y,y,x-y,-2y). For high alpha they are their negatives. With y>x>0 the positive magnitude set is {2x,x+2y,y}, the negative magnitude set {y-x,x,2x+y,2y}. Checking all 12 pair equations on either branch gives only y=3x and delta=2x. Both signs must occur because a single actual A tile has both H and L corners. This step neither assumes positive A density in advance nor asserts that locally legal independent covers extend.

The high-alpha candidate has eta120-3x>90, hence 0<x<10. Its phase residual g(x)=rho(120+x)+rho(120-3x)-120-x is strictly concave: g'' is the sum of two negative rho'' terms with positive squared chain factors. Its tangent is g(0)=0,g'(0)=-1/2 (using radians consistently); therefore g(x)<0 for every x>0. No high-alpha root survives.

The low-alpha candidate has alpha=u120-x, eta=v120+3x, beta120+2x, chi120-6x, delta2x and 0<x<15. The actual nonlinear phase equality remains mandatory. Eliminating this entire angle line proves more than eliminating its roots and does not infer metric existence from the relaxation.

## Exhaustive native-slot and unbounded count audit

On this line every native angle is120+kx. Since x>0 a trivalent triple sums360 exactly when its integer coefficient sum is zero. This excludes isolated rational-angle exceptions. I independently enumerate all 24 oriented raw native sector states cubed; 1,664 triples satisfy cyclic binary ray compatibility. Exactly seven type multisets have zero coefficient:

- (alpha,alpha,beta), (chi,eta,eta);
- (u,u,beta), (v,v,chi);
- (H,u,alpha), (L,v,alpha), (L,u,eta).

The checker preserves u versus alpha and v versus eta as distinct native slots even when their angles coincide. Repetition across tile occurrences and both mirrors are retained. Any further positional geometric restriction could only remove stars from this necessary list and cannot invalidate the resulting identities.

Writing h,t,l for the three A-star counts, Yp for pure pp and Zbeta for (u,u,beta), the five inventory residuals are h-3NA, t+l-3NA, 2Yp+h+t-NB, Yp+Zbeta-NB, h+l+2Zbeta-NB. Their explicit rational combination with coefficients (-2,-1,1,-2,1) is9NA. Every residual is O(R): a fixed-width square boundary band has O(R) tiles because both fixed shapes have positive minimum area and bounded diameter, with uniformly bounded native incidence. Thus NA=O(R) in an actual admitted tiling.

The uniform-density theorem, applied with S={B}, supplies NA>=cR²-O(R), c>0. Its window convention can differ from the vertex inventory only by the same O(R) boundary band. These two inequalities contradict for arbitrarily large R. This establishes actual untileability, not only a zero-frequency necessary condition. Species omission, all mirrors, arbitrary contacts, nongeneric phase roots and boundary terms are accounted for.

## Replay, defects and remaining uncertainty

Independent exact replays completed with exit0:

    conda run --no-capture-output -n arisearch python research/reviews/verify_two_homogeneous_opposite_phase_independent.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_two_homogeneous_opposite_full_independent.py

The new no-author-import checker audits the complete seven-type inventory, both signs of all12 magnitude equations, both native reflection displays, exact phase derivatives/high-branch tangent and the explicit9NA incidence dual. The finite checks support these precise algebraic domains; the analytic concavity and actual whole-plane density argument above are additionally required for the theorem.

No mathematical defect or author repair was needed. The full manuscript incorrectly called its already VALID phase/off-curve dependencies pending; this metadata is corrected with their existing provenance links. The author's console phrase “all9 H/L magnitude matches” counts incorrectly: its retained equation list and loop contain12. This cosmetic output does not affect the exhaustive result, and the independent checker reports12. No unresolved qualification remains within the stated theorem. Central and pure homogeneous categories, the larger selected family, and the unrestricted target retain separate proof obligations.
