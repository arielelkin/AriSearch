"""NEW separation-three mixed-corner gate; pure B stars have separate torus escape.
Finite domain: all support subsets of the mixed actual-corner stars in eight
specified cyclic representatives. No geometric realization claim.
"""
import runpy,json,argparse
from itertools import combinations,permutations
from pathlib import Path
D=runpy.run_path(str(Path(__file__).with_name('hexagon-six-five-ring-selection-2026-10-15.py')))
REPS=[(0,1,3,5,1,6),(0,1,5,3,1,6),(0,2,6,5,3,6),(0,2,6,3,5,6),
      (0,1,3,0,2,4),(0,1,3,0,4,2),(0,1,3,5,1,2),(0,1,5,0,4,2)]
def canonical(B):
    return min(tuple((sg*x+sh)%6 if x<6 else x for x in w[i:]+w[:i])
               for sg in (-1,1) for sh in range(6) for w in (B,B[::-1]) for i in range(6))

counts=[];orbits={}
for k in range(6):
    total=0;survivors=0
    for common in combinations(range(6),k):
        for p,q,r,s,t in permutations(common+tuple(range(6,11-k))):
            B=(p,q,r,p,s,t)
            if B!=min(B,B[3:]+B[:3],(p,t,s,p,r,q),(p,r,q,p,t,s)):continue
            total+=1
            ss=[s for s in D['atlas'](B) if min(s)<6<=max(s)]
            if {i for st in ss for i in st}==set(range(12)):
                survivors+=1
                C=canonical(B);orbits[C]=orbits.get(C,0)+1
    counts.append(dict(k=k,words=total,survivors=survivors))
assert [c['words'] for c in counts]==[30,180,450,600,450,180]
assert [c['survivors'] for c in counts]==[0,0,0,0,30,36]
assert set(orbits)==set(REPS)
assert [orbits[b] for b in REPS]==[12,12,3,3,12,12,6,6]
records=[]
for B in REPS:
    ss=[s for s in D['atlas'](B) if min(s)<6<=max(s)]
    rr=D['rings'](B);closed=[];uncovered=[]
    for mask in range(1<<len(ss)):
        selected=[s for j,s in enumerate(ss) if mask>>j&1]
        if {i for s in selected for i in s}!=set(range(12)):continue
        if not D['endpoint_closed'](selected,B):continue
        ring=next((r for r in rr if all(s in selected for s in r)),None)
        partition=all(sum(i in s for s in selected)==1 for i in range(12))
        closed.append(dict(support=selected,ring=ring,partition=partition))
        if ring is None and not partition:uncovered.append(selected)
    record=dict(B=B,stars=ss,ring_count=len(rr),endpoint_closed=closed,uncovered=uncovered)
    records.append(record)
    assert not uncovered
assert [len(r['endpoint_closed']) for r in records]==[0,1,1,1,0,1,1,7]
result=dict(domain='all 1890 normalized separation-three words, then all mixed star-support subsets of eight surviving representatives',
            counts=counts,orbits=[dict(B=B,count=orbits[B]) for B in REPS],records=records)
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
