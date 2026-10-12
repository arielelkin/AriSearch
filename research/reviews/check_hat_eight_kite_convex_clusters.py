#!/usr/bin/env python3
"""Independent edge-cancellation/clip audit of fixed eight-kite compiler.
No producer import or convex-hull algorithm is used. Optional output only.
"""
import argparse,hashlib,itertools,json
from collections import Counter,defaultdict
from pathlib import Path
from sage.all import QuadraticField,AA
K=QuadraticField(3,'root_three',embedding=AA(3).sqrt());r=K.gen()
def point(p):return tuple(K(a)+K(b)*r for a,b in p)
def subtract(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def turn(a,b,c):return cross(subtract(b,a),subtract(c,b))
def area2(P):return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1])) if P else K(0)
def simplify(P):
 P=P[:];changed=True
 while changed and len(P)>=3:
  changed=False
  for i in range(len(P)):
   if turn(P[i-1],P[i],P[(i+1)%len(P)])==0:
    assert dot(subtract(P[i],P[i-1]),subtract(P[(i+1)%len(P)],P[i]))>0
    P.pop(i);changed=True;break
 return P
def same(P,Q):return len(P)==len(Q) and any(P[i:]+P[:i]==Q for i in range(len(P)))
def clip(P,clipper):
 for a,b in zip(clipper,clipper[1:]+clipper[:1]):
  result=[]
  if not P:break
  for p,q in zip(P,P[1:]+P[:1]):
   fp=cross(subtract(b,a),subtract(p,a));fq=cross(subtract(b,a),subtract(q,a))
   if fp>=0:result.append(p)
   if (fp<0<fq) or (fq<0<fp):
    t=fp/(fp-fq);result.append(tuple(p[i]+t*(q[i]-p[i]) for i in (0,1)))
  P=result
 return P

def boundary(polygons):
 vertices=set(p for P in polygons for p in P);edges=Counter()
 for P in polygons:
  for a,b in zip(P,P[1:]+P[:1]):
   d=subtract(b,a)
   on=[p for p in vertices if cross(d,subtract(p,a))==0 and 0<=dot(subtract(p,a),d)<=dot(d,d)]
   on.sort(key=lambda p:AA(dot(subtract(p,a),d)))
   edges.update(zip(on,on[1:]))
 residual={edge:count-edges[edge[1],edge[0]] for edge,count in edges.items() if count>edges[edge[1],edge[0]]}
 if any(n!=1 for n in residual.values()):return None
 nxt={};incoming=Counter()
 for a,b in residual:
  if a in nxt:return None
  nxt[a]=b;incoming[b]+=1
 if set(nxt)!=set(incoming) or any(n!=1 for n in incoming.values()):return None
 remaining=set(nxt);cycles=[]
 while remaining:
  start=next(iter(remaining));p=start;P=[]
  while p in remaining:remaining.remove(p);P.append(p);p=nxt[p]
  if p!=start:return None
  cycles.append(simplify(P))
 return cycles[0] if len(cycles)==1 else None

def congruent(P,Q):
 if len(P)!=len(Q):return False
 n=len(P)
 return any(all(dot(subtract(P[i],P[j]),subtract(P[i],P[j]))==dot(subtract(Q[(s+d*i)%n],Q[(s+d*j)%n]),subtract(Q[(s+d*i)%n],Q[(s+d*j)%n])) for i,j in itertools.combinations(range(n),2)) for s in range(n) for d in (1,-1))
def rotate(P,n):
 for _ in range(n):P=[(p[0]/2-r*p[1]/2,r*p[0]/2+p[1]/2) for p in P]
 return P

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args();path=Path('research/certificates/hat-eight-kite-convex-cluster-gate.json');raw=path.read_bytes();data=json.loads(raw)
 kites=[[point(p) for p in P] for P in data['kites']];outline=[point(p) for p in data['hat_outline']]
 assert len(kites)==8 and all(len(P)==4 and area2(P)>0 and all(turn(P[i-1],P[i],P[(i+1)%4])>0 for i in range(4)) for P in kites)
 for P,Q in itertools.combinations(kites,2):assert area2(clip(P,Q))==0
 full=boundary(kites);assert full is not None and same(full,simplify(outline))
 polys={}
 for mask in range(1,256):
  P=boundary([kites[i] for i in range(8) if mask>>i&1])
  if P is None:continue
  if all(cross(subtract(b,a),subtract(p,a))>=0 for a,b in zip(P,P[1:]+P[:1]) for p in P):polys[mask]=P
 stored={row['mask']:row for row in data['convex_subsets']};assert set(polys)==set(stored) and len(polys)==16
 for mask,P in polys.items():assert len(P)==stored[mask]['corners'] and same(P,[point(p) for p in stored[mask]['hull']])
 eligible={m for m,P in polys.items() if len(P)>=5};assert eligible==set(data['eligible_masks'])=={6,9,12,13,14,48,192}
 # Enumerate all combinations of eligible clusters as unordered set covers.
 partitions=[]
 for n in range(1,9):
  for masks in itertools.combinations(sorted(eligible),n):
   if sum(m.bit_count() for m in masks)!=8:continue
   union=0;overlap=False
   for mask in masks:overlap|=bool(union&mask);union|=mask
   if union==255 and not overlap:partitions.append(masks)
 assert partitions==[(6,9,48,192)]
 assert {tuple(sorted(p['masks'])) for p in data['partitions']}==set(partitions)
 assert all(congruent(polys[9],polys[m]) for m in (6,12,48,192)) and congruent(polys[13],polys[14])
 assert all(p['congruence_classes']==1 for p in data['partitions'])
 # Three120-degree sectors of the pair pentagon and two180-degree sectors
 # of the half-hex pentagon exactly partition a regular hexagon.
 hexes=[]
 for mask,copies,step in ((9,3,2),(13,2,3)):
  pieces=[rotate(polys[mask],step*i) for i in range(copies)]
  for P,Q in itertools.combinations(pieces,2):assert area2(clip(P,Q))==0
  H=boundary(pieces);assert H is not None and len(H)==6 and area2(H)==sum(map(area2,pieces))
  assert all(dot(p,p)==4 for p in H) and all(dot(subtract(a,b),subtract(a,b))==4 for a,b in zip(H,H[1:]+H[:1]))
  hexes.append(mask)
 result={'status':'PASSED','source_sha256':hashlib.sha256(raw).hexdigest(),'primitive_intersection_pairs_checked':28,'nonempty_subsets_checked':255,'convex_subsets':16,'eligible_masks':sorted(eligible),'eligible_partitions':[list(x) for x in partitions],'periodic_regular_hexagon_compilers':{'pair_pentagon_copies':3,'half_hexagon_pentagon_copies':2},'scope':'Fixed retained eight-kite geometry; whole-kite clusters only; every convex cluster has an admitted monohedral periodic escape'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
