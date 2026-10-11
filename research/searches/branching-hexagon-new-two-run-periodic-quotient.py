"""Exact sixteen guided lifts of cos15 two-run native-edge support.
Normal replay is read-only; --output explicitly retains a positive quotient.
"""
import argparse,json
from pathlib import Path
from itertools import product
def evaluate(faces,pairs):
    offsets=[];total=0
    for face in faces:offsets.append(total);total+=len(face['angles'])
    parent=list(range(total));weight=[x for face in faces for x in face['angles']]
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for (u,i),(v,j) in pairs:
        n=len(faces[u]['angles']);m=len(faces[v]['angles'])
        for x,y in ((offsets[u]+i,offsets[v]+(j+1)%m),
                    (offsets[u]+(i+1)%n,offsets[v]+j)):
            x,y=root(x),root(y)
            if x!=y:
                if weight[x]+weight[y]>360:return None
                parent[y]=x;weight[x]+=weight[y]
    roots={root(i) for i in range(total)}
    if any(weight[r]!=360 for r in roots):return None
    graph=[set() for f in faces]
    for (u,i),(v,j) in pairs:graph[u].add(v);graph[v].add(u)
    reached={0};todo=[0]
    while todo:
        for nxt in graph[todo.pop()]-reached:reached.add(nxt);todo.append(nxt)
    if len(reached)!=len(faces):return None
    assert len(roots)-len(pairs)+len(faces)==0
    return [[(u,i) for u,face in enumerate(faces) for i in range(len(face['angles']))
             if root(offsets[u]+i)==r] for r in roots]

def search(output=None):
    base=[{'species':'A','mirror':False,'labels':['p','q']*3,'angles':[135,105]*3},
          {'species':'B','mirror':False,'labels':['p','p','p','q','q','q'],'angles':[105,120,120,135,90,150]}]
    faces=[dict(f,base_face=u,copy=t) for u,f in enumerate(base) for t in(0,1)]
    nonself=[((0,0),(1,0)),((0,1),(1,4)),((0,2),(1,2)),((0,4),(1,1))]
    selfs=[(0,3),(0,5),(1,3),(1,5)]
    for k,bits in enumerate(product((0,1),repeat=4),1):
        pairs=[((2*u+t,i),(2*v+(t^bit),j)) for ((u,i),(v,j)),bit in zip(nonself,bits) for t in(0,1)]+[((2*u,i),(2*u+1,i)) for u,i in selfs]
        v=evaluate(faces,pairs)
        if v:
            r={'kind':'two-run-cos15','faces':faces,'paired_edges':pairs,'vertex_classes':v,'lift_bits':bits,'attempts_before_witness':k,'finite_domain':'16 two-copy lifts of exact four-star primal orientation0 seam support'}
            if output:Path(output).write_text(json.dumps(r,indent=2)+'\n')
            print('WITNESS',k,'faces',4,'edges',12,'vertices',8);return r
    print('EXHAUSTED16LIFTS');return None
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();search(a.output)
