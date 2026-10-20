#!/usr/bin/env python3
"""One exact intrinsic Penrose-center Voronoi omission witness; no census."""
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
idx=23; center=centers[idx]; supports=[21,68,18,22]
verts=[]
for j,k in zip(supports[-1:]+supports[:-1],supports):
    d,e=centers[j]-center,centers[k]-center
    a=intersect(d,e,norm(d)/2,norm(e)/2)
    b=intersect(d,e,K(rh[idx][0]-rh[j][0])/2,K(rh[idx][0]-rh[k][0])/2)
    verts.append((a,b))
lo=None; hi=None; limiting=[[],[]]
for vi,(a,b) in enumerate(verts):
    for j,q in enumerate(centers):
        d=q-center
        A=dot(d,a)-norm(d)/2
        B=dot(d,b)-K(rh[idx][0]-rh[j][0])/2
        assert sign(A)<=0
        if B:
            root=-A/B
            if sign(B)>0:
                if hi is None or sign(root-hi)<0: hi=root; limiting[1]=[(vi,j)]
                elif root==hi: limiting[1].append((vi,j))
            else:
                if lo is None or sign(root-lo)>0: lo=root; limiting[0]=[(vi,j)]
                elif root==lo: limiting[0].append((vi,j))

assert lo==-QQ(1)/4 and hi==phi/3+QQ(1)/4
# Each original support is a genuine positive-length side on [lo,hi).
for k in range(4):
    def turn(t):
        P=[a+b*t for a,b in verts]
        return cross(P[(k+1)%4]-P[k],P[(k+2)%4]-P[(k+1)%4])
    f0,f1,f2=turn(lo),turn((lo+hi)/2),turn(hi)
    middle=2*f1-(f0+f2)/2
    assert sign(f0)>0 and sign(middle)>=0 and sign(f2)>=0
# Convexity of squared norm bounds every affine vertex throughout the interval.
assert all(sign(norm(a+b*t)-1)<0 for a,b in verts for t in (lo,hi))
# Exact source-tail bound, valid uniformly because |delta|<1 and |v|<1.
edges=Counter(frozenset((v[j],v[(j+1)%4])) for _,v in rh for j in range(4))
assert all(k in (1,2) for k in edges.values())
boundary=[tuple(e) for e,k in edges.items() if k==1]
def dist2(p,a,b):
    t=dot(p-a,b-a)/norm(b-a)
    if sign(t)<0: return norm(p-a)
    if sign(t-1)>0: return norm(p-b)
    return norm(p-a-t*(b-a))
margin=min((dist2(center,a,b) for a,b in boundary),key=lambda x:AA(emb(x)))
assert sign(margin-9)>0 and sign(lo+1)>0 and sign(1-hi)>0
h=(w-w.conjugate())/2
def realpair(x):
    coeff=list(K(x).vector()); b=coeff[2]; a=coeff[0]-b
    assert x==a+b*phi
    return [str(a),str(b)]
def xy(z): return [realpair((z+z.conjugate())/2),realpair((z-z.conjugate())/(2*h))]
D={"scope":"complete strict convex quadrilateral for every delta in [-1/4,phi/3+1/4); no classification outside this interval", "weight_convention":"weight delta for blue/thick rhombs, zero for red/thin", "field":"phi^2=phi+1, phi>1; z=x+i*sin(36deg)*y", "source_triangles":len(tri),"source_rhombs":len(rh),"nested_seed_triangles":len(levels[1]),"source_index":idx,"source_type":rh[idx][0],"center_cyclotomic":vec(center),"supports":supports,"vertices_affine_xy":[{"constant":xy(a),"delta_coefficient":xy(b)} for a,b in verts],"finite_constraint_interval":[realpair(lo),realpair(hi)],"limiting_vertex_site_pairs":[[list(pair) for pair in side] for side in limiting],"source_boundary_distance_squared":realpair(margin),"tail_certificate":"distance >=3; vertex radius <1; |delta|<1; D^2-2D-1>=2>0", "interval_upper_endpoint":"excluded: two turns vanish"}
path=Path('research/searches/penrose-weighted-center-first-gate-sol-2026-10-19.json')
if '--check' in __import__('sys').argv: assert json.loads(path.read_text())==D
else: path.write_text(json.dumps(D,indent=2)+'\n')
print('PASS: complete quadrilateral on [-1/4, phi/3+1/4); tail certified')
