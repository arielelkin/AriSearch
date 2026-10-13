#!/usr/bin/env python3
"""Independent straight-collapse geometry and40-step arc proof replay.
No producer imports, solver calls, floats, output writers or search bounds.
"""
import json,runpy
from pathlib import Path
from itertools import combinations,product
weighted=runpy.run_path('research/reviews/check_penrose_dual_fusion_exterior_budget.py')
base=weighted['base'];P=base['P'];phase=base['phase'];bounds=weighted['bounds']
C=json.loads(Path('research/certificates/penrose-dual-fusion-opposite-ray-collapse.json').read_text())
rows=[];collapsed=[]
for row in base['reconstructed']:
    r=row['rhomb'];ns=row['cyclic_neighbor_ids'];choices=[]
    for i,j in combinations(range(4),2):
        if phase((P[ns[j]]-P[r])/(P[ns[i]]-P[r]))==-1:
            choices.append({'retained_neighbor_ids':[ns[i],ns[j]],'angle_ids':[]})
    if choices:collapsed.append({'rhomb':r,'opposite_neighbor_pairs':[c['retained_neighbor_ids'] for c in choices]})
    rows.append({**row,'choices':choices+row['choices']})
assert rows==C['point_choices'] and collapsed==C['opposite_ray_points'] and len(collapsed)==10
signatures=[]
for row in rows:
    s=tuple(tuple(c['angle_ids']) for c in row['choices'])
    if s not in signatures:signatures.append(s)
assert [len(s) for s in signatures]==[5,3,3,3,5,3]
minimum=10**9;count=0;hist={};witness=None
for selected in product(*signatures):
    count+=1;union=set().union(*(set(c) for c in selected));cost=sum(bounds[a] for a in union)
    hist[str(cost)]=hist.get(str(cost),0)+1
    if cost<minimum:minimum=cost;witness=sorted(union)
assert count==2025 and minimum==605==C['minimum_integer_exterior_bound']
assert witness==C['minimum_witness_angle_ids'] and hist==C['cost_histogram']
assert minimum+len(witness)==616<720
T=json.loads(Path('research/certificates/penrose-dual-collapse-shared-edge-arc-certificate.json').read_text())
R={r['rhomb']:r for r in rows};domains={r:set(range(len(row['choices']))) for r,row in R.items()}
for step in T['elimination_trace']:
    r=step['rhomb'];n=step['neighbor'];assert n in R and n in R[r]['cyclic_neighbor_ids']
    assert sorted(domains[n])==step['neighbor_domain']
    support={int(r in R[n]['choices'][j]['retained_neighbor_ids']) for j in domains[n]}
    rejected=sorted(i for i in domains[r] if int(n in R[r]['choices'][i]['retained_neighbor_ids']) not in support)
    assert rejected==step['removed_choice_ids'] and rejected
    domains[r].difference_update(rejected)
assert len(T['elimination_trace'])==40
assert {str(r):sorted(v) for r,v in domains.items()}==T['remaining_domains']
forced=set();by_point={}
for r,row in R.items():
    assert domains[r]
    for n in row['cyclic_neighbor_ids']:
        if n not in R:continue
        support={int(r in R[n]['choices'][j]['retained_neighbor_ids']) for j in domains[n]}
        assert all(int(n in row['choices'][i]['retained_neighbor_ids']) in support for i in domains[r])
    req=set.intersection(*(set(row['choices'][i]['angle_ids']) for i in domains[r]));forced|=req;by_point[str(r)]=sorted(req)
assert by_point==T['forced_angles_per_point'] and sorted(forced)==T['forced_angle_ids']
cost=sum(bounds[a] for a in forced)
assert cost==750==T['certified_exterior_floor_sum'] and cost>720 and T['negative_certificate']
print('PASS: ten exact straight-collapse points; 2025 independent unions permit605-degree lower bound;40 sound shared-edge eliminations force11 distinct native angles costing at least750>720 degrees. No CSP solver verdict used.')
