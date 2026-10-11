#!/usr/bin/env python3
"""No-author-import full-cone Cairo boundary checker; nondestructive."""
import json
from pathlib import Path
from sage.all import QQ,QuadraticField,PolynomialRing,vector,matrix,ceil,floor,AA
K=QuadraticField(3,"w");w=K.gen()
R=PolynomialRing(K,names=("a","c","d","D"));a,c,d,D=R.gens()
V=lambda x,y:vector(R,[x,y]);zero=V(0,0)
units=[V(1,0),V(0,1),V(-w/2,QQ(1)/2),V(-QQ(1)/2,-w/2),V(QQ(1)/2,-w/2)]
b=c+w*(d-a);bigB=a+w*(D-c);e=w*c+d-2*a;f=w*a+D-2*c
words=[(a,b,c,d,e),(c,bigB,a,D,f)]
def make(word):
 out=[zero]
 for L,unit in zip(word,units):out.append(out[-1]+L*unit)
 assert out[-1]==zero
 return out[:-1]
p,q=map(make,words)
S=matrix(R,[[-w/2,QQ(1)/2],[QQ(1)/2,w/2]])
assert S.transpose()*S==matrix.identity(R,2) and S.det()==-1
faces=[p,[p[4]-x for x in p],[S*(x-q[2])for x in q]]
faces.append([faces[2][4]+faces[2][0]-x for x in faces[2]])
p0,p1,q0,q1=faces
u=p1[0]-q1[2];v=p0[2]-q0[0]
assert u==V((a-3*w*c-d+w*D)/2,(-w*a+c+w*d+5*D)/2)
assert v==V((3*a-2*w*c+w*D)/2,(-w*a+2*w*d+3*D)/2)
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
area=lambda T:sum(cross(T[i],T[(i+1)%5])for i in range(5))/2
assert -cross(u,v)==2*area(p)+2*area(q)
whole=[(0,4,1,4,zero,False),(2,4,3,4,zero,False),
       (0,0,2,2,zero,True),(1,0,3,2,u,True),
       (0,2,2,0,v,True),(1,2,3,0,u-v,True)]
used=set()
for F,i,G,j,t,same in whole:
 assert (F,i)not in used and(G,j)not in used
 used.update([(F,i),(G,j)])
 if same:
  assert faces[F][i]==faces[G][j]+t and faces[F][(i+1)%5]==faces[G][(j+1)%5]+t
 else:
  assert faces[F][i]==faces[G][(j+1)%5]+t and faces[F][(i+1)%5]==faces[G][j]+t
assert {(F,i)for F in range(4)for i in range(5)}-used=={(F,i)for F in range(4)for i in[1,3]}
# Every directed bank chain, including its internal break, is expressed in
# one common origin/direction. Positivity handles all orders and equalities.
O=q0[4];n=V(0,1);total=b+D
assert q0[3]==p0[1]==O+D*n and p0[2]==O+total*n
assert p1[2]+v-u==O
assert p1[1]+v-u==q1[3]+v==O+b*n
assert q1[4]+v==O+total*n
O=v;n=V(-QQ(1)/2,-w/2);total=bigB+d
assert q0[2]+v==O
assert q0[1]+v==p0[3]==O+bigB*n and p0[4]==O+total*n
assert p1[4]+v==O
assert p1[3]+v==q1[1]+u==O+d*n and q1[2]+u==O+total*n
# Independent comparison against the retained certificate's polynomial data.
cert=json.loads(Path("research/certificates/partial-contact-cairo-swapped-arms-periodic.json").read_text())
decode=lambda x:vector(R,[R(z)for z in x])
assert [decode(x)for x in cert["P"]]==p
assert [decode(x)for x in cert["Q"]]==q
assert [[decode(x)for x in T]for T in cert["motifs"]]==faces
assert decode(cert["u"])==u and decode(cert["v"])==v
assert R(cert["area_P"])==area(p) and R(cert["area_Q"])==area(q)
# Full sign fixtures and both coalescence boundaries; no extrapolation of
# these finite checks supplies the symbolic proof.
fixtures=[("author",(1,2,3,4)),("reverse_signs",(3,3,2,2)),
          ("positive_positive",(3,3,5,QQ(7)/2)),("negative_negative",(3,3,QQ(7)/2,5)),
          ("b_equals_D",(1,2,3,2+2*w)),("d_equals_B",(1,2,1+2*w,4)),
          ("both_equal",(1,QQ(6)/5,1,QQ(6)/5))]
def numeric(z,pars):return K(z(*[K(x)for x in pars]))
def numeric_vector(z,pars):return vector(K,[numeric(x,pars)for x in z])
def disjoint(P,Q):
 for T in[P,Q]:
  for i in range(5):
   edge=T[(i+1)%5]-T[i];pp=[AA(cross(edge,x))for x in P];qq=[AA(cross(edge,x))for x in Q]
   if max(pp)<=min(qq)or max(qq)<=min(pp):return True
 return False
summaries=[]
for name,pars in fixtures:
 forms=[numeric(z,pars)for z in(a,c,d,D,b,bigB,e,f)]
 assert all(AA(z)>0 for z in forms),(name,forms)
 polygons=[[numeric_vector(z,pars)for z in T]for T in[p,q]]
 for T in polygons:
  for i in range(5):
   for j in range(5):
    if j not in[i,(i+1)%5]:assert AA(cross(T[(i+1)%5]-T[i],T[j]-T[i]))>0
 mf=[[numeric_vector(z,pars)for z in T]for T in faces]
 U,W=numeric_vector(u,pars),numeric_vector(v,pars)
 assert AA(-cross(U,W))>0
 inv=matrix(K,[[U[0],W[0]],[U[1],W[1]]]).inverse();lf=[[inv*z for z in T]for T in mf]
 comparisons=[]
 for i in range(4):
  for j in range(4):
   bounds=[]
   for k in range(2):
    lo=ceil(min(AA(x[k])for x in lf[i])-max(AA(x[k])for x in lf[j]))
    hi=floor(max(AA(x[k])for x in lf[i])-min(AA(x[k])for x in lf[j]))
    bounds.append((int(lo),int(hi)))
   for n in range(bounds[0][0],bounds[0][1]+1):
    for m in range(bounds[1][0],bounds[1][1]+1):
     if i==j and n==m==0:continue
     assert disjoint(mf[i],[x+n*U+m*W for x in mf[j]]),(name,i,j,n,m)
     comparisons.append([i,j,n,m])
 if name=="author":assert comparisons==cert["complete_lattice_comparisons"]
 sign=lambda z:0 if z==0 else(1 if AA(z)>0 else -1)
 summaries.append((name,sign(numeric(b-D,pars)),sign(numeric(d-bigB,pars)),len(comparisons)))
assert set((x[1],x[2])for x in summaries[:4])=={(1,-1),(-1,1),(1,1),(-1,-1)}
assert summaries[4][1]==0 and summaries[5][2]==0 and summaries[6][1:3]==(0,0)
print("PASS: independent full4D closure, six seams, two oriented interval chains, area identity, certificate agreement")
print("PASS: seven exact order/coalescence fixtures",summaries)
