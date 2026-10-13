#!/usr/bin/env python3
"""Independent exact geometry and solver-free 1296-choice palette verifier.
Reads retained data, imports no producer, invokes no solver, writes no file.
"""
import json
from pathlib import Path
from collections import defaultdict
from itertools import combinations, product
from sage.all import CyclotomicField, QQbar, AA, QQ
D=json.loads(Path('research/certificates/penrose-dual-fusion-angle-palette.json').read_text())
S=json.loads(Path('research/certificates/penrose-centered-dual-single-fusion-source.json').read_text())
K=CyclotomicField(10); w=K.gen(); embed=K.hom([QQbar.zeta(10)])
def decode(v):return sum(K(c)*w**i for i,c in enumerate(v))
def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def sign(z):return int(AA(embed(z)).sign())
def phase(r):
    z=embed(r)
    return z/(z*z.conjugate()).real().sqrt()
V=[decode(v) for v in S['verts']]; R=S['rhombs']; P=[]; E=defaultdict(list)
for i,(kind,vs,frame) in enumerate(R):
    P.append(sum(V[v] for v in vs)/4+(QQ(1)/100*w**frame if kind=='thin' else 0))
    for j in range(4):E[tuple(sorted((vs[j],vs[(j+1)%4])))].append(i)
for i,(_,vs,_) in enumerate(R):
    ori=sign(sum(cross(V[vs[j]],V[vs[(j+1)%4]]) for j in range(4)))
    assert all(ori*sign(cross(V[vs[(j+1)%4]]-V[vs[j]],P[i]-V[vs[j]]))>0 for j in range(4))
for (v,u),rs in E.items():
    if len(rs)!=2:continue
    i,j=rs; a=P[i]; delta=P[j]-a; edge=V[u]-V[v]
    lam=cross(V[v]-a,edge)/cross(delta,edge)
    mu=cross(a-V[v],delta)/cross(edge,delta)
    assert 0<AA(embed(lam))<1 and 0<AA(embed(mu))<1
A=[phase(decode(r['raw_ratio'])) for r in D['exact_angle_sources']]
assert len(A)==26 and len(set(A))==26 and all(a.imag()>0 for a in A)
for a,r in zip(A,D['exact_angle_sources']):
    assert decode(r['raw_ratio'])==(P[r['outgoing']]-P[r['center']])/(P[r['incoming']]-P[r['center']])
reconstructed=[]
for r,(_,vs,_) in enumerate(R):
    ns=[]
    for i in range(4):
        incident=E[tuple(sorted((vs[i],vs[(i+1)%4])))]; ns.append(next((n for n in incident if n!=r),None))
    if None in ns:continue
    if sign(sum(cross(V[vs[i]],V[vs[(i+1)%4]]) for i in range(4)))<0:ns.reverse()
    choices=[]
    for degree in (3,4):
        for subset in combinations(range(4),degree):
            selected=[ns[i] for i in subset]; ids=[]; ok=True
            for i in range(degree):
                z=phase((P[selected[(i+1)%degree]]-P[r])/(P[selected[i]]-P[r]))
                if z.imag()<0 or (z.imag()==0 and z.real()!=-1):ok=False;break
                if z.imag()==0:continue
                assert z in A
                ids.append(A.index(z))
            if ok:choices.append({'retained_neighbor_ids':selected,'angle_ids':sorted(set(ids))})
    reconstructed.append({'rhomb':r,'cyclic_neighbor_ids':ns,'choices':choices})
assert reconstructed==D['point_choices'] and len(reconstructed)==35
signatures=[]
for row in reconstructed:
    sig=tuple(tuple(c['angle_ids']) for c in row['choices'])
    if sig not in signatures:signatures.append(sig)
assert len(signatures)==6
sizes=[len(s) for s in signatures]; assert sizes==[4,3,3,3,4,3]
minimum=26; witness=None; count=0
for choices in product(*signatures):
    count+=1; union=set().union(*(set(c) for c in choices))
    if len(union)<minimum:minimum=len(union);witness=sorted(union)
assert count==1296 and minimum==14
assert D['minimum_palette']==14
print('PASS: independently reconstructed 35 point constraints, 26 exact distinct angles, 6 choice signatures; all 1296 products have union size >=14, attained at',witness)
