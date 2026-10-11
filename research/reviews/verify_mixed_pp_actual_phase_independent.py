"""Fresh root mixed-pp actual-phase audit using cos(alpha), not author code.
The complete arrangement and strong duals are independently reviewed elsewhere.
"""
import json
from pathlib import Path
from sage.all import QQ,QuadraticField,PolynomialRing,matrix,vector
K=QuadraticField(3,'w');w=K.gen();R=PolynomialRing(QQ,'c');c=R.gen()
# alpha in(90,180): -1<c<0 and sin(alpha)>0.
# Raw p-chain=1+exp(i(180-alpha))+exp(i alpha)=1+2i*sin(alpha).
# Necessary imag(exp(i alpha)*P)/sin(alpha) for alpha+rho180.
sumphase=1+2*c
assert set(sumphase.roots(multiplicities=False))=={QQ(-1)/2}
# Necessary imag(exp(-2i alpha)*P)/sin(alpha) for rho2alpha-180.
doublephase=2*(2*c*c-1-c)
assert doublephase==2*(2*c+1)*(c-1)
assert set(doublephase.roots(multiplicities=False))=={QQ(-1)/2,QQ(1)}
assert not -1<QQ(1)<0
# On(90,180) cosine is one-to-one: c=-1/2 gives alpha120,
# sin(alpha)=w/2>0, P=(1,w), rho60 and |P|=2.
assert (w/2)**2==1-QQ(1)/4 and 1+w*w==4
D=json.loads(Path('research/certificates/branching-hexagon-two-run-mixed-pp-strata-slot-balance.json').read_text())
assert D['counts']=={'unsat':71,'sat':22}
sat=[r for r in D['records'] if r['status']=='sat'];assert len(sat)==22
conditions=[vector(QQ,[-120,0,1,0]),vector(QQ,[-180,0,1,1]),vector(QQ,[180,0,-2,1])]
names=['alpha120','alpha_plus_rho180','rho_equals_2alpha_minus180']
for r in sat:
 space=matrix(QQ,[[QQ(x) for x in row] for row in r['flat_basis']]).row_space()
 assert any(v in space for v in conditions)
planes=[vector(QQ,p) for p in D['planes']];active=[]
for i,p in enumerate(planes):
 assert p[0]+120*p[2]+60*p[3]==0
 if p[1]==0:active.append(i)
assert active==[4,5,12,16,17]
survivors=[]
for r in sat:
 rows=matrix(QQ,[[QQ(x) for x in row] for row in r['flat_basis']]).rows()
 if all(row[1]==0 and row[0]+120*row[2]+60*row[3]==0 for row in rows) and r['active_exception_equations']==active:survivors.append(r['index'])
assert survivors==[73]
F=json.loads(Path('research/certificates/branching-hexagon-two-run-mixed-pp-strata-metric-filter.json').read_text())
assert F['actual_surviving_stratum']==73 and F['metric_active_equations']==active
filters={r['stratum_index']:r for r in F['all22_SAT_phase_filters']};assert set(filters)=={r['index'] for r in sat}
for r in sat:
 space=matrix(QQ,[[QQ(x) for x in row] for row in r['flat_basis']]).row_space()
 assert filters[r['index']]['forced_actual_phase_conditions']==[n for n,v in zip(names,conditions) if v in space]
 assert filters[r['index']]['actual_metric_possible']==(r['index']==73)
print('PASS22 necessary-primal phase filters; independent cosine factors and all allowed roots; nonvanishing actualarc; unique active metric stratum73 alpha120/rho60, known periodic curve.')
