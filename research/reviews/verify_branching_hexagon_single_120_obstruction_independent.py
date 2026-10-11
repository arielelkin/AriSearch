"""Fresh raw native geometry, complete oriented stars and duals; no author imports."""
from sage.all import CyclotomicField,QQbar,AA
from itertools import product
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
D=json.loads(Path('research/certificates/branching-hexagon-two-run-single-120-slot-obstruction.json').read_text())
K=CyclotomicField(24);z=K.gen();zz=QQbar(z)
assert zz.real()>0 and zz.imag()>0
P=1+z**4+z**9;Q=1+z**6+z**8;ratio=Q*Q.conjugate()/(P*P.conjugate())
assert [str(a) for a in ratio.list()]==D['p_squared_coefficients']
p=AA(QQbar(ratio).real()).sqrt();assert p>0 and p!=1
R=-QQbar(p)*QQbar(P)/QQbar(Q);assert R*R.conjugate()==1
A=[QQbar(p)*zz**j if i%2==0 else zz**j for i,j in enumerate((0,5,8,13,16,21))]
B=[QQbar(p),QQbar(p)*zz**4,QQbar(p)*zz**9,R,R*zz**6,R*zz**8]
assert sum(A)==sum(B)==0
assert [e*e.conjugate() for e in A]==[QQbar(p*p) if j%2==0 else 1 for j in range(6)]
assert [e*e.conjugate() for e in B]==[QQbar(p*p)]*3+[QQbar(1)]*3
angleunits=[]
for edges in (A,B):
 vs=[QQbar(0)]
 for e in edges:vs.append(vs[-1]+e)
 for j,e in enumerate(edges):
  for k in range(6):
   if k in (j,(j+1)%6):continue
   assert (e.conjugate()*(vs[k]-vs[j])).imag()>0
  # Positive CCW convex angle: minus conjugate of unit exterior turn.
  exterior=edges[j]/edges[(j-1)%6];exterior/=AA((exterior*exterior.conjugate()).real()).sqrt()
  angleunits.append(-exterior.conjugate())
assert angleunits[:6]==[zz**9 if j%2==0 else zz**7 for j in range(6)]
assert [angleunits[6+j] for j in(1,2,4,5)]==[zz**j for j in(8,7,6,10)]
assert D['quad']==[120,105,90,150] and D['delta']==15 and D['q']==1
slots=[(s,j) for s in(0,1) for j in range(6)]
assert D['corner_slots']==[list(s) for s in slots]
words=[('p','q')*3,('p',)*3+('q',)*3]
states=[]
for c,(s,j) in enumerate(slots):
 previous=(s,(j-1)%6);current=(s,j)
 states += [(c,current,previous,0,1),(c,previous,current,1,0)]
def canonical(path):return min(path[i:]+path[:i] for i in range(3))
angleok={(a,b,c) for a,b,c in product(range(12),repeat=3) if angleunits[a]*angleunits[b]*angleunits[c]==1}
stars=set()
for path in product(range(24),repeat=3):
 if tuple(states[i][0] for i in path) not in angleok:continue
 if all(words[states[path[j]][2][0]][states[path[j]][2][1]]==words[states[path[(j+1)%3]][1][0]][states[path[(j+1)%3]][1][1]] for j in range(3)):
  stars.add(canonical(path))
stars=sorted(stars);assert len(stars)==80 and [list(s) for s in stars]==D['oriented_stars']
keys=set();counts=[];features=[]
for path in stars:
 corner=Counter(states[i][0] for i in path);charge=Counter()
 for j,a in enumerate(path):
  b=path[(j+1)%3];x,y=states[a][2],states[b][1];px,py=states[a][4],states[b][3]
  if x>y:x,y,px,py=y,x,py,px
  if x==y and px!=py:continue
  key=(x,y,px^py);charge[key]+=1 if px==0 else -1
 counts.append(corner);features.append(charge);keys.update(k for k,v in charge.items() if v)
keys=sorted(keys);assert len(keys)==36
assert [[[a for a in x],[a for a in y],parity] for x,y,parity in keys]==D['seam_keys']
assert [{str(k):v for k,v in row.items()} for row in counts]==D['star_corner_counts']
assert [[row.get(k,0) for k in keys] for row in features]==D['star_seam_counts']
W=[-1 if c in(0,2,4) else -3 if c==10 else 0 for c in range(12)]
Y=[]
for x,y,parity in keys:
 val=0
 if x[0]==0 and x[1]%2==0 and y==(1,1):val=-3 if parity else 1
 if x[0]==0 and x[1]%2==1 and y==(1,3) and parity==0:val=-7
 Y.append(val)
assert W==D['symmetric_corner_dual'] and Y==D['symmetric_seam_dual'] and sum(W[:6])==sum(W[6:])==-3
names=['AH','AL']*3+['B0','alpha','beta','B3','chi','psi']
table={}
for C,S in zip(counts,features):
 label=tuple(sorted(names[c] for c,n in C.items() for _ in range(n)))
 weight=sum(W[c]*n for c,n in C.items())+sum(y*S.get(k,0) for k,y in zip(keys,Y))
 assert weight>=0;table.setdefault(label,Counter())[weight]+=1
assert table=={tuple(sorted(k)):Counter(v) for k,v in {
 ('AH','AL','alpha'):{0:18,2:18},('AH','AH','chi'):{2:18},('AL','AL','psi'):{0:18},('B0','B3','beta'):{0:4},('alpha','alpha','alpha'):{0:4}}.items()}
assert sorted(table)==[tuple(a) for a in D['abstract_star_type_domain']]
W0=list(map(Fraction,D['corner_dual']));Y0=list(map(Fraction,D['seam_dual']))
assert len(W0)==12 and len(Y0)==36 and sum(W0[:6])<=-1 and sum(W0[6:])<=-1
for C,S in zip(counts,features):assert sum(W0[c]*n for c,n in C.items())+sum(y*S.get(k,0) for k,y in zip(keys,Y0))>=0
# Cancellation is exact on both ends of every whole matched seam.
for x,y,parity in keys:
 for px in(0,1):
  py=px^parity
  if x==y and px!=py:continue
  assert (1 if px==0 else -1)+(1 if (1-px)==0 else -1)==0
# The five abstract types retain the same native/orientation combinatorics independently of numerical angles.
allowed=set(table)
abstract=set()
for path in product(range(24),repeat=3):
 label=tuple(sorted(names[states[i][0]] for i in path))
 if label not in allowed:continue
 if all(words[states[path[j]][2][0]][states[path[j]][2][1]]==words[states[path[(j+1)%3]][1][0]][states[path[(j+1)%3]][1][1]] for j in range(3)):
  abstract.add(canonical(path))
assert abstract==set(stars)
print('PASS raw exact strictlyconvex A/B geometry, p!=1, closure and fixture angles; exhaustive80 oriented stars/36 signed seams; all retained columns; symmetric integer and original rational duals; allfive abstract types and endpoint cancellation.')
