"""Independent reconstruction; does not import or execute the producer."""
import itertools,json,cmath
from pathlib import Path
import sympy as s
z=s.Symbol('z'); modulus=s.cyclotomic_poly(30,z)
def R(x):
 n,d=s.fraction(s.cancel(x));return s.rem(n*s.invert(d,modulus,z),modulus,z).expand()
def Z(n):return R(z**(n%30))
def C(x):return R(x.subs(z,Z(-1)))
def D(x,y):return R(C(x)*y-x*C(y))
def N(x):return complex(s.N(x.subs(z,s.exp(s.I*s.pi/15)),30))
pairs=[(1,6),(4,9),(0,10),(2,23),(3,18),(5,17),(7,16),(8,11),(12,15),(13,20),(14,21),(19,22)]
rows=[[108]*5,[108]*5,[144,144,120,120,120,120,132],[144,144,120,120,120,120,132]]
off=[0,5,10,17];sizes=[5,5,7,7]
face={o+i:f for f,(o,n) in enumerate(zip(off,sizes)) for i in range(n)}
prev={o+i:o+(i-1)%n for o,n in zip(off,sizes) for i in range(n)}
H=1+Z(3)+Z(-3)
a=R(H*(Z(3)-Z(-3))/(Z(5)-Z(-5)))
b=R(H*(Z(2)-Z(-2))/(Z(5)-Z(-5)))
vertices=[]
T=[0,Z(6)+2,s.Integer(1),Z(6)+1]
for f,row in enumerate(rows):
 v=[s.Integer(0)];heading=[0,15,15,0][f]
 for i,angle in enumerate(row):
  if i:heading+=(180-angle)//12
  length=([1,1,1,a,b,1,1][i] if f>=2 else 1)
  v.append(R(v[-1]+length*Z(heading)))
 assert v[-1]==0
 vertices.extend([R(x+T[f]) for x in v[:-1]])
u=R(Z(7)-Z(3)-Z(2)-1)
v=R(Z(7)-s.Rational(7,3)*Z(6)-s.Rational(5,3)*Z(5)-s.Rational(5,3)*Z(4)-s.Rational(10,3)*Z(3)+s.Rational(4,3)*Z(2)+s.Rational(7,3)*z-s.Rational(1,3))
coeff=[(0,0),(1,0),(0,0),(0,0),(1,0),(0,0),(0,0),(-1,0),(1,0),(0,1),(-1,1),(-1,0)]
nxt={o+i:o+(i+1)%n for o,n in zip(off,sizes) for i in range(n)}
for (i,j),(m,n) in zip(pairs,coeff):
 shift=R(m*u+n*v)
 assert R(vertices[i]-vertices[nxt[j]]-shift)==0
 assert R(vertices[nxt[i]]-vertices[j]-shift)==0
metric=json.loads(Path('research/searches/resonance-minimal-carrier-sol-2026-10-19-metric.json').read_text())
assert R(s.sympify(metric['k'])-a)==R(s.sympify(metric['ell'])-b)==0
assert all(R(s.sympify(metric['translations'][str(f)])-T[f])==0 for f in range(4))
assert all(R(s.sympify(x)-y)==0 for x,y in zip(metric['basis'],[u,v]))
assert metric['shifts']==[list(c) for c in coeff]
area2=R(sum(D(vertices[i],vertices[nxt[i]]) for i in range(24)))
assert R(area2-2*D(u,v))==0
# The orientation sign is also forced geometrically by positive polygon areas.
print('Lengths',N(a).real,N(b).real,'det',N(D(u,v)/(2*s.I)).real)
alpha=dict(pairs);alpha.update((j,i) for i,j in pairs)
unseen=set(range(24));stars=[]
while unseen:
 t=min(unseen);star=[]
 while t in unseen:
  unseen.remove(t);star.append(t);t=alpha[prev[t]]
 assert t==star[0] and len(star)==3
 assert sum(rows[face[d]][d-off[face[d]]] for d in star)==360
 stars.append(star)
print('Stars',stars)
def matchings(xs):
 if not xs:yield [];return
 for j in range(1,len(xs)):
  for tail in matchings(xs[1:j]+xs[j+1:]):yield [(xs[0],xs[j])]+tail
results=[]
for reflected in [False,True]:
 rr=[r[:] for r in rows]
 if reflected:rr[3]=[144,144,132,120,120,120,120]
 aa=sum(rr,[]);directions=[]
 for row in rr:
  h=0
  for i in range(len(row)):
   if i:h+=180-row[i]
   directions.append(h%360)
 counts=[0,0,0];good=[]
 # Choose AA assignments directly, then biject the four remaining PQ darts.
 for aa_targets in [(10,17),(17,10)]:
  for rest in itertools.permutations([11,16,18,23]):
   cross=[(0,aa_targets[0]),(5,aa_targets[1])]+list(zip([2,3,7,8],rest))
   for pp in matchings([1,4,6,9]):
    for qq in matchings([12,13,14,15,19,20,21,22]):
     counts[0]+=1;edges=pp+cross+qq
     A=dict(edges);A.update((j,i) for i,j in edges)
     # Test each orbit via permutation cube and angle sums, independently of cycle extraction.
     f=lambda d:A[prev[d]]
     if any(f(f(f(d)))!=d or f(d)==d or aa[d]+aa[f(d)]+aa[f(f(d))]!=360 for d in range(24)):continue
     counts[1]+=1
     rotations={0:0}
     for _ in range(4):
      for i,j in edges:
       fi,fj=face[i],face[j];delta=(directions[i]+180-directions[j])%360
       if fi in rotations and fj not in rotations:rotations[fj]=(rotations[fi]+delta)%360
       if fj in rotations and fi not in rotations:rotations[fi]=(rotations[fj]-delta)%360
     if len(rotations)!=4:continue
     if any((rotations[face[j]]-rotations[face[i]]-directions[i]-180+directions[j])%360 for i,j in edges):continue
     counts[2]+=1;good.append(sorted(tuple(sorted(e)) for e in edges))
 results.append(dict(reflected=reflected,counts=counts,maps=good))
assert [r['counts'] for r in results]==[[15120,2,2],[15120,2,0]]
producer=json.loads(Path('research/searches/resonance-minimal-carrier-sol-2026-10-19.json').read_text())
for result,source in zip(results,producer):
 assert result['counts']==[source['counts'][k] for k in ['all','vertex','direction']]
 assert result['maps']==[sorted(tuple(sorted(e)) for e in q['pairs']) for q in source['survivors']]
print('Independent census',results)
