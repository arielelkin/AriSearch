#!/usr/bin/env python3
"""Exact original-vertex chord gate; at most two chords, 30-second cap."""
import itertools,json,sys,time
from fractions import Fraction as F
from pathlib import Path
START=time.monotonic()
SOURCE=Path('research/certificates/hat-eight-kite-convex-cluster-gate.json')
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(p):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1]))
def simplify(face,pts):
 f=list(face)
 while len(f)>2:
  rem=[i for i in range(len(f)) if cross(pts[f[i-1]],pts[f[i]],pts[f[(i+1)%len(f)]])==0]
  if not rem:break
  f.pop(rem[0])
 return f

def canon(face,pts):
 p=[pts[i] for i in face];n=len(p)
 def d(a,b):return (a[0]-b[0])**2+3*(a[1]-b[1])**2
 return min(tuple(d(p[(s+e*i)%n],p[(s+e*j)%n]) for i in range(n) for j in range(i+1,n)) for s in range(n) for e in (-1,1))
def run():
 raw=json.loads(SOURCE.read_text())['hat_outline'];pts=[]
 for p in raw:
  assert F(p[0][1])==F(p[1][0])==0
  a,b=2*F(p[0][0]),2*F(p[1][1]);assert a.denominator==b.denominator==1
  pts.append((int(a),int(b)))
 n=len(pts);assert n==13 and area(pts)>0
 assert all(cross(pts[i-1],pts[i],pts[(i+1)%n])!=0 for i in range(n))
 # A dissection into k faces has at least 5k incidences, n+2(k-1) total.
 max_chords=(n-5)//3;assert max_chords==2
 states={():[list(range(n))]};counts=[];accepted=[];classes={}
 for depth in range(max_chords+1):
  counts.append(len(states))
  nxt={}
  for cuts,faces in sorted(states.items()):
   if time.monotonic()-START>30:raise TimeoutError('incomplete: 30 second cap')
   simple=[simplify(f,pts) for f in faces]
   if all(len(f) in (5,6) and all(cross(pts[f[i-1]],pts[f[i]],pts[f[(i+1)%len(f)]])>0 for i in range(len(f))) for f in simple):
    ids=[]
    for f in simple:
     key=canon(f,pts)
     if key not in classes:classes[key]=len(classes)
     ids.append(classes[key])
    accepted.append(dict(cuts=cuts,faces=faces,genuine_faces=simple,classes=ids))
   if depth==max_chords:continue
   for fi,face in enumerate(faces):
    m=len(face)
    for i in range(m):
     for j in range(i+2,m):
      if i==0 and j==m-1:continue
      chord=tuple(sorted((face[i],face[j])))
      nc=tuple(sorted(cuts+(chord,)))
      nf=faces[:fi]+faces[fi+1:]+[face[i:j+1],face[j:]+face[:i+1]]
      nxt[nc]=nf
  states=nxt
 out=dict(status='COMPLETE',source=str(SOURCE),coordinate_map='(X,Y) -> (X/2,sqrt(3)*Y/2)',outline=pts,max_chords=max_chords,runtime_cap_seconds=30,combinatorial_dissection_counts=counts,accepted_partitions=accepted,shape_class_count=len(classes),two_class_partitions=[p for p in accepted if len(set(p['classes']))==2],periodic_audit='Not reached when no two-class partition exists',elapsed_seconds=time.monotonic()-START)
 Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
