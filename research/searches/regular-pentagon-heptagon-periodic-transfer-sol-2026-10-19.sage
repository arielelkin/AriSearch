from sage.all import *
from sage.version import version as sage_version
import json
# Two FIXED maps only. No pairing enumeration and no parameter samples.
K=CyclotomicField(20); w=K.gen()
R=PolynomialRing(K,"h"); h=R.gen()
t=w+w**(-1); k=-(w**3+w**15)/w**9
assert AA(t)>0 and 0<AA(k)<1
P=[R(sum((w**(4*j) for j in range(i)),K(0))) for i in range(5)]
lengths=[R(1),t+h,R(1),t+k*h,R(1),t+h,R(1)]
Q=[sum((lengths[j]*w**(3*j) for j in range(i)),R(0)) for i in range(7)]
assert sum((lengths[j]*w**(3*j) for j in range(7)),R(0))==0
assert sum((w**(4*j) for j in range(5)),K(0))==0

def cj(z): return R([a.conjugate() for a in R(z).list()])
def cross(a,b): return (cj(a)*b-a*cj(b))/(2*w**5)
def area(T):
 return sum((cross(T[i],T[(i+1)%len(T)]) for i in range(len(T))),R(0))/2
# Q reflection works identically throughout the parameter family.
assert set(w**8*cj(z) for z in Q)==set(Q)
assert set(w**6*cj(z) for z in P)==set(P)
# In x=h+t>0, all edge/other-vertex strict left-turn polynomials
# have nonnegative real coefficients, at least one strictly positive.
def positive_on_domain(pol):
 shifted=pol(h-t)
 assert shifted and all(c==c.conjugate() and AA(c)>=0 for c in shifted.list())
 assert any(AA(c)>0 for c in shifted.list())
 return str(shifted)
convex=[]
for name,C in [("P",P),("Q",Q)]:
 for i,a in enumerate(C):
  for j,z in enumerate(C):
   if j in (i,(i+1)%len(C)): continue
   pol=cross(C[(i+1)%len(C)]-a,z-a)
   convex.append(dict(face=name,edge=i,vertex=j,polynomial=str(pol),in_x_h_plus_t=positive_on_domain(pol)))
base_pairs=[(0,5),(1,16),(6,23),(4,17),(9,10),(2,21),(3,12),(7,14),(8,19),(11,18),(13,20),(15,22)]
n=[5,5,7,7]; D=[(f,i) for f in range(4) for i in range(n[f])]
index={d:i for i,d in enumerate(D)}
nextd=[index[(f,(i+1)%n[f])] for f,i in D]
labels=['P' if f<2 else ('A' if i==0 else 'B') for f,i in D]
swap=lambda d: d+7 if 10<=d<17 else d-7 if d>=17 else d
maps=[base_pairs,[(min(swap(a),swap(b)),max(swap(a),swap(b))) for a,b in base_pairs]]
shifts0=[(0,0)]*5+[(1,0),(0,1),(-1,0),(0,-1),(0,-1),(1,-1),(1,0)]
L1=w*h+2*w**4+w**2+2
L2=(w**7-w**5+w**3-w)*h+3*w**6-w**4+w**2-3
det=cross(L1,L2)
det_positive=positive_on_domain(det)
a=(w**3-w**7)/2
assert AA(a)>0
assert det(h-t)==a*h**2+(4+k)*h+2*t+4*a
records=[]
for mapid,pairs in enumerate(maps):
 polys=[P,P,Q,Q]
 # Normalize the connected PP/PQ spanning tree (pairs 0,1,3).
 # This solves rotations and translations, without using QQ lengths.
 rot={0:R(1)}; trans={0:R(0)}
 for a,b in [pairs[i] for i in (0,1,3)]:
  f,i=D[a]; g,j=D[b]
  assert f in rot and g not in rot
  ef=polys[f][(i+1)%n[f]]-polys[f][i]
  eg=polys[g][(j+1)%n[g]]-polys[g][j]
  assert ef.degree()==eg.degree()==0
  rot[g]=R(-rot[f]*ef[0]/eg[0])
  trans[g]=rot[f]*polys[f][(i+1)%n[f]]+trans[f]-rot[g]*polys[g][j]
 assert len(rot)==4
 assert all(rot[f]*cj(rot[f])==1 for f in rot)
 tiles=[[rot[f]*z+trans[f] for z in polys[f]] for f in range(4)]
 assert cross(L1,L2)==sum((area(T) for T in tiles),R(0))
 alpha=[None]*24; directed_delta={}; equations=[]
 for e,(a,b) in enumerate(pairs):
  f,i=D[a]; g,j=D[b]
  alpha[a]=b; alpha[b]=a
  va=tiles[f][(i+1)%n[f]]-tiles[f][i]
  vb=tiles[g][(j+1)%n[g]]-tiles[g][j]
  assert va+vb==0
  ds=tiles[f][i]-tiles[g][(j+1)%n[g]]
  de=tiles[f][(i+1)%n[f]]-tiles[g][j]
  assert ds==de
  ab=shifts0[e]
  if mapid==1 and e>=9:ab=(-ab[0],-ab[1])
  assert ds==ab[0]*L1+ab[1]*L2
  directed_delta[a]=ds; directed_delta[b]=-ds
  equations.append(dict(darts=[a,b],faces_edges=[D[a],D[b]],contact_type=('PP' if f<2 and g<2 else 'QQ' if f>=2 and g>=2 else 'PQ'),opposite_edge_residual=str(va+vb),start_displacement=str(ds),end_displacement=str(de),lattice_coefficients=ab,lattice_residual=str(ds-ab[0]*L1-ab[1]*L2)))
 perm=[nextd[alpha[d]] for d in range(24)]
 unseen=set(range(24)); cycles=[]
 while unseen:
  d=min(unseen); c=[]
  while d not in c:
   c.append(d); unseen.remove(d); d=perm[d]
  assert d==c[0]
  word=sorted(labels[d] for d in c)
  assert word in [['A','P','P'],['B','B','P']]
  angles=[108 if labels[d]=='P' else 144 if labels[d]=='A' else 126 for d in c]
  assert sum(angles)==360
  residual=sum((directed_delta[d] for d in c),R(0))
  assert residual==0
  cycles.append(dict(darts=c,labels=[labels[d] for d in c],angles_degrees=angles,total_degrees=sum(angles),vertex_holonomy_residual=str(residual)))
 assert len(cycles)-len(pairs)+4==0
 records.append(dict(map=mapid,pairs=pairs,rotations={str(f):str(rot[f]) for f in rot},translations={str(f):str(trans[f]) for f in trans},edge_equations=equations,vertex_cycles=cycles,vertices=len(cycles),edges=len(pairs),faces=4,euler_characteristic=0,area_residual=str(det-sum((area(T) for T in tiles),R(0)))))
print(json.dumps(dict(status="EXACT_TRANSFER_ALL_ADMISSIBLE_PARAMETERS",domain="real h > -t",t=str(t),k=str(k),coefficient_field="CyclotomicField(20), w=exp(2*pi*i/20)",ring="K[h]",lattice=[str(L1),str(L2)],determinant=str(det),determinant_in_x_h_plus_t=det_positive,strict_convexity_certificates=convex,reflection_symmetry="w^8 conjugate(Q(h))=Q(h)",maps=records,software=sage_version,method="symbolic polynomial identities, exact AA coefficient signs, degree-one local-isometry coverage proof in companion markdown",solver=None,seed=None,timeout=None,complete=True),indent=2,default=lambda x:int(x)))
