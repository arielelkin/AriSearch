# Frontier consolidation and replay registry audit

Date: 2026-10-13. Status: internally checked consolidation; root consolidation review passed;
full disposable replay pending. This note records maintenance, not a new
mathematical theorem or a proof review.

## Current mathematical frontier

The restart log first corrected nine of eleven reviewed B5+1 words, then
integrated the independently reviewed closure of both remaining words. It now
records all eleven at every actual metric on 108 < x < 126, x != 120, with a
separate independently VALID whole-synthesis review. Actual used AA22 seams
force periodic omission escapes; the reviewed support theorem handles their
absence without side-length inequalities. No residual B5+1 word remains.

The stale five-of-eleven coverage count, active middle-word assignments and
A002112 AAA-stratum follow-up have been replaced. Their historical artifacts
remain retained; the log explicitly marks these assignments superseded. The
complete complementary-angle claim in the opening paragraph was clarified to
distinguish complete two-angle coverage from the distinct/non-120 three-angle
scope. No unrestricted impossibility or surviving construction is asserted.

## Fourteen added registered checks

All fourteen passed through `research/searches/verify.py --only SCRIPT` with
assertions enabled. The registry now contains 43 producer/certificate pairs
and 223 verifier entries (266 registered checks total).

| Added script | Check and write behavior |
| --- | --- |
| `check_two_hexagon_alternating_residual_periodic_actions.py` | Rechecks seven exact positive native metric tori; `--output` points to temporary storage. |
| `verify_reordered_acute_pentagon_four_face_carrier.py` | Exact native supports, side aliases, connected orientable flat four-face torus; required `--output` points to temporary storage. |
| `verify_five_one_001212_011202_boundary_resources_independent.py` | Independent native seam/resource reconstruction for both boundary exclusions; stdout only. |
| `verify_terra_five_one_001212_boundary_transfer.py` | Reconstructs all native poses, boundary edges and true bi-infinite cycles against retained certificate; read-only. |
| `verify_terra_five_one_011202_boundary_transfer.py` | Companion exact native transfer certificate check; read-only. |
| `verify_terra_five_one_empty_boundaries.py` | Exact 010212/012021 empty interfaces and width-one obstruction; read-only. |
| `verify_terra_five_one_001122_cross_22_gate.py` | 64 AAA cycles, 96 two-ended cases, all 203 partitions and exact separator against retained certificate; read-only. |
| `verify_terra_cross22_luna.py` | Independent unordered-block reconstruction of the cross22 counts, H2 sufficient cases and separator; stdout only. |
| `verify_terra_five_one_002112_chebyshev_gate.py` | Exact retained 42-partition, algebraic-cut and BB-endpoint certificate reconstruction; read-only. |
| `verify_terra_five_one_002112_corner_strip_gate.py` | Exact retained 42-partition AAA/corner-strip certificate check; read-only. |
| `five-one-all-mask-no-cross-binary-lift.py` | Rebuilds the finite native-fibre certificate in explicit `--check` mode; no output writes and no theorem promotion. |

The newly completed `terra-five-one-010122-cross-22-gate.py` producer is also
registered with `--check research/certificates/terra-five-one-010122-cross-22-gate.json`.
This replays all 96 cases and all 203 partitions without writing; its
independent proof review subsequently passed. Its default invocation would write the retained
certificate, so the explicit check argument is necessary.

Two new independent checkers were then added and passed with no arguments or
output writes: `verify_five_one_unused_aa22_support.py` and
`verify_five_one_010122_cross22_independent.py`. They reconstruct the strengthened
support fibres and the complete A010122 seam certificate independently.

The two A002112 checks preserve local evidence superseded for family coverage;
they do not resume its research search. The no-cross producer checks a completed
fixed finite table, not an enlarged search or an independent proof.

## Intentionally unregistered legacy scripts

The replay registry is explicit; it is not a command to execute every Python
file. The audit found the following remaining classes of omissions:

- Fixed-path writers such as `boundary-attachment-ammann-h-gate-review.py` and
  `kite-dart-exclusion-audit-algebra.py` / `kite-dart-exclusion-audit-source.py`
  overwrite retained evidence. They need separate output-path repairs before
  registration. The boundary script also executes solver queries.
- `kite-dart-exclusion-audit.py` has an output path but runs a historical
  solver audit; solver UNKNOWN does not reliably become a failing process.
  Its imported algebra/source companions retain separate review roles.
- The three `verify_ammann_forcing_reconstruction_*` programs, and
  `verify_two_hexagon_global_develop.py`, report key negative outcomes in text
  without reliably returning failure. The latter is numerical development
  evidence. Registering them as-is would risk false PASS labels. The current
  exact Ammann repair rereview and retained torus checks remain registered.
- `verify_ammann_forcing_local_genericity.py` and
  `verify_ammann_forcing_local_stars.py` preserve older hostile diagnostic
  questions; they are not replacements for the registered repaired theorem
  checker. `verify_dzuklevski_scaffold.py` is a historical exact diagram
  fixture rather than a current frontier dependency.
- `verify_two_hexagon_balanced_rank_five_root.py` writes a retained certificate
  and reruns bounded solver experiments. The independent solver-free ring
  checker is already registered. `verify_two_hexagon_global_strata.py` offers
  multiple modes, including fresh SAT queries; its exact retained-record
  obligations are covered by the current registered checks.
- `verify_terra_001122_b_neighbourhood.py` is an older fixed-fixture checker
  whose independent counterpart and broader all-metric checks are registered.

These exclusions are not a claim that all omitted scripts are invalid. They
identify why blind registration is inappropriate in a nondestructive, failing
on error replay. No paused global query or bound was increased.

## Verification boundary

All fourteen added checks passed targeted registered replays. The existing
saturation palette checker also passed during whole-synthesis review. Full disposable replay must follow the
research freeze so the runner can compare a stable source/evidence snapshot.
The consolidation itself does not certify the proof dependency chain.

## Final maintenance review state

Root reviewed the registry check/temp modes and legacy exclusion decisions.
The independent whole-synthesis review passed, and the four earlier middle-word
lemma headers now link their already completed reviews and full-domain scope
extension; no proof text was changed in those four files. The construction
strategy received a separate independent review and its two practical
clarifications were integrated. Final full replay and Git checkpoint outcomes
will be recorded by the root after the research freeze.

## Root completion after research freeze

Root completed the disposable full replay: all 43 certificate reproductions
and 223 verifiers passed (266 checks), exit status 0, with original research
files unchanged. [Full transcript](frontier-full-replay-2026-10-13.txt).
Locked environment verification also passed. The
[root integration review](frontier-root-integration-review-2026-10-13.md)
records review scope and the final local preservation checkpoint.
