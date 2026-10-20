"""Predeclared domain: every triangular face-lattice HNF quotient of index 1..6.
24 raw geometric states per cell. Shared total solver budget: 60 seconds.
"""
import json,time
from pathlib import Path
import z3
U=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
W=((5,3,3,4,4,2),(1,3,3,2,2,4))
assert all(min(w)>0 and w[0]-w[3]==w[2]-w[5]==w[4]-w[1]!=0 for w in W)
S=[dict(tile=t,r=r,eps=e,lengths=[W[t][(r+e*k)%6] for k in range(6)]) for t in range(2) for r in range(6) for e in (-1,1)]
started=time.monotonic(); records=[]; witness=None
for n in range(1,7):
 for a in range(1,n+1):
  if n%a:continue
  c=n//a
  for b in range(a):
   left=60-(time.monotonic()-started)
   if left<=0:break
   def reduce(x,y):
    q,y=divmod(y,c)
    return ((x-b*q)%a,y)
   cells=[(x,y) for y in range(c) for x in range(a)]; indices={p:i for i,p in enumerate(cells)}
   vs=[z3.Int('s%d'%i) for i in range(n)]; sol=z3.Solver(); sol.set(timeout=max(1,int(left*1000)))
   for v in vs:sol.add(v>=0,v<24)
   def length(v,k):return z3.Sum([z3.If(v==i,s['lengths'][k],0) for i,s in enumerate(S)])
   for i,(x,y) in enumerate(cells):
    for k,(dx,dy) in enumerate(U[:3]):
     j=indices[reduce(x+dx,y+dy)]
     sol.add(length(vs[i],k)==length(vs[j],k+3))
   answer=sol.check(); records.append(dict(a=a,b=b,c=c,n=n,result=str(answer)))
   if answer==z3.sat:
    m=sol.model(); witness=dict(a=a,b=b,c=c,cells=cells,states=[S[m.eval(v).as_long()] for v in vs]);break
  if witness or time.monotonic()-started>=60:break
 if witness or time.monotonic()-started>=60:break
result=dict(domain='all HNF <(a,0),(b,c)> with ac<=6, 0<=b<a; all 24 states; monohedral permitted',budget_seconds=60,elapsed_seconds=time.monotonic()-started,z3_version=z3.get_version_string(),records=records,witness=witness)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
