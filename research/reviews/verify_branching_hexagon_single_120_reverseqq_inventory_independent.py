"""Independent raw directions, complete48 named binary stars,14 affine exceptions."""
from sage.all import QuadraticField,AA,PolynomialRing
from fractions import Fraction as Q
from itertools import product,combinations_with_replacement
from pathlib import Path
import json
D=json.loads(Path('research/certificates/branching-hexagon-two-run-single-120-reverseqq-exceptional-stars.json').read_text())
assert D['coefficient_order']==['constant','delta','beta','rho']
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
# Raw edge-direction derivation of all native interior-angle vectors.
dirs=[(0,0,0,0),(60,0,0,0),(240,0,-1,0),(120,1,0,1),(180,-1,0,1),(240,1,0,1)]
angles=[]
for j,direction in enumerate(dirs):
 turn=sub(direction,dirs[j-1])
 if j==0:turn=add(turn,(360,0,0,0))
 angles.append(sub((180,0,0,0),turn))
named=dict(zip(('B0','alpha','beta','B3','chi','psi'),angles))
named.update(AH=(120,1,0,0),AL=(120,-1,0,0))
assert {k:list(v) for k,v in named.items()}==D['named_native_angles']
# Native rays force exactly0 or2 mixed corners.
for rays in product(('p','q'),repeat=3):assert sum(rays[j]!=rays[(j+1)%3] for j in range(3)) in(0,2)
types={tuple(sorted(a)) for pair in(('alpha','beta'),('chi','psi')) for a in combinations_with_replacement(pair,3)}
for pair in combinations_with_replacement(('AH','AL','B0','B3'),2):
 for homogeneous in('alpha','beta','chi','psi'):types.add(tuple(sorted(pair+(homogeneous,))))
assert len(types)==48
records=D['complete48named_star_domain'];assert len(records)==48
seen=set();identities=set();classes={}
def ray(v):
 v=tuple(map(Q,v))
 if not any(v):return None
 first=next(x for x in v if x);return tuple(x/first for x in v)
for i,r in enumerate(records):
 typ=tuple(sorted(r['native_type']));assert typ in types and typ not in seen;seen.add(typ)
 total=(0,0,0,0)
 for name in typ:total=add(total,named[name])
 raw=sub(total,(360,0,0,0));assert list(raw)==r['raw_angle_sum_minus360_coefficients']
 k=ray(raw);assert k==(None if r['canonical_equation'] is None else ray(r['canonical_equation']))
 if k is None:identities.add(typ)
 else:classes.setdefault(k,[]).append(i)
expected_ident={tuple(sorted(x)) for x in [('alpha',)*3,('AH','AH','psi'),('AL','AL','chi'),('AH','AL','alpha'),('B0','B3','beta')]}
assert seen==types and identities==expected_ident and len(identities)==5
assert identities=={tuple(sorted(a)) for a in D['five_identical_types']}
assert len(classes)==15 and sum(map(len,classes.values()))==43
boundary=ray((0,1,0,0));assert boundary in classes
kept=classes.keys()-{boundary}
explicit={ray((-120,-k,1,0)) for k in(-2,0,2)}
explicit|={ray((-60,-k,0,1)) for k in(-4,-2,-1,0,2)}
explicit|={ray((-180,-k,1,1)) for k in(-4,-2,-1,0,2)}
explicit.add(ray((-240,2,1,2)))
assert len(explicit)==14 and kept==explicit
retained={}
for r in D['all15proper_equation_classes']:
 k=ray(r['coefficients']);assert k not in retained and r['raw_star_indices']==classes[k]
 assert r['excluded_domain_boundary']==(k==boundary);retained[k]=r['raw_star_indices']
assert retained==classes
retained14={}
for r in D['remaining14exception_curves']:
 k=ray(r['coefficients']);assert k not in retained14 and r['raw_star_indices']==classes[k];retained14[k]=r['raw_star_indices']
assert set(retained14)==kept
# Independently verify all-real chain geometry algebra, with formal phase cos/sin.
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,['t','b','C','S']);t,b,C,S=R.gens();F=R.fraction_field()
cs=lambda a:F(1-a*a)/F(1+a*a);sn=lambda a:F(2*a)/F(1+a*a)
cd,sd,cb,sb=cs(t),sn(t),cs(b),sn(b)
pbeta=(F(3)/2-cb/2-w*sb/2,w/2-w*cb/2+sb/2)
assert pbeta[0]==(1+2*b*b-w*b)/(1+b*b)
assert pbeta[1]==(w*b*b+b)/(1+b*b)
assert (-w)**2-4*2*1==-5
# For b=tan(beta/2)>0, the imaginary numerator is positive; the real quadratic is positive for all realb.
def rot(z,c,s):return(c*z[0]-s*z[1],s*z[0]+c*z[1])
q=[rot(rot((-F(1)/2,w/2),cd,sd),C,S),rot(rot((-1,0),cd,-sd),C,S),rot(rot((-F(1)/2,-w/2),cd,sd),C,S)]
assert tuple(sum(z[j] for z in q) for j in(0,1))==(-2*cd*C,-2*cd*S)
# All six turn increments equal180 minus the stated interior angles, add to360.
turns=[sub((180,0,0,0),a) for a in angles]
assert tuple(sum(a[j] for a in turns) for j in range(4))==(360,0,0,0)
assert angles[0]==(60,1,0,1) and angles[3]==(300,-1,-1,-1)
print('PASS reverseqq raw native angle/direction vectors, exactp/q-chain algebra and positivephase;complete48 named binary types/5 identities/43 exceptions;all15 canonicalclasses and recordindices;exact14 retained auxiliaryaffine relations, no curve outcome inferred.')
