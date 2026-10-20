"""Exact comparison of retained complete B atlas with seven literal dihedral orbits."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / "research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json"
retained = ROOT / "research/certificates/hexagon-five-four-all-words-orbits-sol-2026-10-19.json"
data = json.loads(source.read_text())
cert = json.loads(retained.read_text())
rows = {tuple(r["B"]): r for r in data["rows"]}
assert len(data["rows"]) == len(rows) == 180
assert set(rows) == set(itertools.permutations((0, 0, 1, 1, 2, 3)))
full = {w for w, r in rows.items() if set(r["covered_corners"]) == set(range(12))}
expected = [(0,0,1,1,2,3), (0,0,1,2,3,1), (0,0,2,1,1,3),
            (0,1,0,2,1,3), (0,1,2,0,1,3), (0,1,1,0,2,3),
            (0,1,2,0,3,1)]
counts = [(12,2), (10,1), (12,1), (12,1), (16,4), (22,7), (32,100)]
assert [tuple(r["representative"]) for r in cert["orbits"]] == expected
seen = set()
for rep, count, recorded in zip(expected, counts, cert["orbits"]):
    orbit = {v[i:] + v[:i] for v in (rep, rep[::-1]) for i in range(6)}
    assert len(orbit) == 12 and not orbit & seen
    assert orbit <= full
    assert orbit == {tuple(w) for w in recorded["words"]}
    assert {(len(rows[w]["fixed_stars"]), len(rows[w]["boundary_coronas"])) for w in orbit} == {count}
    assert recorded["star_corona_counts"] == [list(count)]
    seen |= orbit
assert seen == full and len(full) == 84 and len(set(rows) - full) == 96
assert (cert["total_words"], cert["full_cover"], cert["non_full_cover"]) == (180,84,96)
print("CHECK PASS: 180 = 96 + 7*12; literal disjoint orbits and all star/corona counts")
