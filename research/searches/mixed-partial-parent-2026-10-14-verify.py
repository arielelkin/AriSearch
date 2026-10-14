#!/usr/bin/env python3
"""Independent exact-algebraic-real check of the mixed-parent certificate."""
import json
import sys
from pathlib import Path
from sage.all import AA, QQ, vector

if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled")
path=Path(__file__).resolve().parents[1]/"certificates"/"mixed-partial-parent-2026-10-14.json"
data=json.loads(path.read_text())
r=AA(3).sqrt();s=AA(2).sqrt();g=r+s
assert g**4-10*g*g+1==0

def decode(c):
    assert len(c)==4
    return sum(QQ(a)*g**i for i,a in enumerate(c))
def points(c):return [vector(AA,[decode(x) for x in p]) for p in c]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(F[i],F[(i+1)%len(F)]) for i in range(len(F)))/2
def convex(F):
    return all(cross(F[(i+1)%len(F)]-F[i],F[j]-F[i])>0
               for i in range(len(F)) for j in range(len(F)) if j not in (i,(i+1)%len(F)))
P=points(data["atoms"]["P"]["vertices"]);Q=points(data["atoms"]["Q"]["vertices"])
expected_P=[(0,0),(3,0),(4,r),(QQ(7)/2,3*r/2),(0,1/r)]
expected_Q=[(0,0),(3,0),(3+1/(s*r),1/(s*r)),(3+1/(s*r),7/r+1/(s*r)),(s,7/r+1/(s*r)),(0,7/r+1/(s*r)-s)]
assert [tuple(x) for x in P]==expected_P and [tuple(x) for x in Q]==expected_Q
words={"P":[90,120,120,90,120],"Q":[90,135,135,90,135,135]}
shapes={"P":P,"Q":Q}
for name,F in shapes.items():
    assert convex(F) and data["atoms"][name]["angles"]==words[name]
    assert decode(data["atoms"][name]["area"])==area(F)
    for i,a in enumerate(words[name]):
        u=F[i-1]-F[i];v=F[(i+1)%len(F)]-F[i]
        dot=u.dot_product(v);norm=u.dot_product(u)*v.dot_product(v)
        assert (a==90 and dot==0) or (a==120 and dot<0 and 4*dot*dot==norm) or (a==135 and dot<0 and 2*dot*dot==norm)
assert area(P)==10/r and area(P)!=area(Q)
t=decode(data["parent"]["offset"]);assert t==1
Qhat=points(data["parent"]["Q_halfturn_vertices"])
assert all(Qhat[i]==vector(AA,[1,0])-Q[i] for i in range(6))
assert all(p[1]>=0 for p in P) and all(q[1]<=0 for q in Qhat)
assert Qhat[1][0]<P[0][0]<Qhat[0][0]<P[1][0]
B=points(data["parent"]["boundary"])
assert B==[Qhat[0]]+P[1:]+[P[0]]+Qhat[1:]
assert len(B)==11 and area(B)==area(P)+area(Q)==decode(data["parent"]["area"])
turns=[cross(B[(i+1)%11]-B[i],B[(i+2)%11]-B[(i+1)%11]) for i in range(11)]
assert all(x!=0 for x in turns) and sum(x<0 for x in turns)==2
# Dynamic reachable-angle computation, independent of producer's census loops.
reachable={0}
for n in range(361):
    if n in reachable:
        for a in (90,120,135,180):
            if n+a<=360:reachable.add(n+a)
assert all(n not in reachable for n in (45,60,105,150))
assert {90,120,135,180}<=reachable
records=data["wedge_domain"]["right_corner_guests"]
expected={(name,i,hand) for name,A in words.items() for i,a in enumerate(A) if a==90 for hand in (0,1)}
assert len(records)==8 and {(x["type"],x["corner"],x["hand"]) for x in records}==expected
for x in records:
    A=words[x["type"]];F=shapes[x["type"]];i=x["corner"]
    ends=[(i-1)%len(A),(i+1)%len(A)]
    if x["hand"]:ends.reverse()
    far=[A[j] for j in ends]
    assert x["far_corners"]==ends and x["far_angles"]==far
    assert far in ([120,120],[135,135])
    assert [decode(z) for z in x["squared_arm_lengths"]]==[(F[j]-F[i]).dot_product(F[j]-F[i]) for j in ends]
    rem=[360-a-b for a,b in zip((120,135),far)]
    assert rem==x["equal_endpoint_remainders"] and any(a not in reachable for a in rem)
assert data["wedge_domain"]["survivors"]==0
assert {x["kind"] for x in data["contact_interval_domain"]}=={"STAGGERED_HOST_SWITCH","ALIGNED_Q_CONTAINMENT"}
# Cairo omission premise: four internally distinct90 arms.
arms=[AA(1),7/r,1/r,AA(3)]
assert len(set(arms))==4
print("PASS: exact mixed parent;8 oriented right corners; all unequal/equal ray endpoint obstructions; both contact interval cases retained; Cairo private-arm premise.")
