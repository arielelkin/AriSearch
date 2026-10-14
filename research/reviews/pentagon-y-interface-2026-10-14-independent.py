"""Independent exact geometry/angle/omission/intact-parent audit; no author imports."""
import itertools,json
from fractions import Fraction as F
import sympy as s
P=[(0,0),(2,0),(3,2),(2,3),(0,2)]
Q=[(2,3),(1,4),(-1,4),(-2,3),(0,2)]
H=[(-2,0),(2,0),(3,2),(1,4),(-1,4),(-3,2)]
angle={'r':(2,0),'a':(4,-1),'b':(1,1),'c':(3,-1),'g':(3,0),'d':(0,2)}
words=['rabba','cggcd','aabggb']
z=(1+2*s.I)/s.sqrt(5)
w=(1+s.I)/s.sqrt(2)
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def norm2(a):return dot(a,a)
def ar2(v):return sum(cross(a,b) for a,b in zip(v,v[1:]+v[:1]))
geometry=[]
for poly,word in zip([P,Q,H],words):
 turns=[];sides=[]
 for i,t in enumerate(word):
  incoming=sub(poly[i],poly[i-1]);outgoing=sub(poly[(i+1)%len(poly)],poly[i])
  turns.append(cross(incoming,outgoing));assert turns[-1]>0
  ray1=tuple(-v for v in incoming)
  actual=(dot(ray1,outgoing)+s.I*cross(outgoing,ray1))/s.sqrt(norm2(ray1)*norm2(outgoing))
  a,b=angle[t];expected=w**a*z**b
  assert s.simplify(actual-expected)==0,(word,i)
  sides.append(norm2(outgoing))
 geometry.append({'word':word,'twice_area':ar2(poly),'turns':turns,'side_squared':sides})
assert 2*ar2(P)+ar2(Q)==ar2(H)
# Irrational theta/pi: 2*cos(2 theta)=-6/5 is rational nonintegral;
# if theta/pi were rational this root-of-unity sum would be algebraic integer.
assert s.simplify(z**2+z**(-2))==-s.Rational(6,5)
def legal(letters,total):
 # Each actual native angle exceeds pi/4, so <=8 corners at 2pi
 # (and <=4 at pi); harmless exhaustive larger bound.
 ans=[]
 for n in range(1,9):
  for word in itertools.combinations_with_replacement(letters,n):
   if tuple(sum(angle[t][j] for t in word) for j in [0,1])==(total,0):ans.append(''.join(word))
 return ans
p360,p180=legal('rab',8),legal('rab',4)
q360,q180=legal('cgd',8),legal('cgd',4)
assert p360==['rrrr'] and p180==['rr']
assert q360==[] and q180==[]
parent360,parent180=legal('abg',8),legal('abg',4)
assert parent360==['abg'] and parent180==[]
# Parent all angles > pi/2, independently established from cosine <0.
for t in 'abg':
 a,b=angle[t];assert s.simplify(s.re(w**a*z**b))<0
# Reconstruct side arms from coordinates, retaining their native cyclic order.
harms=[]
for i,t in enumerate(words[2]):
 har=(norm2(sub(H[i],H[i-1])),norm2(sub(H[(i+1)%6],H[i])))
 harms.append((t,har))
matching=0
for order in itertools.permutations('abg'):
 choices=[[arms for typ,arms in harms if typ==t] for t in order]
 for selected in itertools.product(*choices):
  for flips in itertools.product([False,True],repeat=3):
   arms=[v[::-1] if flip else v for v,flip in zip(selected,flips)]
   matching+=all(arms[i][1]==arms[(i+1)%3][0] for i in range(3))
assert matching==0
# Source omission conclusions include side-interior contacts: any corner
# sums at a vertex equal 2pi, or equal pi with a single flat sector.
# No actual corner is pi, so two flat sectors leave no corner room.
# Exact convex clipping independently verifies the local dissection.
def intersection(subject,clip):
 poly=[tuple(F(v) for v in pt) for pt in subject]
 for a,b in zip(clip,clip[1:]+clip[:1]):
  if not poly:break
  out=[];direction=sub(b,a)
  for start,end in zip(poly,poly[1:]+poly[:1]):
   ds,de=cross(direction,sub(start,a)),cross(direction,sub(end,a))
   if (ds>=0)!=(de>=0):
    ratio=F(ds,ds-de)
    out.append(tuple(start[j]+ratio*(end[j]-start[j]) for j in [0,1]))
   if de>=0:out.append(end)
  poly=out
 return poly
children=[P,[(-x,y) for x,y in reversed(P)],Q]
for child in children:
 assert ar2(intersection(child,H))==ar2(child)
for child1,child2 in itertools.combinations(children,2):
 assert ar2(intersection(child1,child2))==0
# Independently derive type/arm records from native indexed polygon geometry.
arms={}
for poly,word in zip([P,Q],words[:2]):
 for i,typ in enumerate(word):
  rec=((norm2(sub(poly[i],poly[i-1])),word[i-1]),
       (norm2(sub(poly[(i+1)%len(poly)],poly[i])),word[(i+1)%len(poly)]))
  if typ in arms:assert rec==arms[typ] or rec[::-1]==arms[typ]
  else:arms[typ]=rec
full=legal('rab cgd'.replace(' ',''),8)
flat=legal('rab cgd'.replace(' ',''),4)
def add(types):return tuple(sum(angle[t][j] for t in types) for j in [0,1])
counts={}
for star in full:
 raw=kept=0
 for order in set(itertools.permutations(star)):
  for flip in itertools.product([False,True],repeat=len(star)):
   v=[arms[t][::-1] if f else arms[t] for t,f in zip(order,flip)]
   if any(v[i][1][0]!=v[(i+1)%len(v)][0][0] for i in range(len(v))):continue
   raw+=1;ok=True
   for i in range(len(v)):
    far=add([v[i][1][1],v[(i+1)%len(v)][0][1]])
    target=(8-far[0],-far[1])
    completions=[w for n in range(7) for w in itertools.combinations_with_replacement(angle,n) if add(w)==target]
    if not completions and target!=(4,0):ok=False
   kept+=ok
 counts[star]=[raw,kept]
assert counts=={'rgg':[6,6],'aad':[6,6],'abg':[6,6],'rrrr':[16,16],'rrbc':[0,0],'rccd':[0,0],'bbcc':[12,8]},counts
assert set(flat)=={'rr','bc'}
report={'geometry':geometry,'irrationality_certificate':'2 cos(2 theta)=-6/5, rational noninteger algebraic-integer contradiction',
 'P_full_stars':p360,'P_flat_corner_sums':p180,'Q_full_stars':q360,'Q_flat_corner_sums':q180,
 'full_native_stars':full,'flat_stars':flat,'indexed_endpoint_counts':counts,'partition':'exact containment, zero-area pair intersections, area equality verified','parent_stars':parent360,'parent_flat_corner_sums':parent180,'parent_oriented_whole_seam_survivors':matching,
 'verdict':'omissions and intact parent excluded; mixed infinite existence and universal recognition unresolved'}
print(json.dumps(report,indent=2))
