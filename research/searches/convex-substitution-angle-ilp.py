#!/usr/bin/env python3
"""Length-independent angle-incidence relaxation for a homothetic dissection.

Question: can the convex parent with angle word P (units pi/N) be partitioned
into nA convex children with angle word WA and nB with word WB, for SOME side
lengths?  Necessary integer conditions (see convex-substitution-search.md and
research/lemmas/convex-substitution-dissection-euler.md):

  * every planarized vertex is a parent corner (child angles sum to that
    corner), a half vertex (boundary-flat or T-junction; child corners sum to
    pi, >= 2 corners) or a full vertex (sum 2pi, >= 3 corners);
  * every child corner is used exactly once (aggregated by angle value);
  * Euler (F): 2F = 2 + H + V_f + X, F = nA + nB, X = total corner excess.

Variables are counts of vertex configurations (multisets of child angles).
CP-SAT decides feasibility exactly (pure integer model; no time limit is hit
in the recorded runs -- status is recorded).  Infeasible => no dissection for
any lengths with these words and counts.

Usage: python3 convex-substitution-angle-ilp.py --N 5 [--maxchildren 40] [--output F]
"""
import argparse, importlib.util, json, sys
from functools import lru_cache
from pathlib import Path
from ortools.sat.python import cp_model

def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(fname))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def multisets(target, values, mincount):
    vals = sorted(set(values))
    out = []
    def rec(i, rem, cur):
        if rem == 0:
            if len(cur) >= mincount: out.append(tuple(cur))
            return
        if i == len(vals): return
        v = vals[i]
        k = 0
        while k * v <= rem:
            rec(i + 1, rem - k * v, cur + [v] * k)
            k += 1
    rec(0, target, [])
    return out

def feasible(N, P, WA, WB, nA, nB):
    vals = sorted(set(WA) | set(WB)) if nB else sorted(set(WA))
    if nA == 0: vals = sorted(set(WB))
    supply = {v: nA * WA.count(v) + nB * WB.count(v) for v in vals}
    m = cp_model.CpModel()
    use = {v: [] for v in vals}
    excess = []
    # parent corners: exactly one configuration each
    for i, alpha in enumerate(P):
        confs = multisets(alpha, vals, 1)
        if not confs: return False
        xs = [m.NewBoolVar(f"c{i}_{j}") for j in range(len(confs))]
        m.Add(sum(xs) == 1)
        for x, c in zip(xs, confs):
            for v in vals:
                if c.count(v): use[v].append((c.count(v), x))
            excess.append((len(c) - 1, x))
    F = nA + nB
    ub = 4 * F * max(len(WA), len(WB)) + 10
    H = 0; Vf = 0
    for target, mc, kind in ((N, 2, "h"), (2 * N, 3, "f")):
        for j, c in enumerate(multisets(target, vals, mc)):
            y = m.NewIntVar(0, ub, f"{kind}{j}")
            for v in vals:
                if c.count(v): use[v].append((c.count(v), y))
            excess.append((len(c) - mc, y))
            if kind == "h": H = H + y
            else: Vf = Vf + y
    for v in vals:
        m.Add(sum(k * x for k, x in use[v]) == supply[v])
    m.Add(2 * F == 2 + H + Vf + sum(k * x for k, x in excess))
    s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = 60
    st = s.Solve(m)
    if st == cp_model.INFEASIBLE: return False
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL): return True
    return None  # unknown

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=5)
    ap.add_argument("--maxchildren", type=int, default=40)
    ap.add_argument("--output")
    a = ap.parse_args()
    shp = _load("cs_shapes", "convex-substitution-shapes.py")
    N = a.N
    pw = [w for w in shp.cyclic_words(5, 3 * N, N - 1) if not shp.adjacent_supplementary(w, N)]
    hw = shp.cyclic_words(6, 4 * N, N - 1)
    words = {"P" + "".join(map(str, w)): w for w in pw}
    words.update({"H" + "".join(map(str, w)): w for w in hw})
    res = {}
    names = list(words)
    for na in names:
        if not na.startswith("P"): continue          # A is always a pentagon
        for nb in names:
            for parent in (na, nb):
                key = f"{na}|{nb}|parent={parent}"
                feas = []; unknown = []
                for nA in range(0, a.maxchildren + 1):
                    for nB in range(0, a.maxchildren + 1 - nA):
                        if nA + nB < 2: continue
                        if na == nb and nB: continue   # same word: treat as one word
                        f = feasible(N, words[parent], words[na], words[nb], nA, nB)
                        if f is None: unknown.append([nA, nB])
                        elif f: feas.append([nA, nB])
                res[key] = {"feasible_counts": feas, "unknown": unknown}
        print(na, file=sys.stderr, flush=True)
    out = {"N": N, "maxchildren": a.maxchildren, "words": words, "results": res}
    txt = json.dumps(out)
    if a.output: Path(a.output).write_text(txt)
    else: print(txt)

if __name__ == "__main__":
    main()
