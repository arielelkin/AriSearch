#!/usr/bin/env python3
"""Enumerate realisable closed angle types T (flats of the triple arrangement)
up to the 288 relabellings, by rank, and count those covering all 12 corners.

A closed type T = set of corner triples whose 360-equations hold on an affine
flat F_T (cut out by T and the two 720 sums) that meets the open box
(0,180)^12.  Realisable exact types are exactly such T (generic point of the
flat).  Only covering T matter for aperiodicity: if a corner of A lies in no
triple of T, A never occurs and X(T,~) consists of monohedral B tilings
(periodic by the imported monohedral classification, or empty).
"""
import sys, os, json, time, importlib.util
_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cg", os.path.join(_here, "two-hexagon-global-cegar.py"))
cg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cg)


def canon(T):
    best = None
    for g in cg.GROUP:
        k = tuple(sorted(cg.img_triple(g, t) for t in T))
        if best is None or k < best:
            best = k
    return best


def covers(T):
    return len({c for t in T for c in t}) == 12


def main():
    maxrank = int(sys.argv[1]); out = sys.argv[2]
    level = {(): ()}
    allflats = {}
    for r in range(1, maxrank + 1):
        nxt = {}
        t0 = time.time()
        for key in level:
            T = list(key)
            Ts = set(T)
            for tau in cg.TRIPLES:
                if tau in Ts:
                    continue
                T2 = cg.closure(T + [tau])
                c = canon(T2)
                if c in nxt or c in allflats:
                    continue
                ok, _ = cg.angle_feasible_plain(list(c))
                if not ok:
                    continue
                nxt[c] = c
        ncov = sum(1 for c in nxt if covers(c))
        print("rank", r, "flats", len(nxt), "covering", ncov, "%.0fs" % (time.time() - t0), flush=True)
        for c in nxt:
            allflats[c] = r
        level = nxt
        json.dump([[list(map(list, c)), allflats[c]] for c in allflats], open(out, "w"))


if __name__ == "__main__":
    main()
