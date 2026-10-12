#!/usr/bin/env python3
"""Exact decision of homothetic substitutions for the b=c=1 area-compatible
golden pair of research/searches/pentagrid-golden-metric-area-compatible.md:
    U lengths (phi^3,phi^3,1,1,1), angles-after-sides (1,3,4,4,3);
    V lengths (1,3phi+1,1,2phi,2phi), angles-after-sides (2,2,4,3,4).
By research/lemmas/pentagrid-generic-metric-substitution-obstruction.md
(complementary field case) lambda = p+q*phi in Z[phi] with child counts
U-parent (a,d)=(p^2+q^2, 2pq+q^2), V-parent (d,a+d), d>0.  For every such
lambda with a+d+... <= MAXC we run the complete corner-filling search
(convex-substitution-core.py) on the U parent and, if it succeeds, the V parent.
Usage: python3 convex-substitution-uv-golden.py [--maxc 60] [--nodes 5000000] [--output F]
"""
import argparse, importlib.util, json, math, time
from pathlib import Path
spec = importlib.util.spec_from_file_location("cs_core", Path(__file__).with_name("convex-substitution-core.py"))
core = importlib.util.module_from_spec(spec); spec.loader.exec_module(core)
PHI = (1 + 5 ** 0.5) / 2

def conv(after, L):
    n = len(after); return [after[(i - 1) % n] for i in range(n)], L

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--maxc", type=int, default=60)
    ap.add_argument("--nodes", type=int, default=5_000_000); ap.add_argument("--output")
    a_ = ap.parse_args()
    Uang, UL = conv((1, 3, 4, 4, 3), [(1, 2), (1, 2), (1, 0), (1, 0), (1, 0)])
    Vang, VL = conv((2, 2, 4, 3, 4), [(1, 0), (1, 3), (1, 0), (0, 2), (0, 2)])
    U = core.polygon_from_word(Uang, UL); V = core.polygon_from_word(Vang, VL)
    assert core.is_strictly_convex_ccw(U) and core.is_strictly_convex_ccw(V)
    assert core.zmul((0, 1), core.area4(U)) == core.area4(V)      # area(V)=phi*area(U)
    rows = []
    for p in range(-12, 13):
        for q in range(0, 13):
            lam = p + q * PHI
            if lam <= 1: continue
            a = p * p + q * q; d = 2 * p * q + q * q
            if d <= 0 or a + d > a_.maxc: continue
            rec = {"lambda": f"{p}+{q}phi", "lambda_float": round(lam, 6), "U_parent_counts": [a, d], "V_parent_counts": [d, a + d]}
            for name, X, cnt in (("U", U, {"U": a, "V": d}), ("V", V, {"U": d, "V": a + d})):
                if sum(cnt.values()) > a_.maxc: rec[name + "_parent"] = "not run (children > maxc)"; break
                t = time.time()
                D = core.Dissector([core.pscale((p, q), x) for x in X], {"U": U, "V": V}, cnt, node_limit=a_.nodes)
                s = D.run()
                rec[name + "_parent"] = {"found": bool(s), "nodes": D.nodes, "limit_hit": D.limit_hit,
                                         "seconds": round(time.time() - t, 2),
                                         "solution": [[n, [list(x) for x in pts]] for n, pts in s[0]] if s else None}
                if not s: break
            rows.append(rec); print(json.dumps({k: v for k, v in rec.items() if k != "solution"}), flush=True)
    out = {"pair": "b=c=1 golden U/V", "maxc": a_.maxc, "node_limit": a_.nodes, "rows": rows}
    if a_.output: Path(a_.output).write_text(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
