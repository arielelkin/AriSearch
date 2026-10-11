"""Independent fixed-native geometry audit of the retained mixed Cairo quotient.
No author module or solver import; polynomial identities cover the full cone.
"""
from sage.all import *
from pathlib import Path
import json


K=QuadraticField(3,'w'); w=K.gen()
R=PolynomialRing(K,names=('x','y')); a,b=R.gens()
c=(3*w*a+b)/4;d=(a+w*b)/4;e=2*d
A=4*b-w*a;B=a;C=3*w*b-2*a;D=b;E=2*b
P=(a,b,c,d,e); Q=(A,B,C,D,E)
assert B-C==w*(D-A) and E==w*C+D-2*A
assert A-b==w*(C-a)/3 and E==2*b
prefix='partial-contact-cairo-mixed-quotient-orbit6-flat239'
source=json.loads(Path('research/certificates/'+prefix+'-ten-faces.json').read_text())
cert=json.loads(Path('research/certificates/'+prefix+'-development.json').read_text())
def parse(s):return R(sage_eval(s,locals={'w':w,'x':a,'y':b}))
def vec(s):return vector(R,[parse(t) for t in s])
cos=[K(t) for t in (1,w/2,1/2,0,-1/2,-w/2,-1,-w/2,-1/2,0,1/2,w/2)]
sin=[K(t) for t in (0,1/2,w/2,1,w/2,1/2,0,-1/2,-w/2,-1,-w/2,-1/2)]
def frame(t,s):return matrix(K,[[cos[t],-s*sin[t]],[sin[t],s*cos[t]]])
native_dirs=(0,3,5,8,10)
local=[]
for word in (P,)*8+(Q,)*2:
 v=vector(R,[0,0]); vertices=[]
 for L,t in zip(word,native_dirs):
  vertices.append(v); v+=L*vector(K,[cos[t],sin[t]])
 assert v==vector(R,[0,0])
 local.append(vertices)
# Original Q faces have two actual positive subdivision pieces.
atoms=[]
for face in range(10):
 V=local[face]
 if face<6:atoms.append(V)
 elif face<8:atoms.append([V[0],V[1],V[2],V[3],V[4],V[4]+d*vector(K,[cos[10],sin[10]])])
 else:atoms.append([V[0],V[0]+b*vector(K,[1,0]),V[1],V[2],V[2]+a*vector(K,[cos[5],sin[5]]),V[3],V[4],V[4]+b*vector(K,[cos[10],sin[10]])])
blocks=[[i for i,j in enumerate(source['dart_face']) if j==face] for face in range(10)]
atomic={dart:atoms[face][k] for face,block in enumerate(blocks) for k,dart in enumerate(block)}
assert {int(i):vec(v) for i,v in cert['local_atomic_vertices'].items()}==atomic
nxt={dart:block[(k+1)%len(block)] for block in blocks for k,dart in enumerate(block)}
assert [nxt[i] for i in range(58)]==source['next_dart']
forms=lambda terms:sum(K(t)*v for t,v in zip(terms,(a,b)))
assert [forms(v) for v in source['arm_forms']]==list(P[:4]+Q[:4])
assert [forms(v) for v in source['e_forms']]==[e,E]
for i in range(58):
 delta=atomic[nxt[i]]-atomic[i]
 t=source['native_direction_labels'][i]
 length=forms(source['edge_colors'][i][1])
 assert delta==length*vector(K,[cos[t],sin[t]])
angles=[120,90,120,90,120]*6+[120,90,120,90,120,180]*2+[120,180,90,120,180,90,120,180]*2
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
assert set(paired)==set(range(58))
visited=set(); cycles=[]
for flag in links:
 if flag in visited:continue
 start=flag;route=[]
 while flag not in visited:
  visited.add(flag); other=(flag[0],1-flag[1]);assert other not in visited
  visited.add(other);route.append(flag[0]);flag=links[other]
 assert flag==start and sum(angles[i] for i in route)==360
 cycles.append(route)
assert len(cycles)==19 and {frozenset(v) for v in cycles}=={frozenset(v) for v in cert['vertex_links']}
# Audit reported placements directly, without reproducing the producer BFS.
states=[tuple(v) for v in cert['lift_states']];assert len(states)==len(set(states))==10
assert {s[0] for s in states}==set(range(10))
positions={s:vec(v) for s,v in zip(states,cert['positions'])}
periods=[vec(v) for v in cert['periods']];assert len(periods)==2
area=lambda V:sum(matrix(R,[V[k],V[(k+1)%len(V)]]).det() for k in range(len(V)))/2
faceareas=[area(V) for V in local]
assert [parse(v) for v in cert['local_face_areas']]==faceareas
sumarea=sum(faceareas[s[0]] for s in states);det=matrix(R,periods).det()
assert -det==sumarea==parse(cert['total_lift_face_area']) and det==parse(cert['covolume_signed'])
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
assert len(observed)==58
for (s,i),(t,j) in observed.items():assert observed[t,j]==(s,i)
assert matrix(ZZ,coords).row_module()==ZZ**2
# An exact interior metric proves that the domain is nonempty.
fixture={a:K(1),b:K(6)/5}
value=lambda v:K(v.subs(fixture))
assert all(value(t)>0 for t in P+Q+(A-b,C-a))
assert len(set(value(t) for t in P[:4]))==len(set(value(t) for t in Q[:4]))==4
assert set(value(t) for t in P[:4])&set(value(t) for t in Q[:4])=={value(a),value(b)}
for V in local:
 VV=[vector(K,[value(t) for t in v]) for v in V]
 for k in range(5):
  edge=VV[(k+1)%5]-VV[k]
  for j in range(5):
   if j not in (k,(k+1)%5):assert matrix(K,[edge,VV[j]-VV[k]]).det()>0
eq={a:K(1),b:1/w}
evaluate=lambda t:K(t.subs(eq))
assert evaluate(A-b)==evaluate(C-a)==0 and all(evaluate(t)>0 for t in P+Q)
zero={i for i in range(58) if evaluate(forms(source['edge_colors'][i][1]))==0}
assert zero=={43,46,51,54} and all(paired[i][0] in zero for i in zero)
assert evaluate(sumarea)>0 and evaluate(-det)==evaluate(sumarea)
print('PASS orbit6flat239 HIGH-DOMAIN full polynomial native geometry/cuts, all19 circular links, 10 original placements, 58 reverseboundary transitions, primitive lattice, area/covolume and exact private-arm fixture.')
