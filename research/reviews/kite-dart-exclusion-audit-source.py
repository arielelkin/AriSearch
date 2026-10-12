#!/usr/bin/env python3
"""Independent labelled embedding census and source-sun legality witness."""
import importlib.util,itertools,json,time,collections
from pathlib import Path
from sage.all import matrix,ZZ
here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('audit',here/'kite-dart-exclusion-audit.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
K,w,phi=a.K,a.w,a.kp;start=time.monotonic()
def canonical(pieces):
 possibilities=[]
 for swap in (False,True):
  def label(x):return ('Q' if x=='P' else 'P' if x=='Q' else x) if swap else x
  faces=[]
  for face in pieces:
   seq=[label(str(v)) for v in face];faces.append(min(tuple(seq[i:]+seq[:i]) for i in range(len(seq))))
  possibilities.append(tuple(sorted(faces)))
 return min(possibilities)
expected={canonical([[x for x,y in f] for f in t['pieces']]) for t in a.T};assert len(expected)==98
possible=[('P',str(j)) for j in range(4)]+[('Q',str(j)) for j in range(4)]+[('P','Q'),('0','2'),('1','3')]
found=set();rotation_systems=0
for mask in range(1<<11):
 interior=[e for i,e in enumerate(possible) if mask>>i&1]
 if ('0','2') in interior and ('1','3') in interior:continue
 nb={str(j):[] for j in range(4)}
 for x,y in interior:nb.setdefault(x,[]).append(y);nb.setdefault(y,[]).append(x)
 if 'Q' in nb and 'P' not in nb:continue
 if any(len(nb[v])<3 for v in ('P','Q') if v in nb):continue
 nodes=list(nb);choices=[]
 for v in nodes:
  if v in '0123':choices.append([((str((int(v)+1)%4),)+p+(str((int(v)-1)%4),)) for p in itertools.permutations(nb[v])])
  else:
   first=min(nb[v]);rest=[x for x in nb[v] if x!=first];choices.append([(first,)+p for p in itertools.permutations(rest)])
 for orders in itertools.product(*choices):
  rot=dict(zip(nodes,orders));successor={}
  for v,neighbors in rot.items():
   for i,u in enumerate(neighbors):successor[u,v]=(v,neighbors[i-1])
  unseen=set(successor);cycles=[]
  while unseen:
   edge=min(unseen);first=edge;cyc=[]
   while edge in unseen:unseen.remove(edge);cyc.append(edge);edge=successor[edge]
   assert edge==first;cycles.append(cyc)
  if len(nodes)-(len(interior)+4)+len(cycles)!=2:continue
  outside=next(f for f in cycles if ('1','0') in f)
  if len(outside)!=4:continue
  pieces=[[u for u,v in f] for f in cycles if f!=outside]
  if any(len(set(f))!=len(f) for f in pieces):continue
  rotation_systems+=1;found.add(canonical(pieces))
assert found==expected
print(json.dumps({'independent_embedding_count':len(found),'accepted_rotation_systems':rotation_systems}),flush=True)
# Direct two-halfstep subdivision, without importing source builder.
def area(tri):
 return sum(a.cross(tri[i],tri[(i+1)%3]) for i in range(3))
def halfstep(tris):
 out=[]
 for t,x,y,z in tris:
  if t=='a1':
   p=x/phi+y/phi**2;children=[('a2',p,z,x),('o2',z,p,y)]
  elif t=='o1':children=[('o2',x,y,z)]
  elif t=='a2':children=[('a1',x,y,z)]
  else:
   p=x/phi**2+z/phi;children=[('a1',y,x,p),('o1',z,p,y)]
  # Verify every child is geometrically contained in its parent triangle;
  # exact area equality plus containment excludes an overlap or a gap.
  sg=a.sign(area([x,y,z]));parent=[x,y,z]
  for _,xx,yy,zz in children:
   for v in (xx,yy,zz):assert all(sg*a.sign(a.cross(parent[(i+1)%3]-parent[i],v-parent[i]))>=0 for i in range(3))
  assert sum(positive(area([xx,yy,zz])) for _,xx,yy,zz in children)==positive(area(parent))
  out.extend(children)
 return out
# Exact positive normalization in the specified real embedding.
def positive(q):return q if a.sign(q)>=0 else -q
proto=('a1',K(1),K(0),w);tris=[proto];sun=None
for n in range(1,5):
 tris=halfstep(halfstep(tris));paired=collections.defaultdict(list)
 for tri in tris:t,x,y,z=tri;paired[t,frozenset((x,y))].append(tri)
 stars=collections.defaultdict(list)
 for (t,axis),ts in paired.items():
  if len(ts)!=2:continue
  _,x,y,z=ts[0];_,xx,yy,zz=ts[1];assert x==xx and y==yy
  assert zz==x+(y-x)/(y-x).conjugate()*(z-x).conjugate()
  origin=y if t=='a1' else x;end=x if t=='a1' else y
  cyc=[origin,z,end,zz]
  if a.sign(sum(a.cross(cyc[i],cyc[(i+1)%4]) for i in range(4)))<0:cyc=[origin,zz,end,z]
  for j,v in enumerate(cyc):stars[v].append((t,j,ts,cyc))
 for center,inc in stars.items():
  if len(inc)==5 and all(t=='a1' and j==0 for t,j,ts,cyc in inc):sun=(n,center,inc);break
 if sun:break
assert sun and sun[0]==4
n,center,inc=sun;ten=[tri for t,j,ts,cyc in inc for tri in ts]
u=ten[0][1]-center
assert u*phi**n in {w**j for j in range(10)}
expected_sun={('a1',center+u*w**(2*j),center,center+u*w**(2*j+epsilon)) for j in range(5) for epsilon in (1,-1)}
assert set(ten)==expected_sun
# Every normalized sun triangle lies in this one a1 supertile, so continuing
# the identical local substitution six more halfsteps embeds the recorded
# patch3 (after its boundary-half removal), up to one direct similarity.
# Check strict containment of all sun vertices, strengthening legal occurrence.
parent=[proto[1],proto[2],proto[3]];sg=a.sign(area(parent));strict=True
for tri in ten:
 for v in tri[1:]:
  strict &= all(sg*a.sign(a.cross(parent[(i+1)%3]-parent[i],v-parent[i]))>0 for i in range(3))
# Two-step type/chirality count: a1 -> a1 same + a1 opposite + o1 same;
# o1 -> a1 opposite + o1 same. This 4-state matrix is primitive.
o=next(t for t in halfstep(halfstep([proto])) if t[0]=='o1')
M=matrix(ZZ,4,4)
for ti,t in enumerate((proto,o)):
 for si,sgn in enumerate((1,-1)):
  parent=t if sgn==1 else tuple([t[0]]+[q.conjugate() for q in t[1:]])
  ps=a.sign(area(parent[1:]));base=2*ti+si
  for kind,x,y,z in halfstep(halfstep([parent])):
   cs=a.sign(area([x,y,z]));childtype=0 if kind=='a1' else 1
   # Sign is absolute relative to the chosen unreflected prototype sign.
   refsign=a.sign(area((proto if childtype==0 else o)[1:]));ci=0 if cs==refsign else 1
   M[2*childtype+ci,base]+=1
primitive_power=next(k for k in range(1,20) if all(c>0 for c in (M**k).list()))
result={'independent_embedding_count':len(found),'accepted_rotation_systems':rotation_systems,
 'sun_legal_in_single_a1_supertile':True,'sun_deflations':n,'sun_center':[str(x) for x in center.vector()],
 'sun_axis_vector':[str(x) for x in u.vector()],'sun_strictly_interior':bool(strict),'sun_triangles':[[t]+[[str(c) for c in v.vector()] for v in (x,y,z)] for t,x,y,z in ten],
 'type_and_chirality_substitution_matrix':[list(map(int,row)) for row in M.rows()],'primitive_power':primitive_power,
 'source_occurrence_scope':'The primitive marked alternating Lang-Hayes half-tile substitution hull, allowing source isometries. Single-half sun legality embeds patch3 after three further deflations. Excludes no arbitrary unmarked kite/dart tiling claim.',
 'elapsed_seconds':round(time.monotonic()-start,3)}
(a.C/'kite-dart-exclusion-audit-source.json').write_text(json.dumps(result,indent=1)+'\n');print(json.dumps(result),flush=True)
