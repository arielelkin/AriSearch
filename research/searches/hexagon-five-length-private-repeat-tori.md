# Focused private-repeat endpoint and torus certificates

**Objects:** A=(0,1,0,2,3,4), B=(5,3,5,2,1,4), representing six pairwise distinct
positive numerical lengths. Corners a_i,b_i are after native side slot i.
The [conditional geometric theorem](../lemmas/hexagon-five-length-private-repeat-periodicity.md)
uses generic corner-angle choices (x,y) and nongeneric supports x=y.

## Finite verification domain

The retained certificate contains exactly two explicit four-face quotients,
one for x=y=0 and one for x=y=1. Each uses two A and two B faces. For the first,
A1 and B1 are reflected; for the second all faces use the displayed references.
The reflected reference word is the original word in reverse order, and its
corner slot i corresponds to original corner (4-i) mod6. The checker verifies
24 whole native side occurrences, 12 equal-length pairings, the precise eight
three-corner vertex classes, connectedness, and Euler characteristic0.
Every edge reverses endpoint order in its chosen face-boundary orientations,
so each quotient is orientable. Its source-angle triples each occur twice;
the theorem supplies their 2pi sums and the Euclidean development.

For all four generic (x,y) supports, the checker visits every same-numerical-length
neighbor-side occurrence from either type and both endpoint bijections, for
each of the twelve native side slots. This is 192 candidates in total. A candidate
survives exactly when its endpoint corner pairs both belong to an allowed
source star (corner multiplicities are retained using integer counters).
Exactly one relative neighbor-side/endpoint candidate survives per side.
Convexity and opposite side interiors then determine a unique relative
isometry mathematically; no numerical placement calculation is used.

## Commands, conditions, and outcome

```text
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-private-repeat-verify.py
```

Retained [certificate](../certificates/hexagon-five-length-private-repeat-tori.json).
The checker neither imports a search generator nor edits its inputs. Integer
arithmetic only; no solver, randomness, floating-point geometry, time limit,
or memory cap. Assertions must remain enabled.

Execution on 2026-10-09: Conda `arisearch`, Python 3.12.13,
Linux x86_64; standard library only. Fresh verification
completed in 0.030s excluding Conda startup:

```text
PASS: both private-repeat four-face tori; eight specified corner triples; connected orientable chi=0; all192 endpoint candidates give unique neighbors for four generic supports.
```

Certificate SHA-256: `dba8222715575ad8f98890db37ddd21f78b9d292eb872f0ebba18cba259ed645`.

## Discovery reconnaissance and scope

Discarded reconnaissance enumerated the 3^6 whole-side matchings on four faces
and eight reference reflection choices, checking trivalent topology only. It supplied
the two retained explicit witnesses. Its failure to yield other four-face
supports is **not** used: generic uncoupled supports are handled instead by
[the intrinsic-state geometric lemma](../lemmas/hexagon-five-length-intrinsic-determinism.md).
The discarded enumeration is not part of the evidence chain; only the
small retained certificates and direct verifier support the finite claims.

These computations do not infer a plane tiling from local stars or prove an
unrestricted two-hexagon theorem. The group lemma additionally requires actual
connected full-side tiling and geometry-derived unique relative isometries.
Whole-claim fresh hostile review of both proofs is pending. No novelty claim.
