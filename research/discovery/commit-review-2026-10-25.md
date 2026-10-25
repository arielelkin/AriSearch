# Pre-commit review and disposition — 2026-10-25

Scope: all three tracked changes (`README.md`, `discovery-log.md`, `mise.toml`)
and all 64 previously untracked files under `research/discovery/`, including
scientific code, independent verifiers, tests, reports and retained evidence.
This review did not start a new research domain or create a commit.

## Finding addressed

**P2 — standalone mixed-catalogue verification accepted inconsistent records.**
`verify_catalogue` reconstructed all geometry, but trusted species annotations
and aggregate counters and compared support definitions only as sets. A P
pentagon relabelled Q, with the corresponding Q-prefixed ID, was accepted as
valid with 19 P and 399 Q tiles. Incorrect aggregate totals and duplicated
support definitions were also accepted. The retained catalogue itself has none
of these defects; its correct counts remain 20 P and 398 Q.

The checker now binds species to the polygon family, checks every aggregate
catalogue counter against independent enumeration, and rejects duplicate support
definitions. Three regression tests reproduced the failures before the change
and pass afterwards. Mathematical engines and retained run files are unchanged.
The complete post-fix validation outcome is recorded in
[checkpoint-validation-2026-10-25.json](checkpoint-validation-2026-10-25.json).
Full post-fix validation passed: locked environment, 95 tests, and all five
fresh bundle replays. All seven driver checks returned 0 in 260.951 seconds;
the 73-file before/after guard detected no source or evidence mutation. This
validation record and final documentation updates were saved after validation.
No further blocking correctness issue was found in this review.

## Commit or discard

**Retain all original changes. No existing diff file warrants discarding.**
The following inventory accounts for all 64 original discovery files; sizes
are decimal bytes including the verifier/test fix, excluding this review record.

| Files | Count | Bytes | Decision and reason |
|---|---:|---:|---|
| Scientific generators, solvers, renderers, independent verifiers, replay and guarded workflow code | 18 | 254,967 | Commit. These define the finite domains, produce and validate certificates, and make the checkpoint reproducible. Preserve pinned baseline engines with their matching evidence. |
| Regression tests | 11 | 69,500 | Commit. They exercise independent enumeration, exact geometry, bounded-solver outcomes, adversarial certificates and output protection. |
| Machine evidence under the five run directories | 18 | 58,627,664 | Commit. Catalogues, complete scale audits, finite outcomes, witnesses and manifests bind the reported exclusions and comparisons. Negative results remain consequential evidence. |
| HTML/SVG diagnostic galleries | 9 | 5,209,979 | Commit. They are derived and optional for machine replay, but the reports link them to inspect patches, periodic escapes and searched geometry without rerunning code. They have no mathematical authority beyond their exact source records. |
| Reports, README, checkpoint, dated review and validation record | 8 | 59,457 | Commit. They document scope, resource limits, replay commands, stop decisions and the historical review. Preserve the dated validation as history alongside the new validation. |

Commit the root README and mise tasks as the discoverable entry points, and
commit the discovery log as the current restart state. Keep its existing
October 20 strategy changes. The new verifier fix, tests, this review and the
new dated validation record belong with the same checkpoint.

No temporary search output, environment installation, cache, lock, orphaned
scratch file or unrelated product change was found in the proposed files.
Local Markdown links in the original diff resolve. The evidence is about
64 MB in total; its size alone is not a reason to discard the chain of evidence.
Compacting or deduplicating it would be a separate schema/replay change.

## Progress assessment

The bounded experiments are complete and reproducible, with zero live leads.
The kite pilot's six shapes all have periodic singleton witnesses. The four
initial M6 survivors have explicit eight-face periods. M8 has 21,945 pair
outcomes and no survivor. Mixed support has 150,226 unique pair/scales and no
survivor; the remaining incidence-feasible cases fail the angle cycle.
Angular-first preserves the outcome and removes work, with a single-run CPU
measurement of 66.09 to 49.46 seconds. M8 overlaps M6, and angular-first reorders
the mixed experiment; do not add their counts as independent discoveries.

This is useful elimination, a reusable necessary angular obstruction and
stronger reproducibility. It has not produced a new candidate with plane
existence or an unrestricted forcing proof, nor a general impossibility
theorem. Candidate yield is the present bottleneck. Stop the exhausted domains;
retain the bounded joint contact/metric pilot in [CHECKPOINT.md](CHECKPOINT.md)
as a proposal only. Its first useful milestone is exact compatible rings
around both species in a changed contact structure. Continued investment still
requires a concrete extension and recognition mechanism; larger patches alone
will not discharge those obligations.

The separate historical replay registry was not rerun for this review: its
code and scientific inputs were not changed. Direct historical generator
invocations still carry the documented overwrite risk; use the guarded
`generate` entry point for fresh mixed runs.
