#!/usr/bin/env python3
"""Bounded exact 4-face mixed-period attack; not an arbitrary tiling search.
All native/atomic same-length side pairings, both placement chiralities.
"""
import argparse
import itertools
import json
from pathlib import Path


def matchings(xs):
    if not xs:
        yield [];return
    a,*tail=xs
    for i,b in enumerate(tail):
        for rest in matchings(tail[:i]+tail[i+1:]):
            yield [(a,b)]+rest


def query(atomic):
    if atomic:
        angles=[[60,180,60,150,120,150]]*2+[[60,60,150,120,150]]*2
        words=[['D','E','b','C','D','e']]*2+[['C','E','t','t','E']]*2
    else:
        angles=[[60,60,150,120,150]]*4
        words=[['a','b','C','D','e']]*2+[['C','E','t','t','E']]*2
    offsets=[sum(map(len,angles[:f])) for f in range(4)]
    total=sum(map(len,angles));groups={}
    for f,W in enumerate(words):
        for i,name in enumerate(W):groups.setdefault(name,[]).append((f,i))
    choices=[list(matchings(group)) for group in groups.values()]
    trials=connected_trials=solutions=0
    for signs in itertools.product((1,-1),repeat=3):
        signs=(1,)+signs
        for matches in itertools.product(*choices):
            pairs=list(itertools.chain.from_iterable(matches));trials+=1
            parents=list(range(total));links=[[] for _ in range(total)]
            def root(i):
                while parents[i]!=i:i=parents[i]
                return i
            def join(i,j):
                parents[root(i)]=root(j);links[i].append(j);links[j].append(i)
            adj={f:set() for f in range(4)}
            for(f,i),(g,j) in pairs:
                adj[f].add(g);adj[g].add(f)
                u,v=offsets[f]+i,offsets[f]+(i+1)%len(words[f])
                w,x=offsets[g]+j,offsets[g]+(j+1)%len(words[g])
                if signs[f]==signs[g]:join(u,x);join(v,w)
                else:join(u,w);join(v,x)
            seen={0};todo=[0]
            while todo:
                f=todo.pop()
                for g in adj[f]:
                    if g not in seen:seen.add(g);todo.append(g)
            if len(seen)!=4:continue
            connected_trials+=1
            vertices={}
            for f,A in enumerate(angles):
                for i,value in enumerate(A):vertices.setdefault(root(offsets[f]+i),[]).append(value)
            assert all(len(link)==2 for link in links)
            if all(sum(values)==360 for values in vertices.values()):
                assert len(vertices)-len(pairs)+4==0
                solutions+=1
    assert trials==(3240 if atomic else 216)
    assert solutions==0
    return dict(atomic_long_side_split=atomic,face_count=4,
                A_faces=2,B_faces=2,side_words=words,angle_words=angles,
                trial_count=trials,connected_trial_count=connected_trials,
                legal_flat_tori=solutions)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path)
    args=p.parse_args()
    result=dict(scope='Bounded same-length four-face quotient gate only; no exclusion of larger tori or different subdivisions',
                rows=[query(False),query(True)])
    if args.check:assert json.loads(args.check.read_text())==result
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
