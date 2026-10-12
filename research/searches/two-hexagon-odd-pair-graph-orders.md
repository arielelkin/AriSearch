# Spatial and metric census of the unique-B-corner pair-graph family

Date: 2026-10-12. **Exact finite computations completed; fresh independent
review in progress.** This extends the two-disjoint-triangle root to all
eight odd-component pair-graph types. It is not a census of arbitrary
two-hexagon angle types or a solution of the unrestricted problem.

## Domain

Each of the six native B corners belongs to precisely one allowed triple,
which contains that corner and a two-multiset of native A corners. The six
A pairs form a pseudograph on the six native A positions. Loops count
twice toward degree. The separate
[pair-graph classification](../lemmas/two-hexagon-unique-b-pair-graph-classification.md)
provides the reduction to degree two and the exact-closure condition.

All degree-two labelled pseudographs are enumerated by a finite degree-budget
search over the 21 unordered A pairs, allowing repeated edges. There are
388 graphs. Exactly 268 have an odd component and therefore belong to the
stated exact six-AAB-triple family. Their component shapes and graph counts are:

| Components | Labelled graphs |
|---|---:|
| 5+1 | 72 |
| 4+1+1 | 45 |
| 3+3 | 10 |
| 3+2+1 | 60 |
| 3+1+1+1 | 20 |
| 2+2+1+1 | 45 |
| 2+1+1+1+1 | 15 |
| 1+1+1+1+1+1 | 1 |

For each graph enumerate cyclic orders of its six pair **values** modulo
rotation and reflection. Parallel edge occurrences with identical pair
values yield identical native triple data and need not be distinguished.
This is safe with arbitrary side equivalences: each native B position
still has its own side labels, and the theorem quantifies over every e.
No dihedral quotient on the native A positions is taken. The exact domain
contains **11,850 rooted orders**; these are not claimed globally inequivalent.

## Solver-free angle-state census

For each order enumerate every full B ring and its neighbour compatibility
using the definitions of the
[one-B ring reduction](../lemmas/two-hexagon-one-b-ring-spatial-reduction.md).
Repeatedly remove states lacking a directional successor, then states
without a compatible completion of an elementary B-lattice triangle.
Every deletion is retained as an integer state/direction record. No grid
solver or bounded negative torus search establishes these exclusions.

| Components | Empty cores | Functional cores | Branching cores |
|---|---:|---:|---:|
| 1+1+1+1+1+1 | 60 | 0 | 0 |
| 2+1+1+1+1 | 450 | 0 | 0 |
| 3+1+1+1 | 1198 | 2 | 0 |
| 2+2+1+1 | 708 | 0 | 12 |
| 4+1+1 | 2676 | 6 | 18 |
| 3+2+1 | 1794 | 6 | 0 |
| 5+1 | 4272 | 48 | 0 |
| 3+3 | 581 | 15 | 4 |
| **Total** | **11,739** | **77** | **34** |

An empty angle core excludes every side equivalence. A functional core
has a direction with at most one successor per full state. The general
functional-direction theorem then gives a periodic escape for every
actual metric configuration, including those obtained by the unrestricted
defect-free-limit reduction.

## Metric coverage of all branching cores

Each surviving full ring forces twelve native side equalities. Let E_ring
be their equivalence closure. Every actual e permitting the ring contains
E_ring. A torus whose required side pairs belong to E_ring is consequently
a periodic witness for the same actual e, not just for an angle-only model.

The four 3+3 branching orders were already covered by nineteen distinct
local metric closures and their exact tori. The thirty other branching
orders each have one common E_ring across their surviving states. Eighteen
have a retained periodic torus of original cell index three or six.

The remaining twelve orders have shape 4+1+1 and twelve-state cores with
two successors per direction. A positive witness attempt at original cell
indices nine and twelve found a torus for **every one** of them. Thus the
complete branching library has **49 metric closures and exact escapes**:
nineteen for the old four orders, eighteen for the new small-index cases,
and twelve for the final residue. No negative bounded search is needed
for the completed coverage argument.

The residue rooted IDs are:

    374,418,923,1155,3627,4148,5482,5757,5998,8614,9887,10940.

There is also a solver-free structural explanation. For each of the 144
residue states, its six neighbours each have at most two candidate states.
Of the at most 64 choices, precisely one satisfies all six neighbour-neighbour relations
around the wheel. Any global field therefore uses the induced deterministic
successor maps. The wheel certificate provides another exact finite gate;
the separate strategy agent independently reconstructed commuting state
maps and explicit index-twelve stripe witnesses.

## Artifacts

Producers:

* `research/searches/two-hexagon-odd-pair-graph-orders.py` — exact graph,
  cyclic-order, ring, compatibility and pruning enumeration.
* `research/searches/two-hexagon-balanced-root-ring-metrics.py` — forced
  local metric closures and positive index-three/six torus witnesses.
* `research/searches/two-hexagon-odd-pair-residue-tori.py` — the twelve
  remaining positive index-nine/twelve witness attempts.
* `research/searches/two-hexagon-odd-pair-residue-wheels.py` — the 144
  exact unique-wheel computations, without a solver.

Certificates:

* `research/certificates/two-hexagon-odd-pair-graph-orders.json`
* `research/certificates/two-hexagon-odd-pair-graph-ring-metrics.json`
* `research/certificates/two-hexagon-odd-pair-residue-tori.json`
* `research/certificates/two-hexagon-odd-pair-residue-wheels.json`
* The previous 3+3 certificates remain their original retained files.

The metric SAT producer uses OR-Tools CP-SAT with one worker, seed zero
and a three-second timeout per torus. Every retained SAT labelling is checked
directly. No timeout occurred in the completed positive library. Earlier
bounded negative queries remain labelled only by their finite scope.

The fresh independent reviewer exclusively maintains
`research/reviews/check_two_hexagon_odd_pair_graph_orders.py`; it generates
the graph domain from cycle-cover permutations rather than the producer's
degree-budget search, reconstructs native rings without producer imports,
checks every pruning record, and checks required native side pairs of tori.
The final review record controls when these computations may support an
extracted family theorem.

## Replay

All commands use the locked research environment. Regeneration writes the
explicit output path, so use temporary paths to preserve retained evidence.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/two-hexagon-odd-pair-graph-orders.py TEMP_ORDERS.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/two-hexagon-balanced-root-ring-metrics.py research/certificates/two-hexagon-odd-pair-graph-orders.json TEMP_METRICS.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/two-hexagon-odd-pair-residue-tori.py TEMP_RESIDUE_TORI.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/two-hexagon-odd-pair-residue-wheels.py TEMP_WHEELS.json

## Exact remaining scope

Subject to the separate reviewed graph-classification, global hexagon
encoding and ring-periodicity theorems, this complete finite library excludes
the exact six-star unique-B-pair family for all metrics and native orders.
Additional angle triples, multiple A pairs assigned to one B corner, pure
stars, one-A/two-B triples and pentagon-containing pairs remain outside it.
No finite census here licenses exclusion of those broader domains.
