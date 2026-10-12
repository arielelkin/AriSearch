#!/usr/bin/env python3
"""Exhaustive CEGAR search for two-class convex decorations of hat tilings.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/source-decoration-hat-search.py PATCH.json OUT.json [D]

DOMAIN (explicit).  A decoration is a set X of primitive lattice segments
(endpoints in the hexPt lattice: kite vertices and kite-axis midpoints, no
lattice point in the open segment) contained in the closed reference hat,
pairwise non-crossing; 154 candidates.  Every hat of a hat tiling carries
the image of X under its isometry (reflected hats the mirrored image).  The
faces are the faces of the union of all decoration segments (hat edges are
erased unless chosen).  Required: every face convex, of diameter < D
(default D = 7 hex sides; the hat itself has diameter < 4), at least 5
corners, and exactly <= 2 congruence classes (mirror identified).

ENCODING (exact integer arithmetic, z3 Boolean CEGAR):
  x_s                local segment s chosen (154 vars)
  e_O = OR_{s in O} x_s   one aux per owner set O of a global segment
  (C1) convexity at every core lattice point p: for every incident global
       segment g, e_g -> OR of e_{g'} with ccw angle(g, g') in (0, 180].
       (Excludes reflex corners and dangling ends.)
  (C2) no two crossing local segments.
  (C3) X non-empty.
  Lazy cuts, each valid for every decoration in the domain:
  (L1) ray cut: from a lattice-triangle centroid q, along one of the 6
       lattice directions, some chosen segment meets the ray within
       distance D (the face of q is convex with diameter < D).
  (L2) face cut: a complete face F with <= 4 corners cannot occur:
       OR_{g in dF} not e_g  OR  OR_{g meets int F} e_g.
  (L3) class cut: three complete faces of pairwise distinct classes
       cannot co-occur (disjunction of their three L2 clauses).
UNSAT after the lazy loop = no decoration in the domain (restricted to the
local configurations of the patch core, which are configurations of every
hat tiling) has <= 2 classes.  Every SAT model that passes is reported.
"""
import sys, json, math, time, importlib.util, os
from functools import cmp_to_key
from collections import defaultdict
import z3

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('hl', os.path.join(here, 'source-decoration-hat-lattice.py'))
hl = importlib.util.module_from_spec(spec); spec.loader.exec_module(hl)
sub, add, cross, dot2, norm2 = hl.sub, hl.add, hl.cross, hl.dot2, hl.norm2

def real(p):   # lattice -> real (scale: hex side = 1 for patch coords at scale 2? see note)
    return (p[0] + p[1] / 2.0, p[1] * math.sqrt(3) / 2.0)

def cmp_dir(a, b):
    if hl.ang_lt(a, b): return -1
    if hl.ang_lt(b, a): return 1
    return 0

def canon_poly(V):
    """exact congruence invariant (mirror identified) of a lattice polygon."""
    def inv(W):
        n = len(W); E = [sub(W[(i + 1) % n], W[i]) for i in range(n)]
        seq = [(norm2(E[i]), dot2(E[i], E[(i + 1) % n]), cross(E[i], E[(i + 1) % n])) for i in range(n)]
        return min(tuple(seq[k:] + seq[:k]) for k in range(n))
    Wm = [hl.matvec(hl.S, p) for p in reversed(V)]
    return min(inv(V), inv(Wm))

def corners(V):
    n = len(V); out = []
    for i in range(n):
        a = sub(V[i], V[i - 1]); b = sub(V[(i + 1) % n], V[i])
        c = cross(a, b)
        if c == 0 and dot2(a, b) > 0:
            continue
        out.append((V[i], c))
    return out

class Search:
    def __init__(self, patch, D=7.0):
        self.D = D
        self.hats = hl.load_patch(patch)
        self.P, self.segs, self.onb = hl.reference_data()
        nS = len(self.segs)
        # crossing pairs within the hat
        self.cross_pairs = []
        for i in range(nS):
            a, b = self.P[self.segs[i][0]], self.P[self.segs[i][1]]
            for j in range(i + 1, nS):
                c, d = self.P[self.segs[j][0]], self.P[self.segs[j][1]]
                if hl.seg_proper_cross(a, b, c, d):
                    self.cross_pairs.append((i, j))
        # global segments
        owners = defaultdict(set)
        for h in self.hats:
            for s, (i, j) in enumerate(self.segs):
                p, q = hl.apply(h, self.P[i]), hl.apply(h, self.P[j])
                owners[(min(p, q), max(p, q))].add(s)
        self.gsegs = {g: frozenset(o) for g, o in owners.items()}
        # geometry: centre and core radius (patch coordinates are lattice at scale 2 => hex side = 1 real unit * ...)
        pts = [real(v) for h in self.hats for v in h['verts']]
        self.cx = sum(p[0] for p in pts) / len(pts); self.cy = sum(p[1] for p in pts) / len(pts)
        # hat lattice units: reference hat edges 1 and sqrt3 -> hex side 2.  Normalise D to these units.
        self.unit = 2.0
        # core: lattice points all of whose surrounding is covered: use distance to farthest-covered estimate
        self.Rcov = self.covered_radius()
        self.Rcore = self.Rcov - 2 * self.unit
        self.Rinner = self.Rcore - self.D * self.unit
        # sample disc for ray cuts / face analysis: a face meeting it that is not complete
        # has diameter > 2D, while a convex face whose 6 rays (from an interior sample point)
        # all stop within D has diameter <= 2D; so such a face always yields a ray cut.
        self.Rs = self.Rcore - 2 * self.D * self.unit - 2
        assert self.Rs > 3 * self.unit, (self.Rcov, self.Rs)
        print('hats', len(self.hats), 'global segments', len(self.gsegs), 'Rcov', round(self.Rcov, 2),
              'Rcore', round(self.Rcore, 2), 'Rinner', round(self.Rinner, 2), 'Rs', round(self.Rs, 2), flush=True)
        self.inc = defaultdict(list)
        for g in self.gsegs:
            self.inc[g[0]].append(g); self.inc[g[1]].append(g)
        self.solver = z3.Solver()
        self.x = [z3.Bool('x%d' % s) for s in range(nS)]
        self.aux = {}
        self.build_static()

    def dist(self, p):
        r = real(p); return math.hypot(r[0] - self.cx, r[1] - self.cy)

    def covered_radius(self):
        # nearest lattice point to the centre that is not interior to the union of hats,
        # detected as a lattice point whose incident hat corner angles do not sum to 360.
        # simpler robust approach: count, for each patch vertex, the hats containing it as a vertex
        # or on an edge; compute exact interior angle sums with floats rounded to 30 deg multiples.
        tot = defaultdict(float)
        for h in self.hats:
            V = h['verts']; n = len(V)
            sgn = -1 if h['refl'] else 1
            for i in range(n):
                a = real(sub(V[(i + 1) % n], V[i])); b = real(sub(V[i - 1], V[i]))
                t = math.atan2(sgn * (a[0] * b[1] - a[1] * b[0]), a[0] * b[0] + a[1] * b[1])
                if t <= 0: t += 2 * math.pi
                tot[V[i]] += t
            # straight boundary points (midpoint of the length-2 edge) also count 180
            for i in range(n):
                a, b = V[i], V[(i + 1) % n]; d = sub(b, a)
                g = math.gcd(abs(d[0]), abs(d[1]))
                for k in range(1, g):
                    tot[(a[0] + d[0] * k // g, a[1] + d[1] * k // g)] += math.pi
        bad = [self.dist(p) for p, t in tot.items() if abs(t - 2 * math.pi) > 1e-6]
        return min(bad)

    def e(self, O):
        O = frozenset(O)
        if len(O) == 1:
            return self.x[next(iter(O))]
        if O not in self.aux:
            v = z3.Bool('e%d' % len(self.aux)); self.aux[O] = v
            self.solver.add(v == z3.Or([self.x[s] for s in O]))
        return self.aux[O]

    def build_static(self):
        S = self.solver
        for i, j in self.cross_pairs:
            S.add(z3.Or(z3.Not(self.x[i]), z3.Not(self.x[j])))
        S.add(z3.Or(self.x))
        seen = set(); n = 0
        for p, gs in self.inc.items():
            if self.dist(p) > self.Rcore:
                continue
            dirs = [(sub(g[1], g[0]) if g[0] == p else sub(g[0], g[1]), self.gsegs[g]) for g in gs]
            for d, O in dirs:
                ok = frozenset(frozenset(O2) for d2, O2 in dirs if d2 != d and hl.ccw_turn_le180(d, d2))
                key = (O, ok)
                if key in seen: continue
                seen.add(key)
                S.add(z3.Implies(self.e(O), z3.Or([self.e(O2) for O2 in ok]) if ok else False))
                n += 1
        print('static convexity clauses (deduplicated):', n, flush=True)
        # ray data (static), computed lazily per check
        self.ray_cache = {}

    # ---------------------------------------------------------------- model analysis
    def chosen_globals(self, model):
        X = {s for s in range(len(self.segs)) if z3.is_true(model.eval(self.x[s], model_completion=True))}
        return X, [g for g, O in self.gsegs.items() if O & X]

    def faces(self, G):
        adj = defaultdict(list)
        for a, b in G:
            adj[a].append(b); adj[b].append(a)
        rot = {v: sorted(nb, key=cmp_to_key(lambda u, w, v=v: cmp_dir(sub(u, v), sub(w, v)))) for v, nb in adj.items()}
        seen = set(); out = []
        for v in adj:
            for x in adj[v]:
                if (v, x) in seen: continue
                f = []; a, b = v, x
                while (a, b) not in seen:
                    seen.add((a, b)); f.append(a)
                    r = rot[b]; i = r.index(a); c = r[(i - 1) % len(r)]
                    a, b = b, c
                out.append(f)
        return out

    def area2(self, V):
        return sum(cross(V[i], V[(i + 1) % len(V)]) for i in range(len(V)))

    def face_clause(self, V):
        """not( dF all present and nothing in int F )"""
        n = len(V); bnd = []
        for i in range(n):
            a, b = V[i], V[(i + 1) % n]; g = (min(a, b), max(a, b))
            bnd.append(self.gsegs[g])
        inside = []
        xs = [p[0] for p in V]; ys = [p[1] for p in V]
        for g, O in self.gsegs.items():
            a, b = g
            if max(a[0], b[0]) < min(xs) or min(a[0], b[0]) > max(xs) or max(a[1], b[1]) < min(ys) or min(a[1], b[1]) > max(ys):
                continue
            if self.meets_interior(a, b, V):
                inside.append(O)
        return [z3.Not(self.e(O)) for O in bnd] + [self.e(O) for O in inside]

    def meets_interior(self, a, b, V):
        n = len(V)
        def strictly_in(P2):     # P2 doubled coords
            for i in range(n):
                A = (2 * V[i][0], 2 * V[i][1]); B = (2 * V[(i + 1) % n][0], 2 * V[(i + 1) % n][1])
                if cross(sub(B, A), sub(P2, A)) <= 0:
                    return False
            return True
        if strictly_in((2 * a[0], 2 * a[1])) or strictly_in((2 * b[0], 2 * b[1])) or strictly_in((a[0] + b[0], a[1] + b[1])):
            return True
        for i in range(n):
            if hl.seg_proper_cross(a, b, V[i], V[(i + 1) % n]):
                return True
        return False

    def build_buckets(self):
        self.B = 4
        self.buckets = defaultdict(list)
        for g, O in self.gsegs.items():
            (a, b) = g
            ra, rb = real(a), real(b)
            for i in range(int(min(ra[0], rb[0]) // self.B), int(max(ra[0], rb[0]) // self.B) + 1):
                for j in range(int(min(ra[1], rb[1]) // self.B), int(max(ra[1], rb[1]) // self.B) + 1):
                    self.buckets[(i, j)].append(g)

    def ray_segments(self, q3, d):
        """Global segments meeting the ray {q + t d : 0 < t <= D} (|d| = 1 for the
        6 unit lattice directions).  Exact integer test; q3 in tripled coords."""
        key = (q3, d)
        if key in self.ray_cache: return self.ray_cache[key]
        if not hasattr(self, 'buckets'):
            self.build_buckets()
        Tmax = 3 * int(round(self.D * self.unit))
        cand = set()
        q = (q3[0] / 3.0, q3[1] / 3.0)
        for k in range(0, int(self.D * self.unit) + 2):
            r = real((q[0] + k * d[0], q[1] + k * d[1]))
            bi, bj = int(r[0] // self.B), int(r[1] // self.B)
            for i in (bi - 1, bi, bi + 1):
                for j in (bj - 1, bj, bj + 1):
                    cand.update(self.buckets.get((i, j), ()))
        out = []
        for g in cand:
            a, b = g
            A = (3 * a[0], 3 * a[1]); BB = (3 * b[0], 3 * b[1])
            AB = sub(BB, A)
            den = cross(d, AB)
            if den == 0: continue
            w = sub(A, q3)
            Tn = cross(w, AB); un = cross(w, d)
            if den < 0: den, Tn, un = -den, -Tn, -un
            if Tn > 0 and Tn <= Tmax * den and 0 <= un <= den:
                out.append(self.gsegs[g])
        self.ray_cache[key] = out
        return out

    def run(self, max_iter=100000):
        S = self.solver
        DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
        # ray sample points: centroids of lattice triangles inside the inner disc
        qs = []
        R = int(self.Rs) + 2
        cu, cv = int(self.cx - self.cy / math.sqrt(3)), int(2 * self.cy / math.sqrt(3))
        for u in range(cu - 3 * R, cu + 3 * R):
            for v in range(cv - 3 * R, cv + 3 * R):
                for (du, dv) in ((1, 1), (2, 2)):
                    q3 = (3 * u + du, 3 * v + dv)
                    if self.dist((q3[0] / 3.0, q3[1] / 3.0)) <= self.Rs:
                        qs.append(q3)
        qs.sort(key=lambda q3: self.dist((q3[0] / 3.0, q3[1] / 3.0)))
        print('ray sample points', len(qs), flush=True)
        found = []; it = 0; stats = defaultdict(int); t0 = time.time()
        while it < max_iter:
            it += 1
            r = S.check()
            if r == z3.unsat:
                print('UNSAT after', it, 'iterations', dict(stats), flush=True)
                return {'status': 'complete (UNSAT)', 'iterations': it, 'cuts': dict(stats), 'found': found}
            m = S.model()
            X, G = self.chosen_globals(m)
            # (L1) rays
            cut = False
            Gs = set(G)
            for q3 in qs:
                for d in DIRS:
                    segs = self.ray_segments(q3, d)
                    if not any(O & X for O in segs):
                        S.add(z3.Or([self.e(O) for O in segs]) if segs else False)
                        stats['ray'] += 1; cut = True; break
                if cut: break
            if cut:
                if stats['ray'] % 50 == 0:
                    print(it, dict(stats), round(time.time() - t0), 's', flush=True)
                continue
            # faces: complete = all vertices within Rcore
            F = self.faces([g for g in G if self.dist(g[0]) <= self.Rcov and self.dist(g[1]) <= self.Rcov])
            comp = []
            for V in F:
                if self.area2(V) <= 0: continue
                if all(self.dist(p) <= self.Rcore for p in V):
                    comp.append(V)
            # faces touching the inner disc must be complete & convex
            bad = None; classes = {}
            for V in comp:
                if min(self.dist(p) for p in V) > self.Rs:
                    continue
                cs = corners(V)
                if any(c < 0 for p, c in cs) or len(cs) <= 4:
                    bad = V; break
                Vc = [p for p, c in cs]
                classes.setdefault(canon_poly(Vc), []).append(V)
            if bad is not None:
                S.add(z3.Or(self.face_clause(bad))); stats['face'] += 1
                if stats['face'] % 50 == 0:
                    print(it, dict(stats), round(time.time() - t0), 's', flush=True)
                continue
            if len(classes) >= 3:
                reps = [min(v, key=lambda V: self.dist(V[0])) for v in classes.values()]
                reps.sort(key=lambda V: self.dist(V[0]))
                cl = self.face_clause(reps[0]) + self.face_clause(reps[1]) + self.face_clause(reps[2])
                S.add(z3.Or(cl)); stats['class3'] += 1
                if stats['class3'] % 20 == 0:
                    print(it, dict(stats), 'classes', len(classes), 'segs', len(X), round(time.time() - t0), 's', flush=True)
                continue
            # candidate
            rec = {'segments': sorted(X), 'classes': [{'corners': len(corners(v[0])), 'count': len(v),
                                                       'example': [list(p) for p in v[0]]} for v in classes.values()]}
            print('CANDIDATE', rec, flush=True)
            found.append(rec)
            S.add(z3.Or([z3.Not(self.x[s]) if s in X else self.x[s] for s in range(len(self.segs))]))
            stats['candidate'] += 1
        return {'status': 'iteration cap', 'iterations': it, 'cuts': dict(stats), 'found': found}

if __name__ == '__main__':
    D = float(sys.argv[3]) if len(sys.argv) > 3 else 7.0
    s = Search(sys.argv[1], D)
    res = s.run()
    res.update({'domain': {'candidate_segments': len(s.segs), 'lattice_points_in_closed_hat': len(s.P),
                           'D_hex_sides': D, 'hats': len(s.hats)},
                'reference_points': s.P, 'reference_segments': s.segs})
    json.dump(res, open(sys.argv[2], 'w'), indent=1)
