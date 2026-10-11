#!/usr/bin/env python3
"""Exact two-chirality candidate and its certified monohedral periodic escape."""
import argparse,json,sys
from sage.all import AA,QQ,PolynomialRing,NumberField,vector,matrix,ceil,floor
P=PolynomialRing(QQ,"z");z=P.gen()
K=NumberField(z**4-10*z**2+1,"g",embedding=AA(2).sqrt()+AA(3).sqrt());g=K.gen()
h2=(g-1/g)/2;h3=(g+1/g)/2
assert h2*h2==2 and h3*h3==3 and AA(h2)>0 and AA(h3)>0
V=lambda x,y:vector(K,[x,y]);zero=V(0,0)
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
c75=h2*(h3-1)/4;s75=h2*(h3+1)/4
EA=[V(QQ(1)/2,0),V(c75,s75),V(-QQ(1)/4,h3/4),V(-s75,-c75),V(-QQ(1)/4,-h3/4),V(h2/2,-h2/2)]
EB=[V(-QQ(1)/4-h3/2,-QQ(3)/2+h3/4),V(QQ(1)/4,-h3/4),V(1,0),V(h3/2,QQ(1)/2),V(0,1),V(-1,0)]
def vertices(E):
 out=[zero]
 for e in E:out.append(out[-1]+e)
 assert out[-1]==zero
 return out[:-1]
A,B=vertices(EA),vertices(EB)
def convex(Q):
 for i in range(6):
  for j in range(6):
   if j not in [i,(i+1)%6]:assert AA(cross(Q[(i+1)%6]-Q[i],Q[j]-Q[i]))>0
convex(A);convex(B)
R45=matrix(K,[[h2/2,-h2/2],[h2/2,h2/2]])
Rm45=R45.transpose();R255=matrix(K,[[-c75,s75],[-s75,-c75]])
seamright=V(QQ(1)/2,0)
branches={"rotation_mate":[A,[seamright-x for x in A],[R45*(x-B[4]) for x in B],[seamright-R45*(x-B[4]) for x in B]],
 "reflection_mate":[A,[V(x[0],-x[1]) for x in A],[Rm45*(x-B[5]) for x in B],[seamright+R255*(x-B[3]) for x in B]]}
contacts={"rotation_mate":[(0,0,1,0),(0,5,2,4),(1,1,2,3),(0,1,3,3),(1,5,3,4)],
 "reflection_mate":[(0,0,1,0),(0,5,2,5),(1,5,2,4),(0,1,3,2),(1,1,3,3)]}
def separated(P,Q):
 for T in [P,Q]:
  for i in range(6):
   e=T[(i+1)%6]-T[i];n=V(-e[1],e[0]);p=[AA(n.dot_product(x)) for x in P];q=[AA(n.dot_product(x)) for x in Q]
   if max(p)<=min(q) or max(q)<=min(p):return True
 return False
for name,P in branches.items():
 for f,i,h,j in contacts[name]:
  assert {tuple(P[f][i]),tuple(P[f][(i+1)%6])}=={tuple(P[h][j]),tuple(P[h][(j+1)%6])}
 for i in range(4):
  for j in range(i+1,4):assert separated(P[i],P[j])
# Direct two-face monohedral quotient; no classification import.
u=B[2];v=B[3]+B[4]-B[1]
faces=[B,[B[1]-x for x in B]]
seams=[(0,0,1,0,(0,0)),(0,1,1,1,(1,0)),(0,3,1,3,(0,1)),(0,4,1,4,(-1,1)),(0,2,0,5,(1,0)),(1,2,1,5,(-1,0))]
paired={}
for f,i,h,j,(n,m) in seams:
 shift=n*u+m*v
 assert faces[f][i]==faces[h][(j+1)%6]+shift and faces[f][(i+1)%6]==faces[h][j]+shift
 paired[f,i]=h,j;paired[h,j]=f,i
links=[];seen=set()
for start in sorted(paired):
 if start in seen:continue
 x=start;link=[]
 while x not in seen:
  seen.add(x);link.append(x);h,j=paired[x];x=h,(j+1)%6
 assert x==start and len(link)==3
 links.append(link)
assert len(links)==4
area=lambda Q:sum(cross(Q[i],Q[(i+1)%6]) for i in range(6))/2
assert cross(u,v)==2*area(B) and AA(cross(u,v))>0
inv=matrix(K,[[u[0],v[0]],[u[1],v[1]]]).inverse()
qfaces=[[inv*x for x in Q]for Q in faces];comparisons=[]
for i in range(2):
 for j in range(2):
  bounds=[]
  for k in range(2):
   lo=ceil(min(AA(x[k]) for x in qfaces[i])-max(AA(x[k]) for x in qfaces[j]));hi=floor(max(AA(x[k]) for x in qfaces[i])-min(AA(x[k]) for x in qfaces[j]))
   bounds.append((int(lo),int(hi)))
  for n in range(bounds[0][0],bounds[0][1]+1):
   for m in range(bounds[1][0],bounds[1][1]+1):
    if i==j and n==m==0:continue
    assert separated(faces[i],[x+n*u+m*v for x in faces[j]])
    comparisons.append([i,j,n,m])
enc=lambda x:[str(y) for y in x]
cert={"scope":"two physically distinct A-mate chirality patches; exact candidate killed by monohedral B periodic escape",
 "field":{"polynomial":"g^4-10*g^2+1","isolating_interval":["31/10","16/5"],"sqrt2":"(g-1/g)/2","sqrt3":"(g+1/g)/2"},
 "A":[enc(x) for x in A],"B":[enc(x) for x in B],"squared_edges_A":[str(x.dot_product(x)) for x in EA],"squared_edges_B":[str(x.dot_product(x)) for x in EB],
 "branch_contacts":{k:[list(x)for x in vals]for k,vals in contacts.items()},"period_u":enc(u),"period_v":enc(v),"seams":[list(x[:4])+[list(x[4])]for x in seams],"links":[[list(x)for x in L]for L in links],"area_B":str(area(B)),"complete_lattice_comparisons":comparisons}
p=argparse.ArgumentParser();p.add_argument("--output");args=p.parse_args();out=json.dumps(cert,indent=2,sort_keys=True)+"\n"
if args.output:
 with open(args.output,"w")as f:f.write(out)
else:sys.stdout.write(out)
print(f"PASS: 12 whole-branch separations; 6 monohedral seams, 4 links, {len(comparisons)} complete lattice separations",file=sys.stderr)
