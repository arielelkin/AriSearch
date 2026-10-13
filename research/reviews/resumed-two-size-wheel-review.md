# Independent hostile review: six-piece two-size pentagon wheel

Date:2026-10-13. Reviewed artifacts: research/searches/resumed-two-size-six-wheel.md, research/searches/resumed_intrinsic_two_size_wheel.py and research/certificates/resumed_intrinsic_two_size_wheel.json. Claim: at μ=1+√5, λ=√μ, no genuine convex pentagon with five pairwise distinct angles realizes the stated central-plus-five-corners wheel partition of μP into4P+2λP, at any positive real side lengths. Reviewer did not construct this wheel and independently reconstructed the matrices before reading the producer.

## Geometry and domain audit

The contact scheme explicitly retains five single-child parent corners, one corner child per corner, and exactly two whole child edges on each parent boundary side. It is not claimed that every six-piece pentagon partition has this topology. Strict native corners rule out extra collinear native-edge segmentation; unrestricted internal partial contacts do not invalidate the stipulated whole outer-boundary edges.

Because parent and children are all similar P and its five angles are pairwise distinct, the child at parent corner i must use its native corner i. Mapping the two incident rays has exactly two choices, up to the already fixed target placement: direct isometry preserves the incoming/outgoing native side assignment; reflection swaps it. There is no omitted rotation parameter once that corner and both rays are fixed.

For corner i, its boundary contribution acts on rows and columns(i−1,i). Unreflected gives scale t_i times the2×2 identity block; reflected gives scale t_i times the swap block. This independently yields the producer's side-i equation: start uses t_i*l_i or t_i*l_(i−1), end uses t_(i+1)*l_i or t_(i+1)*l_(i+1). In particular the corner block matrix C is symmetric, providing a useful convention check. Reflection acts on both rays together; independently choosing each incident edge would introduce nongeometric cases, and the producer correctly does not do that.

The count4small+2large is area compatible because μ²=4+2μ. A small center leaves exactly2 large corner children: C(5,2)*32=320. A large center leaves exactly1: C(5,1)*32=160. Thus480 cases, with no symmetry quotient. Center orientations and internal contacts are not enumerated because the boundary equations are independent of them; a boundary impossibility covers all their choices. Cases with repeated native angles, subdivided parent corners, extra boundary children or different outer contact graphs are outside the hypothesis, not silently excluded.

## Exact algebra and independent certificates

The polynomial f(t)=t⁴−2t²−4 is irreducible over Q. Indeed μ=1+√5 is quadratic, and its other real embedding1−√5 is negative. It cannot be a square in Q(√5), since every square has nonnegative image in both real embeddings. Hence λ has degree4. Identify its positive real root by17/10<λ<19/10. Any nonzero coefficient vector in basis(1,λ,λ²,λ³) is therefore nonzero under that real embedding.

The required boundary equation is(μI−C)l=0. Invertibility is over the real embedding, so nonzero determinant excludes every real length vector, not merely lengths belonging to Q(λ). Positivity, edge-vector closure and convexity cannot restore a nonzero kernel. Thus arbitrary quartic or larger metric modules are included in the exclusion.

I first independently computed all480 determinants using corner-block assembly in Sage, obtaining no zero. Then replaced that checker with a stricter independent certificate verifier using ONLY Python integer arithmetic: polynomial4-tuples reduced by λ⁴=2λ²+4 and the120-term Leibniz determinant expansion. It imports neither Sage nor the producer. It verifies certificate keys, strict record types, all corner/reflection domains, no duplicate cases, both320/160 totals, each exact determinant coefficient vector and nonzero status. Every retained coefficient agrees, not just the zero/nonzero verdict.

Independent verifier: research/reviews/resumed-two-size-wheel-independent.py. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed-two-size-wheel-independent.py

Observed result: PASS: all480 certificate determinants independently reconstructed by integer polynomial Leibniz expansion;320/160 complete domains.

The finite domain is exactly these480 matrices; each determinant has120 permutation terms. No random seed, floating arithmetic, tolerance, timeout, solver or inherited enumeration is used. The certificate is the producer's retained JSON; the independent checker makes no mutations.

## Hostile attacks and verdict

Attacks checked: off-by-one angle/side indexing, reflection at the wrong endpoint, skipped direct/opposite congruences, incorrectly enumerated center type counts, omitted central rotation choices, native-side truncation at parent corners, restriction of the real kernel to an algebraic field, nonminimal field presentation, padded/duplicated/missing certificate records and determinant algorithm dependence. No unresolved defect was found and no repair was needed.

**Verdict: VALID** for the stated fixed distinct-angle wheel scheme at these scales, including arbitrary positive real metrics and all reflected corner placements. Its no-realization conclusion is exact; it does not exclude repeated-angle wheel variants, other six-piece topologies, another size multiplier, all two-size substitutions or the original unrestricted aperiodicity problem. No novelty claim was assessed.
