# Exact scalene Cairo pair: finite periodic witness verification

The [lemma](../lemmas/cairo-two-scalene-periodic.md) gives exact original polygons
and a four-face periodic escape. The candidate parameter family is falsified
as an aperiodicity construction by a complete torus witness, not bounded search.

## Exact domain and encoding

The concrete coordinates lie in Q(w), w^2=3 and1<w<2. Each coordinate is retained
as a pair of rational coefficients (constant,w). Parameters are p=1,r=1/2,
q=w-1/2,s=2-w/2. The certificate specifies20whole side occurrences on four
unreflected faces A,A,B,B and10reversed endpoint pairings. The finite checker
uses exactly these two five-vertex polygons and this one gluing list. It checks
all5squared lengths, all5angle cosines, every native edge's support inequality
against all polygon vertices, unequal congruence classes, all20sides used once,
6quotient vertices (four triples/two quadruples), source-angle sums360degrees,
connectedness, and Euler characteristic0. Boundary reversal makes the quotient
orientable; the mathematical proof develops the flat universal cover.

The checker also verifies the [finite local diagnostic](../counterexamples/cairo-partial-beta-length-graph.md)
by exact cone inequalities for three transformed copies of A. Their interiors
are disjoint and cover sectors0..120,120..240,240..360at the origin. Two shared
rays have unequal native edge lengths p,q and only length-p contact. No global
extension of this patch is claimed.

## Replay, certificate, and execution

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_two_scalene.py
```

Retained [certificate](../certificates/cairo-two-scalene-torus.json). Assertions
must be enabled. No random seed, solver, timeout, or memory cutoff is used.
All consequential computations use exact Sage rational/quadratic-field arithmetic;
the positive real embedding is specified by Sage AA(sqrt3), not a floating-point
sign approximation. No rendered geometry is needed.

Execution,2026-10-09: Conda `arisearch`; Python3.12.13;
10.9; Linux x86_64. Fresh verifier completed
in2.002s excluding Conda startup:

```text
PASS: exact Q(sqrt3) distinct convex Cairo pentagons; four-face connected orientable flat torus; exact three-copy partial-contact beta-star diagnostic.
```

Certificate SHA-256: `d05ffcae5478d61145435e3d6a20ea78f445fd19e03adc196ec7dc1a83798da1`.

## Discarded reconnaissance and limitations

The witness was located by enumerating the105perfect matchings of8p-side
occurrences and105matchings of8q-side occurrences, with the two private-side
pairs forced. Four faces with A0unreflected and three independent reference
reflection flags give an88,200-model complete domain. The first valid model
was found at6,281tested candidates, so that discovery run was **not exhausted**.
Its search script/output are discarded reconnaissance: none of the proof
relies on exhaustion or on negative claims. The retained direct certificate
and independent checker are the complete finite evidence for the witness.
A separate18-model two-A-face exploratory check found none; that negative
experiment is also discarded and proves no monohedral exclusion.

The beta-to-right native sides permit partial-edge contacts ending in right
T-junctions. Consequently a corner graph based on full native lengths is not
valid at arbitrary beta vertices. Neither original member's monohedral
plane tilability is classified here. No novelty claim is made. Fresh independent
hostile review of the exact family and this failed local shortcut is pending.
