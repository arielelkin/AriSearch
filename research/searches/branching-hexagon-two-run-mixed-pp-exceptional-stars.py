"""Complete48named angle-star domain on mixed21pp/qq-low-high slice.
Read-only replay by default; explicit--output writes. No curve classification.
"""
import argparse,json,itertools,math
from collections import Counter
from pathlib import Path
angles={'AH':(120,1,0,0),'AL':(120,-1,0,0),'B0':(60,-1,0,1),'B3':(60,1,1,-1),
        'alpha':(0,0,1,0),'beta':(360,0,-2,0),'chi':(120,-2,0,0),'psi':(120,2,0,0)}
def canon(v):
    g=math.gcd(*v)
    if not g:return None
    w=tuple(x//g for x in v)
    if next(x for x in w if x)<0:w=tuple(-x for x in w)
    return w
def inventory(output=None):
    tris=[]
    for arc in [('alpha','beta'),('chi','psi')]:tris+=list(itertools.combinations_with_replacement(arc,3))
    for pair in itertools.combinations_with_replacement(['AH','AL','B0','B3'],2):
        for h in ['alpha','beta','chi','psi']:tris.append(pair+(h,))
    assert len(tris)==48
    records=[];proper={};ident=[]
    for i,tri in enumerate(tris):
        v=[sum(angles[x][j] for x in tri) for j in range(4)];v[0]-=360;k=canon(v)
        records.append({'native_type':tri,'raw_angle_sum_minus360_coefficients':v,'canonical_equation':k})
        if k is None:ident.append(tuple(sorted(tri)))
        else:proper.setdefault(k,[]).append(i)
    expected={tuple(sorted(t)) for t in [('alpha','alpha','beta'),('AH','AH','chi'),('AL','AL','psi')]}
    assert set(ident)==expected and len(ident)==3
    delta0=canon((0,1,0,0));assert delta0 in proper
    allowed=set(proper)-{delta0}
    explicit=set()
    for k in[-2,-1,0,1,2]:explicit.add(canon((-120,-k,1,0)))
    for k in[0,2]:
        explicit.add(canon((-180,-k,1,1)));explicit.add(canon((180,-k,-2,1)))
    explicit.add(canon((-240,-2,1,2)));explicit.add(canon((240,-2,-3,2)))
    for k in[-2,0,1,2,4]:
        explicit.add(canon((60,-k,-1,1)));explicit.add(canon((-60,-k,0,1)))
    assert allowed==explicit and len(allowed)==21
    out={'domain':'actualstrictconvexbinarymixed21ppslice:2alpha+beta360;chi120-2delta;psi120+2delta;0delta30;90alpha180;alpha-rho+delta<120;p2cosdelta/abs(Palpha);p!=1',
         'coefficient_order':['constant','delta','alpha','rho'],
         'Palpha':'1+2i*sin(alpha)','rho':'actualnativepchainphase',
         'named_native_angles':angles,'complete48named_star_domain':records,'three_identical_types':ident,
         'all22proper_equation_classes':[{'coefficients':k,'raw_star_indices':idx,'excluded_domain_boundary':k==delta0} for k,idx in sorted(proper.items())],
         'remaining21exception_curves':[{'coefficients':k,'raw_star_indices':proper[k]} for k in sorted(allowed)],
         'scope':'outside21planescompletelegalstarsetcontainsnomorethanthreeidentitytypes;dualityneededforglobaluntileability;oncurvesnooutcomeclaimed'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS48types;3identities45rawexceptions;22properclassesminusdelta0=21exactplanes');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();inventory(args.output)
