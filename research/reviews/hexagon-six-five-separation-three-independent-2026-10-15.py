"""Independent separation-three census and geometry-bridge finite check.
Reuses only the independent stdlib reviewer utility, never producer code.
"""
import runpy,itertools as it,json
from collections import defaultdict
from pathlib import Path
D=runpy.run_path(str(Path(__file__).with_name('hexagon-six-five-independent-2026-10-15.py')))
stars,canon,closes,torus,deterministic=[D[x] for x in ['stars','canon','closes','torus','deterministic']]
def rolecanonical(B):
    choices=[]
    for orientation in [B,B[::-1]]:
        for i in range(6):
            w=orientation[i:]+orientation[:i]
            if w[0]==w[3]:choices.append(w)
    return min(choices)
words=set();survivors=defaultdict(set)
for k in range(6):
    for common in it.combinations(range(6),k):
        labels=common+tuple(range(6,11-k))
        for p,q,r,s,t in it.permutations(labels):
            B=(p,q,r,p,s,t)
            if B!=rolecanonical(B):continue
            words.add(B)
            mixed=[st for st in stars(B) if min(st)<6<=max(st)]
            if set(c for st in mixed for c in st)==set(range(12)):
                survivors[k].add(B)
assert len(words)==1890
orbits={canon(B) for group in survivors.values() for B in group}
REPS=[(0,1,3,5,1,6),(0,1,5,3,1,6),(0,2,6,5,3,6),(0,2,6,3,5,6),
      (0,1,3,0,2,4),(0,1,3,0,4,2),(0,1,3,5,1,2),(0,1,5,0,4,2)]
assert len(orbits)==8 and orbits=={canon(B) for B in REPS}
closedcounts=[];rings=det=0
for B in REPS:
    ss=[st for st in stars(B) if min(st)<6<=max(st)]
    closed=[]
    for bits in it.product([False,True],repeat=len(ss)):
        S=tuple(st for st,yes in zip(ss,bits) if yes)
        if set(c for st in S for c in st)!=set(range(12)):continue
        if not closes(S,B):continue
        closed.append(S)
        if torus(B,S) is not None:rings+=1
        else:
            assert deterministic(S,B)
            det+=1
    closedcounts.append(len(closed))
assert closedcounts==[0,1,1,1,0,1,1,7]
# Pure-B escape: actual side slots p,q,r,p,s,t. Self-pair repeated
# slots in each face and pair every other slot across the two faces.
parent=list(range(12))
def find(x):
    while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
    return x
pairs=[((f,0),(f,3)) for f in (0,1)]+[((0,i),(1,i)) for i in (1,2,4,5)]
for (f,j),(g,k) in pairs:
    for a,b in [((j-1)%6,k),(j,(k-1)%6)]:parent[find(6*f+a)]=find(6*g+b)
groups=defaultdict(list)
for f in (0,1):
    for c in range(6):groups[find(6*f+c)].append(c)
assert len(groups)==4
assert sorted(tuple(sorted(cs)) for cs in groups.values())==[(0,1,2),(0,1,2),(3,4,5),(3,4,5)]
assert 4-6+2==0
print(json.dumps(dict(status='PASS separation three',words=len(words),survivors={k:len(v) for k,v in survivors.items()},orbits=len(orbits),closedcounts=closedcounts,direct_tori=rings,deterministic=det,pureB_torus=True),sort_keys=True))
