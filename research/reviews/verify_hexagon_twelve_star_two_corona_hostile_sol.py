import itertools as I,json
from pathlib import Path
from sage.all import QQ,matrix
root=Path(__file__).resolve().parents[2]
c=json.loads((root/'research/certificates/hexagon-twelve-star-two-corona-support-sol-2026-10-19.json').read_text())
W=((0,1,2,0,3,4),(0,0,1,1,2,3))
def arms(p):
 x,h=p;f,j=divmod(x,6);return (6*f+j,6*f+(j+1)%6)[::h]
def color(s):return W[s//6][s%6]
def cyclic(t):return min(t,t[1:]+t[:1],t[2:]+t[:2])
def other(p,s):
 x,h=p;return (s//6*6+((s%6-1)%6 if x==s else s%6),h)
S={cyclic(t) for t in I.product(I.product(range(12),(1,-1)),repeat=3) if all(color(arms(t[k])[1])==color(arms(t[(k+1)%3])[0]) for k in range(3))}
while True:
 pairs={(t[k],t[(k+1)%3]) for t in S for k in range(3)}
 N={t for t in S if all((other(t[(k+1)%3],arms(t[(k+1)%3])[0]),other(t[k],arms(t[k])[1])) in pairs for k in range(3))}
 if N==S:break
 S=N
S=sorted(S);assert S==[tuple(map(tuple,t)) for t in c['stars']]
req=[]
for t in S:
 needs=[]
 for k in range(3):
  q,p=t[(k+1)%3],t[k];remote=(other(q,arms(q)[0]),other(p,arms(p)[1]))
  needs.append({j for j,u in enumerate(S) if any((u[l],u[(l+1)%3])==remote for l in range(3))})
 req.append(needs)
# Reconstruct signed two-sector factors directly from the corners around each boundary vertex.
F=[{} for _ in range(5)]
for j,t in enumerate(S):
 for k,p in enumerate(t):
  before,after=t[(k-1)%3],t[(k+1)%3]
  if p[1]==1 and p[0]<4:
   pair=((arms(before)[1],before[1]),(arms(after)[0],after[1]));F[p[0]+1].setdefault(pair,set()).add(j)
  if p==(4,1) and after==(5,1):
   pair=((arms(before)[1],before[1]),(arms(before)[0],before[1]));F[0].setdefault(pair,set()).add(j)
cycles=[]
def walk(states,groups):
 k=len(groups)
 if k==10:
  if states[-1]==states[0]:cycles.append((states,groups))
  return
 for (a,b),ids in F[k%5].items():
  if not states or a==states[-1]:walk(([a] if not states else states)+[b],groups+[ids])
walk([],[]);assert len(cycles)==2
surv=[];counts=[0,0]
for mask in range(4096):
 ids={j for j in range(12) if mask>>j&1}
 if {p[0] for j in ids for p in S[j]}!=set(range(12)):continue
 if any(not(ids&g) for j in ids for g in req[j]):continue
 hits=[k for k,(_,groups) in enumerate(cycles) if all(ids&g for g in groups)]
 if hits:
  surv.append(mask)
  for k in hits:counts[k]+=1
assert surv==c['support_masks'];assert sorted(counts)==[6,8]
mins=[x for x in surv if not any(y!=x and y&x==y for y in surv)];assert mins==[1622,2216]
for rec in c['minimal_supports']:
 rows=[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]
 rows += [[sum(p[0]==i for p in S[j]) for i in range(12)]+[2] for j in range(12) if rec['mask']>>j&1]
 M=matrix(QQ,rows);assert [[str(x) for x in row] for row in M.echelon_form()]==rec['angle_rref']
 if rec['mask']==1622:assert M.stack(matrix(QQ,[[int(i<3) for i in range(12)]+[2]])).rank()==M.rank()
# Native vertex v precedes side v; corner index is v-1. Reverse abstract boundary direction on every glued interval.
H=(1,1,-1,-1);edges=c['carrier']['native_edge_pairs'];adj={i:[] for i in range(24)};used=[]
for f,i,g,j in edges:
 used += [(f,i),(g,j)];assert W[f//2][i]==W[g//2][j]
 first=(i,(i+1)%6) if H[f]==1 else ((i+1)%6,i)
 second=(j,(j+1)%6) if H[g]==1 else ((j+1)%6,j)
 for v,w in zip(first,second[::-1]):
  a,b=6*f+(v-1)%6,6*g+(w-1)%6;adj[a].append(b);adj[b].append(a)
assert sorted(used)==list(I.product(range(4),range(6)))
left=set(adj);links=[]
while left:
 component={min(left)}
 while True:
  new=component|{v for u in component for v in adj[u]}
  if new==component:break
  component=new
 assert len(component)==3 and all(len(adj[u])==2 and len(set(adj[u]))==2 for u in component)
 left-=component;links.append(tuple(sorted(6*(u//12)+u%6 for u in component)))
assert sorted(links)==sorted([(0,6,7),(1,8,9),(2,3,10),(4,5,11)]*2)
B=W[1];orbit={B[k:]+B[:k] for k in range(6)}|{B[::-1][k:]+B[::-1][:k] for k in range(6)}
assert len(orbit)==12
print('Independent atlas, 4096 supports, rational rows, EVERY color pair, reflected links and twelve-word orbit PASS')
