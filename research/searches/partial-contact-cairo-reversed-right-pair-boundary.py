"""Exact symbolic boundary cancellation for a proposed reversed-right-pair Cairo motif."""
from sage.all import QuadraticField,PolynomialRing,vector,matrix,ceil,floor,AA
from itertools import product
import json,argparse
K=QuadraticField(3,"w");w=K.gen();R=PolynomialRing(K,"u");u=R.gen();V=lambda x,y:vector(R,(x,y))
P=(R(1),u,(3*w-u)/2,(w*u-1)/2,R(2));Q=(u,R(1),(3*w*u-1)/2,(w-u)/2,2*u)
R120=matrix(R,[[-R(1)/2,-w/2],[w/2,-R(1)/2]])
def native(L):
 a,b,c,d,e=L
 assert b-c==w*(d-a) and e==w*c+d-2*a
 return [V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
def quad(L):
 a,b,c,d,e=L
 return [V(0,0),V(d,0),V(d+e/2,w*e/2),V(d+(e-a)/2,w*(e+a)/2),V(0,c)]
faces=[];atoms=[]
for H,L in enumerate((P,Q)):
 for sx,sy in product((-1,1),repeat=2):
  transform=lambda z:V(sx*z[0],sy*z[1]) if H==0 else V(sy*z[1],3*w-sx*z[0])
  raw=quad(L);N=native(L)
  assert raw==[R120*(N[i]-N[3]) for i in (3,4,0,1,2)]
  assert all((N[(i+1)%5]-N[i]).dot_product(N[(i+1)%5]-N[i])==L[i]**2 for i in range(5))
  poly=[transform(z) for z in raw]
  if sx*sy<0:poly.reverse()
  faces.append(poly)
  # All native boundaries: split e at its midpoint; retain the two internal-axis edges.
  segments=[(raw[0],raw[1]),(raw[1],(raw[1]+raw[2])/2),((raw[1]+raw[2])/2,raw[2]),(raw[2],raw[3]),(raw[3],raw[4]),(raw[4],raw[0])]
  for A,B in segments:
   A,B=transform(A),transform(B)
   if sx*sy<0:A,B=B,A
   atoms.append((A,B))
periods=[V(w*u,-w),V(3*w*u,3*w)]
sample=K(4)/5;ev=lambda z:vector(K,[x(sample) for x in z])
U=matrix(K,[[ev(t)[i] for t in periods] for i in range(2)]);Ui=U.inverse();bounds=[]
for A,B in atoms:
 vals=[Ui*ev(A),Ui*ev(B)]
 bounds.append([(min(v[k] for v in vals),max(v[k] for v in vals)) for k in range(2)])
pairs=[];unpaired=set(range(len(atoms)))
while unpaired:
 i=min(unpaired);A,B=atoms[i];found=[]
 for j in sorted(unpaired-{i}):
  C,D=atoms[j]
  ranges=[range(int(ceil(bounds[i][k][0]-bounds[j][k][1])),int(floor(bounds[i][k][1]-bounds[j][k][0]))+1) for k in range(2)]
  for m,n in product(*ranges):
   shift=m*periods[0]+n*periods[1]
   if A==D+shift and B==C+shift:found.append((j,m,n))
 if not found:
  print("UNMATCHED",i,[[str(x) for x in z] for z in (A,B)],flush=True);unpaired.remove(i);continue
 assert len(found)==1,(i,found)
 j,m,n=found[0];pairs.append((i,j,m,n));unpaired.remove(i);unpaired.remove(j)
assert len(pairs)==len(atoms)//2==24
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
areas=[sum(cross(poly[i],poly[(i+1)%5]) for i in range(5))/2 for poly in faces]
covol=cross(*periods)
assert sum(areas)==covol==18*u
assert areas[:4]==[9*u/4+w*(1-u*u)/8]*4
assert areas[4:]==[9*u/4-w*(1-u*u)/8]*4
supports=[];AR=PolynomialRing(AA,"z");assert AA(w)>0
for L in(P,Q):
 N=native(L)
 for i in range(5):
  edge=N[(i+1)%5]-N[i]
  for j in range(5):
   if j in(i,(i+1)%5):continue
   determinant=cross(edge,N[j]-N[i])
   assert determinant(sample)>0
   roots=AR([AA(t) for t in determinant.list()]).roots(AA)
   assert all(not AA(1/w)<root<AA(w) for root,multiplicity in roots)
   supports.append(str(determinant))
result={"strict_support_polynomials":supports,"parameter_interval":[str(1/w),str(w)],"symbolic_pair_count":len(pairs),"atomic_edge_count":len(atoms),"pairs":pairs,"atoms":[[[str(x) for x in z] for z in atom] for atom in atoms],"faces":[[[str(x) for x in z] for z in p] for p in faces],"periods":[[str(x) for x in t] for t in periods],"area":str(covol)}
ap=argparse.ArgumentParser();ap.add_argument("--output");args=ap.parse_args()
if args.output:
 with open(args.output,"w") as f:json.dump(result,f,indent=2);f.write("\n")
print("SYMBOLIC",len(pairs),"of",len(atoms)//2,"reverseboundarypairs;area",covol)
