"""Fresh exact phase/local/count ledger. No author imports and no solver.
Run: conda run --no-capture-output -n arisearch python research/reviews/verify_two_homogeneous_opposite_phase_independent.py
"""
from itertools import product,combinations
from sage.all import QQ,AA,QuadraticField,PolynomialRing,matrix,vector,SR,sin,cos,atan,diff
words={'A':'pqpqpq','B':'pppqqq'}
cs=[(s,j) for s in words for j in range(6)]
def bounds(c,m):
 s,j=c;ids=(j,(j-1)%6)
 if m:ids=ids[::-1]
 return [(words[s][i],i) for i in ids]
def mixed(c):
 s,j=c;return words[s][j]!=words[s][j-1]
n=0
for star in product(cs,repeat=3):
 for flags in product((0,1),repeat=3):
  bs=[bounds(c,f) for c,f in zip(star,flags)]
  if not all(bs[j][1][0]==bs[(j+1)%3][0][0] for j in range(3)):continue
  n+=1
  assert sum(map(mixed,star)) in(0,2)
  if any(star[j][0]==star[(j+1)%3][0]=='A' for j in range(3)):continue
  if sum(c[0]=='A' for c in star)==1:
   other=[c for c in star if c[0]=='B']
   assert sum(map(mixed,other))==1
# Recompute all native mixed/homogeneous angle choices algebraically.
R=PolynomialRing(QQ,['a','e','u','x','y','z']);a,e,u,x,y,z=R.gens()
v=a+e-u;g=[a,360-2*a,360-2*e,e]
res=[[2*u+h-360,u+v+h-360,2*v+h-360] for h in g]
cover=[[360-u-h-120,360-v-h-120] for h in g]
assert res[1]==[2*(u-a),e-a,2*(e-u)]
assert res[2]==[2*(u-e),a-e,2*(a-u)]
assert [cover[1][i]+cover[2][j]+240 for i,j in product(range(2),repeat=2)]==[2*v,a+e,a+e,2*u]
for U,V in((120,120+x-y),(120+x-y,120)):
 subst={a:120+x,e:120-y,u:U}
 assert set(t.subs(subst) for t in cover[1])=={2*x,x+y}
 assert set(t.subs(subst) for t in cover[2])=={-2*y,-x-y}
 assert set(t.subs(subst) for t in cover[0])=={-x,y-2*x}
 assert set(t.subs(subst) for t in cover[3])=={y,2*y-x}
 assert set(t.subs(subst) for t in res[3])=={-y,x-2*y,2*x-3*y}
subst={a:120+x,e:120-x,u:120-z}
assert [t.subs(subst) for t in res[0]]==[x-2*z,x,x+2*z]
assert [t.subs(subst) for t in res[3]]==[-x-2*z,-x,-x+2*z]
assert set(t.subs(subst) for row in(cover[0],cover[3]) for t in row)=={x-z,x+z,-x-z,-x+z}
assert set(t.subs(subst) for row in(cover[1],cover[2]) for t in row)=={2*x-z,2*x+z,-2*x-z,-2*x+z}
# Direct derivatives of the actual phase, radians.
w=SR.var('w');rho=atan(2*sin(w));den=1+4*sin(w)**2
assert (diff(rho,w)-2*cos(w)/den).simplify_trig()==0
assert (diff(rho,w,2)+2*sin(w)*(5+4*cos(w)**2)/den**2).simplify_trig()==0
# Raw opposite q-chain and half-angle exceptional curve, including pole equation.
K=QuadraticField(3,'root3',embedding=AA(3).sqrt());root3=K.gen()
L=K.extension(PolynomialRing(K,'q').gen()**2+1,'i');ii=L.gen()
T=PolynomialRing(L,['Z','S']);Z,S=T.gens();F=T.fraction_field()
assert 1-Z**2+Z==Z*(1+1/Z-Z)
U=PolynomialRing(QQ,'t');t=U.gen();FF=U.fraction_field()
sa,ca=FF(2*t)/(1+t*t),FF(1-t*t)/(1+t*t)
N=t*(3*t*t-1);D=1+8*t*t-t**4;P=t**4+3*t**3-8*t*t-t-1
assert sa*(1-2*ca)/(2*ca+4*sa*sa)==FF(N)/D
assert D-N==-P
assert (2*ca+4*sa*sa)==FF(2*D)/(1+t*t)**2
assert P(1)==-6 and P(2)==5 and P.derivative()(1)==-4
assert P.derivative(2)(1+t)==12*t*t+42*t+14
assert P(root3)==8*root3-16
assert (FF(4*t)/(1+t*t)-t)==FF(t*(3-t*t))/(1+t*t)
planes=[((1,0),120),((2,1),360),((1,2),360),((0,1),120)]
for (x1,b1),(x2,b2) in combinations(planes,2):
 assert matrix(QQ,[x1,x2]).solve_right(vector(QQ,[b1,b2]))==vector(QQ,[120,120])
# Exact native inventory elimination, no species frequencies fixed.
C=PolynomialRing(QQ,['NA','NB','Yp','Yq','Ma','Mb','Mc','Me'])
na,nb,yp,yq,ma,mb,mc,me=C.gens()
I=C.ideal([na-nb+yp+yq,ma-nb+2*yp,mb-nb+yp,mc-nb+yq,me-nb+2*yq])
assert mb+mc-nb-na in I
assert ma+me-2*na in I
J=I+C.ideal([mc-3*na,mb+me-3*na])
assert 2*yp+yq-nb in J and 3*yp+2*yq-2*nb in J
assert matrix(QQ,[[2,1],[3,2]]).solve_right(vector(QQ,[1,2]))==vector(QQ,[0,1])
print(f'PASS {n} native orientedstars; all12 repeated/singleton residuals and8 Acover forms; 3locus inventories; exactrho derivatives; exceptionalcurve N/D/pole/Froot identities; sixpureplane intersections and allnativecount eliminations.')
