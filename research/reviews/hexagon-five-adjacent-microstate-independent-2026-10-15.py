#!/usr/bin/env python3
"""No-import adjacent-repeat native-state reconstruction; ordered directed sectors."""
from itertools import permutations,product
from collections import Counter,defaultdict
from pathlib import Path
import argparse,json
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'research/certificates/hexagon-five-adjacent-microstate-gate-2026-10-15.json'
A=(0,0,1,2,3,4)

def generate(W):
    sectors=[]
    for f,w in enumerate(W):
        for i in range(6):
            c=6*f+i
            slots=(6*f+i,6*f+(i+1)%6)
            far=(6*f+(i-1)%6,6*f+(i+1)%6)
            for left,right in ((0,1),(1,0)):
                sectors.append((c,slots[left],slots[right],far[left],far[right],w[slots[left]%6],w[slots[right]%6]))
    # Enumerate all ordered, independently reflected sectors, repetitions allowed.
    byleft=defaultdict(list)
    for s in sectors:byleft[s[5]].append(s)
    states=set()
    for x in sectors:
        for y in byleft[x[6]]:
            for z in byleft[y[6]]:
                if z[6]!=x[5]:continue
                rays=[]
                for l,r in ((x,y),(y,z),(z,x)):
                    rays.append((tuple(sorted((l[2],r[1]))),tuple(sorted((l[0],r[0]))),tuple(sorted((l[4],r[3])))))
                states.add((tuple(sorted((x[0],y[0],z[0]))),tuple(sorted(rays))))
    return states

def fixed(states):
    current=set(states)
    while True:
        endpoints=defaultdict(set)
        for star,seams in current:
            for slots,here,there in seams:endpoints[slots].add(here)
        nxt={s for s in current if all(there in endpoints[slots] for slots,here,there in s[1])}
        if nxt==current:return current
        current=nxt

def classify(states,bp):
    cover=sorted({c for t,ss in states for c in t})
    adj={i:set() for i in range(12)}
    for t,ss in states:
        for slots,here,there in ss:
            x,y=slots;adj[x].add(y);adj[y].add(x)
    components=[];unseen=set(range(12))
    while unseen:
        seen={min(unseen)};todo=list(seen)
        for x in todo:
            for y in adj[x]:
                if y not in seen:seen.add(y);todo.append(y)
        unseen-=seen;components.append(sorted(seen))
    joined=[any({x,y}<=set(c) for c in components) for x,y in ((0,1),(6,6+bp))]
    kind='no_cover' if len(cover)<12 else ('both_joined' if all(joined) else 'color_escape')
    return cover,components,joined,kind

def build():
    records=[];summary=[]
    for bp in (1,2,3):
        counts=Counter()
        for repeated in range(5):
            for p in permutations([c for c in range(5) if c!=repeated]):
                B=[repeated if i in (0,bp) else None for i in range(6)]
                it=iter(p);B=tuple(next(it) if v is None else v for v in B)
                initial=generate((A,B));last=fixed(initial)
                cover,comps,joined,kind=classify(last,bp);counts[kind]+=1
                records.append({'B_repeat_separation':bp,'B':B,'initial_states':sorted(initial),'fixed_states':sorted(last),'covered_corners':cover,'components':comps,'repeated_joined':joined,'kind':kind})
        summary.append({'B_repeat_separation':bp,'counts':dict(counts)})
    assert [s['counts'] for s in summary]==[{'no_cover':88,'color_escape':24,'both_joined':8},{'no_cover':96,'color_escape':24},{'no_cover':92,'color_escape':24,'both_joined':4}]
    return {'schema':'INDEPENDENT_ADJACENT_COMMON_FIVE_NATIVE_GATE_V1','A':A,'raw_word_count':360,'summary':summary,'records':records}

def canon(data):return json.loads(json.dumps(data))
def check_b2():
    from fractions import Fraction as F
    W=(A,(0,0,2,4,1,3));M=fixed(generate(W));stars=sorted({t for t,ss in M})
    assert len(stars)==14 and len(M)==16
    def rank(rows):
        a=[[F(x) for x in r] for r in rows];k=0
        for j in range(len(a[0])):
            pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
            if pivot is None:continue
            a[k],a[pivot]=a[pivot],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
            for i in range(len(a)):
                if i!=k:
                    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
            k+=1
        return k
    supports=[]
    for bits in product((False,True),repeat=len(stars)):
        S={t for t,b in zip(stars,bits) if b}
        if {c for t in S for c in t}!=set(range(12)):continue
        N=fixed({s for s in M if s[0] in S})
        if {t for t,ss in N}==S:supports.append((S,N))
    assert Counter(len(S) for S,N in supports)=={6:2,7:2,12:3,13:4,14:1}
    for S,N in supports:
        if len(S)>7:
            rows=[[int(i<6) for i in range(12)],[int(i>=6) for i in range(12)]]+[[t.count(i) for i in range(12)] for t in S]
            assert rank(rows)==12
            assert all(sum(F(2,3)*x for x in row)==rhs for row,rhs in zip(rows,[4,4]+[2]*len(S)))
        else:
            mixed={t for t in S if min(t)<6<=max(t)}
            assert len(mixed)==6
            majority=0 if all(sum(c<6 for c in t)==2 for t in mixed) else 1
            assert all(sum(c//6==majority for c in t)==2 for t in mixed)
            if len(S)==7:assert S-mixed=={(6*majority,)*3}
            # Small-six support: unique whole AB neighbor, not just one endpoint.
            L=fixed({state for state in M if state[0] in mixed})
            assert len(L)==6 and {t for t,ss in L}==mixed
            keys={(slots,here) for t,ss in L for slots,here,there in ss}
            for f,i in product(range(2),range(6)):
                g=1-f;options=[]
                for j,rev in product(range(6),(False,True)):
                    if W[f][i]!=W[g][j]:continue
                    x=(6*f+(i-1)%6,6*f+i);y=(6*g+(j-1)%6,6*g+j)
                    if rev:y=y[::-1]
                    slots=tuple(sorted((6*f+i,6*g+j)))
                    if all((slots,tuple(sorted((a,b)))) in keys for a,b in zip(x,y)):options.append((j,rev))
                assert len(options)==1
    # Derive closure coefficients from exact coordinates of six directions.
    directions=((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
    closure=[]
    for w in W:
        for axis in (0,1):closure.append([sum(directions[i][axis] for i,c in enumerate(w) if c==v) for v in range(5)])
    assert closure==[[3,-1,-2,-1,1],[1,1,0,-1,-1],[3,-1,-1,1,-2],[1,-1,1,-1,0]]
    assert rank(closure)==4 and all(sum(r)==0 for r in closure)
    return 'B2: 12 exact supports, eight all-120-angle contradictions, two pure-star parity contradictions, two deterministic AB-parity supports'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');args=p.parse_args()
    data=build();b2=check_b2()
    if args.output:Path(args.output).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert canon(data)==json.loads(CERT.read_text())
    print('PASS:',b2)
    print('PASS: all 360 ordered-sector native microstate gates; counts (88,24,8), (96,24,0), (92,24,4)')
