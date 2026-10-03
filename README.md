# Two Convex Tiles

An autonomous attempt to construct two unmarked convex polygons that tile the plane only aperiodically, or prove that no such pair exists.

Open the repository in its dev container, then give [`main_prompt.md`](main_prompt.md) to a research agent. The target and procedure are defined in [`research-problem.md`](research-problem.md) and [`research-protocol.md`](research-protocol.md).

The [current discovery log](discovery-log.md) is the restart entry point. The
problem remains unresolved; both recorded exact pentagon–hexagon pairs are
falsified. See [the artifact guide](research/README.md) for proof organization,
review coverage, reproduction limits, and historical checkpoints.

Replay all retained certificates without overwriting them:

```text
conda run --no-capture-output -n arisearch python3 research/verify.py
```

Inspired by DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) and OpenAI's [Cycle Double Cover prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf).
