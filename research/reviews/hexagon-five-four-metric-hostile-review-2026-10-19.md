# Independent hostile audit of fixed five/four metric gate

Date: 2026-10-19. Verdict: **valid** for the finite support classification, equiangular exclusion, polynomial formulation, and explicitly unresolved first metric query. Nonequiangular realizability remains **unresolved**.

## Claim and assumptions

Reviewed producer, explanatory Markdown, certificate and checker named `hexagon-five-four-metric-gate-2026-10-19`, together with the forced-dimer atlas producer, certificate and its independent hostile review. The fixed words are A=(0,1,2,0,3,4) and B=(0,1,1,0,2,3). Five colors mean pairwise distinct positive lengths. Full corner cover and dimer-corona necessity are conditional on a mixed edge-to-edge trivalent source. No theorem supplying such a source for an arbitrary tileable pair is established here.

## Independent finite reconstruction

The retained script `research/reviews/hexagon-five-four-metric-independent-check-2026-10-19.py` imports no producer. It takes the independently reviewed 22-star atlas as input, derives opposite-endpoint ordered port pairs directly from native side endpoints, derives each corona factor directly from signed triples, and exhausts all 4194304 masks. It does not use the producer endpoint-microstate table or factor dictionary.

Its predicate is: every native corner occurs; every seam of every selected star has at least one selected opposite star; and at least one of the seven complete corona cycles has a selected witnessing star at every factor. Reflection signs remain distinct. The same star may witness multiple factors; external identities and geometric consistency are deliberately relaxed. This is an upper approximation, hence necessary for an actual source, and cannot supply existence.

Result: **PASS**, exactly 446 masks, corona counts (254,128,128,256,128,128,256), digest `6114da92d9a00b6b96fb2073c6c58a21b6a0e94d59bf594dc80a207474d25372`, and seven inclusion-minimal masks {33416,41032,1118212,2625540,20774,22550,3543044}. Every retained mask contains one of these minima. The checker verifies the retained first query was mask 33416 with stars 3,7,9,15 and UNKNOWN/timeout; it does not re-run that query or independently certify elapsed time.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-four-metric-independent-check-2026-10-19.py

## Metric attacks

The equiangular rows are correct: x coefficients are twice the sums of cos(j*pi/3), y coefficients are (2/sqrt(3)) times sums of sin(j*pi/3). They give the displayed rank-three matrix and exactly l1=l2=l3=l4. The existing independent checker was run and passed. Independent polygon rotations multiply a zero closure vector by an invertible rotation and do not affect this conclusion. This only excludes equal native interior angles of 120 degrees.

There is no off-by-one corner defect. Atlas side j joins native corners j-1 and j. The metric producer first draws side j and then rotates by native corner j, which is consistent. Starting each polygon with side0 horizontal fixes two independent Euclidean orientation gauges and imposes no relation between their physical placements.

Each unit complex variable with positive sine has a unique exterior angle in (0,pi). For three corners the product (-1,0) implies the sum is pi: the only odd multiple of pi strictly within (0,3pi) is pi. Thus it is exactly the trivalent interior-angle equation, with no missing handedness sign; reflections preserve angle magnitudes. Cyclic shifts and repeated native corners are correctly handled by the commutative product.

Positive lengths, distinctness, and normalization l0=1 are legitimate because common scaling preserves all feasibility conditions. The six vector increments use the right side colors, both polygon closures are imposed, and final rotation equals one. Each directed edge places every other vertex strictly to its left. These halfplane conditions imply six distinct extreme vertices in cyclic order, no crossing, and strict convexity; consequently they also exclude multiple winding that a unit rotation product alone might admit. Conversely every strictly convex native-order realization can be translated and rotated into this encoding and satisfies these inequalities. A model would therefore be an exact polygon metric candidate, subject to model extraction and independent checking, rather than a tiling witness.

## Minimal-support logic and limits

Feasible supports are not required to be upward closed under the combinatorial predicate. That is unnecessary. In the finite family every support contains an inclusion-minimal retained support. The metric constraints for this smaller set are a subset of the original star equations; all polygon constraints remain the same. Therefore infeasibility of all seven minima would exclude all 446 supports. A SAT minimum would establish only its own metric feasibility and would leave larger supports and actual-source extension open. No determinism conclusion follows from this reduction.

The retained certificate contains only the first UNKNOWN, reason timeout, with approximately 30.23 seconds reported. The remaining six queries were not launched. UNKNOWN supplies no negative feasibility evidence. There is no recorded UNSAT certificate to audit and no conclusion that any nonequiangular support is impossible.

## Defects, repair, remaining uncertainty

No mathematical defect requiring repair was found. The original checker explicitly omitted independent support completeness; the added enumeration now supplies that check relative to the already reviewed source atlas. The producer report should link this review and new checker when updating its review-status paragraph. Solver encoding was audited by reading and mathematical reconstruction, not by an external formal translation checker. No longer solver query was run. The exact next obligation is an algebraic witness or analytic infeasibility argument for the first minimum, followed by the remaining minima as logically required. Global tilability, periodicity, the source reduction, and the original two-convex-tile problem remain unresolved.
