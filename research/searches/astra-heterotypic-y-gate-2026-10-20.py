"""Exact normalized 3-P Y angle/native-seam preflight, no metric search."""
from sage.all import QQ, matrix, vector, Polyhedron
from itertools import product

def row(indices):
 r=[QQ(0)]*5
 for i in indices:r[i%5]+=1
 return r
def forced(A,b,r,t):
 return matrix(QQ,[list(x)+[y] for x,y in zip(A.rows(),b)]+[list(r)+[t]]).rank()==A.augment(matrix(QQ,5,1,list(b))).rank()
counts={}; survivors=[]
for k1,k2,s1,s2 in product(range(5),range(5),(1,-1),(1,-1)):
 ks=[0,k1,k2];ss=[1,s1,s2]
 rows=[[QQ(1)]*5,row(ks)];rhs=[540,360];lr=[]
 for i in range(3):
  j=(i+1)%3
  rows.append(row([ks[i]-ss[i],ks[j]+ss[j]]));rhs.append(180)
  incoming=(ks[i]-1 if ss[i]==1 else ks[i])%5
  outgoing=(ks[j] if ss[j]==1 else ks[j]-1)%5
  rr=[QQ(0)]*5;rr[incoming]+=1;rr[outgoing]-=1;lr.append(rr)
 A=matrix(QQ,rows);b=vector(QQ,rhs);L=matrix(QQ,lr)
 if A.rank()!=A.augment(matrix(QQ,5,1,list(b))).rank():status='inconsistent'
 else:
  eqns=[[-y]+list(x)+[0] for x,y in zip(rows,rhs)]
  ieqs=[[0]+row([i])+[-1] for i in range(5)]+[[180]+[-x for x in row([i])]+[-1] for i in range(5)]+[[0]+[0]*5+[1]]
  poly=Polyhedron(eqns=eqns,ieqs=ieqs,base_ring=QQ)
  if poly.is_empty() or max(v[-1] for v in poly.vertices())<=0:status='no_strict_angles'
  else:
   hits=[i for i in range(5) if forced(A,b,row([i,i+1]),180)]
   if hits:
    status='adjacent_supplementary'
    print('PERIODIC_OMISSION',ks,ss,'adjacent vertices',hits)
   elif len(set(ks))==1:status='same_center'
   else:status='SURVIVE';survivors.append((ks,ss,A.solve_right(b),list(A.right_kernel().basis()),list(L.rows())))
 counts[status]=counts.get(status,0)+1
 if status=='SURVIVE':print('SURVIVE',survivors[-1])
print('TOTAL',sum(counts.values()),counts)
assert counts=={'same_center':4,'no_strict_angles':78,'adjacent_supplementary':12,'inconsistent':6}
assert not survivors
