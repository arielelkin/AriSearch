"""Root independent exact actual-phase filter for single120 seam primals.
No author imports or solver. Arrangement/dual completeness is a separate review.
"""
import json
from pathlib import Path
from sage.all import QQ,QuadraticField,PolynomialRing,matrix,vector
K=QuadraticField(3,'w');w=K.gen();R=PolynomialRing(K,'t');t=R.gen()
# beta in(0,180) gives finite t=tan(beta/2)>0.
cb=(1-t*t)/(1+t*t);sb=2*t/(1+t*t)
# P=1+exp(i60)+exp(i(240-beta)); exact real and imaginary parts.
Pr=K(3)/2-cb/2-w*sb/2
Pi=w/2-w*cb/2+sb/2
# Necessary imaginary zero for rho60. Its complete positive roots are 1/w,w.
a=Pi/2-w*Pr/2
assert a == -w*(t-1/w)*(t-w)/(2*(1+t*t))
assert set(R(a.numerator()).roots(multiplicities=False))=={1/w,w}
# Necessary imaginary zero for rho+beta180.
b=sb*Pr+cb*Pi
assert b==t*(3-w*t)/(1+t*t)
assert set(R(b.numerator()).roots(multiplicities=False))=={K(0),w}
assert t.parent()==R
# Both rho60 candidates have correct positive rotated real part.
for tau in (1/w,w):
 re=Pr(tau);im=Pi(tau)
 assert re>0 and im>0 and im==w*re
# beta60:rho60 => m3=180+delta, outside strictconvexity for all delta>0.
# beta120:rho60 => |P|=2 => p=cos(delta); exact gamma60 periodic cone.
assert Pr(w)==1 and Pi(w)==w and Pr(w)**2+Pi(w)**2==4
D=json.loads(Path('research/certificates/branching-hexagon-two-run-single-120-strata-slot-balance.json').read_text())
planes=[vector(QQ,p) for p in D['planes']]
necessary=[vector(QQ,[-120,0,1,0]),vector(QQ,[-60,0,0,1]),vector(QQ,[-180,0,1,1])]
sat=[r for r in D['records'] if r['status']=='sat'];assert len(sat)==14
for r in sat:
 space=matrix(QQ,[[QQ(x) for x in row] for row in r['flat_basis']]).row_space()
 assert any(v in space for v in necessary),(r['index'],'no actual phase filter plane')
# At the only actual metric candidate, all nonactive forms are nonzero
# multiples of delta and no omitted plane can occur for delta>0.
active=[]
for i,p in enumerate(planes):
 c=p[0]+120*p[2]+60*p[3]
 assert c==0
 if p[1]==0:active.append(i)
 else:assert p[1]!=0
assert active==[1,6,9]
survivors=[]
for r in sat:
 A=matrix(QQ,[[QQ(x) for x in row] for row in r['flat_basis']])
 # At beta120/rho60 each row is a*delta+b.
 coeffs=[(row[1],row[0]+120*row[2]+60*row[3]) for row in A]
 if all(a==0 and b==0 for a,b in coeffs) and r['active_exception_equations']==active:
  survivors.append(r['index'])
assert survivors==[33]
F=json.loads(Path('research/certificates/branching-hexagon-two-run-single-120-strata-metric-filter.json').read_text())
assert F['actual_surviving_stratum']==33 and F['metric_active_equations']==active
filters={r['stratum_index']:r for r in F['all14_SAT_phase_filters']}
assert set(filters)=={r['index'] for r in sat}
condition_names=['beta120','rho60','rho_plus_beta180']
for r in sat:
 space=matrix(QQ,[[QQ(x) for x in row] for row in r['flat_basis']]).row_space()
 assert filters[r['index']]['forced_phase_conditions']==[n for n,v in zip(condition_names,necessary) if v in space]
 assert filters[r['index']]['actual_metric_possible']==(r['index']==33)
print('PASS all14 relaxed primals force an actual phase filter; exact positive halfangle roots; beta60 strictconvexity exclusion; beta120/rho60 periodic candidate occurs only in exact stratum33.')
