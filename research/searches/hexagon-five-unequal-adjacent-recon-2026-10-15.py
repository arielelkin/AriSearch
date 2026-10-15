#!/usr/bin/env python3
"""UNREVIEWED unequal-palette adjacent-repeat necessary gate, integer only.
All 11160 words. Ordered directed sectors permit every union color, repeated
native corner occurrences and independent reflected arm assignments. Stores
summary and residual classes only, no negative atlas archive or torus search.
"""
from itertools import permutations,product,combinations
from collections import Counter,defaultdict
from pathlib import Path
import argparse,json
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

def normalized(p,bp):
    w=list(p);w.insert(bp,p[0]);return tuple(w)

def canonical(B,bp,source_A=A):
    choices=[]
    for sh,dr in product(range(6),(1,-1)):
        mp={};valid=True
        for i in range(6):
            old=source_A[(sh+dr*i)%6]
            if old in mp and mp[old]!=A[i]:valid=False;break
            mp[old]=A[i]
        if not valid or len(set(mp.values()))!=5:continue
        for bs,bd in product(range(6),(1,-1)):
            raw=tuple(B[(bs+bd*i)%6] for i in range(6))
            if raw[0]!=raw[bp]:continue
            cm=dict(mp);fresh=5
            for x in raw:
                if x not in cm:cm[x]=fresh;fresh+=1
            target=tuple(cm[x] for x in raw)
            choices.append((target,{'A_shift':sh,'A_direction':dr,'B_shift':bs,'B_direction':bd,'color_map':cm}))
    assert choices
    return min(choices,key=lambda x:x[0])

def build():
    summary=defaultdict(Counter);hard=[];total=0
    for bp in (1,2,3):
        for k in range(5):
            for shared in combinations(range(5),k):
                palette=shared+tuple(range(5,10-k))
                for p in permutations(palette):
                    B=normalized(p,bp);initial=generate((A,B));last=fixed(initial)
                    cover,components,joined,kind=classify(last,bp);total+=1
                    summary[f'B{bp}_shared{k}'][kind]+=1
                    if kind=='both_joined':
                        representative,witness=canonical(B,bp)
                        hard.append({'B':B,'B_repeat_separation':bp,'shared_count':k,'representative':representative,'equivalence':witness,'initial_state_count':len(initial),'fixed_state_count':len(last),'fixed_star_count':len({t for t,ss in last})})
    assert total==11160
    classes=[]
    for bp,B in sorted({(r['B_repeat_separation'],r['representative']) for r in hard}):
        members=[r for r in hard if r['B_repeat_separation']==bp and r['representative']==B]
        initial=generate((A,B));last=fixed(initial)
        swap,swapmap=canonical(A,1,source_A=B)
        classes.append({'species_swap_representative':swap,'species_swap_equivalence':swapmap,'B_repeat_separation':bp,'B':B,'raw_word_count':len(members),'shared_count':members[0]['shared_count'],'fixed_states':sorted(last),'fixed_star_count':len({t for t,ss in last}),'raw_words':[r['B'] for r in members]})
    return {'schema':'UNEQUAL_PALETTE_ADJACENT_RECON_V1','status':'UNREVIEWED_AUTHOR_RECONNAISSANCE','A':A,'domain':{'raw_words':total,'B_separations':[1,2,3],'shared_counts':list(range(5)),'palettes_per_separation':31,'assignments_per_palette':120,'private_labels':'5 through 9-k'},'summary':{k:dict(v) for k,v in sorted(summary.items())},'residual_raw_count':len(hard),'residual_class_count':len(classes),'unordered_class_count':len({min(tuple(c['B']),tuple(c['species_swap_representative'])) for c in classes}),'classes':classes,'hard_records':hard,'scope':'Necessary source gate only, with monohedral opposite-repeat escape handled separately. No metric realization, periodic completeness or main-problem conclusion.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');p.add_argument('--summary',action='store_true');a=p.parse_args()
    d=build();encoded=json.dumps(d,sort_keys=True,indent=2)+'\n'
    if a.output:Path(a.output).write_text(encoded)
    if a.summary:
        print(json.dumps({k:d[k] for k in ('domain','summary','residual_raw_count','residual_class_count')},sort_keys=True,indent=2))
        for c in d['classes']:print('CLASS',c['B_repeat_separation'],c['B'],'raw',c['raw_word_count'],'stars',c['fixed_star_count'],'states',len(c['fixed_states']))
    else:print(encoded,end='')
