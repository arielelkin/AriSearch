#!/usr/bin/env python3
"""Independent hostile re-check of the two-hexagon generic partition census.

Re-implemented from the WRITTEN conventions of
research/lemmas/two-hexagon-global-sft-encoding.md (Section 1) and
research/lemmas/two-hexagon-global-census.md; no import of the authors' code.

Conventions (from the lemma text):
  directions D_k = (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1);
  slot k of z = vertex shared by z, z+D_k (its slot k+2), z+D_{k+1} (slot k+4);
  side-slot k of z joins slots k,k+1, shared with z+D_{k+1} (its side-slot k+3);
  symbol (q,r,s): corner r+s*k at slot k; side r+k (s=1) or r-k-1 (s=-1);
  certificate symbol index = 12q + 6[s=-1] + r; corners/sides 0..5 = A, 6..11 = B.

Replay reconstructs partition closures from the retained certificate; no
agent-specific scratch file or prior combin run is required.

Parts (selected by argv[1]):
  combin   : group (288), partition orbits (expect 100), closures T(Pi) by an
             independent parametric method, rank, exact generic rational point,
             match with certificate; rank-2 covering flats.
  tori     : every torus record: legality in T, glued pairs E(x), F-generation,
             lattice stats, symmetry-action soundness (transformed tori legal).
  sat LO HI: z3 (QF_FD, SAT backend; NOT CP-SAT) re-solve of the final query
             for classes LO..HI-1 with an independent CNF encoding.
"""
import sys, json, itertools, random, time
from fractions import Fraction as Fr

CERT = "research/certificates/two-hexagon-global-partition-strata.json"
D = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
SYMS = [(i // 12, i % 6, 1 if (i % 12) < 6 else -1) for i in range(24)]
assert all(12 * q + 6 * (s == -1) + r == i for i, (q, r, s) in enumerate(SYMS))


def corner(i, k):
    q, r, s = SYMS[i]
    return 6 * q + (r + s * k) % 6


def side(i, k):
    q, r, s = SYMS[i]
    return 6 * q + ((r + k) % 6 if s == 1 else (r - k - 1) % 6)


def plus(z, d):
    return (z[0] + d[0], z[1] + d[1])


# ------------------------------------------------------------------ group
def build_group():
    """Elements: (corner perm, side perm, symbol perm). Built from dihedral
    relabellings c -> a + eps*c of each hexagon, optionally swapping A,B."""
    G = []
    for a0 in range(6):
        for e0 in (1, -1):
            for a1 in range(6):
                for e1 in (1, -1):
                    for sw in (0, 1):
                        cp, sp, yp = [0] * 12, [0] * 12, [0] * 24
                        for q, (a, e) in enumerate(((a0, e0), (a1, e1))):
                            q2 = q ^ sw
                            for c in range(6):
                                cp[6 * q + c] = 6 * q2 + (a + e * c) % 6
                                # side c joins corners c, c+1 -> images a+e c, a+e(c+1)
                                u, v = (a + e * c) % 6, (a + e * (c + 1)) % 6
                                sp[6 * q + c] = 6 * q2 + (u if (v - u) % 6 == 1 else v)
                            for r in range(6):
                                for s in (1, -1):
                                    i = 12 * q + 6 * (s == -1) + r
                                    r2, s2 = (a + e * r) % 6, e * s
                                    yp[i] = 12 * q2 + 6 * (s2 == -1) + r2
                        G.append((tuple(cp), tuple(sp), tuple(yp)))
    assert len(set(G)) == 288
    # soundness of the symbol action: corner/side at every slot transforms
    for cp, sp, yp in G:
        for i in range(24):
            for k in range(6):
                assert corner(yp[i], k) == cp[corner(i, k)]
                assert side(yp[i], k) == sp[side(i, k)]
    return G


def img_triple(g, t):
    return tuple(sorted(g[0][c] for c in t))


def img_pair(g, p):
    a, b = g[1][p[0]], g[1][p[1]]
    return (min(a, b), max(a, b))


TRIPLES = list(itertools.combinations_with_replacement(range(12), 3))
PAIRS = list(itertools.combinations(range(12), 2))


# ------------------------------------------------------------------ algebra (sympy, parametric)
def flat_param(eqs):
    """eqs: list of (row of 12 ints, rhs). Returns particular solution and nullspace basis."""
    import sympy as sp
    M = sp.Matrix([r for r, _ in eqs]); b = sp.Matrix([h for _, h in eqs])
    sol, params = M.gauss_jordan_solve(b)
    p = sol.subs({t: 0 for t in params})
    N = M.nullspace()
    return [Fr(int(x.p), int(x.q)) for x in p], [[Fr(int(x.p), int(x.q)) for x in n] for n in N], M.rank()


def tvec(t):
    v = [0] * 12
    for c in t:
        v[c] += 1
    return v


SUMS = [([1] * 6 + [0] * 6, 720), ([0] * 6 + [1] * 6, 720)]


def closure_param(gens):
    p, N, rk = flat_param(SUMS + [(tvec(t), 360) for t in gens])
    T = []
    for t in TRIPLES:
        v = tvec(t)
        if sum(a * b for a, b in zip(v, p)) == 360 and all(sum(a * b for a, b in zip(v, n)) == 0 for n in N):
            T.append(t)
    return T, rk - 2, p, N


def generic_point(T, p, N, tries=4000, seed=1):
    """exact rational point of the flat in (0,180)^12 whose 360-triples are exactly T."""
    import numpy as np
    from scipy.optimize import linprog
    rng = random.Random(seed)
    Ts = set(T)
    d = len(N)
    if d == 0:
        cands = [p]
    else:
        # LP: maximise slack s with 0 + s <= p + N c <= 180 - s
        P = np.array([float(x) for x in p]); NN = np.array([[float(x) for x in n] for n in N]).T
        A, bb = [], []
        for i in range(12):
            A.append(list(-NN[i]) + [1]); bb.append(P[i])
            A.append(list(NN[i]) + [1]); bb.append(180 - P[i])
        res = linprog([0] * d + [-1], A_ub=A, b_ub=bb, bounds=[(None, None)] * d + [(0, 90)])
        if not res.success or res.x[-1] <= 1e-9:
            return None
        c0 = res.x[:d]; slack = res.x[-1]
        cands = []
        for _ in range(tries):
            c = [Fr(c0[j]).limit_denominator(1000) + Fr(rng.randint(-10 ** 6, 10 ** 6), 10 ** 7) * Fr(slack).limit_denominator(1000) / (1 + d)
                 for j in range(d)]
            cands.append([p[i] + sum(c[j] * N[j][i] for j in range(d)) for i in range(12)])
    for a in cands:
        if not all(0 < x < 180 for x in a):
            continue
        if sum(a[:6]) != 720 or sum(a[6:]) != 720:
            continue
        S = {t for t in TRIPLES if sum(a[c] for c in t) == 360}
        if S == Ts:
            return a
    return None


# ------------------------------------------------------------------ partitions
def partitions12():
    def rec(rem):
        if not rem:
            yield ()
            return
        f = rem[0]
        for a, b in itertools.combinations(rem[1:], 2):
            r = [x for x in rem if x not in (f, a, b)]
            for rest in rec(r):
                yield ((f, a, b),) + rest
    yield from rec(list(range(12)))


def canon_blocks(bl, G):
    return min(tuple(sorted(img_triple(g, b) for b in bl)) for g in G)


def part_combin():
    G = build_group()
    print("group order", len(G), "(symbol action verified slot-by-slot)")
    parts = list(partitions12())
    print("partitions of 12 into four 3-blocks:", len(parts))
    orbits = {}
    for bl in parts:
        orbits.setdefault(canon_blocks(bl, G), []).append(bl)
    print("orbits under 288:", len(orbits), " orbit sizes sum", sum(len(v) for v in orbits.values()))
    cert = json.load(open(CERT))
    cmap = {}
    for st in cert["strata"]:
        k = canon_blocks([tuple(b) for b in st["partition"]], G)
        assert k not in cmap, "duplicate class in certificate"
        cmap[k] = st
    print("certificate classes", len(cmap), " equal to my orbit set:", set(cmap) == set(orbits))
    out = {}
    nreal = 0; badT = 0; mixed_vs_tori = []
    ranks = {}
    for k, st in cmap.items():
        bl = [tuple(b) for b in st["partition"]]
        T, rk, p, N = closure_param(bl)
        if sorted(map(tuple, st["T"])) != T:
            badT += 1; print("T MISMATCH", st["index"], T, st["T"])
        ranks[rk] = ranks.get(rk, 0) + 1
        a = generic_point(T, p, N)
        nreal += a is not None
        allmixed = all(any(c < 6 for c in b) and any(c >= 6 for c in b) for b in bl)
        nomixed = all(all(c < 6 for c in b) or all(c >= 6 for c in b) for b in bl)
        mixed_vs_tori.append((allmixed, len(st["tori"]) == 0))
        out[st["index"]] = {"T": T, "rank": rk, "allmixed": allmixed, "nomixed": nomixed,
                            "generic_point": [str(x) for x in a] if a else None,
                            "flat_dim": len(N) - 0}
    print("T(Pi) mismatches:", badT, " ranks (mod 4pi sums):", ranks)
    print("classes with exact generic rational point (realisable exact type):", nreal, "/ 100")
    agree = sum(1 for am, nt in mixed_vs_tori if am == nt)
    print("all-mixed <=> zero tori in certificate: agree on", agree, "/ 100; all-mixed count",
          sum(am for am, _ in mixed_vs_tori), "; zero-tori count", sum(nt for _, nt in mixed_vs_tori))
    print("no-mixed classes:", sorted(i for i, v in out.items() if v["nomixed"]),
          "ranks", sorted({v["rank"] for v in out.values() if v["nomixed"]}))
    return out


# ------------------------------------------------------------------ rank-2 covering flats (fast Fraction rref)
def rref(rows):
    M = [list(map(Fr, r)) for r in rows]; piv = []; rk = 0
    for c in range(13):
        pr = next((r for r in range(rk, len(M)) if M[r][c] != 0), None)
        if pr is None:
            continue
        M[rk], M[pr] = M[pr], M[rk]; pv = M[rk][c]; M[rk] = [x / pv for x in M[rk]]
        for r in range(len(M)):
            if r != rk and M[r][c] != 0:
                f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[rk])]
        piv.append(c); rk += 1
    return M[:rk], piv


def part_flats2():
    """Enumerate all closures of 1 or 2 triples; keep rank-2 (mod sums) flats that
    meet the open box; report how many cover all 12 corners, up to symmetry."""
    import numpy as np
    from scipy.optimize import linprog
    G = build_group()
    base = [r + [h] for r, h in SUMS]

    def clos(gens):
        M, piv = rref(base + [tvec(t) + [360] for t in gens])
        res = []
        for t in TRIPLES:
            v = list(map(Fr, tvec(t) + [360]))
            for row, c in zip(M, piv):
                if v[c] != 0:
                    f = v[c]; v = [x - f * y for x, y in zip(v, row)]
            if all(x == 0 for x in v):
                res.append(t)
        return tuple(res), len(M) - 2

    def feasible(T):
        A_eq = [[1] * 6 + [0] * 6, [0] * 6 + [1] * 6] + [tvec(t) for t in T]
        b_eq = [720, 720] + [360] * len(T)
        r = linprog([0] * 12 + [-1], A_eq=[a + [0] for a in A_eq], b_eq=b_eq,
                    A_ub=[[(-1 if j == i else 0) for j in range(12)] + [1] for i in range(12)] +
                         [[(1 if j == i else 0) for j in range(12)] + [1] for i in range(12)],
                    b_ub=[0] * 12 + [180] * 12, bounds=[(None, None)] * 12 + [(0, 1)])
        return r.success and r.x[-1] > 1e-7

    seen = {}
    for t1, t2 in itertools.combinations(TRIPLES, 2):
        T, rk = clos([t1, t2])
        if rk != 2:
            continue
        c = min(tuple(sorted(img_triple(g, t) for t in T)) for g in G)
        if c in seen:
            continue
        seen[c] = feasible(T)
    feas = [c for c, f in seen.items() if f]
    cov = [c for c in feas if len({x for t in c for x in t}) == 12]
    print("rank-2 flats up to symmetry:", len(seen), " feasible:", len(feas), " covering:", len(cov))
    for c in cov:
        print("  covering rank-2 flat:", c)


# ------------------------------------------------------------------ tori
def torus_reduce(lat):
    n, s, m = lat

    def red(z):
        x, y = z
        q = y // m
        return ((x - s * q) % n, y - m * q)
    return red


def torus_usage(lab, lat):
    """lab: dict (x,y)->symbol index on the fundamental domain; returns
    (vertex triples, glued side pairs) checking ALL six slots of every cell."""
    red = torus_reduce(lat)
    n, s, m = lat
    assert set(lab) == {(x, y) for x in range(n) for y in range(m)}, "domain mismatch"
    U, E = set(), set()
    for z, i in lab.items():
        for k in range(6):
            b = lab[red(plus(z, D[k]))]; c = lab[red(plus(z, D[(k + 1) % 6]))]
            U.add(tuple(sorted((corner(i, k), corner(b, (k + 2) % 6), corner(c, (k + 4) % 6)))))
            w = lab[red(plus(z, D[(k + 1) % 6]))]
            a1, a2 = side(i, k), side(w, (k + 3) % 6)
            if a1 != a2:
                E.add((min(a1, a2), max(a1, a2)))
    return U, E


def eq_classes(pairs):
    par = list(range(12))

    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    for a, b in pairs:
        par[f(a)] = f(b)
    return [f(i) for i in range(12)]


def load_records():
    cert = json.load(open(CERT))
    recs = []
    for st in cert["strata"]:
        for t in st["tori"]:
            lab = {tuple(map(int, k.split(","))): v for k, v in t["sol"].items()}
            recs.append((st["index"], st, t, lab))
    return cert, recs


def retained_partition_closures():
    """Independently derive the former scratch input from retained partitions."""
    cert = json.load(open(CERT))
    out = {}
    for st in cert["strata"]:
        T, _, _, _ = closure_param([tuple(b) for b in st["partition"]])
        assert T == sorted(map(tuple, st["T"])), "Partition closure mismatch"
        out[str(st["index"])] = {"T": T}
    return out


def part_tori():
    G = build_group()
    comb = retained_partition_closures()
    cert, recs = load_records()
    fails = 0; idx = {}; mono = 0; Ediff = 0
    for ci, st, t, lab in recs:
        T = set(map(tuple, comb[str(ci)]["T"]))
        lat = tuple(t["lat"])
        assert lat[0] >= 1 and lat[2] >= 1
        U, E = torus_usage(lab, lat)
        ok = U <= T
        if set(map(tuple, t["E"])) != E:
            Ediff += 1; print("E differs", ci, sorted(E), t["E"])
        cl = eq_classes(t["F"])
        ok &= all(cl[a] == cl[b] for a, b in E)
        # legality under the recorded class vector
        ok &= all(t["cls"][a] == t["cls"][b] for a, b in E)
        # symmetry images: for every g in Stab(T), the transformed torus is legal with U'<=T, E' = g(E)
        stab = [g for g in G if {img_triple(g, x) for x in T} == T]
        for g in stab:
            lab2 = {z: g[2][v] for z, v in lab.items()}
            U2, E2 = torus_usage(lab2, lat)
            ok &= U2 <= T and E2 == {img_pair(g, p) for p in E}
        if not ok:
            fails += 1; print("FAIL", ci, t)
        idx[lat[0] * lat[2]] = idx.get(lat[0] * lat[2], 0) + 1
        mono += len({SYMS[v][0] for v in lab.values()}) == 1
    print("records", len(recs), "failures", fails, "E mismatches", Ediff)
    assert fails == 0 and Ediff == 0, "Torus verification failed"
    print("lattice index distribution", dict(sorted(idx.items())), " monohedral", mono, " both tiles", len(recs) - mono)
    print("distinct labelled tori (lat, labelling):", len({(tuple(t['lat']), tuple(sorted(lab.items()))) for _, _, t, lab in recs}))


# ------------------------------------------------------------------ z3 SAT re-check
def hex_cells(R):
    return [(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1) if max(abs(x), abs(y), abs(x + y)) <= R]


def sat_query(T, Erecs, G, R=3, all_equal=False, timeout_ms=None, fix=None, eq_fix=None):
    import z3
    T = set(T)
    s = z3.SolverFor("QF_FD")
    if timeout_ms:
        s.set("timeout", timeout_ms)
    cells = hex_cells(R); cs = set(cells)
    X = {z: [z3.Bool("x_%d_%d_%d" % (z[0], z[1], i)) for i in range(24)] for z in cells}
    for z in cells:
        s.add(z3.Or(X[z]))
        for i, j in itertools.combinations(range(24), 2):
            s.add(z3.Or(z3.Not(X[z][i]), z3.Not(X[z][j])))
    C, S = {}, {}
    for z in cells:
        for k in range(6):
            for c in range(12):
                v = z3.Bool("c_%d_%d_%d_%d" % (z[0], z[1], k, c))
                src = [X[z][i] for i in range(24) if corner(i, k) == c]
                assert len(src) == 2
                s.add(v == z3.Or(src)); C[(z, k, c)] = v
                w = z3.Bool("s_%d_%d_%d_%d" % (z[0], z[1], k, c))
                src = [X[z][i] for i in range(24) if side(i, k) == c]
                assert len(src) == 2
                s.add(w == z3.Or(src)); S[(z, k, c)] = w
    e = {p: z3.Bool("e_%d_%d" % p) for p in PAIRS}

    def E(a, b):
        return True if a == b else e[(min(a, b), max(a, b))]
    if all_equal:
        for p in PAIRS:
            s.add(e[p])
    for a, b, c in itertools.permutations(range(12), 3):
        s.add(z3.Or(z3.Not(E(a, b)), z3.Not(E(b, c)), E(a, c)))
    verts, edges = set(), set()
    nv = ne = 0
    for z in cells:
        for k in range(6):
            b, c = plus(z, D[k]), plus(z, D[(k + 1) % 6])
            if b in cs and c in cs:
                key = frozenset((z, b, c))
                if key not in verts:
                    verts.add(key); nv += 1
                    for i, j, l in itertools.product(range(12), repeat=3):
                        if tuple(sorted((i, j, l))) not in T:
                            s.add(z3.Or(z3.Not(C[(z, k, i)]), z3.Not(C[(b, (k + 2) % 6, j)]), z3.Not(C[(c, (k + 4) % 6, l)])))
            w = plus(z, D[(k + 1) % 6])
            if w in cs and frozenset((z, w)) not in edges:
                edges.add(frozenset((z, w))); ne += 1
                for i in range(12):
                    for j in range(12):
                        if i != j:
                            s.add(z3.Or(z3.Not(S[(z, k, i)]), z3.Not(S[(w, (k + 3) % 6, j)]), E(i, j)))
    stab = [g for g in G if {img_triple(g, x) for x in T} == T]
    ncl = 0
    seen = set()
    for Ex in Erecs:
        for g in stab:
            key = frozenset(img_pair(g, p) for p in Ex)
            if key in seen:
                continue
            seen.add(key); ncl += 1
            s.add(z3.Or([z3.Not(e[p]) for p in key]) if key else False)
    if fix is not None:          # positive control: force a given labelling
        for z in cells:
            s.add(X[z][fix[z]])
    if eq_fix is not None:       # force e to be exactly a given equivalence
        for p in PAIRS:
            s.add(e[p] if p in eq_fix else z3.Not(e[p]))
    t0 = time.time()
    r = s.check()
    res = [str(r), time.time() - t0, nv, ne, ncl, len(stab)]
    if r == z3.sat:              # decode and re-check the patch independently of the CNF
        mdl = s.model()
        lab = {z: [i for i in range(24) if z3.is_true(mdl.eval(X[z][i]))] for z in cells}
        assert all(len(v) == 1 for v in lab.values())
        lab = {z: v[0] for z, v in lab.items()}
        ev = {p for p in PAIRS if z3.is_true(mdl.eval(e[p]))}
        good = True
        for z in cells:
            for k in range(6):
                b, c = plus(z, D[k]), plus(z, D[(k + 1) % 6])
                if b in cs and c in cs:
                    good &= tuple(sorted((corner(lab[z], k), corner(lab[b], (k + 2) % 6), corner(lab[c], (k + 4) % 6)))) in T
                w = plus(z, D[(k + 1) % 6])
                if w in cs:
                    a1, a2 = side(lab[z], k), side(lab[w], (k + 3) % 6)
                    good &= a1 == a2 or (min(a1, a2), max(a1, a2)) in ev
        res.append(good)
    return tuple(res)


def unfold(lab, lat, R=3):
    red = torus_reduce(lat)
    return {z: lab[red(z)] for z in hex_cells(R)}


def part_controls():
    G = build_group()
    comb = retained_partition_closures()
    cert, recs = load_records()
    nok = 0
    for ci, st, t, lab in recs:
        T = [tuple(x) for x in comb[str(ci)]["T"]]
        U, E = torus_usage(lab, tuple(t["lat"]))
        cl = eq_classes(E)
        eqc = {p for p in PAIRS if cl[p[0]] == cl[p[1]]}
        r = sat_query(T, [], G, fix=unfold(lab, tuple(t["lat"])), eq_fix=eqc)
        nok += r[0] == "sat" and r[-1] is True
        if r[0] != "sat":
            print("CONTROL FAIL (torus rejected by encoding)", ci, t["lat"])
    print("unfolded tori accepted by the CNF:", nok, "/", len(recs))
    # dropping the escape clauses must give SAT on every class that has tori
    done = set()
    for ci, st, t, lab in recs:
        if ci in done:
            continue
        done.add(ci)
        T = [tuple(x) for x in comb[str(ci)]["T"]]
        r = sat_query(T, [], G)
        print("class", ci, "no escape clauses ->", r[0], "decoded patch legal:", r[-1] if r[0] == "sat" else None, flush=True)


def part_sat(lo, hi, outfn):
    G = build_group()
    comb = retained_partition_closures()
    cert, recs = load_records()
    byclass = {}
    for ci, st, t, lab in recs:
        byclass.setdefault(ci, []).append(torus_usage(lab, tuple(t["lat"]))[1])
    out = open(outfn, "a")
    for ci in range(lo, hi):
        T = [tuple(x) for x in comb[str(ci)]["T"]]
        Erecs = byclass.get(ci, [])
        if not Erecs:
            r = sat_query(T, [], G, all_equal=True)
            mode = "all-sides-equal, no clauses"
        else:
            r = sat_query(T, Erecs, G)
            mode = "free e, %d torus records" % len(Erecs)
        rec = {"class": ci, "mode": mode, "result": r[0], "secs": round(r[1], 1), "vertices": r[2],
               "edges": r[3], "clauses": r[4], "stab": r[5]}
        out.write(json.dumps(rec) + "\n"); out.flush()
        print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "combin":
        part_combin()
    elif mode == "flats2":
        part_flats2()
    elif mode == "tori":
        part_tori()
    elif mode == "controls":
        part_controls()
    elif mode == "sat":
        part_sat(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
