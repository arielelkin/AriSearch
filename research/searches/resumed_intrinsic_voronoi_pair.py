#!/usr/bin/env python3
"""Exact singleton Voronoi construction and omission/defect certificate.
No solver, no search over metrics. Domain described in accompanying Markdown.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm, comb
from pathlib import Path
import argparse, json

D = (F(1,10), F(49,100))
BASES = ((F(0),F(0)), D, tuple(-a for a in D))
BOX = ((-F(1,2),-F(1,2)),(F(1,2),-F(1,2)),(F(1,2),F(1,2)),(-F(1,2),F(1,2)))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def clip(poly,q):
    c=dot(q,q)/2; out=[]
    for p,r in zip(poly,poly[1:]+poly[:1]):
        a=dot(q,p)-c; b=dot(q,r)-c
        if a<=0: out.append(p)
        if a*b<0:
            t=a/(a-b); out.append(tuple(x+t*(y-x) for x,y in zip(p,r)))
    return out

def cell(p, defect=False):
    poly=list(BOX)
    for base in BASES:
        for n in product(range(-2,3),repeat=2):
            site=tuple(base[k]+n[k] for k in range(2))
            if defect and site==D: site=(site[0]+F(1,10000),site[1])
            q=sub(site,p)
            if any(q): poly=clip(poly,q)
    assert len(set(poly))==len(poly)
    assert all(cross(sub(poly[i],poly[i-1]),sub(poly[(i+1)%len(poly)],poly[i]))>0 for i in range(len(poly)))
    return poly

def primitive(re,im):
    den=lcm(re.denominator,im.denominator); r=int(re*den);s=int(im*den);g=gcd(r,s)
    return (r//g,s//g)

def phases(poly):
    ans=[]
    for i,p in enumerate(poly):
        a=sub(p,poly[i-1]);b=sub(poly[(i+1)%len(poly)],p)
        t=dot(a,b); c=cross(a,b)
        assert c>0
        # cos(interior)=-t/sqrt(||a||²||b||²) < 1/2 proves angle>60 degrees.
        assert t>=0 or 4*t*t<dot(a,a)*dot(b,b)
        ans.append(primitive(-t,c))
    return ans

def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def angle_check(z, full_max, half_max):
    zz=list(dict.fromkeys(z));reals=[];full_bad=[];half_bad=[];tested=0
    for count in product(range(full_max+1),repeat=len(zz)):
        if not 1<=sum(count)<=full_max: continue
        tested+=1; w=(1,0)
        for v,n in zip(zz,count):
            for _ in range(n):w=mul(w,v)
        if w[1]==0:
            row={'counts':count,'product':w};reals.append(row)
            if w[0]>0: full_bad.append(row)
            if sum(count)<=half_max and w[0]<0:half_bad.append(row)
    assert tested==comb(full_max+len(zz),len(zz))-1
    assert not full_bad and not half_bad
    return {'distinct_phases':zz,'full_max':full_max,'half_max':half_max,'count_vectors_checked':tested,'real_products':reals,'full_phase_witnesses':full_bad,'half_phase_witnesses':half_bad}

def central(poly):
    if len(poly)%2:return False
    n=len(poly)//2;c=tuple(poly[0][k]+poly[n][k]for k in range(2))
    return all(tuple(poly[i][k]+poly[i+n][k]for k in range(2))==c for i in range(n))
def area(poly):return sum(cross(p,q)for p,q in zip(poly,poly[1:]+poly[:1]))/2

def encode(obj):
    if isinstance(obj,F):return str(obj)
    if isinstance(obj,tuple):return [encode(x)for x in obj]
    if isinstance(obj,list):return [encode(x)for x in obj]
    if isinstance(obj,dict):return {k:encode(v)for k,v in obj.items()}
    return obj

def build():
    q=cell((F(0),F(0)));p=cell(D);pm=cell(tuple(-a for a in D));qd=cell((F(0),F(0)),True)
    assert len(q)==8 and len(p)==5 and len(pm)==5 and len(qd)==8
    assert set(pm)=={tuple(-a for a in v)for v in p}
    assert central(q) and not central(qd)
    assert area(q)+2*area(p)==1
    pw=[tuple(v[k]+D[k]for k in range(2))for v in p]
    pp=[pw[i]for i in (4,0,1)]
    parent=q[:2]+pp+q[2:6]+[tuple(-a for a in v)for v in pp]+q[6:]
    assert len(parent)==14 and area(parent)==1
    assert sum(cross(sub(parent[i],parent[i-1]),sub(parent[(i+1)%14],parent[i]))<0 for i in range(14))==4
    pphase=phases(p);qphase=phases(q)
    assert all(z[0]<0 for z in qphase) # all octagon angles>90 degrees
    return encode({'status':'EXACT PERIODIC PAIR; APERIODIC CONSTRUCTION FALSIFIED',
      'site_offset':D,'lattice':[(1,0),(0,1)],'neighbor_index_domain':[-2,2],
      'pentagon':p,'octagon':q,'pentagon_area':area(p),'octagon_area':area(q),'repeatable_parent':parent,'parent_reflex_count':4,'parent_area':area(parent),
      'pentagon_angle_test':angle_check(pphase,5,2),'octagon_angle_test':angle_check(qphase,3,1),
      'defect_displacement':(F(1,10000),F(0)),'defect_origin_octagon':qd,
      'defect_centrally_symmetric':central(qd),
      'scope':'One fixed periodic 3-site lattice motif and one isolated moved site; no parameter classification.'})

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--check',type=Path)
    a=ap.parse_args(); data=build()
    if a.check:
        assert json.loads(a.check.read_text())==data
    if a.output:a.output.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: exact (5,8) Voronoi pair; both monohedral angle tests empty; isolated phason creates third class.')
