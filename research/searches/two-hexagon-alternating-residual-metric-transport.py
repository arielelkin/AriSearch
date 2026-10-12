#!/usr/bin/env python3
"""Direct side-matched native rings for the37 remaining ALT metric orbits.

Intrinsic shape aliases have identical six corner colours and six side classes,
so canonical replacement preserves every actual angle/length seam. Raw full
native rings are retained before this reversible geometric alias quotient.
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

local=module('residual_native','research/searches/two-hexagon-interleaved-local-side-gate.py')
colour=module('residual_prune','research/searches/two-hexagon-rank-nine-colour-transport.py')

def alias(word):
    profiles=[tuple(local.WORDS['ALT'][local.corner(i,k)] for k in range(6))+
              tuple(word[local.side(i,k)] for k in range(6)) for i in range(12)]
    return [profiles.index(p) for p in profiles],profiles

def states(a,b):
    raw=[]
    for bs in range(12):
        w=[local.WORDS['ALT'][local.corner(bs,k)] for k in range(6)]
        choices=[[i for i in range(12)
                  if local.WORDS['ALT'][local.corner(i,k+2)]==w[k]
                  and local.WORDS['ALT'][local.corner(i,k+3)]==w[(k-1)%6]
                  and a[local.side(i,k+2)]==b[local.side(bs,k-1)]] for k in range(6)]
        for aa in itertools.product(*choices):
            if all(a[local.side(aa[k],k+1)]==a[local.side(aa[(k+1)%6],k+4)] for k in range(6)):
                raw.append({'B':bs,'A_ring':list(aa)})
    am,ap=alias(a);bm,bp=alias(b)
    keys=sorted({(bm[q['B']],tuple(am[i] for i in q['A_ring'])) for q in raw})
    canonical=[{'B':bs,'A_ring':list(aa)} for bs,aa in keys]
    return raw,canonical,am,bm,ap,bp

def main(source,path):
    ledger=json.load(open(source));rows=[]
    for row in ledger['rows']:
        k=max(row['A_native_side_partition'])+1
        if k==6 or row['verdict']=='NO_ADMISSIBLE_ACTUAL_METRIC':continue
        a=row['A_native_side_partition'];b=row['B_native_side_word']
        raw,qs,am,bm,ap,bp=states(a,b);rel=colour.relations(qs);alive,trace=colour.prune(qs,rel)
        degrees=[max((sum(x==i and y in alive for x,y in edges) for i in alive),default=0) for edges in rel]
        signatures=sorted({tuple(qs[i]['A_ring']) for i in alive});qid={i:signatures.index(tuple(qs[i]['A_ring'])) for i in alive}
        qrel=[sorted({(qid[x],qid[y]) for x,y in edges if x in qid and y in qid}) for edges in rel]
        qdegree=[max((sum(x==i for x,y in edges) for i in range(len(signatures))),default=0) for edges in qrel]
        fibres=[[i for i in alive if qid[i]==j] for j in range(len(signatures))]
        verdict='EMPTY' if not alive else 'FUNCTIONAL_DIRECTION' if min(degrees)<=1 else 'FUNCTIONAL_OVERLAP_QUOTIENT' if min(qdegree)<=1 else 'BRANCHING'
        rec={'joint_metric_orbit_id':row['id'],'A_native_side_partition':a,'B_native_side_word':b,
             'geometry_verdict':row['verdict'],'geometry_exception_angles':row['admissible_rank_drop_angles'],
             'raw_full_native_ring_states':raw,'A_alias_map':am,'B_alias_map':bm,'A_slot_profiles':ap,'B_slot_profiles':bp,
             'canonical_ring_states':qs,'compatibility':rel,'triangle_deletion_rounds':trace,'survivors':alive,
             'maximum_successor_degrees':degrees,'overlap_signature_quotient':{'A_ring_signatures':signatures,
                 'full_ring_fibres':fibres,'compatibility':qrel,'maximum_successor_degrees':qdegree},'verdict':verdict}
        rows.append(rec)
        print(row['id'],'raw',len(raw),'canonical',len(qs),'core',len(alive),'Q',len(signatures),verdict,flush=True)
    assert len(rows)==37
    out={'scope':'37 necessary residual ALT joint metric orbits (k4/k5) after local all-distinct obstruction; full local corner/side matching with exact intrinsic shape alias canonicalization; no geometry-existence inference',
         'joint_geometry_source':source,'stats':dict(Counter(r['verdict'] for r in rows)),'rows':rows}
    with open(path,'w') as f:json.dump(out,f,indent=2)
    print('FINAL',out['stats'],flush=True)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
