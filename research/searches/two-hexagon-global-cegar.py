#!/usr/bin/env python3
"""Counterexample-guided census of ALL combinatorial types of two-hexagon pairs.

A type is (T, ~): T a set of corner multisets {c1,c2,c3} (corners 0..11,
0..5 = A, 6..11 = B) declared to have angle sum 360, and ~ an equivalence
relation on the 12 sides (0..5 = A sides, 6..11 = B sides).  The vertex-star
SFT X(T,~) uses exactly the stars whose corner multiset is in T and whose
glued sides are ~-equivalent.  X is monotone: T'<=T, ~'<=~ => X(T',~') <= X(T,~).

Query Q_R (CP-SAT): find booleans t (364 triples), an equivalence e on sides,
and a legal labelled hexagonal patch of radius R in X(t,e), subject to all
blocking clauses learnt so far:
  * torus clause    : not( U(x) <= t  and  E(x) <= e ) for every torus x found
                      (U = triples used, E = side pairs glued); valid because
                      x is then a torus of X(t,e).
  * angle core      : not( S <= t ) if the 360-equations of S are infeasible
                      with 0<angle<180 and the two 720 sums (exact, z3).
  * closure clause  : S <= t  =>  t_tau  if the equations of S imply tau.
  * emptiness clause: t not<= T0 or e not<= ~0, whenever X(T0,~0) has no
                      legal patch of radius R2.
  * candidate block : same shape, for recorded unresolved candidates.
All clauses are closed under the 288 relabelling symmetries.

If Q_R becomes UNSAT with no candidate recorded, then for EVERY angle-realisable
exact type (T,~) [lengths not even required to be realisable], X(T,~) is empty
or contains a torus.  Candidates are listed for separate treatment.
"""
import sys, os, json, time, itertools, importlib.util
from fractions import Fraction as Fr
from ortools.sat.python import cp_model
import z3

_here = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_here, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
S_ = _load("thg_sft", "two-hexagon-global-sft.py")
D = S_.D; add = S_.add
SYMS = S_.symbols()
NS = len(SYMS)

TRIPLES = list(itertools.combinations_with_replacement(range(12), 3))
TIDX = {t: i for i, t in enumerate(TRIPLES)}
PAIRS = [(i, j) for i in range(12) for j in range(i + 1, 12)]
PIDX = {p: i for i, p in enumerate(PAIRS)}


def corner_id(sym, k):
    return 6 * sym[0] + S_.corner_at(sym, k)


def side_id(sym, k):
    return 6 * sym[0] + S_.side_at(sym, k)


# ---------------------------------------------------------------- symmetry
def group():
    d6 = [(r, s) for r in range(6) for s in (1, -1)]
    G = []
    for (ra, sa) in d6:
        for (rb, sb) in d6:
            for swap in (0, 1):
                cm = [0] * 12; sm = [0] * 12
                for t, (r, s) in ((0, (ra, sa)), (1, (rb, sb))):
                    tt = t ^ swap
                    for i in range(6):
                        cm[6 * t + i] = 6 * tt + (r + s * i) % 6
                        sm[6 * t + i] = 6 * tt + ((r + i) % 6 if s == 1 else (r - i - 1) % 6)
                G.append((tuple(cm), tuple(sm)))
    return G


GROUP = group()


def img_triple(g, t):
    return tuple(sorted(g[0][c] for c in t))


def img_pair(g, p):
    a, b = g[1][p[0]], g[1][p[1]]
    return (min(a, b), max(a, b))


# ---------------------------------------------------------------- exact algebra
def rref_rank(rows):
    M = [list(map(Fr, r)) for r in rows]
    rank = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = None
        for r in range(rank, len(M)):
            if M[r][c] != 0:
                piv = r; break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][c]
        M[rank] = [v / pv for v in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
    return rank


def eqrow(t):
    r = [0] * 12
    for c in t:
        r[c] += 1
    return r + [360]


BASE = [[1] * 6 + [0] * 6 + [720], [0] * 6 + [1] * 6 + [720]]


def rref_basis(rows):
    M = [list(map(Fr, r)) for r in rows]
    piv = []; rank = 0
    for c in range(13):
        pr = None
        for r in range(rank, len(M)):
            if M[r][c] != 0:
                pr = r; break
        if pr is None:
            continue
        M[rank], M[pr] = M[pr], M[rank]
        pv = M[rank][c]; M[rank] = [v / pv for v in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        piv.append(c); rank += 1
    return M[:rank], piv


def in_span(basis, v):
    B, piv = basis
    v = list(map(Fr, v))
    for row, c in zip(B, piv):
        if v[c] != 0:
            f = v[c]; v = [a - f * b for a, b in zip(v, row)]
    return all(x == 0 for x in v)


def closure(T):
    bas = rref_basis(BASE + [eqrow(t) for t in T])
    return [t for t in TRIPLES if in_span(bas, eqrow(t))]


def closure_contains(S, targets):
    bas = rref_basis(BASE + [eqrow(t) for t in S])
    return all(in_span(bas, eqrow(t)) for t in targets)


def minimal_generating(S, targets):
    """greedy-minimal subset S' of S whose closure contains all targets."""
    S = list(S)
    i = 0
    while i < len(S):
        S2 = S[:i] + S[i + 1:]
        if closure_contains(S2, targets):
            S = S2
        else:
            i += 1
    return S


def eq_closure_contains(F, targets):
    cls = classes_from_pairs(F)
    return all(cls[a] == cls[b] for a, b in targets)


def minimal_eq_generating(F, targets):
    F = list(F); i = 0
    while i < len(F):
        F2 = F[:i] + F[i + 1:]
        if eq_closure_contains(F2, targets):
            F = F2
        else:
            i += 1
    return F


def angle_feasible(T):
    """exact: returns (True, model angles) or (False, core subset of T)."""
    s = z3.Solver()
    a = [z3.Real("a%d" % i) for i in range(12)]
    for v in a:
        s.add(v > 0, v < 180)
    s.add(z3.Sum(a[:6]) == 720, z3.Sum(a[6:]) == 720)
    lits = []
    for i, t in enumerate(T):
        p = z3.Bool("p%d" % i)
        s.add(z3.Implies(p, z3.Sum([a[c] for c in t]) == 360))
        lits.append(p)
    r = s.check(*lits)
    if r == z3.sat:
        return True, None
    core = s.unsat_core()
    idx = sorted(int(str(p)[1:]) for p in core)
    S = [T[i] for i in idx]
    # minimise
    i = 0
    while i < len(S):
        ok, _ = angle_feasible_plain(S[:i] + S[i + 1:])
        if not ok:
            S = S[:i] + S[i + 1:]
        else:
            i += 1
    return False, S


def angle_feasible_plain(T):
    s = z3.Solver()
    a = [z3.Real("a%d" % i) for i in range(12)]
    for v in a:
        s.add(v > 0, v < 180)
    s.add(z3.Sum(a[:6]) == 720, z3.Sum(a[6:]) == 720)
    for t in T:
        s.add(z3.Sum([a[c] for c in t]) == 360)
    return s.check() == z3.sat, None


# ---------------------------------------------------------------- typed SFT
class TypeSFT:
    def __init__(self, T, cls):
        self.T = set(T); self.cls = cls  # cls[side] -> class id
        self.tab = {}
        for k in (0, 1):
            al = []
            for i, j, l in itertools.product(range(NS), repeat=3):
                a, b, c = SYMS[i], SYMS[j], SYMS[l]
                tri = tuple(sorted((corner_id(a, k), corner_id(b, k + 2), corner_id(c, k + 4))))
                if tri not in self.T:
                    continue
                if cls[side_id(a, (k - 1) % 6)] != cls[side_id(b, (k + 2) % 6)]:
                    continue
                if cls[side_id(a, k % 6)] != cls[side_id(c, (k + 3) % 6)]:
                    continue
                if cls[side_id(b, (k + 1) % 6)] != cls[side_id(c, (k + 4) % 6)]:
                    continue
                al.append((i, j, l))
            self.tab[k] = al
        self.syms = SYMS

    model = S_.SFT.model
    solve = S_.SFT.solve
    patch = S_.SFT.patch
    torus = S_.SFT.torus
    tori = S_.SFT.tori


def usage(sol, lat):
    """triples and glued side pairs used by a torus solution."""
    n, s, mm = lat
    def wrap(z):
        x, y = z
        q = y // mm
        return ((x - s * q) % n, y - mm * q)
    U, E = set(), set()
    for z, v in sol.items():
        a = SYMS[v]
        for k in (0, 1):
            b = SYMS[sol[wrap(add(z, D[k]))]]; c = SYMS[sol[wrap(add(z, D[k + 1]))]]
            U.add(tuple(sorted((corner_id(a, k), corner_id(b, k + 2), corner_id(c, k + 4)))))
        for k in range(6):
            w = wrap(add(z, D[(k + 1) % 6]))
            p, q = side_id(a, k), side_id(SYMS[sol[w]], (k + 3) % 6)
            if p != q:
                E.add((min(p, q), max(p, q)))
    return sorted(U), sorted(E)


def classes_from_pairs(E):
    par = list(range(12))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for p, q in E:
        par[f(p)] = f(q)
    m = {}
    return [m.setdefault(f(i), len(m)) for i in range(12)]


def pairs_of_classes(cls):
    return [p for p in PAIRS if cls[p[0]] == cls[p[1]]]


# ---------------------------------------------------------------- query model
class Query:
    def __init__(self, R, grid=0):
        self.R = R
        m = cp_model.CpModel()
        self.m = m
        self.t = [m.NewBoolVar("t%d" % i) for i in range(len(TRIPLES))]
        self.grid = grid
        if grid:
            # exact angle vector on the grid (1/grid degree); t is then exactly
            # the set of 360-triples of this vector (closure automatic)
            K = grid
            self.a = [m.NewIntVar(1, 180 * K - 1, "a%d" % i) for i in range(12)]
            m.Add(sum(self.a[:6]) == 720 * K); m.Add(sum(self.a[6:]) == 720 * K)
            for i, tri in enumerate(TRIPLES):
                expr = sum(self.a[c] for c in tri)
                m.Add(expr == 360 * K).OnlyEnforceIf(self.t[i])
                m.Add(expr != 360 * K).OnlyEnforceIf(self.t[i].Not())
        self.e = [m.NewBoolVar("e%d" % i) for i in range(len(PAIRS))]
        one = m.NewConstant(1)
        def ev(i, j):
            return one if i == j else self.e[PIDX[(min(i, j), max(i, j))]]
        for i, j, k in itertools.permutations(range(12), 3):
            m.AddBoolOr([ev(i, j).Not(), ev(j, k).Not(), ev(i, k)])
        cells = [(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1)
                 if max(abs(x), abs(y), abs(x + y)) <= R]
        cs = set(cells)
        X = {z: m.NewIntVar(0, NS - 1, "x%d_%d" % z) for z in cells}
        self.X = X
        C = {}; Sd = {}
        ctab = [[corner_id(SYMS[i], k) for i in range(NS)] for k in range(6)]
        stab = [[side_id(SYMS[i], k) for i in range(NS)] for k in range(6)]
        def cvar(z, k):
            if (z, k) not in C:
                v = m.NewIntVar(0, 11, ""); m.AddElement(X[z], ctab[k], v); C[(z, k)] = v
            return C[(z, k)]
        def svar(z, k):
            if (z, k) not in Sd:
                v = m.NewIntVar(0, 11, ""); m.AddElement(X[z], stab[k], v); Sd[(z, k)] = v
            return Sd[(z, k)]
        tarr = [self.t[TIDX[tuple(sorted((a, b, c)))]] for a in range(12) for b in range(12) for c in range(12)]
        earr = [ev(a, b) for a in range(12) for b in range(12)]
        for z in cells:
            for k in (0, 1):
                b, c = add(z, D[k]), add(z, D[k + 1])
                if b in cs and c in cs:
                    I = m.NewIntVar(0, 1727, "")
                    m.Add(I == 144 * cvar(z, k) + 12 * cvar(b, k + 2) + cvar(c, (k + 4) % 6))
                    m.AddElement(I, tarr, one)
            for k in range(6):
                w = add(z, D[(k + 1) % 6])
                if w in cs and z < w:
                    I = m.NewIntVar(0, 143, "")
                    m.Add(I == 12 * svar(z, k) + svar(w, (k + 3) % 6))
                    m.AddElement(I, earr, one)
        self.ev = ev
        self.nclauses = 0

    def add_not_all(self, U, E):
        """clause: not (all t in U and all e in E), with all symmetric images."""
        seen = set()
        for g in GROUP:
            key = (tuple(sorted(img_triple(g, t) for t in U)), tuple(sorted(img_pair(g, p) for p in E)))
            if key in seen:
                continue
            seen.add(key)
            lits = [self.t[TIDX[t]].Not() for t in key[0]] + [self.e[PIDX[p]].Not() for p in key[1]]
            self.m.AddBoolOr(lits); self.nclauses += 1

    def add_implication(self, S, tau):
        seen = set()
        for g in GROUP:
            key = (tuple(sorted(img_triple(g, t) for t in S)), img_triple(g, tau))
            if key in seen:
                continue
            seen.add(key)
            self.m.AddBoolOr([self.t[TIDX[t]].Not() for t in key[0]] + [self.t[TIDX[key[1]]]])
            self.nclauses += 1

    def add_escape(self, T0, E0):
        """clause: some triple outside T0 or some pair outside E0 is on."""
        seen = set()
        for g in GROUP:
            T1 = frozenset(img_triple(g, t) for t in T0); E1 = frozenset(img_pair(g, p) for p in E0)
            key = (T1, E1)
            if key in seen:
                continue
            seen.add(key)
            lits = [self.t[i] for i, t in enumerate(TRIPLES) if t not in T1] + \
                   [self.e[i] for i, p in enumerate(PAIRS) if p not in E1]
            self.m.AddBoolOr(lits); self.nclauses += 1

    def solve(self, time_limit, workers=8):
        s = cp_model.CpSolver()
        s.parameters.max_time_in_seconds = time_limit
        s.parameters.num_workers = workers
        st = s.Solve(self.m)
        if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return "SAT", s
        return ("UNSAT" if st == cp_model.INFEASIBLE else "UNKNOWN"), s


def proposal_usage(q, s):
    R = q.R
    sol = {z: s.Value(v) for z, v in q.X.items()}
    cs = set(sol)
    U, E = set(), set()
    for z in sol:
        a = SYMS[sol[z]]
        for k in (0, 1):
            b, c = add(z, D[k]), add(z, D[k + 1])
            if b in cs and c in cs:
                U.add(tuple(sorted((corner_id(a, k), corner_id(SYMS[sol[b]], k + 2), corner_id(SYMS[sol[c]], k + 4)))))
        for k in range(6):
            w = add(z, D[(k + 1) % 6])
            if w in cs:
                p, qq = side_id(a, k), side_id(SYMS[sol[w]], (k + 3) % 6)
                if p != qq:
                    E.add((min(p, qq), max(p, qq)))
    return sorted(U), sorted(E), sol


def main():
    R = int(sys.argv[1]); R2 = int(sys.argv[2]); N = int(sys.argv[3])
    outdir = sys.argv[4]
    maxit = int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 9
    os.makedirs(outdir, exist_ok=True)
    log = open(os.path.join(outdir, "log.jsonl"), "a")
    grid = int(os.environ.get("GRID", "0"))
    q = Query(R, grid)
    tori, cores, implications, empties, candidates = [], [], [], [], []
    t0 = time.time()
    libs = sys.argv[6].split(",") if len(sys.argv) > 6 else []
    for lp in libs:
        if lp.endswith(".jsonl"):
            recs = [json.loads(l) for l in open(lp)]
            items = [(r["U"], r["E"], r["lat"], None) for r in recs if r.get("event") == "torus"]
        else:
            items = json.load(open(lp))
        for U, E, lat, lab in items:
            U = [tuple(t) for t in U]; E = [tuple(p) for p in E]
            S = minimal_generating(U, U)
            tori.append((U, E, tuple(lat)))
            q.add_not_all(S, E)
    print("library records", len(tori), "clauses", q.nclauses, flush=True)
    for it in range(maxit):
        st, s = q.solve(600)
        if st != "SAT":
            print("QUERY", st, "after", it, "iterations", flush=True)
            log.write(json.dumps({"event": "final", "status": st, "it": it}) + "\n")
            break
        U, E, patch = proposal_usage(q, s)
        if grid:
            U = [t for i, t in enumerate(TRIPLES) if s.Value(q.t[i])]
        print("it %d query %.1fs |U|=%d |E|=%d" % (it, s.WallTime(), len(U), len(E)), flush=True)
        ok, core = angle_feasible(U)
        if not ok:
            q.add_not_all(core, []); cores.append(core)
            log.write(json.dumps({"event": "core", "S": core}) + "\n"); log.flush()
            continue
        Tc = closure(U)
        cls = classes_from_pairs(E)
        Ecl = pairs_of_classes(cls)
        cov = None
        for tu, te, _ in tori:
            if closure_contains(U, tu) and eq_closure_contains(E, te):
                cov = (tu, te); break
        if cov is not None:
            S = minimal_generating(U, cov[0]); F = minimal_eq_generating(E, cov[1])
            q.add_not_all(S, F)
            continue
        sft = TypeSFT(Tc, cls)
        lat, sol = sft.tori(N, time=60)
        if lat is not None and lat[0] != "UNKNOWN":
            Ux, Ex = usage(sol, lat)
            tori.append((Ux, Ex, lat))
            S = minimal_generating(U, Ux) if closure_contains(U, Ux) else minimal_generating(Ux, Ux)
            F = minimal_eq_generating(E, Ex) if eq_closure_contains(E, Ex) else Ex
            q.add_not_all(S, F)
            log.write(json.dumps({"event": "torus", "U": Ux, "E": Ex, "lat": list(lat),
                                  "sol": {"%d,%d" % z: v for z, v in sol.items()},
                                  "T": Tc, "cls": cls}) + "\n"); log.flush()
            print("it %d torus#%d lat=%s |U|=%d |E|=%d clauses=%d  %.0fs" % (it, len(tori), lat, len(Ux), len(Ex), q.nclauses, time.time() - t0), flush=True)
            continue
        st2, _ = sft.patch(R2, time=120)
        if st2 == "UNSAT":
            q.add_escape(Tc, Ecl); empties.append((Tc, Ecl))
            log.write(json.dumps({"event": "empty", "R2": R2, "T": Tc, "E": Ecl}) + "\n"); log.flush()
            print("it %d empty#%d |T|=%d |E|=%d" % (it, len(empties), len(Tc), len(Ecl)), flush=True)
            continue
        q.add_escape(Tc, Ecl); candidates.append((Tc, Ecl, st2))
        log.write(json.dumps({"event": "candidate", "R2": R2, "patch": st2, "T": Tc, "E": Ecl, "cls": cls, "torus_search": str(lat)}) + "\n"); log.flush()
        print("it %d CANDIDATE#%d |T|=%d |E|=%d patchR2=%s torus=%s" % (it, len(candidates), len(Tc), len(Ecl), st2, lat), flush=True)
    print("summary tori=%d cores=%d empties=%d candidates=%d" % (len(tori), len(cores), len(empties), len(candidates)))


if __name__ == "__main__":
    main()
