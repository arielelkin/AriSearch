"""Replay the exact pinned four-face quotient at p=sqrt(2+sqrt3).
Normal replay is read-only; raw geometry is checked by the development producer.
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

def replay():
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-new-two-run-sqrt2plus3-four-face-periodic.json'
    r=json.loads(source.read_text());actual=evaluate(r['faces'],r['paired_edges'])
    assert {frozenset(map(tuple,x)) for x in actual}=={frozenset(map(tuple,x)) for x in r['vertex_classes']}
    print('PASS pinned4facequotient;12edges8vertices')
if __name__=='__main__':replay()
