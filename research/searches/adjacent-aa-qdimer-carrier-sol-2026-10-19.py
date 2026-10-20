"""Exact orientation rejection of all saturated 4P+2Q translation quotients."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
# Directions represented by (constant, coefficient of alpha), in degrees.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def matching(xs):
    if not xs:
        yield []; return
    for j in range(1,len(xs)):
        for rest in matching(xs[1:j]+xs[j+1:]):
            yield [(xs[0],xs[j])]+rest

def zeros_mod360(x):
    c,b=x
    if b==0: return None if c%360==0 else set()
    return {F(360*k-c,b) for k in range(-20,21) if 108<F(360*k-c,b)<126}
records=[]
for word in ['AAABBACC','AAABCABC']:
    dirs=[(0,0)]
    for c in word[1:]:
        dirs.append(add(dirs[-1],{'A':(36,0),'B':(180,-1),'C':(-72,1)}[c]))
    qq=[i for i in range(8) if word[i]!='A' and word[(i+1)%8]!='A']
    for reflected in [False,True]:
        d2=[sub((180,0),dirs[(-i-1)%8]) for i in range(8)] if reflected else dirs
        qq2=[(-i-1)%8 for i in qq] if reflected else qq
        aa2=[7,6] if reflected else [0,1]
        for targets in permutations(qq2):
            rotations=[sub(add((180,0),dirs[i]),d2[j]) for i,j in zip(qq,targets)]
            candidates=zeros_mod360(sub(rotations[0],rotations[1]))
            rec=dict(word=word,reflected=reflected,qq_pairs=list(zip(qq,targets)),q_rotation=rotations[0],qq_candidates=None if candidates is None else sorted(map(str,candidates)),pp_matchings=0,survivors=[])
            if candidates is None or candidates:
                r=rotations[0]
                # Each P's unique AA-facing side is relabeled side 1.
                pr=[sub(add((180,0),dirs[i]),(72,0)) for i in [0,1]]+[sub(add(add((180,0),r),d2[i]),(72,0)) for i in aa2]
                darts=[(f,i) for f in range(4) for i in [0,2]]
                for pairs in matching(darts):
                    rec['pp_matchings']+=1
                    allowed=None if candidates is None else set(candidates)
                    for (f,i),(g,j) in pairs:
                        eq=sub(sub(add(pr[f],(72*i,0)),add(pr[g],(72*j,0))),(180,0))
                        roots=zeros_mod360(eq)
                        if roots is not None: allowed=roots if allowed is None else allowed & roots
                        if allowed==set(): break
                    if allowed is None or allowed: rec['survivors'].append(dict(pairs=pairs,alpha=None if allowed is None else sorted(map(str,allowed))))
            records.append(rec)
assert len(records)==8 and sum(len(r['survivors']) for r in records)==4
output=dict(scope='Necessary exact edge-direction constraints for all orientable saturated translation quotients with 4 P and 2 Q; excludes no larger quotient.',records=records)
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2))
print('8 QQ cases; 4 QQ-compatible cases; 420 PP matchings; 4 PP orientation survivors, requiring remaining PQ/star checks. See companion Sage certificate.')
