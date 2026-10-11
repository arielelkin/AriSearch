"""Fresh symbolic audit: native slot/event completeness and interval geometry.
No author imports, no numerical sampling, no fixture continuity argument.
"""
from itertools import combinations,combinations_with_replacement
from sage.all import QuadraticField,PolynomialRing,AA,vector,matrix
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,'x');x=R.gen();one=R(1)
lo=1/w;hi=2-1/w;exceptions={(2*w-1)/(w+2),K(1),5/(w+2)}
P=[one,x,(3*w-x)/2,(w*x-1)/2,R(2)]
Q=[(w*(2-x)-1)/2,(3*w-(2-x))/2,2-x,one,R(2)]
assert lo<min(exceptions)<1<max(exceptions)<hi

def interior_roots(f):
 if not f:return None
 return [a for a in f.change_ring(AA).roots(multiplicities=False) if AA(lo)<a<AA(hi)]
def positive(f):
 f=R(f);assert f and f((lo+hi)/2)>0
 assert f(lo)>=0 and f(hi)>=0
 assert not interior_roots(f)

def planar(a,b):return a[0]*b[1]-a[1]*b[0]
for sides in (P,Q):
 for side in sides:positive(side)
 a,b,c,d,e=sides
 edges=[vector(R,[a,0]),vector(R,[0,b]),vector(R,[-w*c/2,c/2]),
  vector(R,[-d/2,-w*d/2]),vector(R,[e/2,-w*e/2])]
 assert sum(edges,vector(R,[0,0]))==0
 verts=[vector(R,[0,0])]
 for edge in edges[:-1]:verts.append(verts[-1]+edge)
 for i in range(5):
  for j in range(5):
   if j not in [i,(i+1)%5]:positive(planar(edges[i],verts[j]-verts[i]))
# Enumerate all28 internal/cross distinct native arm comparisons.
arms=[('P',i,P[i]) for i in range(4)]+[('Q',i,Q[i]) for i in range(4)]
identity=[];exceptional=[]
for i,j in combinations(range(8),2):
 diff=arms[i][2]-arms[j][2]
 if not diff:identity.append((i,j));continue
 roots=interior_roots(diff)
 for root in roots:
  assert any(root==AA(e) for e in exceptions)
  exceptional.append((i,j,root))
assert identity==[(0,7)]
assert {root for i,j,root in exceptional}=={AA(e) for e in exceptions}
# Eight oriented90-corner slots; exhaust every possible perpendicular mate.
slots=[]
for label,sides in [('P',P),('Q',Q)]:
 for perp,bank in [(0,1),(1,0),(2,3),(3,2)]:slots.append((label,perp,bank,sides[perp],sides[bank]))
events=[]
for i,j in combinations_with_replacement(range(8),2):
 difference=slots[i][3]-slots[j][3]
 if not difference:events.append((i,j,slots[i][4]+slots[j][4]))
 else:
  for root in interior_roots(difference):assert root in {AA(e) for e in exceptions}
assert len(events)==9
assert [(i,j) for i,j,total in events if i!=j]==[(0,7)]
# Exhaust all36 bank-sum comparisons, not merely the arm value comparisons.
identical_sums=[]
for a,b in combinations(range(9),2):
 diff=events[a][2]-events[b][2]
 if not diff:identical_sums.append((a,b));assert events[a][2]==2
 else:
  for root in interior_roots(diff):assert root in {AA(e) for e in exceptions}
assert len(identical_sums)==3
assert sum(total==2 for i,j,total in events)==3
for i,j,total in events:
 if total!=2:
  for root in interior_roots(total-2):assert root in {AA(e) for e in exceptions}
# Deliberately inspect native arm=e equalities, omitted from arm privacy table.
arm_e_roots=[]
for label,i,arm in arms:
 for root in interior_roots(arm-2) or []:arm_e_roots.append((label,i,root))
assert {(label,i) for label,i,root in arm_e_roots}=={('P',2),('Q',1)}
assert {root for label,i,root in arm_e_roots}=={AA(3*w-4),AA(6-3*w)}
# Uniform reflected-face overlap; use parameterx as the filler speciesz.
z=x;d=(w*z-1)/2;c=(3*w-z)/2
face=[vector(R,[0,0]),vector(R,[d,0]),vector(R,[d+1,-w]),
 vector(R,[d+K(1)/2,-3*w/2]),vector(R,[0,-c])]
seam=vector(R,[-w*z/2,-3*w/2]);u=vector(R,[w/2,K(1)/2])
F=2*matrix(R,2,1,list(u))*matrix(R,1,2,list(u))-matrix.identity(R,2)
W=vector(R,[w*z/5+K(3)/10,7*z/10-7*w/5])
assert F*F==matrix.identity(R,2) and F.det()==-1
assert W==seam+F*(W-seam)
for i in range(5):positive(-planar(face[(i+1)%5]-face[i],W-face[i]))
reflected_center=seam-F*seam
assert reflected_center==vector(R,[(9-w*z)/4,(3*z-9*w)/4])
positive(reflected_center[0])
assert reflected_center[0](3*w)==0 and reflected_center[1](3*w)==0
print('PASS:positive lengths,closure,30 support inequalities;28 complete native-arm comparisons;36 perpendicular-pair events→9 generic events;36 bank-sum comparisons;2 harmless arm=e roots;5 universal strict overlap inequalities;repaired center distinction z=3sqrt3.')
