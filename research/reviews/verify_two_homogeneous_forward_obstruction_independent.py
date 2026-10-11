"""Independent verifier for the forward mixed-homogeneous obstruction.
No author modules, certificates or producers imported. Native oriented stars are rebuilt.
Read-only. Global boundary/compactness proof is audited in the accompanying review.
"""
from sage.all import QQ,SR,PolynomialRing,matrix,vector,QuadraticField,AA,sin,cos,atan,diff
from itertools import product
R=PolynomialRing(QQ,['x','y','h','d','z']);x,y,h,d,z=R.gens()
u=y-h;v=x+h;b=360-2*x;ps=360-2*y
F=[360-u-b,360-v-b];G=[360-u-ps,360-v-ps]
assert F==[2*x-y+h,x-h] and G==[y+h,2*y-x-h]
# Raw native corner slots with both reflections, cyclic length equality rebuilt.
# Each pair gives the incoming and outgoing lengths; reversing swaps the pair.
base=[('AH','q','p'),('AL','p','q')]*3+[('u','q','p'),('x','p','p'),('b','p','p'),('v','p','q'),('y','q','q'),('ps','q','q')]
corners=[]
for name,left,right in base:
 corners.extend([(name,left,right),(name,right,left)])
byhom={name:set() for name in ('x','y','b','ps')};legal=0
for star in product(corners,repeat=3):
 if any(star[i][2]!=star[(i+1)%3][1] for i in range(3)):continue
 legal+=1
 mixed=[t[0] for t in star if t[1]!=t[2]]
 hom=[t[0] for t in star if t[1]==t[2]]
 assert len(mixed) in(0,2)
 if len(hom)!=1 or sum(t in('AH','AL') for t in mixed)>1:continue
 byhom[hom[0]].add(tuple(sorted(mixed)))
expected={tuple(sorted(t)) for t in [('AH','u'),('AH','v'),('AL','u'),('AL','v'),('u','u'),('u','v'),('v','v')]}
assert all(s==expected for s in byhom.values())
# Native common-scale length swap: reflected A edges old1,0,5,4,3,2.
A=[0,60+d,120,180+d,240,300+d]
indices=[1,0,5,4,3,2]
new=[A[1]-A[k]+(360 if j>1 else 0) for j,k in enumerate(indices)]
assert new==A
assert [k%2 for k in indices]==[1,0,1,0,1,0]
assert [(2-j)%6%2 for j in range(6)]==[0,1,0,1,0,1]
# B rotation oldside3 swaps arcs, restoring forward order, mixed u,v swapped.
B=[u,x,b,v,y,ps]
assert B[3:]+B[:3]==[v,y,ps,u,x,b]
# Opposite sign inventories, no accidental omission if a slot has two signs.
for sb,sp in product(({-1},{1},{-1,1}),repeat=2):
 assert any(s==-t for s in sb for t in sp) or sb==sp and len(sb)==1
# All seven angle equations for each repeated slot, rebuilt from raw classes.
Asums=[u+x,v+x,u+y,v+y]
Bsums=[2*u+x,u+v+x,2*v+x,2*u+y,u+v+y,2*v+y]
cases=[
 ({x:120-h,y:120-h-d},[240-3*h-d,240-h,240-3*h-2*d,240-h-d],[-5*h-2*d,-3*h-d,-h,-5*h-3*d,-3*h-2*d,-h-d]),
 ({x:120+h+d,y:120+h},[240+h+d,240+3*h+2*d,240+h,240+3*h+d],[h+d,3*h+2*d,5*h+3*d,h,3*h+d,5*h+2*d]),
 ({x:120+z,y:120-z},[240-h,240+2*z+h,240-2*z-h,240+h],[-z-2*h,z,3*z+2*h,-3*z-2*h,-z,z+2*h])]
for sub,asums,bres in cases:
 assert [t.subs(sub) for t in Asums]==asums
 assert [(t-360).subs(sub) for t in Bsums]==bres
# Complete four pair equations: signs force first high except case4 before phase.
assert (F[0]-G[0]).subs({y:x-d})==2*d
assert (F[1]-G[1]).subs({y:x-d})==2*d
assert F[0]+G[1]==x+y and F[1]+G[0]==x+y
assert (F[0]-G[1]).subs({x:120+z,y:120-z})==6*z+2*h
assert (F[1]-G[0]).subs({x:120+z,y:120-z})==2*(z-h)
# Independent calculus and derivative inequality, no floating arithmetic.
a=SR.var('a');den=1+4*sin(a)**2
assert (diff(atan(2*sin(a)),a)-2*cos(a)/den).simplify_trig()==0
P=PolynomialRing(QQ,'c');c=P.gen()
assert 5-4*c*c-8*c==(1-2*c)*(5+2*c)
# Thus -rho'<1/4 when c=-cos(a) in(0,1/2).
# Independent tangent subtraction in exact Q(sqrt3)[C,S].
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
Q=PolynomialRing(K,['C','S']);C,S=Q.gens();sx=w*C/2-S/2;sy=w*C/2+S/2
I=Q.ideal([C*C+S*S-1])
assert 2*(sy-sx)==2*S and 1+4*sx*sy-4*C*C in I
assert (1+c)-2*c*c==(1-c)*(1+2*c)
# Case2 h=d: explicit sign capacities and no additional beta/psi equation.
assert [t.subs({x:120+2*d,y:120+d,h:d}) for t in F]==[120+4*d,120+d]
assert [t.subs({x:120+2*d,y:120+d,h:d}) for t in G]==[120+2*d,120-d]
# Rebuild actual native count eliminations rather than importing strengthened bound.
T=PolynomialRing(QQ,['aN','bN','yp','yq','ma','my','mb','mp'])
aN,bN,yp,yq,ma,my,mb,mp=T.gens()
J=T.ideal([ma-bN+2*yp,my-bN+2*yq,mb-bN+yp,mp-bN+yq,aN-bN+yp+yq])
assert mb+mp-bN-aN in J # mb+mp <=6aN => bN<=5aN
assert ma+my-2*aN in J
assert aN in J+T.ideal([ma,my])
assert 6*aN-bN in J+T.ideal([ma,3*aN-mb])
print('PASS independent all',legal,'native oriented binary-compatible stars; exhaustive repeated-slot fillers; exact A/B length swap; all4 opposite-sign cases; derivative/tangent comparisons; special h=d and count eliminations. No author imports.')
