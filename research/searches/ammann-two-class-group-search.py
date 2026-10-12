#!/usr/bin/env python3
"""Exact <=2-class collapse search (group level) for surviving decorations.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-two-class-group-search.py TYPES.json PATCH7.json \
      SURV_PAIRWISE.json OUT.json

Input SURV_PAIRWISE.json is the output of
ammann-two-class-survivor-collapse.py: for every pair of generic classes
(X_a, X_b), a < b, the list of (m, D_X, D_Y, orientation, shift) whose
congruence ideal is not the unit ideal (systems with unit ideal are
certified impossible there).

A collapse to <= 2 classes is a partition of the classes into <= 2 blocks
such that, at one common parameter point, all members of each block are
congruent.  For a block with representative X = min(block), a common
target corner count m and deletion set D_X are fixed, and each other member
Y contributes one of its non-empty systems with X (same m, same D_X).  The
search is depth first over members, summing ideals and pruning as soon as
the ideal becomes (1) (Groebner basis over K = Q(w)).  Both blocks share the
same parameters, so the two blocks' ideals are summed as well.

Every complete combination with a non-unit ideal is reported with its
dimension; zero-dimensional ones are solved exactly (QQbar) and the real
points are tested exactly: the actual number of congruence classes of the
tiles at that point (straight vertices removed, mirror images identified)
and weak convexity of every tile.
"""
import sys, json, itertools, importlib.util, os
from sage.all import QQbar, AA, PolynomialRing

here = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(here, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
pa = _load('pa', 'ammann-two-class-pairs.py')
sc = _load('sc', 'ammann-two-class-survivor-collapse.py')

def system_gens(R, X, Y, nx, ny, m, DX, DY, orient, k):
    PX, PXb = X; PY, PYb = Y
    keepX = [i for i in range(nx) if i not in DX]; keepY = [i for i in range(ny) if i not in DY]
    Xr = [PX[i] for i in keepX]; Xrb = [PXb[i] for i in keepX]
    Yr = [PY[i] for i in keepY]; Yrb = [PYb[i] for i in keepY]
    f = sc.edges(Yr); fb = sc.edges(Yrb)
    if orient == 'direct':
        e = sc.edges(Xr); eb = sc.edges(Xrb)
    else:
        e = sc.edges(list(reversed(Xrb))); eb = sc.edges(list(reversed(Xr)))
    gens = []
    for i in range(1, m):
        q = f[(k + i) % m] * e[0] - f[k] * e[i]
        gens += [q, sc.cpoly(R, q)]
    gens.append(f[k] * fb[k] - e[0] * eb[0])
    gens += [sc.straight_eq(R, PX, PXb, i) for i in DX] + [sc.straight_eq(R, PY, PYb, i) for i in DY]
    gens = [g for g in gens if g != 0]
    return gens, (e[0] * eb[0]) * (f[k] * fb[k])

def classes_at_point(CP, corners, vals):
    """exact number of congruence classes (mirror identified) at a real point"""
    polys = []
    convex = True
    for (P, Pb) in CP:
        Pq = [sc.qeval(p, vals) for p in P]
        st = sc.convex_status(Pq)
        if any(x not in ('strict', 'straight') for x in st):
            convex = False
        Pq = [Pq[i] for i in range(len(Pq)) if st[i] != 'straight']
        polys.append(Pq)
    reps = []
    for P in polys:
        for r in reps:
            if len(r) == len(P) and (sc_congruent(r, P) or sc_congruent(r, [x.conjugate() for x in reversed(P)])):
                break
        else:
            reps.append(P)
    return len(reps), [len(r) for r in reps], convex

def sc_congruent(P, Q):
    e = sc.edges(P); f = sc.edges(Q); n = len(e)
    if len(f) != n or e[0] == 0:
        return False
    for k in range(n):
        u = f[k] / e[0]
        if u * u.conjugate() == 1 and all(f[(k + i) % n] == u * e[i] for i in range(n)):
            return True
    return False

def main(types_path, patch_path, pairwise_path, out_path):
    T, verts, rh, eo = pa.load(types_path, patch_path)
    PW = json.load(open(pairwise_path))
    report = []
    for entry in PW:
        i, j = entry['thin'], entry['thick']
        r = pa.analyze(T[i], T[j], verts, rh, eo)
        cls = r['classes']
        assert [c['corners'] for c in cls] == [c['corners'] for c in entry['classes']]
        params = entry['params']
        R, Z, Zb = sc.build_ring(params)
        CP = sc.class_polys(cls, R, Z, Zb)
        N = len(cls); corners = [c['corners'] for c in cls]
        # pairwise options: opts[(a,b)][(m, DX)] = list of (DY, orient, shift)
        opts = {}
        for pr in entry['pairs']:
            a, b = pr['X'], pr['Y']
            for s in pr['nonempty_systems']:
                opts.setdefault((a, b), {}).setdefault((s['m'], tuple(s['DX'])), []).append(
                    (tuple(s['DY']), s['orient'], s['shift']))
        results = []; nchecks = [0]
        U = R.gen(R.ngens() - 1)
        def full(gens, norms):
            N = R(1)
            for q in norms:
                N *= q
            return gens + [U * N - 1]
        def is_unit(gens, norms):
            nchecks[0] += 1
            return R.ideal(full(gens, norms)).dimension() < 0
        def block_options(block):
            """yield generator lists for all consistent choices for one block"""
            if len(block) == 1:
                yield [], [], ('single', block[0]); return
            X = block[0]
            keys = set.intersection(*[set(opts.get((X, Y), {}).keys()) for Y in block[1:]])
            for (m, DX) in sorted(keys):
                lists = [opts[(X, Y)][(m, DX)] for Y in block[1:]]
                order = sorted(range(len(lists)), key=lambda q: len(lists[q]))
                def dfs(pos, gens, norms, chosen):
                    if pos == len(order):
                        yield gens, norms, ('block', X, m, DX, dict(chosen)); return
                    q = order[pos]; Y = block[1 + q]
                    for (DY, orient, k) in lists[q]:
                        gg, nn = system_gens(R, CP[X], CP[Y], corners[X], corners[Y], m, list(DX), list(DY), orient, k)
                        g2 = gens + gg; n2 = norms + [nn]
                        if is_unit(g2, n2):
                            continue
                        chosen2 = chosen + [(Y, (DY, orient, k))]
                        yield from dfs(pos + 1, g2, n2, chosen2)
                yield from dfs(0, [], [], [])
        partitions = []
        for mask in range(1 << (N - 1)):
            b1 = [0] + [q for q in range(1, N) if not (mask >> (q - 1)) & 1]
            b2 = [q for q in range(1, N) if (mask >> (q - 1)) & 1]
            partitions.append([b1] + ([b2] if b2 else []))
        for blocks in partitions:
            # quick necessary test: every non-representative member needs some option with its rep
            if any(len(b) > 1 and any((b[0], y) not in opts for y in b[1:]) for b in blocks):
                continue
            g1s = list(block_options(blocks[0]))
            g2s = list(block_options(blocks[1])) if len(blocks) > 1 else [([], [], None)]
            for (gA, nA, dA) in g1s:
                for (gB, nB, dB) in g2s:
                    gens = gA + gB; norms = nA + nB
                    if gens and is_unit(gens, norms):
                        continue
                    I = R.ideal(full(gens, norms))
                    d = I.dimension()
                    rec = {'blocks': blocks, 'choiceA': str(dA), 'choiceB': str(dB), 'dim': int(d)}
                    if d == 0:
                        pts = []
                        for v in I.variety(QQbar):
                            vals = [v[g] for g in R.gens()]
                            if any(x.imag() != 0 for x in vals):
                                continue
                            vals = [AA(x) for x in vals]
                            ncls, sizes, convex = classes_at_point(CP, corners, vals)
                            pts.append({'point': [str(x) for x in vals], 'minpolys': [str(x.minpoly()) for x in vals],
                                        'classes_at_point': ncls, 'corner_counts': sizes,
                                        'all_tiles_weakly_convex': convex})
                        rec['real_points'] = pts
                    else:
                        rec['groebner_basis'] = [str(g) for g in I.groebner_basis()]
                    results.append(rec)
                    print(i, j, blocks, 'dim', d, rec.get('real_points', 'POSDIM'), flush=True)
        report.append({'thin': i, 'thick': j, 'nclasses': N, 'corners': corners, 'params': params,
                       'partitions_tested': len(partitions), 'groebner_checks': nchecks[0],
                       'nonunit_complete_combinations': results})
        print('== done', i, j, 'checks', nchecks[0], 'nonunit combos', len(results), flush=True)
        json.dump(report, open(out_path, 'w'), indent=1, default=str)

if __name__ == '__main__':
    main(*sys.argv[1:5])
