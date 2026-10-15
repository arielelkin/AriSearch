"""Exact identical-donor precursor fixture with context-dependent cuts allowed.
No random/grid/metric/congruence search. All4 source cases,16 receiving quads.
"""
import argparse,json
from itertools import combinations
from sage.all import QQbar,AA,QQ
z=QQbar.zeta(20);ii=z**5
c=AA((z**2+z**-2)/2);s=AA((z**2-z**-2)/(2*ii))
c72=2*c*c-1;s72=2*s*c
ratio=QQ(1)/100
uX=(s+ratio*c)/(s*(1-ratio*ratio)+2*ratio*c);hX=ratio*uX
uY=uX;hY=hX
mX=uX*((1+ratio*ratio)/(1+ratio*s/(1+c))+QQ(1)/10**6);mY=mX
params={'X':(uX,hX,mX),'Y':(uY,hY,mY)}
assert all(0<m<u<1 and h>0 for u,h,m in params.values())
# tan(head_X)=tan(beta+36), exactly; both tail base slopes equal.
assert hX/(1-uX)==(ratio+s/c)/(1-ratio*s/c)

def add(a,b):return tuple(a[i]+b[i] for i in (0,1))
def sub(a,b):return tuple(a[i]-b[i] for i in (0,1))
def mul(a,k):return tuple(x*k for x in a)
def dot(a,b):return sum(a[i]*b[i] for i in (0,1))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2)
def convex(poly):
    values=[]
    for i,a in enumerate(poly):
        e=sub(poly[(i+1)%len(poly)],a)
        for j,b in enumerate(poly):
            if j not in (i,(i+1)%len(poly)):values.append(cross(e,sub(b,a)))
    return all(v>0 for v in values) or all(v<0 for v in values)
def separated(P,Q):
    for poly in (P,Q):
        for i,a in enumerate(poly):
            e=sub(poly[(i+1)%len(poly)],a);n=(-e[1],e[0])
            p=[dot(v,n) for v in P];q=[dot(v,n) for v in Q]
            if max(p)<=min(q) or max(q)<=min(p):return True
    return False
ARROWS={'thin':[(0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')],
        'thick':[(0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')]}
records=[];source=[];receiving_partitions=[];central=[]
for species,cS,sS in [('thin',c,s),('thick',c72,s72)]:
    V=[(AA(0),AA(0)),(AA(1),AA(0)),(1+cS,sS),(cS,sS)]
    for parity in (0,1):
        donor={}
        for edge in range(parity,4,2):
            T,H,Z=ARROWS[species][edge];u,h,m=params[Z]
            direction=sub(V[H],V[T]);e=sub(V[(edge+1)%4],V[edge])
            donor[edge]=add(add(V[T],mul(direction,u)),mul((-e[1],e[0]),h))
        assert all(cross(sub(V[(i+1)%4],V[i]),sub(p,V[i]))>0 for p in donor.values() for i in range(4))
        cells=[[V[e],V[(e+1)%4],p] for e,p in donor.items()]
        cells += [[V[e],V[(e+1)%4],donor[(e+1)%4],donor[(e-1)%4]] for e in range(1-parity,4,2)]
        valid=all(convex(P) for P in cells) and all(separated(P,Q) for P,Q in combinations(cells,2)) and sum(area(P) for P in cells)==sS
        valid=valid and all(cross(sub(V[(i+1)%4],V[i]),sub(p,V[i]))>=0 for P in cells for p in P for i in range(4))
        assert valid;source.append(dict(species=species,parity=parity,valid=True))
        for edge in range(1-parity,4,2):
            T,H,Z=ARROWS[species][edge];u,h,m=params[Z]
            a=sub(V[H],V[T]);e=sub(V[(edge+1)%4],V[edge]);n=(-e[1],e[0])
            t=add(add(V[T],mul(a,u)),mul(n,-h));M=add(V[T],mul(a,m))
            pts={edge:donor[(edge-1)%4],(edge+1)%4:donor[(edge+1)%4]}
            C=[M,donor[(edge+1)%4],donor[(edge-1)%4]]
            assert convex(C)
            central.append(dict(species=species,parity=parity,receiver=edge,strict=True))
            Qs=[[V[endpoint],t,M,p] for endpoint,p in pts.items()]
            old_sector=[V[edge],V[(edge+1)%4],donor[(edge+1)%4],donor[(edge-1)%4]]
            external=[V[edge],V[(edge+1)%4],t]
            assert all(separated(P,Q) for P,Q in combinations(Qs+[C],2))
            assert sum(area(P) for P in Qs+[C])==area(old_sector)+area(external)
            # Each quad splits along the retained-endpoint-to-M diagonal into
            # one external-donor triangle and one original-sector triangle.
            def inside(poly,point):
                signs=[cross(sub(poly[(i+1)%len(poly)],poly[i]),sub(point,poly[i])) for i in range(len(poly))]
                return all(x>=0 for x in signs) or all(x<=0 for x in signs)
            for endpoint,p in pts.items():
                assert all(inside(external,x) for x in (V[endpoint],t,M))
                assert all(inside(old_sector,x) for x in (V[endpoint],M,p))
            assert all(inside(old_sector,x) for x in C)
            receiving_partitions.append(dict(species=species,parity=parity,receiver=edge,pairwise_disjoint=True,area_identity=True,contained_by_diagonal_splits=True))
            for endpoint,p in pts.items():
                Q=[V[endpoint],t,M,p];assert convex(Q)
                x=dot(sub(p,V[T]),a);y=dot(sub(p,V[T]),n);assert y>0
                other=(endpoint-1)%4 if endpoint==edge else endpoint
                DT,DH,DZ=ARROWS[species][other];du,dg,dm=params[DZ]
                donor_role='tail' if endpoint==DT else 'head'
                projection=du if donor_role=='tail' else 1-du
                cs=cS if endpoint%2==0 else -cS
                sn=sS
                local_x=projection*cs+dg*sn;local_y=projection*sn-dg*cs
                assert y==local_y and x==(local_x if endpoint==T else 1-local_x)
                D=m*(y+h)-u*y-h*x
                assert D>0 if endpoint==T else D<0
                from sage.all import RealIntervalField
                MR=RealIntervalField(80)
                mcot=dot(sub(t,M),sub(p,M))/abs(cross(sub(t,M),sub(p,M)))
                Mdegrees=90-MR(mcot).arctan()*180/MR.pi()
                records.append(dict(retained_M_degrees_display=str(Mdegrees),species=species,parity=parity,receiver=edge,endpoint=endpoint,mark=Z,role='tail' if endpoint==T else 'head',adjacent_donor_mark=DZ,adjacent_donor_endpoint=donor_role,source_angle=(36 if endpoint%2==0 else 144) if species=='thin' else (72 if endpoint%2==0 else 108),strict=True,normalized_D_sign=1 if D>0 else -1))
# Direct exact precursor inequalities and external donor half-angle gate.
# Cotangents decrease strictly on (0,180); no floating-point decision.
u,h,m=params['X']
cot_tail=(h*h-u*(m-u))/(h*m)
cot_head=(h*h+(1-u)*(m-u))/(h*(1-m))
assert cot_tail>0 and cot_tail<c72/s72  # 72 < theta_tail < 90
cot54=s/c                         # tan36=cot54
assert cot_head<cot54 and cot_head>0 # 54 < theta_head < 90
assert m < u-h*h/u
assert 0 < ratio < (1-c)/s        # beta < 18, actually beta < 9 separately
from sage.all import RealIntervalField
R=RealIntervalField(80)
beta=R(ratio).arctan()*180/R.pi()
assert beta.upper()<9
tail=R(cot_tail).arctan()*180/R.pi()
tail=90-tail
head=R(cot_head).arctan()*180/R.pi()
head=90-head
# This point is chosen analytically just above the strict thin-tail
# boundary, to challenge a universal cross-tail M<108 assertion.
C=2*c*c-1;S=2*c*s
p=(-(1-u)*C+h*S,(1-u)*S+h*C)
a=(u-m,-h);b=(p[0]-m,p[1])
Mdot=dot(a,b);Mdet=abs(cross(a,b));Mcot=Mdot/Mdet
assert Mcot < -C/S # retained cross-tail M strictly greater than108
Mangle=90-R(Mcot).arctan()*180/R.pi()
assert m>QQ(1)/2
result=dict(status='PASS_PRECURSOR_ONLY',common_H_gate='FAIL: m>1/2 contradicts unique36/72 opposite-diagonal metric constraint' ,domain='one exact identical-donor fixture; all16 strict quads,4 source partitions,8 central triangles,8 receiving partitions',
 parameters=dict(tan_beta='1/100',cos36='(1+sqrt(5))/4',sin36='sqrt(10-2*sqrt(5))/4',
 u='(sin36+tan_beta*cos36)/(sin36*(1-tan_beta^2)+2*tan_beta*cos36)',h='u/100',m='u*((1+r^2)/(1+r*tan18)+1/1000000)',X_equals_Y=True),
 exact_inequalities=dict(tail_angle_between_72_and_90=True,head_angle_between_54_and_90=True,m_less_than_u_minus_h_squared_over_u=True),
 display_intervals_only=dict(beta=str(beta),tail=str(tail),head=str(head),cross_tail_M=str(Mangle)),
 source_partitions=source,central_triangles=central,receiving_partitions=receiving_partitions,records=records)
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();print(json.dumps(result,indent=2))
if args.output:
    from pathlib import Path
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
