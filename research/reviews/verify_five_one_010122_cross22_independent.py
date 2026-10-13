#!/usr/bin/env python3
"""Independent actual-AA22 audit: rebuild rays, graph partitions, H1/H2.
No producer import. Finite domain: 3 partner edges, 2 endpoint bijections,
4 oriented third-corner choices at each end; every set partition of 6 sides.
"""
from itertools import permutations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
C = (0, 1, 0, 1, 2, 2)
ANGLE = ((1, 0), (-5, 720), (4, -360))

def components(edges):
    adjacency = [set() for _ in range(6)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen, blocks = set(range(6)), []
    while unseen:
        todo, block = [min(unseen)], set()
        while todo:
            v = todo.pop()
            if v in block:
                continue
            block.add(v)
            todo.extend(adjacency[v] - block)
        unseen -= block
        blocks.append(frozenset(block))
    return frozenset(blocks)

def encoded(blocks):
    ordered = sorted(blocks, key=min)
    return tuple(next(k for k, b in enumerate(ordered) if i in b) for i in range(6))

def same(blocks, a, b):
    return any(a in block and b in block for block in blocks)

def coarsens(big, small):
    return all(any(block <= container for container in big) for block in small)

def all_partitions(n):
    if n == 0:
        yield ()
        return
    for prior in all_partitions(n - 1):
        yield prior + (frozenset({n - 1}),)
        for k in range(len(prior)):
            yield prior[:k] + (prior[k] | {n - 1},) + prior[k + 1:]

# A relabelling is an ordered sequence of native corner IDs. Its side maps
# are reconstructed by endpoint incidence, not a signed index formula.
NATIVE_EDGES = [frozenset((i, (i + 1) % 6)) for i in range(6)]

def hits(blocks):
    answer = set()
    for start, direction in product(range(6), (1, -1)):
        corners = [(start + direction * i) % 6 for i in range(6)]
        sides = [NATIVE_EDGES.index(frozenset((corners[i], corners[(i + 1) % 6]))) for i in range(6)]
        def total(indices):
            return tuple(sum(ANGLE[C[corners[k]]][j] for k in indices) for j in range(2))
        if total((0, 1, 2)) == (0, 360) and same(blocks, sides[2], sides[5]):
            answer.add(('H1', start, direction))
        if total((0, 1, 3)) == (0, 360) and same(blocks, sides[1], sides[3]) and same(blocks, sides[2], sides[5]):
            answer.add(('H2', start, direction))
    return answer

def arms(c):
    return {(c - 1) % 6, c}

# Build the two endpoints as three incident sectors and three matching rays.
cases = {}
for partner in range(6):
    ends = tuple(NATIVE_EDGES[partner])
    if any(C[v] == 2 for v in ends):
        continue
    for partner_vertices in permutations(ends):
        offers = []
        for v in partner_vertices:
            missing = ({0, 1, 2} - {2, C[v]}).pop()
            offers.append([(c, order) for c in range(6) if C[c] == missing
                           for order in permutations(sorted(arms(c)))])
        for first, second in product(*offers):
            equalities = [(4, partner)]
            signed = []
            for central, neighbour, (third, order) in zip((4, 5), partner_vertices, (first, second)):
                exposed_a = (arms(central) - {4}).pop()
                exposed_b = (arms(neighbour) - {partner}).pop()
                equalities.extend(((order[0], exposed_a), (order[1], exposed_b)))
                forward = ((third - 1) % 6, third)
                signed.append((third, 1 if order == forward else -1))
            key = (partner, partner_vertices != (partner, partner + 1), tuple(signed))
            blocks = components(equalities)
            assert key not in cases
            cases[key] = blocks
            assert hits(blocks), (key, encoded(blocks))
assert len(cases) == 96
requirements = set(cases.values())
minimal = {p for p in requirements if not any(q != p and coarsens(p, q) for q in requirements)}
assert len(requirements) == 36
assert sorted(encoded(p) for p in minimal) == [(0, 1, 2, 0, 2, 3), (0, 1, 2, 3, 0, 2), (0, 1, 2, 3, 1, 4)]
all_actual = {frozenset(p) for p in all_partitions(6)}
assert len(all_actual) == 203
retained = {p for p in all_actual if any(coarsens(p, q) for q in requirements)}
assert len(retained) == 71 and all(hits(p) for p in retained)

# Check the retained author artifact against independent rows and witnesses.
certificate = json.loads((ROOT / 'research/certificates/terra-five-one-010122-cross-22-gate.json').read_text())
assert tuple(certificate['native_A_word']) == C
assert len(certificate['cross_cases']) == len(cases)
seen = set()
for row in certificate['cross_cases']:
    key = (row['partner_side'], row['partner_endpoints_reversed'], tuple(map(tuple, row['third_A_corner_and_arm_signs'])))
    assert key in cases and key not in seen
    seen.add(key)
    blocks = cases[key]
    assert tuple(row['required_partition']) == encoded(blocks)
    assert components(row['equalities']) == blocks
    assert set(map(tuple, row['monohedral_hits'])) == hits(blocks)
assert seen == set(cases)
assert {tuple(p) for p in certificate['required_partitions']} == {encoded(p) for p in requirements}
assert {tuple(p) for p in certificate['minimal_required_partitions']} == {encoded(p) for p in minimal}
assert {tuple(row['partition']) for row in certificate['actual_partitions']} == {encoded(p) for p in retained}
for row in certificate['actual_partitions']:
    p = next(p for p in retained if encoded(p) == tuple(row['partition']))
    expected_ids = {i for i, c in enumerate(certificate['cross_cases'])
                    if coarsens(p, components(c['equalities']))}
    assert set(row['crosscase_ids']) == expected_ids
    assert set(map(tuple, row['monohedral_hits'])) == hits(p)

# Independently audit the optional complete AAA cycles, including reflections.
expected_aaa = {}
for vertices in product((0, 2), (1, 3), (4, 5)):
    for orders in product(*(tuple(permutations(sorted(arms(c)))) for c in vertices)):
        signs = tuple(1 if order == ((c - 1) % 6, c) else -1 for c, order in zip(vertices, orders))
        edges = [(orders[k][1], orders[(k + 1) % 3][0]) for k in range(3)]
        expected_aaa[(vertices, signs)] = components(edges)
assert len(expected_aaa) == 64 and len(certificate['AAA_native_cycles']) == 64
seen_aaa = set()
for row in certificate['AAA_native_cycles']:
    key = (tuple(row['corners']), tuple(row['arm_signs']))
    assert key not in seen_aaa and key in expected_aaa
    seen_aaa.add(key)
    assert tuple(row['required_partition']) == encoded(expected_aaa[key])
    assert components(row['equalities']) == expected_aaa[key]
for row in certificate['cross_cases']:
    for ids in row['endpoint_AAA_star_ids']:
        assert ids
        for idx in ids:
            assert coarsens(components(row['equalities']), components(certificate['AAA_native_cycles'][idx]['equalities']))
print('PASS independent A010122: 96 ray patterns, 36 requirements, 3 minimal ancestors, 203 partitions, 71 compatible, all H1/H2; complete retained certificate checked')
