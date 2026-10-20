#!/usr/bin/env python3
"""Finite exact whole-kite repartition gate; integer coordinates (x,y/sqrt3)*4."""
import importlib.util,itertools,json,sys
from pathlib import Path
s=importlib.util.spec_from_file_location('hat',Path(__file__).with_name('source-decoration-hat-patch.py'))
h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(p):return sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p)))
def hull(points):
 p=sorted(set(points));lo=[];hi=[]
 for chain,seq in ((lo,p),(hi,p[::-1])):
  for v in seq:
   while len(chain)>1 and cross(chain[-2],chain[-1],v)<=0:chain.pop()
   chain.append(v)
 return lo[:-1]+hi[:-1]
def canon(p):
 n=len(p)
 def d(a,b):return (a[0]-b[0])**2+3*(a[1]-b[1])**2
 return min(tuple(d(p[(s+z*i)%n],p[(s+z*j)%n]) for i in range(n) for j in range(i+1,n)) for s in range(n) for z in (1,-1))
def enc(p):
 x,y=p;assert x.b==0 and y.a==0
 a=x.a*4;b=y.b*4;assert a.denominator==b.denominator==1
 return int(a),int(b)
def edges(p):return [tuple(sorted((p[i],p[(i+1)%len(p)]))) for i in range(len(p))]
def covers(n,rows,allowed):
 by=[[] for _ in range(n)]
 for row in rows:
  if row['class'] in allowed:
   for i in row['cells']:by[i].append(row)
 def rec(rem,out,crossed):
  if not rem:return out if crossed else None
  i=min((i for i in range(n) if rem>>i&1),key=lambda i:sum(r['mask']&rem==r['mask'] for r in by[i]))
  for r in by[i]:
   if r['mask']&rem==r['mask']:
    got=rec(rem^r['mask'],out+[r['mask']],crossed or r['cross_hat'])
    if got:return got
  return None
 return rec((1<<n)-1,[],False)
RK=h.ref_kites();data={};keys={}
for name,meta in zip('HTPF',h.init()):
 out=[];h.expand(meta,h.IDENT,out);cells=[];owners=[]
 for owner,(_,t) in enumerate(out):
  for kite in RK:
   p=[enc(h.transPt(t,v)) for v in kite]
   if area(p)<0:p=p[::-1]
   cells.append(p);owners.append(owner)
 assert len({tuple(sorted(p)) for p in cells})==len(cells)
 adj=[set() for _ in cells];es=[set(edges(p)) for p in cells]
 for i,j in itertools.combinations(range(len(cells)),2):
  if es[i]&es[j]:adj[i].add(j);adj[j].add(i)
 front={1<<i for i in range(len(cells))};counts=[];rows=[]
 for size in range(1,9):
  counts.append(len(front));nxt=set()
  for mask in front:
   ids=[i for i in range(len(cells)) if mask>>i&1]
   p=hull([v for i in ids for v in cells[i]])
   if len(p) in (5,6) and area(p)==sum(area(cells[i]) for i in ids):
    k=canon(p)
    if k not in keys:keys[k]=len(keys)
    rows.append(dict(mask=mask,cells=ids,polygon=p,**{'class':keys[k]},cross_hat=len({owners[i] for i in ids})>1))
   if size<8:
    for j in set().union(*(adj[i] for i in ids)):
     if not mask>>j&1:nxt.add(mask|1<<j)
  front=nxt
 print(name,counts,len(rows),flush=True)
 data[name]=dict(cells=cells,owners=owners,connected_counts=counts,eligible=rows,proxy_outline=[enc(v) for v in meta.shape])
classes=sorted(keys.values());common=set.intersection(*(set(r['class'] for r in d['eligible']) for d in data.values()))
# Allow each region to use either/both classes; require both globally and a crossed boundary globally.
# First enumerate all covers without crossing demand, then test the four-region product.
def allcovers(n,rows,allowed):
 by=[[] for _ in range(n)]
 for r in rows:
  if r['class'] in allowed:
   for i in r['cells']:by[i].append(r)
 def rec(rem,out):
  if not rem:yield out;return
  i=(rem&-rem).bit_length()-1
  for r in by[i]:
   if r['mask']&rem==r['mask']:yield from rec(rem^r['mask'],out+[r])
 return list(rec((1<<n)-1,[]))
witnesses=[];pair_results=[]
# Candidate pairs from all global classes, since a class need not occur in every region.
for pair in itertools.combinations(classes,2):
 cs=[allcovers(len(d['cells']),d['eligible'],pair) for d in data.values()]
 if all(cs):
  count=0
  for combo in itertools.product(*cs):
   used={r['class'] for cover in combo for r in cover}
   if used==set(pair) and any(r['cross_hat'] for cover in combo for r in cover):
    witnesses.append(dict(pair=pair,covers={name:[r['mask'] for r in cover] for name,cover in zip(data,combo)}));count+=1
  pair_results.append(dict(pair=pair,cover_counts=list(map(len,cs)),admissible=count))
result=dict(scope='Connected unions of 1..8 full kites within assigned hat unions of initial H/T/P/F, exact 5/6-corner convex hull equality; all pairs of global congruence classes including reflection; both classes globally and cross-hat piece required.',coordinate_map='physical=(X/4,sqrt(3)*Y/4)',regions=data,classes=[dict(id=v,distance_key=k) for k,v in keys.items()],pairs_with_covers=pair_results,witnesses=witnesses)
Path(sys.argv[1]).write_text(json.dumps(result,indent=2)+'\n')
print('classes',len(classes),'pairs_with_covers',pair_results,'witnesses',len(witnesses))
