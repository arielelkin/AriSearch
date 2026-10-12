#!/usr/bin/env python3
"""I/ALT private-side transport over all 136 AB length words.

Only native even A sides are AA, self-index matched. Odd A side lengths have
one of five partitions; every B side lies in one of those classes, with twice
the native A multiplicity. No assumption about coincidences with even A
lengths is made. Geometry of full shape closure is still a separate gate.
"""
import importlib.util
import itertools
import json
import sys
from collections import Counter

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

local=module('local_private','research/searches/two-hexagon-interleaved-local-side-gate.py')
colour=module('colour_private','research/searches/two-hexagon-rank-nine-colour-transport.py')

def domain():
    states=[];full=0;odd=0
    for bs in range(12):
        w=[local.WORDS['ALT'][local.corner(bs,k)] for k in range(6)]
        choices=[[a for a in range(12)
                  if local.WORDS['I'][local.corner(a,k+2)]==w[k]
                  and local.WORDS['I'][local.corner(a,k+3)]==w[(k-1)%6]]
                 for k in range(6)]
        for aa in itertools.product(*choices):
            full+=1
            if any(local.side(aa[k],k+2)%2!=1 for k in range(6)):continue
            odd+=1
            if any(local.side(aa[k],k+1)!=local.side(aa[(k+1)%6],k+4) for k in range(6)):continue
            states.append({'B':bs,'A_ring':list(aa),'native_side_closure':local.closure(bs,aa)})
    return full,odd,states

def main(path):
    full,odd,states=domain();rows=[]
    partitions=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)]
    for eq in partitions:
        mult=Counter(eq);alphabet=range(max(eq)+1)
        words=[w for w in itertools.product(alphabet,repeat=6)
               if Counter(w)==Counter({c:2*n for c,n in mult.items()})]
        for w in words:
            ids=[i for i,q in enumerate(states)
                 if all(w[local.side(q['B'],k)]==eq[(local.side(q['A_ring'][(k+1)%6],k+3)-1)//2]
                        for k in range(6))]
            subset=[states[i] for i in ids];rel=colour.relations(subset)
            alive,trace=colour.prune(subset,rel)
            degrees=[max((sum(a==i and b in alive for a,b in edges) for i in alive),default=0) for edges in rel]
            signatures=sorted({tuple(subset[i]['A_ring']) for i in alive})
            qid={i:signatures.index(tuple(subset[i]['A_ring'])) for i in alive}
            qrel=[sorted({(qid[a],qid[b]) for a,b in edges if a in qid and b in qid}) for edges in rel]
            qdegrees=[max((sum(a==i for a,b in edges) for i in range(len(signatures))),default=0) for edges in qrel]
            fibres=[[i for i in alive if qid[i]==j] for j in range(len(signatures))]
            witness=None
            if signatures and eq!=(0,0,0):
                assert len(signatures)==6 and qdegrees==[1]*6
                successors=[[next(b for a,b in edges if a==j) for j in range(6)] for edges in qrel]
                assert successors[0][0]==0
                second=successors[1][0]
                assert successors[1][second]==0 and successors[0][second]==second
                labels=[None]*6
                for h,q in [(0,0),(3,second)]:
                    state=subset[fibres[q][0]]
                    labels[h]=12+state['B']
                    for k,(dx,dy) in enumerate(colour.D):
                        z=(h+dx-dy)%6;a=state['A_ring'][k]
                        assert labels[z] in (None,a)
                        labels[z]=a
                length_classes=[0,3+eq[0],1,3+eq[1],2,3+eq[2]]+[3+c for c in w]
                witness=colour.check_torus(6,labels,'I','ALT',length_classes)
                witness['side_length_classes']=length_classes
            rows.append({'A_odd_partition':eq,'B_side_word':w,'starting_domain_state_ids':ids,
                         'compatibility':rel,'triangle_deletion_rounds':trace,
                         'surviving_local_ids':alive,'surviving_domain_ids':[ids[i] for i in alive],
                         'maximum_successor_degrees':degrees,
                         'overlap_signature_quotient':{'A_ring_signatures':signatures,
                             'full_ring_fibres_local_ids':fibres,'compatibility':qrel,
                             'maximum_successor_degrees':qdegrees},
                         'index_six_metric_witness':witness,
                         'verdict':'EMPTY' if not alive else 'FUNCTIONAL_DIRECTION' if min(degrees)<=1 else 'BRANCHING'})
    result={'scope':'Necessary private-side/full-native ring and exact AB length-class words; no polygon closure or Euclidean existence implied',
            'full_native_ring_count':full,'odd_AB_ring_count':odd,'self_indexed_AA_ring_count':len(states),
            'domain_states':states,'A_odd_partitions':partitions,'metric_word_count':len(rows),
            'stats':dict(Counter(r['verdict'] for r in rows)),'rows':rows}
    with open(path,'w') as f:json.dump(result,f,indent=2)
    print(full,odd,len(states),'words',len(rows),result['stats'],flush=True)
    print('nonempty',[(i,r['A_odd_partition'],r['B_side_word'],len(r['surviving_domain_ids']),r['maximum_successor_degrees'])
                      for i,r in enumerate(rows) if r['verdict']!='EMPTY'],flush=True)

if __name__=='__main__':main(sys.argv[1])
