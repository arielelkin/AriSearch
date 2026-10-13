#!/usr/bin/env python3
"""Exact singleton bevelled-chair check; no search-domain enlargement."""
from fractions import Fraction as F
import json
import argparse
from pathlib import Path
S=(F(1,6),F(1,3)); R=(F(1),F(1))
P=[S,(F(1,2),F(0)),(F(2),F(0)),(F(2),F(1)),R]
Q=[S,R,(F(1),F(2)),(F(0),F(2)),(F(0),F(1,2))]
C=[(F(1,2),F(0)),(F(2),F(0)),(F(2),F(1)),R,(F(1),F(2)),(F(0),F(2)),(F(0),F(1,2))]
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(v): return sum(cross(v[i],v[(i+1)%len(v)]) for i in range(len(v)))/2
def convex(v): return all(cross(sub(v[(i+1)%len(v)],v[i]),sub(v[(i+2)%len(v)],v[(i+1)%len(v)]))>0 for i in range(len(v)))
def contains(v,p): return all(cross(sub(v[(i+1)%len(v)],v[i]),sub(p,v[i]))>0 for i in range(len(v)))
def disjoint(a,b):
    for v in (a,b):
        for i in range(len(v)):
            e=sub(v[(i+1)%len(v)],v[i])
            pa=[cross(e,x) for x in a]; pb=[cross(e,x) for x in b]
            if max(pa)<=min(pb) or max(pb)<=min(pa): return True
    return False
hp=lambda p:(4-p[0],1-p[1])
H=[S,P[1],hp(R),hp(S),hp(P[1]),R]
u=sub(H[2],H[0]); v=sub(H[4],H[0]); det=cross(u,v)
inv=lambda x:(cross(x,v)/det,cross(u,x)/det)
bounds=[max(abs(inv(sub(a,b))[k]) for a in H for b in H) for k in range(2)]
assert convex(P) and convex(Q) and convex(H)
assert area(P)!=area(Q) # sufficient for distinct congruence classes
assert area(P)+area(Q)==area(C)
assert area(H)==2*area(P)==det
assert disjoint(P,[hp(p) for p in P])
assert all(x<3 for x in bounds)
checks=[]
for i in range(-2,3):
    for j in range(-2,3):
        if not (i or j): continue
        t=(i*u[0]+j*v[0],i*u[1]+j*v[1])
        assert disjoint(H,[add(p,t) for p in H])
        checks.append([i,j])
w=(F(3,4),F(1,16))
assert contains(P,w) and w[0]+w[1]<1
rot=lambda p:(-p[1],p[0])
negrot=lambda p:(p[1],-p[0])
children=[C,[add(p,(1,1)) for p in C],[add(rot(p),(4,0)) for p in C],[add(negrot(p),(0,4)) for p in C]]
assert sum(area(c) for c in children)==4*area(C)
def enc(p): return [str(x) for x in p]
result={"status":"CERTIFIED_FIXED_SCHEME_FALSIFIED","P":list(map(enc,P)),"Q":list(map(enc,Q)),"C":list(map(enc,C)),"areas":{"P":str(area(P)),"Q":str(area(Q)),"C":str(area(C)),"carrier":str(area(H))},"P_carrier":list(map(enc,H)),"lattice":[enc(u),enc(v)],"inverse_difference_bounds":list(map(str,bounds)),"disjoint_lattice_neighbors":checks,"extension_children":[list(map(enc,c)) for c in children],"extension_protrusion_point":enc(w),"finite_domain":"one exact pair; four fixed chair placements; 24 carrier-neighbor checks","repair_count":0}
parser=argparse.ArgumentParser(); parser.add_argument('--output'); parser.add_argument('--check'); args=parser.parse_args()
if args.check: assert result==json.loads(Path(args.check).read_text())
if args.output: Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":result["status"],"areas":result["areas"],"lattice":result["lattice"],"checks":len(checks)},sort_keys=True))
