"""Exact analytical M determinant gate and ONE hand-derived strict fixture.
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
uY=AA(QQ(2)/5);hY=ratio*uY
mX=uX+QQ(337)/1000*hX;mY=uY+QQ(708)/1000*hY
params={'X':(uX,hX,mX),'Y':(uY,hY,mY)}
assert all(0<u<m<1 and h>0 for u,h,m in params.values())
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
records=[];source=[]
for species,cS,sS in [('thin',c,s),('thick',c72,s72)]:
    V=[(AA(0),AA(0)),(AA(1),AA(0)),(1+cS,sS),(cS,sS)]
    for parity in (0,1):
        donor={}
        for edge in range(parity,4,2):
            T,H,Z=ARROWS[species][edge];u,h,m=params[Z]
            direction=sub(V[H],V[T]);e=sub(V[(edge+1)%4],V[edge])
            donor[edge]=add(add(V[T],mul(direction,u)),mul((-e[1],e[0]),h))
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
            assert convex([M,donor[(edge+1)%4],donor[(edge-1)%4]])
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
                records.append(dict(species=species,parity=parity,receiver=edge,endpoint=endpoint,mark=Z,role='tail' if endpoint==T else 'head',adjacent_donor_mark=DZ,adjacent_donor_endpoint=donor_role,source_angle=(36 if endpoint%2==0 else 144) if species=='thin' else (72 if endpoint%2==0 else 108),strict=True,normalized_D_sign=1 if D>0 else -1))
# Cotangent at external apex in triangle(T,M,t). Cot is decreasing on(0,180).
# cos108=-cos72,sin108=sin72.
for Z,(u,h,m) in params.items():
    cot_tail=(h*h-u*(m-u))/(h*m)
    assert cot_tail<(-c72)/s72
result=dict(status='PASS',domain='one exact analytic fixture,all16strictquads,both externaltailangles>108',parameters=dict(tan_beta='1/100',uY='2/5',kX='337/1000',kY='708/1000'),source_partitions=source,records=records)
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();print(json.dumps(result,indent=2))
if args.output:
    from pathlib import Path
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
