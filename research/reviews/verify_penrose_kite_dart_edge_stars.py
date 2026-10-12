#!/usr/bin/env python3
"""Independent embedding/rotation-system controls for endpoint-star screen.

These are encoding controls, not an independent hostile mathematical review.
An exact midpoint embedding with centres w/2 (kite), w/4 (dart) reconstructs
face walks from the clockwise predecessor of each reverse half-edge, rather
than unioning source fan pieces. Endpoints are deleted only conditionally
on convexity, not because the midpoint embedding aligns the spokes.
"""
import argparse, hashlib, importlib.util, json
from collections import Counter, defaultdict
from functools import cmp_to_key, lru_cache
from pathlib import Path
from sage.all import AA
HERE=Path(__file__).resolve().parents[1]/'searches'

def module(name,file):
    s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
stars=module('controlstars','penrose-kite-dart-edge-stars.py');align=stars.align
K,w,phi=align.K,align.w,align.phi

def sign(x):a=AA(x);return 1 if a>0 else -1 if a<0 else 0
@lru_cache(None)
def compare(u,v):
    def half(z):
        im=stars.p2.cross_sign((1,0,0,0),tuple(z));re=sign(z+z.conjugate())
        return 0 if im>0 or im==0 and re>=0 else 1
    hu,hv=half(u),half(v)
    if hu!=hv:return -1 if hu<hv else 1
    cr=stars.p2.cross_sign(tuple(u),tuple(v))
    assert cr!=0 or sign(u.conjugate()*v+v.conjugate()*u)<0,'Collinear incident spokes in control embedding'
    return -cr

def embedding_faces(P,V,owners,roles,active,mk,md):
    points={};adj=defaultdict(set)
    def add(a,b):adj[a].add(b);adj[b].add(a)
    for ri,(kind,gv,a) in enumerate(P['tiles']):
        centre=('p',ri);C=V[gv[0]]+w**a*w/(2 if kind=='kite' else 4);points[centre]=C
        # Centre is in the visibility kernel, guaranteeing every fan ray lies
        # inside its source polygon. Exact half-plane determinants only.
        for i in range(4):
            e=V[gv[(i+1)%4]]-V[gv[i]];q=C-V[gv[i]]
            assert stars.p2.cross_sign(tuple(e),tuple(q))>0
        mask=mk if kind=='kite' else md
        for i in range(4):
            if mask>>i&1:
                nd=('v',gv[i]);points[nd]=V[gv[i]];add(centre,nd)
            if roles[kind,i][0] in active:
                nd=('e',*sorted((gv[i],gv[(i+1)%4])));points[nd]=(V[gv[i]]+V[gv[(i+1)%4]])/2;add(centre,nd)
    rotations={nd:sorted(neighbours,key=cmp_to_key(lambda a,b:compare(points[a]-points[nd],points[b]-points[nd]))) for nd,neighbours in adj.items()}
    nxt={}
    for a,neighbours in adj.items():
        for b in neighbours:
            rev=rotations[b];nxt[a,b]=(b,rev[(rev.index(a)-1)%len(rev)])
    visited=set();bounded=[];outer=0
    for start in nxt:
        if start in visited:continue
        cyc=[];cur=start
        while cur not in visited:visited.add(cur);cyc.append(cur[0]);cur=nxt[cur]
        assert cur==start
        area=sum((points[a].conjugate()*points[b]-points[b].conjugate()*points[a]) for a,b in zip(cyc,cyc[1:]+cyc[:1]))
        # Positive imaginary area means counterclockwise bounded face.
        sg=stars.p2.cross_sign((1,0,0,0),tuple(area))
        if sg>0:bounded.append(cyc)
        else:outer+=1
    assert len(visited)==len(nxt)
    return bounded,outer,len(adj),len(nxt)//2

def main():
    a=argparse.ArgumentParser();a.add_argument('--checkpoint',required=True);a.add_argument('--output',required=True);args=a.parse_args()
    rows=stars.p2.checkpoint(Path(args.checkpoint));assert len(rows)==706
    actual={(tuple(r['active_orbits']),r['kite_mask'],r['dart_mask']) for r in rows}
    expected=set()
    tabchecks=0
    for active in [(0,),(1,),(0,1)]:
        masks=[m for m in range(16) if m.bit_count()+2*len(active)>=3]
        expected.update((active,mk,md) for mk in masks for md in masks)
    assert actual==expected
    p3='research/certificates/penrose-kite-dart-patch3.json';p4='research/certificates/penrose-kite-dart-patch4.json'
    P,V,owners,components,roles,pairs=align.source(p4)
    assert align.source(p3)[-1]==pairs
    orbitchecks=[]
    # In every allowed source fan, boundary intervals partition exactly once,
    # and each selected spoke appears twice in opposite directions.
    for active in [(0,),(1,),(0,1)]:
        R,E,D,_,_,records,_=align.geometry(p4,active)
        R3,E3,D3,*_=align.geometry(p3,active)
        assert set(map(str,E))==set(map(str,E3)) and set(map(str,D))==set(map(str,D3))
        orbitchecks.append({'active_orbits':active,'matching_instances':len(records),'distinct_alignment_equations':len(E)})
        for kind in ('kite','dart'):
            for mask in range(16):
                if mask.bit_count()+2*len(active)<3:continue
                boundary,pieces=stars.tables(kind,mask,active,roles)
                assert set(boundary)==set(range(8))
                ds=Counter(e for piece in pieces for e in piece)
                assert all(ds[b,a]==c==1 for (a,b),c in ds.items())
                tabchecks+=1
    traces=[]
    for row in rows:
        if row['dead'] is not None:continue
        active=tuple(row['active_orbits']);mk,md=row['kite_mask'],row['dart_mask']
        faces,outer,nv,ne=embedding_faces(P,V,owners,roles,active,mk,md)
        assert outer==1 and nv-ne+len(faces)==1,'Connected planar Euler control'
        assert len(faces)==row['interior_faces']
        histogram=Counter(len([v for v in c if v[0]!='e']) for c in faces)
        recorded=Counter()
        for c in row['classes']:recorded[c['corners']]+=c['count']
        assert histogram==recorded
        assert all(len(c)==len(set(c)) for c in faces)
        traces.append({'kite_mask':mk,'dart_mask':md,'faces':len(faces),'corner_histogram':dict(histogram),'vertices':nv,'edges':ne,'outer_faces':outer})
    result={'status':'passed','recipe_coverage':706,'fan_table_controls':tabchecks,'orbit_controls':orbitchecks,
            'independent_rotation_system_face_controls':traces,'review_status':'Encoding controls only; not hostile review of exclusion or solver proofs',
            'checkpoint_sha256':hashlib.sha256(Path(args.checkpoint).read_bytes()).hexdigest()}
    stars.p2.atomic_json(Path(args.output),result);print(json.dumps(result),flush=True)
if __name__=='__main__':main()
