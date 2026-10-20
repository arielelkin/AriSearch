from collections import Counter
import json
core=[tuple('i'+str(x) for x in t[::-1]) for t in [(0,1,2),(0,2,3),(0,3,5),(3,4,5)]]
inner=0;outer=0
for advances in [0,2,1,0,2,1]:
    for _ in range(advances):
        nxt=(outer+1)%6
        core.append((f'i{inner}',f'a{nxt}',f'a{outer}'));outer=nxt
    nxt=(inner+1)%6
    core.append((f'i{inner}',f'i{nxt}',f'a{outer}'));inner=nxt

def make(which):
    faces=list(core)
    boundary=['a0','a1','a2','a3','a4','a5']
    qs={'a0','a1','a3'}
    if which=='P':
        faces.append(('a0','a1','e0'))
        boundary=['a0','e0','a1','a2','a3','a4','a5']
        qs={'a0','a3'}
    preliminary_edges=set(tuple(sorted((t[k],t[(k+1)%3]))) for t in faces for k in range(3))
    dd=Counter(v for e in preliminary_edges for v in e)
    corners={v:(7 if v in qs else 5)-dd[v]-1 for v in boundary}
    edges=Counter(tuple(sorted((t[k],t[(k+1)%3]))) for t in faces for k in range(3))
    directed=Counter((t[k],t[(k+1)%3]) for t in faces for k in range(3))
    assert all(n in [1,2] for n in edges.values())
    assert all(directed[(u,v)]==directed[(v,u)]==1 for (u,v),n in edges.items() if n==2)
    bedges={tuple(sorted((boundary[k],boundary[(k+1)%len(boundary)]))) for k in range(len(boundary))}
    assert {e for e,n in edges.items() if n==1}==bedges
    vs=set(sum((list(t) for t in faces),[]))
    assert len(vs)-len(edges)+len(faces)==1
    deg=Counter(v for e in edges for v in e)
    species={v:('Q' if v in qs else 'P') for v in vs}
    for v in vs:
        native=deg[v]+1+corners[v] if v in corners else deg[v]
        assert native==(7 if v in qs else 5),(which,v,native)
    assert Counter(species.values())==({'P':11,'Q':2} if which=='P' else {'P':9,'Q':3})
    assert sum(corners.values())==({'P':4,'Q':6}[which])
    # Each vertex link must be a connected path on boundary, cycle inside.
    for v in vs:
        link=[tuple(w for w in t if w!=v) for t in faces if v in t]
        ld=Counter(w for e in link for w in e)
        seen={next(iter(ld))}
        while True:
            new=seen|{w for e in link if any(x in seen for x in e) for w in e}
            if new==seen: break
            seen=new
        assert seen==set(ld)
        assert sorted(ld.values())==([1,1]+[2]*(len(ld)-2) if v in corners else [2]*len(ld))
    # Explicit primal corner/seam incidence; face labels f0,... are seam junctions.
    words={}
    parent_index=1
    parent_roles={f't{len(boundary)-1}':0}
    for v in boundary:
        k=boundary.index(v)
        par=[f'u{j}' for j in range(parent_index,parent_index+corners[v])]
        parent_index+=corners[v]
        for u in par: parent_roles[u]=int(u[1:])
        links={}
        for j,t in enumerate(faces):
            if v in t:
                z=t.index(v); x=t[(z+1)%3]; y=t[(z+2)%3]
                links[x]=(y,f'f{j}')
        x=boundary[(k-1)%len(boundary)]; end=boundary[(k+1)%len(boundary)]
        chain=[]
        while x!=end:
            x,f=links[x];chain.append(f)
        words[v]=[f't{(k-1)%len(boundary)}']+par+[f't{k}']+list(reversed(chain))
    for v in sorted(vs-set(boundary)):
        links={}
        for j,t in enumerate(faces):
            if v in t:
                z=t.index(v);links[t[(z+1)%3]]=(t[(z+2)%3],f'f{j}')
        start=min(links);x=start;chain=[]
        while True:
            x,f=links[x];chain.append(f)
            if x==start:break
        words[v]=list(reversed(chain))
    seams=[]
    for edge in sorted(edges):
        ends=[f'f{j}' for j,t in enumerate(faces) if set(edge)<=set(t)]
        if edge in bedges:
            k=next(k for k in range(len(boundary)) if set(edge)=={boundary[k],boundary[(k+1)%len(boundary)]})
            ends.append(f't{k}')
        assert len(ends)==2
        assert all(set(ends)<=set(words[v]) for v in edge)
        assert all(any({words[v][k],words[v][(k+1)%len(words[v])]}==set(ends) for k in range(len(words[v]))) for v in edge)
        directions=[]
        for v in edge:
            w=words[v]
            directions.append(next((w[k],w[(k+1)%len(w)]) for k in range(len(w)) if {w[k],w[(k+1)%len(w)]}==set(ends)))
        assert directions[0]==directions[1][::-1]
        seams.append({'children':edge,'endpoints':ends})
    assert all(len(words[v])==(7 if species[v]=='Q' else 5) for v in vs)
    assert all(c>=0 for c in corners.values())
    assert len(faces)==({'P':17,'Q':16}[which])
    assert len(vs-set(boundary))==6
    return {'corner_words':words,'seams':seams,'parent_corner_roles':parent_roles,'faces':faces,'boundary':boundary,'species':species,'parent_corners_per_arc':corners,'degrees':dict(deg)}
cert={which:make(which) for which in ['P','Q']}
out=__import__('pathlib').Path(__file__).with_suffix('.json')
out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print('PASS: J=1 disks, links, species, primal seam endpoints; '+str(out))
