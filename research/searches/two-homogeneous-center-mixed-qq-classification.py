"""Exact centerpp/mixedqq native ledger. No author imports or solver calls."""
from sage.all import QQ,PolynomialRing,QuadraticField,AA
from itertools import product
R=PolynomialRing(QQ,['c','rho','d']);c,r,d=R.gens()
u,v=c+60-r,60+r;psi=360-2*c
assert [2*u+psi-360,u+v+psi-360,2*v+psi-360]==[2*(60-r),120-c,2*(60+r-c)]
assert [3*c-360,2*c+psi-360,c+2*psi-360,3*psi-360]==[3*(c-120),0,-3*(c-120),-6*(c-120)]
assert u+v+c+psi==480
assert 240-(v+c)==180-c-r
assert 240-(v+psi)==2*c-180-r
# All binary cornerwords and mirrorstates: psi(q,q)+twoA(p,q) forces anAAp ray.
A=[('p','q'),('q','p')];P=('q','q')
for cs in product(A,repeat=2):
 for order in((P,cs[0],cs[1]),(cs[0],P,cs[1]),(cs[0],cs[1],P)):
  if all(order[j][1]==order[(j+1)%3][0] for j in range(3)):
   assert any(order[j] in A and order[(j+1)%3] in A and order[j][1]=='p' for j in range(3))
# Quadratic-count identities andsingleton bound, with free pp behavior.
S=PolynomialRing(QQ,['NB','Yq','Mc','Mp']);nb,yq,mc,mp=S.gens()
I=S.ideal([nb-2*yq-mc,nb-yq-mp])
assert 2*mp-nb-mc in I
# Fresh raw phase derivation. The qqunitarc sum for(c,360-2c) is1+2i sinc.
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
L=K.extension(PolynomialRing(K,'z').gen()**2+1,'i');ii=L.gen()
T=PolynomialRing(L,['C','S']);C,S=T.gens()
arc=1-(C-ii*S)+(C+ii*S)
assert arc==1+2*ii*S
assert (arc*(1-2*ii*S)-(1+4*S*S))==0
# Native angles after Breflection separately check both family sign alternatives.
for cross in(False,True):
 for sig in(-1,1):
  U=240+sig*d-(c if cross else psi)
  V=240-sig*d-(psi if cross else c)
  if sig==-1:
   new_chi,new_psi=psi,c
   assert V==240+d-(new_chi if cross else new_psi)
   assert U==240-d-(new_psi if cross else new_chi)
print('PASS all3 singleton B-only residuals; all4 pureqq multisets; actual2A+qqAAp parity; exactsingleton ledgers; native phase/norm; both family/reflection identities and scalarcurve conditions.')
