"""Fresh retained-certificate audit; no solver and no author imports.
Domain: all nine-plane affine intersections in three variables, every indexed
binary sector triple, rational negative duals, and four full carrier transfers.
"""
from collections import Counter
from itertools import product, combinations
from fractions import Fraction
from sage.all import QQ, matrix, vector, PolynomialRing, SR, sin, cos, sqrt, pi
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
doc=json.loads((root/'research/certificates/branching-hexagon-two-run-center-pp-pure-qq-strata-slot-balance.json').read_text())
angle=[(120,1,0,0),(120,-1,0,0)]*3+[(300,0,-1,-1),(120,0,0,0),(120,0,0,0),(60,0,0,1),(120,0,0,0),(0,0,1,0)]
words=('pqpqpq','pppqqq')
sector=[]
for cid in range(12):
 s,j=divmod(cid,6)
 for mirror in range(2):
  nextside=(s,j); prevside=(s,(j-1)%6)
  endpoints=((nextside,0),(prevside,1))
  if mirror:endpoints=endpoints[::-1]
  sector.append((cid,endpoints))
raw={}
for codes in product(range(24),repeat=3):
 if any(words[sector[codes[j]][1][1][0][0]][sector[codes[j]][1][1][0][1]] != words[sector[codes[(j+1)%3]][1][0][0][0]][sector[codes[(j+1)%3]][1][0][0][1]] for j in range(3)):continue
 key=min(codes,codes[1:]+codes[:1],codes[2:]+codes[:2])
 residual=tuple(sum(angle[sector[k][0]][i] for k in key)-(360 if i==0 else 0) for i in range(4))
 raw[key]=residual
# Rank-one residual row spaces independently recover the nine nonexcluded planes.
plane_spaces={tuple(matrix(QQ,[r]).row_space().basis_matrix().row(0)) for r in raw.values() if any(r)}
plane_spaces -= {tuple(matrix(QQ,[r]).row_space().basis_matrix().row(0)) for r in [(0,1,0,0),(120,0,-1,0)]}
planes=[tuple(p) for p in doc['inventory']['exception_planes9']]
assert plane_spaces=={tuple(matrix(QQ,[p]).row_space().basis_matrix().row(0)) for p in planes}
flats={}; subsets=0
for k in range(4):
 for ids in combinations(range(9),k):
  subsets+=1; m=matrix(QQ,[planes[i] for i in ids]) if ids else matrix(QQ,0,4)
  if m.rank()!=m[:,1:].rank():continue
  basis=m.row_space().basis_matrix(); key=tuple(tuple(str(x) for x in r) for r in basis.rows())
  flats.setdefault(key,[]).append(list(ids))
assert subsets==130 and len(flats)==31

def charge(left,right):
 (x,px),(y,py)=left,right
 if x==y and px!=py:return None,0
 if y<x:x,y,px,py=y,x,py,px
 return (x,y,px^py),1-2*px
for left,right in product([((s,j),e) for s,j,e in product(range(2),range(6),range(2))],repeat=2):
 (s,j),px=left;(t,k),py=right
 if words[s][j]!=words[t][k]:continue
 feature,w=charge(left,right); reverse,v=charge(((s,j),1-px),((t,k),1-py))
 assert feature==reverse and w+v==0
seen=set(); total=ndual=0;statuses=Counter()
for rec in doc['linear_infeasible_flats']+doc['records']:
 key=tuple(map(tuple,rec['flat_basis'])); assert key in flats and key not in seen;seen.add(key)
 assert rec['generating_subsets']==flats[key]
 m=matrix(QQ,[[QQ(x) for x in r] for r in key]) if key else matrix(QQ,0,4)
 space=m.row_space();active=[i for i,p in enumerate(planes) if vector(QQ,p) in space]
 assert active==rec['active_exception_planes']
 if 'status' not in rec:
  assert vector(QQ,[0,1,0,0]) in space or vector(QQ,[120,0,-1,0]) in space
  continue
 d,t,r=map(QQ,rec['strict_linear_sample']);pt=vector(QQ,[1,d,t,r])
 assert 0<d<30 and 0<t<180 and t!=120 and 0<r<90 and r+t>120
 assert all(b*pt==0 for b in m.rows())
 assert all((vector(QQ,p)*pt==0)==(i in active) for i,p in enumerate(planes))
 legal=sorted(st for st,row in raw.items() if vector(QQ,row) in space)
 assert list(map(list,legal))==rec['oriented_stars'];total+=len(legal)
 columns=[];seams=[];keys=set()
 for st in legal:
  corners=Counter(sector[k][0] for k in st);seam=Counter()
  for j,k in enumerate(st):
   feature,weight=charge(sector[k][1][1],sector[st[(j+1)%3]][1][0])
   if feature is not None:seam[feature]+=weight
  columns.append(corners);seams.append(seam);keys.update(seam)
 keys=sorted(keys)
 assert [[list(x),list(y),p] for x,y,p in keys]==rec['seam_keys']
 assert [{str(k):v for k,v in c.items()} for c in columns]==rec['star_corner_counts']
 assert [[c[k] for k in keys] for c in seams]==rec['star_seam_counts']
 statuses[rec['status']]+=1
 if rec['status']=='unsat':
  W=list(map(Fraction,rec['corner_dual']));Y=dict(zip(keys,map(Fraction,rec['seam_dual'])))
  assert sum(W[:6])<=-1 and sum(W[6:])<=-1
  assert all(sum(W[k]*v for k,v in c.items())+sum(Y[k]*v for k,v in s.items())>=0 for c,s in zip(columns,seams));ndual+=len(legal)
 else:
  assert rec['status']=='sat' and set(active)&{0,2,5,7}
  f=list(map(Fraction,rec['species_frequencies']));x=list(map(Fraction,rec['star_frequencies']))
  assert len(x)==len(legal) and min(f+x)>=0 and sum(f)==1
  assert all(sum(x[j]*c[k] for j,c in enumerate(columns))==f[k//6] for k in range(12))
  assert all(sum(x[j]*c[k] for j,c in enumerate(seams))==0 for k in keys)
assert seen==set(flats) and statuses=={'unsat':10,'sat':14}
# Full native reflection with pp word preservation.
assert ''.join(words[1][j] for j in (2,1,0,5,4,3))==words[1]
R=PolynomialRing(QQ,['D','T','R']);D,T,P=R.gens()
for eq,family,reflected in [(P-60+D,'same',False),(P-60-D,'same',True),(P+T-180+D,'cross',False),(P+T-180-D,'cross',True)]:
 u,v,c,t=300-P-T,60+P,R(120),T
 if reflected:u,v,c,t=v,u,t,c
 native=[300-v,480-v-c,660-v-c-t]
 desired=([60+D+c,240+D,420+D-t] if family=='same' else [60+D+t,240+D+t-c,420+D-c])
 assert all(a-b in R.ideal(eq) for a,b in zip(native,desired))
# Analytic metric identities exactly, independent of any retained phase sample.
z=SR.var('z');a=1+cos(pi/3)+cos(4*pi/3-z);b=sin(pi/3)+sin(4*pi/3-z)
assert (a*a+b*b-4+2*sqrt(3)*cos(z-pi/6)).simplify_trig()==0
assert (sin(z-2*pi/3)*a+cos(z-2*pi/3)*b-sqrt(3)*(QQ(1)/2-cos(z))).simplify_trig()==0
print(f'PASS 130 subsets/31 affine flats; {total} native indexed stars; {ndual} rational dual inequalities; 10 negative strata/14 necessary primals; all endpoint cancellations; four reflected full direction transfers; exact native phase identities.')
