"""Independent SMT census of the normalized three-P hexagon Y angle words."""
from collections import Counter
from itertools import product
import z3

angles = z3.Reals("y_a0 y_a1 y_a2 y_a3 y_a4")


def classify(k1, k2, s1, s2):
    centers = (0, k1, k2)
    signs = (1, s1, s2)
    equalities = [z3.Sum(*angles) == 540,
                  z3.Sum(*[angles[k] for k in centers]) == 360]
    for i in range(3):
        j = (i+1) % 3
        equalities.append(angles[(centers[i]-signs[i]) % 5] +
                          angles[(centers[j]+signs[j]) % 5] == 180)
    s = z3.Solver()
    s.add(*equalities)
    if s.check() == z3.unsat:
        return "inconsistent"
    s.add(*[z3.And(a > 0, a < 180) for a in angles])
    if s.check() == z3.unsat:
        return "no_strict_angles"
    for i in range(5):
        s.push()
        s.add(angles[i]+angles[(i+1) % 5] != 180)
        forced = s.check() == z3.unsat
        s.pop()
        if forced:
            return "adjacent_supplementary"
    if len(set(centers)) == 1:
        return "same_center"
    return "survive"


if __name__ == "__main__":
    counts = Counter(classify(k1,k2,s1,s2) for k1,k2,s1,s2 in
                     product(range(5),range(5),(1,-1),(1,-1)))
    print(dict(counts))
    assert counts == {"inconsistent":6, "no_strict_angles":78,
                      "adjacent_supplementary":12, "same_center":4}
