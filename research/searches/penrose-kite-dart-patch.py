#!/usr/bin/env python3
"""Exact P2 source patches from Lang--Hayes (2013), equation (1), pp. 3--5.

Two alternating half-tile steps per P2 deflation. Mirror partners meet on
xy in P2 and xz in P3 (the prose naming the kite axis on p. 4 has a typo;
Figure 3 and exact coordinates identify it). No float decisions are used.

Replay: conda run --no-capture-output -n arisearch python
 research/searches/penrose-kite-dart-patch.py --deflations 3 --output OUT.json
"""
import argparse, importlib.util, json
from collections import Counter, defaultdict
from pathlib import Path
from functools import lru_cache
from sage.all import CyclotomicField, QQbar, AA

K = CyclotomicField(10); w = K.gen(); phi = w + w**-1
emb = K.hom([QQbar.zeta(10)]); iw = w - w.conjugate()

def area(poly):
    s = sum((poly[i].conjugate()*poly[(i+1)%len(poly)] for i in range(len(poly))), K(0))
    return (s-s.conjugate())/iw

@lru_cache(maxsize=None)
def sign(q):
    a = AA(emb(q)); return int(a>0)-int(a<0)

def positive_area(poly):
    v=area(poly); return v if sign(v)>=0 else -v

def step(tris):
    out=[]
    for typ,x,y,z in tris:
        if typ=='a1':
            p=x/phi+y/phi**2
            children=[('a2',p,z,x),('o2',z,p,y)]
        elif typ=='o1': children=[('o2',x,y,z)]
        elif typ=='a2': children=[('a1',x,y,z)]
        elif typ=='o2':
            p=x/phi**2+z/phi
            children=[('a1',y,x,p),('o1',z,p,y)]
        else: raise ValueError(typ)
        assert sum(positive_area([a,b,c]) for _,a,b,c in children)==positive_area([x,y,z])
        out.extend(children)
    return out

def build(n):
    tris=[]
    for j in range(5):
        u=w**(2*j)
        tris.extend([('a1',u,K(0),u*w),('a1',u,K(0),u/w)])
    initial_area=sum(positive_area([x,y,z]) for _,x,y,z in tris)
    for _ in range(2*n): tris=step(tris)
    assert sum(positive_area([x,y,z]) for _,x,y,z in tris)==initial_area
    by=defaultdict(list)
    for t in tris:
        typ,x,y,z=t
        assert typ in ('a1','o1')
        by[(typ,frozenset((x,y)))].append(t)
    coords=[]; ids={}; tiles=[]; half=0; scale=phi**n
    def gid(z):
        z*=scale
        if z not in ids:
            ids[z]=len(coords)
            v=[int(c) for c in z.vector()]
            assert K(v)==z
            coords.append(v)
        return ids[z]
    for (typ,axis), ts in by.items():
        if len(ts)==1: half+=1; continue
        assert len(ts)==2
        _,x,y,z=ts[0]; _,x2,y2,z2=ts[1]
        assert x==x2 and y==y2
        assert z2==x+(y-x)/(y-x).conjugate()*(z-x).conjugate()
        origin=y if typ=='a1' else x
        end=x if typ=='a1' else y
        cyc=[origin,z,end,z2]
        if sign(area(cyc))<0: cyc=[origin,z2,end,z]
        u=(cyc[1]-origin)*scale
        angles=[a for a in range(10) if w**a==u]
        assert len(angles)==1
        ref=[K(0),K(1),w if typ=='a1' else w/phi,w**2]
        assert all((v-origin)*scale==u*r for v,r in zip(cyc,ref))
        tiles.append(['kite' if typ=='a1' else 'dart',[gid(v) for v in cyc],angles[0]])
    ownership=defaultdict(list)
    for i,(_,v,_) in enumerate(tiles):
        for j in range(4): ownership[tuple(sorted((v[j],v[(j+1)%4])))].append((i,j))
    assert all(len(o)<=2 for o in ownership.values())
    return {'source':'Lang--Hayes 2013 equation (1), Figure 3; five-kite sun',
            'source_url':'https://langorigami.com/wp-content/uploads/2015/09/paper-pentasia.pdf',
            'deflations':n,'half_steps':2*n,'scale':'phi^deflations',
            'basis':'1,w,w^2,w^3; w=e^(i*pi/5)',
            'reference_kite':['0','1','w','w^2'],
            'reference_dart':['0','1','w/phi','w^2'],
            'triangle_count':len(tris),'unpaired_boundary_halves':half,
            'tile_counts':dict(Counter(t[0] for t in tiles)),
            'verts':coords,'tiles':tiles,'checks':'exact child areas, mirror partners, reference frames, edge ownership'}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--deflations',type=int,default=3);a.add_argument('--output',required=True)
    args=a.parse_args(); result=build(args.deflations)
    Path(args.output).write_text(json.dumps(result,indent=1)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('verts','tiles')},sort_keys=True))
