#!/usr/bin/env python3
"""Exact fixed one-corona gate for A=(2,1)*3,B=(2,2,3,1,3,2)."""
import json
from pathlib import Path
U=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def add(p,q):return (p[0]+q[0],p[1]+q[1])
def sub(p,q):return (p[0]-q[0],p[1]-q[1])
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def poly(ls):
 q=[(0,0)]
 for k,l in enumerate(ls):q.append(add(q[-1],(l*U[k][0],l*U[k][1])))
 assert q[-1]==(0,0)
 return q[:-1]
def no_T(P,Q):
 for R,T in [(P,Q),(Q,P)]:
  for v in R:
   for k,p in enumerate(T):
    w=T[(k+1)%6]; d=sub(w,p); e=sub(v,p)
    if cross(d,e)==0 and 0<e[0]*d[0]+e[1]*d[1]<d[0]*d[0]+d[1]*d[1]:return False
 return True
def disjoint(P,Q):
 # Ordered CCW coordinates in a positively oriented oblique basis.
 for R,T in [(P,Q),(Q,P)]:
  for k,p in enumerate(R):
   d=sub(R[(k+1)%6],p)
   if all(cross(d,sub(t,p))<=0 for t in T):return True
 return False
A=[2,1,2,1,2,1];B=[2,2,3,1,3,2]
states=[]
for name,base in [('A',A),('B',B)]:
 for r in range(6):
  for eps in [-1,1]:
   ls=[base[(r+eps*k)%6] for k in range(6)]
   states.append(dict(name=name,r=r,eps=eps,ls=ls,q=poly(ls)))
P=poly(B)
candidates=[]
for k in range(6):
 row=[]
 for st in states:
  if st['ls'][(k+3)%6]!=B[k]:continue
  shift=sub(P[k],st['q'][(k+4)%6])
  Q=[add(p,shift) for p in st['q']]
  assert disjoint(P,Q)
  row.append(dict(**st,shift=shift,Q=Q))
 candidates.append(row)
count=0;first=None
# Domain: every 12-state orientation of each of two symbols on the six
# neighbors of this single B, with all six ring seams and disjoint interiors.
def visit(path):
 global count,first
 k=len(path)
 if k==6:
  if path[-1]['ls'][1]!=path[0]['ls'][4]:return
  count+=1
  if first is None:first=[{z:st[z] for z in ['name','r','eps','shift']} for st in path]
  return
 for st in candidates[k]:
  if k and path[-1]['ls'][(k+1)%6]!=st['ls'][(k+4)%6]:continue
  if any(not disjoint(st['Q'],v['Q']) or not no_T(st['Q'],v['Q']) for v in path):continue
  visit(path+[st])
visit([])
result=dict(domain='one fixed B plus its six full-side neighbors; 24 states per neighbor; no outer extension',candidates=[len(c) for c in candidates],labeled_coronas=count,first=first)
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
