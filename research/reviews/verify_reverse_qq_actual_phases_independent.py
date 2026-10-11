"""Fresh root nonlinear filters and native periodic transfers for reverse qq.
No author imports or solver. Full arrangements have separate fresh reviews.
"""
import json
from pathlib import Path
from sage.all import QQ,QuadraticField,PolynomialRing,matrix,vector
K=QuadraticField(3,'w');w=K.gen();R=PolynomialRing(K,'t');t=R.gen()
cb=(1-t*t)/(1+t*t);sb=2*t/(1+t*t)
Pr=K(3)/2-cb/2-w*sb/2;Pi=w/2-w*cb/2+sb/2
assert Pi/2-w*Pr/2==-w*(t-1/w)*(t-w)/(2*(1+t*t))
assert sb*Pr+cb*Pi==t*(3-w*t)/(1+t*t)
assert set(R((Pi/2-w*Pr/2).numerator()).roots(multiplicities=False))=={1/w,w}
assert set(R((sb*Pr+cb*Pi).numerator()).roots(multiplicities=False))=={K(0),w}
for tau in (1/w,w):assert Pr(tau)>0 and Pi(tau)==w*Pr(tau)
# These give beta60/120, both now convex: rho+beta>120-delta.
assert Pr(1/w)**2+Pi(1/w)**2==1
assert Pr(w)**2+Pi(w)**2==4
C=PolynomialRing(QQ,'c');c=C.gen()
assert set((1+2*c).roots(multiplicities=False))=={QQ(-1)/2}
assert set((2*(2*c*c-1-c)).roots(multiplicities=False))=={QQ(-1)/2,QQ(1)}
assert not -1<QQ(1)<0
root=Path('research/certificates')
def read(stem,kind):return json.loads((root/('branching-hexagon-two-run-'+stem+'-reverseqq-'+kind+'.json')).read_text())
def rowspace(rec):return matrix(QQ,[[QQ(x) for x in row] for row in rec['flat_basis']]).row_space()
D=read('single-120','strata-slot-balance');F=read('single-120','strata-metric-filter')
sat=[r for r in D['records'] if r['status']=='sat'];assert len(sat)==14
conditions=[vector(QQ,[-120,0,1,0]),vector(QQ,[-60,0,0,1]),vector(QQ,[-180,0,1,1])]
names=['beta120','rho60','beta_plus_rho180'];filters={r['stratum_index']:r for r in F['all14_SAT_phase_filters']}
assert set(filters)=={r['index'] for r in sat}
for r in sat:assert filters[r['index']]['forced_phase_conditions']==[n for n,v in zip(names,conditions) if v in rowspace(r)] and any(v in rowspace(r) for v in conditions)
planes=list(map(lambda p:vector(QQ,p),D['planes']))
def active(beta,delta):return [i for i,p in enumerate(planes) if p[0]+p[1]*delta+p[2]*beta+p[3]*60==0]
roots=set()
for p in planes:
 if p[1]:
  d=-(p[0]+60*p[2]+60*p[3])/p[1]
  if 0<d<30:roots.add(d)
assert roots=={QQ(15)}
patterns=[(120,QQ(1),[3,6,11]),(60,QQ(1),[3]),(60,QQ(15),[3,8])]
for beta,d,expected in patterns:assert active(beta,d)==expected
assert all(p[0]+120*p[2]+60*p[3]==0 for p in planes)
expected_sets=[x[2] for x in patterns];survivors=[]
for r in sat:
 possible=r['active_exception_equations'] in expected_sets
 assert filters[r['index']]['actual_metric_possible']==possible
 if possible:survivors.append(r['index'])
assert survivors==[38,39,43] and F['actual_surviving_strata']==survivors
D=read('mixed-pp','strata-slot-balance');F=read('mixed-pp','strata-metric-filter')
sat=[r for r in D['records'] if r['status']=='sat'];assert len(sat)==22
conditions=[vector(QQ,[-120,0,1,0]),vector(QQ,[-180,0,1,1]),vector(QQ,[180,0,-2,1])]
names=['alpha120','alpha_plus_rho180','rho_equals_2alpha_minus180']
filters={r['stratum_index']:r for r in F['all22_SAT_phase_filters']};assert set(filters)=={r['index'] for r in sat}
planes=[vector(QQ,p) for p in D['planes']]
assert all(p[0]+120*p[2]+60*p[3]==0 for p in planes)
act=[i for i,p in enumerate(planes) if p[1]==0];assert act==[4,5,12,16,17]
survivors=[]
for r in sat:
 assert filters[r['index']]['forced_actual_phase_conditions']==[n for n,v in zip(names,conditions) if v in rowspace(r)] and any(v in rowspace(r) for v in conditions)
 possible=r['active_exception_equations']==act
 assert filters[r['index']]['actual_metric_possible']==possible
 if possible:survivors.append(r['index'])
assert survivors==[73] and F['actual_surviving_stratum']==73
# Actual B reflection reverses native side order 2,1,0,5,4,3.
# (base,delta coefficient) directions compared modulo360 by their base.
side_map=(2,1,0,5,4,3)
def reflect(dirs,rotation):return [((180-dirs[i][0]+rotation)%360,-dirs[i][1]) for i in side_map]
b60=[(0,0),(60,0),(180,0),(180,1),(240,-1),(300,1)]
comp60=[(0,0),(120,0),(180,0),(240,-1),(300,1),(0,-1)]
assert reflect(b60,0)==comp60
b120=[(0,0),(60,0),(120,0),(180,1),(240,-1),(300,1)]
gamma60=[(0,0),(60,0),(120,0),(180,-1),(240,1),(300,-1)]
assert reflect(b120,-60)==gamma60
# Reflection preserves the pppqqq side word, with lengths p2cos(delta)
# at beta60 and pcos(delta) at beta120. Both target cones are reviewed.
print('PASS reverseqq14+22 actualphase filters, allpositive factor roots, beta60 delta15 special active set, unique mixedpp stratum73, raw native reflection directions to both periodic cones.')
