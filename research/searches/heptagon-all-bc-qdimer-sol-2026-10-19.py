"""Exact symbolic certificate: all BC-pair words, no sampled angle values."""
from itertools import product
from fractions import Fraction as F
import json
from pathlib import Path
starts=(0,5,10,17); sizes=(5,5,7,7)
nxt={s+i:s+(i+1)%n for s,n in zip(starts,sizes) for i in range(n)}
pairs=[(11,18),(13,20),(15,22),(0,10),(5,12),(3,14),(8,16),(6,17),(4,19),(9,21),(2,23),(1,7)]
mate={a:b for a,b in pairs}; mate.update({b:a for a,b in pairs})
cycles=[]; rem=set(range(24))
while rem:
    d=min(rem); cyc=[]; x=d
    while x not in cyc:
        cyc.append(x); x=nxt[mate[x]]
    assert x==d
    rem.difference_update(cyc); cycles.append(cyc)
assert len(cycles)==8 and all(len(c)==3 for c in cycles)
# Angles represented exactly as (constant, coefficient of alpha).
angles={'A':(144,0),'B':(0,1),'C':(252,-1),'P':(108,0)}
words=[]
for bits in product('BC',repeat=3):
    w='A'+''.join(b+('C' if b=='B' else 'B') for b in bits)
    rev=w[0]+w[:0:-1]
    if w>rev: continue
    a=[angles['P']]*10+[angles[c] for c in w]*2
    for cy in cycles:
        assert tuple(sum(a[d][j] for d in cy) for j in (0,1))==(360,0)
    # Relative face rotations in degrees, derived from reversed paired edges.
    heads=[]
    for n,s in zip(sizes,starts):
        h=[(0,0)]
        for i in range(1,n):
            c,k=a[s+i]; h.append((h[-1][0]+180-c,h[-1][1]-k))
        heads+=h
    rot={0:(0,0)}
    face={s+i:f for f,(s,n) in enumerate(zip(starts,sizes)) for i in range(n)}
    for _ in range(4):
        for u,v in pairs:
            f,g=face[u],face[v]
            if f in rot:
                r=(rot[f][0]+heads[u][0]+180-heads[v][0],rot[f][1]+heads[u][1]-heads[v][1])
                r=(r[0]%360,r[1])
                if g in rot: assert rot[g]==r
                else: rot[g]=r
    assert len(rot)==4 and (rot[3][0]-rot[2][0])%360==180 and rot[3][1]==rot[2][1]
    words.append(dict(word=w,face_rotations=rot))
assert [w['word'] for w in words]==['ABCBCBC','ABCBCCB','ABCCBBC','ACBBCBC']
certificate=dict(words=words,pairs=pairs,vertex_cycles=cycles,faces=4,edges=12,vertices=8,euler=0)
Path('research/certificates/heptagon-all-bc-qdimer-sol-2026-10-19.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(certificate,indent=2))
