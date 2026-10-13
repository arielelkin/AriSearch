#!/usr/bin/env python3
"""Fixed-fixture necessary local angle-palette gate; no patch enlargement.
All fully surrounded rhomb points, degree3/4 ray subsets, flat sectors relaxed.
"""
import json,io,runpy
from contextlib import redirect_stdout
from itertools import combinations
from sage.all import QQbar
from ortools.sat.python import cp_model
with redirect_stdout(io.StringIO()):data=runpy.run_path('research/searches/penrose-dual-fusion-thin-deformation.py')
points=data['points']; rhombs=data['d']['rhombs']; edges=data['edges']; sign=data['sign']; cross=data['cross']; emb=data['emb']; encode=data['encode']
angle_values=[]; angle_sources=[]; rows=[]
for r,(_,vs,_) in enumerate(rhombs):
    ns=[]
    for i in range(4):
        incident=edges[tuple(sorted((vs[i],vs[(i+1)%4])))]; ns.append(next((a for a in incident if a!=r),None))
    if None in ns:continue
    # Source edge order gives radial cyclic order because every crossing is inside edge.
    orientation=sign(sum(cross(data['verts'][vs[i]],data['verts'][vs[(i+1)%4]]) for i in range(4)))
    if orientation<0:ns.reverse()
    choices=[]
    for degree in (3,4):
        for subset in combinations(range(4),degree):
            selected=[ns[i] for i in subset]; ids=[]; phases=[]; ok=True
            for i in range(degree):
                a=points[selected[i]]-points[r]; b=points[selected[(i+1)%degree]]-points[r]
                z=emb(b/a); z=z/(z*z.conjugate()).real().sqrt()
                if z.imag()<0 or (z.imag()==0 and z.real()!=-1):ok=False;break
                if z.imag()==0:continue # pi flat sector, allowed relaxation
                if z not in angle_values:
                    angle_values.append(z); angle_sources.append({'center':r,'incoming':selected[i],'outgoing':selected[(i+1)%degree],'raw_ratio':encode(b/a)})
                ids.append(angle_values.index(z))
            if ok:choices.append({'retained_neighbor_ids':selected,'angle_ids':sorted(set(ids))})
    rows.append({'rhomb':r,'cyclic_neighbor_ids':ns,'choices':choices})
model=cp_model.CpModel(); x=[model.new_bool_var(f'a{i}') for i in range(len(angle_values))]
for row in rows:
    ys=[model.new_bool_var(f'p{row["rhomb"]}c{i}') for i in range(len(row['choices']))]
    model.add_exactly_one(ys)
    for y,choice in zip(ys,row['choices']):
        for a in choice['angle_ids']:model.add(x[a]>=y)
model.minimize(sum(x)); solver=cp_model.CpSolver();solver.parameters.num_search_workers=1;solver.parameters.max_time_in_seconds=30
status=solver.solve(model)
out={'domain':'all fully surrounded rhombpoints of retained 3-deflation fixture; size3/4 retained ray subsets; exact convex/flat-sector test',
     'point_count':len(rows),'angle_value_count':len(angle_values),'point_choices':rows,'exact_angle_sources':angle_sources,
     'solver':'CP-SAT one worker, 30 second cap','status':solver.status_name(status),
     'minimum_palette':int(solver.objective_value) if status in (cp_model.OPTIMAL,cp_model.FEASIBLE) else None,
     'bound':solver.best_objective_bound,
     'selected_angle_ids':[i for i,z in enumerate(x) if solver.value(z)] if status in (cp_model.OPTIMAL,cp_model.FEASIBLE) else None}
print(json.dumps(out,indent=2))
