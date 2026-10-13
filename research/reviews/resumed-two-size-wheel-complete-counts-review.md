# Independent hostile review: all six-child two-size wheel counts

Date:2026-10-13. Reviewed claim: research/searches/resumed-two-size-wheel-complete-counts.md and the unchanged fixed-wheel hypotheses from research/searches/resumed-two-size-six-wheel.md. The claim excludes every count b+d=6, b>0, d≥0, μ²=dμ+b, λ²=μ, under five distinct native angles, one central child, five unsubdivided single-child parent corners and two complete neighboring child edges on each parent side. This is not a classification of all six-piece pentagon partitions.

## Independent analytic row pruning

The boundary matrix C is nonnegative in its positive real embedding. Reflection swaps columns but preserves each corner's single contribution to each of its incident boundary rows. Thus row i has exact sum t_i+t_(i+1), where each corner scale is1 orλ. For a proposed positive real native length vector l, choose an index i with maximal l_i. Then

    μ l_i = sum_j C_ij l_j <= (t_i+t_(i+1)) l_i.

Since l_i>0, μ≤max row sum. No irreducibility, limiting argument or Perron–Frobenius theorem is required. Max row sum≤2λ; as μ=λ²>0, μ≤2λ is equivalent to μ≤4. This remains valid if both corner contributions land in the same column or if C is reducible.

The count domain has exactly six cases because d is an integer from0 to5 and b=6−d>0. All roots μ>1: p_d(1)=1−d−(6−d)=−5, and p_d(t)=t²−dt−(6−d) has exactly one positive root. Each quadratic discriminant is nonsquare:24,21,20,21,24,29. No arithmetic case is omitted by an irrationality convention.

| b,d | Exact μ | Independently checked exclusion |
|---|---|---|
|6,0|√6|Every corner is small, row sums2<μ.|
|5,1|(1+√21)/2|At most one large corner, so rows≤1+λ<μ.|
|4,2|1+√5|Prior480 exact nonsingular matrices; independently rerun.|
|3,3|(3+√21)/2|New640 exact nonsingular matrices; independently checked below.|
|2,4|2+√6|μ>4, contradicting μ≤2λ.|
|1,5|(5+√29)/2|μ>5>4, contradicting μ≤2λ.|

For d1, the delicate inequality is valid:1<μ<3 follows from p_1(1)<0<p_1(3). Substitution μ²=μ+5 gives(μ−1)²−μ=6−2μ>0. Since μ−1>0, taking positive square roots gives μ−1>√μ=λ. This is a strict analytic inequality, not a rounded numerical comparison. If the sole large child is the center, every corner is small and the same upper bound still holds.

For d4, p_4(4)=−2<0 proves μ>4; for d5, p_5(5)=−1<0 proves μ>5. The count reductions do not require enumerating any reflection pattern in these four analytically killed cases.

## New640 domain and exact coefficient verification

At d3 there are exactly3 large children. Center-small leaves3 large corners, giving C(5,3)*32=320; center-large leaves2, giving C(5,2)*32=320. No symmetry quotient or orientation restriction is applied. The boundary matrix is independently reconstructed one corner at a time as scale times the identity/swap block on rows/columns(i−1,i), using all five reflection bits. This checks the author's start/end convention rather than importing their matrix construction.

Here μ=(3+√21)/2 has negative conjugate(3−√21)/2. Consequently μ is not a square in Q(√21), and λ has irreducible minimal polynomial t⁴−3t²−3. The root λ is the positive real square root of μ. Nonzero determinant coefficient vectors in basis1,λ,λ²,λ³ remain nonzero at that embedding and therefore exclude all real kernels, including side lengths outside any algebraic field.

Before reading the640 certificate, I independently computed all640 determinants and found each nonzero. After receiving research/certificates/resumed_intrinsic_wheel_d3.json, a separate Python standard-library checker independently verified every full coefficient vector, all case labels and both320/320 totals. It uses exact integer polynomial arithmetic modulo λ⁴=3λ²+3 and120-term Leibniz determinant expansion; it imports neither Sage nor the producer. This differs from the author's Sage matrix determinant algorithm. No floating arithmetic, solver, seed, timeout or sampling is involved.

Independent checker: research/reviews/resumed-two-size-wheel-complete-counts-independent.py. Exact replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed-two-size-wheel-complete-counts-independent.py

Result: PASS: all640 certificate determinants independently reconstructed by integer polynomial Leibniz expansion;320/320 complete domains.

The d2 checker research/reviews/resumed-two-size-wheel-independent.py was also rerun and passed all480 retained coefficient vectors,320/160 totals. Its geometric/native-index audit is retained separately in research/reviews/resumed-two-size-wheel-review.md. Thus the combined exclusion depends on1120 independently verified matrix certificates and four elementary full-domain inequalities, not on a purported2016-case computation.

## Attacks, repairs and scope verdict

Attacks considered: using a row bound for a reducible matrix; positivity of the eigenvector versus arbitrary algebraic kernel; reversed reflection indexing; off-by-one incoming/outgoing side labels; central-large corner counts; hidden orientation restriction; a second positive root; failure of the d1 square comparison; missing d0; repeated/padded certificate labels; extending a nonzero abstract determinant to arbitrary real length vectors. All are discharged above. No repair was needed.

**Verdict: VALID** for the complete specified six-count wheel domain. The conclusion excludes this one explicit distinct-angle outer-boundary topology at every count b+d=6,b>0. It does not prove that all six-pentagon partitions are wheels, exclude repeated-angle corner reassignment or divided parent corners, classify higher child counts, or resolve unrestricted convex-pair aperiodicity. No novelty claim is assessed.
