"""All normalized angle assignments for a four-P convex-hexagon seam tree."""
from sage.all import QQ, matrix, vector, Polyhedron
from itertools import product
import json
from pathlib import Path

def row(indices):
 r=[QQ(0)]*5
 for i in indices:r[i%5]+=1
 return r

counts={}; survivors=[]; records=[]
for kT,kR,kB,sT,sR,sB in product(range(5),range(5),range(5),(1,-1),(1,-1),(1,-1)):
 phases=[0,kT,kR,kB]; signs=[1,sT,sR,sB]
 n=lambda f,i:(phases[f]+signs[f]*i)%5
 # CCW faces L=[U,a,C0,C1,b], T=[U,V,c,C2,a],
 # R=[V,d,C3,C4,c], B=[V,U,b,C5,d].
 stars=[[(0,0),(1,0),(3,1)],[(2,0),(1,1),(3,0)],
        [(0,1),(1,4)],[(0,4),(3,2)],[(2,4),(1,2)],[(2,1),(3,4)]]
 rows=[[QQ(1)]*5]+[row([n(f,i) for f,i in star]) for star in stars]
 rhs=[540,360,360,180,180,180,180]
 A=matrix(QQ,rows); b=vector(QQ,rhs)
 aug=A.augment(matrix(QQ,len(rhs),1,list(b)))
 if A.rank()!=aug.rank():status='inconsistent'
 else:
  eqns=[[-y]+list(x)+[0] for x,y in zip(rows,rhs)]
  ieqs=[[0]+row([i])+[-1] for i in range(5)]+[[180]+[-x for x in row([i])]+[-1] for i in range(5)]+[[0]+[0]*5+[1]]
  poly=Polyhedron(eqns=eqns,ieqs=ieqs,base_ring=QQ)
  if poly.is_empty() or max(v[-1] for v in poly.vertices())<=0:status='no_strict_angles'
  else:
   hits=[]
   for i in range(5):
    rr=row([i,i+1]); ar=A.stack(matrix(QQ,[rr])); br=matrix(QQ,len(rhs)+1,1,list(b)+[180])
    if ar.augment(br).rank()==A.rank():hits.append(i)
   if hits:status='adjacent_supplementary'
   else:
    status='survive'; survivors.append(dict(phases=phases,signs=signs,particular=[str(x) for x in A.solve_right(b)],kernel=[[str(x) for x in r] for r in A.right_kernel().basis()]))
 counts[status]=counts.get(status,0)+1
 records.append(dict(phases=phases,signs=signs,status=status))
assert counts=={'survive':22,'inconsistent':668,'adjacent_supplementary':50,'no_strict_angles':260}
print(json.dumps(dict(counts=counts),indent=2))
Path('research/searches/astra-four-pentagon-hexagon-tree-2026-10-20.json').write_text(json.dumps(dict(counts=counts,survivors=survivors,records=records),indent=2)+'\n')
