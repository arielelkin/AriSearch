# Independent hostile review: last-word resonance strata

Date: 2026-10-19. Verdict: **PASS for the exact certificate and conditional implications; report table needs the correction below.** Original problem unresolved.

Reviewed `research/searches/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.md`, its producer and retained certificate. The independent checker beside this review imports neither producer nor original atlas builder. It reconstructs signed corner triples directly from the native words, prunes by explicitly recomputed opposite endpoint pairs, computes canonical rational row bases for every one of 65536 subsets, independently rebuilds the ten-factor corona chains, and compares every stratum's row basis, lifts, pruning rounds, coverage, corona indices, status and retained neighbor table. Exact Sage QQ arithmetic; no solver, timeout, seed or symmetry quotient.

## Findings and attempted failures

The reconstruction gives 32 signed stars, 16 unsigned triples with two lifts each, and 628 distinct rational row spaces modulo both totals. Canonical-basis enumeration is independent of the producer's closed-mask breadth-first enumeration. All spaces have dimension at least four. All retained normalized rational equations agree exactly.

The affine translation is correct: each three-corner equation has right side 2, while each six-corner total has right side 4; subtracting 2/3 per coordinate homogenizes both. The common strict point alone does not certify an exact support. However, the stated proper-hyperplane argument does: every excluded row is nonzero on the nullspace, finitely many proper rational hyperplanes cannot cover a rational vector space, and rational scaling preserves strictness. No metric closure follows. In particular the regular-angle witness cannot be promoted to a distinct-length metric.

Pure consecutive triples are tested modulo both totals. A triple sum 2 makes the three intervening positive exterior turns sum pi, giving antiparallel sides 0 and 3; these have equal native lengths in both words. The imported reviewed universal strip construction applies to any strict closed metric satisfying this condition. This escape permits using just one species, as required by the original problem. It does not require existence of a mixed tiling or establish metric realization. The 306 count has priority over the other filters.

Every actual seam supplies an actual opposite endpoint star, so deleting a star without any such continuation is necessary. Fixed-point deletion remains necessary by induction. Full corner cover requires both species to occur; an omitted species would invalidate its use as an unrestricted exclusion. The report explicitly confines this filter to mixed full-cover components and leaves monohedral omissions to the prior classification. This is an appropriate scope restriction, not a new unrestricted exclusion theorem.

All 100 formal A-dimer corona chains and their factor incidences reconstruct exactly. Filtering their factors by active stars is necessary when A occurs, because private side 5 forces its equal native A partner. These are finite chains of external side states; they neither identify all repeated external tiles nor certify nonoverlap or extension. No such inference is made.

Independent counts are 306 pure escapes, 300 further failures of full corner cover, 13 deterministic conditional escapes and 9 branching residuals. Exactly 99 spaces pass the coverage/corona filters, including 77 pure escapes; all 22 other survivors have coronas. All 13 complete tables have 24 singleton side states and are involutions. The three active supports match the report. Given fixed strict native polygons, a native neighbor side and relative handedness specify the unique complete side placement; the imported intrinsic determinism theorem therefore applies conditionally to actual ETE trivalent tilings. A formal corona supplies no plane tiling. Defect-free limits and monohedral omissions retain their stated separate hypotheses.

## Exact branching table and defect

|mask|dimension|initial signed lifts|active signed stars|coronas|branching states|
|---:|---:|---:|---:|---:|---:|
|3162|6|12|12|4|8|
|3778|6|12|12|4|8|
|3802|5|16|16|9|14|
|3814|5|16|12|4|8|
|27672|6|12|12|1|10|
|27714|6|12|12|1|12|
|27738|5|16|16|4|16|
|27750|5|16|12|1|12|
|27836|5|18|12|1|10|

The report's original last row gives 16 signed stars for 27836. This equals neither its initial count 18 nor its active count 12. Correct that value and label the column explicitly as initial signed lifts, or use the active counts throughout. The certificate is correct. The initial/active distinction also matters for 3814 and 27750. This is a presentation defect, not a defect in the finite census or escape implications. The inclusion-minimal branching masks are exactly 3162,3778,27672,27714. The displayed 3778 alternative examples agree with the retained full table.

No repaired mathematical lemma is proposed. No new literature theorem or novelty claim is involved. The unresolved obligation remains distinct-positive common-length metric realization together with an unbounded periodic escape/forcing mechanism on the branching residuals. The finite census does not settle that obligation, and stopping this route under protocol section 5 is justified.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-thirtytwo-resonance-strata-hostile-sol-2026-10-19.py

The checker asserts the corrected initial count 18 for 27836 and all active counts separately. Verdict is scoped to the retained finite certificate, exact-stratum argument, and conditional escape applications; imported global results are used at their previously reviewed scope, not independently reproved here.
