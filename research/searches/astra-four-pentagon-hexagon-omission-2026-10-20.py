"""Universal linear omission certificates for the 22 four-P angle survivors."""
from sage.all import QQ,matrix,vector
import json,runpy
from pathlib import Path
RAO=runpy.run_path('research/searches/convex-substitution-shapes.py')['RAO']
data=json.loads(Path('research/searches/astra-four-pentagon-hexagon-tree-2026-10-20.json').read_text())
def row(ids):
 r=[QQ(0)]*5
 for i in ids:r[i]+=1
 return vector(QQ,r)
def implied(A,b,r,t):
 ar=A.stack(matrix(QQ,[r]));return ar.rank()==ar.augment(matrix(QQ,len(b)+1,1,list(b)+[t])).rank()==A.rank()
out=[]
for record in data['survivors']:
 phases=record['phases']; signs=record['signs']
 n=lambda f,i:(phases[f]+signs[f]*i)%5
 side=lambda f,i:(phases[f]+i if signs[f]==1 else phases[f]-i-1)%5
 stars=[[(0,0),(1,0),(3,1)],[(2,0),(1,1),(3,0)],[(0,1),(1,4)],[(0,4),(3,2)],[(2,4),(1,2)],[(2,1),(3,4)]]
 A=matrix(QQ,[[1]*5]+[row([n(f,i) for f,i in st]) for st in stars]); b=vector(QQ,[540,360,360,180,180,180,180])
 seams=[((0,0),(1,4)),((0,4),(3,1)),((2,4),(1,1)),((2,0),(3,4)),((1,0),(3,0))]
 L=matrix(QQ,[row([side(*u)])-row([side(*v)]) for u,v in seams]);z=vector(QQ,[0]*5)
 phits=[]
 for typ,(aeqs,leqs) in RAO.items():
  for s in (1,-1):
   for k in range(5):
    an=[(k+s*i)%5 for i in range(5)];ln=[(k+i if s==1 else k-i-1)%5 for i in range(5)]
    def rr(coef,inds):
     v=vector(QQ,[0]*5)
     for c,i in zip(coef,inds):v[i]+=c
     return v
    if all(implied(A,b,rr(r,an),36*t) for r,t in aeqs) and all(implied(L,z,rr(r,ln),0) for r in leqs):phits.append([typ,s,k])
 ha=[row([n(f,i)]) for f,i in [(0,2),(0,3),(3,3),(2,2),(2,3),(1,3)]]
 hl=[row([side(0,2)]),row([side(0,3),side(3,2)]),row([side(3,3),side(2,1)]),row([side(2,2)]),row([side(2,3),side(1,2)]),row([side(1,3),side(0,1)])]
 hhits=[]
 for s in (1,-1):
  for k in range(6):
   an=[ha[(k+s*i)%6] for i in range(6)];ln=[hl[(k+i if s==1 else k-i-1)%6] for i in range(6)]
   if implied(A,b,an[1]+an[2]+an[3],360) and implied(L,z,ln[0]-ln[3],0):hhits.append(['type1',s,k])
 out.append(dict(phases=phases,signs=signs,P_omission=phits,H_type1=hhits,length_kernel=[[str(x) for x in r] for r in L.right_kernel().basis()]))
assert len(out)==22 and all(any(h[0] in (2,4) for h in r['P_omission']) for r in out)
print('PASS: all 22 strict nonsupplementary templates force a Type 2 or Type 4 periodic P omission')
Path('research/searches/astra-four-pentagon-hexagon-omission-2026-10-20.json').write_text(json.dumps(out,indent=2)+'\n')
