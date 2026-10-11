#!/usr/bin/env python3
"""Independent endpoint and vertex-link audit; does not import author code."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "research/certificates/hexagon-five-length-private-repeat-tori.json"
WORDS = {"A": (0, 1, 0, 2, 3, 4), "B": (5, 3, 5, 2, 1, 4)}


def stars(x, y):
    return [(("A", x), ("A", 2), ("B", 3)),
            (("A", 1-x), ("A", 5), ("B", 4)),
            (("A", 3), ("B", y), ("B", 2)),
            (("A", 4), ("B", 1-y), ("B", 5))]


def expected_neighbor(n, i, x, y):
    if i in (0, 2):
        z = x if n == "A" else y
        return n, i if z else 2-i, bool(z)
    if n == "A":
        return {1: ("B", 4, bool(x)), 3: ("B", 3, True),
                4: ("B", 1, bool(y)), 5: ("B", 5, True)}[i]
    return {1: ("A", 4, bool(y)), 3: ("A", 3, True),
            4: ("A", 1, bool(x)), 5: ("A", 5, True)}[i]


def endpoint_check():
    count = survivors = 0
    for x, y in product((0, 1), repeat=2):
        allowed_pairs = {tuple(sorted(pair)) for star in stars(x, y)
                         for pair in combinations(star, 2)}
        for n, word in WORDS.items():
            for i, length in enumerate(word):
                actual = []
                for m, other in WORDS.items():
                    for j, other_length in enumerate(other):
                        if other_length != length:
                            continue
                        for swap in (False, True):
                            count += 1
                            target = ((j-1) % 6, j)
                            if swap:
                                target = target[::-1]
                            source = ((i-1) % 6, i)
                            if all(tuple(sorted(((n, p), (m, q)))) in allowed_pairs
                                   for p, q in zip(source, target)):
                                actual.append((m, j, swap))
                assert actual == [expected_neighbor(n, i, x, y)], (x, y, n, i, actual)
                survivors += len(actual)
    assert (count, survivors) == (192, 48)


def torus_check(certificate):
    assert certificate["A"] == list(WORDS["A"])
    assert certificate["B"] == list(WORDS["B"])
    assert len(certificate["models"]) == 2
    assert sorted(m["choice"] for m in certificate["models"]) == [0, 1]
    domain = {(f, i) for f in range(4) for i in range(6)}
    for model in certificate["models"]:
        z = model["choice"]
        flags = model["reflected"]
        assert flags == ([False]*4 if z else [False, True, False, True])
        words = [WORDS["A" if f < 2 else "B"][::(-1 if flags[f] else 1)]
                 for f in range(4)]
        twin = {}
        face_adj = {f: set() for f in range(4)}
        for left, right in model["pairs"]:
            f, i = left
            g, j = right
            assert f != g and 0 <= i < 6 and 0 <= j < 6
            assert words[f][i] == words[g][j]
            assert (f, i) not in twin and (g, j) not in twin
            twin[f, i] = (g, j)
            twin[g, j] = (f, i)
            face_adj[f].add(g)
            face_adj[g].add(f)
        assert set(twin) == domain and len(model["pairs"]) == 12
        # Walk around each vertex: cross its incoming edge, whose reversed
        # gluing endpoint lands at the predecessor corner of the paired edge.
        successor = {(f, i): (twin[f, i][0], (twin[f, i][1]-1) % 6)
                     for f, i in domain}
        assert set(successor.values()) == domain
        remaining = set(domain)
        actual_stars = []
        while remaining:
            start = min(remaining)
            cycle = [start]
            p = successor[start]
            while p != start:
                assert p not in cycle
                cycle.append(p)
                p = successor[p]
            assert len(cycle) == 3
            remaining.difference_update(cycle)
            actual_stars.append(tuple(sorted(
                ("A" if f < 2 else "B", (4-i) % 6 if flags[f] else i)
                for f, i in cycle)))
        assert Counter(actual_stars) == Counter({tuple(sorted(t)): 2 for t in stars(z, z)})
        seen = {0}
        frontier = [0]
        while frontier:
            f = frontier.pop()
            for g in face_adj[f] - seen:
                seen.add(g)
                frontier.append(g)
        assert len(seen) == 4 and len(actual_stars) - 12 + 4 == 0


if __name__ == "__main__":
    endpoint_check()
    torus_check(json.loads(CERT.read_text()))
    print("PASS independent audit: 192 endpoint candidates, 48 unique prescribed maps; "
          "both quotients have eight circular three-corner links, connected faces, "
          "reversed edge orientations and chi=0.")
    print("certificate SHA-256:", hashlib.sha256(CERT.read_bytes()).hexdigest())
