# Fresh root hostile audit of the complete distinct-length two-run catalog

**Verdict: VALID for exactly66 distinct-length pairs**, with54 unrestricted untileable and12 explicitly periodic. Root did not develop the catalog enumeration, strong-dual producer or transfer construction. It read the actual [classification](../lemmas/branching-hexagon-new-two-run-catalog-slot-classification.md) and constructed two independent no-producer/no-solver checkers from raw geometry. No general two-run or target-wide classification is claimed.

## Exact finite-domain verification

[Native-slot checker](verify_two_run_catalog_slot_independent.py) independently enumerates all81 ordered tuples in{90,120,150}^4 and computes p from the two three-vector chain lengths. It identifies15p=q exclusions; neither periodicity nor genuine convexity of B is asserted there. One excluded tuple gives redundant180-degree corners, so it must not be quietly counted as a valid hexagon case. Every other reconstructed pair is strictly convex by all native supporting-edge tests.

For each of the66 modeled cases, the checker directly builds ray-compatible oriented corner cycles by a least-index-first DFS, independently of the producer's multiset/permutation/mirror expansion. All native slots, reflection signs and reference endpoints remain separate. Every legal triple is included, including homogeneous ppp/qqq cases. Exact angle-unit product1 is equivalent to angle sum360 because three strict convex angles sum between0 and540. The full cycle sets, native corner vectors, all seam keys and every signed feature vector match the retained certificate.

All54 rational duals are independently verified on every star and both species. The same checker verifies every12 retained nonnegative primal, with free nonnegative species frequencies normalized only by their sum; no equal-frequency or compulsory-use assumption is inserted. These primals are merely necessary local data.

## Infinite rejection proof

The dual consequence is valid for unrestricted original tilings specifically through the independently reviewed defect-free two-hexagon limit theorem. Any hypothetical tiling produces an admitted edge-to-edge trivalent limit by these same shapes. The species may disappear, since both per-tile dual charges are at most−1.

At every complete native star the corner plus signed seam potential is nonnegative. At opposite ends of a seam both endpoint flags toggle, so its canonical smaller-slot sign reverses and cancels. The same-native-slot opposite-endpoint ambiguous case is assigned zero, a safe weakening; no arbitrary occurrence order is used. Selecting tiles intersecting a large square leaves only O(R) incomplete stars and unpaired seam ends, by fixed diameters/minimum area and disjoint interiors. Each native tile has bounded6-corner/6-side incidence and the finite rational weights are bounded. Thus the total native corner charge is at least−O(R), while each selected tile contributes at most−1. Their count is at least a positive constant timesR^2 by coverage and maximum area. Contradiction. This proves unrestricted untileability for each of the54, without assumed frequencies or positive lower density of either species.

## All12 actual periodic outcomes

[Positive-target checker](verify_two_run_catalog_periodic_independent.py) independently reconstructs every target polygon and every native reflected boundary. It verifies the stated source-to-target dihedral native vertex congruences with a common positive scale for both species. More decisively, it verifies the raw target quotients directly: all sides are used once, matched lengths agree, the face graph is connected, and every actual successor-permutation link is one three-corner circle of angle360. There are eight4-face quotients and four8-face quotients. Euler characteristic is0 and orientation-preserving boundary gluings make each a compact flat torus. Its complete Euclidean universal cover is therefore an admitted periodic plane tiling. The positive result does not depend on assuming the third curve's symbolic extension or treating a frequency primal as a tiling.

The retained certificate tuples partition all66 distinct-length cases into54 duals and12 raw flat quotients. No negative conclusion comes from failed assembly, a solver deadline or an incomplete search. The15equal-length tuples are strictly outside this finite theorem. In the original52 angle-frequency survivors,40 are newly rejected and12 periodic.

Both independent replays completed PASS:

    conda run --no-capture-output -n arisearch python research/reviews/verify_two_run_catalog_slot_independent.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_two_run_catalog_periodic_independent.py

The original two-convex-polygon target remains unresolved; arbitrary homogeneous angles and metrics are outside this domain.
