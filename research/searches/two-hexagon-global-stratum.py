#!/usr/bin/env python3
"""Fixed-angle-type census: for a fixed exact angle type T, decide ALL length
structures ~ (every equivalence relation on the 12 sides, realisable or not).

Same CEGAR logic as two-hexagon-global-cegar.py (Theorem 3 of
research/lemmas/two-hexagon-global-sft-encoding.md) with the triple booleans
frozen to T.  Since T is fixed and closed, a torus record is just the set
E(x) of glued side pairs, and an empty record is an equivalence ~0.

Usage:
  python two-hexagon-global-stratum.py partitions R R2 N outdir [first last]
runs every partition class Pi (generic-angle strata, T = closure(Pi)).
"""
import sys, os, json, time, itertools, importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_here, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
cg = _load("cg", "two-hexagon-global-cegar.py")
pc = _load("pc", "two-hexagon-global-partition-census.py")


def stabilizer(T):
    Ts = set(T)
    return [g for g in cg.GROUP if set(cg.img_triple(g, t) for t in Ts) == Ts]


def run_type(T, R, R2, N, log, workers=4, maxit=100000):
    T = sorted(set(map(tuple, T)))
    Tset = set(T)
    stab = stabilizer(T)
    q = cg.Query(R)
    for i, t in enumerate(cg.TRIPLES):
        q.m.Add(q.t[i] == (1 if t in Tset else 0))
    def add_clause_E(F):           # not(F <= e)
        seen = set()
        for g in stab:
            key = tuple(sorted(cg.img_pair(g, p) for p in F))
            if key in seen: continue
            seen.add(key)
            q.m.AddBoolOr([q.e[cg.PIDX[p]].Not() for p in key])
    def add_escape_E(E0):          # e not<= E0
        seen = set()
        for g in stab:
            key = frozenset(cg.img_pair(g, p) for p in E0)
            if key in seen: continue
            seen.add(key)
            q.m.AddBoolOr([q.e[i] for i, p in enumerate(cg.PAIRS) if p not in key])
    tori, empties, cands = [], [], []
    for it in range(maxit):
        st, s = q.solve(600, workers)
        if st != "SAT":
            return {"status": st, "iterations": it, "tori": tori, "empties": empties, "candidates": cands}
        U, E, patch = cg.proposal_usage(q, s)
        cls = cg.classes_from_pairs(E)
        Ecl = cg.pairs_of_classes(cls)
        cov = None
        for (Ex, lat, sol) in tori:
            if cg.eq_closure_contains(E, Ex):
                cov = Ex; break
        if cov is not None:
            add_clause_E(cg.minimal_eq_generating(E, cov)); continue
        sft = cg.TypeSFT(T, cls)
        lat, sol = sft.tori(N, time=60)
        if lat is not None and lat[0] != "UNKNOWN":
            Ux, Ex = cg.usage(sol, lat)
            assert set(Ux) <= Tset
            F = cg.minimal_eq_generating(E, Ex)
            tori.append((Ex, list(lat), {"%d,%d" % z: v for z, v in sol.items()}))
            add_clause_E(F)
            log.write(json.dumps({"event": "torus", "T": T, "E": Ex, "F": F, "lat": list(lat),
                                  "sol": tori[-1][2], "cls": cls}) + "\n"); log.flush()
            continue
        st2, _ = sft.patch(R2, time=300)
        rec = {"T": T, "E": Ecl, "cls": cls, "R2": R2, "patch": st2, "torus_search": str(lat)}
        if st2 == "UNSAT":
            empties.append(Ecl); log.write(json.dumps(dict(rec, event="empty")) + "\n")
        else:
            cands.append(rec); log.write(json.dumps(dict(rec, event="candidate")) + "\n")
            print("   CANDIDATE", json.dumps(rec), flush=True)
        log.flush()
        add_escape_E(Ecl)
    return {"status": "maxit", "tori": tori, "empties": empties, "candidates": cands}


def main():
    mode = sys.argv[1]
    R, R2, N = map(int, sys.argv[2:5]); outdir = sys.argv[5]
    os.makedirs(outdir, exist_ok=True)
    if mode == "partitions":
        G = pc.group(); seen = {}
        for p in pc.partitions12():
            seen.setdefault(pc.canon(p, G), p)
        keys = sorted(seen)
        a, b = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (0, len(keys))
        summ = open(os.path.join(outdir, "summary-%d-%d.jsonl" % (a, b)), "a")
        for idx in range(a, b):
            blocks = keys[idx]
            T = cg.closure([tuple(sorted(bl)) for bl in blocks])
            log = open(os.path.join(outdir, "log-%03d.jsonl" % idx), "w")
            t0 = time.time()
            res = run_type(T, R, R2, N, log)
            out = {"index": idx, "partition": [list(bl) for bl in blocks], "T": T, "status": res["status"],
                   "iterations": res.get("iterations"), "ntori": len(res["tori"]),
                   "nempty": len(res["empties"]), "ncand": len(res["candidates"]),
                   "seconds": round(time.time() - t0, 1)}
            summ.write(json.dumps(out) + "\n"); summ.flush()
            print(json.dumps({k: out[k] for k in out if k != "T"}), flush=True)


def main_flats():
    # python two-hexagon-global-stratum.py flats flats.json maxrank R R2 N outdir first last
    fl = json.load(open(sys.argv[2])); maxrank = int(sys.argv[3])
    R, R2, N = map(int, sys.argv[4:7]); outdir = sys.argv[7]
    os.makedirs(outdir, exist_ok=True)
    items = sorted([tuple(map(tuple, T)) for T, r in fl
                    if r <= maxrank and len({c for t in T for c in t}) == 12])
    a, b = (int(sys.argv[8]), int(sys.argv[9])) if len(sys.argv) > 9 else (0, len(items))
    summ = open(os.path.join(outdir, "summary-%d-%d.jsonl" % (a, b)), "a")
    print("covering flats of rank <= %d: %d" % (maxrank, len(items)), flush=True)
    for idx in range(a, min(b, len(items))):
        T = list(items[idx])
        log = open(os.path.join(outdir, "log-%04d.jsonl" % idx), "w")
        t0 = time.time()
        res = run_type(T, R, R2, N, log)
        out = {"index": idx, "T": T, "status": res["status"], "iterations": res.get("iterations"),
               "ntori": len(res["tori"]), "nempty": len(res["empties"]), "ncand": len(res["candidates"]),
               "seconds": round(time.time() - t0, 1)}
        summ.write(json.dumps(out) + "\n"); summ.flush()
        print(json.dumps({k: out[k] for k in out if k != "T"}), flush=True)


if __name__ == "__main__" and sys.argv[1] == "flats":
    main_flats()
elif __name__ == "__main__":
    main()
