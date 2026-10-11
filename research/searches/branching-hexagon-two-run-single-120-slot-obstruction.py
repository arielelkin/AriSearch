"""One NEW resonant exact metric fixture and five-type native-slot obstruction.
Read-only normal replay; explicit --output required. Reuses the reviewed producer
core as authoring code; fresh verification must not import this or its dependency.
"""
import argparse,json,importlib.util
from pathlib import Path
from sage.all import CyclotomicField
from fractions import Fraction

def produce(output=None):
    source=Path(__file__).with_name('branching-hexagon-new-two-run-catalog-slot-periodic.py')
    spec=importlib.util.spec_from_file_location('reviewed_slot_authoring_core',source);core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
    r=core.balance((120,105,90,150));assert r['status']=='unsat'
    names=['AH','AL','AH','AL','AH','AL','B0','alpha','beta','B3','chi','psi']
    allowed={tuple(sorted(t)) for t in [('alpha',)*3,('AH','AH','chi'),('AL','AL','psi'),('AH','AL','alpha'),('B0','B3','beta')]}
    actual={tuple(sorted(names[o//2] for o in star)) for star in r['oriented_stars']}
    assert actual==allowed
    W=[-1 if i in(0,2,4) else (-3 if i==10 else 0) for i in range(12)]
    Y=[]
    for x,y,parity in r['seam_keys']:
        val=0
        if x[0]==0 and tuple(y)==(1,1) and x[1]%2==0:val=-3 if parity==1 else 1
        if x[0]==0 and tuple(y)==(1,3) and x[1]%2==1 and parity==0:val=-7
        Y.append(val)
    assert all(sum(W[int(c)]*v for c,v in C.items())+sum(y*v for y,v in zip(Y,S))>=0 for C,S in zip(r['star_corner_counts'],r['star_seam_counts']))
    assert sum(W[:6])==sum(W[6:])==-3
    r['symmetric_corner_dual']=W;r['symmetric_seam_dual']=Y
    K=CyclotomicField(24);z=K.gen();P=1+z**4+z**9;Q=1+z**6+z**8;ratio=(Q*Q.conjugate())/(P*P.conjugate())
    assert ratio!=1
    r.update({'delta':15,'q':1,'field':'Q(zeta24),z=exp(i*pi/12)','p_squared_coefficients':[str(x) for x in ratio.list()],
              'native_P_chain_exponents':[0,4,9],'relative_Q_chain_exponents':[0,6,8],
              'abstract_star_type_domain':sorted(allowed),
              'abstract_extension_scope':'any actual admitted strictlyconvex geometry whose legal oriented native stars are contained in these five named types, for alpha120 and chi/psi120minus/plus2delta',
              'authoring_dependency':source.name,'claim_status':'PENDING fresh independent review'})
    if output:Path(output).write_text(json.dumps(r,indent=2)+'\n')
    print('PASS exactnewresonantfixture80stars36seams;five-typeglobaldual retained');return r
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();produce(args.output)
