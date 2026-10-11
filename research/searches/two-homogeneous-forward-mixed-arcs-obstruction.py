"""Exact proof ledger for all four opposite-sign forward mixed-arc cases.
No solver/no imports of author modules. Review required for global assertions.
"""
from sage.all import QQ,PolynomialRing,QuadraticField,AA
from itertools import product
R=PolynomialRing(QQ,['d','h','z','c']);D,h,z,c=R.gens()
def ledger(x,y,h):
 u,v=y-h,x+h
 return [u+x,v+x,u+y,v+y],[2*u+x-360,u+v+x-360,2*v+x-360,2*u+y-360,u+v+y-360,2*v+y-360]
def choices(x,y,h):return [2*x-y+h,x-h],[y+h,2*y-x-h]
# All nonempty actual sign inventories: absence of opposite pair iff both one sign.
for sb in ({-1},{1},{-1,1}):
 for sp in ({-1},{1},{-1,1}):
  opposite=any(b==-q for b in sb for q in sp)
  assert opposite or sb==sp and len(sb)==1
# Case1:F1high,G1low; cases2:F2high,G2low.
x,y=120-h,120-h-D
F,G=choices(x,y,h);assert F[0]==120+D and G[0]==120-D
A,B=ledger(x,y,h)
assert A==[240-3*h-D,240-h,240-3*h-2*D,240-h-D]
assert B==[-5*h-2*D,-3*h-D,-h,-5*h-3*D,-3*h-2*D,-h-D]
assert (2*c-1)*(2*c+5)==4*c*c+8*c-5 # derivative bound on0<c<1/2
x,y=120+h+D,120+h
F,G=choices(x,y,h);assert F[1]==120+D and G[1]==120-D
A,B=ledger(x,y,h)
assert A==[240+h+D,240+3*h+2*D,240+h,240+3*h+D]
assert B==[h+D,3*h+2*D,5*h+3*D,h,3*h+D,5*h+2*D]
# At hdelta, only beta can fill AH; repeatedslotx has no nonhomogeneous star.
F,G=choices(120+2*D,120+D,D)
assert F==[120+4*D,120+D] and G==[120+2*D,120-D]
# Case3 and4: central mean120; exact lists retain every repeated mixedslot.
x,y=120+z,120-z
F,G=choices(x,y,h)
assert F[0]-G[1]==6*z+2*h and F[0]+G[1]==240
assert F[1]-G[0]==2*(z-h) and F[1]+G[0]==240
A,B=ledger(x,y,h)
assert A==[240-h,240+2*z+h,240-2*z-h,240+h]
assert B==[-z-2*h,z,3*z+2*h,-3*z-2*h,-z,z+2*h]
assert A[0]-(240-(3*z+h))==3*z
assert A[1]-(240+(3*z+h))==-z
# OppositeF2/G1delta z-h: two potentially surviving equalities hdelta needz2h.
assert A[0]-(240-(z-h))==z-2*h
assert A[3]-(240+(z-h))==2*h-z
# Raw exact tangent difference atx120+z,y120-z.
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
T=PolynomialRing(K,['C','S']);C,S=T.gens()
sx=w*C/2-S/2;sy=w*C/2+S/2
assert 2*(sy-sx)==2*S
assert (1+4*sx*sy-4*C*C) in T.ideal([C*C+S*S-1])
# Strict comparison h>z/2 andh<z on0<z<30: both factors have known signs.
assert 1+c-2*c*c==(1-c)*(2*c+1)
# Counteliminations: Yp+Yq=NB-NA; Mbetapsi=NB+NA. Zero repeatedslots ⇒NA0.
U=PolynomialRing(QQ,['NA','NB','Yp','Yq','Ma','Mc','Mb','Mp'])
na,nb,yp,yq,ma,mc,mb,mp=U.gens()
I=U.ideal([na-nb+yp+yq,nb-2*yp-ma,nb-2*yq-mc,nb-yp-mb,nb-yq-mp])
assert mb+mp-nb-na in I
assert 2*na-ma-mc in I
assert na in I+U.ideal([ma,mc])
print('PASS exact sign-set selection; all four covercase identities; all repeated-slot A/B angle inventories; derivative/tangent factors; exceptional hdelta H/L roles; exact common and singleton count elimination.')
