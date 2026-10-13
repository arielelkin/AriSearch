#!/usr/bin/env python3
"""Fixed-point controls for both species/six ABB lines and API boundaries.
No global angular query. Exact native type matrices independently reconstructed.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import importlib.util
import sympy as s
from ortools.sat.python import cp_model
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("cut",root/"research/searches/two-hexagon-ternary-angular-filter.py")
cut=importlib.util.module_from_spec(spec);spec.loader.exec_module(cut)

def control(a,b,grid,expected,swap=False):
    full=list(b+a if swap else a+b)
    assert cut.covered([q*grid for q in full],grid)==expected
    m=cp_model.CpModel();v=[m.NewIntVar(-1000*grid,1000*grid,"v%d"%i) for i in range(12)]
    for x,q in zip(v,full):m.Add(x==q*grid)
    cut.add_filter(m,v,grid);solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
    status=solver.Solve(m)
    assert status==(cp_model.INFEASIBLE if expected else cp_model.OPTIMAL)

count=0
for i in range(3):
    for j in range(3):
        if i==j:continue
        x=[0,0,0];x[j]=121;x[i]=124;x[3-i-j]=115
        y=[360-2*q for q in x]
        ac=(0,0,1,1,2,2);bc=(0,1,2,0,2,1)
        a=tuple(x[k] for k in ac);b=tuple(y[k] for k in bc)
        for swap in (False,True):
            for grid in (1,7):control(a,b,grid,True,swap);count+=1
            angles=b+a if swap else a+b
            cols=bc+ac if swap else ac+bc
            pivot=1 if swap else 0
            full=[t for t in combinations_with_replacement(range(12),3) if sum(angles[k] for k in t)==360]
            core=[]
            for t in full:
                sp=[k//6 for k in t];cs=[cols[k] for k in t]
                base=(len(set(sp))==1 and sorted(cs)==[0,1,2]) or (sp.count(pivot)==2 and len(set(cs))==1)
                if base:core.append(t)
            assert len(core)==34 and len(full)==40
            def mat(ts):
                rows=[]
                for t in ts:
                    r=[0]*12
                    for k in t:r[k]+=1
                    rows.append(r)
                return s.Matrix(rows)
            assert mat(core).rank()==10 and mat(full).rank()==11
            # Full type excludes native triples that would merge A colours or give120.
            rep=[6*pivot+ac.index(k) for k in range(3)]
            assert all((k,k,k) not in full for k in rep)
            assert all(tuple(sorted((rep[k],rep[k],rep[3-k-l]))) not in full
                       for k in range(3) for l in range(3) if k!=l)
# Repaired upper bound: the former implicit positivity inference is unnecessary.
for a,b in (((190,200,210)*2,(-20,-40,-60)*2),
            ((90,121,149)*2,(180,118,62)*2),
            ((120,110,130)*2,(120,140,100)*2)):
    for swap in (False,True):control(a,b,1,False,swap);count+=1
assert count==30
print("PASS:24 six-ABB/species/grid controls, six repairedAPI boundary controls; all native cores rank10 and full ABB types rank11 with no degeneracy triples")
