#!/usr/bin/env python3
"""Independent fixed rational pentagon/carrier audit. No author imports."""
from fractions import Fraction as F
import json
import argparse

def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(poly): return sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1]))/2

def turns(poly):
    return [cross(sub(poly[(i+1)%len(poly)],poly[i]),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)])) for i in range(len(poly))]

def clip(poly, cutter):
    for a,b in zip(cutter,cutter[1:]+cutter[:1]):
        out=[]
        for x,y in zip(poly,poly[1:]+poly[:1]):
            dx=cross(sub(b,a),sub(x,a)); dy=cross(sub(b,a),sub(y,a))
            if dx>=0: out.append(x)
            if (dx<0<dy) or (dy<0<dx) or (dx<0 and dy==0) or (dy<0 and dx==0):
                t=dx/(dx-dy)
                z=add(x,(t*(y[0]-x[0]),t*(y[1]-x[1])))
                out.append(z)
        poly=out
        if not poly: return []
    return poly

def carrier_check(atom,h,hexagon):
    assert all(t>0 for t in turns(atom))
    assert all(t>0 for t in turns(hexagon))
    assert area(hexagon)==2*area(atom)>0
    assert all(hexagon[i+3]==h(hexagon[i]) for i in range(3))
    mirror=[h(x) for x in atom]
    assert abs(area(clip(atom,mirror)))==0
    assert abs(area(clip(atom,hexagon)))==area(atom)
    assert abs(area(clip(mirror,hexagon)))==area(atom)
    es=[sub(hexagon[(i+1)%6],hexagon[i]) for i in range(6)]
    assert all(es[i+3]==(-es[i][0],-es[i][1]) for i in range(3))
    u=add(es[0],es[1]); v=add(es[1],es[2]); determinant=cross(u,v)
    assert determinant==area(hexagon)>0
    coordinates=[(cross(x,v)/determinant,cross(u,x)/determinant) for x in hexagon]
    ranges=[max(x[k] for x in coordinates)-min(x[k] for x in coordinates) for k in (0,1)]
    bounds=[r.numerator//r.denominator+1 for r in ranges]
    checked=0
    for m in range(-bounds[0],bounds[0]+1):
        for n in range(-bounds[1],bounds[1]+1):
            if (m,n)==(0,0): continue
            offset=(m*u[0]+n*v[0],m*u[1]+n*v[1])
            moved=[add(x,offset) for x in hexagon]
            intersection=clip(hexagon,moved)
            assert not intersection or abs(area(intersection))==0
            checked+=1
    # Any omitted lattice displacement is outside a necessary coordinate-range
    # intersection bound. Pairwise interior disjointness and exact lattice
    # covolume equality imply full covering (a positive-area gap is impossible).
    return dict(atom_area=str(area(atom)),carrier_area=str(area(hexagon)),
                carrier=[[str(z) for z in x] for x in hexagon],
                periods=[[str(z) for z in x] for x in (u,v)],
                coordinate_ranges=list(map(str,ranges)),bounded_overlap_checks=checked)

def main():
    S=(F(1,6),F(1,3)); R=(F(1),F(1)); A=(F(1,2),F(0)); E=(F(0),F(1,2))
    P=[S,A,(F(2),F(0)),(F(2),F(1)),R]
    Q=[S,R,(F(1),F(2)),(F(0),F(2)),E]
    hp=lambda x:(4-x[0],1-x[1])
    hq=lambda x:(1-x[0],4-x[1])
    H=[R,S,A,hp(R),hp(S),hp(A)]
    K=[E,S,R,hq(E),hq(S),hq(R)]
    assert area(P)!=area(Q)
    assert all(0<=x<=2 and 0<=y<=1 and x+y>=F(1,2) for x,y in P)
    assert all(0<=x<=1 and 0<=y<=2 and x+y>=F(1,2) for x,y in Q)
    # Convexity extends these linear containment bounds to each whole atom.
    assert abs(area(clip(P,Q)))==0
    assert area(P)+area(Q)==F(23,8)
    cells={(0,0),(1,0),(0,1)}
    placements=[cells,{(x+1,y+1) for x,y in cells},
                {(3-y,x) for x,y in cells},{(y,3-x) for x,y in cells}]
    assert sum(map(len,placements))==len(set().union(*placements))==12
    assert set().union(*placements)=={(x,y) for x in range(4) for y in range(4) if x<2 or y<2}
    w=(F(3,4),F(1,16))
    # C={0<=x,y<=2; x<=1 or y<=1; x+y>=1/2}.
    assert 0<w[0]<2 and 0<w[1]<1 and w[0]+w[1]>F(1,2)
    assert w[0]+w[1]<1 # w is outside doubled C, independent of all other children.
    result={'status':'VALID fixed-pair monohedral periodic escape; INVALID four-chair scale2 assembly',
            'P':carrier_check(P,hp,H),'Q':carrier_check(Q,hq,K),
            'parent_area':'23/8','scale2_protrusion_w':list(map(str,w))}
    parser=argparse.ArgumentParser(); parser.add_argument('--output'); args=parser.parse_args()
    rendered=json.dumps(result,indent=2)+'\n'
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(rendered)
    print(rendered,end='')

if __name__=='__main__': main()
