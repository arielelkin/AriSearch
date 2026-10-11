# Exact five-length sparse-sharing classification

**Objective:** classify corner-length patterns for two hexagons having exactly
five distinct lengths, the single repeated length at side-slot separation two,
and at most three shared length values. Support the
[periodic-witness theorem](../lemmas/hexagon-five-length-sparse-sharing.md).

## Complete finite domain

A=(0,1,0,2,3,4). For k=0,1,2,3 choose k shared A symbols and 5-k fresh B-private
symbols. The B word is (p,q,p,r,s,t) on those five symbols; p is repeated and
q is its short-arc neighbor. The remaining three symbols are ordered subject
to r<t, which removes B reversal. There are 5*4*3=60 words per five-symbol set,
and domain counts 60,300,600,600, totaling 1,560. Rotation is fixed by starting
at the first repeat slot on the short arc; reversal exchanges its endpoints.

A graph edge represents an unordered adjacent pair of numerical side lengths.
Actual corner occurrences remain separate despite a duplicated graph edge.
The necessary filter retains a word exactly when every edge of the union of
the two simple corner graphs belongs to a triangle. It retains no word for
k<3 and one for k=3: B=(0,3,0,5,1,6). No numerical geometry or solver is used.
The theorem's additional endpoint relation and four-face flat torus are
mathematical steps; the necessary graph filter alone is not a tiling test.

The separate verifier enumerates all permutations of each five-symbol set
with each repeated symbol added, totaling 93,600 raw permutations (duplicate
permutations from the repeated symbol are deliberately retained). It checks
repeat separation two/four and then quotients rotation/reversal, independently
recovering the stated 1,560 words. It verifies the same unique survivor and
both proposed formal repeated-slot assignments using explicit endpoint unions
of all 24 side occurrences, eight three-corner vertex classes, and a connected
orientable Euler-characteristic-zero quotient. It also checks the exact
rational abstract-angle counterexample and its failed opposite-endpoint sum.

## Replay and execution

```text
conda run --no-capture-output -n arisearch python3 research/searches/hexagon-five-length-classify.py
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-verify.py
```

Retained [JSON certificate](../certificates/hexagon-five-length-classification.json).
The generator prints JSON without modifying the certificate. The verifier does
not import or execute that generator. Assertions must be enabled. No stochastic
seed, solver, floating-point decision, timeout, or memory cap is configured.
Only standard-library integer and rational arithmetic is used.

**Execution record, 2026-10-09:** Conda `arisearch`, Python 3.12.13,
Linux x86_64. Fresh generator completed in 0.114s
(excluding Conda startup) and parsed JSON exactly matched the retained certificate.
Fresh verifier completed in 0.261s:

```text
PASS: 93600 raw words / 1560 normalized words; unique k=3 survivor; 2 four-face endpoint gluings; rational angle-only selection counterexample.
```

Certificate SHA-256: `13b94cf9135f22806cb39cd8a848e49e0fbfdcfec0a44c7aec381bc592e5487d`.

## Scope and restart

This finite domain completed. It does not classify four/five shared lengths,
repeat separation one/three, or a six-distinct/five-distinct pair. Exploratory
counts for the excluded shared-count domains are not used in any stable claim.
The [diagnostic angle support](../counterexamples/hexagon-five-length-angle-support.md)
is abstract angular data without a certified closed polygon pair. Continue by
using full side-slot endpoint compatibility in any larger sharing domain;
angle-only star coverage does not justify a compatible torus witness.
Independent whole-claim hostile review remains to be recorded. No novelty claim
is made, and this restricted result does not resolve the original problem.
