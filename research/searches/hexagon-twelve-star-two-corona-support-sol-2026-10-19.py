#!/usr/bin/env python3
"""Exact 4096-subset two-corona gate and literal universal flat carrier."""
import importlib.util,itertools,json,time,hashlib
from pathlib import Path
from sage.all import QQ,matrix,vector
base=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',base/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
r=m.build((0,0,1,1,2,3));stars=[tuple(map(tuple,t)) for t in r['fixed_stars']];n=len(stars)
def sides(p):
 c,h=p;f,j=divmod(c,6);return (6*f+j,6*f+(j+1)%6) if h==1 else (6*f+(j+1)%6,6*f+j)
requirements=[[] for _ in stars]
for x in r['endpoint_microstates']:
 i=stars.index(tuple(map(tuple,x['star'])))
 requirements[i].append(sum(1<<stars.index(tuple(map(tuple,t))) for t in x['opposite_stars']))
cover=[sum(1<<i for i,t in enumerate(stars) if any(p[0]==c for p in t)) for c in range(12)]
factors=[{} for _ in range(5)]
for k,t in enumerate(stars):
 for i,p in enumerate(t):
  prev=t[(i-1)%3];nxt=t[(i+1)%3]
  if p[1]==1 and 0<=p[0]<=3:
   pair=((sides(prev)[1],prev[1]),(sides(nxt)[0],nxt[1]));a=p[0]+1
   factors[a][pair]=factors[a].get(pair,0)|(1<<k)
  if p==(4,1) and nxt==(5,1):
   q=t[(i+2)%3];pair=((sides(q)[1],q[1]),(sides(q)[0],q[1]));a=0
   factors[a][pair]=factors[a].get(pair,0)|(1<<k)
corona_groups=[[factors[j%5][(tuple(c[j]),tuple(c[j+1]))] for j in range(10)] for c in r['boundary_coronas']]
# Exhaust all 4096 signed-star subsets without symmetry reduction.
counts=[0]*len(corona_groups);survivors=[];digest=hashlib.sha256();start=time.monotonic()
for mask in range(1<<n):
 if not all(mask&g for g in cover):continue
 if any(mask&(1<<i) and any(not(mask&g) for g in requirements[i]) for i in range(n)):continue
 cs=[j for j,groups in enumerate(corona_groups) if all(mask&g for g in groups)]
 if not cs:continue
 survivors.append(mask);digest.update(mask.to_bytes(3,'little'))
 for j in cs:counts[j]+=1
# Inclusion-minimal necessary supports suffice for feasibility: extra stars only add equations.
minimal=[]
for mask in sorted(survivors,key=lambda x:(x.bit_count(),x)):
 if not any(t&mask==t for t in minimal):minimal.append(mask)

records=[]
for mask in minimal:
 rows=[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]
 ids=[i for i in range(n) if mask>>i&1]
 rows += [[sum(p[0]==i for p in stars[k]) for i in range(12)]+[2] for k in ids]
 mat=matrix(QQ,rows)
 implications=[]
 for f in range(2):
  for j in range(6):
   row=[int(i//6==f and (i%6-j)%6<3) for i in range(12)]+[2]
   if mat.stack(matrix(QQ,[row])).rank()==mat.rank():implications.append([f,j])
 witness=[]
 records.append(dict(mask=mask,star_indices=ids,angle_rank=mat.rank(),angle_rref=[[str(v) for v in row] for row in mat.echelon_form()],antiparallel_triple_implications=implications))

assert n==12 and len(corona_groups)==2
assert survivors==[1622,1879,2216,2473,2732,2989,3322,3579,3838,4095]
assert minimal==[2216,1622]
assert [0,0] in records[1]['antiparallel_triple_implications']
# Literal reviewed 33416 carrier transfers because changed B sides 1,3 self-pair.
W=(m.A,tuple(r['B'])); H=(1,1,-1,-1)
P=[(0,0,2,0),(1,0,3,0),(0,1,3,2),(1,1,2,2),
   (0,2,2,4),(1,2,3,4),(0,4,3,5),(1,4,2,5),
   (0,3,1,3),(0,5,1,5),(2,1,3,1),(2,3,3,3)]
assert sorted((f,i) for a in P for f,i in ((a[0],a[1]),(a[2],a[3])))==[(f,i) for f in range(4) for i in range(6)]
adj={i:[] for i in range(24)};dual={f:set() for f in range(4)}
for f,i,g,j in P:
 assert W[f//2][i]==W[g//2][j]
 dual[f].add(g);dual[g].add(f)
 ends=[(i,j),((i-1)%6,(j-1)%6)] if H[f]!=H[g] else [(i,(j-1)%6),((i-1)%6,j)]
 for a,b in ends:adj[6*f+a].append(6*g+b);adj[6*g+b].append(6*f+a)
assert all(len(v)==2 for v in adj.values())
left=set(adj);links=[]
while left:
 start=min(left);cycle=[];prev=None;cur=start
 while cur not in cycle:
  cycle.append(cur);nxt=next(v for v in adj[cur] if v!=prev);prev,cur=cur,nxt
 assert cur==start
 left.difference_update(cycle);links.append(cycle)
triples=[tuple(sorted(6*(x//12)+x%6 for x in c)) for c in links]
T={(0,6,7),(1,8,9),(2,3,10),(4,5,11)}
assert len(links)==8 and all(len(c)==3 for c in links)
assert set(triples)==T and all(triples.count(t)==2 for t in T)
assert {tuple(sorted(p[0] for p in stars[k])) for k in records[0]['star_indices']}==T
seen={0}
while True:
 nxt=seen|set().union(*(dual[f] for f in seen))
 if nxt==seen:break
 seen=nxt
assert len(seen)==4 and len(links)-len(P)+4==0
out=dict(schema='TWELVE_STAR_TWO_CORONA_SUPPORT_SOL_V1',A=m.A,B=r['B'],domain_subsets=1<<n,stars=stars,cover_masks=cover,seam_requirement_masks=requirements,corona_requirement_masks=corona_groups,coronas=r['boundary_coronas'],support_masks=survivors,minimal_supports=records,counts_by_corona=counts,carrier=dict(handedness=H,native_edge_pairs=P,native_corner_links=links,unsigned_triples=triples,connected=True,orientable=True,V=8,E=12,F=4,Euler=0),scope='Necessary supports and literal carrier only; actual closed strictly convex metrics required for geometric theorem')
path=base/'research/certificates/hexagon-twelve-star-two-corona-support-sol-2026-10-19.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(stars=n,coronas=len(corona_groups),survivors=len(survivors),minima=minimal,counts_by_corona=counts,carrier='PASS'),indent=2))
