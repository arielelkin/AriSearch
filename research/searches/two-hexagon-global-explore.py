#!/usr/bin/env python3
"""Random seeded exploration of two-hexagon vertex-star SFTs.

A seed is a random labelled patch P (cells of the triangular lattice with
placement symbols).  We impose exactly the angle-sum and length equalities
needed for P to be legal, pick an exact rational-degree angle point in the
relative interior of the resulting angle flat, a length point in the relative
interior of the resulting length cone, read off the *actual* type of that
concrete pair, and test its SFT:

  * patch(R): does a legal patch of hex-radius R exist?
  * tori(N):  does a legal torus of index <= N exist?

Exploration only; nothing here is used as a proof except the exact torus
certificates (which are re-checked by check_torus and by the developer).
"""
import sys, os, json, random, math, itertools, importlib.util
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.optimize import linprog

_here = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_here, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
S_ = _load("thg_sft", "two-hexagon-global-sft.py")
G_ = _load("thg_geo", "two-hexagon-global-geometry.py")
SYMS = S_.symbols()


def var(t, i):
    return 6 * t + i


def patch_constraints(patch):
    """angle triples (list of 3 corner-vars) and length equalities (pairs)."""
    triples, leq = [], set()
    for z in patch:
        for k in (0, 1):
            a, b, c = z, S_.add(z, S_.D[k]), S_.add(z, S_.D[k + 1])
            if a in patch and b in patch and c in patch:
                A, B, C = SYMS[patch[a]], SYMS[patch[b]], SYMS[patch[c]]
                triples.append(tuple(sorted((var(A[0], S_.corner_at(A, k)),
                                             var(B[0], S_.corner_at(B, k + 2)),
                                             var(C[0], S_.corner_at(C, k + 4))))))
        for k in range(6):
            w = S_.add(z, S_.D[(k + 1) % 6])
            if w in patch:
                A, B = SYMS[patch[z]], SYMS[patch[w]]
                p = var(A[0], S_.side_at(A, k)); q = var(B[0], S_.side_at(B, (k + 3) % 6))
                if p != q:
                    leq.add((min(p, q), max(p, q)))
    return sorted(set(triples)), sorted(leq)


def angle_point(triples, rng, margin=Fr(1, 1)):
    """exact rational point (degrees) on the flat {sums=720, triples=360},
    strictly inside (0,180), chosen near a random relative-interior point."""
    rows, rhs = [], []
    for t in range(2):
        r = [0] * 12
        for i in range(6): r[var(t, i)] = 1
        rows.append(r); rhs.append(720)
    for tr in triples:
        r = [0] * 12
        for v in tr: r[v] += 1
        rows.append(r); rhs.append(360)
    A = sp.Matrix(rows); b = sp.Matrix(rhs)
    # LP: maximise margin
    Aeq = np.array(rows, float); beq = np.array(rhs, float)
    pts = []
    for trial in range(4):
        c = np.zeros(13); c[12] = -1.0
        c[:12] = rng.normal(size=12) * 1e-3
        Aub = []; bub = []
        for i in range(12):
            r = np.zeros(13); r[i] = -1; r[12] = 1; Aub.append(r); bub.append(0)
            r = np.zeros(13); r[i] = 1; r[12] = 1; Aub.append(r); bub.append(180)
        res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub),
                      A_eq=np.hstack([Aeq, np.zeros((len(rows), 1))]), b_eq=beq,
                      bounds=[(None, None)] * 12 + [(0, 60)], method="highs")
        if res.status != 0 or res.x[12] < 1e-6:
            return None
        pts.append(res.x[:12])
    x0 = np.mean(pts, axis=0)
    # exact: particular solution + nullspace, rounded coordinates
    sol, params = A.gauss_jordan_solve(b)
    free = sorted(params, key=lambda s: str(s))
    # least squares for parameter values
    if free:
        J = np.array([[float(sp.diff(e, p)) for p in free] for e in sol], float)
        base = np.array([float(e.subs({p: 0 for p in free})) for e in sol], float)
        tv, *_ = np.linalg.lstsq(J, x0 - base, rcond=None)
        for den in (1, 2, 3, 5, 7, 11, 13):
            jit = [Fr(round(float(v) * den * 7 + rng.integers(-3, 4)), den * 7) for v in tv]
            ang = [sp.nsimplify(e.subs(dict(zip(free, jit)))) for e in sol]
            ang = [Fr(int(sp.fraction(a)[0]), int(sp.fraction(a)[1])) for a in ang]
            if all(0 < a < 180 for a in ang):
                return ang
        return None
    ang = [Fr(int(sp.fraction(e)[0]), int(sp.fraction(e)[1])) for e in sol]
    return ang if all(0 < a < 180 for a in ang) else None


def length_point(angles, leq, rng):
    """random relative-interior positive length vector satisfying closure and
    the equalities; returns (lengths, classes) or None."""
    rows = []
    for t in range(2):
        M = G_.closure_matrix(angles[6 * t:6 * t + 6])
        for r in M:
            row = np.zeros(12); row[6 * t:6 * t + 6] = r; rows.append(row)
    for p, q in leq:
        row = np.zeros(12); row[p] = 1; row[q] = -1; rows.append(row)
    Aeq = np.array(rows)
    pts = []
    for trial in range(6):
        c = np.zeros(13); c[12] = -1; c[:12] = rng.normal(size=12) * 1e-3
        Aub = []; bub = []
        for i in range(12):
            r = np.zeros(13); r[i] = -1; r[12] = 1; Aub.append(r); bub.append(0)
        res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub),
                      A_eq=np.vstack([np.hstack([Aeq, np.zeros((len(rows), 1))]),
                                      np.hstack([np.ones(12), [0]])]),
                      b_eq=np.concatenate([np.zeros(len(rows)), [12.0]]),
                      bounds=[(None, None)] * 12 + [(0, 1)], method="highs")
        if res.status != 0 or res.x[12] < 1e-5:
            return None
        pts.append(res.x[:12])
    w = rng.dirichlet(np.ones(len(pts)))
    L = sum(wi * p for wi, p in zip(w, pts))
    # implied equalities: e_i-e_j in row space of Aeq
    U, sv, Vt = np.linalg.svd(Aeq)
    rank = int((sv > 1e-9).sum())
    Nsp = Vt[rank:]
    cls = list(range(12))
    for i in range(12):
        for j in range(i):
            if np.linalg.norm(Nsp[:, i] - Nsp[:, j]) < 1e-8 if Nsp.size else True:
                cls[i] = cls[j]; break
    # canonical relabel
    m = {}
    lab = [m.setdefault(c, len(m)) for c in cls]
    return L, lab


def random_patch(rng, kind):
    cells = [(0, 0)] + [S_.D[k] for k in range(6)]
    if kind == "star":
        cells = [(0, 0), (1, 0), (0, 1)]
    if kind == "big":
        cells = [(x, y) for x in range(-2, 3) for y in range(-2, 3) if max(abs(x), abs(y), abs(x + y)) <= 2]
        cells = [z for z in cells if rng.random() < 0.6 or z == (0, 0)]
    if kind == "pair":
        cells = [(0, 0), (1, 0), (0, 1), (1, -1)]
    return {z: int(rng.integers(0, 24)) for z in cells}


def run(seed, nseeds, kind, R, N, out):
    rng = np.random.default_rng(seed)
    stats = {}
    found = []
    for it in range(nseeds):
        P = random_patch(rng, kind)
        tr, leq = patch_constraints(P)
        ang = angle_point(tr, rng)
        if ang is None:
            stats["angle_infeasible"] = stats.get("angle_infeasible", 0) + 1; continue
        lp = length_point(ang, leq, rng)
        if lp is None:
            stats["length_infeasible"] = stats.get("length_infeasible", 0) + 1; continue
        L, lab = lp
        angles = [ang[:6], ang[6:]]
        lcls = [lab[:6], lab[6:]]
        sft = S_.SFT(angles, lcls)
        st, _ = sft.patch(R, time=30)
        if st != "SAT":
            stats["patch_" + st] = stats.get("patch_" + st, 0) + 1; continue
        mono = [sft.patch(R, time=30, only={t})[0] for t in (0, 1)]
        if "SAT" in mono:
            stats["mono_patch"] = stats.get("mono_patch", 0) + 1; continue
        lat, sol = sft.tori(N, time=30)
        rec = {"angles": [[str(a) for a in row] for row in angles], "lclass": lcls,
               "lengths": [list(map(float, L[:6])), list(map(float, L[6:]))],
               "seed_patch": {"%d,%d" % z: v for z, v in P.items()}}
        if lat is None or (isinstance(lat, tuple) and lat[0] == "UNKNOWN"):
            stats["no_torus"] = stats.get("no_torus", 0) + 1
            rec["torus"] = str(lat)
            found.append(rec)
            print("CANDIDATE", json.dumps(rec), flush=True)
        else:
            assert S_.check_torus(sft, lat, sol)
            used = sorted({SYMS[v][0] for v in sol.values()})
            key = "torus_types_" + "".join("AB"[u] for u in used)
            stats[key] = stats.get(key, 0) + 1
            # geometric replay of the torus
            _, err = G_.develop(sft, angles, [L[:6], L[6:]], G_.unwrap(lat, sol, 4))
            if err > 1e-6:
                print("DEVELOP-ERROR", err, json.dumps(rec), flush=True)
                stats["develop_error"] = stats.get("develop_error", 0) + 1
    print(json.dumps(stats), flush=True)
    if out:
        with open(out, "w") as f:
            json.dump({"stats": stats, "candidates": found}, f, indent=1)


if __name__ == "__main__":
    seed = int(sys.argv[1]); n = int(sys.argv[2]); kind = sys.argv[3]
    R = int(sys.argv[4]); N = int(sys.argv[5])
    out = sys.argv[6] if len(sys.argv) > 6 else None
    run(seed, n, kind, R, N, out)
