#!/usr/bin/env python3
from itertools import permutations
import math,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
X=(90,150,90,105,105);Y=(90,105,90,105,150)
words=(X,X,Y,Y)
# Fix one reference orientation per prototype; search all reflection choices
# of the second copy of P and both copies of Q.
Pdir=(0,30,120,195,270);Qdir=(0,75,165,240,270)
base=np.array([[math.cos(math.radians(v)) for v in Pdir]+[0.]*5,
               [math.sin(math.radians(v)) for v in Pdir]+[0.]*5,
               [0.]*5+[math.cos(math.radians(v)) for v in Qdir],
               [0.]*5+[math.sin(math.radians(v)) for v in Qdir]])
start=time.monotonic();attempts=0;flat=0;cache={}; flat_records=[]

def root(p,x):
 while p[x]!=x:
  p[x]=p[p[x]];x=p[x]
 return x

def union(p,x,y):p[root(p,x)]=root(p,y)

for mask in range(8):
 ref=(False,bool(mask&1),bool(mask&2),bool(mask&4))
 fw=[tuple(w[(-j)%5] if r else w[j] for j in range(5)) for w,r in zip(words,ref)]
 native=[[(0 if f<2 else 5)+((-j-1)%5 if ref[f] else j) for j in range(5)] for f in range(4)]
 rn=[];nr=[];nn=[]
 for f in range(4):
  for j in range(5):
   a=fw[f][j]==90;b=fw[f][(j+1)%5]==90
   (rn if a else nr if b else nn).append((f,j))
 assert len(rn)==len(nr)==8 and len(nn)==4
 nnpairs=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
 for nm in nnpairs:
  npairs=[(nn[a],nn[b]) for a,b in nm]
  for perm in permutations(nr):
   attempts+=1
   pairs=list(zip(rn,perm))+npairs
   p=list(range(20))
   for (f,j),(g,k) in pairs:
    union(p,5*f+j,5*g+(k+1)%5)
    union(p,5*f+(j+1)%5,5*g+k)
   cls={}
   for f in range(4):
    for j in range(5):cls.setdefault(root(p,5*f+j),[]).append((f,j))
   if len(cls)!=6 or any(sum(fw[f][j] for f,j in v)!=360 for v in cls.values()):continue
   flat+=1
   sp=list(range(10))
   for (f,j),(g,k) in pairs:union(sp,native[f][j],native[g][k])
   part=tuple(root(sp,j) for j in range(10))
   remap={v:i for i,v in enumerate(sorted(set(part)))}
   part=tuple(remap[v] for v in part)
   flat_records.append({"reflected":ref,"pairs":pairs,"vertex_classes":list(cls.values()),"native_side_partition":part})
   if part in cache:continue
   count=len(set(part))
   mat=np.zeros((4,count))
   for j in range(10):mat[:,part[j]]+=base[:,j]
   A=np.vstack((mat,np.ones(count)))
   b=np.array([0.,0.,0.,0.,1.])
   res=linprog(np.zeros(count),A_eq=A,b_eq=b,bounds=[(1e-6,None)]*count,method='highs')
   cache[part]=res.success
   if res.success:
    data={'reflected':ref,'words':fw,'pairs':pairs,'vertex_classes':list(cls.values()),'native_side_partition':part,'positive_lengths':res.x.tolist(),'attempts':attempts,'flat_models':flat,'partition_count':len(cache),'elapsed':time.monotonic()-start}
    Path('research/certificates/new-angle-three-pentagon-preliminary.json').write_text(json.dumps(data,indent=2))
    print(json.dumps(data));raise SystemExit
 print('mask',mask,'attempts',attempts,'flat',flat,'partitions',len(cache),'elapsed',time.monotonic()-start,flush=True)
print('NO NUMERICAL POSITIVE MODEL',attempts,flat,'raw partition labelings',len(cache))
def canonical_partition(part):
 ids={}
 return tuple(ids.setdefault(v,len(ids)) for v in part)
raw_parts={tuple(m['native_side_partition']) for m in flat_records}
canonical_parts={canonical_partition(part) for part in raw_parts}
Path('research/certificates/new-angle-three-pentagon-mixed-word-angle-models.json').write_text(json.dumps({'attempts':attempts,'flat_models':flat,'models':flat_records,'raw_partition_labelings':len(raw_parts),'distinct_equality_relations':len(canonical_parts),'canonical_equality_relations':[list(x) for x in sorted(canonical_parts)]},indent=2)+'\n')
import sympy as sp
D=(Pdir,Qdir)
parts=sorted({tuple(m['native_side_partition']) for m in flat_records})
exact=[]
for part in parts:
 n=len(set(part)); mat=sp.zeros(4,n)
 for i in range(10):
  f,j=divmod(i,5)
  mat[2*f,part[i]]+=sp.cos(D[f][j]*sp.pi/180)
  mat[2*f+1,part[i]]+=sp.sin(D[f][j]*sp.pi/180)
 ns=mat.nullspace()
 record={'partition':part,'canonical_equality_relation':canonical_partition(part),'matrix':[[str(sp.simplify(mat[i,j])) for j in range(n)] for i in range(4)],'nullspace':[[str(sp.simplify(v[j])) for j in range(n)] for v in ns]}
 print(json.dumps(record))
 exact.append(record)
Path('research/certificates/new-angle-three-pentagon-mixed-word-closure.json').write_text(json.dumps({'partitions':exact,'raw_partition_labelings':len(raw_parts),'distinct_equality_relations':len(canonical_parts)},indent=2)+'\n')
