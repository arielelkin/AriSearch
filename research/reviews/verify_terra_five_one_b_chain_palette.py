#!/usr/bin/env python3
from itertools import combinations_with_replacement,permutations,combinations
# angle=(slope in x,constant in degrees):x,y,z,r,s.
a=((1,0),(-5,720),(4,-360),(-2,360),(10,-1080))
identities=[t for t in combinations_with_replacement(range(5),3) if sum(a[i][0] for i in t)==0 and sum(a[i][1] for i in t)==360]
assert identities==[(0,0,3),(0,1,2),(1,1,4),(2,3,3)]
assert all(m*120+c==120 for m,c in a)
assert len({m for m,c in a})==5
# With special B corner0=s, BB eligible native sides1,2,3,4.
masks=[m for m in combinations(range(1,5),2) if all((i-j)%6 not in(1,5) for i,j in combinations(m,2))]
assert masks==[(1,3),(1,4),(2,4)]
requirements=[]
for mask in masks:
    colours=[1 if j==0 else 2 if j in mask or (j-1)%6 in mask else 0 for j in range(6)]
    req={tuple(sorted((colours[j],colours[(j+1)%6]))) for j in range(6) if j not in mask}
    requirements.append(req)
assert requirements==[{(2,2),(0,2),(0,1),(1,2)},{(0,2),(1,2)},{(2,2),(0,2),(0,1),(1,2)}]
canonical=lambda w:min(t[k:]+t[:k] for t in(w,w[::-1]) for k in range(6))
words=sorted({canonical(w) for w in permutations((0,0,1,1,2,2))});assert len(words)==11
kept=[];tuples=0
for w in words:
    palette={tuple(sorted((w[j],w[(j+1)%6]))) for j in range(6)}
    valid=[i for i,req in enumerate(requirements) if req<=palette]
    if valid:kept.append(w)
    print("".join(map(str,w)),"saturated masks",[masks[i] for i in valid])
    for mi in valid:
        mask=masks[mi];c=[1 if j==0 else 2 if j in mask or(j-1)%6 in mask else 0 for j in range(6)]
        count=1
        for j in range(6):
            if j in mask:continue
            pair=tuple(sorted((c[j],c[(j+1)%6])))
            native=sum(tuple(sorted((w[k],w[(k+1)%6])))==pair for k in range(6))
            count*=native*(2 if pair[0]==pair[1] else 1)
        tuples+=12*count
assert set(words)-set(kept)=={(0,0,1,2,2,1),(0,1,1,0,2,2)}
assert len(kept)==9 and tuples==1392
print("PASS35tripletypes=>four identities;three saturated BB masks;11A palettes=>nine survivors,1392partial AB tuples before metrics")
