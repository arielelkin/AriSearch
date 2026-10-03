# Two ended edge review of the joint pentagon and hexagon pair

**Date:** 2026-10-03. **Verdict:** falsified; no plane tiling exists.

## Claim and dependencies

The [joint synthesis](../searches/joint-5-6-restart.md) defines two exact
strictly convex polygons. The original
[local verifier](../searches/joint_5_6_local_verify.py) certifies their positive
closure and five distinct side-length classes. Angle nonresonance forces
edge-to-edge contacts. Its nine angle-and-length-compatible corner rows and
chirality-balanced counts are necessary conditions, not an edge pairing.

## Missing condition

At one endpoint of a shared side, suppose tile sectors a and b are consecutive
in counterclockwise order. At the other endpoint, the same tile occurrences
are consecutive in the order b then a. The native side fixes each tile's
other corner; each tile's reflection flag remains unchanged. Thus this reversed
pair of other corners must occur in some allowed vertex configuration.

Enumerate every ordered/chiral vertex configuration for the exact angle and
side data, not merely the six balanced rows. Remove a configuration whenever
one consecutive pair lacks a compatible opposite endpoint. Repeat on the
remaining language. If a plane tiling existed, all its vertices would survive
each pass: the other endpoint of each edge is another surviving tiling vertex.
This induction makes an empty final language a finite impossibility proof.

## Exhaustion and result

The finite domain is all multisets of 3–5 labelled corners summing to 2 pi,
all their distinct orders, and all binary reflection flags. Six corners are
impossible because the minimum angle is 66 degrees. Nonresonance is checked
exactly in integer units of pi/60.

| Pass | Input configurations | Directed corner pairs | Pairs with opposite endpoints | Retained configurations |
|---|---:|---:|---:|---:|
| 1 | 94 | 44 | 30 | 12 |
| 2 | 12 | 12 | 6 | 0 |

After pass 1, only rows `(2,4,10)` and `(3,8,9)` remain. They already omit
required corners; pass 2 empties the language entirely. The full nine-row
language, including all three rows outside the original balanced support,
is therefore untileable. Reflections and every cyclic order are included.

## Replay and review coverage

[The standalone verifier](verify_joint_5_6_two_ended.py) independently
implements the enumeration from the fixed data and derives other endpoints
from native side endpoints. It does not import the original star enumerator.
Run the repository-wide command from the repository root:

```text
conda run --no-capture-output -n arisearch python3 research/verify.py
```

The runner also accepts an absolute script path from another working directory.
The runner first checks the retained distinct-length closure certificate.
A separate ad hoc calculation using corner increments gave the same two-pass
result during review. A regular-hexagon positive control also survives the
endpoint filter. These are checks by the reviewing agent, not a separate
hostile-agent audit. The permanent verifier retains the positive control.

## Consequences and limits

Positive closure, the initial local language, and its incidence counts remain
correct. The missing compatibility condition prevents them from describing
any tiling. No torus search or chain-synchronization analysis is needed for
these exact shapes. This does not exclude other side partitions with the same
angles, the nonresonant (5,6) mechanism generally, or all two-convex-tile sets.
