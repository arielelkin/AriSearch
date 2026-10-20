"""Exact midpoint/centroid corner-star retiling gate on one depth-3 pinwheel supertile."""
from fractions import Fraction as F
from pathlib import Path
import json
import argparse

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def midpoint(a,b):return mul(add(a,b),F(1,2))
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and dot(sub(p,a),sub(p,b))<=0
def area(t):return cross(sub(t[1],t[0]),sub(t[2],t[0]))/2
base=((F(0),F(0)),(F(2),F(0)),(F(0),F(1)))
big=[((0,0),(2,0),(2,1)),((2,0),(4,0),(4,1)),((4,0),(5,0),(4,2)),((2,1),(4,1),(4,2)),((2,0),(4,1),(2,1))]
def normalize(p):return (F(2)-F(2,5)*p[0]-F(1,5)*p[1],F(1,5)*p[0]-F(2,5)*p[1])
children=[tuple(normalize(p) for p in t) for t in big]
def ordered(t):
 for k in range(3):
  o=t[k];u=t[(k+1)%3];v=t[(k+2)%3]
  if dot(sub(u,o),sub(v,o))==0:
   if dot(sub(u,o),sub(u,o))<dot(sub(v,o),sub(v,o)):u,v=v,u
   return o,u,v
 raise AssertionError('not right')
def subdivide(t):
 o,u,v=ordered(t)
 def f(p):return add(o,add(mul(sub(u,o),p[0]/2),mul(sub(v,o),p[1])))
 return [tuple(f(p) for p in c) for c in children]
def canonical(p):
 ans=[]
 for q in (p,p[::-1]):
  for k in range(len(q)):
   r=q[k:]+q[:k];ans.append(tuple(dot(sub(a,b),sub(a,b)) for i,a in enumerate(r) for b in r[:i]))
 return min(ans)
def enc(p):return [[str(x),str(y)] for x,y in p]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--center',choices=['centroid','fifth'],default='centroid');args=parser.parse_args()
 ts=[base]
 for _ in range(3):ts=[c for t in ts for c in subdivide(t)]
 assert len(ts)==125 and sum(abs(area(t)) for t in ts)==1
 for t in ts:
  assert all(cross(sub(b,a),sub(p,a))>=0 for p in t for a,b in zip(base,base[1:]+base[:1]))
 for i,t in enumerate(ts):
  for u in ts[:i]:
   separated=False
   for q in (t,u):
    for a,b in zip(q,q[1:]+q[:1]):
     e=sub(b,a);n=(-e[1],e[0]);at=[dot(p,n) for p in t];au=[dot(p,n) for p in u]
     if max(at)<=min(au) or max(au)<=min(at):separated=True
   assert separated
 vs=set(p for t in ts for p in t);results=[];classes={}
 for v in sorted(vs):
  if any(on(v,a,b) for a,b in zip(base,base[1:]+base[:1])):continue
  segments={};incident=[]
  for t in ts:
   if not any(on(v,a,b) for a,b in zip(t,t[1:]+t[:1])):continue
   if area(t)<0:t=t[::-1]
   if args.center=='centroid':center=mul(add(add(t[0],t[1]),t[2]),F(1,3))
   else:
    o,u,w=ordered(t);center=add(o,mul(add(sub(u,o),sub(w,o)),F(1,5)))
   neighbors=[]
   for a,b in zip(t,t[1:]+t[:1]):
    if on(v,a,b):
     pts=sorted((p for p in vs if on(p,a,b)),key=lambda p:dot(sub(p,a),sub(b,a)))
     j=pts.index(v)
     if j:neighbors.append(('in',pts[j-1]))
     if j+1<len(pts):neighbors.append(('out',pts[j+1]))
   assert len(neighbors)==2
   prev=next(p for typ,p in neighbors if typ=='in');nxt=next(p for typ,p in neighbors if typ=='out')
   # CCW face boundary enters v from prev; dual boundary runs next-mid, center, prev-mid.
   x,y=midpoint(v,nxt),midpoint(v,prev)
   assert x not in segments and center not in segments
   segments[x]=center;segments[center]=y;incident.append(t)
  start=min(segments);poly=[start];q=segments[start]
  while q!=start:
   assert q not in poly;poly.append(q);q=segments[q]
  assert len(poly)==len(segments)
  changed=True
  while changed:
   changed=False
   for i in range(len(poly)):
    if cross(sub(poly[i],poly[i-1]),sub(poly[(i+1)%len(poly)],poly[i]))==0:
     poly.pop(i);changed=True;break
  turns=[cross(sub(poly[i],poly[i-1]),sub(poly[(i+1)%len(poly)],poly[i])) for i in range(len(poly))]
  convex=all(x>0 for x in turns)
  result={'source_vertex':enc([v])[0],'boundary':enc(poly),'strict_convex':convex,'turns':[str(x) for x in turns],'incident_triangles':[enc(t) for t in incident]}
  results.append(result)
  if convex:classes.setdefault(canonical(poly),result)
 out={'domain':'one exact depth-3 normalized pinwheel supertriangle; all fully interior source/planarization vertices','center':args.center,'source_triangles':125,'interior_vertex_cells':len(results),'strict_convex_cells':sum(r['strict_convex'] for r in results),'strict_convex_congruence_classes':len(classes),'cells':results}
 dest=Path(__file__).with_suffix('.json') if args.center=='centroid' else Path(__file__).with_name(Path(__file__).stem+'-fifth.json');dest.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='cells'}))
if __name__=='__main__':main()
