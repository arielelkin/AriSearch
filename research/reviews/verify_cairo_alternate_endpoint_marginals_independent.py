#!/usr/bin/env python3
"""Rebuild augmented Cairo pieces/stars; verify retained rational primal/duals.
No producer imports or solver calls. Native cuts are rebuilt from coordinates.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
import json
from sage.all import QuadraticField, AA, QQ
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
ROOT=Path(__file__).resolve().parents[2]
ratios={'f2c':(28*w+13)/37,'fac':w,'f2a':(20*w-11)/13,'e2c':1+w,'eac':1+4*w/3,'e2a':1+2*w}
affine=[(K(1),K(0)),(K(0),K(1)),((3+w)/4,(1-w)/4),((3-w)/4,(1+w)/4),((w-1)/2,(w-1)/2),((w-5)/4,(1+3*w)/4)]
lo=(5-w)/(1+3*w);hi=3+2*w
add=lambda u,v:tuple(x+y for x,y in zip(u,v))
sums=[add(affine[i],affine[i]) for i in range(4)]+[add(affine[0],affine[2]),add(affine[1],affine[3])]
for u,v in combinations(sums,2):
 assert u[1]!=v[1] and (v[0]-u[0])/(u[1]-v[1])==1
hits=[]
for u in affine[4:]:
 for v in sums:
  assert u[1]!=v[1]
  k=(v[0]-u[0])/(u[1]-v[1])
  if lo<k<hi and k!=1:hits.append(k)
assert len(hits)==6 and set(hits)==set(ratios.values())

def circuit(edges):
 # Directly place unoriented corner edges around the circular star.
 first,*rest=edges
 def extend(at,remaining,target):
  if not remaining:return at==target
  for i,(x,y) in enumerate(remaining):
   tail=remaining[:i]+remaining[i+1:]
   if x==at and extend(y,tail,target):return True
   if y==at and extend(x,tail,target):return True
  return False
 return extend(first[1],rest,first[0])

def reconstruct(kind):
 k=ratios[kind];a,b,c,d,e,f=[u+v*k for u,v in affine]
 assert 0<c<a<d<b and e>0 and f>0 and e!=f
 words=[(a,b,c,d,e),(a,d,b,c,f)]
 variant_ids=[];corner_lists=[]
 for species,word in enumerate(words):
  A,B,C,D,E=word
  assert E==w*C+D-2*A and B-C==w*(D-A)
  vertices=[(K(0),K(0)),(A,K(0)),(A,B),(A-w*C/2,B+C/2),(-E/2,w*E/2)]
  for i in range(5):
   vx,vy=vertices[i];xx,yy=vertices[(i+1)%5];dx,dy=xx-vx,yy-vy
   assert dx*dx+dy*dy==word[i]**2
   for j,(x,y) in enumerate(vertices):
    if j not in (i,(i+1)%5):assert dx*(y-vy)-dy*(x-vx)>0
  host=species==(1 if kind[0]=='f' else 0)
  options=[-1,0,1] if host and kind.endswith('ac') else ([-1,0] if host else [-1])
  for sa,sb,cut in product((0,1),(0,1),options):
   pieces=[];angles=[]
   for edge,length in enumerate(word):
    # Starts of the directed native edges are120,90,120,90,120.
    positions=[K(0)]
    if length==a and edge<4 and sa:positions.append(c)
    if length==b and edge<4 and sb:positions.append(b-d if species==0 else d)
    if edge==4 and cut>=0:
     bank=c if kind.endswith('2c') else a
     if kind.endswith('ac'):bank=a if cut==0 else c
     positions.append(bank)
    positions.append(length)
    assert all(x<y for x,y in zip(positions,positions[1:]))
    for j,(x,y) in enumerate(zip(positions,positions[1:])):
     pieces.append(y-x);angles.append((120,90,120,90,120)[edge] if j==0 else 180)
   corners=[]
   for j,theta in enumerate(angles):
    incoming=(pieces[j-1],int(angles[j-1]==120)+int(theta==120))
    outgoing=(pieces[j],int(theta==120)+int(angles[(j+1)%len(angles)]==120))
    corners.append((theta,)+tuple(sorted([incoming,outgoing])))
   variant_ids.append(['P' if species==0 else 'Q',sa,sb,cut]);corner_lists.append(corners)
 kinds=sorted(set(x for row in corner_lists for x in row));ids={x:i for i,x in enumerate(kinds)}
 tiles=[Counter(ids[x] for x in row) for row in corner_lists]
 stars=[]
 for n in (3,4):
  for star in combinations_with_replacement(range(len(kinds)),n):
   selected=[kinds[i] for i in star]
   if sum(x[0] for x in selected)==360 and circuit([x[1:] for x in selected]):stars.append(list(star))
 return variant_ids,kinds,tiles,stars

for name in ratios:
 data=json.loads((ROOT/'research/certificates'/('partial-contact-cairo-alternate-'+name+'-endpoint-marginals.json')).read_text())
 vs,ks,ts,ss=reconstruct(name)
 assert vs==data['variants']
 parse=lambda z:sum(K(QQ(t))*w**i for i,t in enumerate(z))
 stored=[(t,(parse(x[0]),x[1]),(parse(y[0]),y[1])) for t,x,y in data['corner_kinds']]
 assert ks==stored and ss==data['stars']
 assert ts==[Counter({int(k):v for k,v in row.items()}) for row in data['type_counts']]
 if name in ('f2c','e2a'):
  assert data['result']=='unsat'
  weights=list(map(QQ,data['dual']));assert len(weights)==len(ks)
  assert all(sum(weights[i] for i in s)>=0 for s in ss)
  assert all(sum(weights[i]*v for i,v in t.items())<=-1 for t in ts)
 else:
  assert data['result']=='sat'
  F=list(map(QQ,data['type_frequencies']));X=list(map(QQ,data['star_frequencies']))
  assert len(F)==len(ts) and len(X)==len(ss) and sum(F)==1 and all(z>=0 for z in F+X)
  for i in range(len(ks)):
   assert sum(t[i]*f for t,f in zip(ts,F))==sum(s.count(i)*x for s,x in zip(ss,X))
 print('PASS',name,len(vs),'whole/hosted variants;',len(ks),'corner kinds;',len(ss),'cyclic stars;',data['result'],'exact certificate')
print('PASS independent six-ratio domain,12 convex polygons,all augmented variants and rational certificates; no solver/producer imports')
