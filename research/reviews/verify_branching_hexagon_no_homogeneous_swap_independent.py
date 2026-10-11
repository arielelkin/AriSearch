"""Independent raw-coordinate length-swap and exact arc audit; no author imports."""
from sage.all import QuadraticField, AA, PolynomialRing
from itertools import product
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,['t','u','v','P']);t,u,v,P=R.gens();F=R.fraction_field()
def cs(z):return F(1-z*z)/F(1+z*z)
def sn(z):return F(2*z)/F(1+z*z)
cd,sd=cs(t),sn(t)
def rot(z,C,S):return (C*z[0]-S*z[1],S*z[0]+C*z[1])
def add(a,b):return tuple(x+y for x,y in zip(a,b))
bases=[(1,0),(K(1)/2,w/2),(-K(1)/2,w/2),(-1,0),(-K(1)/2,-w/2),(K(1)/2,-w/2)]
def edges(p):
 return [tuple((p if j%2==0 else 1)*x for x in (rot(z,cd,sd) if j%2 else z)) for j,z in enumerate(bases)]
e=edges(P);vs=[(F(0),F(0))]
for z in e:vs.append(add(vs[-1],z))
assert vs[-1]==(0,0)
Cr,Sr=-cd/2-w*sd/2,w*cd/2-sd/2
new=[tuple(x/P for x in rot((vs[(-j)%6][0],-vs[(-j)%6][1]),Cr,Sr)) for j in range(6)]
new_edges=[tuple(new[(j+1)%6][k]-new[j][k] for k in (0,1)) for j in range(6)]
assert new_edges==edges(F(1)/P)
# Native incoming/outgoing labels under start-at-old-side3.
word=['p']*3+['q']*3
swapped=[{'p':'q','q':'p'}[word[(j+3)%6]] for j in range(6)]
assert swapped==word
pairs=[(word[(j-1)%6],word[j]) for j in range(6)]
assert [pairs[(j+3)%6] for j in (1,2)]==[('q','q')]*2
assert [pairs[(j+3)%6] for j in (4,5)]==[('p','p')]*2
# Raw 3-edge arc: directions0,180-x,360-x-y.
cx,sx,cy,sy=cs(u),sn(u),cs(v),sn(v)
arc=(1-cx+cx*cy-sx*sy,sx-sx*cy-cx*sy)
mag=arc[0]**2+arc[1]**2
assert mag==3-2*cx-2*cy+2*(cx*cy-sx*sy)
# Low/high internal angles120-2delta,120+2delta, independent of order.
c2,s2=cd*cd-sd*sd,2*cd*sd
low=(-c2/2+w*s2/2,w*c2/2+s2/2)
high=(-c2/2-w*s2/2,w*c2/2-s2/2)
for (cx,sx),(cy,sy) in ((low,high),(high,low)):
 arc=(1-cx+cx*cy-sx*sy,sx-sx*cy-cx*sy)
 assert arc[0]**2+arc[1]**2==4*cd*cd
# Both possible relative endpoint identifications of two H/L sides.
H,L=(120,1),(120,-1)
fillers=[]
for other in ((H,L),(L,H)):
 fillers.append(tuple((360-a[0]-b[0],-a[1]-b[1]) for a,b in zip((H,L),other)))
assert set(fillers)=={((120,-2),(120,2)),((120,0),(120,0))}
# Mixed binary parity and A-only omission.
for rays in product(('p','q'),repeat=3):
 changes=sum(rays[j]!=rays[(j+1)%3] for j in range(3))
 assert changes in (0,2)
print('PASS raw A vertex reflection and all6 new edges; B native block/corner exchange; exact arc F and nonzero low/high factor4cos(delta)^2; exhaustive AA q endpoint alternatives and binary parity.')
