"""Independent exact check: no author imports; raw mathematical definitions.
Manual full-cone proof audit is in branching-hexagon-rational-deformation-review.md.
"""
import json
from pathlib import Path
from itertools import product, combinations
from sage.all import QQ, PolynomialRing, vector, matrix, floor, ceil
S=PolynomialRing(QQ,names=("a","c","r"));a,c,r=S.gens()
vec=lambda x,y:vector(S,(x,y))
E=[vec(a,0),vec(527*a/625,336*a/625),vec(-3*c/5,4*c/5),
   vec(6*c/5-1327*a/625,264*a/625),vec(-3*c/5,-4*c/5),vec(7*a/25,-24*a/25)]
F=[vec(117*r/125,-44*r/125),-E[4],
   vec(1679*a/625-9*c/5-117*r/125,672*a/625-4*c/5+44*r/125),E[3],-E[1],E[5]]

def verts(edges):
    out=[vec(0,0)]
    for d in edges:out.append(out[-1]+d)
    assert out[-1]==out[0]
    return out[:-1]
A,B=verts(E),verts(F)
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
area=lambda p:sum(cross(x,y) for x,y in zip(p,p[1:]+p[:1]))/2
u=vec(39*a/25+117*r/125,-48*a/25-44*r/125)
v=vec(1679*a/625-3*c/5,672*a/625+4*c/5)
faces=[A,[E[0]-x for x in A],[E[0]-A[5]+x for x in B],[A[5]-x for x in B]]
seams=[(0,0,1,0,0,0),(0,2,1,2,0,1),(2,0,3,0,1,0),(2,2,3,2,1,1),
       (0,1,2,4,0,0),(1,1,3,4,0,0),(0,3,3,3,0,1),(1,3,2,3,0,-1),
       (0,4,2,1,-1,0),(1,4,3,1,1,0),(0,5,3,5,0,0),(1,5,2,5,0,0)]
parent={(i,j):(i,j) for i,j in product(range(4),range(6))}
def find(x):
    while parent[x]!=x:x=parent[x]
    return x
def union(x,y):parent[find(x)]=find(y)
mate={}
for f,i,g,j,n,m in seams:
    shift=n*u+m*v
    assert faces[f][i]-faces[g][(j+1)%6]==shift
    assert faces[f][(i+1)%6]-faces[g][j]==shift
    union((f,i),(g,(j+1)%6));union((f,(i+1)%6),(g,j))
    mate[f,i]=(g,j,shift);mate[g,j]=(f,i,-shift)
assert len(mate)==24
classes={}
for x in parent:classes.setdefault(find(x),set()).add(x)
assert len(classes)==8 and all(len(x)==3 for x in classes.values())
# Check each actual link independently of DSU and its exact translational holonomy.
for group in classes.values():
    start=min(group);curr=start;seen=set();total=vec(0,0)
    while curr not in seen:
        seen.add(curr);f,j,t=mate[curr];total+=t;curr=(f,(j+1)%6)
    assert curr==start and seen==group and total==vec(0,0)
Q=2670*a*a-2929*a*c+275*a*r+750*c*c-330*c*r
assert cross(F[1],F[2])==4*c*(-47*a+30*c+30*r)/125
assert cross(F[2],F[3])==4*Q/3125
assert cross(E[2],E[3])==c*(4516*a-3000*c)/3125
assert cross(u,v)==2*area(A)+2*area(B)
Rot=matrix(S,[[-QQ(7)/25,QQ(24)/25],[-QQ(24)/25,-QQ(7)/25]])
Ref=matrix(S,[[-QQ(527)/625,-QQ(336)/625],[-QQ(336)/625,QQ(527)/625]])
assert Rot*Rot.transpose()==matrix.identity(S,2) and Rot.det()==1
assert Ref*Ref.transpose()==matrix.identity(S,2) and Ref.det()==-1
G=[E[0]-B[5]+x for x in B]
branches=[[A,[E[0]-x for x in A],[B[5]-x for x in B],G],
          [A,[Rot*x for x in B],[Ref*x for x in B],G]]
contacts=[[(0,0,1,0),(0,5,2,5),(1,1,2,4),(0,1,3,4),(1,5,3,5)],
          [(0,0,1,5),(0,5,2,5),(1,0,2,0),(0,1,3,4),(1,4,3,5)]]
for patch,rows in zip(branches,contacts):
    for i,j,k,l in rows:
        assert {tuple(patch[i][j]),tuple(patch[i][(j+1)%6])}=={tuple(patch[k][l]),tuple(patch[k][(l+1)%6])}
# Fixed fixture lies strictly in every full-cone condition.
par=(QQ(1),QQ(3)/4,QQ(3)/2)
evalv=lambda z:vector(QQ,[QQ(t(*par)) for t in z])
assert 750*par[1]<1129*par[0] and 30*(par[1]+par[2])>47*par[0] and Q(*par)>0
polyA,polyB=([evalv(z) for z in T] for T in (A,B))
for T in (polyA,polyB):
    for i in range(6):
        for j in range(6):
            if j not in (i,(i+1)%6):assert cross(T[(i+1)%6]-T[i],T[j]-T[i])>0

def disjoint(P,T):
    for shape in (P,T):
        for i in range(6):
            d=shape[(i+1)%6]-shape[i]
            pp=[cross(d,x) for x in P];tt=[cross(d,x) for x in T]
            if max(pp)<=min(tt) or max(tt)<=min(pp):return True
    return False
U,V=evalv(u),evalv(v)
L=matrix(QQ,[list(U),list(V)]).transpose(); inv=L.inverse()
motif=[[evalv(z) for z in T] for T in faces]
coords=[[inv*z for z in T] for T in motif]
checks=[]
for i,j in product(range(4),repeat=2):
    bounds=[(ceil(min(x[k] for x in coords[i])-max(x[k] for x in coords[j])),
             floor(max(x[k] for x in coords[i])-min(x[k] for x in coords[j]))) for k in (0,1)]
    for n,m in product(range(int(bounds[0][0]),int(bounds[0][1])+1),range(int(bounds[1][0]),int(bounds[1][1])+1)):
        if i==j and n==m==0:continue
        assert disjoint(motif[i],[z+n*U+m*V for z in motif[j]])
        checks.append([i,j,n,m])
assert len(checks)==24
for branch in branches:
    fixture=[[evalv(z) for z in T] for T in branch]
    for i,j in combinations(range(4),2):assert disjoint(fixture[i],fixture[j])
# Independent exhaustive intrinsic symmetry check at fixture.
for T in (polyA,polyB):
    dd=lambda i,j:sum(t*t for t in T[i]-T[j])
    good=[(sign,off) for sign in (-1,1) for off in range(6)
          if all(dd(i,j)==dd((off+sign*i)%6,(off+sign*j)%6) for i,j in product(range(6),repeat=2))]
    assert good==[(1,0)]
# Parse retained output only for comparison, never import author producer.
cert=json.loads(Path("research/certificates/branching-hexagon-rational-deformation.json").read_text())
for key,value in (("edges_A",E),("edges_B",F),("vertices_A",A),("vertices_B",B)):
    assert [[S(x) for x in row] for row in cert[key]]==[list(x) for x in value]
assert [S(x) for x in cert["period_u"]]==list(u)
assert [S(x) for x in cert["period_v"]]==list(v)
assert cert["complete_lattice_comparisons"]==checks
assert {frozenset(map(tuple,row)) for row in cert["vertex_links"]}=={frozenset(row) for row in classes.values()}
print("PASS: independent 3D identities, 8 actual links, 10 branch contacts, 24 complete lattice/12 branch separations, certificate comparison")
