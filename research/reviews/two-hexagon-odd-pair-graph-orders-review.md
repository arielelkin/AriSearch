# Independent full odd-pair graph/native-order review

Date: 2026-10-12. **Verdict: VALID for the complete stated unique-B-pair, mixed-only exact angle-type family.** All eight graph families and all branching metric obligations are checked. This is a family exclusion from aperiodicity, not closure of the global two-polygon problem.

## Independent domain census

[The checker](check_two_hexagon_odd_pair_graph_orders.py) imports no producer or solver and never runs CP-SAT. It generates degree-two pseudographs by orienting disjoint cycles: for every permutation of the six A vertices it records the multiset of unordered edges i--p(i), then deduplicates. Every degree-two pseudograph admits such a cycle orientation, including a fixed-point loop and a two-cycle represented by two parallel edge occurrences. Thus this generation is complete and structurally independent of the producer's degree-budget search.

It obtains 388 labeled degree-two pseudographs, of which 268 have an odd component. Every loop contributes two incidences and every parallel occurrence is counted separately. The eight odd-component families and counts are:

| Components | Graphs | B cyclic words | Empty | Functional | Branching |
| --- | ---: | ---: | ---: | ---: | ---: |
| 5+1 | 72 | 4320 | 4272 | 48 | 0 |
| 4+1+1 | 45 | 2700 | 2676 | 6 | 18 |
| 3+3 | 10 | 600 | 581 | 15 | 4 |
| 3+2+1 | 60 | 1800 | 1794 | 6 | 0 |
| 3+1+1+1 | 20 | 1200 | 1198 | 2 | 0 |
| 2+2+1+1 | 45 | 720 | 708 | 0 | 12 |
| 2+1+1+1+1 | 15 | 450 | 450 | 0 | 0 |
| Six loops | 1 | 60 | 60 | 0 | 0 |
| Total | 268 | 11850 | 11739 | 77 | 34 |

Distinct multiset words are independently built recursively from their occurrence counts, then explicitly partitioned into rotation/reversal orbits. This verifies all 11850 native B pair-value representatives without treating parallel edges as distinct values or silently losing multiplicity. The A labels remain fixed; no inequivalent SFT count under A symmetry is claimed. Exchanging indistinguishable parallel occurrences changes no native pair-value word and imposes no side-length equality beyond the independently handled metric data.

The mathematical reduction from the stated unique-B exact type to this domain is consistent with [the graph classification](../lemmas/two-hexagon-unique-b-pair-graph-classification.md). With one B corner per star, the species phase and invariant corner ledger give B weight 1/3. Since each native B corner has one star, its weight is 1/3 individually. Each A native corner then has degree two, counting loop multiplicity. The six defining rows have rank five modulo polygon sums. Their additional closure triples are exactly pure-B perfect matchings, so mixed-only exact types require an odd component. Every B label's unique occurrence also makes every covering closed ancestor equal to the entire six-star type. Those conditions are essential to the complete-family scope.

## Full local spatial verification

For every native-order row the checker rebuilds all B-centered rings from independently derived canonical triangle incidences and full reflected A/B placement labels. It checks 29736 ring states. Pair relations are reconstructed by lattice coordinate subtraction at the two shared A cells. Every edge deletion and triangle deletion is independently justified against the state set **before** its simultaneous deletion round. All 1843 recorded rounds are valid.

The actual retained successor degrees agree. Empty cores discharge 11739 orders; 77 cores have a direction with outdegree at most one and satisfy the independently reviewed [functional periodicity criterion](../lemmas/two-hexagon-one-b-ring-spatial-reduction.md). The function acts on full ring states, not just species or B orientation. A surviving or branching local core alone is never promoted to infinite extension.

The earlier 780-word analytic loop exclusion was withdrawn. Only the universal all-six-loops argument yields the stated 60-word analytic subfamily. This checker does not use either claim as a shortcut: it explicitly reconstructs **every** word in all eight rows, including all loop-containing mixed graphs. Consequently the withdrawn argument is not a dependency of any retained census result. Mixed loops can have a nonloop star at the opposite A/A endpoint, so they cannot silently inherit the all-loop chirality argument.

## Complete metric and periodic-witness coverage

All 34 branching orders are covered by 49 required forced side-equivalence closures. The closures are independently reconstructed from every surviving ring by enumerating the seven-cell patch's actual adjacent cells and mapping native sides through their corner endpoints. This includes the reflected-side offset r−k−1.

For 30 new branching orders, the direct metric artifact supplies 18 periodic witnesses and the residue artifact supplies the remaining 12 positive witnesses at original-cell indices nine or twelve. Their earlier bounded-no-torus fields remain historical outcomes; they are not unresolved obligations after the new retained labels are verified.

The four old two-triangle orders require care because the new lexicographic B necklaces and old rooted representatives can choose opposite reflections. The checker finds an explicit native B dihedral corner map, derives its side map from corner endpoints, transforms all B placement symbols and side classes, and checks the resulting torus labels against the **new** angle triple set and forced metric closure. Nineteen old metric witnesses transfer correctly. A labels and lattice coordinates stay fixed; no unproved equality of differently labeled side classes is assumed.

Every one of the 49 torus labelings has its complete fundamental cell set, valid placement symbols, exact used native corner triples and glued native sides independently checked. Used triples belong to the corresponding six-star T and side equalities belong to the forced equivalence closure. An actual metric admitting any surviving ring has an equality relation at least that coarse, so it admits the corresponding torus. No solver infeasibility verdict or proposed finite torus-size bound is needed for this implication.

[Controls](two-hexagon-odd-pair-graph-orders-check.json) retain the exact hashes of the all-order census, new metric artifact, residue artifact and two old transfer sources. They confirm 34 covered branching orders, 49 forced metric closures and 49 legal periodic witnesses.

## Scope and replay

Combining the complete graph domain, exact empty-core exclusions, functional-state criterion and forced-metric torus gates excludes aperiodicity throughout the stated unique-B-pair mixed-only exact angle-type family. It does not classify all descendants or specializations with extra angle triples, all 2A+1B types with multiple B stars, other species compositions, or the global hexagon/pentagon problem. Abstract graph or torus feasibility does not create a Euclidean polygon realization.

The checker prints controls by default and optionally writes them to --output PATH. Registered replay can use a temporary output. It rechecks retained finite artifacts and calls no search solver:

```bash
MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_two_hexagon_odd_pair_graph_orders.py --metrics research/certificates/two-hexagon-odd-pair-graph-ring-metrics.json --residue research/certificates/two-hexagon-odd-pair-residue-tori.json
```
