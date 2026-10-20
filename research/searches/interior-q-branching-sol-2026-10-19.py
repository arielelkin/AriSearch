"""Arithmetic certificate for the analytic six-interior-core obstruction; no graph enumeration."""
import json
from pathlib import Path

def partitions(total, lower=1):
    if total == 0:
        yield ()
    for s in range(lower, total+1):
        for tail in partitions(total-s, s):
            yield (s,)+tail

def planar_cap(n):
    return 0 if n == 1 else 1 if n == 2 else 3*n-6

cut_cases = [dict(block_sizes=list(p),edge_cap=sum(planar_cap(s+1) for s in p))
             for p in partitions(5) if len(p)>=2]
disconnected = [dict(component_sizes=list(p),edge_cap=sum(planar_cap(s) for s in p))
                for p in partitions(6) if len(p)>=2]
assert max(x['edge_cap'] for x in cut_cases)==10
assert max(x['edge_cap'] for x in disconnected)==9
budgets={}
for parent,n,b,qmax in [('P',13,7,2),('Q',12,6,3)]:
    E=3*n-b-3
    base=30-E+b
    budgets[parent]=dict(children=n,boundary=b,interior=6,edges=E,
                         triangles=2*n-b-2,core_edge_base=base)
    assert base == (8 if parent=='P' else 9)
assert 9+2>10
for e in [11,12]:
    hull=15-e
    deep=6-hull
    forced_edges=deep*hull+deep*(deep-1)//2+hull
    assert forced_edges>e
out=dict(status='PASS arithmetic only; planar proof in adjacent Markdown',
         budgets=budgets,cut_vertex_cases=cut_cases,disconnected_cases=disconnected,
         graph_enumeration=False)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
