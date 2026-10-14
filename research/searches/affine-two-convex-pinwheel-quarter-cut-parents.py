"""Specified cross-boundary resection, squared-pinwheel parent packing domain.
No whole-face inflation or shape-only forcing is assumed.
"""
from fractions import Fraction as F
import runpy,subprocess,json,itertools
from ortools.sat.python import cp_model
D=runpy.run_path('research/searches/pinwheel-three-triangle-convex-clusters.py')
add,sub,mul,dot,cross,hull,area,canonical=[D[n] for n in ('add','sub','mul','dot','cross','hull','area','canonical')]
def mat(A,p):return tuple(sum(A[i][j]*p[j] for j in range(2)) for i in range(2))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv(A):
 d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
 return ((A[1][1]/d,-A[0][1]/d),(-A[1][0]/d,A[0][0]/d))
def orth(e):return ((e[0],-e[1]),(e[1],e[0]))
def encode(P):return [[str(x),str(y)] for x,y in P]
def decode(P):return tuple(tuple(F(z) for z in p) for p in P)
record=json.loads(subprocess.run(['python','research/searches/affine-two-convex-pinwheel-four-face-gate.py'],check=True,capture_output=True,text=True).stdout)
P=((F(0),F(-1)),(F(4,5),F(-8,5)),(F(2),F(0)),(F(4,5),F(8,5)),(F(0),F(1)))
H=((F(0),F(0)),(F(6,5),F(-8,5)),(F(2),F(-1)),(F(2),F(0)),(F(4,5),F(8,5)),(F(0),F(1)))
J=((F(-7,25),F(-24,25)),(F(24,25),F(-7,25)))
shift=sub(P[1],mat(J,H[1])); Q=tuple(add(mat(J,z),shift) for z in H)
assert Q[1]==P[1] and Q[2]==P[0] and D['interior_disjoint'](P,Q)
w=add(P[1],mul(sub(P[2],P[1]),F(1,4)))
Pn=P[:1]+(w,)+P[2:];Qn=Q[:1]+(w,)+Q[2:]
assert area(Pn)==F(15,4) and area(Qn)==F(17,4)
for T in (Pn,Qn):
 assert len(hull(T))==len(T)
 assert all(cross(sub(b,a),sub(z,a))>0 for i,(a,b) in enumerate(D['edges'](T)) for j,z in enumerate(T) if j not in (i,(i+1)%len(T)))
# The old P/Q pair partitions its unchanged union after moving shared corner.
assert D['interior_disjoint'](Pn,Qn) and area(Pn)+area(Qn)==8
source=[]
for C in record['classes']:
 B=decode(C['boundary'])
 if B==P:source += [decode(t) for t in C['triangles']]
 if B==H:source += [tuple(add(mat(J,z),shift) for z in decode(t)) for t in C['triangles']]
assert len(source)==8
M=((F(2),F(1)),(F(-1),F(2))); M2=mm(M,M); assert M2==((3,4),(-4,3))
primitive=[((0,0),(0,-2),(-1,-2)),((0,0),(2,-1),(0,-1)),((0,-1),(2,-1),(0,-2)),((0,-2),(2,-1),(2,-2)),((2,-1),(4,-2),(2,-2))]
primitive=[hull(tuple(tuple(F(z) for z in p) for p in T)) for T in primitive]
def subdivide(T):
 for i,p in enumerate(T):
  others=[q for j,q in enumerate(T) if j!=i]
  if dot(sub(others[0],p),sub(others[1],p))==0:break
 q=next(q for q in others if dot(sub(q,p),sub(q,p))==4)
 r=next(q for q in others if dot(sub(q,p),sub(q,p))==1)
 e=mul(sub(q,p),F(1,2));f=mul(sub(r,p),F(-1)); A=((e[0],f[0]),(e[1],f[1]))
 B=mm(mm(M,A),inv(M));tr=mat(M,p)
 return [hull(tuple(add(mat(B,z),tr) for z in C)) for C in primitive]
for _ in range(2):source=[U for T in source for U in subdivide(T)]
assert len(source)==200 and all(area(T)==1 for T in source)
# Only full-native-side connected four-cell old face occurrences are compiled.
adj=[set() for T in source]
edgemap={}
for i,T in enumerate(source):
 for a,b in D['edges'](T):edgemap.setdefault(tuple(sorted((a,b))),[]).append(i)
for cells in edgemap.values():
 for i,j in itertools.combinations(cells,2):adj[i].add(j);adj[j].add(i)
clusters={frozenset((i,)) for i in range(200)}
for n in range(2,5):
 clusters={C|{j} for C in clusters for j in set.union(*(adj[i] for i in C))-C}
keys={canonical(P):('P',P,Pn),canonical(Q):('Q',Q,Qn)}
oldfaces=[]
for C in sorted(clusters,key=lambda S:tuple(sorted(S))):
 B=hull([p for i in C for p in source[i]])
 if area(B)==4 and canonical(B) in keys:oldfaces.append((C,B,keys[canonical(B)]))
def maps(S,T):
 e=sub(S[1],S[0]); E=orth(e)
 for rev in (T,T[::-1]):
  for k in range(len(T)):
   R=rev[k:]+rev[:k]
   if canonical(R)!=canonical(S):continue
   f=sub(R[1],R[0]); A=mm(orth(f),inv(E))
   for sign in (1,-1):
    # Native distance agreement, not a chosen handedness, selects the map.
    if sign==-1:A=mm(((f[0],f[1]),(f[1],-f[0])),inv(E))
    b=sub(R[0],mat(A,S[0]))
    if tuple(add(mat(A,z),b) for z in S)==R:yield A,b
parents=[('P',tuple(mat(M2,z) for z in Pn),8,15),('Q',tuple(mat(M2,z) for z in Qn),17,10)]
result={'scope':'fixed quarter-corner resection, 200 squared-pinwheel source cells; full-native-connected old4cell P/H compilers only; exact contained convex packing', 'P':encode(Pn),'Q':encode(Qn),'M2':M2,'source_cells':200,'four_cell_cluster_count':len(clusters),'old_face_occurrences':len(oldfaces),'parents':[]}
for name,parent,np,nq in parents:
 candidates={}
 for C,B,(species,old,new) in oldfaces:
  for A,b in maps(old,B):
   T=tuple(add(mat(A,z),b) for z in new)
   if all(cross(sub(v,u),sub(z,u))>=0 for u,v in D['edges'](parent) for z in T):candidates[(species,tuple(sorted(T)))]=T
 names=list(candidates);faces=list(candidates.values());model=cp_model.CpModel();chosen=[model.new_bool_var(str(i)) for i in range(len(faces))]
 model.add(sum(chosen[i] for i,n in enumerate(names) if n[0]=='P')==np);model.add(sum(chosen[i] for i,n in enumerate(names) if n[0]=='Q')==nq)
 overlaps=0
 for i,T in enumerate(faces):
  for j in range(i):
   if not D['interior_disjoint'](T,faces[j]):model.add(chosen[i]+chosen[j]<=1);overlaps+=1
 solver=cp_model.CpSolver();solver.parameters.num_search_workers=1;solver.parameters.max_time_in_seconds=30
 status=solver.solve(model);entry={'parent':name,'candidate_counts':{s:sum(n[0]==s for n in names) for s in ('P','Q')},'required_counts':[np,nq],'overlap_constraints':overlaps,'status':solver.status_name(status)}
 if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):entry['tiles']=[{'species':names[i][0],'vertices':encode(faces[i])} for i,x in enumerate(chosen) if solver.value(x)]
 result['parents'].append(entry)
print(json.dumps(result,default=lambda x:str(x),indent=2))
