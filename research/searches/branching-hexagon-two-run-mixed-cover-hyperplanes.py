"""Complete prespecified binary mixed-corner cover elimination, exact and read-only.
Writes only with explicit --output. A proper necessary hyperplane inventory,
not sufficient local coverage and not a periodicity or exhaustive resonance theorem.
"""
import argparse,json,itertools,math
from fractions import Fraction as F
from pathlib import Path
# order [constant,delta,alpha,beta,chi,psi]
S=[F(0),F(0),F(1),F(1),F(1),F(1)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def canonical(v):
    den=math.lcm(*(x.denominator for x in v));a=[int(x*den) for x in v]
    g=math.gcd(*a);assert g;a=[x//g for x in a]
    first=next(x for x in a if x)
    if first<0:a=[-x for x in a]
    assert any(a[2:]);return tuple(a)
def inventory(output=None):
    alternatives=[]
    for r,name in enumerate(['alpha','beta','chi','psi'],start=2):
        for partner in ['A_high','A_low','self']:
            v=[F(240),F(-1 if partner=='A_high' else 1),F(0),F(0),F(0),F(0)]
            v[r]=-1
            if partner=='self':v=[F(180),F(0),F(0),F(0),F(0),F(0)];v[r]=F(-1,2)
            alternatives.append({'homogeneous_corner':name,'other_mixed_corner':partner,'value_coefficients':[str(x) for x in v]})
    records=[]
    for r,name in enumerate(['alpha','beta','chi','psi'],start=2):
        v=list(S);v[0]=-360;v[r]-=1
        records.append({'kind':'opposite_B_mixed_joint','homogeneous_corner':name,'hyperplane_coefficients':canonical(v)})
    for x,y in itertools.product(range(12),repeat=2):
        vx=list(map(F,alternatives[x]['value_coefficients']));vy=list(map(F,alternatives[y]['value_coefficients']))
        v=add(add(vx,vy),S);v[0]-=720
        records.append({'kind':'separate_B0_B3_cover','B0_alternative':x,'B3_alternative':y,'hyperplane_coefficients':canonical(v)})
    assert len(records)==148
    classes={}
    for i,r in enumerate(records):classes.setdefault(r['hyperplane_coefficients'],[]).append(i)
    assert sum(map(len,classes.values()))==148
    # Every variable-coordinate hyperplane has nonzero homogeneous-angle part.
    assert all(any(k[2:]) for k in classes)
    homogeneous=[]
    for j in [2,4]:
        for m in range(4):
            v=[F(-360),F(0),F(0),F(0),F(0),F(0)];v[j]=m;v[j+1]=3-m
            k=canonical(v);assert k not in classes;homogeneous.append(k)
    assert len(set(homogeneous))==8
    out={'homogeneous_resonance_vectors_disjoint_from72':homogeneous,'domain':'delta0..30;nativeBhomogeneousangles0..180;actual strictconvexclosed binaryp!=q shapes only',
         'coefficient_order':['constant','delta','alpha','beta','chi','psi'],
         'mixed_sum':'B0+B3=720-alpha-beta-chi-psi',
         'raw_prespecified_domain':'4 opposite-mixed joint covers plus12x12 separate covers, no symmetry quotient before retention',
         'mixed_value_alternatives':alternatives,'all148_cover_eliminations':records,
         'canonical_hyperplanes':[{'coefficients':k,'raw_record_indices':idx} for k,idx in sorted(classes.items())],
         'distinct_hyperplane_count':len(classes),'claim':'necessary union only; outside union unrestricted untileable via admitted trivalent limit; no sufficiency on union'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS148completecovereliminations;distinctproperhyperplanes',len(classes));return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();inventory(args.output)
