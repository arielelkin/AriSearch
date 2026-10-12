#!/usr/bin/env python3
"""Independent full native index-nine torus and reflected-ring verification."""
import argparse,hashlib,importlib.util,itertools,json
from pathlib import Path
sp=importlib.util.spec_from_file_location('independent_private_transport',Path(__file__).with_name('check_two_hexagon_interleaved_alternating_private_transport.py'))
private=importlib.util.module_from_spec(sp);sp.loader.exec_module(private);g=private.g
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/two-hexagon-interleaved-alternating-equal-odd-torus.json');cert=json.loads(path.read_text())
    source=json.loads(Path('research/certificates/two-hexagon-interleaved-alternating-private-transport.json').read_text())
    states=[q for q in source['domain_states'] if all(g.P[q['A_ring'][k]][1]==-g.P[q['A_ring'][(k+1)%6]][1] for k in range(6))]
    assert len(states)==36 and states==cert['reflection_ring_states']
    for q in states:
        assert list(private.local.closure(g.P[q['B']],[g.P[i] for i in q['A_ring']]))==q['native_side_closure']
    rel=private.relations(states);assert rel==[set(map(tuple,r)) for r in cert['compatibility']]
    signatures=sorted({tuple(q['A_ring']) for q in states});assert len(signatures)==6 and signatures==list(map(tuple,cert['A_ring_signatures']))
    fibres=[[i for i,q in enumerate(states) if tuple(q['A_ring'])==p] for p in signatures]
    assert fibres==cert['full_ring_fibres'] and all(len(f)==6 for f in fibres)
    qid={i:j for j,f in enumerate(fibres) for i in f}
    qr=[{(qid[i],qid[j]) for i,j in r} for r in rel]
    assert qr==[set(map(tuple,r)) for r in cert['quotient_compatibility']]
    maps=[]
    for edges in qr:
        assert len(edges)==6 and {i for i,j in edges}==set(range(6))
        maps.append([next(j for i,j in edges if i==k) for k in range(6)])
    assert maps==cert['quotient_successors']
    assert all(maps[k][maps[k][maps[k][i]]]==i for k,i in itertools.product(range(6),range(6)))
    torus=cert['torus'];assert torus['hnf']==[3,0,3]
    cells=list(map(tuple,torus['cell_order']));assert cells==[(x,y) for y in range(3) for x in range(3)]
    labels=dict(zip(cells,torus['labels']));assert len(labels)==9
    lengths=[0,3,1,3,2,3]+[3]*6;assert torus['side_length_classes']==lengths
    def at(z):return labels[z[0]%3,z[1]%3]
    stars=[];seams=[];parent=list(range(12));reflected_aa=0
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    for z in sorted(cells):
        species,p=divmod(at(z),12)
        for o in (0,1):
            entries=[];colours=[]
            for cell,k in zip((z,g.add(z,g.D[o]),g.add(z,g.D[o+1])),(o,o+2,o+4)):
                s,pi=divmod(at(cell),12);corner=(g.P[pi][0]+g.P[pi][1]*k)%6
                entries.append(6*s+corner);colours.append(g.WORDS['I' if s==0 else 'ALT'][corner])
            assert sorted(i//6 for i in entries)==[0,0,1] and len(set(colours))==1;stars.append(entries)
        for k in range(6):
            other,pi=divmod(at(g.add(z,g.D[(k+1)%6])),12)
            i=6*species+g.side(g.P[p],k);j=6*other+g.side(g.P[pi],(k+3)%6)
            assert lengths[i]==lengths[j];seams.append([i,j]);parent[find(j)]=find(i)
            if species==other==0:
                assert i==j and i%2==0 and g.P[p][1]==-g.P[pi][1];reflected_aa+=1
    assert stars==torus['vertex_stars'] and seams==torus['side_equalities'] and len(stars)==18 and len(seams)==54
    classes={};closure=[]
    for i in range(12):
        root=find(i)
        if root not in classes:classes[root]=len(classes)
        closure.append(classes[root])
    assert closure==[0,1,2,1,3,1]+[1]*6 and reflected_aa==18
    result={'status':'PASSED','reflected_native_rings':36,'full_A_ring_signatures':6,'quotient_cycle_orders':3,'torus_index':9,'native_vertex_stars':18,'directed_native_seams':54,'reflected_directed_AA_seams':18,'exact_required_native_side_closure':closure,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Universal direct periodic escape for I/ALT equal odd A lengths/equilateral B, preserving all three even A lengths independently'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
