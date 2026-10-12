#!/usr/bin/env python3
"""Exact constrained angle-state census for all odd-component pair graphs.

Six A corners have pair-degree two, loops counted twice. This is the
unique-B-corner AAB family only, not the full higher-rank registry.
"""
import importlib.util,itertools,json,sys
from collections import Counter
from pathlib import Path

spec=importlib.util.spec_from_file_location('rings',Path('research/searches/two-hexagon-balanced-root-cyclic-orders.py'))
ring=importlib.util.module_from_spec(spec);spec.loader.exec_module(ring)

def graphs():
    edges=list(itertools.combinations_with_replacement(range(6),2))
    result=[]
    def search(start,degrees,chosen):
        if len(chosen)==6:
            assert not any(degrees)
            result.append(tuple(chosen));return
        for i in range(start,len(edges)):
            a,b=edges[i]
            if a==b:
                if degrees[a]<2:continue
            elif not degrees[a] or not degrees[b]:continue
            reduced=list(degrees);reduced[a]-=1;reduced[b]-=1
            search(i,tuple(reduced),chosen+[edges[i]])
    search(0,(2,)*6,[])
    return result

def components(edges):
    neighbors={i:set() for i in range(6)}
    for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
    unseen=set(range(6));sizes=[]
    while unseen:
        todo=[min(unseen)];seen=set()
        while todo:
            a=todo.pop()
            if a in seen:continue
            seen.add(a);todo+=list(neighbors[a]-seen)
        unseen-=seen;sizes.append(len(seen))
    return tuple(sorted(sizes,reverse=True))

def cyclic_orders(edges):
    orders=set()
    for order in set(itertools.permutations(edges)):
        equivalent=[order[k:]+order[:k] for k in range(6)]
        reverse=tuple(reversed(order))
        equivalent += [reverse[k:]+reverse[:k] for k in range(6)]
        orders.add(min(equivalent))
    return sorted(orders)

def main(output):
    G=graphs()
    assert len(G)==388
    selected=[g for g in G if any(n%2 for n in components(g))]
    assert len(selected)==268
    expected={(5,1):72,(4,1,1):45,(3,3):10,(3,2,1):60,(3,1,1,1):20,
              (2,2,1,1):45,(2,1,1,1,1):15,(1,1,1,1,1,1):1}
    assert dict(Counter(components(g) for g in selected))==expected
    rows=[];stats=Counter();component_stats={};metadata=[]
    for gi,g in enumerate(selected):
        shape=components(g);orders=cyclic_orders(g)
        metadata.append({'id':gi,'edges':g,'components':shape,'cyclic_order_count':len(orders)})
        for pairs in orders:
            states=ring.ring_states(pairs);relations=ring.compatibility(states)
            edge_alive,deleted=ring.prune(states,relations)
            alive,triangle_deleted=ring.triangle_prune(edge_alive,relations)
            degrees=[max((sum(a==i and b in alive for a,b in rel) for i in alive),default=0) for rel in relations]
            verdict='EMPTY' if not alive else ('FUNCTIONAL' if min(degrees)<=1 else 'BRANCHING')
            stats[verdict]+=1;component_stats.setdefault(shape,Counter())[verdict]+=1
            rows.append({'id':len(rows),'graph_id':gi,'B_pair_order':pairs,'states':states,
                         'compatibility':relations,'edge_deletion_rounds':deleted,
                         'edge_consistent_states':edge_alive,'triangle_deletion_rounds':triangle_deleted,
                         'surviving_states':alive,'max_successor_degrees':degrees,'verdict':verdict})
        if gi%20==0:print('graphs',gi+1,'orders',len(rows),'stats',dict(stats),flush=True)
    data={'domain':'All labeled pair-degree2 pseudographs on six native A corners with an odd component; B pair-value cyclic orders modulo rotation and reversal (parallel occurrence duplicates identified).',
          'all_pair_graphs':388,'odd_component_graphs':268,'rooted_order_count':len(rows),
          'stats':dict(stats),'component_stats':{'-'.join(map(str,k)):dict(v) for k,v in component_stats.items()},
          'graphs':metadata,'rows':rows}
    Path(output).write_text(json.dumps(data,separators=(',',':')))
    print('FINAL',len(rows),'orders',dict(stats),data['component_stats'],flush=True)

if __name__=='__main__':main(sys.argv[1])
