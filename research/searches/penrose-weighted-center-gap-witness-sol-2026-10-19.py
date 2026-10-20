#!/usr/bin/env python3
"""One fixed-gap-sample Penrose power-cell witness and exact affine interval."""
import json
from pathlib import Path
from collections import defaultdict, Counter
from sage.all import CyclotomicField, QQ, AA, QQbar
K=CyclotomicField(10); w=K.gen(); phi=w+1/w
emb=K.hom([QQbar.zeta(10)])
def sign(v):
    a=AA(emb(v)); return (a>0)-(a<0)
def dot(a,b): return (a.conjugate()*b+a*b.conjugate())/2
def norm(a): return dot(a,a)
def cross(a,b): return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def vec(a): return [str(x) for x in K(a).vector()]
def sun():
    out=[]
    for i in range(10):
        B,C=w**i,w**(i+1)
        if i%2==0: B,C=C,B
        out.append((0,K(0),B,C))
    return out
# Author's displayed red/blue recurrence, Preshing 2011.
def sub(ts):
    out=[]
    for c,A,B,C in ts:
        if c==0:
            P=A+(B-A)/phi
            out.extend([(0,C,P,B),(1,P,C,A)])
        else:
            Q=B+(A-B)/phi; R=B+(C-B)/phi
            out.extend([(1,R,C,A),(1,Q,R,B),(0,R,Q,A)])
    return out
levels={}; ts=sun()
for n in range(6):
    if n in (1,5): levels[n]=[(c,A*phi**n,B*phi**n,C*phi**n) for c,A,B,C in ts]
    ts=sub(ts)
assert set(levels[1])<=set(levels[5])
tri=levels[5]; by=defaultdict(list)
for t in tri: by[frozenset(t[2:])].append(t)
rh=[]; unmatched=[]
for key,items in by.items():
    assert len(items) in (1,2)
    if len(items)==1: unmatched.append(items[0]); continue
    t,u=items
    assert t[0]==u[0] and t[2:]==u[2:]
    c,A,B,C=t; D=u[1]
    assert sign(cross(B-A,D-B))!=0
    assert sign(cross(C-B,A-B))*sign(cross(C-B,D-B))==-1
    cyc=[A,B,D,C]
    assert all(norm(cyc[(j+1)%4]-cyc[j])==1 for j in range(4))
    rh.append((c,cyc))
# Every unmatched base is on the outer regular decagon boundary.
outer=[phi**5*w**i for i in range(10)]
def onseg(p,a,b): return cross(b-a,p-a)==0 and sign(dot(p-a,p-b))<=0
assert all(any(onseg(t[2],a,b) and onseg(t[3],a,b) for a,b in zip(outer,outer[1:]+outer[:1])) for t in unmatched)
centers=[sum(v)/4 for _,v in rh]

# Weight is delta for blue/thick rhombs, zero for red/thin.
def intersect(d,e,r,s):
    # z=x+h*y, exact metric.
    h=(w-w.conjugate())/2
    a,b=dot(d,K(1)),dot(d,h); u,v=dot(e,K(1)),dot(e,h)
    det=a*v-b*u
    assert det
    return (r*v-b*s)/det+h*(a*s-r*u)/det
# One fixed sample only; floating clipping proposes candidates, exact arithmetic certifies.
import numpy as np
sample=-QQ(3)/4
assert len(rh)==430 and sign(sample-(-QQ(21)/44-QQ(9)/22*phi))>0 and sign(-QQ(1)/4-sample)>0
xyfloat=np.array([[float(emb(z).real()),float(emb(z).imag())] for z in centers])
def propose(i):
    P=[np.array(v,dtype=float) for v in [(-30,-30),(30,-30),(30,30),(-30,30)]]
    for j in range(len(rh)):
        if j==i:continue
        d=xyfloat[j]-xyfloat[i]
        rhs=np.dot(d,d)/2+float(sample)*(rh[i][0]-rh[j][0])/2
        out=[]
        for a,b in zip(P,P[1:]+P[:1]):
            fa=np.dot(d,a)-rhs;fb=np.dot(d,b)-rhs
            if fa<=1e-10:out.append(a)
            if fa*fb<0:out.append(a+(b-a)*fa/(fa-fb))
        P=out
        if not P:return []
    clean=[]
    for a in P:
        if not clean or np.linalg.norm(a-clean[-1])>1e-8:clean.append(a)
    if len(clean)>1 and np.linalg.norm(clean[0]-clean[-1])<1e-8:clean.pop()
    if len(clean)!=4:return []
    ids=[]
    for a,b in zip(clean,clean[1:]+clean[:1]):
        mid=(a+b)/2
        matches=[j for j in range(len(rh)) if j!=i and abs(np.dot(xyfloat[j]-xyfloat[i],mid)-np.dot(xyfloat[j]-xyfloat[i],xyfloat[j]-xyfloat[i])/2-float(sample)*(rh[i][0]-rh[j][0])/2)<1e-7]
        if len(matches)!=1:return []
        ids.append(matches[0])
    return ids
h=(w-w.conjugate())/2
def realpair(x):
    coeff=list(K(x).vector());b=coeff[2];a=coeff[0]-b
    assert x==a+b*phi
    return [str(a),str(b)]
def xy(z):return [realpair((z+z.conjugate())/2),realpair((z-z.conjugate())/(2*h))]
edges=Counter(frozenset((v[j],v[(j+1)%4])) for _,v in rh for j in range(4))
assert all(k in (1,2) for k in edges.values())
boundary=[tuple(e) for e,k in edges.items() if k==1]
def dist2(p,a,b):
    t=dot(p-a,b-a)/norm(b-a)
    if sign(t)<0:return norm(p-a)
    if sign(t-1)>0:return norm(p-b)
    return norm(p-a-t*(b-a))
scanned=[];record=None
for idx in sorted(range(len(rh)),key=lambda j:(AA(emb(norm(centers[j]))),j)):
    supports=propose(idx);scanned.append(idx)
    if not supports:continue
    c=centers[idx];verts=[]
    for j,k in zip(supports[-1:]+supports[:-1],supports):
        d,e=centers[j]-c,centers[k]-c
        verts.append((intersect(d,e,norm(d)/2,norm(e)/2),intersect(d,e,K(rh[idx][0]-rh[j][0])/2,K(rh[idx][0]-rh[k][0])/2)))
    P=[a+b*sample for a,b in verts]
    assert all(sign(cross(P[(k+1)%4]-P[k],P[(k+2)%4]-P[(k+1)%4]))>0 for k in range(4))
    lo=None;hi=None;limiting=[[],[]]
    for vi,(a,b) in enumerate(verts):
        for j,q in enumerate(centers):
            d=q-c;A=dot(d,a)-norm(d)/2;B=dot(d,b)-K(rh[idx][0]-rh[j][0])/2
            assert sign(A+B*sample)<=0
            if not B:continue
            root=-A/B;side=1 if sign(B)>0 else 0
            old=hi if side else lo
            if old is None or sign(root-old)==(-1 if side else 1):
                if side:hi=root
                else:lo=root
                limiting[side]=[[vi,j]]
            elif root==old:limiting[side].append([vi,j])
    margin=min((dist2(c,a,b) for a,b in boundary),key=lambda x:AA(emb(x)))
    # At this sample: R<1 and D>3 imply omitted power slack >2.
    tail=sign(margin-9)>0 and all(sign(norm(p)-1)<0 for p in P)
    if not tail:
        record=dict(status='candidate tail failed',index=idx);break
    assert lo is not None and hi is not None
    assert sign(sample-lo)>0 and sign(hi-sample)>0
    assert all(sign(dot(q-c,a+b*t)-norm(q-c)/2-t*K(rh[idx][0]-rh[j][0])/2)<=0 for a,b in verts for j,q in enumerate(centers) for t in (lo,hi))
    # Each edge vector is affine. Its scalar along its fixed support line is
    # affine too: positive endpoint/midpoint turns certify the open interval.
    turns=[]
    for t in (lo,(lo+hi)/2,hi):
        Q=[a+b*t for a,b in verts]
        turns.append([sign(cross(Q[(k+1)%4]-Q[k],Q[(k+2)%4]-Q[(k+1)%4])) for k in range(4)])
    assert all(v>0 for v in turns[1]) and all(v>=0 for row in (turns[0],turns[2]) for v in row)
    for k in range(4):
        def turn(t):
            Q=[a+b*t for a,b in verts]
            return cross(Q[(k+1)%4]-Q[k],Q[(k+2)%4]-Q[(k+1)%4])
        f0,fm,f1=turn(lo),turn((lo+hi)/2),turn(hi)
        assert sign(2*fm-(f0+f1)/2)>=0
    endpoint_tail=sign(margin-64)>0 and all(sign(norm(a+b*t)-4)<0 for a,b in verts for t in (lo,hi)) and sign(lo+2)>0 and sign(2-hi)>0
    assert endpoint_tail
    A=-QQ(21)/44-QQ(9)/22*phi
    record=dict(status='complete strict convex quadrilateral',index=idx,type=rh[idx][0],supports=supports,center_cyclotomic=vec(c),vertices_affine_xy=[dict(constant=xy(a),delta_coefficient=xy(b)) for a,b in verts],maximal_finite_affine_support_interval=[realpair(lo),realpair(hi)],limiting_pairs=limiting,endpoint_turn_signs=turns,endpoint_included=[all(v>0 for v in turns[0]),all(v>0 for v in turns[2])],boundary_distance_squared=realpair(margin),uniform_interval_tail_certified=endpoint_tail,overlaps_reviewed_lower=sign(lo-A)<0,overlaps_reviewed_upper=sign(hi+QQ(1)/4)>0)
    break
D=dict(sample='-3/4',source_rhombs=len(rh),source_triangles=len(tri),scanned_indices=scanned,witness=record,scope='one fixed sample, first quadrilateral candidate; no other delta samples or source enlargement',tail='sample: D>3,R<1,|delta|<1; full interval: D>8,R<2,|delta|<2 gives D^2-2DR-|delta|>30')
path=Path('research/searches/penrose-weighted-center-gap-witness-sol-2026-10-19.json')
if '--check' in __import__('sys').argv:assert json.loads(path.read_text())==D
else:path.write_text(json.dumps(D,indent=2)+'\n')
print(json.dumps(D,indent=2))
