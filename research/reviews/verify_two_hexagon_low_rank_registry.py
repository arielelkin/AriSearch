#!/usr/bin/env python3
"""Independent exact checks and aggregation of the stored rank <= 3 census.

No imports from the enumeration or census implementations.  Input completeness
as an enumeration of all angle flats remains a separate obligation; this checks
every stored rank, and exact closure, symmetry and census coverage for every
stored covering flat. All triples are multisets, not just distinct corners.
Use --check to compare with retained outputs without writing either artifact.
"""
import argparse
import hashlib
import itertools
import json
import tarfile
from collections import Counter
from pathlib import Path
from sage.all import QQ, matrix, vector


def group():
    maps = [(r, s) for r in range(6) for s in (1, -1)]
    return [tuple(6 * (q ^ swap) + (rs[q][0] + rs[q][1] * i) % 6
                  for q in range(2) for i in range(6))
            for rs in itertools.product(maps, repeat=2) for swap in (0, 1)]


GROUP = group()
TRIPLES = list(itertools.combinations_with_replacement(range(12), 3))
BASE = [[1] * 6 + [0] * 6, [0] * 6 + [1] * 6]


def key(T):
    return tuple(sorted(tuple(sorted(t)) for t in T))


def canon(T):
    return min(tuple(sorted(tuple(sorted(g[c] for c in t)) for t in T))
               for g in GROUP)


def rows(T):
    return BASE + [[t.count(c) for c in range(12)] for t in T]


def rank_and_closure(T):
    M = matrix(QQ, rows(T))
    # All equations share the interior solution alpha_i = 120 degrees.
    # Translate by this solution: affine implication becomes homogeneous.
    nullspace = M.right_kernel().basis()
    C = [t for t in TRIPLES if all(sum(v[c] for c in t) == 0 for v in nullspace)]
    return M.rank() - 2, key(C)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--flats', default='research/certificates/two-hexagon-global-angle-flats-rank3.json')
    p.add_argument('--logs', default='research/certificates/two-hexagon-global-covering-rank3-raw-logs.tar.gz',
                   help='Raw census log directory or retained tar.gz archive')
    p.add_argument('--partitions', default='research/certificates/two-hexagon-global-partition-strata.json')
    p.add_argument('--certificate', default='research/certificates/two-hexagon-global-covering-rank3-strata.json')
    p.add_argument('--registry', default='research/certificates/two-hexagon-global-low-rank-registry-audit.json')
    p.add_argument('--check', action='store_true',
                   help='Compare retained certificate/registry without writing them')
    args = p.parse_args()
    raw = json.loads(Path(args.flats).read_text())
    flat_rank = {}
    rank_counts = Counter()
    covering = {}
    for T0, r in raw:
        T = key(T0)
        assert T not in flat_rank
        assert matrix(QQ, rows(T)).rank() - 2 == r
        flat_rank[T] = r
        rank_counts[r] += 1
        if len({c for t in T for c in t}) == 12:
            rr, C = rank_and_closure(T)
            assert rr == r and C == T and canon(T) == T
            covering[T] = r
    parts = json.loads(Path(args.partitions).read_text())['strata']
    partT = {}
    no_mixed = set()
    for s in parts:
        r, C = rank_and_closure(key(s['partition']))
        assert C == key(s['T'])
        c = canon(C)
        assert c not in partT
        assert c in covering and covering[c] == r
        partT[c] = s['index']
        if all(all(c < 6 for c in b) or all(c >= 6 for c in b)
               for b in s['partition']):
            no_mixed.add(c)
    rank2 = {T for T, r in covering.items() if r == 2}
    rank3 = {T for T, r in covering.items() if r == 3}
    partition3 = {T for T in partT if covering[T] == 3}
    assert rank2 == no_mixed and len(rank2) == 6
    assert len(rank3) == 310 and len(partition3) == 94
    assert len(rank3 - partition3) == 216
    assert len(covering) == 316
    summaries = {}
    logs = Path(args.logs)
    if logs.is_file():
        # Read archive members in memory; never extract paths to the workspace.
        with tarfile.open(logs, 'r:gz') as archive:
            raw_logs = {Path(member.name).name: archive.extractfile(member).read()
                        for member in archive.getmembers() if member.isfile()}
    else:
        raw_logs = {f.name: f.read_bytes() for f in logs.glob('*.jsonl')}
    summary_names = sorted(name for name in raw_logs
                           if name.startswith('summary-') and name.endswith('.jsonl'))
    for name in summary_names:
        for line in raw_logs[name].decode().splitlines():
            rec = json.loads(line)
            assert rec['index'] not in summaries
            summaries[rec['index']] = rec
    assert set(summaries) == set(range(316))
    indexed = sorted(covering)
    out = []
    for idx in range(316):
        r = summaries[idx]
        T = key(r['T'])
        assert T == indexed[idx]
        recs = [json.loads(l) for l in raw_logs['log-%04d.jsonl' % idx].decode().splitlines()]
        assert all(key(x['T']) == T for x in recs)
        tori = [{k: x[k] for k in ('E', 'F', 'lat', 'sol', 'cls')}
                for x in recs if x['event'] == 'torus']
        empties = [x for x in recs if x['event'] == 'empty']
        candidates = [x for x in recs if x['event'] == 'candidate']
        assert (len(tori), len(empties), len(candidates)) == (r['ntori'], r['nempty'], r['ncand'])
        assert r['status'] == 'UNSAT' and not empties and not candidates
        out.append(dict(index=idx, T=r['T'], rank=covering[T],
                        partition_class=partT.get(T), status=r['status'],
                        iterations=r['iterations'], tori=tori,
                        empties=empties, candidates=candidates))
    cert = dict(description='Stored covering rank <= 3 census: 316 final UNSAT queries, 695 torus escape records. This aggregation checks exact identities; independent query verification has a separate log.',
                conventions='research/lemmas/two-hexagon-global-sft-encoding.md section 1',
                flat_enumeration_sha256=sha(args.flats), flats=out)
    if args.check:
        assert json.loads(Path(args.certificate).read_text()) == cert, 'Retained census aggregation differs'
    else:
        Path(args.certificate).write_text(json.dumps(cert, indent=1) + '\n')
    registry = dict(status='PASS; exact stored-flat identities, not an independent completeness proof for the flat enumeration',
                    enumeration_path=args.flats, enumeration_sha256=sha(args.flats),
                    raw_flat_rank_counts=dict(rank_counts),
                    stored_covering_rank_counts=dict(Counter(covering.values())),
                    all_stored_ranks_checked=True, all_stored_covering_closures_and_canonical_labels_checked=True,
                    partition_closures_checked=100,
                    rank2_equals_no_mixed_partitions=True,
                    rank3_partition_subset_count=94,
                    rank3_nonpartition_count=216,
                    summaries_sha256={str(logs) + '::' + name: hashlib.sha256(raw_logs[name]).hexdigest()
                                      for name in summary_names},
                    final_query_status_counts=dict(Counter(r['status'] for r in out)),
                    torus_records=sum(len(r['tori']) for r in out),
                    rank3_nonpartition_indices=[r['index'] for r in out if r['rank'] == 3 and r['partition_class'] is None],
                    remaining_exact_type_definition='Every rationally closed, covering triple set T of rank 4..10 whose angle flat meets (0,pi)^12, modulo D6 x D6 x swap; for each T, all side-length equivalence structures not discharged by inherited escape records or empty-supertype certificates.',
                    note='A proper specialization of any rank <=3 flat is a higher-rank exact type; enumerate it once by its full closure. Angle-box feasibility is not polygon realizability.',
                    certificate=args.certificate)
    if logs.is_file():
        registry['raw_census_log_archive'] = dict(path=str(logs), sha256=sha(logs),
                                                  bytes=logs.stat().st_size)
    registry['enumeration_completeness_guard'] = (
        'Retain noncovering parent flats when extending ranks; minimal covering '
        'roots can have higher rank. Enumerating descendants of the 316 covering '
        'types alone is not justified.')
    verification_log = Path('research/certificates/two-hexagon-global-covering-rank3-verification.log')
    if verification_log.exists():
        lines = verification_log.read_text().splitlines()
        if (len(lines) == 317 and lines[-1] == 'non-INFEASIBLE: 0'
                and [int(line.split()[0]) for line in lines[:-1]] == list(range(316))
                and all(line.split()[1] == 'INFEASIBLE' for line in lines[:-1])):
            registry['independent_one_hot_query_verification'] = dict(
                queries=316, INFEASIBLE=316, other_statuses=0, proof_logs=False,
                log=str(verification_log), sha256=sha(verification_log))
    if args.check:
        retained = json.loads(Path(args.registry).read_text())
        # Only the separate torus check is externally supplied metadata.
        # Compare the full remaining schema, including optional fields: a
        # missing/invalid one-hot log must not preserve a stale retained PASS.
        reconstructed = json.loads(json.dumps(registry))
        checked = {k: v for k, v in retained.items() if k != 'independent_torus_check'}
        assert checked == reconstructed, 'Retained registry differs or lacks a valid supporting log'
    else:
        Path(args.registry).write_text(json.dumps(registry, indent=1) + '\n')
    print(json.dumps({k: registry[k] for k in ('raw_flat_rank_counts', 'stored_covering_rank_counts', 'rank3_partition_subset_count', 'rank3_nonpartition_count', 'torus_records')}), flush=True)


if __name__ == '__main__':
    main()
