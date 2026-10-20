"""Independent exact incidence/row-space audit of the four-pentagon tree.

Does not read the producer's certificate or import its Rao table.
"""
from itertools import product
from sage.all import QQ, matrix, vector, Polyhedron

faces = (
    ("U", "a", "C0", "C1", "b"),
    ("U", "V", "c", "C2", "a"),
    ("V", "d", "C3", "C4", "c"),
    ("V", "U", "b", "C5", "d"),
)
interior = ("U", "V")
boundary = ("a", "b", "c", "d")
side_pairs = ((0, 1, 1, 0), (0, 4, 3, 1), (2, 4, 1, 1),
              (2, 0, 3, 4), (1, 0, 3, 0))


def unit(i):
    return vector(QQ, [int(j == i) for j in range(5)])


def implied(A, rhs, row, target):
    rows = A.stack(matrix(QQ, [row]))
    return rows.rank() == A.rank() == rows.augment(
        matrix(QQ, len(rhs) + 1, 1, list(rhs) + [target])).rank()


def label(f, i, phases, signs):
    return (phases[f] + signs[f] * i) % 5


def side(f, i, phases, signs):
    return (phases[f] + i) % 5 if signs[f] == 1 else (phases[f] - i - 1) % 5


def periodic(A, rhs, L, phases, signs):
    z = vector(QQ, [0] * L.nrows())
    for sign, offset in product((1, -1), range(5)):
        ang = lambda i: unit((offset + sign * i) % 5)
        leng = lambda i: unit((offset + i) % 5 if sign == 1 else (offset - i - 1) % 5)
        core = implied(A, rhs, ang(0) + ang(1) + ang(3), 360)
        if not core:
            continue
        if implied(L, z, leng(2) - leng(4), 0):
            return (2, sign, offset)
        if (implied(A, rhs, ang(4), 90)
                and implied(L, z, leng(3) - leng(4), 0)
                and implied(L, z, leng(1) - leng(2), 0)):
            return (4, sign, offset)
    return None


def main():
    # Derive angle stars from face words, not from the producer's star list.
    stars = {v: [(f, word.index(v)) for f, word in enumerate(faces) if v in word]
             for v in interior + boundary}
    assert list(map(len, stars.values())) == [3, 3, 2, 2, 2, 2]
    census = dict(inconsistent=0, no_strict_angles=0,
                  adjacent_supplementary=0, survive=0)
    witnesses = []
    for values in product(range(5), repeat=3):
        for turns in product((1, -1), repeat=3):
            phases = (0,) + values
            signs = (1,) + turns
            A = matrix(QQ, [[1] * 5] + [
                sum((unit(label(f, i, phases, signs)) for f, i in stars[v]), vector(QQ, 5))
                for v in interior + boundary])
            rhs = vector(QQ, [540, 360, 360, 180, 180, 180, 180])
            if A.rank() != A.augment(matrix(QQ, 7, 1, list(rhs))).rank():
                census["inconsistent"] += 1
                continue
            eqs = [[-b] + list(r) + [0] for r, b in zip(A.rows(), rhs)]
            ieqs = ([[0] + list(unit(i)) + [-1] for i in range(5)]
                     + [[180] + list(-unit(i)) + [-1] for i in range(5)]
                     + [[0] + [0] * 5 + [1]])
            poly = Polyhedron(eqns=eqs, ieqs=ieqs, base_ring=QQ)
            if poly.is_empty() or max(v[-1] for v in poly.vertices()) <= 0:
                census["no_strict_angles"] += 1
                continue
            if any(implied(A, rhs, unit(i) + unit((i + 1) % 5), 180)
                   for i in range(5)):
                census["adjacent_supplementary"] += 1
                continue
            census["survive"] += 1
            L = matrix(QQ, [
                unit(side(f, i, phases, signs)) - unit(side(g, j, phases, signs))
                for f, i, g, j in side_pairs])
            hit = periodic(A, rhs, L, phases, signs)
            assert hit is not None, (phases, signs)
            witnesses.append((phases, signs, hit))
    assert census == dict(inconsistent=668, no_strict_angles=260,
                          adjacent_supplementary=50, survive=22), census
    assert len(witnesses) == 22
    print("PASS independent exact 1000-template census and 22 Type 2/4 implications")
    print(census)


if __name__ == "__main__":
    main()
