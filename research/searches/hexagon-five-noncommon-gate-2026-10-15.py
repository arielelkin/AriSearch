#!/usr/bin/env python3
"""Cheap exact unequal-five-palette endpoint/component gate; integer only.
Domain: each repeat separation 2/3, all shared subsets of A's five colors,
canonical private colors, all 120 native B assignments per palette.
Pure stars are removed under the separately proved monohedral-escape case.
No torus search or geometric realization inference.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from pathlib import Path
import argparse, json
TRIPLES=tuple(combinations(range(12),3))

def native_word(colors,sep):
    a,b,c,d,e=colors
    return (a,b,a,c,d,e) if sep==2 else (a,b,c,a,d,e)

def gate(W,seps):
    arms=[frozenset((W[f][i],W[f][(i+1)%6])) for f in range(2) for i in range(6)]
    def slot(c,r):
        f,i=divmod(c,6)
        return 6*f+(i if W[f][i]==r else (i+1)%6)
    def far(c,r):
        j=slot(c,r);f,i=divmod(j,6)
        return 6*f+(i-1)%6 if c==j else j
    full=[t for t in TRIPLES if len({arms[c] for c in t})==3 and len(set().union(*(arms[c] for c in t)))==3]
    mixed=[t for t in full if t[0]<6<=t[-1]]
    demands={}
    seams={}
    for t in mixed:
        ds=[];es=[]
        for a,b in combinations(t,2):
            common=arms[a]&arms[b]
            assert len(common)==1
            r=next(iter(common))
            ds.append(tuple(sorted((far(a,r),far(b,r)))))
            es.append(tuple(sorted((slot(a,r),slot(b,r)))))
        demands[t]=ds;seams[t]=es
    S=mixed;rounds=[]
    while True:
        pairs={p for t in S for p in combinations(t,2)}
        T=[t for t in S if all(p in pairs for p in demands[t])]
        if T==S:break
        rounds.append({'removed':[t for t in S if t not in T]});S=T
    cover=sorted({c for t in S for c in t})
    parent=list(range(12))
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    edges=sorted({e for t in S for e in seams[t]})
    for a,b in edges:parent[find(a)]=find(b)
    comps=sorted(tuple(i for i in range(12) if find(i)==r) for r in sorted({find(i) for i in range(12)}))
    joins=[find(0)==find(seps[0]),find(6)==find(6+seps[1])]
    status='no_cover' if len(cover)<12 else ('hard' if all(joins) else 'six_color_escape')
    out={'A':W[0],'B':W[1],'full_atlas':full,'mixed_atlas':mixed,'rounds':rounds,'fixed_atlas':S,'covered':cover,'seams':edges,'components':comps,'repeated_joined':joins,'status':status}
    return out,demands

def supports(row,demands):
    S=row['fixed_atlas'];out=[]
    assert len(S)<=24, ('support gate needs a separate plan',len(S))
    for mask in range(1<<len(S)):
        T=[t for i,t in enumerate(S) if mask>>i&1]
        if {c for t in T for c in t}!=set(range(12)):continue
        pairs={p for t in T for p in combinations(t,2)}
        if all(p in pairs for t in T for p in demands[t]):out.append(T)
    return out

def canonical_with_witness(A,B,sep):
    choices=[]
    for shift in range(6):
        for direction in (-1,1):
            mapping={};valid=True
            for i in range(6):
                old=A[(shift+direction*i)%6]
                if old in mapping and mapping[old]!=A[i]:valid=False;break
                mapping[old]=A[i]
            if not valid or len(set(mapping.values()))!=5:continue
            for bs in range(6):
                for bd in (-1,1):
                    vals=[B[(bs+bd*i)%6] for i in range(6)]
                    if vals[0]!=vals[sep]:continue
                    m=dict(mapping);nextcolor=5
                    for x in vals:
                        if x not in m:m[x]=nextcolor;nextcolor+=1
                    canonical=tuple(m[x] for x in vals)
                    witness={'A_shift':shift,'A_direction':direction,
                             'B_shift':bs,'B_direction':bd,'color_map':m}
                    choices.append((canonical,witness))
    assert choices
    return min(choices,key=lambda pair:pair[0])

def build():
    summary=defaultdict(Counter);hard=[];seen=Counter()
    for sa in (2,3):
        A=native_word((0,1,2,3,4),sa)
        for sb in (2,3):
            for k in range(5):
                for shared in combinations(range(5),k):
                    palette=shared+tuple(range(5,10-k))
                    assert len(palette)==5
                    for assignment in permutations(palette):
                        B=native_word(assignment,sb)
                        row,demands=gate((A,B),(sa,sb))
                        key=f'A{sa}_B{sb}_shared{k}'
                        summary[key][row['status']]+=1;seen[(sa,sb,k)]+=1
                        if row['status']=='hard':
                            row['shared_colors']=shared
                            row['supports']=supports(row,demands)
                            canonical,witness=canonical_with_witness(A,B,sb)
                            row['canonical_B']=canonical;row['class_equivalence']=witness
                            hard.append(row)
    for sa in (2,3):
        for sb in (2,3):
            assert sum(seen[sa,sb,k] for k in range(5))==3720
    classes=[]
    for key in sorted({(tuple(r['A']),tuple(r['canonical_B'])) for r in hard}):
        rows=[r for r in hard if (tuple(r['A']),tuple(r['canonical_B']))==key]
        representative=next(r for r in rows if tuple(r['B'])==key[1])
        classes.append({'A':key[0],'B':key[1],'raw_word_count':len(rows),
                        'fixed_atlas':representative['fixed_atlas'],
                        'supports':representative['supports']})
    assert len(hard)==20 and len(classes)==6
    assert sum(len(r['supports']) for r in hard)==64
    assert sum(len(r['supports']) for r in classes)==22
    return {'schema':'FIVE_NONCOMMON_ENDPOINT_COMPONENT_GATE_V1','hard_classes':classes,'domain':{'A_separations':[2,3],'B_separations':[2,3],'shared_counts':list(range(5)),'private_color_normalization':'5,6,...,9-k','raw_words_per_separation_pair':3720,'total_raw_words':14880,'pure_stars':'deleted conditionally on established monohedral escape'},'summary':{k:dict(v) for k,v in sorted(summary.items())},'hard_records':hard,'scope':'Exact necessary native gate only; supports need not have geometric realizations.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--summary',action='store_true');args=ap.parse_args()
    data=build()
    if args.output:Path(args.output).write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    display={'domain':data['domain'],'summary':data['summary'],'hard_count':len(data['hard_records'])} if args.summary else data
    print(json.dumps(display,sort_keys=True,indent=2))
