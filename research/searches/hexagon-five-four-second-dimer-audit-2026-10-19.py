"""Exact second candidate audit. Domain: all AA full-side dimers at every A side,
all equal-length partner sides and both chiralities; endpoint fans contain
at most four tiles because every interior angle >=90. No partial contacts.
"""
from sage.all import QuadraticField,vector,matrix
import json
from pathlib import Path
K=QuadraticField(3,'r');r=K.gen();V=lambda x:vector(K,x)
L=[K(1),4-2*r,-4+3*r,2-r,-6+4*r]
W=[(0,1,2,0,3,4),(0,1,1,0,2,3)]
G=[(90,150,90,120,150,120),(150,120,120,90,150,90)]
R={30:(r/2,K(1)/2),60:(K(1)/2,r/2),90:(K(0),K(1))}
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
P=[]
for w,g in zip(W,G):
 p=V([0,0]);d=V([1,0]);vs=[]
 for i in range(6):
  vs.append(p);p+=L[w[i]]*d;c,s=R[180-g[i]];d=V([c*d[0]-s*d[1],s*d[0]+c*d[1]])
 assert p==V([0,0])
 assert all(cross(vs[(i+1)%6]-vs[i],vs[j]-vs[i])>0 for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
 P.append(vs)
assert min(L)>0 and len(set(L))==5
# Full Reinhardt systems in end-of-side indexing, all dihedral labels.
hits=[]
for f in range(2):
 for k in range(6):
  for rev in (False,True):
   # ordered native sides: reversal side k maps to old k; its end corner old k-1.
   ss=[(k+(-i if rev else i))%6 for i in range(6)]
   a=[G[f][(j-1)%6 if rev else j] for j in ss];l=[L[W[f][j]] for j in ss]
   if a[5]+a[0]+a[1]==360 and l[2]==l[5]:hits.append((f,k,rev,'H1'))
   if a[5]+a[0]+a[2]==360 and l[1]==l[3] and l[2]==l[5]:hits.append((f,k,rev,'H2'))
   if a[5]==a[1]==a[3]==120 and l[0]==l[1] and l[2]==l[3] and l[4]==l[5]:hits.append((f,k,rev,'H3'))
assert not hits
# Represent polygons CCW also after reflection (reverse vertex ordering).
def attach(q,j,a,b,flip):
 if flip:a,b=b,a
 q=[V([x[0],-x[1]]) for x in q] if flip else q
 u,v=q[j],q[(j+1)%6];e=v-u;t=b-a
 c=e.dot_product(t)/e.dot_product(e);s=cross(e,t)/e.dot_product(e)
 out=[a+V([c*(x-u)[0]-s*(x-u)[1],s*(x-u)[0]+c*(x-u)[1]]) for x in q]
 return list(reversed(out)) if flip else out

def overlap(p,q):
 # strict separating axis theorem: touching allowed
 return not any(max(cross(b-a,x-a) for x in q)<=0 for a,b in zip(p,p[1:]+p[:1])) and not any(max(cross(b-a,x-a) for x in p)<=0 for a,b in zip(q,q[1:]+q[:1]))
def candidates(a,b):
 ll=(b-a).dot_product(b-a)
 for f,q in enumerate(P):
  for j in range(6):
   if (q[(j+1)%6]-q[j]).dot_product(q[(j+1)%6]-q[j])==ll:
    for flip in (False,True):yield f,attach(q,j,b,a,flip)
def key(p):return tuple(sorted(tuple(x) for x in p))
def complete(tiles,point,seen):
 # fill a full-side fan about point; at most 4 incident convex corners.
 boundary=[]
 for _,p in tiles:
  for a,b in zip(p,p[1:]+p[:1]):
   if a!=point and b!=point:continue
   if not any(any(a==d and b==c for c,d in zip(q,q[1:]+q[:1])) for _,q in tiles):boundary.append((a,b))
 if not boundary:return [tiles]
 if sum(point in p for _,p in tiles)>=4:return []
 a,b=boundary[0];out=[]
 for f,q in candidates(a,b):
  kk=key(q)
  if kk in seen or point not in q or any(overlap(p,q) for _,p in tiles):continue
  out+=complete(tiles+[(f,q)],point,seen|{kk})
 return out
def carrier(ts):
 # Finite domain: candidate periods are translation differences between
 # identically oriented same-type tiles in each completed dimer corona.
 diffs=set()
 def shift(p,q):
  for b in q:
   t=b-p[0]
   if key([x+t for x in p])==key(q):return t
  return None
 for f,p in ts:
  for g,q in ts:
   if f==g:
    t=shift(p,q)
    if t is not None and t!=V([0,0]):diffs.add(tuple(t))
 ds=[V(x) for x in diffs]
 for h in ds:
  for t in ds:
   M=matrix(K,[h,t]).transpose()
   if M.det()<=0:continue
   Mi=M.inverse();reps=[]
   def integral(v):return all(x.denominator()==1 for x in v)
   for f,p in ts:
    if not any(f==g and (d:=shift(q,p)) is not None and integral(Mi*d) for g,q in reps):reps.append((f,p))
   area=sum(sum(cross(p[i],p[(i+1)%6]) for i in range(6))/2 for _,p in reps)
   if area!=M.det():continue
   if all(sum(1 for _,q in reps for j in range(6) if b-a==q[j]-q[(j+1)%6] and integral(Mi*(a-q[(j+1)%6])))==1 for _,p in reps for a,b in zip(p,p[1:]+p[:1])):
    return dict(periods=[[str(x) for x in h],[str(x) for x in t]],representatives=[dict(type=f,vertices=[[str(x) for x in v] for v in p]) for f,p in reps])
 return None
results=[]
for i,j in ((i,j) for i in range(6) for j in range(6) if W[0][i]==W[0][j]):
 for flip in (False,True):
  q=attach(P[0],j,P[0][(i+1)%6],P[0][i],flip)
  assert not overlap(P[0],q)
  seed=[(0,P[0]),(0,q)];fans=complete(seed,P[0][i],{key(p) for _,p in seed})
  done=[]
  for ts in fans:done+=complete(ts,P[0][(i+1)%6],{key(p) for _,p in ts})
  front=done;counts=[];cap=False
  for point in list(dict.fromkeys(tuple(x) for _,p in seed for x in p)):
   nxt=[]
   for ts in front:
    nxt+=complete(ts,V(point),{key(p) for _,p in ts})
    if len(nxt)>1000:cap=True;break
   front=nxt;counts.append(len(front))
   if cap or not front:break
  witnesses=[w for ts in front if (w:=carrier(ts)) is not None]
  results.append(dict(periodic_witnesses=witnesses,root_side=i,partner_side=j,reflected=flip,first_endpoint_fans=len(fans),both_endpoint_completions=len(done),dimer_vertex_corona_frontiers=counts,corona_cap_reached=cap))
out=dict(lengths=[str(x) for x in L],vertices=[[[str(x) for x in v] for v in p] for p in P],reinhardt_hits=hits,AA_all_fullside_dimer_fans=results)
Path('research/certificates/hexagon-five-four-second-dimer-audit-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
