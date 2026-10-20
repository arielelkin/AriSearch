#!/usr/bin/env python3
"""Independent fixed-map audit. Does not import either construction/search script."""
import json, hashlib, time, sys
from pathlib import Path
from collections import Counter, defaultdict
import z3
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'research/searches/deep-p-wheel-incidence-sol-2026-10-19.json'
data=json.loads(source.read_text())
summary={}
for parent,d in data.items():
    fs=d['faces']; boundary=d['boundary']; words=d['corner_words']; species=d['species']
    edgefaces=defaultdict(list); directed=Counter()
    for j,t in enumerate(fs):
        assert len(set(t))==3
        for a,b in zip(t,t[1:]+t[:1]):
            edgefaces[tuple(sorted((a,b)))].append(j); directed[a,b]+=1
    vertices=set(v for t in fs for v in t)
    deg=Counter(v for e in edgefaces for v in e)
    assert dict(deg)==d['degrees']
    assert all(deg[v]==5 for v in ['z','i0','i1','i2','i3','i4'])
    assert set(vertices)-set(boundary)=={'z','i0','i1','i2','i3','i4'}
    # Reconstruct the specified disk without using the generator's advance walk.
    expected=[['z','i1','i0'],['z','i2','i1'],['z','i3','i2'],['z','i4','i3'],['z','i0','i4'],
      ['i0','a1','a0'],['i0','i1','a1'],['i1','a2','a1'],['i1','i2','a2'],
      ['i2','a3','a2'],['i2','i3','a3'],['i3','a4','a3'],['i3','i4','a4'],
      ['i4','a0','a4'],['i4','i0','a0'],['a0','a1','e0']]
    if parent=='P':expected.append(['a0','e0','e1'])
    assert fs==expected
    expected_boundary=(['a0','e1','e0','a1','a2','a3','a4'] if parent=='P' else ['a0','e0','a1','a2','a3','a4'])
    assert boundary==expected_boundary
    assert {v for v,t in species.items() if t=='Q'}==({'a0','a1'} if parent=='P' else {'a0','a1','a3'})
    assert set(words)==set(species)==vertices
    bd={tuple(sorted((a,b))) for a,b in zip(boundary,boundary[1:]+boundary[:1])}
    assert {e for e,f in edgefaces.items() if len(f)==1}==bd
    assert len(vertices)-len(edgefaces)+len(fs)==1
    for e,f in edgefaces.items():
        assert len(f) in (1,2)
        if len(f)==2: assert directed[e]==directed[e[::-1]]==1
    nodes=defaultdict(list)
    for v,w in words.items():
        assert len(set(w))==len(w)==(5 if species[v]=='P' else 7)
        for x in w:nodes[x].append(v)
        # Independently recover vertex link and check its manifold type.
        adj=defaultdict(set)
        for t in fs:
            if v in t:
                a,b=[x for x in t if x!=v];adj[a].add(b);adj[b].add(a)
        seen=set(); stack=[next(iter(adj))]
        while stack:
            a=stack.pop()
            if a not in seen: seen.add(a);stack.extend(adj[a]-seen)
        assert seen==set(adj)
        assert sorted(map(len,adj.values()))==(([1,1]+[2]*(len(adj)-2)) if v in boundary else [2]*len(adj))
    assert set(nodes)=={'f'+str(j) for j in range(len(fs))}|{'t'+str(j) for j in range(len(boundary))}|{'u'+str(j) for j in range(1,5 if parent=='P' else 7)}
    assert sum(map(len,words.values()))==3*len(fs)+2*len(boundary)+(4 if parent=='P' else 6)
    for j,t in enumerate(fs):assert sorted(nodes['f'+str(j)])==sorted(t)
    for k,a in enumerate(boundary):assert sorted(nodes['t'+str(k)])==sorted([a,boundary[(k+1)%len(boundary)]])
    expected_seams={}
    for e,ff in edgefaces.items():
        ends=['f'+str(j) for j in ff]
        if e in bd:ends+=['t'+str(next(k for k,a in enumerate(boundary) if set(e)=={a,boundary[(k+1)%len(boundary)]}))]
        assert len(ends)==2
        directions=[]
        for v in e:
            w=words[v]; candidates=[(a,b) for a,b in zip(w,w[1:]+w[:1]) if {a,b}==set(ends)]
            assert len(candidates)==1;directions+=candidates
        assert directions[0]==directions[1][::-1]
        expected_seams[e]=set(ends)
    assert len(d['seams'])==len(expected_seams)
    for seam in d['seams']:assert expected_seams[tuple(sorted(seam['children']))]==set(seam['endpoints'])
    # Outer child boundary consists exactly of incoming t, ordered untouched corners, outgoing t.
    roles={'t'+str(len(boundary)-1):0}; nextcorner=1; arc=[]
    for k,v in enumerate(boundary):
        w=words[v]; start=w.index('t'+str((k-1)%len(boundary))); end=w.index('t'+str(k))
        outer=[];q=(start+1)%len(w)
        while q!=end:outer.append(w[q]);q=(q+1)%len(w)
        assert outer==['u'+str(j) for j in range(nextcorner,nextcorner+len(outer))]
        for x in outer:assert nodes[x]==[v];roles[x]=nextcorner;nextcorner+=1
        arc.append(len(outer))
        assert len(outer)==d['parent_corners_per_arc'][v]
    assert roles==d['parent_corner_roles']
    assert nextcorner==(5 if parent=='P' else 7)
    assert Counter(species.values())==({'P':11,'Q':2} if parent=='P' else {'P':9,'Q':3})
    summary[parent]={'V':len(vertices),'E':len(edgefaces),'F':len(fs),'arc_corners':arc,'native_total':sum(map(len,words.values())),'interior_P':6,'split_corner_count':1}
# Alternative formulation: each child has a bounded integer phase and Boolean orientation;
# nested If maps the phase to each of the native real variables. No selector permutation disjunctions.
s=z3.Solver();s.set(timeout=180000,random_seed=0)
a={t:[z3.Real('native_'+t+str(i)) for i in range(n)] for t,n in [('P',5),('Q',7)]}
for t in a:
    s.add(z3.Sum(a[t])==(3 if t=='P' else 5))
    s.add(*[z3.And(x>0,x<1) for x in a[t]])
nodes=defaultdict(list);d=data['P']
for v,w in d['corner_words'].items():
    aa=a[d['species'][v]];n=len(aa);p=z3.Int('phase_'+v);flip=z3.Bool('flip_'+v)
    s.add(p>=0,p<n)
    if '--orbit' in sys.argv:
        values=[z3.Real('corner_'+v+'_'+str(k)) for k in range(n)]
        branches=[]
        for orient in (aa,list(reversed(aa))):
            for shift in range(n):
                rotated=orient[shift:]+orient[:shift]
                branches.append(z3.And(*[x==y for x,y in zip(values,rotated)]))
        s.add(z3.Or(*branches))
        for node,val in zip(w,values):nodes[node].append(val)
        continue
    for k,node in enumerate(w):
        vals=[z3.If(flip,aa[(j-k)%n],aa[(j+k)%n]) for j in range(n)]
        val=vals[-1]
        for j in reversed(range(n-1)):val=z3.If(p==j,vals[j],val)
        nodes[node].append(val)
for node,vals in nodes.items():
    target=a['P'][d['parent_corner_roles'][node]] if node in d['parent_corner_roles'] else (2 if node[0]=='f' else 1)
    s.add(z3.Sum(vals)==target)
start=time.monotonic();status=s.check()
out={'topology':'PASS','counts':summary,'P_angle_status':str(status),'seconds':time.monotonic()-start,'timeout_ms':180000,'z3':z3.get_version_string(),'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'encoding':('explicit rotated and reversed native-angle orbit' if '--orbit' in sys.argv else 'bounded integer phases, Boolean reflections, nested If native lookup')+'; exact strict LRA'}
if status==z3.unknown:out['reason_unknown']=s.reason_unknown()
Path(__file__).with_suffix('.orbit.json' if '--orbit' in sys.argv else '.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
