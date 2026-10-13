#!/usr/bin/env python3
"""Independent exact one-seam and repaired-kink audit; no author imports."""
from sage.all import CyclotomicField, QQbar, AA, QQ
import json
import argparse

F=CyclotomicField(10); w=F.gen(); embed=F.hom([QQbar.zeta(10)])
def xy(z):
    v=embed(z); return (AA(v.real()),AA(v.imag()))
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(poly): return sum(cross(x,y) for x,y in zip(poly,poly[1:]+poly[:1]))/2
def turns(poly): return [cross(sub(poly[(i+1)%len(poly)],poly[i]),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)])) for i in range(len(poly))]
def hull(points):
    ps=sorted(set(points)); lo=[]; hi=[]
    for p in ps:
        while len(lo)>=2 and cross(sub(lo[-1],lo[-2]),sub(p,lo[-1]))<=0: lo.pop()
        lo.append(p)
    for p in ps[::-1]:
        while len(hi)>=2 and cross(sub(hi[-1],hi[-2]),sub(p,hi[-1]))<=0: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def enc(z): return list(map(str,F(z).vector()))

def main():
    j=QQ(1)/2+QQ(4)/5*w
    v=1+w**4*(j-1); k=w**2+w**6*(j-1)
    h=[F(0),v,F(1),j,w,w+w**6*(j-w)]
    p=[F(0),v,F(1),1+w**7*(j-1-w),k]
    rot=v/k; assert rot*rot.conjugate()==1 and rot*k==v
    cp=rot*sum(p)/5; ch=sum(h)/6
    Q=[F(0),cp,v,ch]; coords=list(map(xy,Q))
    assert cross(xy(v),xy(ch))>0 and cross(xy(v),xy(cp))<0
    assert all(x>0 for x in turns(coords))
    U,V=v,ch; m=(U+V)/2-QQ(1)/1000*(w-w.conjugate())*(V-U)
    T=[v,F(1),ch]; tcoords=list(map(xy,T)); mcoords=xy(m)
    assert all(cross(sub(b,a),sub(mcoords,a))>0 for a,b in zip(tcoords,tcoords[1:]+tcoords[:1]))
    newq=list(map(xy,[F(0),cp,v,m,ch])); newt=list(map(xy,[v,F(1),ch,m]))
    assert all(x>0 for x in turns(newq))
    assert turns(newt)[2]<0
    assert area(newq)+area(newt)==area(coords)+area(tcoords)
    # Independent convex-halfturn carrier; choose first suitable FIXED side.
    carriers=[]
    for i in range(4):
        centre=Q[i]+Q[(i+1)%4]
        opposite=[centre-z for z in Q]
        carrier=hull(coords+list(map(xy,opposite)))
        if area(carrier)==2*area(coords): carriers.append((i,carrier))
    assert carriers
    side,H=carriers[0]; assert len(H) in (4,6)
    assert all(x>0 for x in turns(H))
    # Area equality proves convex carrier equals glued union: both polygons
    # are inside hull, and their interiors are opposite across the glue line.
    midpoint=(xy(Q[side])[0]+xy(Q[(side+1)%4])[0],xy(Q[side])[1]+xy(Q[(side+1)%4])[1])
    n=len(H); assert all((H[i][0]+H[(i+n//2)%n][0],H[i][1]+H[(i+n//2)%n][1])==midpoint for i in range(n))
    # Convex centrally symmetric 4/6-gons tile by translations (standard
    # hexagon opposite-side pairing; detailed independent packing in B audit).
    result={'status':'VALID exact local crossed convex diamond and INVALID convex-only kink repair',
            'diamond_turn_signs':[int(x.sign()) for x in turns(coords)],
            'repaired_diamond_turn_signs':[int(x.sign()) for x in turns(newq)],
            'neighbor_at_M':int(turns(newt)[2].sign()),
            'M_inside_neighbor_fan':True,'exact_area_conserved':True,
            'fixed_omission_carrier_glue_side':side,'carrier_corner_count':n,
            'diamond_field_vertices':[enc(z) for z in Q],
            'kink_field_vertex':enc(m),
            'scope':'one required source seam and one repair; global topological covering proved analytically, no global convexity or two-class census'}
    parser=argparse.ArgumentParser(); parser.add_argument('--output'); a=parser.parse_args()
    rendered=json.dumps(result,indent=2)+'\n'
    if a.output:
        from pathlib import Path
        Path(a.output).write_text(rendered)
    print(rendered,end='')

if __name__=='__main__': main()
