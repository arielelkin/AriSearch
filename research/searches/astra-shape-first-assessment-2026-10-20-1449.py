"""Exact three-arm convex-parent experiment and finite first-boundary rejection."""
from sage.all import AA, RealIntervalField, matrix, vector
from importlib.util import spec_from_file_location, module_from_spec
from itertools import product
s=AA(3).sqrt(); R=matrix(AA,[[-AA(1)/2,-s/2],[s/2,-AA(1)/2]])
O=vector(AA,[0,0]); S=vector(AA,[1,0]); T=R*S
v=vector(AA,[AA(1)/10,AA(3)/5]); V=S+v; W=T-R*v
P=[O,S,V,W,T]; G=[V,W,R*V,R*W,R*R*V,R*R*W]
lam=(2+AA(7).sqrt()).sqrt(); H=[x/lam for x in G]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(p): return sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2
def data(p):
 n=len(p); edges=[p[(i+1)%n]-p[i] for i in range(n)]; lengths=[x.norm() for x in edges]
 assert all(cross(edges[i],edges[(i+1)%n])>0 for i in range(n))
 rif=RealIntervalField(128)
 angles=[rif(-edges[i-1].dot_product(edges[i])/(lengths[i-1]*lengths[i])).arccos()*180/rif.pi() for i in range(n)]
 return lengths,angles
pl,pa=data(P); gl,ga=data(G); hl,ha=data(H)
a=AA(37).sqrt()/10; b=((337-120*s)/100).sqrt()
assert pl==[AA(1),a,b,a,AA(1)] and gl==[b,2*a,b,2*a,b,2*a]
assert cross(V-S,R*R*W-S)==0 and (V-S).dot_product(R*R*W-S)<0
assert area(G)==3*area(P)
# P lies in the closed 120-degree sector from S to T, so its three rotations
# have disjoint interiors; their areas equal G, proving the exact dissection.
assert all(cross(S,x)>=0 and cross(x,T)>=0 for x in P)
assert all(cross(G[(i+1)%6]-G[i],x-G[i])>=0 for x in P for i in range(6))
assert lam**2*area(H)==3*area(P)
assert lam**2*area(P)==4*area(P)+area(H)
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec); spec.loader.exec_module(mod)
possible=[]
for typ,(aeqs,leqs) in mod.RAO.items():
 for sign in (1,-1):
  for off in range(5):
   aa=[pa[(off+sign*i)%5] for i in range(5)]
   smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
   if all(0 in sum(c*x for c,x in zip(row,aa))-36*target for row,target in aeqs) and all(sum(c*pl[i] for c,i in zip(row,smap))==0 for row in leqs): possible.append((typ,sign,off))
assert not possible
assert all(x>90 for x in ga)
assert all(0 not in k*ga[0]+(3-k)*ga[1]-360 for k in range(4))
# Each strictly convex child contributes at most one entire edge to a fixed
# parent side. Four P children, one H child: this deliberately overinclusive
# list of 105 edge sums contains every possible cover of the length-lam side.
cases=[]; hits=[]
for m,n,k in product(range(5),repeat=3):
 if m+n+k>4:continue
 for h in (AA(0),b/lam,2*a/lam):
  cases.append((m,n,k,h))
  if lam==m+n*a+k*b+h:hits.append((m,n,k,h))
assert len(cases)==105 and not hits
print('Strict convexity and exact three-arm G=3P dissection: PASS')
print('Rao possible hits:',possible,'; H corner triples: none')
print('P angles:',pa)
print('G/H angles:',ga)
print('Prescribed lambda P = 4P + H first-side covers:',len(cases),'checked,',len(hits),'hits')
print('FIXED SUBSTITUTION REJECTED; unrestricted pair tilability unresolved')
