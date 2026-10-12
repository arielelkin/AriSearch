#!/usr/bin/env python3
"""Independent 136-word metric domain and complete A-ring quotient audit."""
import argparse,collections,hashlib,importlib.util,itertools,json
from pathlib import Path
sp=importlib.util.spec_from_file_location('independent_native_ring_edges',Path(__file__).with_name('check_two_hexagon_interleaved_local_side_gate.py'))
local=importlib.util.module_from_spec(sp);sp.loader.exec_module(local);g=local.g
def relations(states):
    answer=[]
    for delta in g.DELTA:
        overlaps=[(i,j) for i,x in enumerate(g.D) for j,y in enumerate(g.D) if x==g.add(delta,y)]
        answer.append({(i,j) for i,a in enumerate(states) for j,b in enumerate(states) if all(a['A_ring'][p]==b['A_ring'][q] for p,q in overlaps)})
    return answer
def prune(rel,n):
    out=[collections.defaultdict(set) for _ in range(6)]
    for k,edges in enumerate(rel):
        for i,j in edges:out[k][i].add(j)
    alive=set(range(n));trace=[]
    while alive:
        bad=[]
        for i in sorted(alive):
            for k in range(6):
                direction=g.DELTA.index(g.sub(g.DELTA[(k+1)%6],g.DELTA[k]))
                left=out[k][i]&alive;right=out[(k+1)%6][i]&alive
                if not any(out[direction][j]&right for j in left):bad.append([i,k]);break
        if not bad:break
        trace.append(bad);alive-={i for i,k in bad}
    return sorted(alive),trace
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/two-hexagon-interleaved-alternating-private-transport.json');cert=json.loads(path.read_text())
    states=[];full=0;odd=0
    for bi,bp in enumerate(g.P):
        bw=g.placed(g.WORDS['ALT'],bp);choices=[]
        for z in g.D:
            incidences=[inc for inc in g.INC if z in inc]
            choices.append([i for i,p in enumerate(g.P) if all(g.placed(g.WORDS['I'],p)[inc[z]]==bw[inc[(0,0)]] for inc in incidences)])
        for aa in itertools.product(*choices):
            full+=1
            ab=[];aa_seams=[]
            for k,z in enumerate(g.D):
                inward=g.D.index(g.sub((0,0),z));ab.append(g.side(g.P[aa[k]],(inward-1)%6))
                j=(k+1)%6;direction=g.D.index(g.sub(g.D[j],z));reverse=g.D.index(g.sub(z,g.D[j]))
                aa_seams.append((g.side(g.P[aa[k]],(direction-1)%6),g.side(g.P[aa[j]],(reverse-1)%6)))
            if any(index%2!=1 for index in ab):continue
            odd+=1
            if any(i!=j for i,j in aa_seams):continue
            states.append({'B':bi,'A_ring':list(aa),'native_side_closure':list(local.closure(bp,[g.P[i] for i in aa]))})
    assert (full,odd,len(states))==(49152,8748,216)
    assert states==cert['domain_states'] and full==cert['full_native_ring_count'] and odd==cert['odd_AB_ring_count'] and len(states)==cert['self_indexed_AA_ring_count']
    partitions=[]
    for p in itertools.product(range(3),repeat=3):
        if p[0]==0 and all(p[i]<=max(p[:i])+1 for i in (1,2)):partitions.append(p)
    assert partitions==list(map(tuple,cert['A_odd_partitions']))
    keys=[]
    for p in partitions:
        inventory=collections.Counter({value:2*count for value,count in collections.Counter(p).items()})
        keys.extend((p,w) for w in itertools.product(range(max(p)+1),repeat=6) if collections.Counter(w)==inventory)
    assert len(keys)==136 and keys==[(tuple(row['A_odd_partition']),tuple(row['B_side_word'])) for row in cert['rows']]
    allrel=relations(states);stats=collections.Counter();nonempty=[];tori=0
    for row in cert['rows']:
        eq=row['A_odd_partition'];word=row['B_side_word'];ids=[]
        for i,q in enumerate(states):
            okay=True
            for k in range(6):
                z=g.D[(k+1)%6];inward=g.D.index(g.sub((0,0),z));aindex=g.side(g.P[q['A_ring'][(k+1)%6]],(inward-1)%6)
                assert aindex%2==1
                if word[g.side(g.P[q['B']],k)]!=eq[(aindex-1)//2]:okay=False;break
            if okay:ids.append(i)
        assert ids==row['starting_domain_state_ids']
        mapping={i:j for j,i in enumerate(ids)}
        rel=[{(mapping[i],mapping[j]) for i,j in edges if i in mapping and j in mapping} for edges in allrel]
        assert rel==[set(map(tuple,r)) for r in row['compatibility']]
        alive,trace=prune(rel,len(ids));assert alive==row['surviving_local_ids'] and trace==row['triangle_deletion_rounds']
        assert [ids[i] for i in alive]==row['surviving_domain_ids']
        subset=[states[i] for i in ids];signatures=sorted({tuple(subset[i]['A_ring']) for i in alive})
        fibres=[[i for i in alive if tuple(subset[i]['A_ring'])==signature] for signature in signatures]
        qid={i:j for j,fibre in enumerate(fibres) for i in fibre}
        qrel=[{(qid[i],qid[j]) for i,j in edges if i in qid and j in qid} for edges in rel]
        degrees=[max((sum(i==a for a,b in edges) for i in range(len(signatures))),default=0) for edges in qrel]
        qq=row['overlap_signature_quotient']
        assert signatures==list(map(tuple,qq['A_ring_signatures'])) and fibres==qq['full_ring_fibres_local_ids'] and qrel==[set(map(tuple,r)) for r in qq['compatibility']] and degrees==qq['maximum_successor_degrees']
        # Every quotient edge is complete across its full central-B fibres.
        for k,edges in enumerate(qrel):
            assert {(i,j) for a,b in edges for i in fibres[a] for j in fibres[b]}=={(i,j) for i,j in rel[k] if i in qid and j in qid}
        if not alive:stats['EMPTY']+=1
        elif degrees==[1]*6:
            assert len(alive)==12 and len(signatures)==6 and all(len(f)==2 for f in fibres)
            maps=[[next(b for a,b in edges if a==i) for i in range(6)] for edges in qrel]
            assert all(sorted(f)==list(range(6)) for f in maps)
            assert all(maps[i][maps[j][q]]==maps[j][maps[i][q]] for i,j,q in itertools.product(range(6),range(6),range(6)))
            witness=row['index_six_metric_witness'];assert witness['hnf']==[6,1,1]
            lengths=[0,3+eq[0],1,3+eq[1],2,3+eq[2]]+[3+c for c in word]
            assert witness['side_length_classes']==lengths
            assert g.verify_torus(witness,'I','ALT',lengths)==(12,36)
            closure=witness['required_side_closure']
            assert len({closure[i] for i in (0,2,4)})==3
            assert {closure[i] for i in (0,2,4)}.isdisjoint({closure[i] for i in (1,3,5,6,7,8,9,10,11)})
            tori+=1
            stats['FUNCTIONAL_A_RING_QUOTIENT']+=1;nonempty.append({'partition':eq,'B_word':word,'full_states':12,'quotient_states':6})
        else:
            assert eq==[0,0,0] and word==[0]*6 and len(alive)==216 and len(signatures)==36 and all(len(f)==6 for f in fibres)
            stats['UNRESOLVED_EQUAL_ODD']+=1
    assert dict(stats)=={'UNRESOLVED_EQUAL_ODD':1,'FUNCTIONAL_A_RING_QUOTIENT':12,'EMPTY':123}
    assert tori==12
    result={'status':'PASSED','native_domain_counts':[full,odd,len(states)],'proper_odd_length_partitions':5,'metric_words':136,'reviewed_outcomes':dict(stats),'functional_quotient_words':nonempty,'index_six_metric_tori':tori,'torus_native_vertex_stars':144,'torus_directed_seams':432,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'123 words empty,12 nonconstant words have periodic escapes via full A-ring quotient and direct metric tori preserving arbitrary even A lengths; equal odd lengths/B equilateral remains unresolved'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
