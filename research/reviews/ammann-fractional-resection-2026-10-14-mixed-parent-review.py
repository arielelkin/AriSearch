#!/usr/bin/env python3
"""Independent endpoint-order audit of the mixed-parent angle theorem.

This does not import either producer or its verifier. Representative positions
cover every weak endpoint ordering of two intersecting side intervals: two
points below P, its left endpoint, two in its interior, its right endpoint,
and two above it. Values encode order only; no metric is sampled.
"""
from itertools import product

PWORD = (90, 120, 120, 90, 120)
QWORD = (90, 135, 135, 90, 135, 135)
PSIDES = {(PWORD[i], PWORD[(i+1) % 5]) for i in range(5)}
QSIDES = {(QWORD[i], QWORD[(i+1) % 6]) for i in range(6)}
# Both native traversals and their reflected reversals are retained.
PSIDES |= {(b, a) for a, b in tuple(PSIDES)}
QSIDES |= {(b, a) for a, b in tuple(QSIDES)}
reachable = {0}
for n in range(361):
    if n in reachable:
        reachable.update(n+a for a in (90, 120, 135, 180) if n+a <= 360)
assert not reachable.intersection((45, 60, 105, 150))


def allowed_endpoint(x, angle, lo, hi, angles):
    if lo < x < hi:
        return 360-180-angle in reachable
    if x == lo:
        return 360-angle-angles[0] in reachable
    if x == hi:
        return 360-angle-angles[1] in reachable
    return True


def endpoint_consistent(pa, qa, left, right):
    return all((
        allowed_endpoint(0, pa[0], left, right, qa),
        allowed_endpoint(3, pa[1], left, right, qa),
        allowed_endpoint(left, qa[0], 0, 3, pa),
        allowed_endpoint(right, qa[1], 0, 3, pa),
    ))


def prove_wedge(host, guest):
    # Along each arm, a shorter guest leaves its own native angle in a
    # host flat sector; a longer guest leaves the host native angle in a
    # guest flat sector. Neither is allowed for these far angles.
    for h, g in zip(host, guest):
        assert 360-180-g not in reachable
        assert 360-180-h not in reachable
    # If both arm endpoints coincide, at least one ray remains forbidden.
    assert any(360-h-g not in reachable for h, g in zip(host, guest))


def main():
    survivors = []
    tested = 0
    for pa, qa in product(sorted(PSIDES), sorted(QSIDES)):
        for left, right in product(range(-2, 6), repeat=2):
            if not left < right or max(0, left) >= min(3, right):
                continue
            tested += 1
            if not endpoint_consistent(pa, qa, left, right):
                continue
            survivors.append((pa, qa, left, right))
            # Reverse the line if needed so that P's native120 is right.
            if pa == (120, 90):
                pa, qa = pa[::-1], qa[::-1]
                left, right = 3-right, 3-left
            assert pa == (90, 120) and qa == (135, 90)
            assert left <= 0 < right < 3
            # Q90 is strictly inside the P side. P's remaining right arm
            # ends at120; Q's other native arm ends at135. Both are actual
            # native side segments. Reflected corner arms are homogeneous.
            for word in (PWORD, QWORD):
                for i, corner in enumerate(word):
                    if corner == 90:
                        guest = (word[i-1], word[(i+1) % len(word)])
                        assert guest in ((120, 120), (135, 135))
                        prove_wedge((120, 135), guest)
                        prove_wedge((120, 135), guest[::-1])
    assert survivors
    assert any(left == 0 or right == 3 for _, _, left, right in survivors)
    assert any(left < 0 or right > 3 for _, _, left, right in survivors)
    print(f"PASS: {tested} positive-overlap endpoint order/side-word cases; "
          f"{len(survivors)} interval representatives survive first gate; "
          "all normalize to staggered or aligned Q containment and die at mixed120/135 wedge")


if __name__ == "__main__":
    main()
