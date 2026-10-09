# Two Convex Tiles

An autonomous attempt to construct two unmarked convex polygons that tile the plane only aperiodically, or prove that no such pair exists.

Open the repository in its dev container, then give [`main_prompt.md`](main_prompt.md) to a research agent. The target and procedure are defined in [`research-problem.md`](research-problem.md) and [`research-protocol.md`](research-protocol.md).

The devcontainer persists Codex and Claude state on the host under
`~/.agent-state/<checkout-folder>/`, including Claude's `.claude.json`.
VS Code server files are shared through `~/.vscode-server`, with workspace
state isolated in `~/.vscode-server-workspaces/<checkout-folder>/`. These
mounts survive container deletion and rebuilds.

The [current discovery log](discovery-log.md) is the restart entry point. The
problem remains unresolved; both recorded exact pentagon–hexagon pairs are
falsified. The discovery log indexes the subject-specific proofs, exact
searches, certificates, literature findings, and reviews under `research/`,
including verification scope and remaining research obligations.

Replay all retained certificates without overwriting them:

```text
conda run --no-capture-output -n arisearch python3 research/searches/verify.py
```

Inspired by DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) and OpenAI's [Cycle Double Cover prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf).
