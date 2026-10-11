#!/usr/bin/env python3
"""Fresh exact Q3 coordinate/clip audit, importing no author code.

Construct native walks independently; check actual quotient and all translates
whose inverse-lattice projection boxes can intersect. Exact AA clipping is
independent of the author's separating-axis method. Normal replay writes nothing.
"""
from itertools import product
from pathlib import Path
import json
from sage.all import AA, QQ, QQbar, CyclotomicField, vector

ROOT = Path(__file__).resolve().parents[2]
K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1
a = 2*phi-2
phia = (1+AA(5).sqrt())/2
s = (1-(phia/2)**2).sqrt()
embedding = K.hom([QQbar(phia/2)+QQbar.gen()*QQbar(s)], QQbar)

def walk(lengths, powers):
    points=[K(0)]
    for length,power in zip(lengths,powers):
        points.append(points[-1]+length*z**power)
    assert points[-1]==0
    return points[:-1]

def plane(p):
    q=embedding(p)
    return vector(AA,[q.real(),q.imag()])

def cross(p,q):
    return p[0]*q[1]-p[1]*q[0]

def area(poly):
    return sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2

def clipped(subject,clipper):
    result=list(subject)
    for j,b in enumerate(clipper):
        if not result:break
        edge=clipper[(j+1)%len(clipper)]-b
        previous=result[-1]
        hp=cross(edge,previous-b)
        next_result=[]
        for current in result:
            hc=cross(edge,current-b)
            if (hp<0 and hc>=0) or (hp>=0 and hc<0):
                next_result.append(previous+(current-previous)*hp/(hp-hc))
            if hc>=0:next_result.append(current)
            previous,hp=current,hc
        result=next_result
    return result

def coefficients(p):
    return list(map(str,list(p)+[QQ(0)]*(4-len(list(p)))))

def main():
    c=json.loads((ROOT/'research/certificates/new-octagon-q3-metric-deformation.json').read_text())
    pl=[a,phi,K(1),phi,a]
    ql=[phi**2,a,phi,phi**2,K(1),a,phi,phi]
    assert len({p for p in pl})==3
    assert phi**2 not in pl and ql.count(phi**2)==2
    q=walk(ql,[0,1,2,4,5,6,7,8])
    native_p=walk(pl,[0,2,4,6,8])
    p0=native_p
    p1=walk([pl[(1-j)%5] for j in range(5)],[0,2,4,6,8])
    H=q[3]+q[4]
    faces=[q,[H-t for t in q],
           [q[2]-z*t for t in p0],[q[3]-z**2*t for t in p1],
           [H-q[6]+z**6*t for t in p0],[H-q[7]+z**7*t for t in p1]]
    u=-3*phi+(7*phi-1)*z
    w=3*phi+4-2*phi**2*z
    assert H-q[1]==u
    assert [[coefficients(p) for p in face] for face in faces]==c['motif_coefficients']
    assert [coefficients(u),coefficients(w)]==c['period_coefficients']
    polys=[[plane(p) for p in face] for face in faces]
    for f,poly in enumerate(polys):
        assert area(poly)>0
        for j,p in enumerate(poly):
            edge=poly[(j+1)%len(poly)]-p
            for k,qpoint in enumerate(poly):
                if k not in (j,(j+1)%len(poly)):
                    assert cross(edge,qpoint-p)>0
            incoming=poly[(j-1)%len(poly)]-p
            expected=(1-phia)/2 if f>=2 or j in (0,3) else -phia/2
            actual=incoming.dot_product(edge)/(incoming.norm()*edge.norm())
            assert actual==expected
    # Native reflection/rotation tests: only identity preserves both Q data.
    qa=[3,4,4,3,4,4,4,4]
    sym=[]
    for k in range(8):
        if all(qa[(j+k)%8]==qa[j] and ql[(j+k)%8]==ql[j] for j in range(8)):
            sym.append(('rotation',k))
        if all(qa[(k-j)%8]==qa[j] and ql[(k-j-1)%8]==ql[j] for j in range(8)):
            sym.append(('reflection',k))
    assert sym==[('rotation',0)]
    mate={}
    adjacency={i:set() for i in range(6)}
    for i,h,j,g,n,m in c['whole_side_seams']:
        assert faces[i][h]==faces[j][(g+1)%len(faces[j])]+n*u+m*w
        assert faces[i][(h+1)%len(faces[i])]==faces[j][g]+n*u+m*w
        assert (i,h) not in mate and (j,g) not in mate
        mate[i,h]=(j,g,n,m)
        mate[j,g]=(i,h,-n,-m)
        adjacency[i].add(j);adjacency[j].add(i)
    assert len(mate)==36
    reached={0}
    while True:
        expanded=reached|set().union(*(adjacency[i] for i in reached))
        if expanded==reached:break
        reached=expanded
    assert len(reached)==6
    seen=set();cycles=[]
    for start in sorted(mate):
        if start in seen:continue
        current=start;cycle=[];shift=[0,0]
        while current not in seen:
            seen.add(current);cycle.append(current)
            j,g,n,m=mate[current]
            shift[0]+=n;shift[1]+=m
            current=(j,(g+1)%len(faces[j]))
        assert current==start and shift==[0,0] and len(cycle)==3
        assert sum(3 if f>=2 else qa[h] for f,h in cycle)==10
        cycles.append(cycle)
    assert len(cycles)==12 and 12-18+6==0
    assert {frozenset(t) for t in cycles}=={frozenset(map(tuple,t)) for t in c['actual_corner_links']}
    U,W=plane(u),plane(w)
    determinant=cross(U,W)
    assert determinant/s==-(34*phia+11)
    assert sum(area(p) for p in polys)==abs(determinant)
    assert area(polys[0])/s==(20*phia+13)/2
    assert area(polys[2])/s==(7*phia-1)/2
    def coordinates(p):
        return (cross(p,W)/determinant,cross(U,p)/determinant)
    boxes=[]
    for poly in polys:
        coords=[coordinates(p) for p in poly]
        boxes.append([(min(t[k] for t in coords),max(t[k] for t in coords)) for k in (0,1)])
    comparisons=[]
    for i,j in product(range(6),repeat=2):
        ranges=[range(int((boxes[i][k][0]-boxes[j][k][1]).ceil()),
                      int((boxes[i][k][1]-boxes[j][k][0]).floor())+1) for k in (0,1)]
        for n,m in product(*ranges):
            if i==j and n==m==0:continue
            cut=clipped(polys[i],[p+n*U+m*W for p in polys[j]])
            assert not cut or area(cut)==0,(i,j,n,m)
            comparisons.append([i,j,n,m])
    assert comparisons==c['complete_overlap_comparisons'] and len(comparisons)==36
    print('PASS independent Q3 walks, convexity, 18 seams, 12 zero-holonomy links, all36 exact clips and coverage density1')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
