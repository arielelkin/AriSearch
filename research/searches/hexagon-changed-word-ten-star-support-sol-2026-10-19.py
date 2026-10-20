#!/usr/bin/env python3
"""Exact 1024-subset changed-word gate; rational angle consequences and orbit."""
import importlib.util,itertools,json,time,hashlib
from pathlib import Path
from sage.all import QQ,matrix
base=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',base/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
r=m.build((0,0,1,2,3,1));stars=[tuple(map(tuple,t)) for t in r['fixed_stars']];n=len(stars)
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
# Exhaust all 2^10 signed-star subsets, including asymmetrical handed supports.
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

assert n==10 and len(corona_groups)==1
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
 records.append(dict(mask=mask,star_indices=ids,angle_rank=mat.rank(),angle_rref=[[str(v) for v in row] for row in mat.echelon_form()],antiparallel_triple_implications=implications))
assert survivors==[298,303,586,591,874,879,922,927,954,959,986,991,1018,1023]
assert minimal==[298,586,922]
assert all(len({p[0]//6 for p in t})==1 for t in stars)
B=tuple(r['B'])
orbit={w[i:]+w[:i] for w in (B,B[::-1]) for i in range(6)}
atlas=json.loads((base/'research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json').read_text())
ten={tuple(row['B']) for row in atlas['rows'] if len(row['fixed_stars'])==10 and len(row['covered_corners'])==12}
assert ten==orbit and len(orbit)==12
for record in records:
 assert [0,0] in record['antiparallel_triple_implications']
out=dict(dihedral_orbit=sorted(orbit),all_ten_star_full_cover_rows_equal_dihedral_orbit=True,no_mixed_species_stars=True,schema='CHANGED_WORD_TEN_STAR_SUPPORT_V1',A=m.A,B=r['B'],domain_subsets=1<<n,stars=stars,coronas=r['boundary_coronas'],support_masks=survivors,minimal_supports=records,counts_by_corona=counts,scope='Exact necessary full-cover seam-closed corona-witness support subsets only; no metric feasibility or tilability assertion')
path=base/'research/certificates/hexagon-changed-word-ten-star-support-sol-2026-10-19.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
