#!/usr/bin/env python3
"""Bounded exact inverse search for homothetic two-tile convex substitutions,
angles in units pi/N (N in {4,5,6}), sides in Z[w] (w = sqrt2, phi, sqrt3).

For each N the exact finite domain is:
  * A: a convex pentagon whose angle word has no adjacent supplementary pair
    (otherwise Rao type 1 => tiles alone) -- free sides 2,3,4 from ALPH[N];
  * B: such a pentagon, or (with --hexagons) any convex hexagon word with
    free sides 2..5 from HALPH[N];
  * sides 0,1 solved exactly from closure (must be positive and in Z[w]);
    all free lengths multiplied by SCALE[N] so the solved sides are integral;
  * neither shape tiles alone (Rao Table 2 / Reinhardt; conservative);
  * lambda in LAMBDAS[N] (lambda in Z[w], lambda^2 irrational);
  * every nonnegative integer M with char poly = min poly of lambda^2, total
    children per parent <= maxchildren;
  * area eigen-relation exact, every parent side a whole-child-side knapsack,
    every parent angle a sum of child angles;
  * complete corner-filling dissection search of lambda*A then lambda*B, each
    with a node limit (limit hits are reported as UNKNOWN, never as negative).
Usage: python3 convex-substitution-cyclotomic.py --N 6 [--hexagons]
       [--heptagons] [--maxchildren 20] [--nodes 20000] [--output FILE]
  --heptagons adds convex heptagon partners (free sides 2..6 from H7ALPH[N]).
"""
import argparse, importlib.util, json, sys, time
from itertools import product
from pathlib import Path

def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(fname))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
core = _load("cs_core", "convex-substitution-core.py")
shp = _load("cs_shapes", "convex-substitution-shapes.py")
shp.core = core  # share configured module state

ALPH = {
    5: [(1, 0), (0, 1), (1, 1), (2, 0), (1, 2), (2, 1), (0, 2), (2, 2), (-1, 1), (2, -1)],
    6: [(1, 0), (0, 1), (2, 0), (1, 1), (2, 1), (0, 2), (3, 0), (1, 2), (3, 1), (2, 2)],
    4: [(1, 0), (0, 1), (2, 0), (1, 1), (2, 1), (0, 2), (3, 0), (1, 2), (3, 1), (2, 2)],
}
HALPH = {5: [(1, 0), (0, 1), (1, 1), (2, 0), (-1, 1), (0, 2)],
         6: [(1, 0), (0, 1), (2, 0), (1, 1), (2, 1), (0, 2)],
         4: [(1, 0), (0, 1), (2, 0), (1, 1), (2, 1), (0, 2)]}
H7ALPH = {5: [(1, 0), (0, 1), (1, 1), (-1, 1), (2, 0)], 6: [(1, 0), (0, 1), (2, 0), (1, 1)],
          4: [(1, 0), (0, 1), (2, 0), (1, 1)]}
SCALE = {5: 2, 6: 12, 4: 4}
LAMBDAS = {
    5: {"phi": (0, 1), "phi^2": (1, 1), "2phi": (0, 2), "2+phi": (2, 1), "phi^3": (1, 2)},
    6: {"1+r3": (1, 1), "2+r3": (2, 1), "3+r3": (3, 1), "2+2r3": (2, 2), "1+2r3": (1, 2)},
    4: {"1+r2": (1, 1), "2+r2": (2, 1), "1+2r2": (1, 2), "2+2r2": (2, 2), "3+r2": (3, 1), "3+2r2": (3, 2)},
}
WNAME = {5: "phi", 6: "sqrt3", 4: "sqrt2"}

def zs(u): return f"{u[0]}+{u[1]}{WNAME[core.HALF]}"

def canonical(w, L):
    n = len(w); reps = []
    for s in range(n):
        reps.append((tuple(w[s:] + w[:s]), tuple(L[s:] + L[:s])))
        rw = tuple(w[(-i + s) % n] for i in range(n))
        rl = tuple(L[(-i - 1 + s) % n] for i in range(n))
        reps.append((rw, rl))
    return min(reps)

def enumerate_shapes(words, alphabet, scale):
    out = []
    for name, w in words.items():
        n = len(w); seen = set()
        for free in product(alphabet, repeat=n - 2):
            L = shp.solve_closure(w, [core.zscale(scale, x) for x in free])
            if L is None: continue
            key = canonical(w, L)
            if key in seen: continue
            seen.add(key)
            if n == 5: alone = shp.pentagon_tiles_alone(w, L)
            elif n == 6: alone = shp.hexagon_tiles_alone(w, L)
            else: alone = None   # convex n>=7 never tiles alone
            if alone is not None: continue
            pts = core.polygon_from_word(w, L)
            out.append({"word": name, "angles": w, "lengths": L, "pts": pts,
                        "area": core.area4(pts), "key": key})
    return out

def char_poly(lam2):
    s, t = lam2
    if core.Q1 == 1: return 2 * s + t, s * s + s * t - t * t
    return 2 * s, s * s - core.Q0 * t * t

def matrices(lam, maxchildren):
    tr, det = char_poly(core.zmul(lam, lam))
    out = []
    for m11 in range(tr + 1):
        m22 = tr - m11; P = m11 * m22 - det
        if P <= 0: continue
        for m21 in range(1, P + 1):
            if P % m21: continue
            m12 = P // m21
            if m11 + m21 <= maxchildren and m12 + m22 <= maxchildren:
                out.append((m11, m12, m21, m22))
    return out

def knapsack(target, lengths, limit=100000):
    seen = {core.ZERO}; frontier = [core.ZERO]
    while frontier:
        nxt = []
        for v in frontier:
            for L in lengths:
                w = core.zadd(v, L); c = core.zsign(core.zsub(target, w))
                if c == 0: return True
                if c > 0 and w not in seen:
                    seen.add(w); nxt.append(w)
                    if len(seen) > limit: return True   # inconclusive: do not filter
        frontier = nxt
    return False

def angle_fill(alpha, angles):
    reach = {0}
    for _ in range(alpha):
        reach |= {r + a for r in reach for a in angles if r + a <= alpha}
    return alpha in reach

def boundary_ok(lam, P, Q):
    lens = sorted(set(P["lengths"]) | set(Q["lengths"]))
    angs = set(P["angles"]) | set(Q["angles"])
    for X in (P, Q):
        for L in set(X["lengths"]):
            if not knapsack(core.zmul(lam, L), lens): return False
        for a in set(X["angles"]):
            if not angle_fill(a, angs): return False
    return True

def run(a):
    N = a.N; core.configure(N)
    t0 = time.time()
    pw = {"P" + "".join(map(str, w)): w for w in shp.cyclic_words(5, 3 * N, N - 1)
          if not shp.adjacent_supplementary(w, N)}
    pents = enumerate_shapes(pw, ALPH[N], SCALE[N])
    Bs = list(pents)
    hw = {}
    if a.hexagons:
        hw = {"H" + "".join(map(str, w)): w for w in shp.cyclic_words(6, 4 * N, N - 1)}
        Bs += enumerate_shapes(hw, HALPH[N], SCALE[N])
    if a.heptagons:
        h7 = {"S" + "".join(map(str, w)): w for w in shp.cyclic_words(7, 5 * N, N - 1)}
        hw.update(h7)
        Bs += enumerate_shapes(h7, H7ALPH[N], SCALE[N])
    stats = {"N": N, "pentagon_words": pw, "hexagon_words": len(hw),
             "pentagons_not_alone": len(pents), "B_not_alone": len(Bs)}
    print(json.dumps(stats), file=sys.stderr, flush=True)
    by_area = {}
    for i, Q in enumerate(Bs): by_area.setdefault(Q["area"], []).append(i)
    recs = []; area_pass = 0
    for lname, lam in LAMBDAS[N].items():
        lam2 = core.zmul(lam, lam)
        for (m11, m12, m21, m22) in matrices(lam, a.maxchildren):
            for P in pents:
                A = P["area"]; num = core.zmul(core.zsub(lam2, (m11, 0)), A)
                if num[0] % m21 or num[1] % m21: continue
                b = (num[0] // m21, num[1] // m21)
                for j in by_area.get(b, []):
                    Q = Bs[j]
                    if Q["key"] == P["key"]: continue
                    if core.zmul(lam2, b) != core.zadd(core.zscale(m12, A), core.zscale(m22, b)): continue
                    area_pass += 1
                    if boundary_ok(lam, P, Q):
                        recs.append((lname, (m11, m12, m21, m22), P, Q))
    stats.update(area_pass=area_pass, boundary_pass=len(recs))
    print(json.dumps({k: stats[k] for k in ("area_pass", "boundary_pass")}), file=sys.stderr, flush=True)
    results = []
    for lname, (m11, m12, m21, m22), P, Q in recs:
        lam = LAMBDAS[N][lname]
        shapes = {"A": P["pts"], "B": Q["pts"]}
        out = {"lambda": lname, "children_of_A": [m11, m21], "children_of_B": [m12, m22],
               "A": {"word": P["word"], "lengths": [zs(x) for x in P["lengths"]]},
               "B": {"word": Q["word"], "lengths": [zs(x) for x in Q["lengths"]]}}
        for pname, X, cnt in (("A", P, {"A": m11, "B": m21}), ("B", Q, {"A": m12, "B": m22})):
            par = [core.pscale(lam, p) for p in X["pts"]]
            D = core.Dissector(par, shapes, cnt, node_limit=a.nodes, want=1)
            sols = D.run()
            out[pname + "_parent"] = {"nodes": D.nodes, "limit_hit": D.limit_hit, "found": bool(sols),
                                      "solution": [[n, [list(p) for p in pts]] for n, pts in sols[0]] if sols else None}
            if not sols: break
        results.append(out)
        if any(v.get("found") or v.get("limit_hit") for k, v in out.items() if k.endswith("_parent")):
            print(json.dumps({k: out[k] for k in ("lambda", "children_of_A", "children_of_B", "A", "B")}),
                  {k: (v["found"], v["limit_hit"], v["nodes"]) for k, v in out.items() if k.endswith("_parent")},
                  file=sys.stderr, flush=True)
    summ = {"exhausted_negative": 0, "unknown_limit": 0, "A_parent_found": 0, "both_found": 0}
    for r in results:
        if "B_parent" in r and r["B_parent"]["found"]: summ["both_found"] += 1
        if r["A_parent"]["found"]: summ["A_parent_found"] += 1
        if any(r[k]["limit_hit"] for k in ("A_parent", "B_parent") if k in r): summ["unknown_limit"] += 1
        elif not ("B_parent" in r and r["B_parent"]["found"]): summ["exhausted_negative"] += 1
    stats["outcome"] = summ
    from collections import Counter
    stats["A_parent_node_histogram"] = sorted(Counter(r["A_parent"]["nodes"] for r in results).items())
    stats["pairs_by_word_and_lambda"] = sorted(Counter((r["A"]["word"], r["B"]["word"], r["lambda"]) for r in results).items())
    if a.compact:
        results = [r for r in results if r["A_parent"]["found"] or r["A_parent"]["limit_hit"]]
    print(json.dumps(stats["outcome"]), file=sys.stderr, flush=True)
    return {"stats": stats, "elapsed_s": round(time.time() - t0, 1),
            "alphabet": [zs(x) for x in ALPH[N]], "hex_alphabet": [zs(x) for x in HALPH[N]],
            "scale": SCALE[N], "lambdas": {k: zs(v) for k, v in LAMBDAS[N].items()},
            "maxchildren": a.maxchildren, "node_limit": a.nodes, "results": results}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=5)
    ap.add_argument("--hexagons", action="store_true")
    ap.add_argument("--heptagons", action="store_true")
    ap.add_argument("--maxchildren", type=int, default=20)
    ap.add_argument("--nodes", type=int, default=20000)
    ap.add_argument("--output")
    ap.add_argument("--compact", action="store_true", help="retain only found / limit-hit records")
    a = ap.parse_args()
    res = run(a)
    txt = json.dumps(res, indent=1, default=str)
    if a.output: Path(a.output).write_text(txt)
    else: print(txt)
