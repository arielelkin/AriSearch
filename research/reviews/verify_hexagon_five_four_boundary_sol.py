"""Independent boundary check using reviewed exposed-edge certificate as input."""
from pathlib import Path
import json
from sage.all import QuadraticField, vector, matrix, floor
K=QuadraticField(3,'r');r=K.gen();base=Path(__file__).resolve().parents[1]
read=lambda n:json.loads((base/'certificates'/n).read_text())
parent=read('hexagon-five-four-corona-translation-2026-10-19.json')
claim=read('hexagon-five-four-strip-boundary-completion-2026-10-19.json')
def pt(p):return vector(K,list(map(K,p)))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
for old,new in zip(parent['rows'],claim['rows']):
 assert old['row_index']==new['row_index']
 v=pt(old['translation']);N=v*v
 def canonical(p):
  n=floor(min(x*v for x in p)/N)
  return frozenset(tuple(x-n*v) for x in p)
 actual={canonical([pt(p) for p in e['endpoints']]) for e in old['boundary']}
 chains=[[pt(p) for p in c['vertices']] for c in new['chains']]
 assert len(chains)==2 and all(len(c)==5 for c in chains)
 claimed={canonical([c[k],c[k+1]]) for c in chains for k in range(4)}
 assert claimed==actual and len(claimed)==8
 D=[[c[k+1]-c[k] for k in range(4)] for c in chains]
 assert all(D[0][k]==-D[1][k] for k in range(4))
 assert chains[0][-1]-chains[0][0]==v
 assert chains[1][-1]-chains[1][0]==-v
 lengths=[x*x for x in D[0]]
 assert len(set(lengths))==4 and all(x>0 for x in lengths)
 assert all(cross(D[0][k],D[0][(k+1)%4])!=0 for k in range(4))
 # Reconstruct each possible orthogonal map from the source first edge
 # and each signed target edge, rather than presupposing a period-line map.
 cases=0
 for s in range(2):
  u=D[s][0];Ju=vector(K,[-u[1],u[0]])
  U=matrix(K,[[u[0],Ju[0]],[u[1],Ju[1]]])
  for t in range(2):
   target={canonical([chains[t][k],chains[t][k+1]]) for k in range(4)}
   for j,w in enumerate(D[t]):
    if u*u!=w*w:continue
    for direction in (-1,1):
     z=direction*w;Jz=vector(K,[-z[1],z[0]])
     for det in (-1,1):
      M=matrix(K,[[z[0],det*Jz[0]],[z[1],det*Jz[1]]])*U.inverse()
      assert M.transpose()*M==matrix.identity(K,2)
      if det*(M*(chains[s][-1]-chains[s][0]))!=-(chains[t][-1]-chains[t][0]):continue
      anchor=chains[t][j] if direction==1 else chains[t][j+1]
      offset=anchor-M*chains[s][0]
      image={canonical([M*chains[s][k]+offset,M*chains[s][k+1]+offset]) for k in range(4)}
      assert image!=target
      cases+=1
 assert len(new['tests'])==32 and all(not x['match'] for x in new['tests'])
 print('PASS',new['row_index'],'eight independently supplied edges; length-compatible opposite-interior maps',cases)
