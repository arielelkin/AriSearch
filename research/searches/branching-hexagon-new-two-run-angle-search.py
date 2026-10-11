#!/usr/bin/env python
"""Exact 81-pattern angle test for A(delta=15), B(pppqqq)."""
from sage.all import QQbar, AA
import itertools, json
import z3
from pathlib import Path
z = QQbar.zeta(24)
assert z.real()>AA(96)/100 and z.real()<AA(97)/100
assert z.imag()>AA(25)/100 and z.imag()<AA(26)/100

def cross(a,b): return (a.conjugate()*b).imag()
def vertices(edges):
    out=[QQbar(0)]
    for e in edges: out.append(out[-1]+e)
    assert out[-1]==0
    return out[:-1]
def convex(edges):
    vs=vertices(edges)
    return all(cross(edges[i],vs[j]-vs[i])>0
        for i in range(6) for j in range(6) if j not in [i,(i+1)%6])
def angles(edges):
    return [-((edges[i]/abs(edges[i]))/(edges[i-1]/abs(edges[i-1]))).conjugate() for i in range(6)]
records=[]
for quad in itertools.product([90,120,150], repeat=4):
    a,b,c,d=quad
    pd=[QQbar(1),z**((180-a)//15),z**((360-a-b)//15)]
    qd=[QQbar(1),z**((180-c)//15),z**((360-c-d)//15)]
    ps,qs=sum(pd),sum(qd)
    if ps==0 or qs==0:
        records.append(dict(quad=quad,status='zero-chain-sum')); continue
    p=AA((qs*qs.conjugate()).real()/(ps*ps.conjugate()).real()).sqrt()
    if p==1:
        records.append(dict(quad=quad,status='equal-lengths')); continue
    rot=-QQbar(p)*ps/qs
    assert rot*rot.conjugate()==1
    be=[QQbar(p)*u for u in pd]+[rot*u for u in qd]
    if not convex(be):
        records.append(dict(quad=quad,status='not-strict-convex')); continue
    ae=[QQbar(p)*z**0,z**5,QQbar(p)*z**8,z**13,QQbar(p)*z**16,z**21]
    assert convex(ae)
    aug=angles(ae)+angles(be)
    pairs=[('p','q')]*6+[('p','q'),('p','p'),('p','p'),('p','q'),('q','q'),('q','q')]
    legal=[]
    for tri in itertools.combinations_with_replacement(range(12),3):
        if aug[tri[0]]*aug[tri[1]]*aug[tri[2]]!=1: continue
        pp=sum(pairs[i]==('p','p') for i in tri)
        qq=sum(pairs[i]==('q','q') for i in tri)
        pq=3-pp-qq
        if (pp,qq,pq) not in [(3,0,0),(1,0,2),(0,1,2),(0,3,0)]: continue
        legal.append(tri)
    fa,fb=z3.Reals('fa fb'); vv=[z3.Real('v%d'%i) for i in range(len(legal))]
    solver=z3.Solver(); solver.add(fa>0,fb>0,fa+fb==1)
    solver.add(*[x>=0 for x in vv])
    for native in range(12):
        solver.add(z3.Sum([v*tri.count(native) for v,tri in zip(vv,legal)])==(fa if native<6 else fb))
    status=solver.check()
    rec=dict(quad=quad,status=str(status),legal_corner_triples=legal,p_minpoly=str(p.minpoly()))
    if status==z3.sat:
        m=solver.model(); rec['model']={'fa':str(m.eval(fa)),'fb':str(m.eval(fb)),
            'vertices':[{ 'triple':tri,'frequency':str(m.eval(v))} for v,tri in zip(vv,legal) if m.eval(v).as_fraction()!=0]}
    records.append(rec)
result={'domain': '81 ordered (beta1,beta2,beta4,beta5) tuples in {90,120,150}^4; delta=15; q=1',
        'records':records}
path=Path(__file__).resolve().parents[1]/'certificates'/'branching-hexagon-new-two-run-angle-search.json'
if '--write-certificate' in __import__('sys').argv: path.write_text(json.dumps(result,indent=2)+'\n')
else:
    retained=json.loads(path.read_text())
    from fractions import Fraction
    def strip_models(data):
        return {'domain':data['domain'],'records':[{k:v for k,v in r.items() if k!='model'} for r in data['records']]}
    assert strip_models(retained)==strip_models(json.loads(json.dumps(result))), 'Retained geometry/status certificate differs'
    for rec in retained['records']:
        if rec['status']=='sat':
            fm=rec['model']; fa=Fraction(fm['fa']); fb=Fraction(fm['fb'])
            assert fa>0 and fb>0 and fa+fb==1
            totals=[Fraction(0)]*12
            for item in fm['vertices']:
                assert item['triple'] in rec['legal_corner_triples']
                v=Fraction(item['frequency']); assert v>=0
                for native in item['triple']: totals[native]+=v
            assert totals==[fa]*6+[fb]*6
        elif rec['status']=='unsat':
            assert all(6 not in tri and 9 not in tri for tri in rec['legal_corner_triples'])
from collections import Counter
print(dict(Counter(r['status'] for r in records)))
print('feasible angle tuples:', [r['quad'] for r in records if r['status']=='sat'])
