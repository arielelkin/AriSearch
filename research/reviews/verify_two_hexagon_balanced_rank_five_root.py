#!/usr/bin/env python3
"""Exact balanced minimal covering rank-five example and narrow SFT test."""
import itertools,json,importlib.util
from fractions import Fraction
from pathlib import Path
from sage.all import QQ, matrix, vector

T=[(0,1,6),(1,2,7),(0,2,8),(3,4,9),(4,5,10),(3,5,11)]
alltriples=list(itertools.combinations_with_replacement(range(12),3))
def counts(t):
    return vector(QQ,[t.count(i) for i in range(12)])
base=[vector(QQ,[int(i<6) for i in range(12)]),vector(QQ,[int(i>=6) for i in range(12)])]
def closure(gs):
    M=matrix(QQ,base+[counts(t) for t in gs])
    S=M.row_space()
    return M.rank()-2,[t for t in alltriples if counts(t) in S]

rank,closed=closure(T)
assert rank==5 and set(closed)==set(T)
balance=sum((QQ(1)/3*counts(t) for t in T),vector(QQ,[0]*12))
assert balance==QQ(2)/3*base[0]+QQ(1)/3*base[1]
assert all(sum(c in t for t in T)==1 for c in range(6,12))
subsets_checked=0
for size in (1,2,3):
    for gs in itertools.combinations(T,size):
        _,closed_subset=closure(gs)
        assert set(c for t in closed_subset for c in t)!=set(range(12))
        subsets_checked+=1
assert subsets_checked==41
offsets=[1,10,100,1000,10000,-11111,-11,-110,-101,-11000,1111,10111]
angles=[Fraction(120)+Fraction(d,1000) for d in offsets]
assert sum(angles[:6])==sum(angles[6:])==720
assert all(0<a<180 for a in angles)
assert {t for t in alltriples if sum(angles[i] for i in t)==360}==set(T)
out={'T':T,'rank_mod_polygon_sums':rank,'closure':closed,
     'weights':['1/3']*6,'species_weights':['2/3','1/3'],
     'rank_le_three_generator_subsets_checked':subsets_checked,
     'rank_le_three_covering_ancestors':0,
     'generic_angles_degrees':[str(a) for a in angles]}
print('PASS: exact balanced rank-five root, closure six triples, no covering proper ancestor.',flush=True)

path=Path('research/searches/two-hexagon-global-sft.py')
spec=importlib.util.spec_from_file_location('angle_sft',path)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sft=module.SFT([angles[:6],angles[6:]],[[0]*6,[0]*6])
# Independent finite cycle CSP for the six neighbours of a B cell. It uses
# only the native corner formulas, not CP-SAT or SFT.vertex_ok.
native_A=[(r,d) for d in (1,-1) for r in range(6)]
star_rows=[]
for br,bd in native_A:
    relations=[]
    for k in range(6):
        bc=6+(br+bd*k)%6
        rel=[]
        for i,(ar,ad) in enumerate(native_A):
            for j,(cr,cd) in enumerate(native_A):
                t=tuple(sorted(((ar+ad*(k+2))%6,(cr+cd*(k+4))%6,bc)))
                if t in T:rel.append((i,j))
        relations.append(rel)
    solutions=[]
    def walk(path):
        k=len(path)-1
        if k==5:
            if (path[-1],path[0]) in relations[5]:solutions.append(path)
            return
        for a,b in relations[k]:
            if a==path[-1]:walk(path+[b])
    for first in range(12):walk([first])
    star_rows.append({'B_placement':[br,bd],'relations':relations,'cycle_solutions':solutions})
out['exact_B_star_cycle_audit']=star_rows
assert all(len(row['cycle_solutions'])==1 for row in star_rows)
print('exact B-star ring cycles:',[len(row['cycle_solutions']) for row in star_rows],flush=True)
compatible_B_pairs=[]
for first in star_rows:
    for second in star_rows:
        for a in first['cycle_solutions']:
            for b in second['cycle_solutions']:
                if a[0]==b[4] and a[1]==b[3]:
                    compatible_B_pairs.append([first['B_placement'],second['B_placement']])
out['opposite_B_stars_shared_A_edge_compatible_pairs']=compatible_B_pairs
print('opposite B stars compatible:',len(compatible_B_pairs),flush=True)
direction_relations=[]
for k in range(6):
    options=[]
    for i,first in enumerate(star_rows):
        for j,second in enumerate(star_rows):
            for a in first['cycle_solutions']:
                for b in second['cycle_solutions']:
                    if a[k]==b[(k+4)%6] and a[(k+1)%6]==b[(k+3)%6]:options.append((i,j))
    direction_relations.append(options)
possible_centers=set(range(12))
for options in direction_relations:possible_centers&={i for i,j in options}
out['six_direction_B_pair_relations']=direction_relations
out['B_states_with_all_six_required_neighbors']=sorted(possible_centers)
assert not possible_centers
assert not ({i for i,j in direction_relations[0]} & {i for i,j in direction_relations[1]})
print('B states admitting all six B neighbours:',sorted(possible_centers),flush=True)
from ortools.sat.python import cp_model
import ortools
out['sft_test']={'scope':'Declared native corner ordering, all side classes equal (angle-only superset); no relabeling census or geometric realisability claim.',
                 'ortools_version':ortools.__version__,'workers':1,'seed':0,
                 'timeout_per_query_seconds':30,'patches':[]}
for radius in (1,2,3):
    cells=[(x,y) for x in range(-radius,radius+1) for y in range(-radius,radius+1)
           if max(abs(x),abs(y),abs(x+y))<=radius]
    model,X=sft.model(cells)
    solver=cp_model.CpSolver()
    solver.parameters.num_workers=1
    solver.parameters.random_seed=0
    solver.parameters.max_time_in_seconds=30
    status=solver.Solve(model)
    label=solver.StatusName(status)
    row={'radius':radius,'cells':len(cells),'status':label,'wall_time_seconds':solver.WallTime()}
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        solution={z:solver.Value(v) for z,v in X.items()}
        for z in cells:
            for k in (0,1):
                zs=[z,module.add(z,module.D[k]),module.add(z,module.D[k+1])]
                if all(q in solution for q in zs):
                    assert sft.vertex_ok(*(sft.syms[solution[q]] for q in zs),k)
        row['labels']=[[x,y,solution[x,y]] for x,y in cells]
    out['sft_test']['patches'].append(row)
    print('angle-only patch',radius,label,flush=True)
    if status==cp_model.INFEASIBLE:
        break
out['sft_test']['tori']=[]
for index in range(1,9):
    for n in range(1,index+1):
        if index%n:continue
        height=index//n
        for shear in range(n):
            def wrap(z):
                x,y=z
                q=y//height
                return ((x-shear*q)%n,y-q*height)
            cells=[(x,y) for x in range(n) for y in range(height)]
            model,X=sft.model(cells,wrap)
            solver=cp_model.CpSolver()
            solver.parameters.num_workers=1
            solver.parameters.random_seed=0
            solver.parameters.max_time_in_seconds=5
            status=solver.Solve(model)
            row={'lattice':[n,shear,height],'status':solver.StatusName(status),
                 'timeout_seconds':5,'wall_time_seconds':solver.WallTime()}
            if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
                solution={z:solver.Value(v) for z,v in X.items()}
                assert module.check_torus(sft,(n,shear,height),solution)
                row['labels']=[[x,y,solution[x,y]] for x,y in cells]
            out['sft_test']['tori'].append(row)
print('tori index <=8:',len(out['sft_test']['tori']),'queries',
      sorted(set(row['status'] for row in out['sft_test']['tori'])),flush=True)
Path('research/certificates/two-hexagon-balanced-minimal-covering-root.json').write_text(json.dumps(out,indent=2)+'\n')
