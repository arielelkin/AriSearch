# Independent hostile review: Q-only equiangular hexagon

Date: 2026-10-19. Reviewer: Sol. Target: `research/searches/resonance-qonly-hexagon-sol-2026-10-19.md`.

**Verdict: mathematical result passes, conditional on the cited classification. One bibliographic correction is required: v2 is dated 28 April 2026, not 2025.** The arXiv identifier was first assigned in 2025; the version actually checked is v2. No claim that the external classification proof was independently re-proved is made.

## Primary-source applicability

I directly inspected [Zhu–Wang–Yan, v2](https://arxiv.org/html/2508.01404v2), introduction and Section 2. The Main Theorem concerns plane tilings by congruent straight-edged hexagons and requires at least three tiles at every vertex. It makes no convexity requirement. The paragraph immediately following explicitly states that convex hexagons satisfy that condition. Section 2 explicitly permits tilings that are not edge-to-edge and distinguishes native sides from the edges formed by subdividing them. Thus arbitrary partial side contacts are within scope. Congruence has no orientation restriction; the paper also explicitly enumerates independently flipped first-layer tiles (discussion accompanying Figure 20). Reflections are covered. The target correctly transcribes H1, H2, and H3 with side i joining vertices i and i+1. Cyclic permutation and reversal are permitted relabelings.

For the actual all-120-degree Q, the hypothesis is even easier: two corners cannot fill 360 degrees, and a corner in an open side would leave 180 degrees to fill with 120-degree corners, which is impossible. Any plane tiling is edge-to-edge and trivalent. This observation is not an extra assumption imposed on the classification.

## Independent algebra audit

With z=exp(i*pi/3), closure is

    (s0-s3)+(s1-s4)z+(s2-s5)z²=0.

Using z²=z-1 gives exactly

    s0-s3=s2-s5=-(s1-s4).

Hence any opposite equality forces all three; H1 and H2 both contain s2=s5. Equal opposite side vectors with reversed directions imply v_i+v_(i+3) is constant, proving central symmetry. H3 sets s=(a,a,b,b,c,c), yielding a-b=b-c=c-a, hence a=b=c. No hidden distinctness of side lengths is needed. The specialization is valid under every allowed relabeling.

## Periodic construction, including the more general central case

For any strictly convex centrally symmetric hexagon centered at zero, put

    t0=v0+v1, t1=v1+v2, t2=v2+v3=t1-t0.

The copy translated by v_i+v_(i+1) shares precisely the opposite side with the original and lies across its supporting line. Adjacent midpoint rays are independent: the center is strictly inside the polygon, and a ray from it meets the boundary only once, so distinct adjacent side midpoints cannot share a ray; they cannot be opposite either, since their supporting normals delimit an angle below pi. Thus L=Zt0+Zt1 is a rank-two lattice.

The target supplies a valid global development argument for its equiangular case. It also extends to every centrally symmetric strictly convex hexagon: label the abstract honeycomb consistently with opposite labels on shared sides. The three corners at a honeycomb vertex have labels 0,2,4, or 1,3,5. Central symmetry gives opposite equal angles, and each of these alternating sums is 360 degrees because the six-angle sum is 720 degrees. Consequently all vertex neighborhoods are flat even when individual angles differ from 120 degrees. Face triangulations give a metric uniformly comparable to the regular honeycomb, hence completeness. The simply connected complete flat development covers the Euclidean plane exactly once. All side gluings have identity linear part, so faces are translates, and connectedness together with the three neighbor displacements ±t0, ±t1, ±(t1-t0) gives precisely Q+L. This proves global coverage and disjoint interiors, not merely a local matching diagram. Both t0 and t1 are nonzero periods.

The target only needs the equiangular subcase, so its 120-degree sentence is correctly scoped; it should not be quoted verbatim as a proof for arbitrary central hexagons without the alternating-angle substitution above.

## Independent mixed-species exclusion

Take P to be the regular pentagon (108-degree corners), and Q to have only 120-degree corners. All corners exceed 90 degrees, so four corners exceed 360 degrees; two do not reach 360 degrees. A side-interior contact would require corners totaling 180 degrees and is impossible. At a full vertex the possible three-corner sums are

    PPP=324, PPQ=336, PQQ=348, QQQ=360 degrees.

Only QQQ is allowed. Therefore no corner of P can occur anywhere in a plane tiling. This excludes even one P tile, with no frequency, density, periodicity, contact, or reflection assumption. In the resonance alphabet, PPA and PBC are unavailable because Q has neither A=144 nor C=132; BBB is the sole star. The target’s imported mixed-tiling exclusion is independently verified.

## Required correction and limitations

Replace the source year 2025 by 2026 when identifying v2, including the concluding scope sentence. Subject to that correction, no mathematical defect was found in the Q-only closure. The conclusion is existence of a periodic tiling for every tileable all-120 Q, not periodicity of every tiling and not tileability of every all-120 hexagon. The external Main Theorem remains the stated imported dependency.
