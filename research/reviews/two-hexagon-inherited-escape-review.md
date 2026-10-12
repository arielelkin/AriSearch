# Inherited two-hexagon escape query: independent retained-output review

Date: 2026-10-12. Verdict: **VALID retained support and refinement certificates; ITERATION_LIMIT is inconclusive**.

[The checker](two-hexagon-inherited-escape-check.py) imports no producer or CP-SAT code and does not rerun the query. It recomputes every source torus's used corner triples and glued side equalities directly from its labelled lattice. Torus fundamental domains are checked for complete cell coverage; source triple membership is checked by exact rational affine row space, and side equality membership by independently traversed equivalence graphs. All 695 source records pass, giving 38 distinct direct supports.

The checker independently constructs all 288 relabellings: separate dihedral corner permutations on the two species followed by optional species exchange. Crucially it derives each side permutation from the images of the two incident corner endpoints, rather than copying the producer's reflected-side formula. Reflection therefore sends side i to r−i−1, with the required one-side offset. Applying these actions gives exactly 554 distinct supports, matching the retained metadata.

Every one of the 20 refinements passes all of the following exact checks: its generating corner support S is contained in the physical support U; each missing triple is absent from U and belongs to the reported escape; the two 720-degree polygon sums together with S imply every missing 360-degree equation; S is inclusion-minimal for those implications; the escape is a retained source support under a verified symmetry; its corner equations are implied by U; and its side equalities belong to the transitive closure of the physical side pairs E. No physical U/E closure already contains an initially blocked retained torus. These verify that every added implication is valid for any genuine angle vector, even though the query's initial Boolean angle flags need not already satisfy rational closure.

The actual one-worker CP-SAT default random seed is 1, and the root corrected the output's earlier reported seed 0 to 1. The checker requires the corrected value. [The verification output](two-hexagon-inherited-escape-check.json) retains the exact corrected certificate digest.

The record ends after 20 refinements with ITERATION_LIMIT. There is no retained finite residual patch and no UNSAT conclusion. The intermediate Boolean assignments and labelled patches were not stored, so this verifier does not independently reproduce each intermediate SAT decision or its precise missing-flag list. It verifies the recorded mathematical implications and inherited escape witnesses. Passing those checks supplies no unrestricted periodic-escape classification, actual Euclidean polygon realization, or plane tilability.

For a future RESIDUAL_FINITE_PATCH output, the same checker verifies the complete radius-R cell set, symbol range, exact physical usage, full rational corner closure, complete side equivalence relation, reported rank and corner coverage, and absence of any inherited support in that closed type. Such a passed residual would still be a relaxed finite combinatorial fixture. An arbitrary UNSAT or UNKNOWN status is accepted only as a reported solver status, without an independently verified proof.

Replay:

```bash
MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/two-hexagon-inherited-escape-check.py
```

## Resumed analytic-balance pass

The resumed radius-three record has 40 verified refinements: the original 20
are retained unchanged as parsed JSON, with the exact resume-file digest,
and 20 new refinements were added before a second ITERATION_LIMIT.
The checker verifies the analytic-empty source digest and integer potential,
its two species sums −1 and minimum coordinate −2, the 195-triple region,
and all 288 symmetry actions giving 144 distinct regions. It independently
enumerates the radius-12 ball: 469 cells, 864 complete stars and 222
remaining corner incidences. Complete stars use distinct cell/corner
incidences. The inequality 469>2×222 verifies the finite empty-patch
certificate without any solver.

The analytic-empty clause constrains solver flags, which may contain unused
triples. A future physical closed type lying inside an empty symmetry region
must therefore receive the diagnostic
`RESIDUAL_FINITE_PATCH_IN_EMPTY_REGION`; it is a ruled-out exact type.
The checker validates that membership, and any reported symmetry index.
A plain finite residual must avoid those regions. Neither current record
contains a residual.

The checker prints controls without changing retained files by default;
`--output PATH` explicitly saves them, and `--certificate PATH` selects the
resumed record. The attachment audit likewise accepts `--output-dir DIR`
for all of its generated controls and SMT files, allowing temporary-output
registered replay.

## Exact angle-grid mode

The root's query change passes `--grid K` to the existing query model. That
model bounds all twelve integer angle numerators strictly between 0 and
180K, imposes both species sums 720K, and equates every Boolean triple
flag to its exact 360K angle test in both directions. The revised retained
T is consequently the full exact angle type rather than merely the rational
closure of physically used triples U. Physical usage remains a subset of T.
This resolves unused extra triple flags for positive-grid queries. Torus
blocking and the analytic empty-region clauses remain sound for this
full type; the independent support symmetry checks still apply.

For a retained grid residual, the checker independently tests numerator
integrality, strict bounds, both polygon sums and all 364 triple sums. It
checks exact T equality, U subset T, rational closure(T)=T, reported rank,
all physical patch constraints, inherited torus avoidance and analytic-region
status. For grid zero it preserves the previous closure(U) interpretation.
Prior certificates without angle_grid use zero. An UNKNOWN grid query has
no retained angle vector or finite residual to verify. Completeness of a
particular universal denominator belongs to its separate mathematical
lemma; finite grid checking alone does not prove it.

The retained radius-three K=323633 query returned UNKNOWN after its one
60-second solver call, with no refinement or residual. The independent
checker passed its source-library, symmetry, analytic-empty-region and
metadata checks; [controls](two-hexagon-complete-grid-radius3-check.json)
retain the exact certificate digest. No angle numerators were retained,
so the future residual numerator-checking branch was not exercised by
this inconclusive record.
