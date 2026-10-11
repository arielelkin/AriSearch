"""Changed4sharedarm Cairo candidate: exact4face periodic fixture checker.
Full cone proof in linked lemma; independent audit pending.
"""
from sage.all import QuadraticField,PolynomialRing,vector,matrix,ceil,floor
from itertools import product
K=QuadraticField(3,'w');w=K.gen();a,c,d,D=map(K,(1,2,3,4));b=c+w*(d-a);B=a+w*(D-c);e=w*c+d-2*a;f=w*a+D-2*c
vv=lambda x,y:vector(K,(x,y))
def poly(z):
 a,b,c,d,e=z
 return[vv(0,0),vv(a,0),vv(a,b),vv(a-w*c/2,b+c/2),vv(-e/2,w*e/2)]
P=poly((a,b,c,d,e));Q=poly((c,B,a,D,f));S=matrix(K,[[-w/2,K(1)/2],[K(1)/2,w/2]])
Q0=[S*(x-Q[2]) for x in Q];P1=[P[4]-x for x in P];Q1=[Q0[4]+Q0[0]-x for x in Q0]
u=P1[0]-Q1[2];v=P[2]-Q0[0];motif=[P,P1,Q0,Q1]
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
area=lambda p:sum(cross(p[i],p[(i+1)%5]) for i in range(5))/2
assert all(x>0 for x in(a,b,c,d,e,c,B,a,D,f))
assert len(set((a,b,c,d,e)))==5 and len(set((c,B,a,D,f)))==5
for p in(P,Q):
 for i in range(5):
  for j in range(5):
   if j not in(i,(i+1)%5):assert cross(p[(i+1)%5]-p[i],p[j]-p[i])>0
assert -cross(u,v)==2*area(P)+2*area(Q)
lattice=matrix(K,[u,v]).transpose();iv=lattice.inverse();coords=[[iv*z for z in p] for p in motif]
def disjoint(p,q):
 for t in(p,q):
  for i in range(5):
   edge=t[(i+1)%5]-t[i];pvs=[cross(edge,x) for x in p];qvs=[cross(edge,x) for x in q]
   if max(pvs)<=min(qvs) or max(qvs)<=min(pvs):return True
 return False
checks=[]
for i,j in product(range(4),repeat=2):
 bounds=[(ceil(min(x[k] for x in coords[i])-max(x[k] for x in coords[j])),floor(max(x[k] for x in coords[i])-min(x[k] for x in coords[j]))) for k in(0,1)]
 for n,m in product(range(bounds[0][0],bounds[0][1]+1),range(bounds[1][0],bounds[1][1]+1)):
  if i==j and n==m==0:continue
  assert disjoint(motif[i],[z+n*u+m*v for z in motif[j]]),(i,j,n,m)
  checks.append((i,j,n,m))
print('PASS: changed Cairo4face exact periodic fixture;',len(checks),'complete lattice comparisons')
# Full-cone symbolic equations are checked independently of the fixture.
R=PolynomialRing(K,names=("a","c","d","D"));aa,cc,dd,DD=R.gens()
bb=cc+w*(dd-aa);BB=aa+w*(DD-cc);ee=w*cc+dd-2*aa;ff=w*aa+DD-2*cc
sv=lambda x,y:vector(R,(x,y))
def sympoly(L):
 A,B,C,D,E=L
 return[sv(0,0),sv(A,0),sv(A,B),sv(A-w*C/2,B+C/2),sv(-E/2,w*E/2)]
p0=sympoly((aa,bb,cc,dd,ee));qs=sympoly((cc,BB,aa,DD,ff));SR=matrix(R,S)
q0=[SR*(x-qs[2]) for x in qs];p1=[p0[4]-x for x in p0];q1=[q0[4]+q0[0]-x for x in q0]
uu=p1[0]-q1[2];vvv=p0[2]-q0[0]
assert -cross(uu,vvv)==2*area(p0)+2*area(qs)
assert p0[4]==p1[0] and p0[0]==p1[4]
assert q0[4]==q1[0] and q0[0]==q1[4]
for x,i,y,j,t in((p0,0,q0,2,sv(0,0)),(p1,0,q1,2,uu),(p0,2,q0,0,vvv),(p1,2,q1,0,uu-vvv)):
 assert x[i]==y[j]+t and x[i+1]==y[j+1]+t
# Both bank chains have identical outer endpoints and collinear internal breaks.
assert p0[1]==q0[3]
assert q1[4]+vvv==p0[2] and p1[2]+vvv-uu==q0[4]
assert q1[3]+vvv==p1[1]+vvv-uu
assert q0[2]+vvv==vvv and q0[1]+vvv==p0[3]
assert q1[2]+uu==p0[4] and p1[4]+vvv==vvv
assert q1[1]+uu==p1[3]+vvv
# All bank vectors have exactly the common fixed unit direction, with positive
# coefficients bb, DD, dd, BB throughout the domain.
assert p0[2]-p0[1]==sv(0,bb)
assert q0[4]-q0[3]==sv(0,-DD)
assert q1[4]-q1[3]==sv(0,DD)
assert p1[2]-p1[1]==sv(0,-bb)
assert p0[4]-p0[3]==sv(-dd/2,-w*dd/2)
assert q0[1]-q0[2]==sv(-BB/2,-w*BB/2)
assert p1[4]-p1[3]==sv(dd/2,w*dd/2)
assert q1[1]-q1[2]==sv(BB/2,w*BB/2)
import argparse,json,platform
encode=lambda z:[str(t) for t in z]
cert={"scope":"full4D positive partial-contact Cairo sufficient periodic cone",
      "parameters":["a","c","d","D"],"positive_forms":[str(z) for z in(aa,cc,dd,DD,bb,BB,ee,ff)],
      "P":[encode(z) for z in p0],"Q":[encode(z) for z in qs],
      "motifs":[[encode(z) for z in x] for x in(p0,p1,q0,q1)],
      "u":encode(uu),"v":encode(vvv),"area_P":str(area(p0)),"area_Q":str(area(qs)),
      "fixture_P":[encode(z) for z in P],"fixture_Q":[encode(z) for z in Q],
      "fixture_u":encode(u),"fixture_v":encode(v),"complete_lattice_comparisons":[list(x) for x in checks],
      "software":{"python":platform.python_version(),"sage":__import__("sage.env",fromlist=["SAGE_VERSION"]).SAGE_VERSION}}
ap=argparse.ArgumentParser();ap.add_argument("--output");args=ap.parse_args()
if args.output:
 with open(args.output,"w") as out:json.dump(cert,out,indent=2,sort_keys=True);out.write("\n")
print("PASS: full4D polynomial seams, bank chains, covolume and44 complete exact fixture separations")
