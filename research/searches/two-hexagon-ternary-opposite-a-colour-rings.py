#!/usr/bin/env python3
"""Complete 11-word ternary domain; no solver or metric enumeration."""
from itertools import permutations, product
from collections import Counter
import json
import sys

PLACEMENTS = [(r,s) for s in (1,-1) for r in range(6)]
A = (0,1,2,0,1,2)
def profile(w,r,s):
    return tuple(w[(r+s*k)%6] for k in range(6))
def orbit(w):
    return sorted({profile(w,r,s) for r,s in PLACEMENTS})
def canonical(w):
    return min(v[k:]+v[:k] for v in (w,w[::-1]) for k in range(6))
def main(path):
    bracelets = sorted({canonical(w) for w in permutations((0,0,1,1,2,2))})
    assert len(bracelets)==11
    aw=orbit(A)
    assert len(aw)==6
    for k in range(6):
        assert {(u[k],u[(k+1)%6]) for u in aw} == {(i,j) for i in range(3) for j in range(3) if i!=j}
    rows=[]
    for bw in bracelets:
        profiles=orbit(bw)
        multiplicities=Counter(profile(bw,r,s) for r,s in PLACEMENTS)
        assert max(multiplicities.values())<=2
        states=[]
        for w in profiles:
            choices=[[i for i,u in enumerate(aw)
                      if u[(k+2)%6]==w[k] and u[(k+3)%6]==w[(k-1)%6]] for k in range(6)]
            assert all(len(c)<=1 for c in choices)
            for aa in product(*choices):
                outer=[[aw[aa[k]][(k+1)%6],aw[aa[(k+1)%6]][(k+5)%6]] for k in range(6)]
                assert any(x!=y for x,y in outer)
                states.append({'B':w,'A_ring':aa,'outer_AA_endpoint_colour_pairs':outer})
        relations=[[(i,j) for i,u in enumerate(states) for j,v in enumerate(states)
                    if u['A_ring'][k]==v['A_ring'][(k+4)%6]
                    and u['A_ring'][(k+1)%6]==v['A_ring'][(k+3)%6]] for k in range(6)]
        assert not any(relations)
        rows.append({'B_native_word':bw,'B_colour_profiles':profiles,
                     'B_native_profile_fibre_sizes':[multiplicities[w] for w in profiles],
                     'ring_states':states,'overlap_relations':relations,'survivors':[],
                     'first_deletion_round':[[i,0] for i in range(len(states))]})
        print(''.join(map(str,bw)),len(states),'rings; all six overlap relations empty',flush=True)
    assert sum(len(r['ring_states']) for r in rows)==24
    result={'scope':'generic ternary angles; A native word012012; only same-colour AAB stars; complete 11 B bracelets; exact colour profiles, not native metric labels',
            'A_native_word':A,'A_colour_profiles':aw,'rows':rows}
    with open(path,'w') as f:json.dump(result,f,indent=2)
if __name__=='__main__':main(sys.argv[1])
