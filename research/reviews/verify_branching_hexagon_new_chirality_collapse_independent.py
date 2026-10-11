"""No author imports: independent exact chirality fixture/monohedral checker."""
import json
from pathlib import Path
from itertools import product,combinations
from sage.all import AA,QQ,PolynomialRing,NumberField,vector,matrix,ceil,floor
T=PolynomialRing(QQ,"t");t=T.gen()
K=NumberField(t**4-10*t**2+1,"g",embedding=AA(2).sqrt()+AA(3).sqrt());g=K.gen()
h2=(g-1/g)/2;h3=(g+1/g)/2
assert QQ(31)/10<AA(g)<QQ(16)/5
V=lambda x,y:vector(K,(x,y));cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
c75=h2*(h3-1)/4;s75=h2*(h3+1)/4
EA=[V(QQ(1)/2,0),V(c75,s75),V(-QQ(1)/4,h3/4),V(-s75,-c75),V(-QQ(1)/4,-h3/4),V(h2/2,-h2/2)]
EB=[V(-QQ(1)/4-h3/2,-QQ(3)/2+h3/4),V(QQ(1)/4,-h3/4),V(1,0),V(h3/2,QQ(1)/2),V(0,1),V(-1,0)]
def verts(E):
 out=[V(0,0)]
 for x in E:out.append(out[-1]+x)
 assert out[-1]==out[0]
 return out[:-1]
A,B=verts(EA),verts(EB)
for P in(A,B):
 for i,j in product(range(6),repeat=2):
  if j not in(i,(i+1)%6):assert AA(cross(P[(i+1)%6]-P[i],P[j]-P[i]))>0
assert EB[2]==-EB[5]
assert [x.dot_product(x) for x in EA]==[QQ(1)/4,1,QQ(1)/4,1,QQ(1)/4,1]
assert [x.dot_product(x) for x in EB]==[QQ(13)/4-h3/2,QQ(1)/4,1,1,1,1]
for i in range(6):
 dot=EA[i-1].dot_product(EA[i]);den=K(QQ(1)/2)
 assert -dot/den==(-h2/2 if i%2==0 else -c75)
for i,expected in((3,-h3/2),(4,-K(1)/2),(5,K(0))):
 assert -EB[i-1].dot_product(EB[i])==expected
R45=matrix(K,[[h2/2,-h2/2],[h2/2,h2/2]])
R255=matrix(K,[[-c75,s75],[-s75,-c75]])
x=V(QQ(1)/2,0)
patches=[[A,[x-z for z in A],[R45*(z-B[4]) for z in B],[x-R45*(z-B[4]) for z in B]],
         [A,[V(z[0],-z[1]) for z in A],[R45.transpose()*(z-B[5]) for z in B],[x+R255*(z-B[3]) for z in B]]]
contacts=[[(0,0,1,0),(0,5,2,4),(1,1,2,3),(0,1,3,3),(1,5,3,4)],
          [(0,0,1,0),(0,5,2,5),(1,5,2,4),(0,1,3,2),(1,1,3,3)]]
def disjoint(P,Q):
 for shape in(P,Q):
  for i in range(6):
   edge=shape[(i+1)%6]-shape[i]
   pv=[AA(cross(edge,z)) for z in P];qv=[AA(cross(edge,z)) for z in Q]
   if max(pv)<=min(qv) or max(qv)<=min(pv):return True
 return False
for patch,rows in zip(patches,contacts):
 for i,j,k,l in rows:
  assert {tuple(patch[i][j]),tuple(patch[i][(j+1)%6])}=={tuple(patch[k][l]),tuple(patch[k][(l+1)%6])}
 for i,j in combinations(range(4),2):assert disjoint(patch[i],patch[j])
u=B[2];v=B[3]+B[4]-B[1];faces=[B,[B[1]-z for z in B]]
seams=[(0,0,1,0,0,0),(0,1,1,1,1,0),(0,3,1,3,0,1),(0,4,1,4,-1,1),(0,2,0,5,1,0),(1,2,1,5,-1,0)]
paired={}
for i,j,k,l,n,m in seams:
 shift=n*u+m*v
 assert faces[i][j]==faces[k][(l+1)%6]+shift
 assert faces[i][(j+1)%6]==faces[k][l]+shift
 paired[i,j]=(k,l,shift);paired[k,l]=(i,j,-shift)
seen=set();links=[]
for start in sorted(paired):
 if start in seen:continue
 curr=start;group=[];shift=V(0,0)
 while curr not in group:
  group.append(curr);seen.add(curr);i,j,s=paired[curr];shift+=s;curr=i,(j+1)%6
 assert curr==start and len(group)==3 and shift==V(0,0);links.append(group)
assert len(links)==4
area=sum(cross(B[i],B[(i+1)%6]) for i in range(6))/2
assert cross(u,v)==2*area and AA(area)>0
inv=matrix(K,[list(u),list(v)]).transpose().inverse();qfaces=[[inv*z for z in P] for P in faces]
checks=[]
for i,j in product(range(2),repeat=2):
 bounds=[(ceil(min(AA(z[k]) for z in qfaces[i])-max(AA(z[k]) for z in qfaces[j])),floor(max(AA(z[k]) for z in qfaces[i])-min(AA(z[k]) for z in qfaces[j]))) for k in(0,1)]
 for n,m in product(range(int(bounds[0][0]),int(bounds[0][1])+1),range(int(bounds[1][0]),int(bounds[1][1])+1)):
  if i==j and n==m==0:continue
  assert disjoint(faces[i],[z+n*u+m*v for z in faces[j]])
  checks.append([i,j,n,m])
assert len(checks)==16
cert=json.loads(Path("research/certificates/branching-hexagon-new-chirality-collapse.json").read_text())
for key,p in(("A",A),("B",B)):
 assert [vector(K,[K(z) for z in row]) for row in cert[key]]==p
assert vector(K,[K(z) for z in cert["period_u"]])==u
assert vector(K,[K(z) for z in cert["period_v"]])==v
assert cert["complete_lattice_comparisons"]==checks
assert {frozenset(map(tuple,L)) for L in cert["links"]}=={frozenset(L) for L in links}
print("PASS: independent exact angles/10 branch contacts/12 branch separations/6 mono seams/4 zero-holonomy links/16 complete lattice comparisons")
