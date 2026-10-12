#!/usr/bin/env python3
"""Independent clipping/boundary/long-edge occupancy audit of six-A strip."""
import argparse,collections,hashlib,importlib.util,itertools,json
from pathlib import Path
from sage.all import QQ
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('independent_clip',HERE/'check_hat_eight_kite_convex_clusters.py')
g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
K,r=g.K,g.r
def number(v):return sum(K(QQ(n)/d)*r**i for i,(n,d) in enumerate(v))
def point(v):return tuple(number(a) for a in v)
def polygon(v):return [point(p) for p in v]
def shift(P,t):return [tuple(x+y for x,y in zip(p,t)) for p in P]
def ccw(P):return P if g.area2(P)>0 else P[::-1]
def atoms(polys):
    vertices={p for P in polys for p in P};edges=collections.Counter()
    for P in map(ccw,polys):
        for u,v in zip(P,P[1:]+P[:1]):
            d=g.subtract(v,u);n=g.dot(d,d)
            on=sorted((g.dot(g.subtract(p,u),d)/n,p) for p in vertices if g.cross(d,g.subtract(p,u))==0 and 0<=g.dot(g.subtract(p,u),d)<=n)
            edges.update((p,q) for (_,p),(_,q) in zip(on,on[1:]))
    return {(u,v) for (u,v),n in edges.items() if n>edges[v,u]}
def coverage(P,others):
    u,v=P[:2];d=g.subtract(v,u);n=g.dot(d,d);intervals=[]
    for Q in others:
        for x,y in zip(Q,Q[1:]+Q[:1]):
            if g.cross(d,g.subtract(x,u)) or g.cross(d,g.subtract(y,u)):continue
            low,high=sorted((g.dot(g.subtract(x,u),d)/n,g.dot(g.subtract(y,u),d)/n))
            low=max(K(0),low);high=min(K(1),high)
            if low<high:intervals.append((low,high))
    end=K(0)
    for low,high in sorted(intervals):
        assert low<=end
        end=max(end,high)
    return end
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/acute-long-edge-construction-features.json');cert=json.loads(path.read_text())
    A=polygon(cert['six_tile_module'][0]);polys=[polygon(P) for P in cert['six_tile_module']];T=point(cert['strip_period']);boundary=polygon(cert['six_tile_boundary'])
    assert len(polys)==6 and len(boundary)==18
    for P in polys:
        assert len(P)==5 and g.congruent(A,P)
        Q=ccw(P);assert all(g.turn(Q[i-1],Q[i],Q[(i+1)%5])>0 for i in range(5))
    for P,Q in itertools.combinations(polys,2):assert g.area2(g.clip(ccw(P),ccw(Q)))==0
    assert atoms(polys)==set(zip(boundary,boundary[1:]+boundary[:1]))
    assert g.area2(boundary)==sum(abs(g.area2(P)) for P in polys)
    covered=[coverage(P,[Q for j,Q in enumerate(polys) if i!=j]) for i,P in enumerate(polys)]
    assert covered==[1]*6
    translated=[shift(P,T) for P in polys]
    for P,Q in itertools.product(polys,translated):assert g.area2(g.clip(ccw(P),ccw(Q)))==0
    arcs=atoms(polys);matched={(u,v) for u,v in arcs if (g.subtract(v,T),g.subtract(u,T)) in arcs}
    assert len(matched)==1
    u,v=next(iter(matched));assert g.dot(g.subtract(v,u),g.subtract(v,u))==16
    projections=[g.dot(p,T) for P in polys for p in P];width=max(projections)-min(projections);norm=g.dot(T,T)
    assert norm<width<2*norm
    assert cert['cap_propagation_arrests'] and not cert['strip_is_full_plane_tiling']
    # Independent full-c/B-a bridge attempt. B is reconstructed from its
    # native lengths, not from the producer's attachment coordinates.
    bl=[number(v) for v in cert['B_lengths']]
    dirs=[(K(1),K(0)),(-K(1)/2,r/2),(-r/2,K(1)/2),(-r/2,-K(1)/2),(-K(1)/2,-r/2)]
    B=[(K(0),K(0))]
    for length,direction in zip(bl,dirs):B.append(tuple(x+length*y for x,y in zip(B[-1],direction)))
    assert B.pop()==(0,0) and bl[0]==4 and bl[1]==bl[4] and bl[2]==bl[3]
    # Reflection in the perpendicular bisector of a preserves this B.
    assert set((bl[0]-x,y) for x,y in B)==set(B)
    bridges=[]
    for i,P in enumerate(polys):
        u,v=P[2:4]
        if (u,v) not in arcs and (v,u) not in arcs:continue
        p,q=(u,v) if g.area2(P)>0 else (v,u)
        if (g.subtract(q,T),g.subtract(p,T)) in arcs or (tuple(x+y for x,y in zip(q,T)),tuple(x+y for x,y in zip(p,T))) in arcs:continue
        start,end=(v,u) if g.area2(P)>0 else (u,v)
        cosine,sine=(end[0]-start[0])/bl[0],(end[1]-start[1])/bl[0]
        Q=[(start[0]+cosine*x-sine*y,start[1]+sine*x+cosine*y) for x,y in B]
        obstructions=[]
        for n,j in itertools.product((-1,0,1),range(6)):
            target=shift(polys[j],tuple(n*x for x in T));intersection=g.clip(Q,ccw(target));a2=g.area2(intersection)
            if a2>0:obstructions.append({'strip_shift':n,'A_index':j,'intersection_area_twice':str(a2)})
        bridges.append({'A_index':i,'blocked_by_A':obstructions,'polygon':Q})
    usable=[b for b in bridges if not b['blocked_by_A']]
    pair_obstructions=[]
    for left,right in itertools.combinations_with_replacement(usable,2):
        for n in (-1,0,1):
            if left is right and n==0:continue
            a2=g.area2(g.clip(left['polygon'],shift(right['polygon'],tuple(n*x for x in T))))
            if a2>0:pair_obstructions.append([left['A_index'],right['A_index'],n,str(a2)])
    assert len(bridges)==4
    if 'B_bridge_polygons' in cert:
        recorded=[polygon(P) for P in cert['B_bridge_polygons']]
        assert {frozenset(b['polygon']) for b in bridges}=={frozenset(P) for P in recorded}
        for overlap in cert['B_bridge_overlaps']:
            P=recorded[overlap['B_bridge_index']];Q=shift(polys[overlap['A_face_index']],tuple(overlap['A_cell_period']*x for x in T));witness=point(overlap['strict_interior_point'])
            for U in (ccw(P),ccw(Q)):
                assert all(g.cross(g.subtract(v,u),g.subtract(witness,u))>0 for u,v in zip(U,U[1:]+U[:1]))
        assert len(cert['B_bridge_overlaps'])==sum(len(b['blocked_by_A']) for b in bridges)==2
    for b in bridges:del b['polygon']
    result={'status':'PASSED','six_tile_pairs_clipped':15,'adjacent_strip_tile_pairs_clipped':36,'atomic_boundary_edges':18,'fully_occupied_native_a_edges':6,'strip_shared_c_edges':1,'nonadjacent_strip_separation':'Exact projection width less than twice the period norm','full_c_B_a_bridge_attempts':bridges,'surviving_B_bridge_pair_overlaps':pair_obstructions,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Six-A cap arrest, one-dimensional strip, and specific full-c/B-a attachment obstruction only; no plane tiling or forcing'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
