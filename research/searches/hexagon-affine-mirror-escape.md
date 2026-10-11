# Exact affine mirror hexagon periodic escape

**Status:** witness found and fully checked by an exact direct lattice verifier;
fresh independent hostile review pending. **Date:** 2026-10-09 UTC.

## Mathematical question and retained object

Does an explicit noncentral non-equilateral pair with repeated side lengths,
an irrational area ratio, at least one irrational angle, and no monohedral tiling nonetheless admit a
periodic tiling? The retained [proof](../lemmas/hexagon-affine-mirror-periodic-escape.md)
and [certificate](../certificates/hexagon-affine-mirror-escape.json) answer yes.
No global classification or aperiodicity claim is made.

The construction is the affine image D=diag(2,1) of the reviewed three-face
H(a),H(2a) torus, cos(a)=sqrt(15)/4, sin(a)=1/4. Its two A motifs are related by
reflection in the horizontal axis; that reflection commutes with D. Unlike
an arbitrary affine deformation, this operation retains exactly two Euclidean
congruence classes. The computational witness has two A tiles and one B tile
per rank-two lattice cell. No periodic search domain was enlarged or sampled.

## Exact verification domain

The verifier reads fixed algebraic coordinates in Q(sqrt(3),sqrt(5)). Its primitive
element g=sqrt(3)+sqrt(5) satisfies g^4-16g^2+4=0, isolated by 39/10<g<4;
w=(g-2/g)/2 and h=(g+2/g)/2 give the exact coordinate basis 1,w,h,w*h. It checks all strict polygon
half-plane inequalities; all twelve squared native side lengths; all nine
retained full-side endpoint seam equalities; and the affine mirror identity.

For non-overlap, it checks every ordered pair of the three motifs, translated
by n*u+m*v for integers n,m. Bounding boxes reduce this infinite domain
exactly: q=n+m and k=n-m are integers in closed algebraic intervals determined
by those boxes, with equal parity. Exact floor and ceiling on real algebraic
numbers enumerate all possible intersecting boxes. Excluding identical copies
leaves exactly 18 candidate comparisons. Each comparison uses the complete
convex polygon separating-axis criterion, allowing boundary contacts.
Every translate outside the intervals has disjoint bounding boxes. The total
three-motif area equals the lattice determinant exactly, which, together with
closedness and non-overlap, proves plane coverage.

Additional finite length-pattern gates exclude all cyclic/reflected Reinhardt
systems under the imported unrestricted monohedral hexagon classification.
The irrational-angle proof is the rational nonintegral trace 118/61 of a
hypothetical root of unity; its exact value is checked. The exact irrational area ratio B/A=sqrt(15)/2-1
is checked separately from the rational tile-count ratio 2:1. No numerical angle
approximation, SAT solver, random seed, face bound, or denominator cutoff is
used. There is no discarded negative search supporting the claim.

## Replay and execution

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_affine_mirror_escape.py
```

- Python: 3.12.13.
- SageMath: 10.9.
- Replay elapsed time within selected environment: 1.212 seconds.
- Verifier SHA-256: `ef05e9b6026b516bd375cb8c280b806253c967911ffe252bfb3722cabbedd124`.
- Certificate SHA-256: `5c9eee720950433b36c3cc00af02569417ee2e5aad80c1e5bab6629470a42561`.
- Output: `PASS: exact convex pair, five/three repeated lengths, 18 exhaustive lattice overlap comparisons, area=det, non-monohedral Reinhardt gates, irrational direction trace and B/A area ratio.`.
- Resource limits: no imposed timeout; finite exact check completed.

## Primary literature boundary

On 2026-10-09, the query `Zhu Wang Yan 2508.01404 hexagon Reinhardt H1 H2 H3
side lengths` located [arXiv:2508.01404](https://arxiv.org/abs/2508.01404), and
[version 2 HTML](https://arxiv.org/html/2508.01404v2) was examined. Its Main
Theorem and Section 1's exact H1,H2,H3 conditions are the sole classification
import, used only for monohedral exclusion. The geometric pair witness is
checked independently. This search does not establish priority; no novelty
claim is made. The earlier two-triangle torus already works at arbitrary real
a, and this record's additional step is the affine/reflection preservation of
exactly two non-equilateral congruence classes.
