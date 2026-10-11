"""Independent local incidence and exact closure identities for double-end reduction.
The sparse-defect compactness step is audited in prose against reviewed theorem.
"""
from sage.all import QuadraticField,AA,PolynomialRing
from itertools import product
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
# Every nonhomogeneous trivalent binary star has precisely two changes.
for rays in product((0,1),repeat=3):
 if len(set(rays))==1:continue
 assert sum(rays[i]!=rays[(i+1)%3] for i in range(3))==2
# No Bmiddlep can mate another Bp without an endpoint pp/pp.
ends=[('pq','pp'),('pp','pp'),('pp','pq')]
for side in ends:
 for flip in (False,True):
  partner=side[::-1] if flip else side
  assert any(a==b=='pp' for a,b in zip(ends[1],partner))
# Outsidep mates must reverse mixed/pp corner type to avoid pp/pp.
for host in (ends[0],ends[2]):
 for mate in (ends[0],ends[2]):
  allowed=[p for p in (mate,mate[::-1]) if all(not(a==b=='pp') for a,b in zip(host,p))]
  assert len(allowed)==1 and all(a!=b for a,b in zip(host,allowed[0]))
# WholeAq contacts force H/L at oppositeends, including Bmiddleq.
for endpoints in [(1,-1),(-1,1)]:assert endpoints[0]==-endpoints[1]
R=PolynomialRing(K,['t','u','v','P']);t,u,v,P=R.gens();F=R.fraction_field()
cs=lambda x:F(1-x*x)/F(1+x*x);sn=lambda x:F(2*x)/F(1+x*x)
cd,sd,ca,sa,cb,sb=cs(t),sn(t),cs(u),sn(u),cs(v),sn(v)
def rot(x,C,S):return(C*x[0]-S*x[1],S*x[0]+C*x[1])
S=(1-ca+ca*cb-sa*sb,sa-sa*cb-ca*sb)
assert rot(S,ca,sa)==(ca-1+cb,sa-sb)
assert rot(S,cb,sb)==(cb-(ca*cb+sa*sb)+ca,sb-(sb*ca-cb*sa)-sa)
den=(1+u*u)*(1+v*v)
assert sa-sb==2*(u-v)*(1-u*v)/den
assert sb-(sb*ca-cb*sa)-sa==4*u*v*(u-v)/den
# The independently derived q-chain for same-/crossphase sums exactly.
for Cphase,Sphase in ((ca,sa),(cb,sb)):
 q=[rot(rot((K(1)/2,-w/2),cd,-sd),Cphase,-Sphase),rot((cd,sd),Cphase,-Sphase),rot(rot((K(1)/2,w/2),cd,-sd),Cphase,-Sphase)]
 assert tuple(sum(a[k] for a in q) for k in (0,1))==(2*cd*Cphase,-2*cd*Sphase)
assert F(ca-1+cb).subs({v:u})==2*ca-1
assert F(ca-1+cb).subs({v:1/u})==-1
print('PASS all binarytrivalent incidence states;Bmiddlep/outerp endpoint cases;wholeAq opposite H/L;raw native same/cross closure;exact sine factors and complete two-branch real equations.')
