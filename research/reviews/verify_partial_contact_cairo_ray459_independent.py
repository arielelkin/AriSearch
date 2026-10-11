"""Independent exact original-native, placement and coverage certificate audit.

No producer or seam-balance module is imported. The raw gluing and developed
placement certificates are treated as untrusted input. Common scale is fixed
to one; every coordinate scales linearly, proving the whole positive ray.
"""
from collections import Counter
from pathlib import Path
import json
from sage.all import QuadraticField, matrix, vector, ZZ, QQ, identity_matrix

ROOT = Path(__file__).resolve().parents[2]
K = QuadraticField(3, "w")
w = K.gen()


def load(name):
    return json.loads((ROOT / "research/certificates" / name).read_text())


def scalar(text):
    # Development expressions are polynomials in a common scale x. Work in
    # Q(sqrt(3))[x,y,z], then substitute x=1,y=z=0, checking homogeneity.
    from sage.all import PolynomialRing
    ring = PolynomialRing(K, names=("x", "y", "z"))
    p = ring(text)
    assert p == p.monomial_coefficient(ring.gen(0))*ring.gen(0) or p == 0
    return K(p(1, 0, 0))


def point(texts):
    return vector(K, [scalar(t) for t in texts])


def cross(a, b):
    return matrix(K, [a, b]).det()


def native(word):
    a, b, c, d, e = word
    assert all(t > 0 for t in word)
    assert b - c == w*(d-a) and e == w*c+d-2*a
    p = [vector(K, t) for t in ((0, 0), (a, 0), (a, b),
         (a-w*c/2, b+c/2), (-e/2, w*e/2))]
    edges = [p[(i+1) % 5]-p[i] for i in range(5)]
    assert [v.dot_product(v) for v in edges] == [t*t for t in word]
    # All nonincident vertices lie strictly to the left of every native edge.
    assert all(cross(edges[i], p[j]-p[i]) > 0
               for i in range(5) for j in range(5)
               if j not in (i, (i+1) % 5))
    area = sum(cross(p[i], p[(i+1) % 5]) for i in range(5))/2
    assert area > 0
    return p, area


P = tuple(map(K, ("1", "(6*w+13)/61", "(81*w+23)/122",
                   "(w+53)/122", "(12*w+26)/61")))
Q = tuple(map(K, ("(40-5*w)/61", "1", "(81*w+23)/122",
                   "(23*w-1)/122", "(33*w+41)/61")))
native_points, areas = zip(*(native(z) for z in (P, Q)))
raw = load("partial-contact-cairo-mixed-quotient-orbit7-flat459-eight-faces.json")
cert = load("partial-contact-cairo-mixed-quotient-orbit7-flat459-development.json")
assert (raw["source_pattern"], raw["source_flat_id"]) == ("orbit7", 459)
assert [K(t[0]) for t in raw["arm_forms"]] == list(P[:4]+Q[:4])
assert [K(t[0]) for t in raw["e_forms"]] == [P[4], Q[4]]
# Independent original flat data, not merely a copied normalized-ray record.
flat_data = load("partial-contact-cairo-remaining-two-cross-event-flats.json")
flat = flat_data["orbit7"]["records"][459]
assert flat["dimension"] == 1 and flat["flat_id"] == 459
original = [tuple(map(K, row)) for row in flat["arm_forms"]+flat["e_forms"]]
assert all(len(row) == 1 for row in original)
assert [row[0]/original[0][0] for row in original] == list(P[:4]+Q[:4]+(P[4], Q[4]))

N = len(raw["angles"])
assert N == 48 and raw["face_count"] == 8
blocks = [[i for i in range(N) if raw["dart_face"][i] == f] for f in range(8)]
assert Counter(raw["variant_native_types"]) == {0: 6, 1: 2}
successor = raw["next_dart"]
local = {int(i): point(p) for i, p in cert["local_atomic_vertices"].items()}
assert set(local) == set(range(N))
h = QQ(1)/2
directions = [vector(K, t) for t in ((1, 0), (w/2, h), (h, w/2),
    (0, 1), (-h, w/2), (-w/2, h), (-1, 0), (-w/2, -h),
    (-h, -w/2), (0, -1), (h, -w/2), (w/2, -h))]
native_directions = (0, 3, 5, 8, 10)
for fid, block in enumerate(blocks):
    assert [successor[i] for i in block] == block[1:]+block[:1]
    species = raw["variant_native_types"][fid]
    vertices = [i for i in block if raw["angles"][i] != 180]
    assert [raw["angles"][i] for i in vertices] == [120, 90, 120, 90, 120]
    assert [local[i] for i in vertices] == list(native_points[species])
    for side, start in enumerate(vertices):
        end = vertices[(side+1) % 5]
        atom = start
        seen = []
        while atom != end or not seen:
            seen.append(atom)
            length = K(raw["edge_colors"][atom][1][0])
            assert length > 0
            assert raw["native_direction_labels"][atom] == native_directions[side]
            assert local[successor[atom]]-local[atom] == length*directions[native_directions[side]]
            atom = successor[atom]
            if atom == end:
                break
            assert len(seen) < N
        assert sum(K(raw["edge_colors"][i][1][0]) for i in seen) == (P, Q)[species][side]

# Reconstruct vertex identifications using endpoint flags. Each corner is an
# interval between its incoming/outgoing flags; gluing must give circular links.
partners = {}
flag_partner = {}
for i, j, same in raw["edge_pairs"]:
    assert i != j and i not in partners and j not in partners
    assert raw["edge_colors"][i] == raw["edge_colors"][j]
    partners[i] = (j, same)
    partners[j] = (i, same)
    ends_i, ends_j = ((i, 1), (successor[i], 0)), ((j, 1), (successor[j], 0))
    for a, b in zip(ends_i, ends_j if same else ends_j[::-1]):
        assert a not in flag_partner and b not in flag_partner
        flag_partner[a], flag_partner[b] = b, a
assert set(partners) == set(range(N)) and len(flag_partner) == 2*N
links, unused = [], set(range(N))
while unused:
    start = (min(unused), 0)
    at, route, flags = start, [], set()
    while at not in flags:
        assert at[0] in unused
        unused.remove(at[0])
        route.append(at[0])
        flags.add(at)
        at = flag_partner[(at[0], 1-at[1])]
    assert at == start and sum(raw["angles"][i] for i in route) == 360
    assert sorted(raw["angles"][i] for i in route) in ([120, 120, 120], [90, 90, 180])
    links.append(frozenset(route))
assert len(links) == 16
assert set(links) == {frozenset(r) for r in cert["vertex_links"]}

# Audit the supplied placement, rather than running the author's development.
states = [tuple(t) for t in cert["lift_states"]]
assert len(states) == len(set(states)) == 16
assert Counter(raw["variant_native_types"][s[0]] for s in states) == {0: 12, 1: 4}
origins = dict(zip(states, map(point, cert["positions"])))
frames = {}
for state in states:
    f, theta, sign = state
    assert sign in (-1, 1) and 0 <= theta < 12
    u = directions[theta]
    F = matrix(K, [[u[0], -sign*u[1]], [u[1], sign*u[0]]])
    assert F.transpose()*F == identity_matrix(K, 2) and F.det() == sign
    frames[state] = F
periods = [point(p) for p in cert["periods"]]
assert periods == [vector(K, [-(39*w+54)/61]*2),
                   vector(K, [-(59*w+138)/61, (59*w+138)/61])]
B = matrix(K, periods)
assert B.det() < 0
total_area = 12*areas[0]+4*areas[1]
assert total_area == -B.det() == (17136*w+28710)/3721

transitions = {}
shift_coordinates = []
for tr in cert["transitions"]:
    a, b = tuple(tr["state"]), tuple(tr["target"])
    i, j = tr["dart"], tr["target_dart"]
    assert a in frames and b in frames and i in blocks[a[0]] and j in blocks[b[0]]
    assert (a, i) not in transitions
    assert partners[i][0] == j
    _, same = partners[i]
    shift = point(tr["shift"])
    integers = vector(ZZ, tr["period_coordinates"])
    assert shift == integers*B
    shift_coordinates.append(integers)
    A = [origins[a]+frames[a]*local[k] for k in (i, successor[i])]
    C = [origins[b]+shift+frames[b]*local[k] for k in (j, successor[j])]
    assert A == (C if same else C[::-1])
    assert a[2]*(A[1]-A[0]) == -b[2]*(C[1]-C[0])
    transitions[a, i] = (b, j, tuple(integers))
assert len(transitions) == 96
for (a, i), (b, j, shift) in transitions.items():
    assert transitions[b, j] == (a, i, tuple(-v for v in shift))
visited, queue = {states[0]}, [states[0]]
for a in queue:
    for i in blocks[a[0]]:
        b = transitions[a, i][0]
        if b not in visited:
            visited.add(b)
            queue.append(b)
assert visited == set(states)
# The retained periods generate the full translation holonomy: integer
# coordinates are exhaustive and contain the two signed unit vectors.
coords = {tuple(v) for v in shift_coordinates}
assert any((s, 0) in coords for s in (-1, 1))
assert any((0, s) in coords for s in (-1, 1))

print("PASS ray459: exact native ray, 30 strict supports, all positive cuts, "
      "16 circular links, 16 original faces, 96 endpoints/48 inverse seams, "
      "primitive rank-two periods, area/covolume; whole positive scaling ray")
