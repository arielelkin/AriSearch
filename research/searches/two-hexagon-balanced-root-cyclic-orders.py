#!/usr/bin/env python3
"""Solver-free census of the 600 rooted cyclic orders of the balanced root.

Domain: A has native order 0..5; ten unordered A-group partitions; sixty
B pair-label cyclic orders modulo D6. These are rooted representatives,
not necessarily inequivalent under dihedral changes of A.
"""
import itertools,json,sys
from collections import Counter

PLACEMENTS=[(r,s) for s in (1,-1) for r in range(6)]
def ring_states(pairs):
    states=[]
    for br,bs in PLACEMENTS:
        relations=[]
        for k in range(6):
            target=set(pairs[(br+bs*k)%6])
            relations.append([(i,j) for i,(ar,as_) in enumerate(PLACEMENTS)
                              for j,(cr,cs) in enumerate(PLACEMENTS)
                              if {(ar+as_*(k+2))%6,(cr+cs*(k+4))%6}==target])
        def walk(path):
            k=len(path)-1
            if k==5:
                if (path[-1],path[0]) in relations[5]:
                    states.append({'B':[br,bs],'A_ring':path})
                return
            for a,b in relations[k]:
                if a==path[-1]:walk(path+[b])
        for first in range(12):walk([first])
    return states

def compatibility(states):
    return [[(i,j) for i,a in enumerate(states) for j,b in enumerate(states)
             if a['A_ring'][k]==b['A_ring'][(k+4)%6]
             and a['A_ring'][(k+1)%6]==b['A_ring'][(k+3)%6]] for k in range(6)]

def prune(states,relations):
    alive=set(range(len(states)))
    records=[]
    rounds=0
    while alive:
        bad=[]
        for i in sorted(alive):
            for k,rel in enumerate(relations):
                if not any(a==i and b in alive for a,b in rel):
                    bad.append([i,k]);break
        if not bad:break
        records.append(bad)
        alive-={i for i,k in bad}
        rounds+=1
    return sorted(alive),records

def triangle_prune(alive,relations):
    alive=set(alive)
    outgoing=[{} for _ in range(6)]
    for k,rel in enumerate(relations):
        for a,b in rel:outgoing[k].setdefault(a,set()).add(b)
    records=[]
    while alive:
        bad=[]
        for i in sorted(alive):
            for k in range(6):
                js=outgoing[k].get(i,set())&alive
                ls=outgoing[(k+1)%6].get(i,set())&alive
                if not any(outgoing[(k+2)%6].get(j,set())&ls for j in js):
                    bad.append([i,k]);break
        if not bad:break
        records.append(bad);alive-={i for i,k in bad}
    return sorted(alive),records

def main(output):
    groups=[(g,tuple(i for i in range(6) if i not in g))
            for g in itertools.combinations(range(6),3) if 0 in g]
    orders=[(0,)+p for p in itertools.permutations(range(1,6)) if p[0]<p[-1]]
    assert len(groups)==10 and len(orders)==60
    rows=[]
    for partition in groups:
        edges=sorted(itertools.combinations(partition[0],2))+sorted(itertools.combinations(partition[1],2))
        for order in orders:
            pairs=[edges[i] for i in order]
            states=ring_states(pairs)
            relations=compatibility(states)
            alive,deleted=prune(states,relations)
            edge_alive=alive
            alive,triangle_deleted=triangle_prune(alive,relations)
            degrees=[max((sum(a==i and b in alive for a,b in rel) for i in alive),default=0) for rel in relations]
            row={'id':len(rows),'A_groups':partition,'B_pair_order':pairs,
                 'T':[list(pair)+[6+i] for i,pair in enumerate(pairs)],
                 'states':states,'compatibility':relations,'deletion_rounds':deleted,
                 'edge_consistent_states':edge_alive,'triangle_deletion_rounds':triangle_deleted,
                 'max_successor_degrees':degrees,'functional_directions':[k for k,d in enumerate(degrees) if d<=1] if alive else [],
                 'surviving_states':alive,'verdict':'EMPTY' if not alive else 'SURVIVOR'}
            rows.append(row)
        print('partition',partition,'completed',flush=True)
    out={'domain':'10 unordered A triple-group partitions x 60 B cyclic pair orders modulo D6; A native order fixed',
         'rooted_order_count':len(rows),'stats':dict(Counter(row['verdict'] for row in rows)),
         'state_counts':dict(Counter(len(row['states']) for row in rows)),
         'surviving_ids':[row['id'] for row in rows if row['surviving_states']],
         'rows':rows}
    with open(output,'w') as f:json.dump(out,f,separators=(',',':'))
    print('FINAL',out['stats'],'survivors',out['surviving_ids'],flush=True)

if __name__=='__main__':main(sys.argv[1])
