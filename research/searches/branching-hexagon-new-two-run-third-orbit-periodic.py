"""Exact1024 two-copy native-seam lifts for third catalog orbit representative.
Normal replay read-only; --output explicitly retains a positive quotient.
Failed1024lifts would not exclude an infinite tiling.
"""
import argparse,json,runpy
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations_with_replacement
from collections import Counter
helper=runpy.run_path(str(Path(__file__).with_name('branching-hexagon-new-two-run-catalog-slot-periodic.py')))
quad=[150,150,90,150]

def evaluate(faces,pairs,legal):
    n=len(faces)*6;parent=list(range(n));size=[1]*n
    root=lambda x: find(x)
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    for (u,i),(v,j) in pairs:
        for a,b in[(6*u+i,6*v+(j+1)%6),(6*u+(i+1)%6,6*v+j)]:
            a,b=find(a),find(b)
            if a!=b:
                if size[a]+size[b]>3:return None
                parent[b]=a;size[a]+=size[b]
    classes={}
    for u,f in enumerate(faces):
        for i in range(6):classes.setdefault(find(6*u+i),[]).append((u,i))
    if any(len(cls)!=3 or tuple(sorted((faces[u]['species_index']*6+((-i)%6 if faces[u]['mirror'] else i)) for u,i in cls)) not in legal for cls in classes.values()):return None
    graph=[set() for f in faces]
    for (u,i),(v,j) in pairs:graph[u].add(v);graph[v].add(u)
    seen={0};todo=[0]
    while todo:
        for v in graph[todo.pop()]-seen:seen.add(v);todo.append(v)
    if len(seen)!=len(faces):return None
    assert len(classes)-len(pairs)+len(faces)==0
    return list(classes.values())

def search(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-new-two-run-catalog-slot-balance.json'
    row=next(r for r in json.loads(source.read_text())['records'] if r['quad']==quad)
    geom=helper['geometry'](quad);p,labels,angles,pts=geom
    legal={t for t in combinations_with_replacement(range(12),3) if angles[t[0]]*angles[t[1]]*angles[t[2]]==1}
    skeleton=set()
    for cyc,x in zip(row['oriented_stars'],row['star_frequencies']):
        if not F(x):continue
        assert F(x)==F(1,2)
        for cycle in(cyc,[o^1 for o in reversed(cyc)]):
            for k,o in enumerate(cycle):
                oo=cycle[(k+1)%3];s,i=(o//2)//6,(o//2)%6;fl=o%2;t,j=(oo//2)//6,(oo//2)%6;fl2=oo%2
                ex=i if fl else(i-1)%6;ey=(j-1)%6 if fl2 else j
                a=(2*s+fl,5-ex if fl else ex);b=(2*t+fl2,5-ey if fl2 else ey)
                skeleton.add(tuple(sorted((a,b))))
    nonself=sorted(x for x in skeleton if x[0]!=x[1]);selfs=sorted(x[0] for x in skeleton if x[0]==x[1]);degree=Counter(e for pair in nonself for e in pair);degree.update(selfs)
    assert len(nonself)==10 and len(selfs)==4 and len(degree)==24 and set(degree.values())=={1}
    base=[{'species_index':s,'species':'A' if s==0 else 'B','mirror':bool(fl),'labels':labels[s][::-1] if fl else labels[s]} for s in(0,1) for fl in(0,1)]
    faces=[dict(f,base_face=u,copy=t) for u,f in enumerate(base) for t in(0,1)]
    for count,bits in enumerate(product((0,1),repeat=10),1):
        pairs=[((2*u+t,i),(2*v+(t^bit),j)) for ((u,i),(v,j)),bit in zip(nonself,bits) for t in(0,1)]+[((2*u,i),(2*u+1,i)) for u,i in selfs]
        verts=evaluate(faces,pairs,legal)
        if verts:
            r={'quad':quad,'faces':faces,'paired_edges':pairs,'vertex_classes':verts,'lift_bits':bits,'attempts_before_witness':count,'finite_domain':'1024 two-copy lifts of exact third-orbit primal seam support'}
            if output:Path(output).write_text(json.dumps(r,indent=2)+'\n')
            print('WITNESS',count,'faces',8,'edges',24,'vertices',16);return r
    print('EXHAUSTED SPECIFIED1024LIFTS');return None
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();search(a.output)
