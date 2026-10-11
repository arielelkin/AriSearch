#!/usr/bin/env python3
"""Fresh exact AA audit of three-angle pentagon periodic counterexamples.

Independent of author radical arithmetic and endpoint union-find. Coordinates
are rederived from unit directions. Corner links use a permutation. Residual
seam holonomies determine a lattice; a complete exact overlap domain and area
identity certify full-plane coverage. No search size supports aperiodicity.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
from sage.all import AA, QQ, QQbar, NumberField, PolynomialRing, matrix, sqrt, vector

ROOT = Path(__file__).resolve().parents[2]
PAIRS = [((0,0),(2,4)), ((0,2),(2,1)), ((1,0),(3,4)), ((1,2),(3,1)),
         ((2,0),(1,4)), ((2,2),(1,1)), ((3,0),(0,4)), ((3,2),(0,1)),
         ((0,3),(1,3)), ((2,3),(3,3))]
IDENT = matrix(AA, [[1,0],[0,1]])
ZERO = vector(AA, [0,0])

def det(u,v):
    return u[0]*v[1]-u[1]*v[0]

def derive(k,t,s):
    h = (1-k*k).sqrt()
    a,b,c = h, (1-2*k*k)/(2*k), h/(2*k)
    unit = [vector(AA,z) for z in ((1,0),(k,h),(-h,k),
                                   (-2*k*h,2*k*k-1),(0,-1))]
    assert all(u.dot_product(u) == 1 for u in unit)
    assert 0 < k < AA(2).sqrt()/2
    lengths = [c*t+s/2,a*t+b*s,b*t+a*s,t,t/2+c*s]
    assert all(z > 0 for z in lengths)
    edges = [z*u for z,u in zip(lengths,unit)]
    vertices = [ZERO]
    for e in edges:
        vertices.append(vertices[-1]+e)
    assert vertices[-1] == ZERO
    vertices.pop()
    for i,e in enumerate(edges):
        assert e.dot_product(e) == lengths[i]**2
        assert all(det(e, vertices[j]-vertices[i]) > 0 for j in range(5)
                   if j not in (i,(i+1)%5))
    # Native angles at v_i are R,theta,R,theta,2pi-2theta.
    # Check all exact cosines at those vertices.
    cosines = [AA(0),-k,AA(0),-k,2*k*k-1]
    for i in range(5):
        prev,nxt = edges[(i-1)%5],edges[i]
        assert -prev.dot_product(nxt) == cosines[i]*lengths[(i-1)%5]*lengths[i]
        assert det(prev,nxt) > 0
    return lengths,vertices,edges

def decode(row):
    return sum(QQ(coefficient)*AA(int(radicand)).sqrt()
               for radicand,coefficient in row.items())

def audit(k,filename,scale=AA(1)):
    assert scale > 0
    t,s = scale,scale*AA(5).sqrt()
    geometry = [derive(k,t,s),derive(k,s,t)]
    lengths = [g[0] for g in geometry]
    assert len(set(lengths[0]+lengths[1])) == 6
    assert t not in lengths[1] and s not in lengths[0]
    assert t/s not in QQ
    if scale == AA(2).sqrt():
        assert t*t == 2 and s*s == 10
        assert t not in QQ and s not in QQ
    faces = [0,0,1,1]
    if filename is not None:
        data = json.loads((ROOT/'research/certificates'/filename).read_text())
        assert [[list(u),list(v)] for u,v in PAIRS] == data['torus_pairings']
        for g,encoded in zip(geometry,data['prototype_geometry']):
            assert g[0] == [scale*decode(z) for z in encoded['side_lengths']]
            assert g[1] == [scale*vector(AA,[decode(x),decode(y)])
                           for x,y in encoded['vertices']]
    twin,adj = {},{f:[] for f in range(4)}
    for (f,i),(g,j) in PAIRS:
        assert (f,i) not in twin and (g,j) not in twin
        assert lengths[faces[f]][i] == lengths[faces[g]][j]
        twin[f,i],twin[g,j] = (g,j),(f,i)
        adj[f].append((g,i,j))
        adj[g].append((f,j,i))
    domain = {(f,i) for f in range(4) for i in range(5)}
    assert set(twin) == domain
    successor = {z:(twin[z][0],(twin[z][1]+1)%5) for z in domain}
    assert set(successor.values()) == domain
    unseen,cycles = set(domain),[]
    while unseen:
        start=min(unseen)
        cycle=[start]
        nxt=successor[start]
        while nxt != start:
            assert nxt not in cycle
            cycle.append(nxt)
            nxt=successor[nxt]
        unseen.difference_update(cycle)
        cycles.append(cycle)
    assert Counter(map(len,cycles)) == {3:4,4:2}
    # Angles as exact coefficients of pi and theta, no angle approximation.
    affine = [(QQ(1)/2,0),(0,1),(QQ(1)/2,0),(0,1),(2,-2)]
    for cycle in cycles:
        assert sum(affine[i][0] for f,i in cycle) == 2
        assert sum(affine[i][1] for f,i in cycle) == 0
    assert len(cycles)-len(PAIRS)+4 == 0
    if filename is not None:
        assert {tuple(sorted(c)) for c in cycles} == {
            tuple(map(tuple,c)) for c in data['torus_vertex_classes']}
    def compose(a,b):
        return a[0]*b[0],a[0]*b[1]+a[1]
    def inverse(a):
        m=a[0].inverse()
        return m,-m*a[1]
    def relative(f,i,g,j):
        gl,gv,ge = geometry[faces[g]]
        fl,fv,fe = geometry[faces[f]]
        src,target = ge[j],-fe[i]
        norm = src.dot_product(src)
        co,si = src.dot_product(target)/norm,det(src,target)/norm
        m = matrix(AA,[[co,-si],[si,co]])
        b = fv[(i+1)%5]-m*gv[j]
        assert m.transpose()*m == IDENT and m.det() == 1
        assert m*gv[(j+1)%5]+b == fv[i]
        return m,b
    placements={0:(IDENT,ZERO)}
    queue=[0]
    while queue:
        f=queue.pop(0)
        for g,i,j in adj[f]:
            if g not in placements:
                placements[g]=compose(placements[f],relative(f,i,g,j))
                queue.append(g)
    assert len(placements) == 4
    periods=[]
    for (f,i),(g,j) in PAIRS:
        m,b=compose(compose(placements[f],relative(f,i,g,j)),inverse(placements[g]))
        assert m == IDENT
        if b != ZERO:
            periods.append(b)
    motif=[[placements[f][0]*z+placements[f][1] for z in geometry[faces[f]][1]]
           for f in range(4)]
    individual_areas=[sum(det(g[1][i],g[1][(i+1)%5]) for i in range(5))/2
                      for g in geometry]
    if k == AA(2)/5:
        expected=[QQ(101)/100*AA(21).sqrt()+QQ(861)/400*AA(5).sqrt(),
                  QQ(151)/100*AA(21).sqrt()+QQ(861)/400*AA(5).sqrt()]
        assert individual_areas == [scale*scale*z for z in expected]
        assert individual_areas[0]/individual_areas[1] not in QQ
    area=sum(sum(det(poly[i],poly[(i+1)%5]) for i in range(5))/2 for poly in motif)
    assert area > 0
    bases=[]
    for u,v in combinations(periods,2):
        m=matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
        if abs(m.det()) != area:
            continue
        inv=m.inverse()
        if all(all(x in QQ and QQ(x).denominator()==1 for x in inv*b) for b in periods):
            bases.append((u,v,m,inv))
    assert bases, 'no complete primitive lattice basis derived from seam holonomy'
    u,v,m,inv=bases[0]
    boxes=[]
    for poly in motif:
        coords=[inv*z for z in poly]
        boxes.append([(min(z[d] for z in coords),max(z[d] for z in coords)) for d in (0,1)])
    def separated(poly,other):
        return any(all(det(poly[(i+1)%5]-poly[i],z-poly[i])<=0 for z in other)
                   for i in range(5))
    checked=0
    for f in range(4):
        for g in range(4):
            ranges=[]
            for d in (0,1):
                lo=int((boxes[f][d][0]-boxes[g][d][1]).ceil())
                hi=int((boxes[f][d][1]-boxes[g][d][0]).floor())
                ranges.append(range(lo,hi+1))
            for n in ranges[0]:
                for r in ranges[1]:
                    if f==g and n==r==0:
                        continue
                    shifted=[z+n*u+r*v for z in motif[g]]
                    assert separated(motif[f],shifted) or separated(shifted,motif[f]),(f,g,n,r)
                    checked+=1
    print('PASS',filename or 'irrational-angle algebraic instance',
          '(scale '+str(QQbar(scale).radical_expression())+')' if scale != 1 else '',
          ': exact shapes; six circle links; rank-two holonomy; complete overlap domain',checked)
    def exact_text(z,factor=AA(1)):
        if k == AA(2)/5:
            # Use the small source field for readable independently checked
            # radicals. r=sqrt(21)+sqrt(5), r^2=26+2sqrt(105),
            # r^3=36sqrt(21)+68sqrt(5).
            ring=PolynomialRing(QQ,'x')
            x=ring.gen()
            field=NumberField(x**4-52*x**2+256,'r',
                              embedding=AA(21).sqrt()+AA(5).sqrt())
            coefficients=list(field(z/factor))
            coefficients += [QQ(0)]*(4-len(coefficients))
            c0,c1,c2,c3=coefficients
            radical_coefficients=[c0+26*c2,c1+68*c3,c1+36*c3,2*c2]
            assert all(c in QQ for c in radical_coefficients)
            if factor in QQ:
                expression=sum(QQ(factor)*c*sqrt(r) for c,r in
                               zip(radical_coefficients,[1,5,21,105]))
            else:
                assert factor*factor in QQ
                expression=sum(c*sqrt(QQ(factor*factor)*r) for c,r in
                               zip(radical_coefficients,[1,5,21,105]))
        else:
            expression=QQbar(z).radical_expression()
        assert AA(expression) == z
        return str(expression)
    print('exact lattice basis:',[exact_text(z,scale) for z in u],
          [exact_text(z,scale) for z in v],'; exact area:',exact_text(area,scale*scale))
    if scale != 1:
        print('private lengths:',exact_text(t,scale),exact_text(s,scale),
              '; both irrational; ratio irrational')
    return u,v,motif,individual_areas,boxes,checked

def main():
    audit((AA(6).sqrt()-AA(2).sqrt())/4,'new-angle-three-pentagon-counterexample.json')
    original=audit(AA(2)/5,'new-angle-three-pentagon-irrational-angle.json')
    scale=AA(2).sqrt()
    scaled=audit(AA(2)/5,'new-angle-three-pentagon-irrational-angle.json',scale)
    assert scaled[0] == scale*original[0] and scaled[1] == scale*original[1]
    assert scaled[2] == [[scale*z for z in poly] for poly in original[2]]
    assert scaled[3] == [scale*scale*a for a in original[3]]
    assert scaled[4:] == original[4:]  # Lattice boxes and complete domain unchanged.
    print('PASS exact sqrt(2) scaling: both private lengths irrational; all overlaps replayed')

if __name__=='__main__':
    main()
