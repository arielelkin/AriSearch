"""Independent finite native-edge audit of private-A endpoint alternatives.
Scope: local necessary length incidence, not geometric extension or density.
"""
from itertools import product,combinations
from collections import Counter
A=tuple(range(6))
u,v,w=0,5,1
# A corner at the first endpoint of native side u is (v,u),
# at the second endpoint it is (u,w). The same private native side of
# a neighboring A can match with either endpoint correspondence.
endpoint_cases=[]
for swap in (False,True):
    neighbor=(w,v) if swap else (v,w)
    # Third corner joins the two non-u rays at each actual endpoint.
    needed=[tuple(sorted(pair)) for pair in zip((v,w),neighbor)]
    endpoint_cases.append(needed)
assert endpoint_cases==[[(5,5),(1,1)],[(1,5),(1,5)]]
count=0
# Compress every other B length to 6: only presence of v,w and their
# native corner incidences enter this lemma. This covers arbitrary repeats.
for B in product((v,w,6),repeat=6):
    corners={tuple(sorted((B[j],B[(j+1)%6]))) for j in range(6)}
    if any(all(pair in corners for pair in needed) for needed in endpoint_cases):
        assert v in B and w in B
        count+=1
alternating=[]
for common in combinations(range(6),3):
    S=set(common)
    if all((j-1)%6 in S and (j+1)%6 in S for j in range(6) if j not in S):alternating.append(common)
assert alternating==[(0,2,4),(1,3,5)]
# Positive multiplicities across all three shared labels. Since every A
# has one side of each and every B side is AB, mx NB=NA+O(R) for each x.
# Positive quadratic NB density makes mx equal. Sum mx=6 fixes each to 2.
solutions=[]
for multiplicities in product(range(1,5),repeat=3):
    if sum(multiplicities)==6 and len(set(multiplicities))==1:solutions.append(multiplicities)
assert solutions==[(2,2,2)]
assert sum(Counter(B)==Counter({0:2,1:2,2:2}) for B in product(range(3),repeat=6))==90
print('PASS: both private-AA endpoint maps; 729 compressed native B words; two alternating shared sets; unique multiplicities (2,2,2), 90 indexed B words')

# Further native-mode classification: all 90 B words with two copies of
# each shared length. A private pair xy allows endpoint swap exactly if
# xy is a B corner; endpoint preserve requires BOTH xx and yy corners.
def bracelet(B):
    candidates=[]
    from itertools import permutations
    for labels in permutations(range(3)):
        word=tuple(labels[x] for x in B)
        for oriented in [word,word[::-1]]:
            candidates.extend(oriented[j:]+oriented[:j] for j in range(6))
    return min(candidates)
classes=Counter();ambiguous=set()
for B in product(range(3),repeat=6):
    if Counter(B)!=Counter({0:2,1:2,2:2}):continue
    edges={tuple(sorted((B[j],B[(j+1)%6]))) for j in range(6)}
    modes={pair:([0] if pair in edges else [])+([1] if all((x,x) in edges for x in pair) else []) for pair in combinations(range(3),2)}
    if not all(modes.values()):continue
    key=bracelet(B);classes[key]+=1
    if any(len(options)>1 for options in modes.values()):ambiguous.add(key)
assert classes==Counter({(0,0,1,1,2,2):12,(0,0,1,2,1,2):36,(0,0,1,2,2,1):18,(0,1,0,2,1,2):18,(0,1,2,0,1,2):6})
assert ambiguous=={(0,0,1,1,2,2)}
print('PASS: 90-word native-mode gate has five bracelets; only adjacent-pair word001122 has endpoint ambiguity')

# Stronger exact corona rule: each B side r faces A's unique r slot;
# its endpoint private slots are the two different pairs incident to r.
corona=Counter()
for B in product(range(3),repeat=6):
    if Counter(B)!=Counter({0:2,1:2,2:2}):continue
    options=[]
    for j in range(6):
        r,s=B[j],B[(j+1)%6]
        options.append([tuple(sorted((r,s)))] if r!=s else [tuple(sorted((r,t))) for t in range(3) if t!=r])
    good=[]
    for state in product(*options):
        if all(state[(j-1)%6]!=state[j] for j in range(6)):good.append(state)
    if good:
        corona[bracelet(B)]+=1
        assert len(good)==1
assert corona==Counter({(0,0,1,2,2,1):18,(0,1,2,0,1,2):6})
print('PASS: all 90 words under exact corona rule leave only001221 and012012, each with unique native private-slot assignment')
