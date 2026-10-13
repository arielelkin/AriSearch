#!/usr/bin/env python3
"""Independent intersections-of-bisectors check; never imports producer."""
from fractions import Fraction as F
from itertools import product, combinations
from functools import cmp_to_key
from math import gcd,lcm,comb
from pathlib import Path
import json
C=json.loads(Path('research/certificates/resumed_intrinsic_voronoi_pair.json').read_text())
D=(F(1,10),F(49,100));bases=[(F(0),F(0)),D,(-D[0],-D[1])]
def vec(v):return tuple(map(F,v))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cr(a,b):return a[0]*b[1]-a[1]*b[0]
def vv(key):return list(map(vec,C[key]))
def reconstruct(p,defect=False):
    hs=[]
    for b in bases:
        for n in product(range(-2,3),repeat=2):
            s=(b[0]+n[0],b[1]+n[1])
            if defect and s==D:s=(s[0]+F(1,10000),s[1])
            q=sub(s,p)
            if q==(0,0):continue
            c=dot(q,q)/2
            # Omit constraints redundant on [-1/2,1/2]^2, retaining equality.
            if c>(abs(q[0])+abs(q[1]))/2:continue
            hs.append((q,c))
    vs=set()
    for (a,x),(b,y) in combinations(hs,2):
        k=cr(a,b)
        if not k:continue
        v=((x*b[1]-a[1]*y)/k,(a[0]*y-x*b[0])/k)
        if all(dot(q,v)<=c for q,c in hs):vs.add(v)
    assert len(vs)>=3
    ctr=tuple(sum(v[k]for v in vs)/len(vs)for k in (0,1))
    def cmp(a,b):
        aa=sub(a,ctr);bb=sub(b,ctr)
        ha=int(aa[1]<0 or (aa[1]==0 and aa[0]<0));hb=int(bb[1]<0 or (bb[1]==0 and bb[0]<0))
        return (ha>hb)-(ha<hb) if ha!=hb else -(cr(aa,bb)>0)+(cr(aa,bb)<0)
    out=sorted(vs,key=cmp_to_key(cmp))
    assert all(cr(sub(out[i],out[i-1]),sub(out[(i+1)%len(out)],out[i]))>0 for i in range(len(out)))
    return out
# Completeness beyond finite index domain: any omitted lattice index has
# |q_k| >= 3-98/100=101/50. For all real y, y^2-|y| >= -1/4.
# Thus ||q||^2-(|q_x|+|q_y|)>0, redundant on the same-base unit square.
a=F(101,50);assert a*a-a-F(1,4)>0
Q=reconstruct((F(0),F(0)));P=reconstruct(D);Pm=reconstruct((-D[0],-D[1]));Qd=reconstruct((F(0),F(0)),True)
assert set(Q)==set(vv('octagon')) and set(P)==set(vv('pentagon'))
assert set(Qd)==set(vv('defect_origin_octagon'))
assert set(Pm)=={(-v[0],-v[1])for v in P}
assert (len(P),len(Q),len(Qd))==(5,8,8)
def area(p):return sum(cr(a,b)for a,b in zip(p,p[1:]+p[:1]))/2
assert area(Q)+2*area(P)==1
assert area(Q)==F(C['octagon_area']) and area(P)==F(C['pentagon_area'])
def phases(p,bound):
    out=[]
    for i,v in enumerate(p):
        x=sub(p[i-1],v);y=sub(p[(i+1)%len(p)],v)
        re=dot(x,y);im=abs(cr(x,y))
        if bound==60:assert re<=0 or 4*re*re<dot(x,x)*dot(y,y)
        else:assert bound==90 and re<0
        d=lcm(re.denominator,im.denominator);rr=int(re*d);ii=int(im*d);g=gcd(rr,ii)
        out.append((rr//g,ii//g))
    return sorted(set(out))
def compositions(total,k):
    if k==1:yield(total,);return
    for n in range(total+1):
        for rest in compositions(total-n,k-1):yield(n,)+rest
def phasecheck(p,bound,maxfull,maxhalf,key):
    zz=phases(p,bound);tested=0;real=[]
    for size in range(1,maxfull+1):
        for counts in compositions(size,len(zz)):
            tested+=1;r,j=1,0
            for (a,b),n in zip(zz,counts):
                for _ in range(n):r,j=r*a-j*b,r*b+j*a
            if j==0:
                assert r<0
                assert size>maxhalf
                real.append((counts,r))
    assert tested==comb(maxfull+len(zz),len(zz))-1
    rec=C[key]
    assert sorted(map(tuple,rec['distinct_phases']))==zz
    assert rec['count_vectors_checked']==tested
    # Certificate count vectors use its own phase order; reconstruct each.
    for row in rec['real_products']:
        counts=row['counts'];r,j=1,0
        for (a,b),n in zip(rec['distinct_phases'],counts):
            for _ in range(n):r,j=r*a-j*b,r*b+j*a
        assert [r,j]==row['product'] and j==0 and r<0
    assert len(real)==len(rec['real_products'])
    assert not rec['full_phase_witnesses'] and not rec['half_phase_witnesses']
phasecheck(P,60,5,2,'pentagon_angle_test');phasecheck(Q,90,3,1,'octagon_angle_test')
def central(p):
    if len(p)%2:return False
    n=len(p)//2;c=tuple(p[0][i]+p[n][i]for i in (0,1))
    return all(tuple(p[j][i]+p[j+n][i]for i in (0,1))==c for j in range(n))
assert central(Q) and not central(Qd)
# Audit parent as union by splitting all polygon boundary edges at every
# available boundary vertex, then cancel opposite directed subsegments.
Pw=[(v[0]+D[0],v[1]+D[1])for v in P];Pmw=[(-v[0],-v[1])for v in Pw]
polys=[Q,Pw,Pmw];allv=set(sum(polys,[]));edges=[]
for poly in polys:
    for a,b in zip(poly,poly[1:]+poly[:1]):
        d=sub(b,a);pts=[v for v in allv if cr(sub(v,a),d)==0 and 0<=dot(sub(v,a),d)<=dot(d,d)]
        pts.sort(key=lambda v:dot(sub(v,a),d))
        for x,y in zip(pts,pts[1:]):
            if (y,x)in edges:edges.remove((y,x))
            else:edges.append((x,y))
parent=vv('repeatable_parent');pe=list(zip(parent,parent[1:]+parent[:1]))
assert set(edges)==set(pe) and len(edges)==14
assert area(parent)==1
assert sum(cr(sub(parent[i],parent[i-1]),sub(parent[(i+1)%14],parent[i]))<0 for i in range(14))==4
print('PASS: independent exact Voronoi cells, finite-domain completeness, 285 corner multisets, parent boundary and defect third class')
