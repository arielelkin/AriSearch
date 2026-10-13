#!/usr/bin/env python3
"""Exact controls for angular filter; explicit full-domain logic at pairings.
Independent recognition uses native colour multiplicities. Finite8100 generic
bracelet-labelled arrangements, plus miniature CP controls and type-kernel.
"""
import importlib.util,json
from itertools import permutations,combinations_with_replacement
from pathlib import Path
from ortools.sat.python import cp_model
import sympy as s
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('angular_cut',root/'research/searches/two-hexagon-ternary-angular-filter.py')
cut=importlib.util.module_from_spec(spec);spec.loader.exec_module(cut)
words=sorted(set(permutations((0,0,1,1,2,2))))
assert len(words)==90
values=(111,121,128);other=tuple(360-2*x for x in values)
# Evaluate the actual mathematical conjunctions used by the fifteen guards.
def guard(a,b):
    return any(all(a[i]==a[j] for i,j in pairs) and
      len({a[i] for i,j in pairs})==3 and
      all(90<a[i]<180 and a[i]!=120 and b.count(360-2*a[i])==2 for i,j in pairs)
      for pairs in cut.MATCHINGS)
for wa in words:
 for wb in words:
    a=[values[i] for i in wa];b=[other[i] for i in wb]
    assert guard(a,b) and cut.covered(a+b,1)
controls=[(values+values,other+other,True),
          ((120,)*6,(120,)*6,False),
          ((110,110,110,110,140,140),(140,140,140,140,80,80),False),
          ((123,123,105,105,132,132),(114,114,114,114,114,150),False),
          (values+values,(138,138,118,118,104,104),True),
          (values+values,(137,139,118,118,104,104),False)]
for a,b,expected in controls:
 for swapped in (False,True):
    full=list(b+a if swapped else a+b)
    assert cut.covered(full,1)==expected
    m=cp_model.CpModel();v=[m.NewIntVar(1,179,'a%d'%i) for i in range(12)]
    for var,val in zip(v,full):m.Add(var==val)
    cut.add_filter(m,v,1);solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
    status=solver.Solve(m)
    assert (status==cp_model.INFEASIBLE)==expected
    assert status in(cp_model.OPTIMAL,cp_model.INFEASIBLE)
# Kernel of complete five-star core forces the family relations for any exact
# representative of its type. Constants center at120, so all rows homogeneous.
colours=(0,0,1,1,2,2)*2
triples=[]
for t in combinations_with_replacement(range(12),3):
    species=[i//6 for i in t];cols=[colours[i] for i in t]
    legal=(species==[0,0,0] or species==[1,1,1]) and sorted(cols)==[0,1,2]
    legal=legal or (species==[0,0,1] and len(set(cols))==1)
    if legal:triples.append(t)
rows=[]
for t in triples:
 row=[0]*12
 for i in t:row[i]+=1
 rows.append(row)
rows += [[1]*6+[0]*6,[0]*6+[1]*6]
M=s.Matrix(rows);assert len(triples)==34 and M.rank()==10
basis=s.Matrix([[1,0],[1,0],[0,1],[0,1],[-1,-1],[-1,-1],[-2,0],[-2,0],[0,-2],[0,-2],[2,2],[2,2]])
assert M*basis==s.zeros(M.rows,2) and basis.rank()==2
print('PASS:8100 native arrangements,12 exact miniature CP controls,34-star rank10/two-dimensional family kernel')
