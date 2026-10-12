#!/usr/bin/env python3
"""Combinatorial tile analysis for every (thin decoration, thick decoration).

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-two-class-pairs.py TYPES.json PATCH.json OUT.json

TYPES.json from ammann-two-class-decorations.py, PATCH.json from
ammann-two-class-patchdata.py.  Pure exact integer arithmetic in Z[w]
(basis 1,w,w^2,w^3), except one documented numeric step: the sign of a
dot product at a vertex whose cross product vanishes IDENTICALLY (exactly
verified) is read at two random parameter values (only used to call such a
vertex 'straight' vs 'spike').

For each pair, pieces are glued across shared rhomb edges (union-find);
components touching the patch boundary are discarded.  Each remaining tile
is a cyclic list of vertex forms  c + w^m z_j  (z_0,z_1 = thin P,Q;
z_2,z_3 = thick P,Q) in the frame of one of its rhombs.  A pair is DEAD
(for every choice of interior points) if some tile
  * contains a slit (both sides of a decoration segment), or is pinched /
    multiply connected, or has an identically degenerate (spike) corner;
  * has at most 4 corners after deleting identically-straight vertices
    (a convex triangle/quadrilateral tiles the plane periodically).
Otherwise the generic direct-congruence classes are computed exactly
(identical affine forms after rotation by a 10th root of unity and
translation; parameter-free tiles compared by exact direct/mirror congruence).
"""
import sys, json, random
from collections import defaultdict, Counter

Z0 = (0, 0, 0, 0)

def add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])
def sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])
def neg(a): return (-a[0], -a[1], -a[2], -a[3])
def mulw(a): return (-a[3], a[0] + a[3], a[1] - a[3], a[2] + a[3])
def mulwk(a, k):
    k %= 10
    for _ in range(k):
        a = mulw(a)
    return a
def mul(a, b):
    acc = Z0; t = b
    for i in range(4):
        if a[i]:
            acc = add(acc, tuple(a[i] * x for x in t))
        t = mulw(t)
    return acc
def conj(a):
    # conj(w^k) = w^(10-k)
    acc = (a[0], 0, 0, 0)
    for i in (1, 2, 3):
        if a[i]:
            acc = add(acc, tuple(a[i] * x for x in mulwk((1, 0, 0, 0), 10 - i)))
    return acc
import cmath
W = cmath.exp(1j * cmath.pi / 5)
def cval(a): return a[0] + a[1] * W + a[2] * W**2 + a[3] * W**3

PARAM = {('thin', 'P'): 0, ('thin', 'Q'): 1, ('thick', 'P'): 2, ('thick', 'Q'): 3}

def load(types_path, patch_path):
    T = json.load(open(types_path)); P = json.load(open(patch_path))
    verts = [tuple(v) for v in P['verts']]
    rh = P['rhombs']
    edge_owner = defaultdict(list)
    for ri, (kind, gv, a) in enumerate(rh):
        for i in range(4):
            edge_owner[frozenset((gv[i], gv[(i + 1) % 4]))].append((ri, i))
    return T, verts, rh, edge_owner

def piece_tables(t):
    """slot -> piece index; decoration darts per piece"""
    slot = {}; dec = []
    for pi, f in enumerate(t['pieces']):
        d = []
        for a, b in f:
            if a in '0123' and b in '0123' and (int(a) + 1) % 4 == int(b):
                slot[int(a)] = pi
            else:
                d.append((a, b))
        dec.append(d)
    return slot, dec

def form_sub(A, B):
    """A - B for forms {key: Zw} key 'c' or param index"""
    out = dict(A)
    for k, v in B.items():
        out[k] = sub(out.get(k, Z0), v)
    return {k: v for k, v in out.items() if v != Z0}

def cross_identically_zero(A, B):
    a0 = A.get('c', Z0); b0 = B.get('c', Z0)
    if sub(mul(conj(a0), b0), mul(a0, conj(b0))) != Z0:
        return False
    params = set(k for k in A if k != 'c') | set(k for k in B if k != 'c')
    for j in params:
        aj = A.get(j, Z0); bj = B.get(j, Z0)
        if sub(mul(conj(a0), bj), mul(aj, conj(b0))) != Z0:
            return False
        if sub(mul(conj(aj), b0), mul(a0, conj(bj))) != Z0:
            return False
    for j in params:
        for k in params:
            if sub(mul(conj(A.get(j, Z0)), B.get(k, Z0)), mul(A.get(k, Z0), conj(B.get(j, Z0)))) != Z0:
                return False
    return True

RNG = random.Random(12345)
ZS = [[complex(RNG.uniform(.2, .8), RNG.uniform(.1, .5)) for _ in range(4)] for _ in range(2)]
def fval(F, zs):
    return sum((cval(v) * (1 if k == 'c' else zs[k])) for k, v in F.items())

def analyze(T_thin, T_thick, verts, rh, edge_owner):
    tabs = {'thin': piece_tables(T_thin), 'thick': piece_tables(T_thick)}
    # union-find over (rhomb, piece)
    parent = {}
    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    bad_comp = set()
    for e, owners in edge_owner.items():
        nodes = [(ri, tabs[rh[ri][0]][0][i]) for ri, i in owners]
        if len(nodes) == 1:
            bad_comp.add(nodes[0])
        else:
            a, b = find(nodes[0]), find(nodes[1])
            if a != b:
                parent[a] = b
    for ri, (kind, gv, a) in enumerate(rh):
        for pi in range(len(tabs[kind][1])):
            find((ri, pi))
    comps = defaultdict(list)
    for x in list(parent):
        comps[find(x)].append(x)
    boundary_roots = set(find(x) for x in bad_comp)
    classes = {}
    const_tiles = []
    ntiles = 0
    for root, members in comps.items():
        if root in boundary_roots:
            continue
        ntiles += 1
        darts = []
        for ri, pi in members:
            kind, gv, a = rh[ri]
            def node(s, ri=ri, gv=gv, kind=kind):
                if s in '0123':
                    return ('v', gv[int(s)])
                return ('p', ri, s)
            for x, y in tabs[kind][1][pi]:
                darts.append((node(x), node(y)))
        ds = set(darts)
        if len(ds) != len(darts):
            return {'dead': 'repeated dart'}
        if any((y, x) in ds for x, y in darts):
            return {'dead': 'slit (segment with the same tile on both sides)'}
        nxt = {}
        for x, y in darts:
            if x in nxt:
                return {'dead': 'pinched tile (boundary revisits a vertex)'}
            nxt[x] = y
        # single cycle
        start = darts[0][0]; cyc = [start]; cur = nxt[start]
        while cur != start:
            cyc.append(cur); cur = nxt[cur]
            if len(cyc) > len(darts):
                return {'dead': 'broken boundary'}
        if len(cyc) != len(darts):
            return {'dead': 'tile not simply connected / several boundary cycles'}
        # forms in frame of reference rhomb
        R = min(ri for ri, pi in members)
        v0R = verts[rh[R][1][0]]; aR = rh[R][2]
        forms = []
        for nd in cyc:
            if nd[0] == 'v':
                forms.append({'c': mulwk(sub(verts[nd[1]], v0R), -aR)})
            else:
                ri, s = nd[1], nd[2]
                kind, gv, a = rh[ri]
                c = mulwk(sub(verts[gv[0]], v0R), -aR)
                f = {'c': c} if c != Z0 else {}
                f[PARAM[(kind, s)]] = mulwk((1, 0, 0, 0), a - aR)
                forms.append(f)
        # delete identically straight vertices; spikes are fatal
        changed = True
        while changed:
            changed = False
            n = len(forms)
            for i in range(n):
                A = form_sub(forms[i], forms[i - 1]); B = form_sub(forms[(i + 1) % n], forms[i])
                if not A or not B:
                    return {'dead': 'zero-length edge identically'}
                if cross_identically_zero(A, B):
                    dots = [(fval(A, zs).conjugate() * fval(B, zs)).real for zs in ZS]
                    if all(d > 0 for d in dots):
                        forms.pop(i); changed = True; break
                    return {'dead': 'identically degenerate corner (spike)'}
        if len(forms) <= 4:
            return {'dead': 'tile with %d corners (triangle/quadrilateral)' % len(forms)}
        key = canon_key(forms)
        if key is None:
            const_tiles.append([f.get('c', Z0) for f in forms])
            continue
        if key not in classes:
            classes[key] = {'corners': len(forms), 'count': 0, 'forms': forms, 'rhombs': len(set(m[0] for m in members))}
        classes[key]['count'] += 1
    # parameter-free tiles: exact pairwise congruence (direct or mirror)
    creps = []
    for P in const_tiles:
        for c in creps:
            if const_congruent(c['poly'], P):
                c['count'] += 1; break
        else:
            creps.append({'poly': P, 'count': 1, 'corners': len(P)})
    cls = [{'corners': v['corners'], 'count': v['count'], 'rhombs': v['rhombs'],
            'forms': [{str(k): list(x) for k, x in f.items()} for f in v['forms']]} for v in classes.values()]
    cls += [{'corners': c['corners'], 'count': c['count'], 'constant': True,
             'forms': [{'c': list(x)} for x in c['poly']]} for c in creps]
    return {'dead': None, 'tiles': ntiles, 'nclasses': len(cls), 'classes': cls}

def canon_key(forms):
    n = len(forms)
    if not any(len([k for k in f if k != 'c']) for f in forms):
        return None
    best = None
    for k in range(n):
        seq = forms[k:] + forms[:k]
        m0 = None
        for f in seq:
            ps = [j for j in f if j != 'c']
            if ps:
                v = f[ps[0]]
                m0 = [e for e in range(10) if mulwk((1, 0, 0, 0), e) == v][0]; break
        out = []
        c0 = mulwk(seq[0].get('c', Z0), -m0)
        for f in seq:
            item = [sub(mulwk(f.get('c', Z0), -m0), c0)]
            for j in sorted(x for x in f if x != 'c'):
                item.append((j, mulwk(f[j], -m0)))
            out.append(tuple(item))
        out = tuple(out)
        if best is None or out < best:
            best = out
    return best

def const_congruent(P, Q):
    if len(P) != len(Q):
        return False
    for R in (Q, [conj(x) for x in reversed(Q)]):
        e = [sub(P[(i + 1) % len(P)], P[i]) for i in range(len(P))]
        f = [sub(R[(i + 1) % len(R)], R[i]) for i in range(len(R))]
        n = len(e)
        for k in range(n):
            if mul(f[k], conj(f[k])) != mul(e[0], conj(e[0])):
                continue
            if all(mul(f[(k + i) % n], e[0]) == mul(f[k], e[i]) for i in range(n)):
                return True
    return False

_G = {}
def _init(types_path, patch_path):
    _G['data'] = load(types_path, patch_path)

def _row(i):
    T, verts, rh, edge_owner = _G['data']
    out = []
    for j, tk in enumerate(T):
        r = analyze(T[i], tk, verts, rh, edge_owner)
        r['thin'] = i; r['thick'] = j
        out.append(r)
    return out

def main(types_path, patch_path, out_path, nproc=8):
    import multiprocessing as mp
    T = json.load(open(types_path))
    res = []; stats = Counter()
    with mp.Pool(nproc, initializer=_init, initargs=(types_path, patch_path)) as pool:
        for rows in pool.imap_unordered(_row, range(len(T))):
            for r in rows:
                stats[r['dead'] or ('ALIVE n=%d' % r['nclasses'])] += 1
                if r['dead'] is None:
                    res.append(r)
            print(len(res), dict(stats), flush=True)
    res.sort(key=lambda r: (r['thin'], r['thick']))
    json.dump({'stats': dict(stats), 'alive': res}, open(out_path, 'w'))
    print('FINAL', dict(stats))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 8)
