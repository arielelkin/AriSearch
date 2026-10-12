#!/usr/bin/env python3
"""Independent identification test for the arrow marking of Lemma 5/6 of
research/lemmas/ammann-forcing-aperiodicity.md against de Bruijn's pentagrid
rhomb tilings (de Bruijn 1981, Indag. Math. 43): for shifts gamma with
sum(gamma) = 0 the dual tiling is a Penrose P3 tiling; for sum(gamma) not in Z
it is a 'generalized Penrose' rhomb tiling that is known NOT to obey Penrose's
matching rules.  We ask, by exact 2-SAT, whether the rhombs of a finite
pentagrid patch can be marked with the lemma's arrows (each thin rhomb: which
obtuse vertex is the X-sink; each thick: which acute vertex is the X-source)
so that every shared edge carries equal marks.

Expected if the marking is the Penrose one: SAT for sum=0, UNSAT for sum=1/2.
Exact arithmetic throughout (Q(w), w = exp(i pi/5); floors decided in Q(sqrt5)).
"""
from fractions import Fraction as Fr
import sys, itertools, math

def V(*c): return tuple(Fr(x) for x in c) + (Fr(0),) * (4 - len(c))
def add(u, v): return tuple(a + b for a, b in zip(u, v))
def sub(u, v): return tuple(a - b for a, b in zip(u, v))
def sc(f, u): return tuple(Fr(f) * a for a in u)
def tw(u):
    a, b, c, d = u
    return (-d, a + d, b - d, c + d)
def mul(u, v):
    r = V(); p = v
    for i in range(4):
        r = add(r, sc(u[i], p)); p = tw(p)
    return r
ONE = V(1); ZERO = V()
def W(k):
    u = ONE
    for _ in range(k % 10): u = tw(u)
    return u
def galois(u, m):
    r = ZERO
    for i in range(4): r = add(r, sc(u[i], W(m * i)))
    return r
def inv(u):
    p = mul(mul(galois(u, 3), galois(u, 7)), galois(u, 9))
    n = mul(u, p)
    assert n[1] == n[2] == n[3] == 0 and n[0] != 0
    return sc(1 / n[0], p)
def conj(u): return galois(u, 9)
def sgn_q5(a, b):
    if b == 0: return (a > 0) - (a < 0)
    if a == 0: return (b > 0) - (b < 0)
    if (a > 0) == (b > 0): return 1 if a > 0 else -1
    d = a * a - 5 * b * b
    if d == 0: return 0
    return (1 if a > 0 else -1) if d > 0 else (1 if b > 0 else -1)
def re_q5(u):   # Re(u) = a + b sqrt5
    c0, c1, c2, c3 = u
    return (c0 + c1 / 4 - c2 / 4 + c3 / 4, c1 / 4 + c2 / 4 - c3 / 4)
def ceil_q5(a, b):
    x = float(a) + float(b) * math.sqrt(5)
    n = math.ceil(x) - 2
    while sgn_q5(a - n, b) > 0:      # while value > n
        n += 1
    # now value <= n ; and value > n-1 ?
    assert sgn_q5(a - (n - 1), b) > 0
    return n, sgn_q5(a - n, b) == 0   # (ceil, value is integer)

Z = [W(2 * j) for j in range(5)]            # zeta_j = exp(2 pi i j / 5)

def tiling(gamma, N):
    """rhombs dual to intersections of grid lines j<k with |n| <= N.
    returns list of (kind, [v0, v1, v2, v3] ccw, vertex tuple of Z[w] ints)"""
    rh = []
    for j, k in itertools.combinations(range(5), 2):
        a, b = conj(Z[j]), Z[j]
        c, d = conj(Z[k]), Z[k]
        det_inv = inv(sub(mul(a, d), mul(b, c)))
        for nj in range(-N, N + 1):
            for nk in range(-N, N + 1):
                cj = sc(2 * (nj - gamma[j]), ONE)
                ck = sc(2 * (nk - gamma[k]), ONE)
                z = mul(sub(mul(cj, d), mul(ck, b)), det_inv)
                # check
                assert re_q5(mul(z, conj(Z[j]))) == (Fr(nj) - gamma[j], 0)
                Kv = [None] * 5
                for l in range(5):
                    if l in (j, k):
                        continue
                    xa, xb = re_q5(mul(z, conj(Z[l])))
                    n, integral = ceil_q5(xa + gamma[l], xb)
                    if integral:
                        raise ValueError('singular grid')
                    Kv[l] = n
                verts = []
                for dj, dk in ((0, 0), (1, 0), (1, 1), (0, 1)):
                    Kv[j] = nj + dj; Kv[k] = nk + dk
                    p = ZERO
                    for l in range(5):
                        p = add(p, sc(Kv[l], Z[l]))
                    verts.append(tuple(int(x) for x in p))
                # make ccw
                e1 = sub(V(*verts[1]), V(*verts[0])); e2 = sub(V(*verts[3]), V(*verts[0]))
                c0, c1, c2, c3 = mul(conj(e1), e2)
                s = c2 + c3
                if sgn_q5(c1 + s / 2, s / 2) < 0:
                    verts = [verts[0], verts[3], verts[2], verts[1]]
                dkj = (k - j) % 5
                kind = 'thick' if dkj in (1, 4) else 'thin'
                rh.append((kind, verts, (j, k, nj, nk)))
    return rh

def acute_obtuse(kind, verts):
    """angle at vertex i: 36/72 acute, else obtuse; via dot product sign"""
    out = []
    for i in range(4):
        p, q, r = V(*verts[i]), V(*verts[(i + 1) % 4]), V(*verts[(i - 1) % 4])
        a, b = re_q5(mul(conj(sub(q, p)), sub(r, p)))
        out.append(sgn_q5(a, b) > 0)    # True = acute
    return out

def markings(kind, verts):
    """the two possible lemma-markings of this rhomb, as dict edge->(type, tail, head)"""
    ac = acute_obtuse(kind, verts)
    res = []
    if kind == 'thin':
        acute = [verts[i] for i in range(4) if ac[i]]
        obt = [verts[i] for i in range(4) if not ac[i]]
        for Bv, Dv in ((obt[0], obt[1]), (obt[1], obt[0])):
            m = {}
            for Av in acute:
                m[frozenset((Av, Bv))] = ('X', Av, Bv)
                m[frozenset((Av, Dv))] = ('Y', Av, Dv)
            res.append(m)
    else:
        acute = [verts[i] for i in range(4) if ac[i]]
        obt = [verts[i] for i in range(4) if not ac[i]]
        for Ev, Gv in ((acute[0], acute[1]), (acute[1], acute[0])):
            m = {}
            for Fv in obt:
                m[frozenset((Ev, Fv))] = ('X', Ev, Fv)
                m[frozenset((Fv, Gv))] = ('Y', Fv, Gv)
            res.append(m)
    return res

def two_sat(nvar, clauses):
    """clauses: list of (lit, lit), lit = (var, value) meaning var==value.
    Return True if satisfiable (Kosaraju SCC on implication graph)."""
    def node(v, val): return 2 * v + (1 if val else 0)
    n = 2 * nvar
    g = [[] for _ in range(n)]; gr = [[] for _ in range(n)]
    for (x, xv), (y, yv) in clauses:
        # (x==xv) or (y==yv): not(x==xv) -> y==yv ; not(y==yv) -> x==xv
        g[node(x, not xv)].append(node(y, yv)); gr[node(y, yv)].append(node(x, not xv))
        g[node(y, not yv)].append(node(x, xv)); gr[node(x, xv)].append(node(y, not yv))
    order = []; seen = [False] * n
    for s in range(n):
        if seen[s]: continue
        stack = [(s, 0)]; seen[s] = True
        while stack:
            u, i = stack.pop()
            if i < len(g[u]):
                stack.append((u, i + 1))
                v = g[u][i]
                if not seen[v]:
                    seen[v] = True; stack.append((v, 0))
            else:
                order.append(u)
    comp = [-1] * n; c = 0
    for s in reversed(order):
        if comp[s] != -1: continue
        stack = [s]; comp[s] = c
        while stack:
            u = stack.pop()
            for v in gr[u]:
                if comp[v] == -1:
                    comp[v] = c; stack.append(v)
        c += 1
    return all(comp[2 * v] != comp[2 * v + 1] for v in range(nvar))

def test(gamma, N, label, log):
    rh = tiling(gamma, N)
    # sanity: tiles do not repeat
    keys = [frozenset(r[1]) for r in rh]
    assert len(set(keys)) == len(keys)
    edges = {}
    for i, (kind, verts, _) in enumerate(rh):
        for a in range(4):
            edges.setdefault(frozenset((verts[a], verts[(a + 1) % 4])), []).append(i)
    assert all(len(v) <= 2 for v in edges.values())
    mk = [markings(kind, verts) for kind, verts, _ in rh]
    clauses = []
    shared = 0
    for e, ids in edges.items():
        if len(ids) != 2: continue
        shared += 1
        i, j = ids
        for ci in (0, 1):
            for cj in (0, 1):
                if mk[i][ci][e] != mk[j][cj][e]:
                    # forbid (i==ci and j==cj): clause (i!=ci) or (j!=cj)
                    clauses.append(((i, ci != 1), (j, cj != 1)))
    sat = two_sat(len(rh), clauses)
    log.append('%s gamma=%s sum=%s N=%d rhombs=%d shared edges=%d markable=%s'
               % (label, [str(g) for g in gamma], sum(gamma), N, len(rh), shared, sat))
    return sat

def main():
    log = []
    g0 = [Fr(1, 10), Fr(2, 10), Fr(3, 10), Fr(17, 100), Fr(-77, 100)]      # sum 0
    g1 = [Fr(1, 10), Fr(2, 10), Fr(3, 10), Fr(17, 100), Fr(-27, 100)]      # sum 1/2
    g2 = [Fr(1, 10), Fr(2, 10), Fr(3, 10), Fr(17, 100), Fr(-57, 100)]      # sum 1/5
    g3 = [Fr(13, 100), Fr(41, 100), Fr(-29, 100), Fr(7, 100), Fr(-32, 100)]  # sum 0
    r = []
    for N in (3, 5, 7):
        r.append(test(g0, N, 'Penrose', log))
        r.append(test(g3, N, 'Penrose', log))
        r.append(not test(g1, N, 'generalized', log))
        r.append(not test(g2, N, 'generalized', log))
    print('\n'.join(log))
    ok = all(r)
    print('PENTAGRID IDENTIFICATION AS EXPECTED' if ok else 'PENTAGRID RESULT NOT AS EXPECTED (see log)')
    if len(sys.argv) > 1:
        open(sys.argv[1], 'w').write('\n'.join(log) + '\n')

if __name__ == '__main__':
    main()
