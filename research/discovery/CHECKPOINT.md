# Discovery restart checkpoint — 2026-10-24

**Unresolved. Zero live candidate pairs.** All declared searches and the
angular-first optimization are complete. No generation search is running.
The proof/review target is unchanged: two unmarked convex shapes, unrestricted
isometries including reflection and contacts, and tilings allowed to omit a
species. Finite experiments remain discovery evidence.

## What is ready

The directory preserves exact generators, bounded finite solvers, independent
positive-geometry checkers, complete finite audit rows, source/data hashes,
static galleries, and replayable commands. The approximately 64 MB working-tree
evidence is retained. Nothing was deleted or compacted for this checkpoint.
Existing October 20 user strategy text in `discovery-log.md` is preserved.

| Bundle | Evidence location | Current result |
|---|---|---|
| Kite8 | `runs/kite-n8-2026-10-24/` | six shapes, six periodic singleton witnesses |
| Boundary M6 and four challenges | `runs/boundary-m6-2026-10-24/` | 2,415 pairs, all four initial leads have 8-face periods |
| Boundary M8 | `runs/boundary-m8-2026-10-24/` | 21,945 pairs, 230 periodic, no surviving lead |
| Mixed support preflight | `runs/mixed-obtuse-2026-10-24/` | 150,226 unique pair/scales; 14 corner-supported → 7 incidence-feasible → 0 after angular cycle |
| Angular-first comparison | `runs/mixed-angular-first-2026-10-24/` | same nominal domain and 0 leads; measured 66.09 → 49.46 CPU seconds |

Counts overlap, and the number of failed metric variants is not a measure of
independent mechanisms explored. The current limitation is candidate yield,
not solver throughput.

## Validation

Latest post-review validation **PASSED** on 2026-10-25: locked environment,
**95 discovery tests**, all five fresh bundle replays and an unchanged
73-file source/evidence snapshot during validation (260.951 seconds). See the
[validation record](checkpoint-validation-2026-10-25.json) and
[pre-commit review](commit-review-2026-10-25.md). The review corrected standalone
catalogue species/count/definition checks; retained scientific evidence and
engine hashes are unchanged. All original diff files are recommended for
commit, with no discard candidates. The following earlier record is historical.

Consolidated full validation **PASSED** on 2026-10-24: locked environment,
**92 discovery tests**, and fresh replays of all five bundles. All seven driver
checks returned 0. The source/evidence before-and-after guard confirmed no
changes during validation (71 checked files). Total validation wall time was
265.57 seconds. The [machine-readable validation record](checkpoint-validation-2026-10-24.json)
was saved after the checks completed. Final documentation records the outcome;
no mathematical source or retained run was changed.

`discovery-checkpoint` verifies retained evidence without regenerating searches;
`discovery-replay` also repeats all fixed finite computations. Both include the
locked-environment verifier and complete test suite. Neither covers the separate
historical registry, whose command remains `mise run replay`.

```bash
mise run discovery-checkpoint
mise run discovery-replay
```

See [README.md](README.md) for safe fresh-run commands, effective CPU limits,
coordinate conventions and the distinction from historical `mise run replay`.
The historical generator defaults must not be used to start a new run on
retained output. The new wrapper refuses existing paths before launching.

## Independent review

Astra inspected the diff including untracked files and independently passed
84 tests. It found no retained-result correctness defect in the inspected
scientific code. It identified an overwrite footgun, ambiguous whole-directory
replay instructions, and different CPU-cap meanings. Those workflow issues
are addressed by the guarded generator, consolidated driver and documentation.
The [review record](checkpoint-review-2026-10-24.md) preserves findings and scope.

## Proposed next direction — not started

Run one **contact-first, jointly solved geometry** pilot. This changes candidate
generation rather than increasing support offsets or integer lengths.

1. Compare the exact proposal and every selected topology with the existing
   [alternate-obtuse P5/Q7 cycle](../searches/alternate-obtuse-p5q7-palette-cycle-2026-10-19.md)
   and [stopped interface route](../searches/regroup-smallest-unresolved-contact-mechanisms.md).
   Existing history already uses contact mechanisms; make no novelty claim
   from terminology or reopen a closed contact stratum without changing a premise.
2. Declare all P5/Q7 cyclic words modulo reflection with angles in
   `{105,120,135,150,165}`, summing to 540/900 respectively. Allow Q105 corners,
   omitted by the last three Q multisets. Apply vertex/cycle rejection before
   geometry (unfillable 165 corners are rejected here). Adding words alone is
   not the changed premise.
3. The changed premise is contact-first generation plus a single shared metric
   realizing both complete neighborhoods, instead of independent support offsets
   or isolated vertex stars. Enumerate consistent reflected native-edge
   descriptions of complete first neighborhoods around both species, including
   neighboring endpoint and edge
   constraints. Solve their shared native-length equalities and both polygon
   vector closures jointly, with exact strict positivity and one common scale.
4. Construct actual polygons and both rings, then verify exact convexity and
   nonoverlap. Keep the free dimension/parameters and exact metric witness.
   Integer or rational-only native lengths must not be imposed, and real
   unknowns in algebraic closure equations must not be incorrectly split into
   independent rational-coefficient equations.
5. Only concrete jointly realized survivors earn a small two-ring extension
   and periodic challenge. A failed representative does not exclude its entire
   positive metric cone.

Caps: one implementation session, ten search CPU minutes, 5,000 canonical paired
neighborhood templates, and 20 realized geometric representatives. Label a capped
enumeration incomplete. Use an existing periodic native fixture as a positive
reconstruction control and the two rejected Q words as negative controls.
Stop if no jointly realized pair appears or every realized contact structure
immediately matches a stopped route or periodic carrier. One structurally
interesting realized survivor can justify follow-up; the old ten-pair/three-word
allocation threshold is not a scientific requirement for this new approach.
Do not build a general partial-contact engine or polished workbench in this pilot.
