#!/usr/bin/env python3
"""Bounded global finite-patch query avoiding retained low-rank escapes.
SAT does not establish joint polygon realisability or infinite tilability.
"""
import argparse, hashlib, importlib.util, json
from pathlib import Path
import ortools
HERE = Path(__file__).resolve().parent

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
cg = module('cg', HERE / 'two-hexagon-global-cegar.py')
ck = module('ck', HERE / 'two-hexagon-global-check.py')

def library(path):
    records = json.loads(Path(path).read_text())
    direct = {}
    count = 0
    for st in records['flats']:
        for i, rec in enumerate(st['tori']):
            lab = {tuple(map(int, z.split(','))): v for z, v in rec['sol'].items()}
            U, E = ck.used(rec['lat'], lab)
            assert sorted(E) == sorted(map(tuple, rec['E']))
            assert ck.span_test(st['T'], U) and ck.eq_test(rec['F'], E)
            direct.setdefault((tuple(sorted(U)), tuple(sorted(E))), [st['index'], i])
            count += 1
    images = {}
    for (U, E), source in direct.items():
        for gi, g in enumerate(cg.GROUP):
            k = (tuple(sorted(cg.img_triple(g, t) for t in U)),
                 tuple(sorted(cg.img_pair(g, p) for p in E)))
            images.setdefault(k, dict(source=source, symmetry=gi))
    return count, direct, images

def run(args):
    assert args.grid >= 0
    n, direct, images = library(args.library)
    q = cg.Query(args.radius, grid=args.grid)
    for U, E in images:
        q.m.AddBoolOr([q.t[cg.TIDX[t]].Not() for t in U] +
                      [q.e[cg.PIDX[p]].Not() for p in E])
    result = dict(scope='Bounded relaxed global patch query with rational-closure refinement; SAT is not plane tilability',
                  library=args.library, library_sha256=hashlib.sha256(Path(args.library).read_bytes()).hexdigest(),
                  source_records=n, distinct_direct_supports=len(direct), distinct_symmetry_supports=len(images),
                  radius=args.radius, angle_grid=args.grid, iterations_limit=args.iterations, seconds_per_query=args.seconds,
                  workers=1, random_seed=1, ortools_version=ortools.__version__, refinements=[])
    if args.resume:
        previous = json.loads(Path(args.resume).read_text())
        assert previous['library_sha256'] == result['library_sha256']
        assert previous['radius'] == args.radius
        for rec in previous['refinements']:
            assert cg.closure_contains(rec['S'], rec['implied'])
            for tau in rec['implied']:
                q.add_implication(rec['S'], tuple(tau))
        result['resumed_from'] = args.resume
        result['resume_sha256'] = hashlib.sha256(Path(args.resume).read_bytes()).hexdigest()
        result['refinements'] = previous['refinements'][:]
    if args.empty_potential:
        from fractions import Fraction
        raw = json.loads(Path(args.empty_potential).read_text())
        d = list(map(Fraction, raw['empty_potential']))
        assert sum(d[:6]) < 0 and sum(d[6:]) < 0
        region = [t for t in cg.TRIPLES if sum(d[c] for c in t) >= 0]
        q.add_escape(region, cg.PAIRS)
        result['analytic_empty_region'] = dict(potential=list(map(str,d)),
            size=len(region), source=args.empty_potential,
            sha256=hashlib.sha256(Path(args.empty_potential).read_bytes()).hexdigest())
    for iteration in range(args.iterations):
        status, solver = q.solve(args.seconds, workers=1)
        print('iteration', iteration, status, flush=True)
        if status != 'SAT':
            result.update(status=status, queries=iteration + 1)
            break
        U, E, patch = cg.proposal_usage(q, solver)
        T = cg.closure(U)
        grid_angles = None
        if args.grid:
            grid_angles = [solver.Value(v) for v in q.a]
            T = [t for t in cg.TRIPLES if sum(grid_angles[c] for c in t) == 360*args.grid]
            assert set(U) <= set(T)
        cls = cg.classes_from_pairs(E)
        Ec = set(cg.pairs_of_classes(cls))
        escapes = [(V, F) for V, F in images if set(V) <= set(T) and set(F) <= Ec]
        if escapes:
            V, F = escapes[0]
            missing = [t for t in V if not solver.Value(q.t[cg.TIDX[t]])]
            assert missing, 'Initial inherited blocking clauses violated'
            S = cg.minimal_generating(U, missing)
            assert cg.closure_contains(S, missing)
            for tau in missing:
                q.add_implication(S, tau)
            result['refinements'].append(dict(U=U, E=E, S=S, implied=missing, escape_U=V, escape_E=F))
            continue
        result.update(status='RESIDUAL_FINITE_PATCH', queries=iteration + 1, U=U, E=E, T=T, classes=cls,
                      rank=cg.rref_rank(cg.BASE + [cg.eqrow(t) for t in T]) - 2,
                      covers=len({c for t in T for c in t}) == 12,
                      patch={','.join(map(str, z)): v for z, v in patch.items()})
        if grid_angles is not None:
            result['angle_grid_numerators'] = grid_angles
        if args.empty_potential:
            for gi, g in enumerate(cg.GROUP):
                image = {cg.img_triple(g,t) for t in region}
                if set(T) <= image:
                    result['status'] = 'RESIDUAL_FINITE_PATCH_IN_EMPTY_REGION'
                    result['empty_region_symmetry'] = gi
                    result['residual_scope'] = 'Exact physical-support type is already analytically empty; larger angle types are not classified.'
                    break
        break
    else:
        result.update(status='ITERATION_LIMIT', queries=args.iterations)
    Path(args.output).write_text(json.dumps(result, indent=1) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('refinements','U','E','T','patch','classes')}), flush=True)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--library', default='research/certificates/two-hexagon-global-covering-rank3-strata.json')
    ap.add_argument('--radius', type=int, default=3)
    ap.add_argument('--iterations', type=int, default=20)
    ap.add_argument('--seconds', type=float, default=30)
    ap.add_argument('--grid', type=int, default=0)
    ap.add_argument('--resume')
    ap.add_argument('--empty-potential')
    ap.add_argument('--output', required=True)
    run(ap.parse_args())
