"""One exact analytically selected counterexample: cross-tail M angle >108.
No random scan, metric optimization, common-H claim, or producer imports.
"""
from sage.all import QQbar,AA,QQ
from itertools import combinations
z=QQbar.zeta(60);I=QQbar.gen()
C=lambda n:AA((z**n).real())
S=lambda n:AA((z**n).imag())
cb=AA(100)/AA(10001).sqrt();sb=AA(1)/AA(10001).sqrt()
singamma=S(6)*cb+C(6)*sb
sintotal=S(6)*(cb*cb-sb*sb)+C(6)*(2*cb*sb)
u=singamma*cb/sintotal;h=u/100
qcrit=(100*C(12)-S(12))/(100*S(12)+C(12))
q=qcrit-QQ(1)/10000
m=u-h*q
assert 0<u<1 and 0<m<1 and h>0 and q>QQ(1)/100
cross=lambda a,b:AA((a.conjugate()*b).imag())
dot=lambda a,b:AA((a.conjugate()*b).real())
def strict(poly):
 vals=[cross(poly[(i+1)%len(poly)]-p,v-p) for i,p in enumerate(poly) for j,v in enumerate(poly) if j not in (i,(i+1)%len(poly))]
 return all(x>0 for x in vals) or all(x<0 for x in vals)
def area(poly):return abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2)
def apart(P,Q):
 for poly in (P,Q):
  for i,p in enumerate(poly):
   normal=I*(poly[(i+1)%len(poly)]-p)
   a=[dot(v,normal) for v in P];b=[dot(v,normal) for v in Q]
   if max(a)<=min(b) or max(b)<=min(a):return True
 return False
def cot_at(poly,k):
 a=poly[k-1]-poly[k];b=poly[(k+1)%len(poly)]-poly[k]
 return dot(a,b)/abs(cross(a,b))
ARROWS={'thin':((0,1),(2,1),(2,3),(0,3)),
        'thick':((0,1),(1,2),(3,2),(0,3))}
quads=0;cells_checked=0;target=None
for species,power in (('thin',6),('thick',12)):
 w=z**power;V=(QQbar(0),QQbar(1),1+w,w)
 for parity in (0,1):
  nodes={}
  for e in range(parity,4,2):
   T,H=ARROWS[species][e]
   nodes[e]=V[T]+u*(V[H]-V[T])+h*I*(V[(e+1)%4]-V[e])
  cells=[(V[e],V[(e+1)%4],p) for e,p in nodes.items()]
  cells += [(V[e],V[(e+1)%4],nodes[(e+1)%4],nodes[(e-1)%4]) for e in range(1-parity,4,2)]
  assert all(strict(P) for P in cells)
  assert all(apart(P,Q) for P,Q in combinations(cells,2))
  assert sum(area(P) for P in cells)==S(power)
  assert all(cross(V[(e+1)%4]-V[e],v-V[e])>=0 for P in cells for v in P for e in range(4))
  cells_checked+=1
  for e in range(1-parity,4,2):
   T,H=ARROWS[species][e];along=V[H]-V[T]
   t=V[T]+u*along-h*I*(V[(e+1)%4]-V[e]);M=V[T]+m*along
   p,n=nodes[(e-1)%4],nodes[(e+1)%4]
   assert strict((M,n,p))
   for endpoint,internal in ((e,p),((e+1)%4,n)):
    P=(V[endpoint],t,M,internal)
    assert strict(P),(species,parity,e,endpoint)
    quads+=1
    if (species,parity,e,endpoint)==('thick',0,1,1):target=P
assert quads==16 and cells_checked==4 and target is not None
# Verify explicitly that the proposed branch inequalities also hold.
assert S(1)/C(1)>QQ(1)/100 # beta<6<9.
external_triangle=(QQbar(0),QQbar(u)-I*h,QQbar(m))
cottail=cot_at(external_triangle,1)
assert QQ(200)/9999<cottail<C(12)/S(12) #72<theta_tail<90-2beta.

# Here U is thick Y-tail: source108, incoming beta, outgoing gamma,
# retained angle72, and its internal node is a HEAD node.
cotM=cot_at(target,2)
assert C(19)/S(19)<cotM<C(18)/S(18) # 108 < angle_M < 114.
# Independent closed form in the locally normalized cross-tail frame.
Lhead=h/singamma
a=Lhead*(C(12)*cb+S(12)*sb)
b=Lhead*(S(12)*cb-C(12)*sb)
assert 0<a<m and b>0
v=QQbar(u-m)-I*h;w=QQbar(a-m)+I*b
assert dot(v,w)/abs(cross(v,w))==cotM
assert b/(m-a)>QQ(1)/100
# The small perturbation is explicit, not selected by a parameter census.
assert m-(u-h*qcrit)==h/10000
print('PASS exact counterexample: tan(beta)=1/100; q=cot(72+beta)-1/10000; m=u-h*q. All4 source partitions and16 precursor quads strict. Thick cross-tail angle_M lies STRICTLY between108 and114 degrees. No common H or cap realization claimed.')
