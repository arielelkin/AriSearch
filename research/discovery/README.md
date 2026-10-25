# Discovery checkpoint

**Status: globally unresolved; zero live leads.** All declared experiments are
complete. The next proposed experiment changes candidate generation to joint
contact/metric synthesis; it has not started.

Latest full checkpoint validation (2026-10-25): **95 tests and all fresh bundle
replays passed**, with source/evidence unchanged during the checks. The
[pre-commit review](commit-review-2026-10-25.md) records the verifier fix,
commit/discard audit and progress assessment; the
[validation record](checkpoint-validation-2026-10-25.json) contains all outcomes.

Start with [CHECKPOINT.md](CHECKPOINT.md) for the current restart state, run
inventory, validation scope, and bounded next-direction proposal. The
[independent Astra review](checkpoint-review-2026-10-24.md) records the diff
findings and fixes.

## Validate the complete discovery checkpoint

From the repository root:

```bash
mise run discovery-checkpoint
mise run discovery-replay
```

Both check the locked environment, the complete discovery test suite, and
all five retained evidence bundles without rewriting source or evidence.
`discovery-checkpoint` verifies the retained certificates and finite audit
records. `discovery-replay` additionally regenerates every declared finite
computation in memory or temporary directories. The historical `mise run replay`
is a separate older registry; it does not cover this discovery directory.

Equivalent direct commands follow the project environment rule:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.checkpoint
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.checkpoint --replay
```

## Retained experiments

| Experiment | Declared domain and outcome | Report |
|---|---|---|
| Kite pilot | Convex whole-kite unions through 8 cells; six shapes, all monohedral periodic | [Pilot](pilot-report-2026-10-24.md) |
| Boundary M6 | Lengths 1–6, 120-degree hexagons; 2,415 pairs; four initial leads all periodic at 8 faces | [Boundary comparison](boundary-report-2026-10-24.md) |
| Boundary M8 | Lengths 1–8; 21,945 pairs; 230 periodic witnesses, no live leads | [Astra follow-up](astra-followup-report-2026-10-24.md) |
| Mixed obtuse | P5/Q7, exact 15-degree directions and support offsets {1,2}; 150,226 pair/scales; final 0 | [Astra follow-up](astra-followup-report-2026-10-24.md) |
| Angular-first | Same nominal mixed domain; earlier necessary angle rejection; same 0 leads, measured 25% less CPU | [Ordering comparison](angular-first-report-2026-10-24.md) |

These counts overlap: M8 contains M6, and angular-first reorders the mixed
census. Do not sum them as independent discoveries. Run manifests and exact
records are under `runs/`. No bounded negative is an unrestricted theorem.

Coordinate conventions are per bundle: kite/native boundary coordinates
`(x,y)` mean `(x,y*sqrt(3))`; mixed geometry records ordinary Euclidean x,y,
each in the exact field Q(sqrt(2),sqrt(3)).

## Start a new fixed-domain run safely

Use the guarded fresh-output entry point. An explicit output directory is
required, existing paths are refused, and CPU caps must be finite and positive:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.generate --output /tmp/arisearch-angular-fresh
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.generate --family mixed --output /tmp/arisearch-mixed-fresh
```

The historical `mixed_angles` generator defaults directly to retained output
and can truncate its audit. Keep it as a pinned replay dependency; use the
fresh-output wrapper to generate another run. Earlier reports retain their
explicit fresh-directory reproduction commands.

The angular comparison wrapper has a 300-second hard process-CPU limit and,
when it launches a worker, a 360-second wall timeout, in addition to the 540-second
cooperative metric cap. The hard limits can stop a worker before it writes a
recoverable capped prefix. The guarded optimized-only invocation inherits the
300-second process limit; it does not add the comparison parent's wall timeout.
None of the retained runs reached these limits. Check each result's `complete`
field when inspecting a newly generated run.

## Code map

- `kite_grid`, `screen`, `verify`, `replay`: original same-grid catalogue,
  periodic screen, independent geometry and kite replay.
- `boundary_words`, `boundary_screen`, `boundary_verify`, `boundary_replay`:
  native hexagon words, finite CSP, exact certificates and M6 replay.
- `length8_experiment`, `calibration_verify`: one bounded M8 calibration.
- `mixed_angles`, `mixed_verify`: support/contact generation and independent
  rational-field, star, incidence and scale-audit verification.
- `angular_first`, `angular_first_verify`: the reordered finite mixed census
  and exact comparison against the retained baseline.
- `checkpoint`, `generate`: complete read-only validation and guarded new runs.

No general mixed-polygon growth engine or saved-patch extension interface has
been implemented. Native boundary `--grow` searches for a fresh larger patch;
it does not extend a particular saved assignment.
