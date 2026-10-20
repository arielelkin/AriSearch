"""Bounded 2P+2H edge-to-edge trivalent torus screen for unequal resonance.

Each side length is represented by its exact equality class. A SAT result is
only a combinatorial quotient until geometric development is checked.
"""
import itertools
import json
import time
from pathlib import Path

import z3

P_ANGLES=(100,130,80,130,100)
H_ANGLES=(100,130,130,100,130,130)
P_LABELS=('p','a','one','s','r')
H_LABELS=('L','one','one','c','r','e')
records=[]
for flips in itertools.product((0,1),repeat=3):
    angles=[];labels=[];rho=[]
    for A,L,flip in zip((P_ANGLES,P_ANGLES,H_ANGLES,H_ANGLES),
                        (P_LABELS,P_LABELS,H_LABELS,H_LABELS),(0,*flips)):
        n=len(A);offset=len(angles)
        indices=tuple(range(n)) if not flip else tuple((-i)%n for i in range(n))
        angles.extend(A[i] for i in indices)
        labels.extend(L[i] if not flip else L[(i-1)%n] for i in indices)
        rho.extend(offset+(i+1)%n for i in range(n))
    N=len(angles)
    solver=z3.Solver();solver.set(timeout=6000,random_seed=0)
    alpha=[z3.Int(f'alpha_{i}') for i in range(N)]
    def elem(values,index):
        array=z3.K(z3.IntSort(),0)
        for j,value in enumerate(values):array=z3.Store(array,j,value)
        return z3.Select(array,index)
    for i in range(N):
        solver.add(z3.Or(*(alpha[i]==j for j in range(N)
                           if j!=i and labels[i]==labels[j])))
        solver.add(elem(alpha,alpha[i])==i)
    vertex=[elem(rho,alpha[i]) for i in range(N)]
    for i in range(N):
        v2=elem(vertex,vertex[i]);v3=elem(vertex,v2)
        solver.add(v3==i,vertex[i]!=i,v2!=i,
                   angles[i]+elem(angles,vertex[i])+elem(angles,v2)==360)
    start=time.monotonic();status=solver.check()
    rec=dict(reflections=(0,*flips),status=str(status),seconds=time.monotonic()-start)
    if status==z3.sat:
        model=solver.model();pair=[model.eval(v).as_long() for v in alpha]
        vert=[rho[pair[i]] for i in range(N)]
        assert all(pair[pair[i]]==i and i!=pair[i] and labels[i]==labels[pair[i]]
                   for i in range(N))
        assert all(vert[vert[vert[i]]]==i and
                   len({i,vert[i],vert[vert[i]]})==3 and
                   angles[i]+angles[vert[i]]+angles[vert[vert[i]]]==360
                   for i in range(N))
        seen={0}
        while True:
            more=seen|{rho[i] for i in seen}|{pair[i] for i in seen}
            if more==seen:break
            seen=more
        rec.update(alpha=pair,rho=rho,angles=angles,labels=labels,
                   connected=len(seen)==N)
    elif status==z3.unknown:
        rec['reason']=solver.reason_unknown()
    print(rec if status!=z3.sat else {k:rec[k] for k in ('reflections','status','seconds','connected')},flush=True)
    records.append(rec)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
    scope='Exactly 2P+2H orientable edge-to-edge trivalent quotient; all eight chirality assignments after fixing first P orientation; 6 s timeout each. SAT needs exact geometric verifier.',
    z3_version=z3.get_version_string(),records=records),indent=2)+'\n')
