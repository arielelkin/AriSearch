#!/usr/bin/env python3
"""Same35 point degree2/3/4 relaxation with shared network-edge retention.
Outside35 nodes unconstrained; no polygon congruence/infinite extension modeled.
"""
import json
from pathlib import Path
from ortools.sat.python import cp_model
C=json.loads(Path('research/certificates/penrose-dual-fusion-opposite-ray-collapse.json').read_text())
B=json.loads(Path('research/certificates/penrose-dual-fusion-exterior-budget.json').read_text());bounds=B['floor_exterior_degrees']
model=cp_model.CpModel(); angle=[model.new_bool_var(f'a{i}') for i in range(len(bounds))];edges={};ys={}
for row in C['point_choices']:
    r=row['rhomb'];y=[model.new_bool_var(f'p{r}c{i}') for i in range(len(row['choices']))];ys[r]=y;model.add_exactly_one(y)
    for n in row['cyclic_neighbor_ids']:
        edge=tuple(sorted((r,n)))
        if edge not in edges:edges[edge]=model.new_bool_var(f'e{edge[0]}_{edge[1]}')
        model.add(edges[edge]==sum(y[i] for i,c in enumerate(row['choices']) if n in c['retained_neighbor_ids']))
    for i,c in enumerate(row['choices']):
        for a in c['angle_ids']:model.add(angle[a]>=y[i])
model.minimize(sum(d*a for d,a in zip(bounds,angle)))
solver=cp_model.CpSolver();solver.parameters.num_search_workers=1;solver.parameters.max_time_in_seconds=30
status=solver.solve(model);positive=status in (cp_model.FEASIBLE,cp_model.OPTIMAL)
selected={str(r):next(i for i,y in enumerate(v) if solver.value(y)) for r,v in ys.items()} if positive else None
used=set()
if positive:
    for row in C['point_choices']:used.update(row['choices'][selected[str(row['rhomb'])]]['angle_ids'])
cost=sum(bounds[a] for a in used);upper=cost+len(used)
out={'domain':'same35 complete rhombpoints; all certified size2 opposite/size3/4 convex choices; both ends of shared networkedge have identical retention; exteriorangle native union; outside nodes unconstrained',
     'solver':'CP-SAT singleworker 30second cap','status':solver.status_name(status),
     'minimum_integer_bound':cost if positive else None,'solver_lower_bound':solver.best_objective_bound,
     'selected_choice_per_rhomb':selected,'used_angle_ids':sorted(used) if positive else None,
     'strict_actual_deficit_upper_bound':upper if positive else None,
     'retained_edge_values':{'-'.join(map(str,e)):int(solver.value(x)) for e,x in edges.items()} if positive else None,
     'scope':'local necessary realization only; no final polygons, shapecongruences, infiniteextension or forcing'}
print(json.dumps(out,indent=2))
