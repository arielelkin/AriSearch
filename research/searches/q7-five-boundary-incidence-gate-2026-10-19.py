"""Supplementary complete five-vertex outerplanarity check; analytic proof in .md."""
import itertools
import json
import platform
from pathlib import Path
import networkx as nx

pairs = list(itertools.combinations(range(5), 2))
counts = {"graphs": 0, "edge_at_least_8": 0, "outerplanar_edge_at_least_8": 0}
outer_max = 0
for mask in range(1 << len(pairs)):
    edges = [edge for bit, edge in enumerate(pairs) if mask & (1 << bit)]
    cone = nx.Graph()
    cone.add_nodes_from(range(6))
    cone.add_edges_from(edges)
    cone.add_edges_from((5, v) for v in range(5))
    planar, _ = nx.check_planarity(cone)
    counts["graphs"] += 1
    if planar:
        outer_max = max(outer_max, len(edges))
    if len(edges) >= 8:
        counts["edge_at_least_8"] += 1
        counts["outerplanar_edge_at_least_8"] += int(planar)
assert counts == {"graphs": 1024, "edge_at_least_8": 56, "outerplanar_edge_at_least_8": 0}
assert outer_max == 7
result = {"status": "complete", "domain": "all 1024 labeled simple graphs on five vertices", "counts": counts, "maximum_outerplanar_edges": outer_max, "python": platform.python_version(), "networkx": nx.__version__, "topological_counts": {"children": 10, "boundary_children": 5, "interior_children": 5, "seams": 22, "boundary_boundary_edges_lower_bound": 5, "interior_degree_sum_lower_bound": 25, "interior_edges_lower_bound": 8}, "seed": None}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
