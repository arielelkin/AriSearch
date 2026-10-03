# Research artifacts and verification

The problem remains unresolved. Read [the current discovery log](../discovery-log.md)
for authoritative route status and next actions, and [the problem](../research-problem.md)
for the acceptance gates. Failed constructions remain useful records; their
certificates prove only the explicitly stated finite claims.

## Artifact organization

- [lemmas/periodic-obstructions.md](lemmas/periodic-obstructions.md) indexes the
  side-count, hexagon-limit, pentagon-curvature, and frequency-balance proofs.
  Other lemma files retain their existing subjects and paths.
- `searches/` contains exact data, finite searches, and retained JSON certificates,
  including falsified branches. Each report states its current status.
- `reviews/` contains claim-specific adversarial reviews and the October 3
  two-ended-edge falsification. Review coverage is stated locally; a passing
  script is not a hostile review of every theorem.
- `literature/` records primary sources and the documented search boundary.
- `counterexamples/` retains exact witnesses against failed shortcuts.
- [runs/2026-10-02-checkpoint.md](runs/2026-10-02-checkpoint.md) preserves the
  historical overnight checkpoint. Its next actions are superseded and its
  deadline applies only to that run.

## Nondestructive verification

From the repository root:

```text
conda run --no-capture-output -n arisearch python3 research/verify.py
```

The [runner](verify.py) uses its own file location to find the checkout, so it
also works from another working directory when invoked with an absolute path.
It captures generated JSON in memory, compares parsed values with all five
retained certificates, and runs three independently implemented verifiers.
It never overwrites certificates. Assertions must remain enabled. A mismatch,
script error, or failed assertion gives a nonzero exit status.

| Retained certificate | Producer replayed | Additional verification |
|---|---|---|
| [Walton vertex rank](searches/walton_vertex_rank_certificate.json) | [Producer](searches/walton_vertex_rank.py) | [Independent vertex verifier](searches/verify_walton_vertex_rank.py) |
| [Walton relative relabelings](searches/walton_relative_relabeling_rank_certificate.json) | [Producer](searches/walton_relative_relabeling_rank.py) | [Independent relabeling verifier](searches/verify_walton_relative_relabeling.py) |
| [Walton state assignments](searches/walton_state_assignment_rank_certificate.json) | [Producer](searches/walton_state_assignment_rank.py) | Recorded [hostile review](reviews/walton-state-assignment-review.md); no standalone independent exhaustive verifier |
| [Original nonresonant scaffold](searches/nonresonant_5_6_scaffold_certificate.json) | [Producer](searches/nonresonant_5_6_scaffold.py) | Recorded [hostile review](reviews/nonresonant-5-6-scaffold-review.md); runner repeats the original exact calculation |
| [Joint local closure and language](searches/joint_5_6_local_certificate.json) | [Original local verifier](searches/joint_5_6_local_verify.py) | [Independent endpoint verifier](reviews/verify_joint_5_6_two_ended.py) proves untileability using the distinct-length closure |

The endpoint verifier derives its local configurations independently and
includes a regular-hexagon positive control. It does not independently
rederive the exact closure intervals; that dependency is checked by the
original local verifier first. Its [review](reviews/joint-5-6-two-ended-review.md)
states the proof and review limits.

Producer reruns reproduce their original calculations; they are not separate
implementations. Independent implementations are still conditional on the
transcribed mathematical input and do not validate all source conventions
or unbounded claims. None of these checks proves a global mixed tiling exists,
universal aperiodicity, or completeness of the literature search.

## Discovery provenance

The joint partition's random seed and randomized discovery generator were
not retained. Only the selected fixed data, exact closure, local language,
and subsequent falsification can be replayed. The deterministic Walton and
scaffold scripts retain their finite domains; see their reports for scope.
Do not claim reproducibility of the missing randomized discovery stage.
