"""Independent full-curve algebra, quotient links and delta15 lattice geometry.
No author imports. Certificate data are checked against raw native geometry.
"""
from sage.all import QuadraticField,PolynomialRing,AA,QQbar,CyclotomicField,vector,gcd,ceil,floor,ZZ,QQ
from itertools import product,combinations
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,'t');t=R.gen();F=R.fraction_field()
c=F(1-t*t)/F(1+t*t);s=F(2*t)/F(1+t*t);p=2*c/(1+w)
def rotate(v,C,S):return (C*v[0]-S*v[1],S*v[0]+C*v[1])
def add(u,v):return tuple(a+b for a,b in zip(u,v))
def sub(u,v):return tuple(a-b for a,b in zip(u,v))
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def polygon(edges):
 out=[];v=(F(0),F(0))
 for e in edges:out.append(v);v=add(v,e)
 assert v==(0,0)
 return out
A=[]
for C,S in [(1,0),(-K(1)/2,w/2),(-K(1)/2,-w/2)]:
 A.extend([rotate((p,0),C,S),rotate((c/2-w*s/2,w*c/2+s/2),C,S)])
B=[(p,0),(w*p/2,p/2),(p/2,w*p/2),rotate((-w/2,K(1)/2),c,-s),rotate((-w/2,-K(1)/2),c,s),rotate((0,-1),c,-s)]
raw=[polygon(A),polygon(B)]
# Exact sign isolation for every full-curve supporting determinant.
endpoint=AA(2-w);mid=endpoint/2
SAA=PolynomialRing(AA,'T')
def nonzero_positive_poly(poly):
 q=SAA([AA(a) for a in poly.list()]);assert q
 assert not any(0<r<endpoint for r,m in q.roots())
 return q(mid)>0
support_count=0
for pts,edges in zip(raw,[A,B]):
 for i,e in enumerate(edges):
  for j in range(6):
   if j in (i,(i+1)%6):continue
   q=F(cross(e,sub(pts[j],pts[i])))
   assert nonzero_positive_poly(q.numerator())==nonzero_positive_poly(q.denominator())
   support_count+=1
assert support_count==48
baseangles=[[(120,1),(120,-1)]*3,[(90,-1),(150,0),(150,0),(90,1),(120,-2),(120,2)]]
direction_words=[[(0,0),(60,1),(120,0),(180,1),(240,0),(300,1)],[(0,0),(30,0),(60,0),(150,-1),(210,1),(270,-1)]]
for typ,word in enumerate(direction_words):
 derived=[]
 for i,(a,b) in enumerate(word):
  prev_a,prev_b=word[i-1]
  if i==0:prev_a-=360
  derived.append((180+prev_a-a,prev_b-b))
 assert derived==baseangles[typ]
 assert all(0<=a<=180 and 0<=a+30*b<=180 and 0<a+15*b<180 for a,b in derived)
for typ,ee in enumerate((A,B)):
 for i,e in enumerate(ee):
  norm=p if (i%2==0 if typ==0 else i<3) else 1
  assert sum(a*a for a in e)==norm*norm
labels=[['p','q']*3,['p']*3+['q']*3]
root=Path(__file__).resolve().parents[1]
quotient=json.loads((root/'certificates/branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json').read_text())
faces=quotient['faces'];pairs=quotient['paired_edges'];assert len(faces)==8 and len(pairs)==24
assert [(f['species'],f['mirror']) for f in faces]==[('A',False)]*2+[('A',True)]*2+[('B',False)]*2+[('B',True)]*2
ang=[];flabel=[]
for f in faces:
 typ=0 if f['species']=='A' else 1
 a=baseangles[typ];l=labels[typ]
 if f['mirror']:a=[a[(-i)%6] for i in range(6)];l=l[::-1]
 ang.append(a);flabel.append(l);assert f['labels']==l
# Following each outgoing side into its glued incoming ray gives actual link cycles.
successor={};dual=[set() for _ in faces]
for (u,i),(v,j) in pairs:
 assert flabel[u][i]==flabel[v][j]
 assert (u,i) not in successor and (v,j) not in successor
 successor[u,i]=(v,(j+1)%6);successor[v,j]=(u,(i+1)%6)
 dual[u].add(v);dual[v].add(u)
assert len(successor)==48 and len(set(successor.values()))==48
unseen=set(successor);cycles=[]
while unseen:
 start=min(unseen);a=start;cycle=[]
 while a not in cycle:cycle.append(a);unseen.remove(a);a=successor[a]
 assert a==start and len(cycle)==3
 assert tuple(sum(ang[u][i][j] for u,i in cycle) for j in (0,1))==(360,0)
 cycles.append(frozenset(cycle))
assert len(cycles)==16 and set(cycles)=={frozenset(map(tuple,c)) for c in quotient['vertex_classes']}
seen={0};todo=[0]
while todo:
 for v in dual[todo.pop()]:
  if v not in seen:seen.add(v);todo.append(v)
assert len(seen)==8 and 16-24+8==0
# Independent Cartesian native delta15 polygons.
r2=AA(2).sqrt();r3=AA(3).sqrt();r6=AA(6).sqrt();c15=(r6+r2)/4;s15=(r6-r2)/4;p15=1/r2
assert AA((2*c15/(1+r3)))==p15
sample_t=s15/(1+c15)
def evaluate(v):return tuple(AA(a(sample_t)) for a in v)
native=[list(map(evaluate,pts)) for pts in raw]
refs=[]
for f in faces:
 pts=native[0 if f['species']=='A' else 1]
 refs.append([(pts[(-i)%6][0],-pts[(-i)%6][1]) for i in range(6)] if f['mirror'] else pts)
def area(pts):return sum(cross(a,pts[(i+1)%len(pts)]) for i,a in enumerate(pts))/2
assert area(native[0])==AA(3)/4+5*r3/8 and area(native[1])==1+3*r3/8
C24=CyclotomicField(24);z=C24.gen();zc=QQbar.zeta(24)
def decode(coeff):
 a=sum(QQbar(QQ(v))*zc**i for i,v in enumerate(coeff))
 return (AA(a.real()),AA(a.imag()))
dev=json.loads((root/'certificates/branching-hexagon-new-two-run-third-orbit-eight-face-development.json').read_text())
assert decode(dev['p'])==(p15,0)
assert [list(map(decode,pp)) for pp in dev['reference_vertices']]==refs
trans=[];placed=[]
for pts,f in zip(refs,dev['face_transforms']):
 rot=decode(f['rotation']);shift=decode(f['translation']);assert sum(a*a for a in rot)==1
 trans.append((rot,shift));placed.append([add(rotate(a,*rot),shift) for a in pts])
x=r6/2+r2;H=(x,AA(0));L=(AA(0),2*x);seams=[];integers=[]
for (u,i),(v,j) in pairs:
 P,Q=placed[u],placed[v]
 assert sub(P[(i+1)%6],P[i])==sub(Q[j],Q[(j+1)%6])
 d=sub(P[i],Q[(j+1)%6]);seams.append(d)
 m=d[0]/x;n=d[1]/(2*x);assert m in ZZ and n in ZZ;integers.append((ZZ(m),ZZ(n)))
assert seams==list(map(decode,dev['seam_holonomies']))
# gcd of all2x2 minors proves this is the complete primitive integer module.
assert gcd([abs(cross(a,b)) for a,b in combinations(integers,2)])==1
assert list(map(decode,dev['period_lattice']))==[(x,2*x),(2*x,6*x)]
assert decode(dev['covolume'])==(7+4*r3,0)
assert 2*x*x==sum(area(P) for P in placed)==7+4*r3
assert list(map(decode,dev['tile_areas']))==[(area(P),0) for P in refs]
# Complete bounding-box inverse rectangular-lattice bound, exact SAT.
def separated(P,Q):
 for S in (P,Q):
  for a,b in zip(S,S[1:]+S[:1]):
   e=sub(b,a);normal=(-e[1],e[0]);pa=[sum(x*y for x,y in zip(v,normal)) for v in P];qa=[sum(x*y for x,y in zip(v,normal)) for v in Q]
   if max(pa)<=min(qa) or max(qa)<=min(pa):return True
 return False
comparisons=0;maxindex=0
for i,P in enumerate(placed):
 for j,Q in enumerate(placed):
  ranges=[]
  for k,period in enumerate((x,2*x)):
   low=ceil((min(a[k] for a in P)-max(a[k] for a in Q))/period)
   high=floor((max(a[k] for a in P)-min(a[k] for a in Q))/period)
   ranges.append(range(low,high+1))
  for m,n in product(*ranges):
   if i==j and m==n==0:continue
   shift=(m*x,n*2*x);T=[add(a,shift) for a in Q]
   assert separated(P,T),(i,j,m,n)
   comparisons+=1;maxindex=max(maxindex,abs(m),abs(n))
print('PASS fullcurve: raw rational closure;48 exact strict support inequalities;48 unique seams;16 actual circular360+0delta links;connected orientable torus.')
print('PASS delta15:8 native congruent placements;all24 translational seam holonomies;full primitive rectangular lattice;exact area/covolume;complete SAT comparisons',comparisons,'maxindex',maxindex)
