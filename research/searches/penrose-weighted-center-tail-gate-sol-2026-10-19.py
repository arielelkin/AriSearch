#!/usr/bin/env python3
"""Two exact same-type quadrilateral witnesses with uniform weighted tails."""
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

h=(w-w.conjugate())/2
edges=Counter(frozenset((v[j],v[(j+1)%4])) for _,v in rh for j in range(4))
assert all(k in (1,2) for k in edges.values())
boundary=[tuple(e) for e,k in edges.items() if k==1]
def dist2(p,a,b):
    t=dot(p-a,b-a)/norm(b-a)
    if sign(t)<0:return norm(p-a)
    if sign(t-1)>0:return norm(p-b)
    return norm(p-a-t*(b-a))
def realpair(x):
    coeff=list(K(x).vector()); b=coeff[2]; a=coeff[0]-b
    assert x==a+b*phi
    return [str(a),str(b)]
def xy(v):return [realpair((v+v.conjugate())/2),realpair((v-v.conjugate())/(2*h))]
def cell(i):
    c=centers[i]; P=[K(-20)-20*h,K(20)-20*h,K(20)+20*h,K(-20)+20*h]
    for j,q in enumerate(centers):
        if j==i or rh[j][0]!=rh[i][0]:continue
        d=q-c; rhs=norm(d)/2;out=[]
        for a,b in zip(P,P[1:]+P[:1]):
            fa=dot(d,a)-rhs; fb=dot(d,b)-rhs
            if sign(fa)<=0:out.append(a)
            if sign(fa)*sign(fb)<0:out.append(a+(b-a)*fa/(fa-fb))
        P=[]
        for x in out:
            if not P or x!=P[-1]:P.append(x)
        if len(P)>1 and P[0]==P[-1]:P.pop()
        assert P
    while any(cross(P[k]-P[k-1],P[(k+1)%len(P)]-P[k])==0 for k in range(len(P))):
        P=[p for k,p in enumerate(P) if cross(p-P[k-1],P[(k+1)%len(P)]-p)!=0]
    return P
records=[]; scanned={}
for typ in (1,0):
    scanned[str(typ)]=[]
    for i in sorted((j for j in range(len(rh)) if rh[j][0]==typ),key=lambda j:(AA(emb(norm(centers[j]))),j)):
        P=cell(i);scanned[str(typ)].append([i,len(P)])
        if len(P)!=4:continue
        c=centers[i]
        assert all(sign(cross(P[(k+1)%4]-P[k],P[(k+2)%4]-P[(k+1)%4]))>0 for k in range(4))
        supports=[]
        for a,b in zip(P,P[1:]+P[:1]):
            ids=[j for j,q in enumerate(centers) if j!=i and rh[j][0]==typ and dot(q-c,a)==norm(q-c)/2 and dot(q-c,b)==norm(q-c)/2]
            assert len(ids)==1;supports.append(ids[0])
        assert all(sign(dot(q-c,v)-norm(q-c)/2)<=0 for v in P for j,q in enumerate(centers) if rh[j][0]==typ)
        radius=max((norm(v) for v in P),key=lambda x:AA(emb(x)))
        margin=min((dist2(c,a,b) for a,b in boundary),key=lambda x:AA(emb(x)))
        # Uniform omitted-site geometric slack is positive if D^2>4R^2.
        assert sign(margin-4*radius)>0
        vals=[(2*dot(q-c,v)-norm(q-c),k,j) for k,v in enumerate(P) for j,q in enumerate(centers) if rh[j][0]!=typ]
        worst=max((x[0] for x in vals),key=lambda x:AA(emb(x)))
        threshold=max((K(0),worst),key=lambda x:AA(emb(x)))
        # thick: delta>=threshold; thin: delta<=-threshold.
        endpoint=threshold if typ else -threshold
        records.append(dict(type=typ,index=i,center_cyclotomic=vec(c),vertices_xy=[xy(v) for v in P],supports=supports,radius_squared=realpair(radius),boundary_distance_squared=realpair(margin),finite_worst_deficit=realpair(worst),threshold=realpair(endpoint),limiting_pairs=[[k,j] for val,k,j in vals if val==worst],halfline='delta >= threshold' if typ else 'delta <= threshold'))
        print('FOUND',typ,i,'endpoint',endpoint,'radius',radius,'margin',margin,flush=True)
        break
    else:break
D=dict(field='Q(phi), phi^2=phi+1, phi>1; z=x+i sin(36deg)y',triangles=len(tri),rhombs=len(rh),search_order='increasing exact squared center distance to origin, then index; stop first quadrilateral per type',scanned=scanned,witnesses=records)
if len(records)==2:
    thick=sum(QQ(v)*phi**k for k,v in enumerate(records[0]['threshold']))
    thin=sum(QQ(v)*phi**k for k,v in enumerate(records[1]['threshold']))
    lo=-QQ(1)/4; hi=QQ(1)/4+phi/3
    D['negative_overlap']=sign(thin-lo)>=0
    D['positive_overlap']=sign(hi-thick)>=0
    D['all_real_covered']=D['negative_overlap'] and D['positive_overlap']
    D['positive_join_kind']='shared endpoint' if hi==thick else 'overlap or gap'
    D['uncovered_gaps']=[dict(lower=realpair(thin),upper=realpair(lo),lower_included=False,upper_included=False)] if sign(thin-lo)<0 else []
path=Path('research/searches/penrose-weighted-center-tail-gate-sol-2026-10-19.json')
if '--check' in __import__('sys').argv:assert json.loads(path.read_text())==D
else:path.write_text(json.dumps(D,indent=2)+'\n')
print(json.dumps(D,indent=2))
