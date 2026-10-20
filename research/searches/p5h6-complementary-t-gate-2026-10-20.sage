"""Exact first gate for the equal-unit P5/H6 complementary T proposal.

Replay with: mise exec -- conda run --no-capture-output -n arisearch sage
research/searches/p5h6-complementary-t-gate-2026-10-20.sage
"""
from sage.all import AA, CyclotomicField, matrix, vector

K = CyclotomicField(36)
z = K.gen()                       # primitive 36th root, ten degrees per power
I = z**9
u = lambda degrees: z**(degrees // 10)
re = lambda w: (w + w.conjugate()) / 2
im = lambda w: (w - w.conjugate()) / (2*I)
cross = lambda a, b: re(a)*im(b) - im(a)*re(b)

P_dirs = (0, 60, 140, 200, 260)
H_dirs = (0, 60, 120, 180, 240, 300)

# Solve closure of P with lengths (p, 1, q, 1+q, 1).
a = u(0)
b = u(140) + u(200)
c = -u(60) - u(200) - u(260)
M = matrix(K, [[re(a), re(b)], [im(a), im(b)]])
p, q = M.solve_right(vector(K, [re(c), im(c)]))
t = 1 + q
L = p + q
assert M.det() != 0
assert q == u(40) + u(320)  # 2 cos 40 degrees
assert L == p + t - 1

P_lengths = (p, K(1), q, t, K(1))
H_lengths = (L, K(1), L, t, p, t)

def vertices(dirs, lengths):
    points = [K(0)]
    for direction, length in zip(dirs, lengths):
        points.append(points[-1] + length*u(direction))
    assert points[-1] == 0
    return tuple(points[:-1])

P = vertices(P_dirs, P_lengths)
H = vertices(H_dirs, H_lengths)
assert all(AA(x) > 0 for x in P_lengths + H_lengths)
for tile in (P, H):
    n = len(tile)
    assert all(AA(cross(tile[(i+1)%n]-tile[i],
                        tile[(i+2)%n]-tile[(i+1)%n])) > 0
               for i in range(n))

# Rao Type 2, in the reviewed Table 2 transcription:
# angles A+B+D = 360 degrees and sides c=e.
# Reverse cyclic indices with offset 4.  The reflected side map has the
# required one-index shift: new side i = old side (4-i-1) mod 5.
angles = (80, 120, 100, 120, 120)
side_map = tuple((4-i-1) % 5 for i in range(5))
angle_map = tuple((4-i) % 5 for i in range(5))
new_angles = tuple(angles[i] for i in angle_map)
new_lengths = tuple(P_lengths[i] for i in side_map)
assert new_angles == (120, 120, 100, 120, 80)
assert side_map == (3, 2, 1, 0, 4)
assert new_angles[0] + new_angles[1] + new_angles[3] == 360
assert new_lengths[2] == new_lengths[4] == 1

print("P lengths: ", tuple(str(AA(x)) for x in P_lengths))
print("H lengths: ", tuple(str(AA(x)) for x in H_lengths))
print("Exact closure, positive sides, strict convexity: PASS")
print("Rao monohedral Type 2: sign=-1 offset=4, A+B+D=360, c=e=1")
print("STOP: periodic P-only omission; no cap or plane-extension search")
