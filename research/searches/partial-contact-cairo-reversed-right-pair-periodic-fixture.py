"""Exact finite fixture for reversed shared right-pair Cairo periodic candidate."""
import argparse,json
from pathlib import Path
from itertools import product
from sage.all import QuadraticField,vector,matrix,ceil,floor
K=QuadraticField(3,"w");w=K.gen();V=lambda x,y:vector(K,(x,y))
z=K(4)/5;d=(w*z-1)/2;c=(3*w-z)/2;dQ=(w-z)/2;cQ=(3*w*z-1)/2
native=[V(0,0),V(1,0),V(1,z),V(1-w*c/2,z+c/2),V(-1,w)]
L=(K(1),z,c,d,K(2))
assert L[1]-L[2]==w*(L[3]-L[0]) and L[4]==w*L[2]+L[3]-2*L[0]
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
for i in range(5):
 E=native[(i+1)%5]-native[i]
 assert E.dot_product(E)==L[i]**2
 for j in range(5):
  if j not in(i,(i+1)%5):assert cross(E,native[j]-native[i])>0
quad=[V(0,0),V(d,0),V(d+1,w),V(d+K(1)/2,3*w/2),V(0,c)]
quadQ=[V(0,0),V(dQ,0),V(dQ+z,w*z),V(dQ+z/2,3*w*z/2),V(0,cQ)]
LQ=(z,K(1),cQ,dQ,2*z)
nativeQ=[V(0,0),V(z,0),V(z,1),V(z-w*cQ/2,1+cQ/2),V(-z,w*z)]
R120=matrix(K,[[-K(1)/2,-w/2],[w/2,-K(1)/2]])
assert quad==[R120*(native[i]-native[3]) for i in (3,4,0,1,2)]
assert quadQ==[R120*(nativeQ[i]-nativeQ[3]) for i in (3,4,0,1,2)]
for L0,N in((L,native),(LQ,nativeQ)):
 for i in range(5):
  E=N[(i+1)%5]-N[i];assert E.dot_product(E)==L0[i]**2
  assert all(cross(E,N[j]-N[i])>0 for j in range(5) if j not in(i,(i+1)%5))
S=[[V(s*x,t*y) for x,y in quad] for s,t in product((-1,1),repeat=2)]
R90=matrix(K,[[0,1],[-1,0]])
SQ=[[V(s*x,t*y) for x,y in quadQ] for s,t in product((-1,1),repeat=2)]
faces=S+[[R90*x+V(0,3*w) for x in p] for p in SQ]
u=V(w*z,-w);v=V(3*w*z,3*w);U=matrix(K,[[u[0],v[0]],[u[1],v[1]]]);Ui=U.inverse()
area=lambda P:abs(sum(cross(P[i],P[(i+1)%5]) for i in range(5)))/2
print("AREAS",[str(area(P)) for P in faces],flush=True)
assert U.det()==sum(area(P) for P in faces)
print("COVOLUME",U.det(),flush=True)
def separated(A,B):
 for C in (A,B):
  for i in range(5):
   E=C[(i+1)%5]-C[i];n=V(-E[1],E[0]);pa=[n.dot_product(x) for x in A];pb=[n.dot_product(x) for x in B]
   if max(pa)<=min(pb) or max(pb)<=min(pa):return True
 return False
bounds=[]
for P in faces:
 T=[Ui*x for x in P]
 bounds.append([(min(x[j] for x in T),max(x[j] for x in T)) for j in range(2)])
comparisons=0;max_abs_index=0
for i,A in enumerate(faces):
 for j,B in enumerate(faces):
  ranges=[range(int(ceil(bounds[i][k][0]-bounds[j][k][1])),int(floor(bounds[i][k][1]-bounds[j][k][0]))+1) for k in range(2)]
  for m,n in product(*ranges):
   if i==j and m==n==0:continue
   shift=m*u+n*v
   assert separated(A,[x+shift for x in B]),(i,j,m,n)
   comparisons+=1;max_abs_index=max(max_abs_index,abs(m),abs(n))
result={'field':'Q(w),w^2=3,1<w<2','native_sides':[str(x) for x in L], 'second_native_sides':[str(x) for x in LQ], 'ratio':str(z), 'periods':[[str(x) for x in u],[str(x) for x in v]], 'face_vertices':[[[str(x) for x in z] for z in P] for P in faces], 'cell_area':str(U.det()),'tile_areas':[str(area(f)) for f in faces],'face_count':8,'complete_lattice_comparisons':comparisons,'maximum_absolute_lattice_index':max_abs_index,'method':'exact inverse-lattice bounding boxes then convex separating axes; area/covolume1 gives coverage'}
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact reversed-right-pair 4/5 fixture:',comparisons,'complete comparisons')
