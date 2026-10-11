"""Independent fixed-native geometry audit of the retained mixed Cairo quotient.
No author module or solver import; polynomial identities cover the full cone.
"""
from sage.all import *
from pathlib import Path
import json
import sys
complementary="--complementary" in sys.argv

K=QuadraticField(3,'w'); w=K.gen()
R=PolynomialRing(K,names=('x','y','z')); a,b,c=R.gens()
d=a+(b-c)/w; e=w*c+d-2*a
A=a; B=3*w*a-2*c; C=b; D=3*a-e; E=2*d
P=(a,b,c,d,e); Q=(A,B,C,D,E)
assert B-C==w*(D-A) and E==w*C+D-2*A
assert B-b==w*(D-a)==w*(2*a-e)
prefix='partial-contact-cairo-mixed-quotient-orbit0-flat23'+('-complement' if complementary else '')
source=json.loads(Path('research/certificates/'+prefix+'-six-faces.json').read_text())
cert=json.loads(Path('research/certificates/'+prefix+'-development.json').read_text())
def parse(s):return R(sage_eval(s,locals={'w':w,'x':a,'y':b,'z':c}))
def vec(s):return vector(R,[parse(t) for t in s])
cos=[K(t) for t in (1,w/2,1/2,0,-1/2,-w/2,-1,-w/2,-1/2,0,1/2,w/2)]
sin=[K(t) for t in (0,1/2,w/2,1,w/2,1/2,0,-1/2,-w/2,-1,-w/2,-1/2)]
def frame(t,s):return matrix(K,[[cos[t],-s*sin[t]],[sin[t],s*cos[t]]])
native_dirs=(0,3,5,8,10)
local=[]
for word in (P,P,P,P,Q,Q):
 v=vector(R,[0,0]); vertices=[]
 for L,t in zip(word,native_dirs):
  vertices.append(v); v+=L*vector(K,[cos[t],sin[t]])
 assert v==vector(R,[0,0])
 local.append(vertices)
# Original Q faces have two actual positive subdivision pieces.
atoms=[]
for face in range(6):
 V=local[face]
 if not complementary:
  if face<4:atoms.append(V)
  else:atoms.append([V[0],V[1],V[1]+(B-b)*vector(K,[0,1]),V[2],V[3],V[3]+(D-a)*vector(K,[cos[8],sin[8]]),V[4],V[4]+d*vector(K,[cos[10],sin[10]])])
 else:
  if face<2:atoms.append([V[0],V[1],V[1]+(b-B)*vector(K,[0,1]),V[2],V[3],V[4]])
  elif face<4:atoms.append([V[0],V[0]+D*vector(K,[1,0]),V[1],V[2],V[3],V[4]])
  else:atoms.append([V[0],V[1],V[2],V[3],V[4],V[4]+d*vector(K,[cos[10],sin[10]])])
blocks=[[i for i,j in enumerate(source['dart_face']) if j==face] for face in range(6)]
atomic={dart:atoms[face][k] for face,block in enumerate(blocks) for k,dart in enumerate(block)}
assert {int(i):vec(v) for i,v in cert['local_atomic_vertices'].items()}==atomic
nxt={dart:block[(k+1)%len(block)] for block in blocks for k,dart in enumerate(block)}
assert [nxt[i] for i in range(36)]==source['next_dart']
forms=lambda terms:sum(K(t)*v for t,v in zip(terms,(a,b,c)))
assert [forms(v) for v in source['arm_forms']]==list(P[:4]+Q[:4])
assert [forms(v) for v in source['e_forms']]==[e,E]
for i in range(36):
 delta=atomic[nxt[i]]-atomic[i]
 t=source['native_direction_labels'][i]
 length=forms(source['edge_colors'][i][1])
 assert delta==length*vector(K,[cos[t],sin[t]])
angles=([120,90,180,120,90,120]*2+[120,180,90,120,90,120]*2+[120,90,120,90,120,180]*2) if complementary else ([120,90,120,90,120]*4+[120,90,180,120,90,180,120,180]*2)
assert angles==source['angles']
# Reconstruct actual corner arcs and seam endpoint involutions.
links={}; paired={}
for i,j,same in source['edge_pairs']:
 assert i not in paired and j not in paired and i!=j
 paired[i]=(j,same);paired[j]=(i,same)
 ends=[((i,1),(j,1)),((nxt[i],0),(nxt[j],0))] if same else [((i,1),(nxt[j],0)),((nxt[i],0),(j,1))]
 for v,u in ends:
  assert v not in links and u not in links
  links[v]=u;links[u]=v
assert set(paired)==set(range(36))
visited=set(); cycles=[]
for flag in links:
 if flag in visited:continue
 start=flag;route=[]
 while flag not in visited:
  visited.add(flag); other=(flag[0],1-flag[1]);assert other not in visited
  visited.add(other);route.append(flag[0]);flag=links[other]
 assert flag==start and sum(angles[i] for i in route)==360
 cycles.append(route)
assert len(cycles)==12 and {frozenset(v) for v in cycles}=={frozenset(v) for v in cert['vertex_links']}
# Audit reported placements directly, without reproducing the producer BFS.
states=[tuple(v) for v in cert['lift_states']];assert len(states)==len(set(states))==(6 if complementary else 12)
assert {s[0] for s in states}==set(range(6))
positions={s:vec(v) for s,v in zip(states,cert['positions'])}
periods=[vec(v) for v in cert['periods']];assert len(periods)==2
area=lambda V:sum(matrix(R,[V[k],V[(k+1)%len(V)]]).det() for k in range(len(V)))/2
A=[area(V) for V in local]
assert [parse(v) for v in cert['local_face_areas']]==A
sumarea=sum(A[s[0]] for s in states);det=matrix(R,periods).det()
assert (det if complementary else -det)==sumarea==parse(cert['total_lift_face_area']) and det==parse(cert['covolume_signed'])
observed={}; coords=[]
for tr in cert['transitions']:
 s=tuple(tr['state']);t=tuple(tr['target']);i=tr['dart'];j=tr['target_dart']
 assert s in positions and t in positions and source['dart_face'][i]==s[0] and source['dart_face'][j]==t[0]
 jj,same=paired[i]; assert j==jj
 assert (s,i) not in observed;observed[s,i]=(t,j)
 q=tuple(tr['period_coordinates']);assert len(q)==2 and all(v in ZZ for v in q)
 shift=sum((q[k]*periods[k] for k in range(2)),vector(R,[0,0]));assert shift==vec(tr['shift'])
 U=[positions[s]+frame(s[1],s[2])*atomic[k] for k in (i,nxt[i])]
 V=[positions[t]+shift+frame(t[1],t[2])*atomic[k] for k in (j,nxt[j])]
 assert U==V if same else U==V[::-1]
 assert s[2]*(U[1]-U[0])==-t[2]*(V[1]-V[0])
 coords.append(vector(ZZ,q))
assert set(observed)=={(s,i) for s in states for i in blocks[s[0]]}
assert len(observed)==(36 if complementary else 72)
for (s,i),(t,j) in observed.items():assert observed[t,j]==(s,i)
assert matrix(ZZ,coords).row_module()==ZZ**2
# An exact interior metric proves that the domain is nonempty.
fixture=({a:K(1),b:K(2),c:K(17)/10} if complementary else {a:K(1),b:K(6)/5,c:K(11)/10})
value=lambda v:K(v.subs(fixture))
assert all(value(t)>0 for t in P+Q+((b-B,a-D) if complementary else (B-b,D-a)))
assert len(set(value(t) for t in P[:4]))==len(set(value(t) for t in Q[:4]))==4
assert set(value(t) for t in P[:4])&set(value(t) for t in Q[:4])=={value(a),value(b)}
for V in local:
 VV=[vector(K,[value(t) for t in v]) for v in V]
 for k in range(5):
  edge=VV[(k+1)%5]-VV[k]
  for j in range(5):
   if j not in (k,(k+1)%5):assert matrix(K,[edge,VV[j]-VV[k]]).det()>0
if not complementary:
 eq={a:K(1),c:K(1),b:3*w-2}
 evaluate=lambda t:K(t.subs(eq))
 assert evaluate(B-b)==evaluate(D-a)==0 and all(evaluate(t)>0 for t in P+Q)
 zero={i for i in range(36) if evaluate(forms(source['edge_colors'][i][1]))==0}
 assert zero=={21,24,29,32} and all(paired[i][0] in zero for i in zero)
 assert sum(1 for state in states for i in blocks[state[0]] if i in zero)==8
 assert evaluate(sumarea)>0 and evaluate(-det)==evaluate(sumarea)
print('PASS orbit0flat23 full polynomial native geometry, two linked bank cuts, 12 circular links, 6/12 native placements, 36/72 reverse boundaries, primitive lattice, area/covolume and exact private-arm fixtures.')
