"""Exact shared-angle SMT gate for the two eight-child P7+H6 disks.
No metric, existence, or aperiodicity inference; retain all native phases/mirrors.
"""
import json
import z3
from pathlib import Path
alpha,beta=z3.Reals('alpha beta')
P=[120,alpha,beta,240-beta,180-alpha]
H=[beta,240-beta]*3
base={
 0:['b0','b1','t01','tu0','t50'],
 1:['b1','b2','t12','t01'],
 2:['b2','b3','t23','t12'],
 3:['b3','b4','t34','tu3','t23'],
 4:['b4','b5','t45','t34'],
 5:['b5','b0','t50','t45'],
 6:['t01','t12','t23','tu3','tu0'],
 7:['tu0','tu3','t34','t45','t50']}
results=[]
for htile,counts in [(0,[1,1,1,0,1,1]),(1,[0,2,1,0,1,1])]:
 solver=z3.Solver();solver.set(timeout=120000)
 solver.add(alpha>0,alpha<180,beta>60,beta<180)
 words={};corners=[]
 for tile,nodes in base.items():
  nodes=nodes[:]
  if tile<6:
   cc=[f'c{tile}_{j}' for j in range(counts[tile])]
   nodes=nodes[:1]+cc+nodes[1:];corners+=cc
  assert len(nodes)==(6 if tile==htile else 5)
  words[tile]=nodes
 assert len(corners)==5
 phases={};angles={}
 for tile,nodes in words.items():
  native=H if tile==htile else P;n=len(native)
  phase=z3.Int(f'phase_{htile}_{tile}');phases[tile]=phase
  solver.add(phase>=0,phase<2*n)
  for j,node in enumerate(nodes):
   values=[native[(off+sign*j)%n] for sign in (1,-1) for off in range(n)]
   angles[tile,node]=z3.Sum([z3.If(phase==q,value,0) for q,value in enumerate(values)])
 parent=z3.Int(f'parent_{htile}');solver.add(parent>=0,parent<10)
 for j,node in enumerate(corners):
  target=z3.Sum([z3.If(parent==q,P[(off+sign*j)%5],0) for q,(sign,off) in enumerate((s,o) for s in (1,-1) for o in range(5))])
  solver.add(z3.Sum([a for (tile,label),a in angles.items() if label==node])==target)
 for node in set(label for _,label in angles)-set(corners):
  incidences=[a for (tile,label),a in angles.items() if label==node]
  assert len(incidences)==(2 if node.startswith('b') else 3)
  solver.add(z3.Sum(incidences)==(180 if node.startswith('b') else 360))
 result=solver.check();record={'H_tile':htile,'result':str(result),'words':words}
 if result==z3.sat:
  model=solver.model();record.update(alpha=str(model.eval(alpha)),beta=str(model.eval(beta)),parent_phase=model.eval(parent).as_long(),phases={i:model.eval(v).as_long() for i,v in phases.items()})
  # Exact rational substitution checks every asserted condition independently of solver.check.
  assert all(z3.is_true(model.eval(c,model_completion=True)) for c in solver.assertions())
 results.append(record);print(json.dumps(record),flush=True)
Path('research/searches/astra-eight-child-angle-gate-2026-10-20.json').write_text(json.dumps(results,indent=2)+'\n')
