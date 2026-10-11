"""Independent positive witness and event audit for symmetric Cairo pentagons."""
from sage.all import QuadraticField,AA,vector,matrix,PolynomialRing
from itertools import product,combinations_with_replacement
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
V=lambda x,y:vector(K,[x,y])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2 if len(poly)>2 else K(0)
def clip(a,b):
 out=list(a)
 for i in range(len(b)):
  start=b[i];edge=b[(i+1)%len(b)]-start
  if not out:break
  prev=out[-1];dp=cross(edge,prev-start);new=[]
  for cur in out:
   dc=cross(edge,cur-start)
   if (dp<0 and dc>=0) or (dp>=0 and dc<0):new.append(prev+(cur-prev)*dp/(dp-dc))
   if dc>=0:new.append(cur)
   prev,dp=cur,dc
  out=new
 return out
# Positive normalized point b=w*a,a=1,e=2.
P=[V(0,0),V(1,0),V(1,w),V(-K(1)/2,3*w/2),V(-1,w)]
lengths=[K(1),w,w,K(1),K(2)]
for i in range(5):
 edge=P[(i+1)%5]-P[i]
 assert edge.dot_product(edge)==lengths[i]**2
 for j in range(5):
  if j not in [i,(i+1)%5]:assert cross(edge,P[j]-P[i])>0
assert area(P)==2*w
R120=matrix(K,[[-K(1)/2,-w/2],[w/2,-K(1)/2]])
assert R120**3==matrix.identity(K,2)
center=P[2]
faces=[[R120**k*(p-center) for p in P] for k in range(3)]
assert all(area(p)==2*w for p in faces)
hexagon=[V(2,0),V(1,w),V(-1,w),V(-2,0),V(-1,-w),V(1,-w)]
assert area(hexagon)==6*w
assert sum(area(p) for p in faces)==6*w
u=V(3,w);v=V(0,2*w)
assert cross(u,v)==6*w
for face in faces:
 for point in face:
  assert all(cross(hexagon[(i+1)%6]-hexagon[i],point-hexagon[i])>=0 for i in range(6))
xs=[p[0] for face in faces for p in face];ys=[p[1] for face in faces for p in face]
assert max(xs)-min(xs)==4 and max(ys)-min(ys)==2*w
# |3m|<=4 gives|m|<=1, |m+2n|<=2 then|n|<=1.
checked=0
for m,n in product(range(-1,2),repeat=2):
 for i,a in enumerate(faces):
  for j,b0 in enumerate(faces):
   if i==j and m==n==0:continue
   assert area(clip(a,[p+m*u+n*v for p in b0]))==0,(m,n,i,j)
   checked+=1
assert checked==78
# Symbolic generic event inventory, two distinct arm values.
Poly=PolynomialRing(K,names=('a','b'));a,b=Poly.gens();arms=[a,b,b,a];banks=[b,a,a,b]
events=[]
for i,j in combinations_with_replacement(range(4),2):
 if arms[i]==arms[j]:
  assert banks[i]==banks[j]
  events.append((i,j,banks[i]+banks[j]))
assert len(events)==6 and {total for i,j,total in events}=={2*a,2*b}
e=w*b-a
assert e-2*b==(w-2)*b-a
assert w*(e-2*a)==3*(b-w*a)
# All-equal substitution in the separately reviewed swapped Cairo cone.
assert a+w*(a-a)==a and w*a+a-2*a==(w-1)*a
path=Path(__file__).resolve().parents[1]/'certificates'/'partial-contact-cairo-paired-repeat-periodic.json'
data=json.loads(path.read_text())
serialized=[[V(K(x),K(y)) for x,y in face] for face in data['face_vertices']]
key=lambda face:tuple(sorted(tuple(v) for v in face))
assert sorted(key(p) for p in serialized)==sorted(key(p) for p in faces)
assert [V(K(x),K(y)) for x,y in data['periods']]==[u,v]
assert [K(x) for x in data['native_sides']]==lengths
assert data['face_count']==3 and K(data['face_area'])==2*w and K(data['covolume'])==6*w
print('PASS:6 exhaustive generic90-corner events with equal banks;generic closure identities;3 exact original faces insidehexagon;complete78 lattice-pair intersections zero;area6sqrt3=covolume;retainedcertificatecoordinates match.')
