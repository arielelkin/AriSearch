#!/usr/bin/env python3
"""Direct index-nine metric torus for I/ALT with equal odd A lengths.

Constructive all-AA-reflection subset, without solver or carrier geometry.
All three even A lengths remain independent.
"""
import importlib.util
import json
import sys

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

colour=module('equal_odd_colour','research/searches/two-hexagon-rank-nine-colour-transport.py')
local=module('equal_odd_native','research/searches/two-hexagon-interleaved-local-side-gate.py')

def main(source,path):
    d=json.load(open(source))
    states=[q for q in d['domain_states']
            if all(local.P[q['A_ring'][k]][1]==-local.P[q['A_ring'][(k+1)%6]][1]
                   for k in range(6))]
    rel=colour.relations(states)
    signatures=sorted({tuple(q['A_ring']) for q in states})
    qid={i:signatures.index(tuple(q['A_ring'])) for i,q in enumerate(states)}
    qrel=[sorted({(qid[a],qid[b]) for a,b in edges}) for edges in rel]
    successors=[[next(b for a,b in edges if a==i) for i in range(len(signatures))] for edges in qrel]
    assert all(len(edges)==len(signatures) for edges in qrel)
    fibres=[[i for i in range(len(states)) if qid[i]==j] for j in range(len(signatures))]
    labels={}
    def put(z,sym):
        z=(z[0]%3,z[1]%3)
        assert labels.get(z,sym)==sym
        labels[z]=sym
    q=0
    for x in range(3):
        state=states[fibres[q][0]]
        put((x,x),12+state['B'])
        for k,(dx,dy) in enumerate(colour.D):put((x+dx,x+dy),state['A_ring'][k])
        q=successors[0][q]
    assert q==0 and len(labels)==9
    lengths=[0,3,1,3,2,3]+[3]*6
    stars=[];seams=[]
    for (x,y),sym in sorted(labels.items()):
        t=sym//12;p=sym%12
        for k in (0,1):
            native=[];colours=[];species=[]
            for dx,dy,slot in [(0,0,k),(*colour.D[k],(k+2)%6),(*colour.D[(k+1)%6],(k+4)%6)]:
                z=labels[((x+dx)%3,(y+dy)%3)];tz=z//12;j=local.corner(z%12,slot)
                native.append(6*tz+j);species.append(tz)
                colours.append(local.WORDS['I' if tz==0 else 'ALT'][j])
            assert sorted(species)==[0,0,1] and len(set(colours))==1
            stars.append(native)
        for k in range(6):
            dx,dy=colour.D[(k+1)%6];z=labels[((x+dx)%3,(y+dy)%3)]
            i=6*t+local.side(p,k);j=6*(z//12)+local.side(z%12,k+3)
            assert lengths[i]==lengths[j]
            seams.append([i,j])
    result={'scope':'Constructive subset: all AA seams reflected; all three Aeven lengths independent; all Aodd and B sides equal',
            'source':source,'reflection_ring_states':states,'compatibility':rel,
            'A_ring_signatures':signatures,'full_ring_fibres':fibres,'quotient_compatibility':qrel,
            'quotient_successors':successors,
            'torus':{'hnf':[3,0,3],'cell_order':[[x,y] for y in range(3) for x in range(3)],
                     'labels':[labels[(x,y)] for y in range(3) for x in range(3)],
                     'vertex_stars':stars,'side_equalities':seams,'side_length_classes':lengths}}
    with open(path,'w') as f:json.dump(result,f,indent=2)
    print('reflection rings',len(states),'overlap quotient',len(signatures),'torus index',len(labels),flush=True)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
