# Two Convex Tiles

An autonomous search for two unmarked convex polygons that tile the plane only aperiodically.

Open the repository in its dev container, then give [`main_prompt.md`](main_prompt.md) to a research agent. The target and procedure are defined in [`research-problem.md`](research-problem.md) and [`research-protocol.md`](research-protocol.md).

Restartable research state is indexed in [`discovery-log.md`](discovery-log.md).
Self-contained partial results, counterexamples, and reviews belong under
[`research/`](research/); none of these artifacts is a solution unless it
satisfies every acceptance criterion in `research-problem.md`.

Inspired by DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) and OpenAI's [Cycle Double Cover prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf).
