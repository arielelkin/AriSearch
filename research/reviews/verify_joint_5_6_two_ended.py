#!/usr/bin/env python3
"""Review certificate: the exact joint (5,6) restart pair cannot tile.

This verifier independently enumerates all cyclic angle stars and chiralities
from the published angle/side data; it does not import the original verifier.
The original rational closure certificate proves the five length classes are
positive and distinct. Angle nonresonance forces full-edge contacts.

At a counterclockwise vertex star, each consecutive pair of sectors shares
one native side. At the OTHER endpoint of that same edge, the two sectors
occur in reversed order, at the other native corners of their respective
sides, with unchanged face chiralities. That directed pair must occur in some
allowed vertex star. Remove every star violating this necessary condition,
then repeat. Every vertex of an actual tiling survives every pass by induction.
The initial 94 ordered/chiral stars shrink to 12, then zero: no tiling exists.
This excludes reflections as well as orientation-preserving placements and
makes no assumptions about periodicity, frequencies, or preferred vertex rows.

Replay: conda run --no-capture-output -n arisearch python3 \
    research/reviews/verify_joint_5_6_two_ended.py
"""
from itertools import combinations_with_replacement, permutations, product
import json

ANGLES = (22, 54, 22, 32, 50, 34, 37, 33, 49, 39, 48)  # pi/60
CLASSES = (0, 2, 0, 1, 2, 2, 3, 1, 4, 0, 1)


def bounds(corner):
    return (0, 5) if corner < 5 else (5, 6)


def sides(flag):
    corner, flip = flag
    offset, size = bounds(corner)
    native = (offset + (corner - offset - 1) % size, corner)
    return native[::-1] if flip else native


def other_corner(flag, side):
    corner, flip = flag
    offset, size = bounds(corner)
    endpoints = (side, offset + (side - offset + 1) % size)
    assert corner in endpoints
    return (endpoints[1] if corner == endpoints[0] else endpoints[0], flip)


def contacts(star):
    return tuple((star[i], star[(i + 1) % len(star)])
                 for i in range(len(star)))


def opposite_contact(pair, classes=CLASSES):
    left, right = pair
    left_side, right_side = sides(left)[1], sides(right)[0]
    assert classes[left_side] == classes[right_side]
    return other_corner(right, right_side), other_corner(left, left_side)


def regular_hexagon_control():
    """Regular equal-sided hexagons must survive this necessary-condition filter."""
    flags = tuple(product(range(5, 11), (0, 1)))
    stars = set(product(flags, repeat=3))
    pairs = {pair for star in stars for pair in contacts(star)}
    assert all(opposite_contact(pair, (0,) * 11) in pairs for pair in pairs)
    return len(stars)


def main():
    control_stars = regular_hexagon_control()
    assert all(0 < angle < 60 for angle in ANGLES)
    # At most two corners can sum to pi; at most five can sum to 2*pi.
    assert 3 * min(ANGLES) > 60 and 6 * min(ANGLES) > 120
    assert not any(sum(ANGLES[c] for c in row) == 60
                   for size in (1, 2)
                   for row in combinations_with_replacement(range(11), size))
    stars = set()
    for size in range(3, 6):
        for row in combinations_with_replacement(range(11), size):
            if sum(ANGLES[c] for c in row) != 120:
                continue
            for order in set(permutations(row)):
                for flips in product((0, 1), repeat=size):
                    star = tuple(zip(order, flips))
                    if all(CLASSES[sides(a)[1]] == CLASSES[sides(b)[0]]
                           for a, b in contacts(star)):
                        stars.add(star)
    rounds = []
    while stars:
        pairs = {pair for star in stars for pair in contacts(star)}
        allowed = {pair for pair in pairs if opposite_contact(pair) in pairs}
        retained = {star for star in stars
                    if all(pair in allowed for pair in contacts(star))}
        rounds.append({
            "input_stars": len(stars), "directed_contacts": len(pairs),
            "two_ended_contacts": len(allowed),
            "retained_stars": len(retained),
            "retained_corner_rows": sorted({tuple(sorted(c for c, f in s))
                                             for s in retained}),
        })
        assert retained != stars, "Unexpected nonempty fixed point"
        stars = retained
    assert [(r["input_stars"], r["retained_stars"]) for r in rounds] == [
        (94, 12), (12, 0)]
    print(json.dumps({"verdict": "no plane tiling", "rounds": rounds,
                      "regular_hexagon_control_surviving_stars": control_stars,
                      "dependency": "joint_5_6_local_verify.py exact distinct-length closure"},
                     indent=2))


if __name__ == "__main__":
    main()
