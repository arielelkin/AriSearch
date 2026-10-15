"""Exact geometry of ONE retained rational-angle off-normal fixture.
No metric/congruence parameter search. Cyclotomic60, all4 source cases.
"""
import argparse,json
from sage.all import QQbar,AA
z=QQbar.zeta(60);ii=z**15
C=lambda n:AA((z**n+z**(-n))/2)
S=lambda n:AA((z**n-z**(-n))/(2*ii))
cot=lambda n:C(n)/S(n)
h=1/(cot(1)+cot(7));u=h*cot(1);m=u+h*cot(9)
assert 0<u<m<1 and h>0
# Exact source triangle and split-angle verification, avoiding decimals.
assert u/h==cot(1) and (1-u)/h==cot(7)
assert (m-u)/h==cot(9)

def add(a,b):return tuple(a[j]+b[j] for j in (0,1))
def sub(a,b):return tuple(a[j]-b[j] for j in (0,1))
def scale(a,k):return tuple(x*k for x in a)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def cornercot(poly,i):
    p=poly[i];a=sub(poly[(i-1)%len(poly)],p);b=sub(poly[(i+1)%len(poly)],p)
    den=abs(cross(a,b));assert den>0
    return sum(a[j]*b[j] for j in (0,1))/den

def convex(poly):
    values=[]
    for i,p in enumerate(poly):
        e=sub(poly[(i+1)%len(poly)],p)
        for j,q in enumerate(poly):
            if j not in (i,(i+1)%len(poly)):values.append(cross(e,sub(q,p)))
    return all(v>0 for v in values) or all(v<0 for v in values)

def degrees_if_grid(value):
    return next((6*n for n in range(1,30) if value==cot(n)),None)

marks={'thin':('X','X','Y','Y'),'thick':('X','Y','Y','X')}
ARROWS={'thin':[(0,1),(2,1),(2,3),(0,3)],'thick':[(0,1),(1,2),(3,2),(0,3)]}
def area(poly):return abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2)
def separated(P,Q):
    for poly in (P,Q):
        for i,a in enumerate(poly):
            e=sub(poly[(i+1)%len(poly)],a);n=(-e[1],e[0])
            proj=lambda point:sum(point[j]*n[j] for j in (0,1))
            pvals=list(map(proj,P));qvals=list(map(proj,Q))
            if max(pvals)<=min(qvals) or max(qvals)<=min(pvals):return True
    return False
records=[];source_records=[]
for species,n in [('thin',6),('thick',12)]:
    c,s=C(n),S(n)
    V=[(AA(0),AA(0)),(AA(1),AA(0)),(1+c,s),(c,s)]
    for parity in (0,1):
        donor={}
        for edge in range(parity,4,2):
            T,H=ARROWS[species][edge];a=sub(V[H],V[T]);e=sub(V[(edge+1)%4],V[edge])
            donor[edge]=add(add(V[T],scale(a,u)),scale((-e[1],e[0]),h))
        cells=[]
        for edge,p in donor.items():cells.append([V[edge],V[(edge+1)%4],p])
        for edge in range(1-parity,4,2):cells.append([V[edge],V[(edge+1)%4],donor[(edge+1)%4],donor[(edge-1)%4]])
        from itertools import combinations
        source_ok=all(convex(poly) for poly in cells) and all(separated(P,Q) for P,Q in combinations(cells,2)) and sum(area(poly) for poly in cells)==s
        # Every source-cell vertex lies in its source rhomb.
        source_ok=source_ok and all(cross(sub(V[(i+1)%4],V[i]),sub(point,V[i]))>=0 for poly in cells for point in poly for i in range(4))
        source_records.append(dict(species=species,parity=parity,strict_cells_disjoint_cover=bool(source_ok)))
        for edge in range(1-parity,4,2):
            T,H=ARROWS[species][edge];a=sub(V[H],V[T]);e=sub(V[(edge+1)%4],V[edge])
            t=add(add(V[T],scale(a,u)),scale((e[1],-e[0]),h))
            M=add(V[T],scale(a,m));p=donor[(edge-1)%4];q=donor[(edge+1)%4]
            assert convex([M,q,p])
            left=[V[edge],t,M,p];right=[V[(edge+1)%4],t,M,q]
            for endpoint,poly in [(edge,left),((edge+1)%4,right)]:
                strict=convex(poly)
                value=cornercot(poly,2)
                turns=[cross(sub(poly[(i+1)%4],poly[i]),sub(poly[(i+2)%4],poly[(i+1)%4])) for i in range(4)]
                signs=[1 if x>0 else -1 if x<0 else 0 for x in turns]
                incoming='tail' if endpoint==T else 'head';Z=marks[species][edge]
                expected_alpha=(36 if incoming=='tail' else 144) if species=='thin' else (144 if Z=='X' and incoming=='head' else 72)
                expected_theta=120 if incoming=='tail' else 12
                expected_inner=360-expected_alpha-expected_theta-156
                records.append(dict(species=species,parity=parity,receiver=edge,endpoint=endpoint,strict_convex=strict,consecutive_turn_signs=signs,minor_M_ray_angle_matches_156=value==cot(26),minor_M_ray_angle_exact_six_degree_grid=degrees_if_grid(value),required_internal_angle=expected_inner,actual_internal_matches_required=(cornercot(poly,3)==cot(expected_inner//6)) if strict else None))
delta=h*(1-m)*(1+C(6))+S(6)*((u-m)*(1-u)-h*h)
from sage.all import QQ
assert QQ(-3254)/10**6<delta<QQ(-3253)/10**6
assert h*(1-m)>0
assert next(r for r in records if r['species']=='thick' and r['parity']==0 and r['receiver']==3 and r['endpoint']==0)['minor_M_ray_angle_exact_six_degree_grid']==108
result=dict(counterexample_delta_M_interval=['-3254/1000000','-3253/1000000'],status='PASS' if all(r['strict_convex'] and r['minor_M_ray_angle_matches_156'] for r in records) else 'FAIL_THIS_ONE_ANGLE_WITNESS',domain='one exact base6/head42/theta120+12 fixture, 16 actual precursor quads',source_partitions=source_records,records=records)
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
print(json.dumps(result,indent=2))
if args.output:
    from pathlib import Path
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
