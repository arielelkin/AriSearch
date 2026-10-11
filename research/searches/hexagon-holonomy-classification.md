# Exact distinct-length hexagon side-order search

**Mathematical purpose:** prove the finite classification used in
[the periodic-witness theorem](../lemmas/hexagon-holonomy-distinct-lengths.md),
then audit every finite torus gluing and the angle-support selection lemma.
This is a completed finite classification, not a bounded periodic search.

## Exact domain and representation

A is the six-cycle (0,1,2,3,4,5). For k=5 shared side-length symbols choose
any five A symbols and the one B-private symbol 6; for k=6 use all six A
symbols. B is any cyclic permutation, modulo its six rotations and two
reflections. The domain is 6*60+60=420 normalized pairs. The generator fixes
the smallest B symbol first and retains the order with second symbol smaller
than last. This exhausts every unoriented cyclic order exactly once.

The graph edge {x,y} means an actual corner between consecutive side symbols,
not a tile adjacency. A pattern survives precisely when every graph edge is
contained in a graph triangle. Shared graph edges retain separate A/B corner
occurrences in the angular audit. Relabelings by A's dihedral group and private
symbol permutations provide the final equivalence classes; both polygon
reflections remain allowed. Four-symbol retained subsets model a chosen periodic
witness's contacts, not imposed restrictions on original tilings.

The independent verifier instead visits all 5,040 linear permutations and
normalizes afterward. It checks that the retained survivor set is complete.
For all 30 surviving normalized pairs, all C(k,4) retained-common-symbol choices
are checked. Exactly 54 choices give the four-triangle ring. Every proposed
four-face quotient is checked using actual edge-slot endpoint unions: 24 whole
sides, 12 pairings, 8 three-corner vertices, connected face graph, Euler
characteristic zero, and the precise source-corner triple at each vertex.
Boundary endpoint reversal gives orientability; the mathematical proof supplies
the flat metric and Euclidean development.

For the four dihedral classes the verifier enumerates all subsets of possible
corner-typed triangle stars (64,64,256,256 subsets respectively). Exactly 95
subsets cover all twelve actual corner slots. For every such subset, it computes
exact rational linear consequences of those star equations and the two hexagon
angle-sum equations. It verifies that some retained four-triangle ring has all
four angle equations in that span. This is stronger than checking one favored
star support; positivity need not be assumed for this algebraic implication.

## Commands and completion

```text
conda run --no-capture-output -n arisearch python3 research/searches/hexagon-holonomy-classify.py
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-holonomy-verify.py
```

The generator prints its certificate without modifying files. Retained exact
JSON: [hexagon-holonomy-classification.json](../certificates/hexagon-holonomy-classification.json).
The independent verifier does not import or execute the generator. Assertions
must be enabled. No solver, stochastic seed, network, floating point geometry,
timeout, or memory cutoff is involved. Integer and rational computations only.

**Execution record, 2026-10-09:** Python 3.12.13,
Linux x86_64, Conda environment `arisearch`,
standard library only. A fresh generator run completed in 0.077 seconds
(excluding Conda startup) and its parsed JSON exactly matched the retained
certificate. A fresh independent verifier run completed in 0.114 seconds:

```text
PASS: 5040 raw words / 420 normalized words; 30 survivors; 54 four-face torus gluings; 95 covering angle-support cases.
```

Certificate SHA-256: `f21355e6fa4a84939a8842d342e5959a70e9aa0e5cf183514efc6eab382afd6f`.

## Scope

The finite classification and all checks above completed. The computation does
not establish arbitrary two-hexagon impossibility or create novel prototiles.
The theorem combines this complete finite domain with a mathematical flat-torus
construction and the existing defect-free limit lemma. Repeated side lengths
within either polygon lie outside this domain. Independent whole-claim hostile
review and the defect-limit dependency's re-review are recorded separately.

## Literature audit, 2026-10-09

The original three narrow queries and primary-source checks have been
consolidated into the broader mechanism-specific
[prior-art audit](../literature/hexagon-distinct-lengths-prior-art.md).
It compares length and corner graphs, local corona assumptions, old
2-isohedral catalogs, and flat-torus realization. No novelty claim is made.
