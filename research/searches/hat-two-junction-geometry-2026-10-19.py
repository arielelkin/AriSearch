"""Exact real feasibility for corrected 32 incidence signatures; finite scoped gate."""
import itertools,json
from pathlib import Path
import z3
Q=z3.RealVal
source=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text())['hat_outline']
assert all(p[0][1]=='0' and p[1][0]=='0' for p in source)
V=[(Q(p[0][0]),Q(p[1][1])) for p in source]
x,y,u,v=z3.Reals('x y u v');X=(x,y);Y=(u,v)
polys=[V[:5]+[X],V[4:9]+[Y,X],V[8:12]+[Y],V[11:]+[V[0],X,Y]]
# Label vertices whose turn may be flat: boundary leaves and junctions.
labels=[['b0',None,None,None,'b1','j0'],['b1',None,None,None,'b2','j1','j0'],['b2',None,None,'b3','j1'],['b3',None,'b0','j0','j1']]
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
rows=[]
for jf in itertools.product([None,0,1,3],[None,1,2,3]):
 for bf in itertools.product(*[[None,(i-1)%4,i] for i in range(4)]):
  sides=[n-sum(f==i for f in jf+bf) for i,n in enumerate([6,7,5,5])]
  if not all(s in (5,6) for s in sides):continue
  flats={f'j{i}':f for i,f in enumerate(jf)}|{f'b{i}':f for i,f in enumerate(bf)}
  s=z3.SolverFor('QF_NRA')
  for k,(poly,labs) in enumerate(zip(polys,labels)):
   for i,(b,lab) in enumerate(zip(poly,labs)):
    a=poly[i-1];c=poly[(i+1)%len(poly)];turn=cross(a,b,c)
    s.add(turn==0 if lab and flats[lab]==k else turn>0)
    # Full supporting halfplanes also rule out self-crossing polygons.
    for p in poly:s.add(cross(b,c,p)>=0)
   for a,b in zip(poly,poly[1:]+poly[:1]):s.add((a[0]-b[0])**2+(a[1]-b[1])**2>0)
  s.add((x-u)**2+(y-v)**2>0)
  r=s.check();row=dict(junction_flats=jf,boundary_flats=bf,sides=sides,status=str(r))
  if r==z3.sat:
   m=s.model();row['junctions_scaled']=[str(m.eval(t)) for t in [x,y,u,v]]
  if r==z3.sat:
   reduced=[[pt for pt,lab in zip(poly,labs) if not(lab and flats[lab]==k)] for k,(poly,labs) in enumerate(zip(polys,labels))]
   def dist(a,b):return (a[0]-b[0])**2+3*(a[1]-b[1])**2
   def cong(a,b):
    if len(a)!=len(b):return z3.BoolVal(False)
    n=len(a)
    return z3.Or(*[z3.And(*[dist(a[i],a[j])==dist(b[(h+eps*i)%n],b[(h+eps*j)%n]) for i in range(n) for j in range(i)]) for h in range(n) for eps in [-1,1]])
   eq={(i,j):cong(reduced[i],reduced[j]) for i in range(4) for j in range(i+1,4)}
   partitions=[]
   for mask in range(1,8):
    groups=[[0]+[i for i in range(1,4) if mask&(1<<(i-1))],[i for i in range(1,4) if not mask&(1<<(i-1))]]
    if not groups[1]:continue
    partitions.append(z3.And(*[eq[i,j] for i in range(4) for j in range(i+1,4) if any(i in g and j in g for g in groups)]))
   # Include split {0} | {1,2,3} (mask zero).
   partitions.append(z3.And(eq[1,2],eq[1,3],eq[2,3]))
   s.add(z3.Or(*partitions));r2=s.check();row['at_most_two_classes']=str(r2)
   if r2==z3.sat:row['two_class_junctions_scaled']=[str(s.model().eval(t)) for t in [x,y,u,v]]
  rows.append(row)
assert len(rows)==32
assert all(row['status'] in ('sat','unsat') for row in rows)
assert sum(row['status']=='sat' for row in rows)==11
assert all(row.get('at_most_two_classes')=='unsat' for row in rows if row['status']=='sat')
out=dict(z3_version=z3.get_version_string(),solver='QF_NRA; no timeout; no random seed or symmetry reduction',status='COMPLETE',scope='Corrected 32 signatures, exact polynomial convex-sector feasibility; y coordinates scaled by sqrt(3).',records=rows)
Path('research/certificates/hat-two-junction-geometry-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
