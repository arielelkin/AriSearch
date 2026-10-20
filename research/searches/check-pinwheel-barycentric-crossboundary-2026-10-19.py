"""Independent minimal rational fixture check; does not certify full producer counts."""
from fractions import Fraction as F

def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def mid(a,b):return ((a[0]+b[0])/2,(a[1]+b[1])/2)
def center(t):return tuple(sum(p[k] for p in t)/3 for k in (0,1))
v=(F(6),F(12))
ts=[tuple(tuple(map(F,p)) for p in t) for t in [((0,0),(12,24),(0,30)),((18,36),(6,12),(18,6)),((6,12),(0,0),(30,0))]]
# Each source face is exactly a congruent 1:2 right triangle.
for t in ts:
 d=sorted(dot(sub(a,b),sub(a,b)) for i,a in enumerate(t) for b in t[:i])
 assert d==[180,720,900]
 assert abs(det(sub(t[1],t[0]),sub(t[2],t[0])))==360
# Radial neighbors of the T-star, clockwise: (0,0),(18,6),(12,24).
# Source face0 has a flat angle at v; face1 and face2 close the other halfplane.
assert det(sub(v,ts[0][0]),sub(ts[0][1],ts[0][0]))==0
assert dot(sub(v,ts[0][0]),sub(v,ts[0][1]))<0
radials=[ts[0][0],ts[1][2],ts[0][1]]
# Unreduced dual boundary, alternating radial midpoint and face centroid.
p=[mid(v,radials[0]),center(ts[2]),mid(v,radials[1]),center(ts[1]),mid(v,radials[2]),center(ts[0])]
# The first and last entries form a collinear pair only through the closing edge.
changed=True
while changed:
 changed=False
 for i in range(len(p)):
  if det(sub(p[i],p[i-1]),sub(p[(i+1)%len(p)],p[i]))==0:
   p.pop(i);changed=True;break
expected=[(3,6),(12,4),(12,9),(14,18),(4,18)]
assert p==expected,(p,expected)
turns=[det(sub(p[i],p[i-1]),sub(p[(i+1)%len(p)],p[i])) for i in range(len(p))]
assert turns==[110,45,-10,90,120]
print('PASS: exact congruent T-star barycentric dual is a concave pentagon; turns',turns)
