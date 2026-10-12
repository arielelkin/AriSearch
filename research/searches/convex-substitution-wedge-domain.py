#!/usr/bin/env python3
"""All-lambda classification of a finite exact domain of pi/5 pentagon pairs
by the local wedge obstruction plus explicit small-lambda searches.

Domain: pentagons with words U,V,W (the only pi/5 words without adjacent
supplementary angles), free sides 2,3,4 from ALPH (times 2), sides 0,1 solved,
neither tiling alone (Rao).  Unordered pairs {P,Q} of distinct shapes whose
area ratio r = area(Q)/area(P) is irrational, positive, with NEGATIVE Galois
conjugate (necessary and sufficient for the existence of a nonnegative integer
M with an eigenvector (1,r) and irrational Perron root; see search record).
For each such pair and each parent X in {P,Q}:
  1. wedge test at each corner angle of X (smallest first) with shapes {P,Q};
  2. if a corner c is 'dead' with certified radius R*, lambda*X has no
     dissection when lambda*h_c > R* (h_c = distance of c to the chord of its
     neighbours);
  3. list every lambda in Z[phi] with lambda <= R*/h_c compatible with r
     (lambda^2 = m11 + m21 r, nonnegative integer M) and run the complete exact
     dissection search of lambda*X with those counts (node limit recorded).
A pair is ALL-LAMBDA EXCLUDED when some parent X has all small-lambda runs
exhausted negative.  Lambda in Z[phi] is forced: lambda*side is a sum of sides
in Z[phi], lambda^2 is an algebraic integer.
Env: CS_N=5|6 (angle unit pi/N), CS_HEX=none|tiny (add hexagon partners with
free sides 2..5 from a 4-value alphabet; hexagon-hexagon pairs are skipped by
research/lemmas/convex-substitution-dissection-euler.md item 2).
Usage: [CS_ALPHABET=small|big] python3 convex-substitution-wedge-domain.py [--jobs 7] [--output F]
(big = the 10-value alphabet of convex-substitution-pentagrid.py)
"""
import argparse, importlib.util, json, math, sys, time
from itertools import product
from multiprocessing import Pool
from pathlib import Path

def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(fname))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
drv = _load("cs_drv", "convex-substitution-cyclotomic.py")
core = drv.core; shp = drv.shp
import os
NN = int(os.environ.get("CS_N", "5"))
core.configure(NN)
if NN == 5: PHI = (1 + 5 ** 0.5) / 2; PHIC = (1 - 5 ** 0.5) / 2
else: PHI = math.sqrt(core.Q0); PHIC = -PHI
import os
ALPHS = {"small": [(1, 0), (0, 1), (1, 1), (2, 0), (-1, 1)],
         "big": [(1, 0), (0, 1), (1, 1), (2, 0), (1, 2), (2, 1), (0, 2), (2, 2), (-1, 1), (2, -1)]}
if NN == 6:
    ALPHS = {"small": [(1, 0), (0, 1), (2, 0), (1, 1), (2, 1)], "big": drv.ALPH[6]}
ALPH = ALPHS[os.environ.get("CS_ALPHABET", "small")]
HEXALPH = {"none": None, "tiny": [(1, 0), (0, 1), (2, 0), (-1, 1) if NN == 5 else (1, 1)]}[os.environ.get("CS_HEX", "none")]
SCALE = {5: 2, 6: 12}[NN]
SHAPES = None

def fval(z): return z[0] + z[1] * PHI
def cval(z): return z[0] + z[1] * PHIC

def diam(P):
    f = [core.pfloat(p) for p in P]
    return max(math.dist(a, b) for a in f for b in f)

def chord_h(P, i):
    f = [core.pfloat(p) for p in P]; n = len(f)
    c, pv, nx = f[i], f[(i - 1) % n], f[(i + 1) % n]
    ex, ey = nx[0] - pv[0], nx[1] - pv[1]
    return abs(ex * (c[1] - pv[1]) - ey * (c[0] - pv[0])) / math.hypot(ex, ey)

def small_lambdas(lam0, aX, aO):
    """lambda in Z[phi], 1<lambda<=lam0, lambda^2*aX = m_self*aX + m_other*aO
    with nonnegative integers (m_other>=1), and the companion relation for the
    other parent with nonnegative integers.  Returns list of (lam, counts)."""
    out = []
    r = None
    for p in range(-60, 61):
        for q in range(0, 61):
            lam = p + q * PHI
            if lam <= 1 or lam > lam0 + 1e-9: continue
            if abs(p + q * PHIC) >= lam: continue          # Perron: |lambda'| < lambda
            lam2 = core.zmul((p, q), (p, q))
            # solve lam2*aX = ms*aX + mo*aO over Z: two integer equations
            for mo in range(1, int(lam0 * lam0 * fval(aX) / fval(aO)) + 2):
                rem = core.zsub(core.zmul(lam2, aX), core.zscale(mo, aO))
                # rem must equal ms*aX for integer ms >= 0
                if aX[1] != 0:
                    if rem[1] % aX[1]: continue
                    ms = rem[1] // aX[1]
                else:
                    if rem[1] != 0 or rem[0] % aX[0]: continue
                    ms = rem[0] // aX[0]
                if ms < 0 or core.zscale(ms, aX) != rem: continue
                out.append(((p, q), ms, mo))
    return out

def work(args):
    i, j = args
    P, Q = SHAPES[i], SHAPES[j]
    shapes = {"P": P["pts"], "Q": Q["pts"]}
    D = max(diam(P["pts"]), diam(Q["pts"]))
    rec = {"P": i, "Q": j, "parents": {}}
    for xname, X, O, oname in (("P", P, Q, "Q"), ("Q", Q, P, "P")):
        res = {"wedge": [], "small": None, "excluded": False}
        best = None
        for alpha in sorted(set(X["angles"])):
            st, nodes, maxd = core.wedge_test(shapes, alpha, radius=60.0, node_limit=20000)
            res["wedge"].append([alpha, st, nodes])
            if st == "dead":
                Rs = maxd + D + 1e-6
                h = max(chord_h(X["pts"], k) for k in range(len(X["angles"])) if X["angles"][k] == alpha)
                lam0 = Rs / h
                if best is None or lam0 < best[0]: best = (lam0, alpha)
                break
        if best is not None:
            lam0 = best[0]
            runs = []; ok = True
            for (lam, ms, mo) in small_lambdas(lam0, X["area"], O["area"]):
                cnt = {xname: ms, oname: mo}
                Dd = core.Dissector([core.pscale(lam, p) for p in X["pts"]], shapes, cnt, node_limit=200000)
                s = Dd.run()
                runs.append([list(lam), ms, mo, bool(s), Dd.limit_hit, Dd.nodes])
                if s or Dd.limit_hit: ok = False
            res["small"] = {"lambda_threshold": lam0, "runs": runs}
            res["excluded"] = ok
        rec["parents"][xname] = res
        if res["excluded"]: break
    rec["excluded"] = any(v["excluded"] for v in rec["parents"].values())
    return rec

def init():
    global SHAPES
    pw = {"P" + "".join(map(str, w)): w for w in shp.cyclic_words(5, 3 * NN, NN - 1) if not shp.adjacent_supplementary(w, NN)}
    SHAPES = drv.enumerate_shapes(pw, ALPH, SCALE)
    if HEXALPH:
        hw = {"H" + "".join(map(str, w)): w for w in shp.cyclic_words(6, 4 * NN, NN - 1)}
        SHAPES = SHAPES + drv.enumerate_shapes(hw, HEXALPH, SCALE)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--jobs", type=int, default=7)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--output")
    a = ap.parse_args()
    init(); t0 = time.time()
    pairs = []
    for i in range(len(SHAPES)):
        for j in range(i + 1, len(SHAPES)):
            a1, a2 = SHAPES[i]["area"], SHAPES[j]["area"]
            # r = a2/a1 irrational, r>0 automatically, conjugate negative
            if a1[0] * a2[1] == a1[1] * a2[0]: continue   # rational ratio
            if cval(a1) * cval(a2) >= 0: continue
            if len(SHAPES[i]["angles"]) == 6 and len(SHAPES[j]["angles"]) == 6: continue  # Euler lemma
            pairs.append((i, j))
    if a.limit: pairs = pairs[:a.limit]
    print(json.dumps({"shapes": len(SHAPES), "pairs_area_condition": len(pairs)}), file=sys.stderr, flush=True)
    with Pool(a.jobs, initializer=init) as pool:
        recs = []
        for k, r in enumerate(pool.imap_unordered(work, pairs, chunksize=20)):
            recs.append(r)
            if k % 2000 == 0: print(k, time.time() - t0, file=sys.stderr, flush=True)
    excl = sum(r["excluded"] for r in recs)
    open_ = [r for r in recs if not r["excluded"]]
    out = {"N": NN, "alphabet": [list(x) for x in ALPH], "hex_alphabet": HEXALPH, "scale": SCALE,
           "shapes": [{"word": s["word"], "angles": s["angles"], "lengths": [list(x) for x in s["lengths"]]} for s in SHAPES],
           "pairs": len(recs), "all_lambda_excluded": excl, "not_excluded": open_,
           "elapsed_s": round(time.time() - t0, 1)}
    print(json.dumps({"pairs": len(recs), "excluded": excl, "not_excluded": len(open_)}), file=sys.stderr)
    if a.output: Path(a.output).write_text(json.dumps(out))

if __name__ == "__main__":
    main()
