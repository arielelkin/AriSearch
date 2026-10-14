"""Independent exact two-Q periodic witness for the quarter-corner fixture."""
from fractions import Fraction as F
import json
Q=((F(-2,5),F(-16,5)),(F(11,10),F(-6,5)),(F(0),F(-1)),(F(-24,25),F(-32,25)),(F(-54,25),F(-72,25)),(F(-34,25),F(-87,25)))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def cross(x,y):return x[0]*y[1]-x[1]*y[0]
def area(P):return sum(cross(p,P[(i+1)%len(P)]) for i,p in enumerate(P))/2
assert all(cross(sub(Q[(i+1)%6],p),sub(z,p))>0 for i,p in enumerate(Q) for j,z in enumerate(Q) if j not in (i,(i+1)%6))
assert sub(Q[3],Q[2])==neg(sub(Q[0],Q[5]))
t=add(Q[0],Q[1]);reps=(Q,tuple(sub(t,z) for z in Q))
a=sub(Q[2],Q[0]);b=sub(add(Q[3],Q[4]),t)
det=cross(a,b);assert det==2*area(Q)==F(17,2)>0
# Solve integral lattice coordinates without restricting the candidate shift window.
partners=[]
for k,P in enumerate(reps):
 for i,p in enumerate(P):
  end=P[(i+1)%6];found=[]
  for l,R in enumerate(reps):
   for j,z in enumerate(R):
    shift=sub(p,R[(j+1)%6])
    if add(z,shift)!=end:continue
    m=cross(shift,b)/det;n=cross(a,shift)/det
    if m.denominator==n.denominator==1:found.append((l,j,int(m),int(n)))
  assert len(found)==1,(k,i,found)
  partners.append([k,i,*found[0]])
assert len(partners)==12
result=dict(scope="Explicit two-Q omission carrier, quarter-corner fixture; complete integral-lattice oriented boundary cancellation and area mean one",Q=Q,reps=reps,periods=(a,b),covolume=det,area_sum=sum(area(P) for P in reps),directed_partners=partners)
print(json.dumps(result,default=lambda z:str(z),indent=2))
