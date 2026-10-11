"""Independent raw geometry and actual circular flat-torus links for all12 targets."""
from pathlib import Path
from collections import Counter
import json
from sage.all import QQbar,AA
ROOT=Path(__file__).resolve().parents[2];DIR=ROOT/'research/certificates'
slot=json.loads((DIR/'branching-hexagon-new-two-run-catalog-slot-balance.json').read_text())
cert=json.loads((DIR/'branching-hexagon-new-two-run-catalog-periodic-transfers.json').read_text())
assert len(cert['records'])==12
assert {tuple(r['quad'])for r in cert['records']}=={tuple(r['quad'])for r in slot['records']if r['status']=='sat'}
z=QQbar.zeta(24)
labels=[['p','q']*3,['p']*3+['q']*3]
def raw(quad):
    a,b,c,d=quad
    P=[z**(k//15)for k in(0,180-a,360-a-b)]
    Q=[z**(k//15)for k in(0,180-c,360-c-d)]
    p=QQbar(AA((sum(Q)*sum(Q).conjugate()).real()/(sum(P)*sum(P).conjugate()).real()).sqrt())
    rotation=-p*sum(P)/sum(Q)
    edges=[[(p if i%2==0 else 1)*z**(deg//15)for i,deg in enumerate((0,75,120,195,240,315))],
           [p*v for v in P]+[rotation*v for v in Q]]
    vertices=[]
    for es in edges:
        pts=[];at=QQbar(0)
        for edge in es:pts.append(at);at+=edge
        assert at==0;vertices.append(pts)
    return p,vertices
counts=Counter()
for record in cert['records']:
    p,base=raw(record['quad']);sp,source=raw(record['source_quad'])
    scale=QQbar(1)if record['common_scale']=='1'else p
    assert record['common_scale']in('1','target_p')and scale>0
    for species,mapping in enumerate(record['native_congruences']):
        sign=mapping['native_orientation'];k=mapping['native_vertex_shift'];assert sign in(-1,1)and 0<=k<6
        transform=lambda v:v if sign==1 else v.conjugate()
        denom=transform(source[species][1]-source[species][0])
        rot=(base[species][(k+sign)%6]-base[species][k])/denom
        assert rot*rot.conjugate()==scale*scale
        assert all(base[species][(k+sign*i)%6]-base[species][k]
                   ==rot*transform(source[species][i]-source[species][0])for i in range(6))
    faces=[];angle=[];edges=[]
    for f in record['faces']:
        s=0 if f['species']=='A'else 1;mirror=f['mirror'];assert f['species']in('A','B')
        assert f['labels']==(labels[s][::-1]if mirror else labels[s])
        pts=[base[s][(-i)%6].conjugate()for i in range(6)]if mirror else list(base[s])
        es=[pts[(i+1)%6]-pts[i]for i in range(6)]
        assert all((es[i].conjugate()*(pts[j]-pts[i])).imag()>0
                   for i in range(6)for j in range(6)if j not in(i,(i+1)%6))
        norm=lambda i:p if f['labels'][i]=='p'else QQbar(1)
        units=[es[i]/norm(i)for i in range(6)]
        assert all(u*u.conjugate()==1 for u in units)
        angle.append([-units[i].conjugate()*units[i-1]for i in range(6)])
        faces.append(pts);edges.append(es)
    n=len(faces);assert n in(4,8);counts[n]+=1
    paired={};graph={i:set()for i in range(n)}
    for x,y in record['paired_edges']:
        a,b=tuple(x),tuple(y);assert a!=b and a not in paired and b not in paired
        paired[a]=b;paired[b]=a;graph[a[0]].add(b[0]);graph[b[0]].add(a[0])
        u,v=edges[a[0]][a[1]],edges[b[0]][b[1]];assert u*u.conjugate()==v*v.conjugate()
    assert set(paired)=={(i,j)for i in range(n)for j in range(6)}
    seen={0};todo=[0]
    while todo:
        i=todo.pop()
        for j in graph[i]-seen:seen.add(j);todo.append(j)
    assert len(seen)==n
    visited=set();links=[]
    for start in paired:
        if start in visited:continue
        at=start;cycle=[]
        while at not in visited:
            visited.add(at);cycle.append(at);i,j=paired[at];at=(i,(j+1)%6)
        assert at==start and len(cycle)==3
        product=QQbar(1)
        for i,j in cycle:product*=angle[i][j]
        assert product==1;links.append(cycle)
    assert len(links)==2*n and len(links)-len(paired)//2+n==0
    assert {frozenset(x)for x in links}=={frozenset(map(tuple,x))for x in record['vertex_classes']}
    print('PASS periodic',record['quad'],n,'nativefaces',len(links),'actual360 circularlinks',flush=True)
assert counts=={4:8,8:4}
print('PASS all12 exact native similarities/common scales and direct target flat-torus constructions;8 fourface targets,4 eightface targets;no producer imports')
