#!/usr/bin/env python3
"""Same35point domain, add exact degree2 straight collapses; no new patch."""
import runpy,io,json
from contextlib import redirect_stdout
from itertools import combinations,product
with redirect_stdout(io.StringIO()):old=runpy.run_path('research/reviews/check_penrose_dual_fusion_angle_palette.py')
P=old['P'];D=old['D'];phase=old['phase'];rows=[];collapsed=[]
for row in old['reconstructed']:
    r=row['rhomb'];ns=row['cyclic_neighbor_ids'];choices=[]
    for i,j in combinations(range(4),2):
        if phase((P[ns[j]]-P[r])/(P[ns[i]]-P[r]))==-1:
            choices.append({'retained_neighbor_ids':[ns[i],ns[j]],'angle_ids':[]})
    if choices:collapsed.append({'rhomb':r,'opposite_neighbor_pairs':[c['retained_neighbor_ids'] for c in choices]})
    rows.append({**row,'choices':choices+row['choices']})
signatures=[]
for row in rows:
    s=tuple(tuple(c['angle_ids']) for c in row['choices'])
    if s not in signatures:signatures.append(s)
B=json.loads(open('research/certificates/penrose-dual-fusion-exterior-budget.json').read());bounds=B['floor_exterior_degrees']
minimum=10**9;union_witness=None;choice_witness=None;count=0;hist={}
for selected in product(*signatures):
    count+=1;union=set().union(*(set(c) for c in selected));cost=sum(bounds[i] for i in union)
    hist[cost]=hist.get(cost,0)+1
    if cost<minimum:minimum=cost;union_witness=sorted(union);choice_witness=selected
out={'domain':'same35 fully interior rhombpoints; size2 exactly opposite rays plus previous convex/flat size3/4 subsets; degree0/1 forbidden',
     'point_count':len(rows),'opposite_ray_points':collapsed,'point_choices':rows,
     'distinct_signature_choice_counts':[len(s) for s in signatures],'enumerated_products':count,
     'minimum_integer_exterior_bound':minimum,'minimum_witness_angle_ids':union_witness,
     'minimum_signature_choices':choice_witness,'cost_histogram':dict(sorted(hist.items())),
     'two_shape_budget':720,'negative_budget_certificate':minimum>720,
     'scope':'local independent choices only; sharededge retention consistency not imposed'}
print(json.dumps(out,indent=2))
