#!/usr/bin/env python3
"""All-lambda exclusion of homothetic substitution for the b=c=1 golden U/V pair.

1. Local wedge test (convex-substitution-core.wedge_test): a pi/5 corner of
   angle alpha with long sides cannot be filled by copies of U,V.  The search
   is complete (corner-filling argument) and finite; every chosen point and
   every placed vertex lies within distance maxd of the apex, every tested
   child within R* = maxd + diam(U,V).  Any convex parent whose corner region
   agrees with the wedge inside the disk of radius R* inherits the same finite
   dead search tree.
2. lambda*U's 36-degree tip agrees with the wedge inside radius lambda*h,
   h = distance from the U tip to the chord joining its two neighbours.
   So lambda*U has no dissection when lambda*h > R*.
3. Every remaining lambda=p+q*phi (lambda^2=a+d*phi, a=p^2+q^2, d=2pq+q^2>0,
   lambda<=R*/h) is listed and must appear in the exact complete runs of
   convex-substitution-uv-golden.py (all returned no U-parent dissection).
Floats are used only for distances (ordering and radius bookkeeping, with a
1e-6 margin); every geometric decision inside the search is exact.
Usage: python3 convex-substitution-uv-golden-wedge.py [--output F]
"""
import argparse, importlib.util, json, math
from pathlib import Path
spec = importlib.util.spec_from_file_location("cs_core", Path(__file__).with_name("convex-substitution-core.py"))
core = importlib.util.module_from_spec(spec); spec.loader.exec_module(core)
PHI = (1 + 5 ** 0.5) / 2

def conv(after, L):
    n = len(after); return [after[(i - 1) % n] for i in range(n)], L

def diam(P):
    f = [core.pfloat(p) for p in P]
    return max(math.dist(a, b) for a in f for b in f)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--output"); a_ = ap.parse_args()
    Ua, UL = conv((1, 3, 4, 4, 3), [(1, 2), (1, 2), (1, 0), (1, 0), (1, 0)])
    Va, VL = conv((2, 2, 4, 3, 4), [(1, 0), (1, 3), (1, 0), (0, 2), (0, 2)])
    U = core.polygon_from_word(Ua, UL); V = core.polygon_from_word(Va, VL)
    D = max(diam(U), diam(V))
    wedges = {}
    for alpha in (1, 2, 3, 4):
        st, nodes, maxd = core.wedge_test({"U": U, "V": V}, alpha, radius=60.0, node_limit=500000)
        wedges[alpha] = {"status": st, "nodes": nodes, "max_vertex_distance": maxd, "R_star": maxd + D + 1e-6}
        print(alpha, wedges[alpha], flush=True)
    # U tip: vertex with angle 1
    i = Ua.index(1); f = [core.pfloat(p) for p in U]
    c, pv, nx = f[i], f[(i - 1) % 5], f[(i + 1) % 5]
    ex, ey = nx[0] - pv[0], nx[1] - pv[1]
    h = abs(ex * (c[1] - pv[1]) - ey * (c[0] - pv[0])) / math.hypot(ex, ey)
    lam0 = wedges[1]["R_star"] / h
    small = []
    for p in range(-40, 41):
        for q in range(0, 41):
            lam = p + q * PHI
            if lam <= 1 or lam > lam0: continue
            aa = p * p + q * q; dd = 2 * p * q + q * q
            if dd <= 0: continue
            small.append({"lambda": f"{p}+{q}phi", "value": lam, "U_children": aa + dd})
    out = {"pair": "golden U/V b=c=1", "U_angles_vertex": Ua, "V_angles_vertex": Va,
           "max_diameter": D, "wedges": wedges, "U_tip_chord_distance_h": h,
           "lambda_threshold": lam0, "small_lambdas_needing_explicit_run": small,
           "max_children_small": max(s["U_children"] for s in small)}
    print(json.dumps({k: v for k, v in out.items() if k != "small_lambdas_needing_explicit_run"}, indent=1))
    print("small lambdas:", [s["lambda"] for s in small])
    if a_.output: Path(a_.output).write_text(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
