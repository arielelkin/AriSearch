#!/usr/bin/env python3
"""Independent native-segment audit; no imports from any producer.
Declared domain: eight r-side matches for one killed word pair, plus one
specified changed word and its entire radius-one endpoint-closure atlas.
"""
from itertools import combinations
from pathlib import Path
import json

A = (0, 1, 0, 2, 3, 4)
KILLED_B = (0, 2, 0, 3, 1, 4)
CHANGED_B = (0, 3, 0, 2, 1, 4)

def arms(words, c):
    f, i = divmod(c, 6)
    return frozenset((words[f][i], words[f][(i + 1) % 6]))

def atlas(words):
    # Select native CORNERS first; unlike the producer's ray-label product.
    result = set()
    for triple in combinations(range(12), 3):
        edges = {arms(words, c) for c in triple}
        rays = set().union(*edges)
        if len(edges) == 3 and len(rays) == 3 and all(len(e) == 2 for e in edges):
            result.add(triple)
    return result

def direct_matches(words):
    # Host A side2 goes from corner1 to corner2; its other arms are x,y.
    out = []
    for f in range(2):
        for j in range(6):
            if words[f][j] != 0:
                continue
            for swap in (False, True):
                near = [6*f + (j-1)%6, 6*f + j]
                if swap:
                    near.reverse()
                completions = []
                for host, guest in zip((1, 2), near):
                    left = next(iter(arms(words, host) - {0}))
                    right = next(iter(arms(words, guest) - {0}))
                    wanted = frozenset((left, right))
                    completions.append([] if left == right else [c for c in range(12) if arms(words, c) == wanted])
                out.append({"neighbor_type": "AB"[f], "neighbor_side": j,
                            "host_corners": [1, 2], "guest_corners": near,
                            "third_corner_choices": completions,
                            "both_endpoints_legal": all(completions)})
    assert len(out) == 8
    return out

def next_corner(words, c, ray):
    f, i = divmod(c, 6)
    if words[f][i] == ray:
        return 6*f + (i-1)%6
    assert words[f][(i+1)%6] == ray
    return 6*f + (i+1)%6

def endpoint_closure(words):
    stars = atlas(words)
    sizes = []
    while True:
        sizes.append(len(stars))
        keep = set()
        for star in stars:
            good = True
            for c, d in combinations(star, 2):
                rays = arms(words, c) & arms(words, d)
                assert len(rays) == 1
                ray = next(iter(rays))
                cc, dd = next_corner(words, c, ray), next_corner(words, d, ray)
                if cc == dd or not any(cc in s and dd in s for s in stars):
                    good = False
                    break
            if good:
                keep.add(star)
        if keep == stars:
            return stars, sizes
        stars = keep

def main():
    words = (A, KILLED_B)
    original = atlas(words)
    direct = direct_matches(words)
    assert not any(r["both_endpoints_legal"] for r in direct)
    assert len(original) == 12
    closed, stages = endpoint_closure(words)
    assert not closed and stages == [12, 1, 0]
    cert_path = Path(__file__).resolve().parents[1] / "certificates/hexagon-shared-repeat-single-family-2026-10-15.json"
    cert = json.loads(cert_path.read_text())
    assert tuple(cert["A"]) == A and tuple(cert["B"]) == KILLED_B
    assert {tuple(s) for s in cert["complete_star_atlas"]} == original
    assert cert["obstructed_corner"] == 1
    expected = []
    for star in sorted(original):
        if 1 not in star:
            continue
        seam_corners = [c for c in star if 0 in arms(words, c)]
        far = sorted(next_corner(words, c, 0) for c in seam_corners)
        assert len(far) == 2 and far[0] != far[1]
        assert not any(all(c in s for c in far) for s in original)
        expected.append({"star": list(star), "ray_label": 0, "far_corner_pair": far})
    assert expected == cert["all_corner_stars_fail"]
    changed = (A, CHANGED_B)
    survivor, rounds = endpoint_closure(changed)
    assert len(survivor) == 16 and rounds == [16]
    assert set().union(*map(set, survivor)) == set(range(12))
    assert any(r["both_endpoints_legal"] for r in direct_matches(changed))
    print(json.dumps({"status": "PASS independent eight-match obstruction",
        "direct_matches": direct, "original_pruning": stages,
        "changed_B": CHANGED_B, "changed_atlas_size": len(survivor),
        "changed_endpoint_pruning": rounds, "changed_atlas": sorted(survivor),
        "changed_A_side2_matches": direct_matches(changed)}, indent=2))

if __name__ == "__main__":
    main()
