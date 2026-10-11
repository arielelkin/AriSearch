"""Independent full complementary cone and fixed-indexed-carrier two-branch audit.
No author imports. Raw rational geometry, actual links and full fixture lattice.
"""
from sage.all import QuadraticField,PolynomialRing,AA,QQ,QQbar,matrix,vector,ZZ,gcd,ceil,floor
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,['t','u','v','P']);t,u,v,P=R.gens();F=R.fraction_field()
cs=lambda x:F(1-x*x)/F(1+x*x)
sn=lambda x:F(2*x)/F(1+x*x)
cd,sd,ca,sa,cb,sb=cs(t),sn(t),cs(u),sn(u),cs(v),sn(v)
def rot(x,C,S):return (C*x[0]-S*x[1],S*x[0]+C*x[1])
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return x[0]*y[1]-x[1]*y[0]
def poly(edges):
 out=[];z=(F(0),F(0))
 for edge in edges:out.append(z);z=add(z,edge)
 assert z==(0,0)
 return out
p=2*cd
A=[]
for C,S in [(1,0),(-K(1)/2,w/2),(-K(1)/2,-w/2)]:A.extend([rot((p,0),C,S),rot(rot((K(1)/2,w/2),cd,sd),C,S)])
qchain=[rot(rot((K(1)/2,-w/2),cd,-sd),ca,-sa),rot((cd,sd),ca,-sa),rot(rot((K(1)/2,w/2),cd,-sd),ca,-sa)]
B=[(p,0),(-p*ca,p*sa),(-p,0)]+qchain
raw=[poly(A),poly(B)]
for typ,edges in enumerate((A,B)):
 for i,e in enumerate(edges):
  length=p if (i%2==0 if typ==0 else i<3) else 1
  assert sum(a*a for a in e)==length*length
# Independent arbitrary-alpha/beta closure, as required by fixed carrier necessity.
Bgeneral=[(P,0),(-P*ca,P*sa),(P*(ca*cb-sa*sb),-P*(sa*cb+ca*sb))]+qchain
closure=rot(tuple(sum(e[k] for e in Bgeneral) for k in (0,1)),ca,sa)
assert closure==(P*(ca-1+cb)+2*cd,P*(sa-sb))
assert sa-sb==2*(u-v)*(1-u*v)/((1+u*u)*(1+v*v))
# For positive half-angle parameters the only two branches are v=u or v=1/u.
assert F(ca-1+cb).subs({v:u})==2*ca-1
assert F(ca-1+cb).subs({v:1/u})==-1
D=[[(0,0,0),(60,1,0),(120,0,0),(180,1,0),(240,0,0),(300,1,0)],[(0,0,0),(180,0,-1),(180,0,0),(300,-1,-1),(360,1,-1),(420,-1,-1)]]
angles=[];turns=[]
for word in D:
 angles.append([(180+word[i-1][0]-word[i][0]-(360 if i==0 else 0),word[i-1][1]-word[i][1],word[i-1][2]-word[i][2]) for i in range(6)])
 turns.append([(word[(i+1)%6][0]-word[i][0]+(360 if i==5 else 0),word[(i+1)%6][1]-word[i][1],word[(i+1)%6][2]-word[i][2]) for i in range(6)])
verts=[(0,60),(0,120),(30,90),(30,30)];bounds=[]
for tw in turns:
 assert tuple(sum(a[k] for a in tw) for k in range(3))==(360,0,0)
 for a in tw:
  values=[a[0]+a[1]*d+a[2]*h for d,h in verts]
  assert min(values)>=0 and 0<max(values)<180;bounds.append((min(values),max(values)))
root=Path(__file__).resolve().parents[1]
r=json.loads((root/'certificates/branching-hexagon-new-two-run-complementary-pp-periodic-cone.json').read_text())
for typ,name in enumerate(('A','B')):
 assert [list(a) for a in D[typ]]==r[name+'_edge_directions']
 assert [list(a) for a in angles[typ]]==r[name+'_angles']
 assert [list(a) for a in turns[typ]]==r[name+'_turns']
assert [list(a) for a in verts]==r['closed_parameter_polygon_vertices']
assert bounds==[(a['closed_domain_min'],a['closed_domain_max']) for a in r['turn_bounds']]
fs=r['faces'];pairs=r['paired_edges'];assert len(fs)==8 and len(pairs)==24
assert [(f['species'],f['mirror']) for f in fs]==[('A',False)]*2+[('A',True)]*2+[('B',False)]*2+[('B',True)]*2
labels=[['p','q']*3,['p']*3+['q']*3];fa=[];fl=[]
for f in fs:
 typ=0 if f['species']=='A' else 1
 fa.append([angles[typ][(-i)%6] for i in range(6)] if f['mirror'] else angles[typ])
 fl.append(labels[typ][::-1] if f['mirror'] else labels[typ]);assert f['labels']==fl[-1]
succ={};dual=[set() for f in fs]
for (a,i),(b,j) in pairs:
 assert fl[a][i]==fl[b][j]
 assert (a,i) not in succ and(b,j) not in succ
 succ[a,i]=(b,(j+1)%6);succ[b,j]=(a,(i+1)%6);dual[a].add(b);dual[b].add(a)
assert len(succ)==48 and len(set(succ.values()))==48
unseen=set(succ);links=[];types=Counter();necessary=[]
while unseen:
 start=min(unseen);a=start;link=[]
 while a not in link:link.append(a);unseen.remove(a);a=succ[a]
 assert a==start and len(link)==3
 assert tuple(sum(fa[a][i][k] for a,i in link) for k in range(3))==(360,0,0)
 links.append(frozenset(link));names=[];row=[0]*8;row[6]=-360
 for a,i in link:
  f=fs[a];j=(-i)%6 if f['mirror'] else i
  if f['species']=='B':row[j]+=1;names.append('B'+str(j))
  else:row[6]+=120;row[7]+=1 if j%2==0 else -1;names.append('AH' if j%2==0 else 'AL')
 necessary.append(row);types[tuple(sorted(names))]+=1
assert len(links)==16 and set(links)=={frozenset(map(tuple,a)) for a in r['vertex_classes']}
assert types==Counter({('AH','B0','B1'):4,('AL','B2','B3'):4,('AH','AH','B4'):4,('AL','AL','B5'):4})
# Unknown native B angles: exact rowspace shows no extra or missing carrier constraint.
expected=matrix(QQ,[[1,1,0,0,0,0,-240,1],[0,0,1,1,0,0,-240,-1],[0,0,0,0,1,0,-120,2],[0,0,0,0,0,1,-120,-2]])
actual=matrix(QQ,necessary)
assert actual.rank()==4 and actual.row_space()==expected.row_space()
seen={0};todo=[0]
while todo:
 for a in dual[todo.pop()]:
  if a not in seen:seen.add(a);todo.append(a)
assert len(seen)==8 and 16-24+8==0
# Exact noncentral delta15 alpha75 raw geometry and full developed lattice check.
r2=AA(2).sqrt();r3=AA(3).sqrt();r6=AA(6).sqrt();c15=(r6+r2)/4;s15=(r6-r2)/4
sample_t=s15/(1+c15);sample_u=c15/(1+s15)
def evaluate(v):return tuple(AA(a(t=sample_t,u=sample_u)) for a in v)
native=[list(map(evaluate,a)) for a in raw];refs=[]
for f in fs:
 pts=native[0 if f['species']=='A' else 1]
 refs.append([(pts[(-i)%6][0],-pts[(-i)%6][1]) for i in range(6)] if f['mirror'] else pts)
for pts in refs:
 for i in range(6):
  for j in range(6):
   if j not in(i,(i+1)%6):assert cross(sub(pts[(i+1)%6],pts[i]),sub(pts[j],pts[i]))>0
z=QQbar.zeta(24)
def decode(encoded):
 a=sum(QQbar(QQ(c))*z**i for i,c in enumerate(encoded));return(AA(a.real()),AA(a.imag()))
dev=json.loads((root/'certificates/branching-hexagon-new-two-run-complementary-pp-eight-face-development.json').read_text())
assert dev['fixture_parameters']=={'delta':15,'alpha':75,'q':1}
assert decode(dev['p'])==(2*c15,0)
assert [list(map(decode,a)) for a in dev['reference_vertices']]==refs
placed=[]
for pts,tf in zip(refs,dev['face_transforms']):
 C,S=decode(tf['rotation']);shift=decode(tf['translation']);assert C*C+S*S==1
 placed.append([add(rot(v,C,S),shift) for v in pts])
U,V=map(decode,dev['period_lattice']);basis=matrix(AA,[[U[0],V[0]],[U[1],V[1]]]);inverse=basis.inverse();assert basis.det()!=0
hol=[];ints=[]
for (a,i),(b,j) in pairs:
 X,Y=placed[a],placed[b];assert sub(X[(i+1)%6],X[i])==sub(Y[j],Y[(j+1)%6])
 h=sub(X[i],Y[(j+1)%6]);hol.append(h);q=inverse*vector(AA,h)
 assert all(v in ZZ for v in q);ints.append(tuple(ZZ(v) for v in q))
assert hol==list(map(decode,dev['seam_holonomies']))
assert gcd([abs(cross(a,b)) for a,b in combinations(ints,2)])==1
area=lambda pts:sum(cross(a,pts[(i+1)%6]) for i,a in enumerate(pts))/2
assert all(area(a)>0 for a in refs)
assert abs(basis.det())==sum(area(a) for a in refs)==decode(dev['covolume'])[0]
assert decode(dev['covolume'])[1]==0 and list(map(decode,dev['tile_areas']))==[(area(a),0) for a in refs]
def separated(P,Q):
 for pts in (P,Q):
  for a,b in zip(pts,pts[1:]+pts[:1]):
   e=sub(b,a);n=(-e[1],e[0]);A=[sum(x*y for x,y in zip(v,n)) for v in P];B=[sum(x*y for x,y in zip(v,n)) for v in Q]
   if max(A)<=min(B) or max(B)<=min(A):return True
 return False
coordinates=[[inverse*vector(AA,v) for v in P] for P in placed];checks=0;maxindex=0
for i,P in enumerate(placed):
 for j,Q in enumerate(placed):
  ranges=[]
  for k in (0,1):
   lo=ceil(min(v[k] for v in coordinates[i])-max(v[k] for v in coordinates[j]));hi=floor(max(v[k] for v in coordinates[i])-min(v[k] for v in coordinates[j]));ranges.append(range(lo,hi+1))
  for m,n in product(*ranges):
   if i==j and m==n==0:continue
   T=[add(v,add(tuple(m*a for a in U),tuple(n*a for a in V))) for v in Q]
   assert separated(P,T),(i,j,m,n);checks+=1;maxindex=max(maxindex,abs(m),abs(n))
print('PASS full complementary cone: rational native closure/norms;12strict affine turn bounds;48unique seams;16actual360+0delta+0alpha links;connected flat torus.')
print('PASS exact fixed-carrier necessity:unknown-B angle rowspace rank4;general rational closure;sin equation factors(u-v)(1-u*v);exact equal/complementary real closures. Scope fixedindexed carrier only.')
print('PASS noncentral fixture:8original congruent polygons,24translation holonomies,primitive integral lattice,exact area/covolume and COMPLETE',checks,'SAT pairs;maxindex',maxindex)
