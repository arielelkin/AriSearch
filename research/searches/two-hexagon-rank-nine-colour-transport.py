#!/usr/bin/env python3
"""Exact tiny colour projection of the 36-star rank-nine family.

No solver and no native-ring enumeration. Colour exclusions are necessary
conditions for the trivalent edge-to-edge SFT; positive colour tori retain
the full side equality closure they require.
"""
import itertools
import json
import math
import sys

D = [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
WORDS = {'C':(0,0,0,1,1,1),'I':(0,0,1,0,1,1),'ALT':(0,1,0,1,0,1)}
PLACEMENTS = [(r,s) for s in (1,-1) for r in range(6)]

def placed(word,r,s):
    return tuple(word[(r+s*k)%6] for k in range(6))

def orbit(word):
    return sorted({placed(word,r,s) for r,s in PLACEMENTS})

def rings(a,b):
    aw = orbit(WORDS[a]); bw = orbit(WORDS[b]); states=[]
    for w in bw:
        choices = [[j for j,u in enumerate(aw)
                    if u[(k+2)%6]==w[k] and u[(k+3)%6]==w[(k-1)%6]]
                   for k in range(6)]
        for path in itertools.product(*choices):
            states.append({'B':list(w),'A_ring':list(path)})
    return aw,states

def relations(states):
    return [[(i,j) for i,a in enumerate(states) for j,b in enumerate(states)
             if a['A_ring'][k]==b['A_ring'][(k+4)%6]
             and a['A_ring'][(k+1)%6]==b['A_ring'][(k+3)%6]]
            for k in range(6)]

def prune(states,rel):
    out=[{} for _ in range(6)]
    for k,edges in enumerate(rel):
        for a,b in edges:out[k].setdefault(a,set()).add(b)
    alive=set(range(len(states))); trace=[]
    while alive:
        bad=[]
        for i in sorted(alive):
            for k in range(6):
                js=out[k].get(i,set())&alive
                ls=out[(k+1)%6].get(i,set())&alive
                if not any(out[(k+2)%6].get(j,set())&ls for j in js):
                    bad.append([i,k]);break
        if not bad:break
        trace.append(bad);alive-={i for i,k in bad}
    return sorted(alive),trace

def side(r,s,k):
    return (r+k if s==1 else r-k-1)%6

def check_torus(n,labels,a,b,length_classes=None):
    # HNF (n,1,1): reduce (x,y) to (x-y mod n,0).
    def at(x,y):return labels[(x-y)%n]
    corners=[]; equalities=[]
    parent=list(range(12))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    def union(i,j):parent[find(j)]=find(i)
    for x,sym in enumerate(labels):
        t=sym//12;r,s=PLACEMENTS[sym%12]
        for k in (0,1):
            entries=[]
            for dx,dy,slot in [(0,0,k),(*D[k],(k+2)%6),(*D[(k+1)%6],(k+4)%6)]:
                z=at(x+dx,dy);tz=z//12;rz,sz=PLACEMENTS[z%12]
                native=(rz+sz*slot)%6
                entries.append((tz,native,WORDS[a if tz==0 else b][native]))
            assert sorted(t for t,c,col in entries)==[0,0,1],entries
            assert len({col for t,c,col in entries})==1,entries
            corners.append([6*t+c for t,c,col in entries])
        for k in range(6):
            dx,dy=D[(k+1)%6];z=at(x+dx,dy)
            tz=z//12;rz,sz=PLACEMENTS[z%12]
            i=6*t+side(r,s,k);j=6*tz+side(rz,sz,(k+3)%6)
            union(i,j);equalities.append([i,j])
            if length_classes is not None:assert length_classes[i]==length_classes[j],(x,k,i,j)
    classes={};closure=[]
    for i in range(12):
        f=find(i)
        if f not in classes:classes[f]=len(classes)
        closure.append(classes[f])
    return {'hnf':[n,1,1],'labels':labels,'vertex_stars':corners,
            'side_equalities':equalities,'required_side_closure':closure}

def stripe(a,b,f):
    n=math.lcm(3,len(f));labels=[];colour_words=[]
    for h in range(n):
        prev=f[(h-1)%len(f)];cur=f[h%len(f)];nxt=f[(h+1)%len(f)]
        w=(cur,1-prev,prev,1-cur,nxt,1-nxt)
        t=1 if h%3==0 else 0
        native=WORDS[b if t else a]
        candidates=[i for i,(r,s) in enumerate(PLACEMENTS) if placed(native,r,s)==w]
        assert candidates,(a,b,h,w)
        labels.append(12*t+candidates[0]);colour_words.append(list(w))
    answer=check_torus(n,labels,a,b)
    answer.update({'A_bracelet':a,'B_bracelet':b,'f':f,'colour_words':colour_words})
    return answer

def main(path):
    rows=[]
    # These are all six pairs with A=C or ALT. The three A=I pairs
    # have explicit positive stripe witnesses instead of huge ring searches.
    for a in ('C','ALT'):
        for b in WORDS:
            aw,states=rings(a,b);rel=relations(states);alive,trace=prune(states,rel)
            row={'A_bracelet':a,'B_bracelet':b,'A_patterns':aw,'states':states,
                 'relations':rel,'triangle_deletion_rounds':trace,'survivors':alive}
            rows.append(row)
            print(a,b,'rings',len(states),'core',len(alive),flush=True)
    witnesses=[stripe(a,b,f) for a,b,f in [
        ('C','C',[0,1]),('I','C',[0,1,1]),('I','I',[0,0,1,1]),
        ('I','ALT',[0,0,1,1,1,0]),('ALT','ALT',[0])]]
    metric=[]
    for bclass,labels in [(0,[12,0,6]),(1,[12,6,0])]:
        lengths=[0,1,0,1,0,1]+[bclass]*6
        q=check_torus(3,labels,'ALT','ALT',lengths)
        q.update({'B_length_class':bclass,'side_length_classes':lengths})
        metric.append(q)
    result={'scope':'trivalent edge-to-edge 36 AAB same-colour corner stars; no metric sufficiency from colour alone',
            'native_bracelets':WORDS,'distinct_colour_patterns':{a:len(orbit(w)) for a,w in WORDS.items()},
            'small_ring_censuses':rows,'stripe_witnesses':witnesses,'alternating_metric_witnesses':metric}
    with open(path,'w') as f:json.dump(result,f,indent=2)

if __name__=='__main__':main(sys.argv[1])
