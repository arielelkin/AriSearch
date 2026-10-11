"""Exact four-face flat quotient reconnaissance for three alternate Cairo ratios.
Finite scope: two P copies and two Q copies, all mirror choices modulo one
global reflection, both possible f subdivision orders, and all equal-length
edge pairings; native arms stay whole in this restricted search. A positive witness is a compact orientable flat torus.
A failed finite search has no infinite untileability implication.
"""
import argparse
from itertools import product
from pathlib import Path
import json
from sage.all import QuadraticField, AA

K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
RATIOS={'f2c':(28*w+13)/37,'fac':w,'f2a':(20*w-11)/13}

def matchings(items):
    if not items:
        yield []
        return
    first=items[0]
    for j in range(1,len(items)):
        other=items[j]
        rest=items[1:j]+items[j+1:]
        for tail in matchings(rest):
            yield [(first,other)]+tail


def faces_for(kind,flags,cuts):
    a=K(1);b=RATIOS[kind]
    c=((3+w)+(1-w)*b)/4;d=((3-w)+(1+w)*b)/4
    e=(w-1)*(1+b)/2;f=((w-5)+(1+3*w)*b)/4
    values={'a':a,'b':b,'c':c,'d':d,'e':e}
    faces=[]
    for idx in range(4):
        if idx<2:
            labels=['a','b','c','d','e'];angles=[120,90,120,90,120]
        else:
            banks={'f2c':('c','c'),'f2a':('a','a'),'fac':(('a','c') if cuts[idx-2]==0 else ('c','a'))}[kind]
            labels=['a','d','b','c']+list(banks)
            angles=[120,90,120,90,120,180]
            assert values[banks[0]]+values[banks[1]]==f
        if flags[idx]:
            # Start vertex0 stays fixed, reverse edge order around its mirror.
            labels=list(reversed(labels));angles=[angles[0]]+list(reversed(angles[1:]))
        faces.append({'species':'P' if idx<2 else 'Q','mirror':bool(flags[idx]),
                      'labels':labels,'angles':angles,'lengths':[values[x] for x in labels]})
    return faces


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


def search(kind, output_dir=None):
    attempted=0
    for free_flags in product((0,1),repeat=3):
        flags=(0,)+free_flags
        for cuts in product((0,1),repeat=(2 if kind=='fac' else 0)):
            if not cuts:cuts=(0,0)
            faces=faces_for(kind,flags,cuts)
            groups={}
            for u,face in enumerate(faces):
                for i,length in enumerate(face['lengths']):groups.setdefault(length,[]).append((u,i))
            if any(len(items)%2 for items in groups.values()):continue
            options=[list(matchings(items)) for items in groups.values()]
            for choice in product(*options):
                attempted+=1;pairs=[p for block in choice for p in block]
                vertices=evaluate(faces,pairs)
                if vertices:
                    cert={'ratio_name':kind,'ratio_coefficients':[str(x) for x in RATIOS[kind].list()],
                          'faces':[{k:v for k,v in face.items() if k!='lengths'} for face in faces],
                          'paired_edges':pairs,'vertex_classes':vertices,'attempts_before_witness':attempted}
                    if output_dir is not None:
                        path=Path(output_dir)/('partial-contact-cairo-alternate-'+kind+'.json')
                        path.write_text(json.dumps(cert,indent=2)+'\n')
                    print('WITNESS',kind,'attempts',attempted,'vertices',len(vertices))
                    return cert
    print('EXHAUSTED FOUR-FACE DOMAIN',kind,'pairings',attempted)
    return None

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir')
    args=parser.parse_args()
    for kind in RATIOS:search(kind,args.output_dir)
