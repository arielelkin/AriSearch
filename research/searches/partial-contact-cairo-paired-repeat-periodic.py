"""Exact paired-repeat obstruction algebra and three-P periodic witness."""
import argparse,json
from pathlib import Path
from itertools import product
from sage.all import QuadraticField,PolynomialRing,vector,matrix,ceil,floor
K=QuadraticField(3,"w");w=K.gen();A=PolynomialRing(K,names=("a","b"));a,b=A.gens();e=w*b-a
assert e-2*b==(w-2)*b-a
assert w*(e-2*a)==3*(b-w*a)
V=lambda x,y:vector(K,(x,y));cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
L=(K(1),w,w,K(1),K(2));native=[V(0,0),V(1,0),V(1,w),V(-K(1)/2,3*w/2),V(-1,w)]
for i in range(5):
 E=native[(i+1)%5]-native[i]
 assert E.dot_product(E)==L[i]**2
 for j in range(5):
  if j not in(i,(i+1)%5):assert cross(E,native[j]-native[i])>0
R=matrix(K,[[-K(1)/2,-w/2],[w/2,-K(1)/2]])
assert R**3==matrix.identity(K,2)
faces=[[(R**k)*(x-native[2]) for x in native] for k in range(3)]
hexagon=[V(2,0),V(1,w),V(-1,w),V(-2,0),V(-1,-w),V(1,-w)]
for P in faces:
 for x in P:
  assert all(cross(hexagon[(i+1)%6]-hexagon[i],x-hexagon[i])>=0 for i in range(6))
area=lambda P:abs(sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P))))/2
assert all(area(P)==2*w for P in faces)
assert area(hexagon)==6*w==sum(area(P) for P in faces)
u=V(3,w);v=V(0,2*w);U=matrix(K,[[u[0],v[0]],[u[1],v[1]]]);Ui=U.inverse()
assert U.det()==6*w
def separated(P,Q):
 for C in (P,Q):
  for i in range(5):
   E=C[(i+1)%5]-C[i];n=V(-E[1],E[0]);p=[n.dot_product(x) for x in P];q=[n.dot_product(x) for x in Q]
   if max(p)<=min(q) or max(q)<=min(p):return True
 return False
bounds=[]
for P in faces:
 T=[Ui*x for x in P];bounds.append([(min(x[i] for x in T),max(x[i] for x in T)) for i in range(2)])
comparisons=0;max_index=0
for i,P in enumerate(faces):
 for j,Q in enumerate(faces):
  ranges=[range(int(ceil(bounds[i][k][0]-bounds[j][k][1])),int(floor(bounds[i][k][1]-bounds[j][k][0]))+1) for k in range(2)]
  for m,n in product(*ranges):
   if i==j and m==n==0:continue
   assert separated(P,[x+m*u+n*v for x in Q]),(i,j,m,n)
   comparisons+=1;max_index=max(max_index,abs(m),abs(n))
result={'field':'Q(w),w^2=3,1<w<2','native_sides':[str(x) for x in L], 'face_vertices':[[[str(x) for x in y] for y in P] for P in faces], 'periods':[[str(x) for x in u],[str(x) for x in v]], 'face_count':3,'face_area':'2*w','covolume':'6*w','complete_lattice_comparisons':comparisons,'maximum_absolute_lattice_index':max_index}
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS:paired-repeat algebra;3 exact Cairo faces form regularhexagon;area6w;{comparisons} complete lattice comparisons;max index{max_index}')
