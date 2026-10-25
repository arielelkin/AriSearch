# Independent Astra diff review — 2026-10-24

Scope: current tracked log diff plus the 58 new discovery files (approximately
64MB), scientific implementations, reports, runtime/replay edges and selected
historical routes. Astra independently ran the discovery suite:84 tests passed
in 31.80 seconds. It did not rerun all full evidence audits or launch another
search during the review. It found no retained-result correctness defect in
the inspected finite generators, solvers or exact verification logic.

## Findings and checkpoint fixes

- **P2: overwrite risk.** The pinned `mixed_angles.py` generator's default
  directory is the retained mixed-obtuse bundle. It reuses the catalogue,
  truncates the scale audit and rewrites the preflight; a tiny cap could replace
  complete evidence with a prefix. Existing evidence was intact. The pinned
  source is preserved for replay. `generate.py` now requires a fresh explicit
  directory and finite positive CPU cap; existing paths and dangling symlinks
  are rejected before a subprocess starts. This mitigates the normal entry
  point; direct execution of the historical default remains unsafe.
- **P2: ambiguous reproduction scope.** The previous README's final
  “Reproduce,” code inventory, coordinate and allocation sections applied to
  the kite pilot but appeared general. README and CHECKPOINT now give a full
  bundle inventory and the complete `discovery-checkpoint` / `discovery-replay`
  commands. The historical `mise run replay` registry remains separate.
- **P3: differing cap meanings.** `angular_first` accepts a 540-second
  cooperative cap, but its worker has a 300-second process limit and its
  comparison parent a 360-second wall timeout. This can prevent a recoverable
  prefix from being written on a slow run. The limits are now explicit;
  retained runs completed far below them. No hash-pinned source was changed.

The new checkpoint driver composes existing checkers and tests, guards against
source/evidence mutation during verification, and can freshly replay every
fixed finite experiment. It is not another mathematical verification model.
All retained records are preserved, and the next candidate-generation
proposal is separate from this checkpoint preparation.

## Strategic recommendation

The 150,226 mixed metric cases came from one P angle word and 16 Q words, and all
metric survivors occupied two words already impossible around a whole P.
Speed improved, but candidate construction remains the bottleneck.

Prefer a bounded contact-first synthesis experiment: consistent full first
neighborhoods around both species, jointly solved native-edge equalities and
polygon closure, strictly positive exact metrics, actual ring geometry and
nonoverlap. Then challenge realized representatives with extension and periods.
The next domain can use the existing 15-degree field and allow Q105 corners;
that expansion alone is not the contribution. Existing alternate-obtuse and
interface histories must be checked before a topology is called new.

Limits and stop/go criteria are recorded in [CHECKPOINT.md](CHECKPOINT.md).
The proposed experiment has not started. Larger independent support palettes,
deep growth without candidates, a universal partial-contact engine and a
separate machine-learning carrier project have lower present expected return.

## Safeguard patch review and validation

Astra reviewed the new checkpoint/generation driver, mise tasks and rewritten
README and found no blocking issue. The guarded generator's eight regression
cases passed. Root then ran the complete checkpoint with fresh replays:
locked environment, 92 tests, all five retained bundles, and before/after source
and evidence hashes **PASSED**. The full result is retained in
[checkpoint-validation-2026-10-24.json](checkpoint-validation-2026-10-24.json).
No new candidate-family search was launched by this checkpoint task.
