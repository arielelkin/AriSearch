"""Exact bounded oriented combinatorial torus search; see accompanying JSON."""
import itertools,json,time
from pathlib import Path
import z3
P=[115,115,100,110,100];Q=[130,130,130,125,125,125,135]
PL=['L','1','1','1','1'];QL=['1','a','1','b','1','1','1']
records=[]
for flips in itertools.product([0,1],repeat=3):
 angles=[];labels=[];rho=[];faces=[]
 for f,(A,L,flip) in enumerate(zip([P,P,Q,Q],[PL,PL,QL,QL],[0,*flips])):
  n=len(A);off=len(angles)
  inds=list(range(n)) if not flip else [(-i)%n for i in range(n)]
  angles += [A[i] for i in inds]
  labels += [L[i] if not flip else L[(i-1)%n] for i in inds]
  rho += [off+(i+1)%n for i in range(n)]
  faces += [f]*n
 n=len(angles);s=z3.Solver();s.set(timeout=6000,random_seed=0)
 alpha=[z3.Int('a%d'%i) for i in range(n)]
 def elem(xs,k):
  ar=z3.K(z3.IntSort(),0)
  for j,val in enumerate(xs):ar=z3.Store(ar,j,val)
  return z3.Select(ar,k)
 for i in range(n):
  s.add(z3.Or([alpha[i]==j for j in range(n) if j!=i and labels[i]==labels[j]]))
  s.add(elem(alpha,alpha[i])==i)
 v=[elem(rho,alpha[i]) for i in range(n)]
 for i in range(n):
  v2=elem(v,v[i]);v3=elem(v,v2)
  s.add(v3==i,v[i]!=i,v2!=i,angles[i]+elem(angles,v[i])+elem(angles,v2)==360)
 t=time.monotonic();status=s.check();r={'reflections':[0,*flips],'status':str(status),'seconds':time.monotonic()-t}
 if status==z3.sat:
  m=s.model();aa=[m.eval(x).as_long() for x in alpha]
  vv=[rho[aa[i]] for i in range(n)]
  assert all(aa[aa[i]]==i and aa[i]!=i and labels[i]==labels[aa[i]] for i in range(n))
  assert all(vv[vv[vv[i]]]==i and len({i,vv[i],vv[vv[i]]})==3 and angles[i]+angles[vv[i]]+angles[vv[vv[i]]]==360 for i in range(n))
  seen={0}
  while True:
   new=seen|{rho[i] for i in seen}|{aa[i] for i in seen}
   if new==seen:break
   seen=new
  r.update(alpha=aa,rho=rho,angles=angles,labels=labels,connected=len(seen)==n)
 elif status==z3.unknown:r['reason']=s.reason_unknown()
 records.append(r)
 print(r,flush=True)
out={'question':'Oriented cellular trivalent quotient with exactly 2 P and 2 Q, allowing reflections; edge lengths treated as four distinct labels. No metric or embedded realization certified.','z3_version':z3.get_version_string(),'records':records}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
