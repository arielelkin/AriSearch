#!/usr/bin/env python3
"""Solver-free complete pair-graph domain and exact representative checks.
Does not duplicate the spatial/metric census or decide periodicity.
"""
import argparse
from collections import Counter, defaultdict
import itertools
import json
from pathlib import Path
import sympy as sp


def cycles_of_permutation(p):
    seen, cycles = set(), []
    for v in range(6):
        if v in seen:
            continue
        cycle, w = [], v
        while w not in seen:
            seen.add(w); cycle.append(w); w = p[w]
        cycles.append(cycle)
    return cycles


def edges_of_cycles(cycles):
    return tuple(sorted(tuple(sorted((v,cycle[(i+1)%len(cycle)])))
                        for cycle in cycles for i,v in enumerate(cycle)))


def graph_domain():
    graphs = {}
    for p in itertools.permutations(range(6)):
        cycles = cycles_of_permutation(p)
        E = edges_of_cycles(cycles)
        partition = tuple(sorted(map(len,cycles),reverse=True))
        if E in graphs:
            assert graphs[E] == partition
        graphs[E] = partition
    assert len(graphs) == 388
    assert all(Counter(v for e in E for v in e) == {v:2 for v in range(6)} for E in graphs)
    return graphs


def cyclic_word(word):
    forms = (word, word[::-1])
    return min(v[j:]+v[:j] for v in forms for j in range(6))


def all_loops(word):
    return all(a == b for a,b in word)


def check_representative(E,partition):
    T = [tuple(sorted((a,b,6+j))) for j,(a,b) in enumerate(E)]
    rows = [[int(i<6) for i in range(12)], [int(i>=6) for i in range(12)]]
    rows += [[t.count(i) for i in range(12)] for t in T]
    M = sp.Matrix(rows)
    assert M.rank()-2 == 5
    kernel = M.nullspace()
    alltriples = list(itertools.combinations_with_replacement(range(12),3))
    closed = [t for t in alltriples if all(sum(v[c] for c in t)==0 for v in kernel)]
    extra = set(closed)-set(T)
    expected = 2**len(partition) if all(n%2==0 for n in partition) else 0
    assert len(extra)==expected
    assert all(all(c>=6 for c in t) for t in extra)
    assert all([sum(t.count(c) for t in T) for c in range(12)][c] == (2 if c<6 else 1) for c in range(12))
    return dict(pair_edges=E, T=T, rank=5, closure_extra_BBB=sorted(extra),
                mixed_only_exact=(not extra))


def ledger():
    graphs = graph_domain()
    grouped = defaultdict(list)
    for E, partition in graphs.items():
        grouped[partition].append(E)
    result = []
    for partition, collection in sorted(grouped.items(),reverse=True):
        closed = any(n%2 for n in partition)
        words = failures = 0
        if closed:
            for E in collection:
                orders = {cyclic_word(tuple(p)) for p in set(itertools.permutations(E))}
                words += len(orders)
                failures += sum(all_loops(w) for w in orders)
        result.append(dict(component_partition=partition, labeled_graphs=len(collection),
                           mixed_only_exact=bool(closed), B_dihedral_words=words,
                           analytic_loop_exclusions=failures,
                           representative=check_representative(collection[0],partition)))
    assert sum(r['labeled_graphs'] for r in result)==388
    assert sum(r['labeled_graphs'] for r in result if r['mixed_only_exact'])==268
    assert sum(r['B_dihedral_words'] for r in result)==11850
    assert sum(r['analytic_loop_exclusions'] for r in result)==60
    return dict(scope='Complete pair-graph and B-word domain before A-dihedral quotient; no spatial or metric census',
                total_regular_graphs=388, mixed_only_graphs=268, B_dihedral_words=11850,
                analytic_loop_exclusions=60, remaining_words=11790, ledger=result)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path); p.add_argument('--check',type=Path)
    args=p.parse_args(); result=ledger()
    normalized=json.loads(json.dumps(result))
    if args.check:
        assert json.loads(args.check.read_text())==normalized
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='ledger'}))
    print(json.dumps([{k:v for k,v in r.items() if k!='representative'} for r in result['ledger']]))

if __name__=='__main__':
    main()
