#!/usr/bin/env python3
"""Independent checker for census records (no import of the census code).

Re-implements the conventions of research/lemmas/two-hexagon-global-sft-encoding.md
from scratch and checks, for every torus record of a census log:
  * the labelling is legal in the type (closure(S), eqclosure(F)) where S,F
    are the generating sets that the record's clause uses, i.e. every vertex
    corner-triple lies in the rational closure of S, and every glued side pair
    lies in the equivalence closure of F.
Usage: python two-hexagon-global-check.py log.jsonl [library.json ...]
"""
import sys, json
from fractions import Fraction as Fr

DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
SYM = [(q, r, s) for q in range(2) for s in (1, -1) for r in range(6)]


def corner(sym, k):
    q, r, s = sym
    return 6 * q + (r + s * k) % 6


def side(sym, k):
    q, r, s = sym
    return 6 * q + ((r + k) % 6 if s == 1 else (r - k - 1) % 6)


def wrapper(lat):
    n, s, m = lat
    def w(z):
        x, y = z
        t = y // m
        return ((x - s * t) % n, y - m * t)
    return w


def used(lat, lab):
    w = wrapper(lat)
    U, E = set(), set()
    for z, v in lab.items():
        a = SYM[v]
        for k in (0, 1):
            b = SYM[lab[w((z[0] + DIRS[k][0], z[1] + DIRS[k][1]))]]
            c = SYM[lab[w((z[0] + DIRS[k + 1][0], z[1] + DIRS[k + 1][1]))]]
            U.add(tuple(sorted((corner(a, k), corner(b, k + 2), corner(c, (k + 4) % 6)))))
        for k in range(6):
            d = DIRS[(k + 1) % 6]
            b = SYM[lab[w((z[0] + d[0], z[1] + d[1]))]]
            p, q = side(a, k), side(b, (k + 3) % 6)
            if p != q:
                E.add((min(p, q), max(p, q)))
    return U, E


def row(t):
    r = [Fr(0)] * 13
    for c in t:
        r[c] += 1
    r[12] = Fr(360)
    return r


def span_test(gen, targets):
    M = [[Fr(1)] * 6 + [Fr(0)] * 6 + [Fr(720)], [Fr(0)] * 6 + [Fr(1)] * 6 + [Fr(720)]] + [row(t) for t in gen]
    piv = []; B = []
    for r in M:
        r = r[:]
        for (c, b) in zip(piv, B):
            if r[c]:
                f = r[c]; r = [x - f * y for x, y in zip(r, b)]
        nz = [i for i in range(13) if r[i]]
        if nz:
            c = nz[0]; f = r[c]; r = [x / f for x in r]
            B2 = []
            for b in B:
                if b[c]:
                    g = b[c]; b = [x - g * y for x, y in zip(b, r)]
                B2.append(b)
            B = B2 + [r]; piv.append(c)
    for t in targets:
        r = row(t)
        for (c, b) in zip(piv, B):
            if r[c]:
                f = r[c]; r = [x - f * y for x, y in zip(r, b)]
        if any(r):
            return False
    return True


def eq_test(F, targets):
    par = list(range(12))
    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    for a, b in F:
        par[f(a)] = f(b)
    return all(f(a) == f(b) for a, b in targets)


def main():
    nt = 0; bad = 0
    for path in sys.argv[1:]:
        if path.endswith(".jsonl"):
            recs = [json.loads(l) for l in open(path)]
            for r in recs:
                if r.get("event") != "torus":
                    continue
                lat = tuple(r["lat"])
                lab = {tuple(map(int, k.split(","))): v for k, v in r["sol"].items()}
                U, E = used(lat, lab)
                ok = sorted(E) == sorted(map(tuple, r["E"]))
                if "U" in r:   # global-census record
                    ok = ok and sorted(U) == sorted(map(tuple, r["U"]))
                ok = ok and span_test([tuple(t) for t in r["T"]], U)
                cls = r["cls"]
                ok = ok and all(cls[a] == cls[b] for a, b in E)
                if "F" in r:   # fixed-angle-type record: clause is not(F <= e)
                    ok = ok and eq_test([tuple(p) for p in r["F"]], E)
                nt += 1; bad += (not ok)
        elif isinstance(json.load(open(path)), dict):
            # census certificate: {"strata"/"flats": [{"T":..., "tori":[...]}, ...]}
            C = json.load(open(path))
            for st in C.get("strata", []) + C.get("flats", []):
                T = [tuple(t) for t in st["T"]]
                for r in st["tori"]:
                    lat = tuple(r["lat"])
                    lab = {tuple(map(int, k.split(","))): v for k, v in r["sol"].items()}
                    U, E = used(lat, lab)
                    ok = sorted(E) == sorted(map(tuple, r["E"])) and span_test(T, U)
                    ok = ok and all(r["cls"][a] == r["cls"][b] for a, b in E)
                    ok = ok and eq_test([tuple(p) for p in r["F"]], E)
                    nt += 1; bad += (not ok)
        else:
            for U0, E0, lat, lab in json.load(open(path)):
                lat = tuple(lat); n, s, m = lat
                cells = [(x, y) for x in range(n) for y in range(m)]
                labd = dict(zip(cells, lab))
                U, E = used(lat, labd)
                ok = sorted(U) == sorted(map(tuple, U0)) and sorted(E) == sorted(map(tuple, E0))
                nt += 1; bad += (not ok)
    print("torus records checked:", nt, "failures:", bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
