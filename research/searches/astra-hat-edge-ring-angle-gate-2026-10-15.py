#!/usr/bin/env python3
"""Named fixed hat-ring necessary angle gates only; no metric or tilability claim."""
import json,sys
from z3 import Solver,Real,Sum,Or,And,sat
p=[Real('p'+str(i)) for i in range(5)];q=[Real('q'+str(i)) for i in range(6)]
mixed='--mixed' in sys.argv
split='--split-center' in sys.argv
outer='--split-outer1' in sys.argv
seven='--mixed-center7' in sys.argv
k,l=(1,5) if mixed or split or outer or seven else (tuple(map(int,sys.argv[1:])) if len(sys.argv)>1 else (1,5))
assert k in(1,2) and l in(5,6)
arcs=[['h'+str(i) for i in range(0,k+1)]+['W'],['W']+['h'+str(i) for i in range(k+1,5)],['h'+str(i) for i in range(4,l+1)]+['U'],['U']+['h'+str(i) for i in range(l+1,9)],['h8','h9','h10','h11'],['h11','h12','h0']]
if mixed:arcs[:2]=[['h0','h1','h2'],['h2','h3','h4']]
words={'Qc':['z'+str(i) for i in range(6)]}
for i,a in enumerate(arcs):
 w=a+['z'+str((i+1)%6),'z'+str(i)]
 words[('P' if len(w)==5 else 'Q')+str(i)]=w
if split:
 del words['Qc']
 words['Pc0']=['r','z1','z2','z3','s']
 words['Pc1']=['s','z4','z5','z0','r']
if outer:
 del words['Q1']
 words['Pa']=['r','h3','h4','z2','s']
 words['Pb']=['s','z1','W','h2','r']
if seven:
 words={'P0':['h0','h1','W','z1','z0'],'Q1':['W','h2','h3','h4','z2','z1'],'P2':['h4','h5','U','z3','z2'],'Q3':['U','h6','h7','h8','z4','z3'],'P4':['h8','h9','V','z5','z4'],'P5':['V','h10','h11','z6','z5'],'P6':['h11','h12','h0','z0','z6'],'Pc':['r','z1','z2','z3','s'],'Qc':['s','z4','z5','z6','z0','r']}
angles={next(n for n in words if n[0]=='P'):p,next(n for n in words if n[0]=='Q'):q}
s=Solver();s.set(timeout=60000)
s.add(*[And(a>0,a<180) for a in p+q]);s.add(Sum(p)==540,Sum(q)==720)
for name,word in words.items():
 if name in angles:continue
 ref=p if name[0]=='P' else q;n=len(ref)
 a=[Real(name+'_'+str(i)) for i in range(n)];angles[name]=a
 s.add(Or(*[And(*[a[i]==ref[(shift+eps*i)%n] for i in range(n)]) for eps in(1,-1) for shift in range(n)]))
budget={**{'h'+str(i):a for i,a in enumerate([240,90,120,120,270,120,90,120,270,120,90,240,90])},'W':180,'U':180,**{'z'+str(i):360 for i in range(6)}}
if mixed:del budget['W']
if seven:budget.update({'V':180,'z6':360})
if split or outer or seven:budget.update({'r':180,'s':180})
for v,total in budget.items():s.add(Sum([angles[name][i] for name,w in words.items() for i,x in enumerate(w) if x==v])==total)
ans=s.check();out={'status':str(ans),'scope':'Necessary native angle budgets and full dihedral congruence correspondences ONLY','timeout_ms':60000,'boundary_edge_indices':(['native_h2',l] if mixed else [k,l]),'split_center':split,'split_outer1':outer,'mixed_center7':seven}
if ans==sat:
 m=s.model();out['angles']={name:[str(m.eval(a)) for a in aa] for name,aa in angles.items()}
 out['correspondences']={name:[[eps,sh] for eps in (1,-1) for sh in range(len(aa)) if all(m.eval(aa[i]-(p if name[0]=='P' else q)[(sh+eps*i)%len(aa)]).as_fraction()==0 for i in range(len(aa)))] for name,aa in angles.items()}
print(json.dumps(out,indent=2))
