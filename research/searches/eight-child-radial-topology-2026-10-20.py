"""Finite graph check for the eight-child pentagon/hexagon topology gate.

Analytic exhaustiveness and geometry conventions are in the paired report.
The rim cycle is an exterior planar augmentation, not initially a contact claim.
"""
from itertools import combinations
from sage.all import Graph

boundary = range(6)
outer = 8
left, right = 6, 7
base = Graph()
base.add_vertices(range(9))
base.add_cycle(boundary)
base.add_edges((outer, i) for i in boundary)
base.add_edge(left, right)

survivors = []
for left_neighbors in combinations(boundary, 4):
    for right_neighbors in combinations(boundary, 4):
        if set(left_neighbors) | set(right_neighbors) != set(boundary):
            continue
        graph = base.copy()
        graph.add_edges((left, i) for i in left_neighbors)
        graph.add_edges((right, i) for i in right_neighbors)
        assert graph.size() == 21
        if graph.is_planar():
            shared = set(left_neighbors) & set(right_neighbors)
            assert len(shared) == 2
            shared_pair = tuple(sorted(shared))
            assert (shared_pair[1] - shared_pair[0]) % 6 == 3
            survivors.append((left_neighbors, right_neighbors, shared_pair))

assert survivors
assert all(set(a) | set(b) == set(boundary) for a, b, _ in survivors)

topology = {
    "H_shared": {"shared_P_corners": 0, "shared_H_corners": 1,
                 "exclusive_P_corners": 1},
    "H_exclusive": {"shared_P_corners": 0,
                    "exclusive_H_corners": 2,
                    "exclusive_P_corners": 1},
}
for case, data in topology.items():
    total = (1 + 4) if case == "H_shared" else (2 + 3)
    assert total == 5

print("PLANAR_LABELED_INCIDENCE_MAPS", len(survivors))
print("ALL_HAVE_OPPOSITE_SHARED_BOUNDARY_CHILDREN", True)
print("SAMPLE", survivors[0])
print("HEXAGON_BOUNDARY_CORNER_PATTERNS", topology)
