#!/usr/bin/env python3
"""Exact 3D non-affine branching hexagon cone. Default is nondestructive."""
import argparse
import json
import platform
import sys
from sage.all import QQ, PolynomialRing, matrix, vector, ceil, floor, sqrt

R = PolynomialRing(QQ, names=("a", "c", "r"))
a, c, r = R.gens()
V = lambda x,y: vector(R,[x,y])
cross = lambda x,y: x[0]*y[1]-x[1]*y[0]
E = [V(a,0), V(527*a/625,336*a/625), V(-3*c/5,4*c/5), None,
     V(-3*c/5,-4*c/5), V(7*a/25,-24*a/25)]
E[3] = -sum((e for e in E if e is not None), V(0,0))
F0 = V(117*r/125,-44*r/125)
F = [F0,-E[4],E[1]+E[4]-E[3]-E[5]-F0,E[3],-E[1],E[5]]
def vertices(edges):
    out=[V(0,0)]
    for e in edges: out.append(out[-1]+e)
    assert out[-1] == out[0]
    return out[:-1]
A,B = vertices(E),vertices(F)
u=E[0]+F0-2*A[5]
v=E[0]+2*E[1]+E[2]
faces=[A,[E[0]-x for x in A],[E[0]-A[5]+x for x in B],
       [A[5]-x for x in B]]
seams=[(0,0,1,0,(0,0)),(0,2,1,2,(0,1)),(2,0,3,0,(1,0)),
       (2,2,3,2,(1,1)),(0,1,2,4,(0,0)),(1,1,3,4,(0,0)),
       (0,3,3,3,(0,1)),(1,3,2,3,(0,-1)),(0,4,2,1,(-1,0)),
       (1,4,3,1,(1,0)),(0,5,3,5,(0,0)),(1,5,2,5,(0,0))]
paired={}
for f,i,g,j,(n,m) in seams:
    shift=n*u+m*v
    assert faces[f][i] == faces[g][(j+1)%6]+shift
    assert faces[f][(i+1)%6] == faces[g][j]+shift
    paired[(f,i)]=(g,j)
    paired[(g,j)]=(f,i)
assert len(paired)==24
seen=set();links=[]
for corner in sorted(paired):
    if corner in seen: continue
    link=[]; x=corner
    while x not in seen:
        seen.add(x);link.append(x)
        g,j=paired[x];x=(g,(j+1)%6)
    assert x==corner and len(link)==3
    links.append(link)
assert len(links)==8
area=lambda P:sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2
assert cross(u,v)==2*area(A)+2*area(B)
assert cross(F[1],F[2])==4*c*(-47*a+30*c+30*r)/125
assert cross(F[2],F[3])==4*(2670*a*a-2929*a*c+275*a*r+750*c*c-330*c*r)/3125
assert cross(E[2],E[3])==c*(4516*a-3000*c)/3125

# Fixed rotations/reflection realizing the second physical branch.
Rot=matrix(R,[[-QQ(7)/25,QQ(24)/25],[-QQ(24)/25,-QQ(7)/25]])
Ref=matrix(R,[[-QQ(527)/625,-QQ(336)/625],[-QQ(336)/625,QQ(527)/625]])
assert Rot.transpose()*Rot==matrix.identity(R,2)
assert Ref.transpose()*Ref==matrix.identity(R,2)
assert Rot.det()==1 and Ref.det()==-1
assert Rot*B[5]==E[0] and Ref*E[5]==E[5]
right=[E[0]-B[5]+x for x in B]
branches={"A_mate":[A,[E[0]-x for x in A],[B[5]-x for x in B],right],
          "B_mate":[A,[Rot*x for x in B],[Ref*x for x in B],right]}
branch_contacts={"A_mate":[(0,0,1,0),(0,5,2,5),(1,1,2,4),(0,1,3,4),(1,5,3,5)],
                 "B_mate":[(0,0,1,5),(0,5,2,5),(1,0,2,0),(0,1,3,4),(1,4,3,5)]}
for name,contacts in branch_contacts.items():
    P=branches[name]
    for f,i,g,j in contacts:
        assert {tuple(P[f][i]),tuple(P[f][(i+1)%6])} == {tuple(P[g][j]),tuple(P[g][(j+1)%6])}

fixture=(QQ(1),QQ(3)/4,QQ(3)/2)
sub=lambda z:QQ(z(*fixture))
subv=lambda x:vector(QQ,[sub(z) for z in x])
Af,Bf=([subv(x) for x in P] for P in [A,B])
uf,vf=subv(u),subv(v)
ff=[[subv(x) for x in P] for P in faces]
def convex(P):
    for i in range(6):
        e=P[(i+1)%6]-P[i]
        for j in range(6):
            if j not in (i,(i+1)%6): assert cross(e,P[j]-P[i])>0
convex(Af);convex(Bf)
def separated(P,Q):
    for T in [P,Q]:
        for i in range(6):
            e=T[(i+1)%6]-T[i];normal=vector(QQ,[-e[1],e[0]])
            pp=[normal.dot_product(z) for z in P];qq=[normal.dot_product(z) for z in Q]
            if max(pp)<=min(qq) or max(qq)<=min(pp):return True
    return False
lattice=matrix(QQ,[[uf[0],vf[0]],[uf[1],vf[1]]])
inv=lattice.inverse();qfaces=[[inv*x for x in P] for P in ff]
comparisons=[]
for i in range(4):
    for j in range(4):
        bounds=[]
        for k in range(2):
            lo=ceil(min(x[k] for x in qfaces[i])-max(x[k] for x in qfaces[j]))
            hi=floor(max(x[k] for x in qfaces[i])-min(x[k] for x in qfaces[j]))
            bounds.append((int(lo),int(hi)))
        for n in range(bounds[0][0],bounds[0][1]+1):
            for m in range(bounds[1][0],bounds[1][1]+1):
                if i==j and n==m==0:continue
                assert separated(ff[i],[x+n*uf+m*vf for x in ff[j]])
                comparisons.append([i,j,n,m])
branch_comparisons=[]
for name,P in branches.items():
    P=[[subv(x) for x in T] for T in P]
    for i in range(4):
        for j in range(i+1,4):
            assert separated(P[i],P[j]);branch_comparisons.append([name,i,j])
def symmetries(P):
    dist=lambda i,j:(P[i]-P[j]).dot_product(P[i]-P[j])
    result=[]
    for sign in [-1,1]:
        for off in range(6):
            if all(dist(i,j)==dist((off+sign*i)%6,(off+sign*j)%6) for i in range(6) for j in range(6)):
                result.append([sign,off])
    return result
assert symmetries(Af)==[[1,0]] and symmetries(Bf)==[[1,0]]
lengths=lambda edges:[str(sub(x.dot_product(x))) for x in edges]
assert len(set(lengths(E)))==3 and len(set(lengths(F)))==5
AA=lengths(E);BB=lengths(F)
assert len(set(AA+BB))==5
# Corner graph obstruction, and its finite triangle inventory.
from itertools import combinations_with_replacement
labels_A=["a","a","c","b","c","a"]
labels_B=["r","c","s","b","a","a"]
def graph(word):return {tuple(sorted((word[i-1],word[i]))) for i in range(6)}
gA,gB=graph(labels_A),graph(labels_B)
def stars(g,labels):
    return [list(t) for t in combinations_with_replacement(labels,3)
            if all(tuple(sorted(pair)) in g for pair in [(t[0],t[1]),(t[1],t[2]),(t[2],t[0])])]
all_labels=["a","b","c","r","s"]
assert not any("b" in t for t in stars(gA,all_labels))
assert not any("r" in t and "c" in t for t in stars(gB,all_labels))

def encode(x):return [str(z) for z in x]
certificate={"scope":"three-parameter sufficient periodic cone; non-affine, irrational-angle physical branching; not unrestricted classification",
 "parameters":["a","c","r"],"domain":["a>0","c>0","r>0","750*c<1129*a","30*(c+r)>47*a","2670*a^2-2929*a*c+275*a*r+750*c^2-330*c*r>0"],
 "edges_A":[encode(x) for x in E],"edges_B":[encode(x) for x in F],
 "vertices_A":[encode(x) for x in A],"vertices_B":[encode(x) for x in B],
 "period_u":encode(u),"period_v":encode(v),"seams":[list(z[:4])+[list(z[4])] for z in seams],
 "vertex_links":[[list(z) for z in L] for L in links],"area_A":str(area(A)),"area_B":str(area(B)),
 "branch_rotation":[encode(row) for row in Rot.rows()],"branch_reflection":[encode(row) for row in Ref.rows()],
 "branch_contacts":{k:[list(x) for x in v] for k,v in branch_contacts.items()},
 "fixture":{"parameters":[str(x) for x in fixture],"A":[encode(x) for x in Af],"B":[encode(x) for x in Bf],
 "u":encode(uf),"v":encode(vf),"squared_side_lengths_A":AA,"squared_side_lengths_B":BB,
 "intrinsic_symmetries_A":symmetries(Af),"intrinsic_symmetries_B":symmetries(Bf)},
 "complete_lattice_comparisons":comparisons,"complete_branch_comparisons":branch_comparisons,
 "complete_length_stars":stars(gA|gB,all_labels),
 "software":{"python":platform.python_version(),"sage":__import__("sage.env",fromlist=["SAGE_VERSION"]).SAGE_VERSION}}
parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
out=json.dumps(certificate,indent=2,sort_keys=True)+"\n"
if args.output:
    with open(args.output,"w") as f:f.write(out)
else:sys.stdout.write(out)
print(f"PASS: 12 polynomial seams, 8 trivalent links, {len(comparisons)} complete lattice separations, 12 branch separations",file=sys.stderr)
