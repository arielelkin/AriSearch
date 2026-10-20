"""Exact 2P+2Q oriented native-edge pairing search; Python stdlib only."""
import itertools,json,sys
from pathlib import Path
starts=[0,5,10,17]; sizes=[5,5,7,7]
nxt={s+i:s+(i+1)%n for s,n in zip(starts,sizes) for i in range(n)}
triples=[(108,108,144),(108,124,128)]
nodes=0

def merge(state,a,b,angles):
    state=state.copy(); x,y=state[a],state[b]
    if x==y:return state
    state=[x if z==y else z for z in state]
    vals=sorted(angles[i] for i,z in enumerate(state) if z==x)
    if not any(all(vals.count(v)<=t.count(v) for v in set(vals)) for t in triples):return None
    return state

def add(state,a,b,angles):
    state=merge(state,a,nxt[b],angles)
    if state is None:return None
    return merge(state,nxt[a],b,angles)

def search(state,ps,qs,pairs,angles):
    global nodes
    nodes+=1
    if not qs:
        a,b=ps
        state=add(state,a,b,angles)
        if state is None:return
        comps=[[i for i in range(24) if state[i]==r] for r in sorted(set(state))]
        if len(comps)!=8 or any(len(c)!=3 for c in comps):return
        yield pairs+[(a,b)],comps
        return
    q=qs[0]
    for p in ps:
        st=add(state,p,q,angles)
        if st is not None:yield from search(st,[x for x in ps if x!=p],qs[1:],pairs+[(p,q)],angles)

def matchings(xs):
    if not xs:
        yield [];return
    a=xs[0]
    for j in range(1,len(xs)):
        for rest in matchings(xs[1:j]+xs[j+1:]):yield [(a,xs[j])]+rest

def main():
    cases=0; results=[]
    for inds in itertools.combinations(range(1,7),3):
        word=[144]+[124 if i in inds else 128 for i in range(1,7)]
        if word>word[:1]+word[:0:-1]:continue
        witness=None
        before=nodes
        for reflect,colors in itertools.product((False,True),((0,1,2),(0,0,1),(0,1,0),(0,1,1),(0,0,0))):
            words=[word,word[:1]+word[:0:-1] if reflect else word]
            angles=[108]*10+words[0]+words[1]
            qedges=[[s+i for i in (0,2,4,6)] for s in (10,17)]
            col={10+i:colors[(i-1)//2] for i in (1,3,5)}
            col.update({17+(6-i if reflect else i):colors[(i-1)//2] for i in (1,3,5)})
            for qq in matchings(sorted(col)):
                if any(col[a]!=col[b] for a,b in qq):continue
                found=try_qq(qq,angles,qedges)
                cases+=1
                if found:
                    pairs,comps=found
                    witness=dict(status='SAT',word=word,Q1_reflected=reflect,length_colors=colors,pairs=pairs,vertices=comps,angles=angles)
                    break
            if witness:break
        results.append(witness or dict(status='UNSAT',word=word))
        results[-1]['nodes']=nodes-before
    out=dict(results=results,cases=cases,nodes=nodes)
    Path('research/certificates/regular-pentagon-heptagon-fourface-carrier-sol-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

def try_qq(qq,angles,qedges):
            state=list(range(24))
            for a,b in qq:
                state=add(state,a,b,angles)
                if state is None:break
            if state is None:return None
            for pairs,comps in search(state,list(range(10)),sum(qedges,[]),qq,angles):
                face=lambda d:next(i for i,(s,n) in enumerate(zip(starts,sizes)) if s<=d<s+n)
                seen={0}
                while True:
                    new=seen|{face(b) for a,b in pairs if face(a) in seen}|{face(a) for a,b in pairs if face(b) in seen}
                    if new==seen:break
                    seen=new
                if len(seen)!=4:continue
                return pairs,comps
if __name__=='__main__':main()
