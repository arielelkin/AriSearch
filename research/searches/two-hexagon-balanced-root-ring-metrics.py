#!/usr/bin/env python3
"""Periodic escapes under each locally forced B-ring side equivalence.

Each query uses one equality closure forced by a surviving local ring.
An independently checked torus is a periodic escape for every coarser e.
Failure/UNKNOWN is not a global exclusion.
"""
import importlib.util,itertools,json,sys,time
from fractions import Fraction
from pathlib import Path
from ortools.sat.python import cp_model
import ortools

spec=importlib.util.spec_from_file_location('sft',Path('research/searches/two-hexagon-global-sft.py'))
sft=importlib.util.module_from_spec(spec);spec.loader.exec_module(sft)
PLACEMENTS=[(r,s) for s in (1,-1) for r in range(6)]
def side(p,k):
    r,d=p
    return (r+k)%6 if d==1 else (r-k-1)%6
def metric(state):
    B=state['B'];A=[PLACEMENTS[i] for i in state['A_ring']]
    equalities=[]
    for k in range(6):
        equalities.append((6+side(B,k-1),side(A[k],k+2)))
        equalities.append((side(A[k],k+1),side(A[(k+1)%6],k+4)))
    parent=list(range(12))
    def find(a):
        while parent[a]!=a:a=parent[a]
        return a
    for a,b in equalities:
        a,b=find(a),find(b)
        parent[max(a,b)]=min(a,b)
    return tuple(find(i) for i in range(12)),equalities

def solve_torus(model,lat,timeout=3):
    n,s,height=lat
    def wrap(z):
        x,y=z;q=y//height
        return ((x-s*q)%n,y-q*height)
    cells=[(x,y) for x in range(n) for y in range(height)]
    m,X=model.model(cells,wrap)
    solver=cp_model.CpSolver();solver.parameters.num_workers=1
    solver.parameters.random_seed=0;solver.parameters.max_time_in_seconds=timeout
    status=solver.Solve(m)
    row={'lattice':lat,'status':solver.StatusName(status),'wall_time_seconds':solver.WallTime()}
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        sol={z:solver.Value(v) for z,v in X.items()}
        assert sft.check_torus(model,lat,sol)
        row['labels']=[[x,y,sol[x,y]] for x,y in cells]
    return row

def main(source,outpath):
    data=json.loads(Path(source).read_text())
    report={'source':source,'scope':'Every distinct forced side-equivalence of an arc-consistent B-ring; tori of index3 or6, the only multiples of3 <=8.',
            'ortools_version':ortools.__version__,'seed':0,'workers':1,'timeout_per_query_seconds':3,'rows':[]}
    offsets=[1,10,100,1000,10000,-11111]
    for row in data['rows']:
        if not row['surviving_states']:continue
        if 'graphs' in data:
            if row['verdict']!='BRANCHING':continue
            if data['graphs'][row['graph_id']]['components']==[3,3]:continue
        if 'T' not in row:
            row['T']=[list(pair)+[6+i] for i,pair in enumerate(row['B_pair_order'])]
        angles=[Fraction(120)+Fraction(d,1000) for d in offsets]
        angles += [Fraction(360)-angles[a]-angles[b] for a,b in row['B_pair_order']]
        assert {t for t in itertools.combinations_with_replacement(range(12),3) if sum(angles[i] for i in t)==360}=={tuple(sorted(t)) for t in row['T']}
        metrics={}
        for state_index in row['surviving_states']:
            classes,eqs=metric(row['states'][state_index])
            metrics.setdefault(classes,{'state_indices':[],'one_ring_equalities':eqs})['state_indices'].append(state_index)
        result={'id':row['id'],'queries':[]}
        for classes,info in metrics.items():
            model=sft.SFT([angles[:6],angles[6:]],[list(classes[:6]),list(classes[6:])])
            query={'length_classes':classes,**info,'torus_queries':[],'verdict':'NO_TORUS_AT_INDEX_LE_8'}
            for N in (3,6):
                done=False
                for n in range(1,N+1):
                    if N%n:continue
                    for shear in range(n):
                        trial=solve_torus(model,(n,shear,N//n))
                        query['torus_queries'].append(trial)
                        if 'labels' in trial:
                            query['verdict']='PERIODIC_ESCAPE';done=True;break
                    if done:break
                if done:break
            if query['verdict']!='PERIODIC_ESCAPE' and any(t['status']=='UNKNOWN' for t in query['torus_queries']):query['verdict']='UNKNOWN'
            result['queries'].append(query)
            print(row['id'],'metric',classes,query['verdict'],flush=True)
            report['rows']=[r for r in report['rows'] if r['id']!=result['id']]+[result]
            Path(outpath).write_text(json.dumps(report,separators=(',',':')))
        print('DONE ROOT',row['id'],'metrics',len(metrics),flush=True)
    print('FINAL',len(report['rows']),'roots',sum(len(r['queries']) for r in report['rows']),'metric closures',flush=True)

if __name__=='__main__':main(*sys.argv[1:3])
