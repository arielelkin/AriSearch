"""Exact finite angle-word gate; no metric or extension claim. Stdlib only."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement

ANGLE = {"P": (108, 0), "A": (144, 0), "B": (0, 1), "C": (252, -1)}

def canonical(w):
    return min(v[i:] + v[:i] for v in (w, w[::-1]) for i in range(len(w)))

def words(a, b, c):
    n = a + b + c
    result = set()
    for aa in combinations(range(n), a):
        rem = [i for i in range(n) if i not in aa]
        for bb in combinations(rem, b):
            result.add(canonical("".join("A" if i in aa else "B" if i in bb else "C" for i in range(n))))
    return sorted(result)

def masks(w, resonance):
    n = len(w)
    for mask in range(1 << n):
        degrees = [((mask >> ((i-1) % n)) & 1) + ((mask >> i) & 1) for i in range(n)]
        if all(d == 0 if x == "A" else d == 1 if x == "C" or not resonance else d in (1, 2)
               for x, d in zip(w, degrees)):
            yield mask, sum(d == 2 for d in degrees)

def survivors(a, b, c, resonance):
    result = []
    for w in words(a, b, c):
        m = sum(w[i] == w[(i+1) % len(w)] == "A" for i in range(len(w)))
        if 5*m > 2*a+c:
            continue
        mm = list(masks(w, resonance))
        target = b-c if resonance else 0
        if mm and min(t for _, t in mm) <= target <= max(t for _, t in mm):
            result.append((w, m, sorted(set(t for _, t in mm))))
    return result

def main():
    stars = []
    for triple in combinations_with_replacement(ANGLE, 3):
        intercept = sum(ANGLE[x][0] for x in triple)
        slope = sum(ANGLE[x][1] for x in triple)
        if not slope:
            if intercept == 360:
                stars.append(("".join(triple), "all"))
        else:
            alpha = Fraction(360-intercept, slope)
            if 108 < alpha < 126:
                stars.append(("".join(triple), str(alpha)))
    assert stars == [("PPA", "all"), ("PBC", "all"), ("BBB", "120")]
    print("STARS", stars)
    generic = [(10-3*k, k, k) for k in range(4)]
    resonance = [(a,b,c) for a in range(11) for b in range(7) for c in range(8)
                 if 3*a+5*b+4*c == 30 and b >= c]
    assert resonance == [(0,6,0),(1,3,3),(2,4,1),(4,2,2),(5,3,0),(7,1,1),(10,0,0)]
    for mode, inventory in ((False,generic),(True,resonance)):
        print("RESONANCE" if mode else "GENERIC")
        for a,b,c in inventory:
            result = survivors(a,b,c,mode)
            print((a,b,c), "all-dihedral-words",len(words(a,b,c)), "survivors",result)
    assert len(survivors(1,3,3,False)) == 10
    assert len(survivors(4,2,2,False)) == 7
    assert [x[0] for x in survivors(2,4,1,True)] == ["AABBBBC"]
    assert not survivors(5,3,0,True)

if __name__ == "__main__":
    main()
