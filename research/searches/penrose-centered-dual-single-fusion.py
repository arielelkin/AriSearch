#!/usr/bin/env python3
"""Exact three-edge fusion gate at the retained marked Penrose three-star.
Domain: one deletion from the centered dual network at source vertex 10.
No infinite-tiling or shape-only forcing assertion is made.
"""
import json
import argparse
from collections import defaultdict
from pathlib import Path
from sage.all import CyclotomicField, QQbar, AA
K=CyclotomicField(10); w=K.gen(); emb=K.hom([QQbar.zeta(10)])
def decode(v): return sum(K(c)*w**i for i,c in enumerate(v))
def encode(z): return [str(c) for c in z.vector()]
def cross(a,b): return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def sign(z): return int(AA(emb(z)).sign())
def area(P): return sum(cross(P[i], P[(i+1)%len(P)]) for i in range(len(P)))
def convex(P):
    return all(sign(cross(P[(i+1)%len(P)]-P[i], P[j]-P[i]))>=0
               for i in range(len(P)) for j in range(len(P)))
source=Path('research/certificates/penrose-centered-dual-single-fusion-source.json')
d=json.loads(source.read_text()); verts=[decode(v) for v in d['verts']]
rh=[x[1] for x in d['rhombs']]; centers=[sum(verts[v] for v in p)/4 for p in rh]
edges=defaultdict(list); incident=defaultdict(list)
for r,p in enumerate(rh):
    assert p[0]!=p[1] and len(set(p))==4
    assert all((verts[p[(i+1)%4]]-verts[p[i]])*(verts[p[(i+1)%4]]-verts[p[i]]).conjugate()==1 for i in range(4))
    for v in p: incident[v].append(r)
    for i in range(4): edges[tuple(sorted((p[i],p[(i+1)%4])))].append(r)
def star(v):
    adj=defaultdict(list)
    for edge,rs in edges.items():
        if v not in edge: continue
        if len(rs)!=2: raise ValueError('incomplete star')
        a,b=rs; adj[a].append(b); adj[b].append(a)
    assert all(len(adj[r])==2 for r in incident[v])
    cyc=[min(incident[v])]; previous=None; r=cyc[0]
    while True:
        nxt=next(t for t in adj[r] if t!=previous)
        if nxt==cyc[0]: break
        assert nxt not in cyc
        cyc.append(nxt); previous,r=r,nxt
    assert set(cyc)==set(incident[v])
    if sign(area([centers[r] for r in cyc]))<0: cyc.reverse()
    return cyc
parser=argparse.ArgumentParser(); parser.add_argument('--vertex',type=int,choices=(10,11),default=10); parser.add_argument('--check',type=Path); args=parser.parse_args()
v=args.vertex; A=star(v); assert len(A)==3
results=[]
for edge,rs in sorted(edges.items()):
    if v not in edge: continue
    assert len(rs)==2
    u=next(x for x in edge if x!=v); B=star(u)
    # Validate source-edge crossing: the centered dual network actually
    # realizes this adjacency, rather than merely formal polygon gluing.
    i,j=rs; a=centers[i]; direction=centers[j]-a; e=verts[u]-verts[v]
    lam=cross(verts[v]-a,e)/cross(direction,e)
    mu=cross(a-verts[v],direction)/cross(e,direction)
    assert 0<AA(emb(lam))<1 and 0<AA(emb(mu))<1
    paths=[]
    for C in (A,B):
        oriented=[(C[k],C[(k+1)%len(C)]) for k in range(len(C))]
        shared=[x for x in oriented if set(x)==set(rs)]
        assert len(shared)==1
        paths += [x for x in oriented if x not in shared]
    successor=dict(paths); assert len(successor)==len(paths)
    start=min(successor); F=[start]
    while successor[F[-1]]!=start:
        F.append(successor[F[-1]]); assert len(F)<=len(paths)
    assert len(F)==len(paths)
    P=[centers[r] for r in F]; assert sign(area(P))>0
    turns=[sign(cross(P[k]-P[k-1],P[(k+1)%len(P)]-P[k])) for k in range(len(P))]
    row={'source_edge':list(edge),'shared_rhombs':rs,'neighbor_star':B,
         'neighbor_side_count':len(B),'neighbor_convex':convex([centers[r] for r in B]),
         'fused_center_ids':F,'fused_coordinates':[encode(z) for z in P],
         'turn_signs':turns,'fused_convex':convex(P),
         'side_squared_lengths':[encode((P[(k+1)%len(P)]-P[k])*(P[(k+1)%len(P)]-P[k]).conjugate()) for k in range(len(P))],
         'intrinsic_side_count':len(P)-turns.count(0)}
    results.append(row)
out={'domain':f'three single-edge deletions at retained source vertex {v}',
                  'central_star':A,'central_convex':convex([centers[r] for r in A]),
                  'results':results}
if v==10:
    P=[centers[r] for r in results[-1]['fused_center_ids']]
    for i,m in enumerate((7,6,4,9,4)):
        ratio=emb((P[i-1]-P[i])/(P[(i+1)%5]-P[i]))
        unit=ratio/(ratio*ratio.conjugate()).real().sqrt()
        assert unit==QQbar.zeta(20)**m
    out['convex_pentagon_exact_angles_degrees']=[126,108,72,162,72]
    out['type1_consecutive_sum360']=[3,4,0]
if args.check:
    assert json.loads(args.check.read_text())==out
    print(f'PASS: three exact single-edge fusion candidates at source vertex {v}.')
else: print(json.dumps(out,indent=2))
