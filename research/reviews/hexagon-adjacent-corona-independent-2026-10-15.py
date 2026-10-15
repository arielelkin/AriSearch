#!/usr/bin/env python3
"""Independent anchored-sector reconstruction of three necessary tile coronas."""
from itertools import product,permutations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'research/certificates/hexagon-adjacent-corona-states-2026-10-15.json').read_text())
A=(0,0,1,2,3,4)
EXPECTED=(
((2,2,1,3,0,4),{(0,1,1),(0,5,10),(2,2,6),(3,4,11),(3,7,8),(4,5,9)}),
((2,2,1,3,0,4),{(0,10,10),(1,8,9),(2,6,7),(3,7,8),(4,5,9),(6,11,11)}),
((0,1,3,0,4,2),{(0,1,6),(0,5,9),(1,2,11),(2,3,7),(3,4,10),(4,5,8)}))

def reconstruct(W,S):
    def color(side):return W[side//6][side%6]
    opts={c:set() for c in range(12)}
    # Fix the host sector's directed arms. Enumerate both possible orders
    # of the other two occurrences and each guest sector's independent flip.
    for c in range(12):
        f,i=divmod(c,6);host=(6*f+i,6*f+(i+1)%6)
        for t in S:
            tt=list(t)
            if c not in tt:continue
            tt.remove(c)
            for d,e in set(permutations(tt)):
                for fd,fe in product((0,1),repeat=2):
                    g,j=divmod(d,6);h,k=divmod(e,6)
                    ds=(6*g+j,6*g+(j+1)%6);es=(6*h+k,6*h+(k+1)%6)
                    dl,dr=ds[fd],ds[1-fd];el,er=es[fe],es[1-fe]
                    if color(host[1])==color(dl) and color(dr)==color(el) and color(er)==color(host[0]):
                        opts[c].add(((er,e),(dl,d)))
    states=[set(),set()]
    for f in (0,1):
        for chosen in product(*(opts[6*f+i] for i in range(6))):
            signature=[]
            for i in range(6):
                j,dprev=chosen[(i-1)%6][1];k,dafter=chosen[i][0]
                if j!=k:break
                g,l=divmod(j,6)
                if {dprev,dafter}!={6*g+(l-1)%6,6*g+l}:break
                signature.append((j,dprev,dafter))
            else:states[f].add(tuple(signature))
    return opts,states

def guest_options(f,state,i,states):
    j,x,y=state[i];g,k=divmod(j,6)
    inverse={x:6*f+(i-1)%6,y:6*f+i}
    wanted=(6*f+i,inverse[6*g+(k-1)%6],inverse[6*g+k])
    return [s for s in states[g] if s[k]==wanted]

def freeze(states):return [{tuple(tuple(x) for x in s) for s in species} for species in states]
assert tuple(D['A'])==A and len(D['records'])==3
for n,(r,(B,S)) in enumerate(zip(D['records'],EXPECTED)):
    assert tuple(r['B'])==B and {tuple(t) for t in r['support']}==S
    opts,initial=reconstruct((A,B),S)
    assert [[list(map(list,p)) for p in sorted(opts[c])] for c in range(12)]==r['corner_port_options']
    assert initial==freeze(r['initial_tile_states'])
    states=initial
    while True:
        nxt=[{s for s in states[f] if all(guest_options(f,s,i,states) for i in range(6))} for f in (0,1)]
        if nxt==states:break
        states=nxt
    assert states==freeze(r['fixed_tile_states'])
    assert tuple(map(len,states))==((2,1),(1,2),(2,1))[n]
    raw=[[tuple(tuple(x) for x in s) for s in species] for species in r['fixed_tile_states']]
    for f in (0,1):
        for k,s in enumerate(raw[f]):
            for i in range(6):
                possible=guest_options(f,s,i,raw)
                g=s[i][0]//6
                assert [raw[g].index(z) for z in possible]==r['neighbor_state_choices'][f][k][i]
                count=len(possible)
                if n==0 and f==0 and i==2:
                    assert count==2 and s[i][0]==2
                elif n==1 and f==1 and i==5:
                    assert count==2 and s[i][0]==11
                else:assert count==1
    if n==0:
        assert (2,2,6) in S
        # Both A copies at this endpoint use native side 3 to reach B.
        assert all(s[3][0]//6==1 for s in states[0])
    if n==1:
        assert (0,10,10) in S
        assert all(s[4][0]//6==0 for s in states[1])
print('PASS: independent corner ports, all three complete coronas, reciprocal choices, two uncertain-edge bypasses, third fully deterministic corona')
