# Two Convex Tiles

An autonomous attempt to construct two unmarked convex polygons that tile the plane only aperiodically, or prove that no such pair exists.

Use native Linux x86-64 (including WSL2 or a Linux VM), with host-installed
[mise](https://mise.jdx.dev/) and [uv](https://docs.astral.sh/uv/).
GitHub operations use the host's `gh`; setup does not install `gh` or `uv`.
Allow at least 12 GiB free for a fresh installation. From the checkout:

```bash
mise trust
mise run setup
```

Mise installs the pinned Conda CLI and runs setup and verification tasks. Conda
owns every research dependency, including Python, SageMath, solvers and
scientific command-line tools. Setup installs the existing
[linux-64 lock](environment/conda-lock.yml), using
`conda-lock==4.0.2` through host uv. Everything installed for research stays
under ignored `.local/conda/`; setup never edits shell startup files or agent
settings. Enable mise's shell integration or use `mise exec --` when running
Conda commands directly.

Setup reports when an environment already exists and always verifies it against
the current lock. A failed verification makes setup fail. After stopping any
jobs and preserving their checkpoints, remove only
`.local/conda/envs/arisearch` and rerun setup to rebuild it.

Run `mise run clean` to reclaim Conda package-cache space after installation.
Cached packages may need to be downloaded again for a rebuild.

Open this folder normally in VS Code, or use Remote SSH/WSL. The workspace
settings default Python to `.local/conda/envs/arisearch/bin/python` and recommend
the Python, Jupyter, and agent extensions. Select that environment for Jupyter
kernels or if VS Code has already saved a different interpreter.
Use ordinary SSH forwarding for an optional HTTP server on port 8000.
Then give [`main_prompt.md`](main_prompt.md) to a research agent when you intend
to resume research. Setup and verification do not resume paused searches.
The target and procedure are defined in [`research-problem.md`](research-problem.md)
and [`research-protocol.md`](research-protocol.md).

The [current discovery log](discovery-log.md) is the restart entry point. The
problem remains unresolved; both recorded exact pentagon–hexagon pairs are
falsified. The discovery log indexes the subject-specific proofs, exact
searches, certificates, literature findings, and reviews under `research/`,
including verification scope and remaining research obligations.

The bounded discovery experiments have their own
[restart checkpoint](research/discovery/CHECKPOINT.md). Their complete checks
and fresh replays are `mise run discovery-checkpoint` and
`mise run discovery-replay`; these are separate from the historical registry
below. The checkpoint records zero live leads and the next proposed generation
experiment. The [pre-commit review](research/discovery/commit-review-2026-10-25.md)
records the latest fixes, validation and file-retention audit.

Run the registered certificate replays and independent checks without
overwriting retained certificates (the registry does not cover every search):

```text
mise run replay
```

`mise run verify-environment` checks locked package builds, Python distribution
versions and unexpected packages, command provenance, and solver smoke tests.
Independently, `mise run replay` runs the entire research registry on a disposable
copy and checks that the original research files remain unchanged. Replay is all-or-nothing. Assertions must remain enabled.
The registry checks retained finite results,
not mathematical completeness or every historical search. Checkpoint-writing
searches must have only one writer; several rely on Linux advisory locks.

To change dependencies deliberately, edit `environment/environment.yml`, run
`mise run lock`, and commit the specification and regenerated lock together.
Rebuild the environment, verify it, and replay research before resuming work.

For checkouts migrated from the devcontainer, retained agent state remains in
`~/.agent-state/<checkout-folder>/`; native applications use their host settings.
Keep old containers and retained state until needed sessions are recovered.
Codespaces permission overrides are not applied to host applications. The native
migration regenerated the lock with identical package versions and artifact
hashes after adding exact pins and an explicit `pyyaml` dependency.

Inspired by DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) and OpenAI's [Cycle Double Cover prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf).
