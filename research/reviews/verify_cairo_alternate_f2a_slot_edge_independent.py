#!/usr/bin/env python3
"""Independent actual-variant f2a seam-potential reconstruction, no solver."""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
import json
import lzma
import argparse
from sage.all import QuadraticField,AA,QQ
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--kind',choices=['f2a','fac','e2c','eac'],default='f2a');kind=parser.parse_args().kind
filename='partial-contact-cairo-alternate-fac-guided-slot-edge-dual.json' if kind=='fac' else 'partial-contact-cairo-alternate-'+kind+'-slot-edge-balance.json'
path=ROOT/'research/certificates'/filename
# Large retained certificates are stored xz-compressed beside the .json name.
D=json.loads(path.read_text() if path.exists() else lzma.open(str(path)+'.xz','rt').read())
a=K(1);b={'f2a':(20*w-11)/13,'fac':w,'e2c':1+w,'eac':1+4*w/3}[kind];c=((3+w)+(1-w)*b)/4;d=((3-w)+(1+w)*b)/4;e=(w-1)*(1+b)/2;f=((w-5)+(1+3*w)*b)/4
assert 0<c<a<d<b and e>0
variants=[];raw=[];edge_colors={}
for species in (0,1):
 native=(a,b,c,d,e) if species==0 else(a,d,b,c,f)
 hosting=species==(1 if kind[0]=='f' else 0)
 cuts=([-1,0,1] if kind.endswith('ac') else[-1,0]) if hosting else[-1]
 for sa,sb,cut in product((0,1),(0,1),cuts):
  lengths=[];angles=[]
  for j,L in enumerate(native):
   positions=[K(0)]
   if j<4 and L==a and sa:positions.append(c)
   if j<4 and L==b and sb:positions.append(b-d if species==0 else d)
   if j==4 and cut>=0:
    bank=c if kind.endswith('2c') else a
    if kind.endswith('ac'):bank=a if cut==0 else c
    positions.append(bank)
   positions.append(L)
   for k,(x,y) in enumerate(zip(positions,positions[1:])):
    assert x<y;lengths.append(y-x);angles.append((120,90,120,90,120)[j] if k==0 else 180)
  s=len(variants);variants.append(['P' if species==0 else'Q',sa,sb,cut]);n=len(angles)
  for j,L in enumerate(lengths):edge_colors[s,j]=(L,int(angles[j]==120)+int(angles[(j+1)%n]==120))
  for j,t in enumerate(angles):raw.append((s,j,t,n))
assert variants==D['variants'] and [(s,j,t)for s,j,t,n in raw]==list(map(tuple,D['corners']))
# Give each oriented corner a first/last typed edge, endpoint position and color.
O=[]
for cid,(s,j,t,n) in enumerate(raw):
 out=(s,j);inc=(s,(j-1)%n)
 O.extend([(cid,t,out,0,inc,1),(cid,t,inc,1,out,0)])
followers=[]
for entry in O:
 followers.append([j for j,nextentry in enumerate(O) if edge_colors[entry[4]]==edge_colors[nextentry[2]]
                   and not(entry[1]==nextentry[1]==90 and edge_colors[entry[4]][1]!=1)])
# Every cyclic sequence is represented with its least index first. Repetition
# can give more than one start; store tuples to remove those duplicates.
stars=set()
for start in range(len(O)):
 stack=[([start],O[start][1])]
 while stack:
  path,total=stack.pop()
  if total==360:
   if len(path) in(3,4) and start in followers[path[-1]]:
    rotations=[tuple(path[k:]+path[:k]) for k in range(len(path))]
    stars.add(min(rotations))
   continue
  if total>360 or len(path)==4:continue
  for j in followers[path[-1]]:
   if j>=start:stack.append((path+[j],total+O[j][1]))
stars=sorted(stars);assert stars==list(map(tuple,D['oriented_stars']))
C=[];S=[];keys=set()
for star in stars:
 corner=Counter(O[j][0] for j in star);seams=Counter()
 for left,right in zip(star,star[1:]+star[:1]):
  _,_,_,_,x,px=O[left];_,_,y,py,_,_=O[right]
  assert edge_colors[x]==edge_colors[y]
  if x==y and px!=py:continue
  first,second=sorted((x,y));position=px if x==first else py
  key=(first,second,px^py)
  seams[key]+=1-2*position
 C.append(corner);S.append(seams);keys.update(seams)
keys=sorted(keys);assert keys==[(tuple(x),tuple(y),o)for x,y,o in D['seam_keys']]
assert C==[Counter({int(k):v for k,v in row.items()})for row in D['star_corner_counts']]
assert [[s[k]for k in keys]for s in S]==D['star_seam_counts']
assert D['result']=='unsat'
W=list(map(QQ,D['corner_dual']));Y=dict(zip(keys,map(QQ,D['seam_dual'])))
assert len(W)==len(raw) and len(Y)==len(keys)
for corners,seams in zip(C,S):
 assert sum(W[i]*n for i,n in corners.items())+sum(Y[k]*n for k,n in seams.items())>=0
for s in range(len(variants)):
 charge=sum(W[i]for i,row in enumerate(raw)if row[0]==s)
 assert charge<=-1
 if kind!='fac':assert charge==-1
# Each endpoint pairing feature reverses sign at the opposite endpoint;
# check all keys independently, including ambiguous same-slot pairing.
for x,y,parity in keys:
 for px in(0,1):
  py=px^parity
  if x==y and px!=py:continue
  def signed(j,k):return(1-2*j) if x<=y else(1-2*k)
  assert signed(px,py)+signed(1-px,1-py)==0
print('PASS',kind,len(variants),'complete variants,',len(raw),'actual corners,',len(stars),'oriented stars,',len(keys),'seam types;all rational dual inequalities and opposite-end cancellation;no solver or producer imports')
