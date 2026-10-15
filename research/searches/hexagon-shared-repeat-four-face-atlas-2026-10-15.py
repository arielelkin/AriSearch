#!/usr/bin/env python3
"""Complete FIXED four-face torus witness atlas for one shared-repeat family.
Domain: two indexed A, two indexed B, all8 sign choices modulo global flip,
and105*3^4 color-respecting pairings. Absence is never aperiodicity evidence.
Stdlib-only; deterministic JSON stdout; explicit --output writes evidence.
"""
from itertools import product
from collections import defaultdict
from pathlib import Path
import argparse
import json

WORDS=((0,1,0,2,3,4),(0,3,0,2,1,4))

def matchings(items):
    if not items:
        yield ()
        return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        for rest in matchings(items[1:j]+items[j+1:]):
            yield ((a,b),)+rest

def build():
    records={};totals=defaultdict(int)
    for tail in product((1,-1),repeat=3):
        signs=(1,)+tail
        groups=defaultdict(list)
        for f in range(4):
            for k in range(6):
                side=k if signs[f]==1 else (-k-1)%6
                groups[WORDS[f//2][side]].append(6*f+k)
        choices=[list(matchings(tuple(groups[c]))) for c in range(5)]
        assert list(map(len,choices))==[105,3,3,3,3]
        for per_color in product(*choices):
            pairs=tuple(pair for block in per_color for pair in block)
            totals['all_pairings']+=1
            faces=[set() for _ in range(4)]
            for a,b in pairs:
                faces[a//6].add(b//6);faces[b//6].add(a//6)
            reached={0}
            while True:
                more=reached|set().union(*(faces[f] for f in reached))
                if more==reached:break
                reached=more
            if len(reached)<4:continue
            totals['connected_pairings']+=1
            parent=list(range(24))
            def find(i):
                while parent[i]!=i:
                    parent[i]=parent[parent[i]];i=parent[i]
                return i
            def unite(a,b):
                a,b=find(a),find(b)
                if a!=b:parent[b]=a
            for a,b in pairs:
                f,k=divmod(a,6);g,l=divmod(b,6)
                unite(6*f+k,6*g+(l+1)%6)
                unite(6*f+(k+1)%6,6*g+l)
            vertices=defaultdict(list)
            for c in range(24):vertices[find(c)].append(c)
            if len(vertices)!=8 or any(len(v)!=3 for v in vertices.values()):continue
            totals['trivalent_tori']+=1
            triples=[]
            for v in vertices.values():
                actual=[]
                for c in v:
                    f,k=divmod(c,6)
                    native_vertex=(signs[f]*k)%6
                    actual.append(6*(f//2)+(native_vertex-1)%6)
                triples.append(tuple(sorted(actual)))
            signature=tuple(sorted(set(triples)))
            records.setdefault(signature,{'signs':signs,'edge_pairs':pairs,
                'vertex_triples':sorted(triples),'angle_support':signature})
    assert totals['all_pairings']==68040
    return {'schema':'SHARED_REPEAT_FOUR_FACE_TORUS_ATLAS_V1',
        'A':WORDS[0],'B':WORDS[1],
        'domain':{'faces':['A','A','B','B'],'orientation_choices':8,
            'r_matchings':105,'other_matching_choices':81,'total':68040,
            'corner_convention':'native corner after side i; A0..5 B6..11'},
        'counts':dict(totals),'distinct_angle_supports':len(records),
        'witnesses':[records[s] for s in sorted(records)]}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args()
    data=build();encoded=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if a.output:Path(a.output).write_text(encoded)
    print(encoded,end='')

if __name__=='__main__':main()
