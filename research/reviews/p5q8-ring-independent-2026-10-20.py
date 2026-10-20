"""Independent exact check of the four forced 12-P ring obstructions."""
from itertools import product
from sage.all import AA, QQ, QQbar, matrix, vector

zeta = QQbar.zeta(36)
def ray(deg):
    w = zeta ** (deg // 10)
    return vector(AA, (w.real(), w.imag()))

def directions(angles):
    theta = 0
    out = []
    for i in range(len(angles)):
        out.append(ray(theta))
        theta += 180 - angles[(i + 1) % len(angles)]
    return out

Pang = (100, 110, 100, 120, 110)
Qang = (150, 130, 140, 130, 140, 120, 140, 130)
Pd, Qd = directions(Pang), directions(Qang)
zero = vector(AA, (0, 0))

def close_two(dirs, lengths, a, b):
    target = -sum((lengths[i] * dirs[i] for i in lengths), zero)
    B = matrix(AA, 2, 2, [dirs[a][0], dirs[b][0], dirs[a][1], dirs[b][1]])
    x, y = B.solve_right(target)
    result = dict(lengths)
    result[a], result[b] = x, y
    assert sum((result[i] * dirs[i] for i in result), zero) == zero
    return [result[i] for i in range(len(dirs))]

def p_lengths(t):
    return close_two(Pd, {0: t, 3: t, 4: AA(1)}, 1, 2)

p0, p1 = p_lengths(AA(0)), p_lengths(AA(1))
t_large = (AA(1) - p0[2]) / (p1[2] - p0[2])

def q_lengths(p, k, reverse, free):
    known = {0: AA(1), 7: AA(1)}
    known[(k - 1) % 8] = p[2] if reverse else p[1]
    known[k] = p[1] if reverse else p[2]
    assert known[0] == known[7] == 1
    slots = [i for i in range(8) if i not in known and i not in (4, 5)]
    assert len(slots) == len(free)
    known.update({i: AA(v) for i, v in zip(slots, free)})
    return close_two(Qd, known, 4, 5)

def polygon(lengths, dirs):
    pts = [zero]
    for L, d in zip(lengths, dirs):
        pts.append(pts[-1] + L * d)
    assert pts[-1] == zero
    return pts[:-1]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def rotation_copy(src, a, b, target_a, target_b):
    u = src[b] - src[a]
    v = target_b - target_a
    assert u.dot_product(u) == v.dot_product(v)
    d = u.dot_product(v) / u.dot_product(u)
    s = cross(u, v) / u.dot_product(u)
    M = matrix(AA, [[d, -s], [s, d]])
    return [target_a + M * (x - src[a]) for x in src]

def corner_copy(src, source0, source1, source2, target0, target1, target2):
    X = matrix(AA, 2, 2, [*(source1 - source0), *(source2 - source0)]).transpose()
    Y = matrix(AA, 2, 2, [*(target1 - target0), *(target2 - target0)]).transpose()
    M = Y * X.inverse()
    assert M.transpose() * M == matrix.identity(AA, 2)
    return [target0 + M * (x - source0) for x in src]

def interiors_meet(a, b):
    for poly in (a, b):
        for i in range(len(poly)):
            edge = poly[(i + 1) % len(poly)] - poly[i]
            normal = vector(AA, (-edge[1], edge[0]))
            aa = [normal.dot_product(x) for x in a]
            bb = [normal.dot_product(x) for x in b]
            if max(aa) <= min(bb) or max(bb) <= min(aa):
                return False
    return True

cases = ((1, True, t_large, (QQ(1)/5,)*3),
         (3, False, AA(QQ(1)/2), (QQ(1)/5,)*2),
         (3, True, AA(QQ(1)/2), (QQ(1)/5,)*2),
         (7, False, t_large, (QQ(1)/5, QQ(1)/2, QQ(2))))

for k, reverse, t, free in cases:
    pl = p_lengths(t)
    ql = q_lengths(pl, k, reverse, free)
    assert all(v > 0 for v in pl + ql)
    seam_pairs = []
    for a, b, reflected in product((0, 3), (0, 3), (False, True)):
        endpoints = ((a, b), ((a+1)%5, (b+1)%5)) if reflected else \
                    ((a, (b+1)%5), ((a+1)%5, b))
        complete = True
        for ia, ib in endpoints:
            vacancy = 360 - Pang[ia] - Pang[ib]
            out_a = pl[(ia-1)%5] if ia == a else pl[ia]
            out_b = pl[(ib-1)%5] if ib == b else pl[ib]
            hits = [(species, j) for species, angles, lengths in
                    (('P', Pang, pl), ('Q', Qang, ql))
                    for j, angle in enumerate(angles)
                    if angle == vacancy and
                    ((lengths[(j-1)%len(lengths)] == out_a and lengths[j] == out_b) or
                     (lengths[(j-1)%len(lengths)] == out_b and lengths[j] == out_a))]
            complete &= bool(hits)
        if complete:
            seam_pairs.append((a, b, reflected))
    assert seam_pairs == [(0, 3, False), (3, 0, False)], seam_pairs
    p = polygon(pl, Pd)
    q = polygon(ql, Qd)
    ring = [p]
    for _ in range(12):
        current = ring[-1]
        ring.append(rotation_copy(p, 3, 4, current[1], current[0]))
    assert ring[12] == ring[0]
    ring = ring[:12]
    assert all(not interiors_meet(ring[i], ring[j]) for i in range(12) for j in range(i+1,12))
    choices = []
    for i in range(12):
        cur, nxt = ring[i], ring[(i+1) % 12]
        V, L, R = cur[0], cur[4], nxt[0]
        these = [corner_copy(q, q[0], q[1], q[7], V, a, b)
                 for a, b in ((L, R), (R, L))]
        assert these[0] != these[1]
        assert all(not interiors_meet(c, tile) for c in these for tile in ring)
        choices.append(these)
    conflict = {(i, a, j, b) for i in range(12) for j in range(i+1,12)
                for a in range(2) for b in range(2)
                if interiors_meet(choices[i][a], choices[j][b])}
    survivors = [bits for bits in product((0,1), repeat=12)
                 if all((i,bits[i],j,bits[j]) not in conflict
                        for i in range(12) for j in range(i+1,12))]
    print(k, reverse, 'choices', 2**12, 'conflicts', len(conflict),
          'survivors', len(survivors))
    assert not survivors
