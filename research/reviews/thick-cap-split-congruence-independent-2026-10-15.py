#!/usr/bin/env python3
"""Independent exact audit of the cap-split cyclic-angle obstruction.
No author imports, sampling, geometry tolerance, or solver. Universal
inequality steps are supplied in the adjacent written hostile review.
"""
from collections import Counter
from fractions import Fraction as F

# Actual native source arrows: (tail vertex, head vertex, mark), boundary
# slots AB,BC,CD,DA. Endpoints, not just mark counts, are audited below.
ARROWS={
 'thin':((0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')),
 'thick':((0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')),
}
def pair(a,b):return tuple(sorted((a,b)))
def boundary(w):return Counter(pair(w[i],w[(i+1)%len(w)]) for i in range(len(w)))
def clipped(w,cut):
 result=[]
 for j,v in enumerate(w):
  if v in cut:result.extend((v+'_'+w[j-1],v+'_'+w[(j+1)%len(w)]))
  else:result.append(v)
 return tuple(result)

audit_cases=audit_nodes=0
for species,arrows in ARROWS.items():
 for parity in (0,1):
  donors={i for i in range(4) if i%2==parity}
  receivers=set(range(4))-donors
  assert Counter(arrows[i][2] for i in donors)==Counter(X=1,Y=1)
  assert Counter(arrows[i][2] for i in receivers)==Counter(X=1,Y=1)
  # Four actual original-source vertex angles. A variable G_v denotes
  # the source rhomb angle; X_tail, X_head etc. denote mark-local base angles.
  endpoint_rows=[]
  for v in range(4):
   row=Counter({'G%d'%v:1})
   for e in ((v-1)%4,v):
    tail,head,mark=arrows[e]
    assert v in (tail,head)
    label=mark+('_tail' if v==tail else '_head')
    row[label]+=(-1 if e in donors else 1)
   endpoint_rows.append(row)
  total={name:sum(row[name] for row in endpoint_rows)
         for name in {'G0','G1','G2','G3','X_tail','X_head','Y_tail','Y_head'}}
  assert total=={'G0':1,'G1':1,'G2':1,'G3':1,
                'X_tail':0,'X_head':0,'Y_tail':0,'Y_head':0}
  # Build EVERY source-local precursor independently by its receiving side.
  outputs=[]
  for i in sorted(receivers):
   U,V='v%d'%i,'v%d'%((i+1)%4)
   m,t='m%d'%i,'e%d'%i
   p,q='d%d'%((i-1)%4),'d%d'%((i+1)%4)
   L=(U,t,m,p);R=(m,t,V,q);C=(m,q,p)
   assert clipped(L,{t,p})==(U,t+'_'+U,t+'_'+m,m,p+'_'+m,p+'_'+U)
   assert clipped(R,{t,q})==(m,t+'_'+m,t+'_'+V,V,q+'_'+V,q+'_'+m)
   assert clipped(C,{p,q})==(m,q+'_'+m,q+'_'+p,p+'_'+q,p+'_'+m)
   outputs.extend((L,R,C))
  for j in sorted(donors):
   node='d%d'%j;observed=Counter()
   for word in outputs:
    if node in word:
     k=word.index(node);observed[pair(word[k-1],word[(k+1)%len(word)])]+=1
   # These two sectors are owned by the rhomb on the other side, but their
   # physical rays at this source donor node are fixed by the base split.
   observed[pair('v%d'%j,'m%d'%j)]+=1
   observed[pair('m%d'%j,'v%d'%((j+1)%4))]+=1
   tail,head,mark=arrows[j]
   def other_receiver(v):
    return next(i for i in receivers if v in (i,(i+1)%4))
   rays=('v%d'%tail,'m%d'%j,'v%d'%head,
         'm%d'%other_receiver(head),'d%d'%((j+2)%4),'m%d'%other_receiver(tail))
   assert len(set(rays))==6
   assert observed==boundary(rays)
   audit_nodes+=1
  # Two C pentagons, four receiver hexagons; add or split the two caps.
  P,H=2,4
  if species=='thin':H+=2
  else:P+=4
  assert (P,H)==((2,6) if species=='thin' else (6,4))
  audit_cases+=1
assert (audit_cases,audit_nodes)==(4,8)

# Equal-radius clipping at an original angle a yields (pi+a)/2 twice.
# Use independent linear forms (U,T,M,P,pi), never numerical angles.
def vec(i):return tuple(F(j==i) for j in range(5))
def plus(*vs):return tuple(sum(x) for x in zip(*vs))
def mul(a,v):return tuple(a*x for x in v)
U,T,M,P,PI=map(vec,range(5))
angles=(U,mul(F(1,2),plus(PI,T)),mul(F(1,2),plus(PI,T)),
        M,mul(F(1,2),plus(PI,P)),mul(F(1,2),plus(PI,P)))
difference=plus(*(mul(1 if i%2==0 else -1,a) for i,a in enumerate(angles)))
assert difference==plus(U,mul(-1,M))
# Any cyclic hexagon, even with center outside it: angle_i = pi minus
# half the sum of its two neighboring positive central gaps.
central_forms=[]
for i in range(6):
 row=[F(0)]*7;row[0]=1;row[1+i]-=F(1,2);row[1+(i-1)%6]-=F(1,2)
 central_forms.append(row)
assert [sum(central_forms[i][j] for i in (0,2,4)) for j in range(7)]==[F(3)]+[F(-1,2)]*6
assert [sum(central_forms[i][j] for i in (1,3,5)) for j in range(7)]==[F(3)]+[F(-1,2)]*6
# Since the six gaps sum to 2pi, each alternate-angle sum is 2pi.

# Normal-foot universal sign: in coordinates M=(m,0), outward t=(m,h),
# inward p=(x,y), the dot product is exactly h*y. h>0,y<0 give negativity.
# Store the polynomial coefficient check without sampling that inequality.
basis=[tuple(F(i==j) for i in range(4)) for j in range(4)]
m,h,x,y=basis;zero=(F(0),)*4
foot=(m,zero);apex=(m,h);inside=(x,y)
def subtract(a,b):return tuple(v-w for v,w in zip(a,b))
dot_polynomial=Counter()
for a,b in zip((subtract(v,w) for v,w in zip(apex,foot)),
               (subtract(v,w) for v,w in zip(inside,foot))):
 for i,ai in enumerate(a):
  for j,bj in enumerate(b):dot_polynomial[tuple(sorted((i,j)))]+=ai*bj
assert {k:v for k,v in dot_polynomial.items() if v}=={(1,3):1}
# A changed off-foot rule may reverse the sign; excluded from the theorem.
assert (-2)*(-1)+1*(-1)>0

# Opposite-edge cap split keeps eight refined cap boundary edges and one
# internal chord counted twice. Both words have five genuine formal slots.
left=('a','c1','c2','c3','b');right=('b','c4','c5','c0','a')
refined=('c0','a','c1','c2','c3','b','c4','c5')
assert boundary(left)+boundary(right)==boundary(refined)+Counter({pair('a','b'):2})
assert len(left)==len(right)==5
print('PASS: 4 actual-arrow endpoint cancellations; 8 independently reconstructed six-ray cap cycles; all clipped native words; cyclic-angle invariant and normal-foot sign reduction; opposite-edge split incidence.')
