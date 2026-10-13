# Independent hostile review: unused AA22 support and A001122 synthesis

Date: 2026-10-13. Reviewer: `/root/cross010122`, independent of the support theorem and A001122 synthesis authors. Verdict: **VALID**, conditional on the explicitly imported reviewed defect-free/honeycomb, native compactness, monohedral, binary-equality, and metric-development dependencies. This review does not independently re-prove those general dependencies or cover the unrestricted two-polygon problem.

Reviewed targets:

- [Unused-AA22 support theorem](../lemmas/five-one-all-mask-no-cross-periodic-escape.md).
- [A001122 all-metric synthesis](../lemmas/five-one-001122-all-metric-periodic-escape.md).

The reviewer authored the separate A010122 used-cross lemma, which is NOT reviewed here. These reviewed targets do not rely on that new result. In particular there is no self-review of A010122 used-seam coverage.

## Material proof gates

1. **Premise change and exact scope.** The support theorem now explicitly assumes a saturated ACTUAL whole-side trivalent field whose A side4 is always AB. It permits all length aliases. The old three-inequality metric hypothesis survives only as a sufficient corollary. All subsequent uses require the absence of an actual AA22 seam, never inequality of formal side values. Angle triples are complete on 108<x<126, x!=120: all five affine angles meet at120 and have different slopes; exactly four unordered triples sum identically to360. I independently reconstructed this palette.

2. **Counting and sparse extraction.** Each A has exactly one22 side. The supported whole-side matching bijects these to the unique AB22 side of each curved B; middle B has none. Thus N_A=N_curvedB+O(R), including fixed-shape boundary errors. Counting the two A-y corners and the unique B-s corner yields 2N_A=2N_B+U+O(R), hence U+2M=O(R). Nonnegative bad-object counts allow arbitrary fixed-radius clean disks by the stated area comparison as R grows. This does not infer that bad objects were absent in the original field. Indexed fixed-shape compactness retains whole-side partners, B saturation, and AB rather than AA on native A side4, even when lengths coincide. The limit has neither AAA nor middle B. A pure limit is impossible in that restricted language. All constants may depend on the actual fixed pair; no uniform parameter compactness is required.

3. **Global species base.** At x/y A corners there is one AA arm, and at z corners none. Direct native incidence forces AA sides0,2 and the opposite marked AB sides1,4 for BOTH words. Each curved B similarly has a unique pair of opposite marked seams. Every cell lies on a complete marked primitive combinatorial line; two distinct primitive directions meet at an integer cell because the direction determinants have absolute value1. Such a meeting would demand four marked neighbours, impossible. Thus all lines share a combinatorial direction. Alternation along them gives row phases q_j. In each B's two adjacent rows, one candidate neighbour has species B. Equal upper/lower row phases make those B neighbours opposite (the excluded middle mask); unequal phases produce the curved masks. Hence q_(j+1)=1-q_(j-1), a period-four recurrence. This is a genuine infinite-field argument, independent of bounded searches and independent of Euclidean centre-line geometry.

4. **Actual native fibres and metric aliases.** I independently reconstructed all12 poses at each of32 base cells. Exactly two A poses and four B poses meet the species-imposed angle roles. Each B's two marked-side branches has two poses. Branch feasibility depends only on the fixed actual metrics, so the selected fibre choice is periodic over the already periodic species base. If both branches are feasible, b2=b3=n and b0=b5=m. The actual B closure and its reversed conjugate give (b1-b4)(E-E^4)=0. Since R in(36,72), E^3 cannot be1, so b1=b4. The native corner/side profiles then have exactly two reflection classes. Further length aliases, including m=n, preserve these equalities and cannot introduce more profiles. Replacing each reflected label by its representative preserves every vertex and edge constraint. No generic four-state lifting claim is needed.

5. **Full legality and nonzero translation.** Every AAB star is precisely two equalities between A-corner maps and the B map r->x,s->y; ABB stars are already legal. Every side condition is an equality of actual native length maps. This is exactly the periodic binary equality system in the imported finite-cover theorem, with the actual restricted field supplying an infinite solution. Its finite-periodic labels satisfy the full SFT constraints, so the imported actual metric-development theorem produces a plane-covering tiling and a nonzero translational symmetry (a glide may be squared). The proof does not infer realizability from an isolated finite fan or infer periodic native labels from periodic species alone.

6. **A001122 composition.** First extract one actual saturated field for the original fixed polygons. If it has a used AA22 seam, the independently reviewed complete96-case A001122 cross theorem gives an A-only periodic tiling; its only non-H2 partition fails actual positive closure by the full-interval separator. Otherwise every native A side4 has B as partner and the support theorem applies. This dichotomy is exhaustive even when formal length equality permits unused cross matches. Reflections, original partial contacts, and omission are retained. The conclusion is existence of a possibly different periodic tiling, not periodicity of every input tiling.

The B closure sentence mentioning an exception at R=120 outside the allowed interval is awkward but has the correct mathematical meaning: there is no exception within(36,72). It is not a gap or an added hypothesis.

## Independent exact evidence

[Independent checker](verify_five_one_unused_aa22_support.py) imports no producer code. It rebuilds native side indexing arithmetically rather than using the producer's endpoint-set search, independently checks the35-triple palette, all32 cells/12 poses, marked directions, actual AA/BB indices, both B branches, reflection-profile quotient and exact B closure identity.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_unused_aa22_support.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_001122_cross_22_gate.py

Both PASS. The second is an existing independent A001122 checker rerun during review; it confirms64 AAA cycles,96 two-ended cross cases, all203 actual partitions,40 H2 cases plus one closure-impossible partition, and the full-interval exact separator. The finite checker does not replace the analytic gates above. No sampled metric, solver timeout, positive-density premise, or finite-to-infinite extension inference is used.

This review permits stable promotion of the support theorem and A001122 all-metric synthesis at the full stated interval. A010122 all-metric promotion additionally requires independent review of its separately authored used-cross theorem and its explicit synthesis. The wider research goal remains unresolved.
