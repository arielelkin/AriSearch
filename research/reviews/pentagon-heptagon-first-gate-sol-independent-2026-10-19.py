"""Independent certificate audit: direct supports, metric vectors, full angle census."""
import itertools,json
from pathlib import Path
import sympy as S
c=json.loads(Path("research/certificates/pentagon-heptagon-astra-first-gate-2026-10-19.json").read_text())
x=S.Symbol("x"); M=S.Poly(x**24-x**12+1,x,domain=S.QQ)
def red(v): return S.rem(S.Poly(v,x,domain=S.QQ),M).as_expr()
def val(v): return sum(S.Rational(a)*x**i for i,a in enumerate(v))
def zp(k): return red(x**(k%72))
def cos(k): return red((zp(k)+zp(-k))/2)
def sin(k): return red((zp(k)-zp(-k))*S.invert(2*zp(18),M.as_expr(),x))
a=c["angle_order"]; stars=set()
for n in range(1,7):
 for t in itertools.combinations_with_replacement(range(7),n):
  total=sum(a[i] for i in t)
  if total in (180,360): stars.add((tuple(t.count(i) for i in range(7)),total==180))
assert stars=={(tuple(t["multiplicities"]),t["flat_host"]) for t in c["stars"]}
for name,dirs in [("P",[0,15,28,39,48]),("Q",[0,6,18,30,42,54,66])]:
 p=c["polygons"][name]; v=[tuple(map(val,t)) for t in p["vertices"]]
 for i,k in enumerate(dirs):
  n=(-sin(k),cos(k)); u=v[i]; w=v[(i+1)%len(v)]
  assert red(sum(n[j]*u[j] for j in (0,1))+1)==0
  assert red(sum(n[j]*w[j] for j in (0,1))+1)==0
  L=val(p["edge_lengths"][i])
  assert all(red(w[j]-u[j]-L*(cos(k),sin(k))[j])==0 for j in (0,1))
 # Listed support gaps are positive and below 180 degrees; their sum is 360.
 gaps=[(dirs[i]-dirs[i-1])%72 for i in range(len(dirs))]
 assert all(0<t<36 for t in gaps) and sum(gaps)==72
 assert [180-5*t for t in gaps]==p["angles"]
# Pairings use a bitmask recurrence, independent from producer list deletion.
def pair(mask):
 if mask==0:
  yield (); return
 low=mask&-mask; i=low.bit_length()-1; rest=mask^low
 for j in range(i+1,12):
  if rest>>j&1:
   for sub in pair(rest^(1<<j)): yield ((i,j),)+sub
dirs=[0,15,28,39,48,0,6,18,30,42,54,66]
count=0; survivors=[0,0]
for matching in pair((1<<12)-1):
 count+=1
 for ci,chir in enumerate((1,-1)):
  phases=[]; ok=True
  for i,j in matching:
   if (i<5)==(j<5):
    if (dirs[i]-dirs[j])%72!=36: ok=False; break
   else: phases.append((dirs[i]+36-chir*dirs[j])%72)
  survivors[ci]+=bool(ok and len(set(phases))<=1)
assert count==10395 and survivors==[0,0]
print("PASS: 12 stars, exact support incidences and edge vectors, strict-convex support gaps, 10395 pairings in both chiralities")
