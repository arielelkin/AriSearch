#!/usr/bin/env python3
"""Sage exact geometry and independent endpoint check of a specific Cairo pair."""
from sage.all import QuadraticField,QQ,AA
from pathlib import Path
from collections import defaultdict,Counter
import json
C=Path(__file__).resolve().parents[2]/'research/certificates/cairo-two-scalene-torus.json'

def main():
    c=json.loads(C.read_text())
    assert c['field']=={'polynomial':'x^2-3','root_interval':['1','2']}
    F=QuadraticField(3,'w',embedding=AA(3).sqrt());w=F.gen()
    assert 1<w<2 and w*w==3
    p=F(QQ(c['parameters']['p']));r=F(QQ(c['parameters']['r']))
    assert p==1 and r==QQ(1)/2
    q=w*p-r;s=2*p-w*r
    V={n:[tuple(QQ(z[0])+QQ(z[1])*w for z in v) for v in c[n]] for n in ('A','B')}
    L={'A':[q,p,p,q,r],'B':[p,q,q,p,s]}
    assert len(set([p,q,r,s]))==4 and all(x>0 for x in (p,q,r,s))
    det=lambda u,v:u[0]*v[1]-u[1]*v[0]
    sub=lambda u,v:(u[0]-v[0],u[1]-v[1])
    angles=[90,120,90,120,120]
    for n in ('A','B'):
        verts=V[n];edges=[sub(verts[(j+1)%5],verts[j]) for j in range(5)]
        assert len(verts)==5 and len(set(verts))==5
        for j,e in enumerate(edges):
            assert e[0]*e[0]+e[1]*e[1]==L[n][j]**2
            for k,v in enumerate(verts):
                val=det(e,sub(v,verts[j]))
                assert val==0 if k in (j,(j+1)%5) else val>0
            f=edges[(j+1)%5]
            dot=-(e[0]*f[0]+e[1]*f[1])
            assert det(e,f)>0
            assert dot==(0 if angles[j]==90 else -L[n][j]*L[n][(j+1)%5]/2)
    # No Type4 equality at either right corner; both prototile classes differ.
    assert q!=p
    assert r not in L['B'] and s not in L['A']
    # Private beta-beta side cannot split into two or more complete neighbor sides.
    assert r<2*min(L['A']) and s<2*min(L['B'])
    assert r not in (p,q) and s not in (p,q)
    faces=c['faces'];assert faces==['A','A','B','B']
    parents=list(range(20));used=[]
    def find(x):
        while parents[x]!=x:x=parents[x]
        return x
    def join(x,y):parents[find(x)]=find(y)
    for (f,i),(g,j) in c['reversed_endpoint_pairs']:
        assert L[faces[f]][i]==L[faces[g]][j]
        assert (f,i)!=(g,j)
        used.extend([(f,i),(g,j)])
        join(5*f+(i-1)%5,5*g+j);join(5*f+i,5*g+(j-1)%5)
    assert sorted(used)==[(f,j) for f in range(4) for j in range(5)]
    vs=defaultdict(list)
    for x in range(20):vs[find(x)].append(divmod(x,5))
    assert len(vs)==6 and Counter(len(v) for v in vs.values())=={3:4,4:2}
    assert all(sum(angles[j] for f,j in v)==360 for v in vs.values())
    seen={0}
    while True:
        new=seen|{g for (f,i),(g,j) in c['reversed_endpoint_pairs'] if f in seen}|{f for (f,i),(g,j) in c['reversed_endpoint_pairs'] if g in seen}
        if new==seen:break
        seen=new
    assert len(seen)==4 and len(vs)-len(c['reversed_endpoint_pairs'])+len(faces)==0
    # Independent algebraic check of the three-copy partial-contact diagnostic.
    a=V['A'];v4=a[4]
    patch=[a,[(v4[0]-u,v4[1]-v) for u,v in a],[(p-v,u-q) for u,v in a]]
    rays=[((F(1),F(0)),(-F(1)/2,w/2)),
          ((-F(1)/2,w/2),(-F(1)/2,-w/2)),
          ((-F(1)/2,-w/2),(F(1),F(0)))]
    for tile,(left,right) in zip(patch,rays):
        assert all(det(left,z)>=0 and det(z,right)>=0 for z in tile)
    assert patch[0][0]==patch[1][4]==patch[2][2]==(0,0)
    assert patch[2][1]==(p,0) and patch[0][1]==(q,0) and q>p
    assert patch[1][3]==(-q/2,-w*q/2) and patch[2][3]==(-p/2,-w*p/2)
    print('PASS: exact Q(sqrt3) distinct convex Cairo pentagons; four-face connected orientable flat torus; exact three-copy partial-contact beta-star diagnostic.')

if __name__=='__main__':main()
