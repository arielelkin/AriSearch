#!/usr/bin/env python3
"""Enumerate abstract decorations of a (marked, vertex-labelled) rhomb.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-two-class-decorations.py [out.json]

A decoration is a plane graph drawn in the closed rhomb with outer cycle
0-1-2-3 (counter-clockwise, labels fixed by the arrow marking), at most two
interior nodes P, Q, and interior edges chosen from
    P-i, Q-i (i = 0..3),  P-Q,  diagonals 0-2, 1-3.
Conditions (all purely combinatorial, necessary for convex pieces):
  * every interior node has degree >= 3;
  * the rotation system is planar (Euler genus 0) with 0123 the outer face;
  * every inner face (piece) is a simple cycle (no repeated node).
Rotation systems enumerated exhaustively: cyclic orders at P, Q and linear
orders of interior neighbours inside each rhomb corner.  Types equivalent
under renaming P <-> Q are identified.  Geometric realisability is NOT
assumed here; it is imposed later (so this list is a superset).
"""
import itertools, json, math, sys

EDGES = [('P', 0), ('P', 1), ('P', 2), ('P', 3), ('Q', 0), ('Q', 1), ('Q', 2), ('Q', 3),
         ('P', 'Q'), (0, 2), (1, 3)]

def cyc_orders(items):
    items = list(items)
    if len(items) <= 1:
        yield tuple(items); return
    first = items[0]
    for perm in itertools.permutations(items[1:]):
        yield (first,) + perm

def faces(rot):
    """rot: node -> tuple ccw neighbours. Returns list of faces (lists of darts)."""
    seen = set(); out = []
    for v in rot:
        for x in rot[v]:
            if (v, x) in seen:
                continue
            f = []; a, b = v, x
            while (a, b) not in seen:
                seen.add((a, b)); f.append((a, b))
                r = rot[b]; i = r.index(a); c = r[(i - 1) % len(r)]
                a, b = b, c
            out.append(f)
    return out

def canon(edges, rot):
    def key(e, r):
        return (tuple(sorted(tuple(sorted(map(str, x))) for x in e)),
                tuple(sorted((str(k), tuple(map(str, v))) for k, v in r.items())))
    k1 = key(edges, rot)
    sw = {'P': 'Q', 'Q': 'P'}
    f = lambda x: sw.get(x, x)
    e2 = [(f(a), f(b)) for a, b in edges]
    r2 = {f(k): tuple(f(x) for x in v) for k, v in rot.items()}
    # normalise cyclic orders at P/Q to start at their smallest element (string order)
    def norm(r):
        out = {}
        for k, v in r.items():
            if k in ('P', 'Q') and v:
                i = min(range(len(v)), key=lambda j: str(v[j]))
                v = v[i:] + v[:i]
            out[k] = tuple(v)
        return out
    k1 = key(edges, norm(rot)); k2 = key(e2, norm(r2))
    return min(k1, k2)

def enumerate_types():
    types = {}
    for mask in range(1 << len(EDGES)):
        es = [EDGES[i] for i in range(len(EDGES)) if mask >> i & 1]
        if (0, 2) in es and (1, 3) in es:
            continue                      # crossing diagonals = an interior node
        nb = {v: [] for v in (0, 1, 2, 3)}
        for a, b in es:
            nb.setdefault(a, []).append(b); nb.setdefault(b, []).append(a)
        if 'Q' in nb and 'P' not in nb:
            continue
        if any(len(nb[x]) < 3 for x in ('P', 'Q') if x in nb):
            continue
        choices = []
        nodes = [0, 1, 2, 3] + [x for x in ('P', 'Q') if x in nb]
        for v in nodes:
            if v in ('P', 'Q'):
                choices.append([('c', o) for o in cyc_orders(nb[v])])
            else:
                choices.append([('l', o) for o in itertools.permutations(nb[v])])
        for combo in itertools.product(*choices):
            rot = {}
            for v, (kind, o) in zip(nodes, combo):
                if kind == 'c':
                    rot[v] = tuple(o)
                else:
                    rot[v] = ((v + 1) % 4,) + tuple(o) + ((v - 1) % 4,)
            fs = faces(rot)
            V = len(nodes); E = len(es) + 4; F = len(fs)
            if V - E + F != 2:
                continue
            outer = [f for f in fs if (1, 0) in f]
            if len(outer) != 1 or len(outer[0]) != 4:
                continue
            inner = [f for f in fs if (1, 0) not in f]
            if any(len(set(a for a, b in f)) != len(f) for f in inner):
                continue
            # no P->P self etc. impossible; record
            k = canon(es, rot)
            if k in types:
                continue
            types[k] = {'edges': [list(map(str, e)) for e in es],
                        'rot': {str(v): [str(x) for x in r] for v, r in rot.items()},
                        'pieces': [[[str(a), str(b)] for a, b in f] for f in inner],
                        'npoints': sum(1 for x in ('P', 'Q') if x in nb)}
    return list(types.values())

if __name__ == '__main__':
    T = enumerate_types()
    from collections import Counter
    print('types:', len(T), Counter(t['npoints'] for t in T))
    if len(sys.argv) > 1:
        json.dump(T, open(sys.argv[1], 'w'))
