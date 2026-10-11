# Exact Cairo internally-distinct edge-to-edge obstruction replay

**Status:** complete exact finite verification; mathematical scope remains edge-to-edge.
**Date:** 2026-10-09 (UTC).
**Claim:** [lemma](../lemmas/cairo-distinct-side-edge-obstruction.md).

## Exact input domain

Both pentagons have angle word (90,120,90,120,120) degrees after their native
sides and each has five internally distinct positive side lengths. Whole-side
matching at 120-degree corners forces the two selected unordered equalities
in the lemma. Each equality has two bijections, giving exactly four second
polygon words:

1. (b,a,d,c,f)
2. (c,a,d,b,f)
3. (b,d,a,c,f)
4. (c,d,a,b,f)

These four cases exhaust the necessary corner constraints, including all
additional cross-type coincidences of f. No bound on faces, patches, periods,
or side-length denominators is involved. Numerical side lengths are not
sampled. Reflections are handled by the unordered corner-edge constraints;
closure is derived separately in each polygon's counterclockwise reference.

## Arithmetic and implementation

[Verifier](../reviews/verify_cairo_distinct_side_ete.py) uses the exact field
Q(w), w^2=3, with the positive real embedding, then the polynomial ring
Q(w)[c,d,e]. The pentagon closure equations eliminate a and b. For each of
the four B words, its first closure eliminates f and its second closure
residual is exactly a nonzero scalar multiple of L=d+e-w*c. It additionally
checks a-d=-L/2 and b-c=w*L/2. The graph and sector-equation checks are finite
exact integer/set operations. This program is a proof check, not a plane
tiling search, and it supplies no unrestricted-contact obstruction.

## Execution and provenance

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_cairo_distinct_side_ete.py
```

- Interpreter: Python 3.12.13.
- SageMath: 10.9.
- Replay wall time in the selected environment: 1.738 seconds.
- Verifier SHA-256: `45b7c56002cfb40041498e8b02af72efa04059923a8e4279fe4d3894b1abd54f`.
- Output: `PASS: exact angle/120-corner graph constraints; all four B closure cases force a=d,b=c.`.

The displayed four-case symbolic identity can also be checked manually; the
lemma contains its full derivation. No theorem of polygon tiling classification
or externally sourced mathematical result is needed here. No novelty claim
is made. The existing [partial-contact counterexample](../counterexamples/cairo-partial-beta-length-graph.md)
records the failed whole-length inference for unrestricted right-angle tilings.
