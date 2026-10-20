"""Independent exact angle audit of the radial 7P+H eight-child topology.

Derive cyclic vertex words from neighbor rotations, rather than copying the
search script's vertex table. Use disjunctions of native angle words, rather
than phase-indexed If expressions. No side lengths are assumed.
"""
import itertools
import json
import z3

alpha, beta = z3.Reals("audit_alpha audit_beta")
pentagon = (z3.RealVal(120), alpha, beta, 240-beta, 180-alpha)
hexagon = (beta, 240-beta) * 3

# -1 denotes the exterior parent face. These are directed neighbor rotations
# of the unique (up to dihedral symmetry) 6-rim, 2-inner triangulation.
rotation = {
    0: (-1, 1, 6, 7, 5),
    1: (-1, 2, 6, 0),
    2: (-1, 3, 6, 1),
    3: (-1, 4, 7, 6, 2),
    4: (-1, 5, 7, 3),
    5: (-1, 0, 7, 4),
    6: (0, 1, 2, 3, 7),
    7: (0, 6, 3, 4, 5),
}


def node(tile, a, b):
    if a == -1 or b == -1:
        other = b if a == -1 else a
        assert tile < 6 and other < 6
        # The boundary endpoint between successive rim children.
        return ("boundary", min(tile, other) if abs(tile-other) == 1 else 5)
    tri = tuple(sorted((tile, a, b)))
    return ("interior", tri)


def vertices(tile):
    neighbors = rotation[tile]
    return [node(tile, neighbors[i-1], neighbors[i]) for i in range(len(neighbors))]


def rotations_and_reflections(word):
    n = len(word)
    return [tuple(word[(offset + sign*j) % n] for j in range(n))
            for sign in (1, -1) for offset in range(n)]


def solve_case(h_tile, parent_corner_counts, enforce_parent=True,
               drop_node=None, junction_type=None):
    s = z3.Solver()
    s.set(timeout=300000)
    s.add(alpha > 0, alpha < 180, beta > 60, beta < 180)

    # Start each outer child at its preceding boundary junction and insert
    # parent corners along the one exterior arc, in boundary order.
    words = {}
    for tile in range(8):
        row = vertices(tile)
        if tile < 6:
            start = row.index(("boundary", 5 if tile == 0 else tile-1))
            row = row[start:] + row[:start]
            row[1:1] = [("corner", tile, k)
                        for k in range(parent_corner_counts[tile])]
        words[tile] = row
        assert len(row) == (6 if tile == h_tile else 5), (tile, row)

    angle_at = {}
    for tile, row in words.items():
        native = hexagon if tile == h_tile else pentagon
        slots = z3.Reals(" ".join(f"a_{h_tile}_{tile}_{j}" for j in range(len(row))))
        for key, slot in zip(row, slots):
            assert (tile, key) not in angle_at
            angle_at[tile, key] = slot
        choices = rotations_and_reflections(native)
        s.add(z3.Or(*[z3.And(*[slots[j] == word[j] for j in range(len(row))])
                      for word in choices]))

    all_nodes = {v for row in words.values() for v in row}
    corners = [v for tile in range(6) for v in words[tile]
               if v[0] == "corner"]
    assert len(corners) == 5 and len(set(corners)) == 5
    internal = [v for v in all_nodes if v[0] == "interior"]
    boundary = [v for v in all_nodes if v[0] == "boundary"]
    assert len(internal) == 8 and len(boundary) == 6
    for v in internal + boundary:
        incident = [slot for (tile, key), slot in angle_at.items() if key == v]
        assert len(incident) == (3 if v[0] == "interior" else 2), (v, incident)
        if v != drop_node and (junction_type is None or v[0] == junction_type):
            s.add(z3.Sum(*incident) == (360 if v[0] == "interior" else 180))

    # Parent corners are a coherent cyclic native P word, with every possible
    # starting vertex and either orientation. The corner order follows the rim.
    cvals = [angle_at[tile, key] for key in corners for tile in range(6)
             if (tile, key) in angle_at]
    assert len(cvals) == 5
    if enforce_parent:
        s.add(z3.Or(*[z3.And(*[cvals[j] == word[j] for j in range(5)])
                      for word in rotations_and_reflections(pentagon)]))
    result = s.check()
    return {
        "h_tile": h_tile,
        "result": str(result),
        "parent_constraint": enforce_parent,
        "dropped_node": str(drop_node),
        "junction_type": junction_type,
        "assertions": len(s.assertions()),
        "interior_nodes": len(internal),
        "boundary_nodes": len(boundary),
        "corner_nodes": len(corners),
        "words": {str(k): [str(v) for v in row] for k, row in words.items()},
    }


if __name__ == "__main__":
    results = [solve_case(0, (1, 1, 1, 0, 1, 1)),
               solve_case(1, (0, 2, 1, 0, 1, 1))]
    print(json.dumps(results, indent=2))
    assert all(r["result"] == "unsat" for r in results)
