#!/usr/bin/env python3
"""Fresh independent Rao-family application check, without polyhedra.

Source: arXiv:1708.00274v1 Table 2 (printed page 14), types 1--15.
The imported complete monohedral classification itself is not replayed.
Angle conditions are independently entered as named scalar expressions;
side reflection maps are reconstructed from unordered edge endpoints.
Strictly positive rowspace certificates refute every empty metric case.
Two nonnegative rowspace certificates handle degenerate V Type 2 cases.
An analytic objective bound verifies both retained exact optima.
"""
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar, QuadraticField, matrix, vector


def require(condition, message):
    if not condition:
        raise ValueError(message)


def angle_gate(kind, angles):
    a, b, c, d, e = angles
    tests = {
        1: (a+b+c == 10,),
        2: (a+b+d == 10,),
        3: (3*e == 10, d+2*e == 10, b+2*e == 10),
        4: (a+b+d == 10, 2*e == 5),
        5: (3*e == 10, a+b+d == 10),
        6: (d+2*e == 10, a+c+d == 10),
        7: (d+2*e == 10, a+2*c == 10),
        8: (d+2*e == 10, 2*b+c == 10),
        9: (d+2*e == 10, 2*a+c == 10),
        10: (2*c+d == 10, b+c+e == 10, a+2*b == 10),
        11: (c+2*d == 10, b+d+e == 10, a+2*b == 10),
        12: (c+2*d == 10, b+d+e == 10, a+2*b == 10),
        13: (b+2*d == 10, a+b+d == 10, 2*e == 5),
        14: (c+2*d == 10, b+d+e == 10, a+2*b == 10),
        15: (c+2*d == 10, 2*b+e == 10, 2*a+d == 10, 2*e == 5),
    }
    return all(tests[kind])


LENGTH_GATES = {
    1: (),
    2: (("C", "E"),),
    3: (("C+E", "D"), ("A", "B")),
    4: (("D", "E"), ("B", "C")),
    5: (("D", "E"), ("B", "C")),
    6: (("C", "D"), ("D", "E"), ("A", "B")),
    7: (("A", "C"), ("C", "D"), ("D", "E")),
    8: (("A", "B"), ("B", "C"), ("C", "D")),
    9: (("A", "B"), ("B", "C"), ("C", "D")),
    10: (("A+C", "D"), ("D", "E")),
    11: (("A", "B"), ("B", "C+2E")),
    12: (("A+C", "B"), ("B", "2E")),
    13: (("A", "2B"), ("B", "C")),
    14: (("A", "B"), ("B", "2C"), ("C", "E")),
    15: (("B", "D"), ("D", "E"), ("C", "2B")),
}


def transformed_length_rows(kind, sides):
    result = []
    for left, right in LENGTH_GATES[kind]:
        row = [0]*5
        for expression, sign in ((left, 1), (right, -1)):
            for term in expression.split("+"):
                coefficient = int(term[:-1]) if len(term) > 1 else 1
                row[sides[ord(term[-1])-ord("A")]] += sign*coefficient
        result.append(row)
    return result


root = Path(__file__).resolve().parents[2]
cert = json.loads((root / "research/certificates/pentagrid-monohedral-family-filter.json").read_text())
K = QuadraticField(5, "r", embedding=AA(5).sqrt())
r = K.gen()
phi = (1+r)/2
words = {"U": (1, 3, 4, 4, 3), "V": (2, 2, 4, 3, 4), "W": (3, 3, 3, 3, 3)}
require(cert["domain"] == {
    "angle_words": {name: list(word) for name, word in words.items()},
    "type_count": 15, "dihedral_maps_per_type": 10, "raw_angle_tests": 450}, "domain")

# Independent outgoing-side recovery from the actual two old endpoints.
old_edges = {frozenset((j, (j+1) % 5)): j for j in range(5)}
expected = {}
for name, word in words.items():
    for kind in range(1, 16):
        for orientation in (1, -1):
            for start in range(5):
                vertices = tuple((start+orientation*j) % 5 for j in range(5))
                new_angles = tuple(word[j] for j in vertices)
                if not angle_gate(kind, new_angles):
                    continue
                sides = tuple(old_edges[frozenset((vertices[j], vertices[(j+1) % 5]))]
                              for j in range(5))
                expected[name, kind, orientation, start] = (
                    new_angles, sides, transformed_length_rows(kind, sides))
require(len(expected) == 16, "compatible case count")
records = cert["compatible_angle_cases"]
require(len(records) == 16, "certificate case count")
keys = [(row["word"], row["type"], row["sign"], row["offset"]) for row in records]
require(len(set(keys)) == 16 and set(keys) == set(expected), "case completeness")

# These closure identities follow independently by exact trig evaluation.
closure_rows = {
    "U": [[1, -1, -phi, -phi, 0], [0, -phi, -phi, -1, 1]],
    "V": [[1, -phi, -phi, 0, 1], [0, -phi, -1, 1, phi]],
}
zeta = QQbar.zeta(10)
for name in ("U", "V"):
    word = words[name]
    directions = [sum(5-word[j] for j in range(1, i+1)) % 10 for i in range(5)]
    cx = [(zeta**d).real() for d in directions]
    sy = [(zeta**d).imag()/zeta.imag() for d in directions]
    require(matrix(AA, closure_rows[name]).rank() == 2, "closure rank")
    require(matrix(AA, closure_rows[name]+[cx, sy]).rank() == 2, "exact trig/closure equivalence")

# Coefficients of a strictly positive vector in each empty-case rowspace.
# RREF is computed from our independently simplified closure identities.
strict_weights = {
    ("U", 2, 1, 1): (1, 2, 4),
    ("U", 2, 1, 3): (1, 4, 1),
    ("U", 2, -1, 2): (1, 8, 1),
    ("U", 2, -1, 4): (1, 1, 4),
}
positive_keys = {("V", 2, 1, 4), ("V", 2, -1, 2)}
degenerate_keys = {("V", 2, 1, 1): 2, ("V", 2, -1, 0): 1}


def decode(value):
    require(isinstance(value, list) and len(value) == 2, "field encoding")
    return QQ(value[0])+QQ(value[1])*r


for row, key in zip(records, keys):
    angles, sides, length_rows = expected[key]
    require(row["angle_word"] == list(angles), "angle relabeling")
    require(row["side_map"] == list(sides), "endpoint-derived side relabeling")
    require(row["length_equations"] == length_rows, "length equations")
    name, kind, orientation, start = key
    M = matrix(K, closure_rows[name]+length_rows)
    R = M.echelon_form()
    require(bool(row["positive_closed_metric"]) == (key in positive_keys), "positivity flag")
    if key not in positive_keys and key not in degenerate_keys:
        if key in strict_weights:
            weights = strict_weights[key]
            require(R.nrows() == len(weights), "strict certificate shape")
        else:
            require(M.rank() == 5 and R == matrix.identity(K, 5), "full rank empty case")
            weights = (1,)*5
        obstruction = vector(K, weights)*R
        require(all(x > 0 for x in obstruction), "strict positive rowspace obstruction")
        # Thus obstruction dot l=0 forces l=0 for l>=0, contradicting sum l=1.
        require(row["max_minimum_side"] is None and row["maximizing_normalized_lengths"] is None,
                "empty polyhedron fields")
        continue
    optimum = decode(row["max_minimum_side"])
    witness = vector(K, [decode(x) for x in row["maximizing_normalized_lengths"]])
    require(sum(witness) == 1 and M*witness == 0, "normalized closure witness")
    require(optimum >= 0 and all(x >= optimum for x in witness), "witness minimum")
    if key in degenerate_keys:
        obstruction = R.row(degenerate_keys[key])
        require(any(x > 0 for x in obstruction) and all(x >= 0 for x in obstruction),
                "nonnegative rowspace obstruction")
        require(optimum == 0, "degenerate optimum")
        continue
    # Each positive gate implies l0 is a positive combination of two
    # other lengths, with coefficient sum sqrt(5). Hence l0>=sqrt(5)*delta
    # and 1=sum(l)>=(4+sqrt(5))*delta. No polyhedron optimizer is used.
    relation = (vector(K, [1, -2*(phi-1), -1, 0, 0])
                if orientation == 1 else vector(K, [1, 0, -2*(phi-1), -1, 0]))
    require(M.stack(matrix(K, [relation])).rank() == M.rank(), "analytic optimum relation")
    require(2*(phi-1)+1 == r, "bound coefficient sum")
    require(optimum == 1/(4+r) == (4-r)/11, "sharp optimum")
    require(all(x > 0 for x in witness), "strict positive witness")
    # Certify actual global convexity of the explicit positive witness.
    directions = [sum(5-words[name][j] for j in range(1, i+1)) % 10 for i in range(5)]
    edge_vectors = [AA(witness[i])*(zeta**directions[i]) for i in range(5)]
    vertices = [QQbar(0)]
    for edge in edge_vectors:
        vertices.append(vertices[-1]+edge)
    require(vertices[-1] == 0, "explicit coordinate closure")
    for i in range(5):
        for j in range(5):
            if j not in (i, (i+1) % 5):
                cross = ((vertices[j]-vertices[i])/edge_vectors[i]).imag()
                require(cross > 0, "strict supporting-side convexity")

require(cert["positive_case_count"] == len(positive_keys) == 2, "positive total")
print("PASS: all 450 source-family angle gates; 16 compatible cases; "
      "12 strict rowspace obstructions, two degenerate obstructions, "
      "two exact positive optima and convex coordinate witnesses.")
