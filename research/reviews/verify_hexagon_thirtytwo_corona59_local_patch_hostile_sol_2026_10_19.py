#!/usr/bin/env python3
"""Independent certificate audit; does not import the builder or producer."""
import json,itertools
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
d=json.loads((root/'research/certificates/hexagon-thirtytwo-corona59-base-patch-sol-2026-10-19.json').read_text())
faces=d['faces']; assert len(faces)==10
V=[0,2,s.Rational(5,2)+s.I*s.sqrt(3)/2,2+s.I*s.sqrt(3),s.I*s.sqrt(3),-s.Rational(1,2)+s.I*s.sqrt(3)/2]
clean=s.simplify
cross=lambda a,b: clean(s.im(s.conjugate(a)*b))
words=((0,1,2,0,3,4),(0,1,2,0,3,1))
verts={};edges={};F={}
for f in faces:
 name=f['name'];v=list(map(s.sympify,f['vertices']));F[name]=v
 native=V if f['hand']==1 else [s.conjugate(z) for z in V]
 rot=clean((v[1]-v[0])/(native[1]-native[0]));assert clean(rot*s.conjugate(rot))==1
 assert all(clean(v[j]-v[0]-rot*(native[j]-native[0]))==0 for j in range(6))
 for j,a in enumerate(v):
  assert f['hand']*cross(v[(j+1)%6]-a,v[(j+2)%6]-v[(j+1)%6])>0
  verts.setdefault(a,[]).append((name,6*f['polygon']+(j-1)%6))
  edges.setdefault(frozenset((a,v[(j+1)%6])),[]).append((name,j))
# Independently develop all ten boundary placements, including both duplicate seams.
assert [tuple(x) for x in d['corona'][1:]]==[(9,1),(1,1),(8,1),(6,-1),(10,1)]*2
developed=[]
for k,(side,h) in enumerate(d['corona'][1:]):
 central=F['Q'] if k<5 else F['P']; j=k%5; ss=side%6
 native=V if h==1 else [s.conjugate(z) for z in V]
 a,b=central[j],central[(j+1)%6]
 aa,bb=(b,a) if h==1 else (a,b)
 rot=clean((bb-aa)/(native[(ss+1)%6]-native[ss]))
 vv=[clean(aa+rot*(z-native[ss])) for z in native]
 developed.append(vv)
 if str(k) in F:assert vv==F[str(k)]
assert developed[0]==developed[9] and developed[4]==developed[5]
byname={f['name']:f for f in faces}
shared=[e for e in edges.values() if len(e)==2]
assert len(verts)==32 and len(edges)==41 and len(shared)==19
assert all(len(e)<=2 for e in edges.values())
for e in shared:
 assert len({words[byname[n]['polygon']][j] for n,j in e})==1
 recorded={frozenset(map(tuple,e['incidence'])) for e in d['edge_incidence'] if len(e['incidence'])==2}
 assert frozenset(e) in recorded
support={tuple(sorted(x)) for x in ((0,1,8),(2,7,11),(3,6,10),(4,5,9))}
triples=[inc for inc in verts.values() if len(inc)==3]
assert len(triples)==10 and all(tuple(sorted(c for n,c in inc)) in support for inc in triples)
assert max(map(len,verts.values()))==3
adj=apart=0
for a,b in itertools.combinations(faces,2):
 av,bv=F[a['name']],F[b['name']]; common=set(av)&set(bv)
 axes=[]
 for f,g in ((a,b),(b,a)):
  fv,gv=F[f['name']],F[g['name']]
  for j,z in enumerate(fv):
   vals=[f['hand']*cross(fv[(j+1)%6]-z,w-z) for w in gv]
   if max(vals)<=0:axes.append(max(vals))
 assert axes and len(common) in (0,2)
 if common:
  assert any(set(e)==common for e in edges if len(edges[e])==2)
  adj+=1
 else:
  assert min(axes)<0;apart+=1
assert (adj,apart)==(19,26)
assert sum(all(n in ('P','Q') for n,j in e) for e in shared)==1
assert sum(sum(n in ('P','Q') for n,j in e)==1 for e in shared)==10
assert sum(all(n not in ('P','Q') for n,j in e) for e in shared)==8
# All outer faces attach directly to the central dimer.
assert {n for e in shared for n,j in e if n not in ('P','Q') and any(m in ('P','Q') for m,k in e)}==set(F)-{'P','Q'}
print('PASS: 10 rigid convex faces, 19 color-matched full edges, 10 supported end-corner stars, 26 strict separations; 1+10+8 edge decomposition.')
