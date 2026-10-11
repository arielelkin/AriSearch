"""Independent raw geometry audit. No author module imports or witness formulas."""
from sage.all import QuadraticField,vector,matrix
from itertools import product
K=QuadraticField(3,'w'); w=K.gen(); r=K(4)/5;t=K(6)/5
V=lambda x,y:vector(K,[x,y])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):
 return sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2 if len(poly)>=3 else K(0)
def ccw(poly):return poly if area(poly)>0 else list(reversed(poly))
def clip(a,b):
 out=ccw(a)
 for i in range(len(b)):
  edge0=b[i];edge=b[(i+1)%len(b)]-edge0;prev=out[-1] if out else None;new=[]
  if prev is None:break
  prevside=cross(edge,prev-edge0)
  for cur in out:
   curside=cross(edge,cur-edge0)
   if (prevside<0 and curside>=0) or (prevside>=0 and curside<0):
    new.append(prev+(cur-prev)*(prevside/(prevside-curside)))
   if curside>=0:new.append(cur)
   prev,prevside=cur,curside
  out=new
 return out

def raw(z):
 d=(w*z-1)/2;c=(3*w-z)/2
 quarter=[V(0,0),V(d,0),V(d+1,w),V(d+K(1)/2,3*w/2),V(0,c)]
 faces=[ccw([V(s*x,s2*y) for x,y in quarter]) for s,s2 in product((-1,1),repeat=2)]
 boundary=[V(d,0),V(d+1,w),V(d+K(1)/2,3*w/2),V(0,c),
  V(-d-K(1)/2,3*w/2),V(-d-1,w),V(-d,0),V(-d-1,-w),
  V(-d-K(1)/2,-3*w/2),V(0,-c),V(d+K(1)/2,-3*w/2),V(d+1,-w)]
 assert area(boundary)>0
 assert len({tuple(v) for v in boundary})==12
 for f in faces:
  assert all(cross(f[(i+1)%5]-f[i],f[j]-f[i])>0 for i in range(5) for j in range(5) if j not in [i,(i+1)%5])
 return faces,boundary
host,_=raw(r);dr=(w*r-1)/2;notch=V(dr,0)
rays=[V(K(1)/2,-w/2),V(K(1)/2,w/2)]
assert rays[0].dot_product(rays[1])==-K(1)/2
count=0;areas=[]
for z in (r,t):
 faces,boundary=raw(z);dz=(w*z-1)/2;H=dr+dz+1
 actual={}
 for i in [1,5,7,11]:
  E=boundary[i];arms=[boundary[(i-1)%12]-E,boundary[(i+1)%12]-E]
  lengths=[a.dot_product(a) for a in arms];assert sorted(lengths)==[1,4]
  for assignment in [(0,1),(1,0)]:
   target=[rays[assignment[j]]*(1 if lengths[j]==1 else 2) for j in range(2)]
   orig=matrix(K,[[arms[0][0],arms[1][0]],[arms[0][1],arms[1][1]]])
   dest=matrix(K,[[target[0][0],target[1][0]],[target[0][1],target[1][1]]])
   O=dest*orig.inverse();assert O.transpose()*O==matrix.identity(K,2)
   center=notch-O*E
   transformed=[[center+O*x for x in f] for f in faces]
   key=tuple(sorted(tuple(center+O*x) for x in boundary))
   actual[key]=(center,transformed)
 assert len(actual)==2
 assert {tuple(c) for c,fs in actual.values()}=={(H,w),(H,-w)}
 for center,B in actual.values():
  assert all(area(clip(a,ccw(b)))==0 for a in host for b in B)
  sign=1 if center[1]>0 else -1
  X=notch+V(K(1)/2,-sign*w/2)
  assert X==V(w*r/2,-sign*w/2)
  # Verify host native edge T and actual filler bank from raw boundary.
  host_e_end=notch+V(1,-sign*w)
  assert X==(notch+host_e_end)/2
  lower_notch=center+V(0,-sign*(3*w-z)/2)
  bank=lower_notch-X
  assert bank==V(w*z/2,sign*z/2)
  assert bank.dot_product(bank)==z*z
  assert bank.dot_product(host_e_end-notch)==0
  bankcol=matrix(K,[[bank[0]],[bank[1]]])
  F=2*bankcol*bankcol.transpose()/(z*z)-matrix.identity(K,2)
  assert F==matrix(K,[[K(1)/2,sign*w/2],[sign*w/2,-K(1)/2]])
  Ccenter=X+F*(center-X);assert Ccenter!=center
  C=[[X+F*(x-X) for x in f] for f in B]
  positive=[area(clip(ccw(b),ccw(c))) for b in B for c in C]
  assert max(positive)>0
  areas.append((str(z),sign,str(max(positive))))
  count+=1
print('PASS:16 raw E/ray placements reduce to4 physical fillers;64 exact initial intersection areas zero;4 forced reflected clusters distinct;4 strict positive-area actual pentagon intersections.')
print('Maximum intersection areas:',areas)
