#!/usr/bin/env python3
"""Bounded exact inverse search for homothetic two-tile convex substitutions
with all angles in pi/5 units and all sides in Z[phi].

Domain (all exact):
  * shape A: pentagon word in {U,V,W} (the only pi/5 pentagon words without an
    adjacent supplementary pair; every other word is Rao type 1 and tiles alone);
  * shape B: pentagon word in {U,V,W} or any convex pi/5 hexagon word;
  * free side lengths (sides 2..n-1) from ALPHABET (times 2), sides 0,1 solved;
  * lambda in LAMBDAS (elements of Z[phi], lambda^2 irrational);
  * M any nonnegative integer 2x2 matrix with characteristic polynomial the
    minimal polynomial of lambda^2 (forced: area ratio is irrational).
Filters in order: monohedral (Rao / Reinhardt), exact area eigen-relation,
whole-side boundary knapsack for every parent side, complete corner-filling
dissection search (node-limited; limit hits are reported, not treated as
negative).

Usage: python3 convex-substitution-pentagrid.py [--hexagons] [--maxchildren N]
            [--nodes N] [--output FILE]
"""
import argparse, importlib.util, json, sys, time
from itertools import product
from pathlib import Path

def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(fname))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
core = _load("cs_core", "convex-substitution-core.py")
shp = _load("cs_shapes", "convex-substitution-shapes.py")

ALPHABET = [(1, 0), (0, 1), (1, 1), (2, 0), (1, 2), (2, 1), (0, 2), (2, 2), (-1, 1), (2, -1)]
#            1      phi     phi^2   2      phi^3   2+phi   2phi    2phi^2  1/phi   1/phi^2
LAMBDAS = {"phi": (0, 1), "phi^2": (1, 1), "2phi": (0, 2), "2+phi": (2, 1), "phi^3": (1, 2)}
PENT_WORDS = {"U": (1, 3, 4, 4, 3), "V": (2, 2, 4, 3, 4), "W": (3, 3, 3, 3, 3)}

def zs(u): return f"{u[0]}+{u[1]}phi"

def enumerate_shapes(words, nfree):
    out = []
    for name, w in words.items():
        n = len(w)
        seen = set()
        for free in product(ALPHABET, repeat=n - 2):
            free2 = [core.zscale(2, x) for x in free]
            L = shp.solve_closure(w, free2)
            if L is None: continue
            pts = core.polygon_from_word(w, L)
            key = canonical(w, L)
            if key in seen: continue
            seen.add(key)
            if n == 5: alone = shp.pentagon_tiles_alone(w, L)
            else: alone = shp.hexagon_tiles_alone(w, L)
            out.append({"word": name, "angles": w, "lengths": L, "pts": pts,
                        "area": core.area4(pts), "alone": alone})
    return out

def canonical(w, L):
    n = len(w); reps = []
    for s in range(n):
        reps.append((tuple(w[s:] + w[:s]), tuple(L[s:] + L[:s])))
        # reversal: vertex i -> -i, side i (i,i+1) -> side (-i-1)
        rw = tuple(w[(-i + s) % n] for i in range(n))
        rl = tuple(L[(-i - 1 + s) % n] for i in range(n))
        reps.append((rw, rl))
    return min(reps)

def matrices(lam, maxchildren):
    s, t = core.zmul(lam, lam)
    tr = 2 * s + t; det = s * s + s * t - t * t
    out = []
    for m11 in range(tr + 1):
        m22 = tr - m11
        P = m11 * m22 - det
        if P <= 0: continue
        for m21 in range(1, P + 1):
            if P % m21: continue
            m12 = P // m21
            if m11 + m21 <= maxchildren and m12 + m22 <= maxchildren:
                out.append((m11, m12, m21, m22))
    return out

def zdiv_int(u, k):
    if u[0] % k or u[1] % k: return None
    return (u[0] // k, u[1] // k)

def knapsack(target, lengths, limit=200000):
    """is target a nonnegative integer combination of lengths (all Z[phi]>0)?"""
    seen = {core.ZERO}; frontier = [core.ZERO]
    while frontier:
        nxt = []
        for v in frontier:
            for L in lengths:
                w = core.zadd(v, L)
                c = core.zsign(core.zsub(target, w))
                if c == 0: return True
                if c > 0 and w not in seen:
                    seen.add(w); nxt.append(w)
                    if len(seen) > limit: return True  # inconclusive -> do not filter
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

def run(args):
    t0 = time.time()
    words = dict(PENT_WORDS)
    pents = enumerate_shapes(PENT_WORDS, 3)
    shapes_B = list(pents)
    hexwords = {}
    if args.hexagons:
        for w in shp.cyclic_words(6, 20):
            hexwords["H" + "".join(map(str, w))] = w
        shapes_B = shapes_B + enumerate_shapes(hexwords, 4)
    stats = {"pentagons": len(pents), "B_shapes": len(shapes_B)}
    A_ok = [P for P in pents if P["alone"] is None]
    B_ok = [Q for Q in shapes_B if Q["alone"] is None]
    stats["pentagons_not_alone"] = len(A_ok); stats["B_not_alone"] = len(B_ok)
    by_area = {}
    for i, Q in enumerate(B_ok):
        by_area.setdefault(Q["area"], []).append(i)
    records = []; area_pass = 0; boundary_pass = 0
    for lname, lam in LAMBDAS.items():
        lam2 = core.zmul(lam, lam)
        for (m11, m12, m21, m22) in matrices(lam, args.maxchildren):
            for P in A_ok:
                a = P["area"]
                num = core.zmul(core.zsub(lam2, (m11, 0)), a)
                b = zdiv_int(num, m21)
                if b is None or b not in by_area: continue
                for j in by_area[b]:
                    Q = B_ok[j]
                    if Q is P: continue
                    # second eigen-equation
                    lhs = core.zmul(lam2, b)
                    rhs = core.zadd(core.zscale(m12, a), core.zscale(m22, b))
                    if lhs != rhs: continue
                    if len(Q["angles"]) == 5 and canonical(Q["angles"], Q["lengths"]) <= canonical(P["angles"], P["lengths"]):
                        continue  # unordered pentagon pairs: keep one order... both roles tested below
                    area_pass += 1
                    if not boundary_ok(lam, P, Q): continue
                    boundary_pass += 1
                    records.append({"lambda": lname, "M": [m11, m12, m21, m22],
                                    "A": P, "B": Q})
    stats.update(area_pass=area_pass, boundary_pass=boundary_pass)
    print(json.dumps(stats), file=sys.stderr)
    results = []
    for rec in records:
        lam = LAMBDAS[rec["lambda"]]
        m11, m12, m21, m22 = rec["M"]
        P, Q = rec["A"], rec["B"]
        shapes = {"A": P["pts"], "B": Q["pts"]}
        out = {"lambda": rec["lambda"], "M_children_of_A": [m11, m21], "M_children_of_B": [m12, m22],
               "A": {"word": P["word"], "angles": P["angles"], "lengths": [zs(x) for x in P["lengths"]]},
               "B": {"word": Q["word"], "angles": Q["angles"], "lengths": [zs(x) for x in Q["lengths"]]}}
        for parent_name, X, cnt in (("A", P, {"A": m11, "B": m21}), ("B", Q, {"A": m12, "B": m22})):
            par = [core.pscale(lam, p) for p in X["pts"]]
            D = core.Dissector(par, shapes, cnt, node_limit=args.nodes, want=1)
            sols = D.run()
            out[parent_name + "_parent"] = {"nodes": D.nodes, "limit_hit": D.limit_hit,
                                             "found": len(sols) > 0,
                                             "solution": [[n, [list(p) for p in pts]] for n, pts in sols[0]] if sols else None}
            if not sols and not D.limit_hit:
                break  # exhaustively impossible for this parent
        results.append(out)
        print(json.dumps({k: out[k] for k in ("lambda", "M_children_of_A", "M_children_of_B", "A", "B")}),
              {k: (v["found"], v["limit_hit"], v["nodes"]) for k, v in out.items() if k.endswith("_parent")},
              file=sys.stderr)
    summary = {"stats": stats, "elapsed_s": round(time.time() - t0, 1),
               "alphabet": [zs(x) for x in ALPHABET], "lambdas": {k: zs(v) for k, v in LAMBDAS.items()},
               "maxchildren": args.maxchildren, "node_limit": args.nodes, "results": results}
    return summary

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--hexagons", action="store_true")
    ap.add_argument("--maxchildren", type=int, default=20)
    ap.add_argument("--nodes", type=int, default=200000)
    ap.add_argument("--output")
    a = ap.parse_args()
    res = run(a)
    txt = json.dumps(res, indent=1, default=str)
    if a.output: Path(a.output).write_text(txt)
    else: print(txt)
