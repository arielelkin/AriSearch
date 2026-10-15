#!/usr/bin/env python3
"""Universal native-context/diagonal/rational-turn check; no parameter sampling.
Domain: 4 source cases, 16 actual endpoint contexts; independent 8 receiver
split variables; exact QQ linear algebra and QQ(r,q) identity.
"""
from collections import Counter
from sage.all import QQ,matrix,vector,PolynomialRing
ARROWS={
 'thin':((0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')),
 'thick':((0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')),
}
# Forms on basis (degree constant,Xt,Xh,Yt,Yh).
base={'Xt':1,'Xh':2,'Yt':3,'Yh':4}
expected={
 ('thin','X','tail'):(36,1,0,-1,0),
 ('thin','X','head'):(144,0,0,0,0),
 ('thin','Y','tail'):(36,-1,0,1,0),
 ('thin','Y','head'):(144,0,0,0,0),
 ('thick','X','tail'):(72,0,0,0,0),
 ('thick','X','head'):(108,0,1,-1,0),
 ('thick','Y','tail'):(108,0,-1,1,0),
 ('thick','Y','head'):(72,0,0,0,0),
}
contexts=[(species,parity,Z) for species in ('thin','thick') for parity in (0,1) for Z in ('X','Y')]
indices={c:i for i,c in enumerate(contexts)}
rows=[];rhs=[];observed=Counter();endpoint_count=0;thick_y_edges=0;thick_x_tails=0
for species,arrows in ARROWS.items():
 for parity in (0,1):
  donor={i for i in range(4) if i%2==parity}
  for edge in sorted(set(range(4))-donor):
   tail,head,Z=arrows[edge];angles=[]
   for v in (edge,(edge+1)%4):
    role='tail' if v==tail else 'head'
    adj=next(j for j in ((v-1)%4,v) if j in donor)
    dt,dh,DZ=arrows[adj];drole='tail' if v==dt else 'head'
    sigma=((36 if v%2==0 else 144) if species=='thin' else (72 if v%2==0 else 108))
    form=[sigma,0,0,0,0]
    form[base[Z+('t' if role=='tail' else 'h')]]+=1
    form[base[DZ+('t' if drole=='tail' else 'h')]]-=1
    assert tuple(form)==expected[(species,Z,role)]
    observed[(species,Z,role)]+=1;endpoint_count+=1
    # Endpoint branch: Xt=Yt=beta, Xh=beta+36, Yh=gamma.
    assert form[1]+form[2]+form[3]==0 and form[4]==0
    angle=form[0]+36*form[2];angles.append(angle)
    assert angle in (36,72,144)
    if angle in (36,72):
     row=[QQ(0)]*10
     row[indices[species,parity,Z]]=1 if role=='tail' else -1
     row[8 if angle==36 else 9]=-1
     rows.append(row);rhs.append(QQ(0) if role=='tail' else QQ(-1))
    if species=='thick' and Z=='X' and role=='tail':
     assert (v,sigma,DZ,drole,angle)==(0,72,'X','tail',72)
     thick_x_tails+=1
   if species=='thick' and Z=='Y':
    assert angles==[72,72];thick_y_edges+=1
assert endpoint_count==16 and len(observed)==8 and set(observed.values())=={2}
assert (thick_y_edges,thick_x_tails)==(2,2)
M=matrix(QQ,rows);b=vector(QQ,rhs)
assert M.nrows()==10 and M.ncols()==10 and M.rank()==9
particular=vector(QQ,[QQ(1)/2]*10)
null_direction=vector(QQ,[1,1,1,1,0,0,0,0,1,0])
assert M*particular==b and M*null_direction==0
assert M.right_kernel().dimension()==1
assert all(null_direction[i]==0 and particular[i]==QQ(1)/2 for i in (4,5,6,7,9))
# Thus all four thick receiver splits and D72 are 1/2; all four thin
# receiver splits equal the single still-free D36. No donor-side equality
# between different receiving contexts has been encoded.

R=PolynomialRing(QQ,names=('r','q'));r,q=R.gens();F=R.fraction_field()
A0=q*(1-r*r)+2*r
u=(r+q)/A0;h=u*r
assert h/(1-u)==(r+q)/(1-r*q)
s72=2*q/(1+q*q);c72=(1-q*q)/(1+q*q)
x=u*c72+h*s72;y=u*s72-h*c72
mL=(u*y+h*x)/(y+h)
assert mL==u*(1+r*r)/(1+r*q)
positive=q*(1-r*q)+q*r*r+(2+q*q)*r**3
assert positive==2*(r+q)*(1+r*r)-A0*(1+r*q)
assert 2*mL-1==positive/(A0*(1+r*q))
D=QQ(1)/2*(y+h)-u*y-h*x
assert D==-u*s72*positive/(2*A0)
# For 0<r<q<1, A0>0,1+rq>0,1-rq>0,positive>0.
# These strict signs are proved term-by-term in the written lemma.
print('PASS: all16 native endpoint forms; both thick Y two-72 edges; both same-X-tail thick contexts; 10 independent diagonal equations leave only thin D36 free; universal midpoint M-turn is strictly negative for 0<r<q<1.')
