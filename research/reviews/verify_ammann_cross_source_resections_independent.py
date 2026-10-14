"""Independent exact audit of four fixed J0 Ammann resection records.

No producer imports, solver, floating-point decision, or patch-size cutoff.
Coordinates/identities use Q(zeta_10); signs use its specified exact embedding.
The lattice test derives its entire finite comparison domain from bounding
boxes in lattice coordinates. See the accompanying review for logical scope.
"""
from collections import Counter
from itertools import product
from sage.all import AA, QQ, QQbar, NumberField, PolynomialRing

R = PolynomialRing(QQ, "x")
x = R.gen()
K = NumberField(x**4 - x**3 + x**2 - x + 1, "z")
z = K.gen()
embed = K.hom([QQbar.zeta(10)], QQbar)
conjugate = K.hom([z**-1], K)


def real(v):
    assert conjugate(v) == v
    return AA(embed(v))


def cross(a, b):
    # Physical cross product divided by the positive sin(pi/5).
    return (conjugate(a)*b - a*conjugate(b))/(z-z**-1)


def area(face):
    return sum(cross(p, face[(i+1) % len(face)])
               for i, p in enumerate(face))/2


def strictly_convex(face):
    assert len(set(face)) == len(face) and real(area(face)) > 0
    for i, p in enumerate(face):
        edge = face[(i+1) % len(face)]-p
        assert all(real(cross(edge, q-p)) > 0
                   for j, q in enumerate(face)
                   if j not in (i, (i+1) % len(face)))


def disjoint_interiors(f, g):
    return any(all(real(cross(f[(i+1) % len(f)]-p, q-p)) <= 0
                   for q in g) for i, p in enumerate(f))


def boundary(faces):
    for f in faces:
        strictly_convex(f)
    for i, f in enumerate(faces):
        for g in faces[i+1:]:
            assert disjoint_interiors(f, g) or disjoint_interiors(g, f)
    directed = Counter((p, f[(i+1) % len(f)])
                       for f in faces for i, p in enumerate(f))
    assert all(n == 1 for n in directed.values())
    outer = {e for e in directed if e[::-1] not in directed}
    # Full internal edges are paired exactly once; no partial cancellation.
    assert (sum(len(f) for f in faces)-len(outer)) % 2 == 0
    following = {}
    for p, q in outer:
        assert p not in following
        following[p] = q
    start = min(following, key=str)
    word = [start]
    while following[word[-1]] != start:
        word.append(following[word[-1]])
        assert len(word) <= len(outer) and len(set(word)) == len(word)
    assert len(word) == len(outer)
    assert area(word) == sum(area(f) for f in faces)
    turns = [cross(word[i]-word[i-1], word[(i+1) % len(word)]-word[i])
             for i in range(len(word))]
    assert all(t != 0 for t in turns)
    refs = [i for i, t in enumerate(turns) if real(t) < 0]
    return word, refs


def forced_halves(word, refs):
    assert len(refs) == 2
    i, j = sorted(refs)
    return word[i:j+1], word[j:]+word[:i+1]


J = K(QQ(1)/2)+QQ(4)/5*z
jp = 1+z**4*(J-1)
jpp = z+z**6*(J-z)
corner_k = z**2+z**6*(J-1)
corner_l = 1+z**7*(J-1-z)
j2 = 1+z+z**2-J
H = [K(0), jp, K(1), J, z, jpp]
P1 = [K(0), jp, K(1), corner_l, corner_k]
P2 = [corner_k, corner_l, 1+z**2, j2, z**2]
rot = z**-2
A = [rot*p for p in P1]
B = [rot*p for p in P2]
assert corner_k == z**2*jp

word, refs = boundary([H, A, B])
assert len(word) == 10 and {word[i] for i in refs} == {K(1), rot*corner_l}
halves = forced_halves(word, refs)
assert sorted(map(len, halves)) == [4, 8]
assert sum(area(f) for f in halves) == area(word)

right_h = [rot+z**-1*p for p in H]
right_p = [p+rot-z**2 for p in P2]
double_rows = []
six_six = None
for kn, left in [("H", H), ("P1", P1)]:
    for ln, right in [("H", right_h), ("P2", right_p)]:
        word, refs = boundary([A, B, left, right])
        expected = {("H", "H"): (12, 3), ("H", "P2"): (11, 2),
                    ("P1", "H"): (11, 3), ("P1", "P2"): (10, 2)}
        assert (len(word), len(refs)) == expected[kn, ln]
        if len(refs) == 3:
            assert cross(word[refs[1]]-word[refs[0]],
                         word[refs[2]]-word[refs[0]]) != 0
            side_counts = None
        else:
            halves = forced_halves(word, refs)
            side_counts = sorted(map(len, halves))
            assert side_counts == ([6, 7] if kn == "H" else [6, 6])
            chord = word[refs[1]]-word[refs[0]]
            for k in refs:
                assert cross(chord, word[k]-word[k-1]) != 0
                assert cross(chord, word[(k+1) % len(word)]-word[k]) != 0
            assert sum(area(f) for f in halves) == area(word)
            if kn == "P1":
                for f in halves:
                    strictly_convex(f)
                six_six = halves
        double_rows.append((kn, ln, len(word), len(refs), side_counts))

# Reconstruct the J-star outputs directly from their stated native corners.
JA = [1+z-z*p for p in P1]
JB = [1+z+z**2-p for p in P2]
word, refs = boundary([H, JA, JB])
assert len(word) == 10 and {word[i] for i in refs} == {K(1), z}
pentagon = [z, jpp, K(0), jp, K(1)]
heptagon = [K(1), JA[3], JA[4], 1+z, JB[0], JB[1], z]
for f in [pentagon, heptagon]:
    strictly_convex(f)
assert disjoint_interiors(pentagon, heptagon)
assert area(pentagon)+area(heptagon) == area(word)
assert {frozenset(f) for f in forced_halves(word, refs)} == {
    frozenset(pentagon), frozenset(heptagon)}

# Complete native-angle multiset audit for the J-star pentagon alone.
# Each interior angle is >=72 degrees, exactly, and <180 by strict convexity.
rho = [(pentagon[(i-1) % 5]-p)/(pentagon[(i+1) % 5]-p)
       for i, p in enumerate(pentagon)]
assert all(real(cross(K(1), r)) > 0 for r in rho)
assert all(real(cross(z**2, r)) >= 0 for r in rho)
assert rho[2]/z**2 == conjugate(rho[2]/z**2)
assert real(rho[2]/z**2) > 0
positive, negative_short = [], []
multisets = 0
for counts in product(range(6), repeat=5):
    total = sum(counts)
    if not 1 <= total <= 5:
        continue
    multisets += 1
    direction = K(1)
    for r, n in zip(rho, counts):
        direction *= r**n
    if direction == conjugate(direction):
        if real(direction) > 0:
            positive.append(counts)
        elif total <= 2:
            negative_short.append(counts)
assert multisets == 251
assert positive == [(0, 0, 5, 0, 0)] and negative_short == []

# Independent full-plane verification of the retained Q-only 6/6 escape.
# Find the opposite-edge identity from either half, independent of indexing.
candidates = []
for q in six_six:
    for i in range(6):
        f = q[i:]+q[:i]
        if f[3]-f[2] == -(f[0]-f[5]):
            candidates.append(f)
assert candidates
f = candidates[0]
f = [p-f[0] for p in f]
a, b, t = f[2], f[3]+f[4]-f[1], f[1]
g = [t-p for p in f]
det = cross(a, b)
assert real(det) > 0 and det == 2*area(f)
motif = [f, g]


def lattice_coordinates(p):
    return real(cross(p, b)/det), real(cross(a, p)/det)


boxes = []
for face in motif:
    points = [lattice_coordinates(p) for p in face]
    boxes.append([(min(p[k] for p in points), max(p[k] for p in points))
                  for k in range(2)])
comparisons = 0
for i, u in enumerate(motif):
    for j, v in enumerate(motif):
        lo = [int((boxes[i][k][0]-boxes[j][k][1]).ceil()) for k in range(2)]
        hi = [int((boxes[i][k][1]-boxes[j][k][0]).floor()) for k in range(2)]
        for m in range(lo[0], hi[0]+1):
            for n in range(lo[1], hi[1]+1):
                if i == j and m == n == 0:
                    continue
                translated = [p+m*a+n*b for p in v]
                assert disjoint_interiors(u, translated) or disjoint_interiors(translated, u)
                comparisons += 1
assert sum(area(q) for q in motif) == det

print("PASS independent Q(zeta_10) geometry: triad 4/8; double rows", double_rows)
print("PASS J-star strict 5/7; 251 exact pentagon angle multisets: only 72^5 at 360, no 180 relation")
print("PASS retained 6/6 omission: complete lattice-coordinate comparison domain",
      comparisons, "ordered pairs; motif area equals positive covolume")
