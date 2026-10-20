# Exact finite metric/native corner gate; SageMath. No plane extension claim.
from itertools import combinations
import json
K=CyclotomicField(180); z=K.gen()
R=AA
words=[]
for inds in combinations(range(6),3):
    w=tuple(124 if i in inds else 128 for i in range(6))
    if w<=w[::-1]: words.append((144,)+w)
assert len(words)==10
def carrier_search(qangles,qlengths):
    # Oriented surface gluing; tile boundary reversal includes all reflection choices.
    # Rotational symmetry normalizes the sole PP edge to edge0 on each pentagon.
    from itertools import product
    visited=0
    for signs in product([False,True],repeat=3):
        polys=[]; lens=[]
        for angles,lengths,rev in [([108]*5,[R(1)]*5,False),([108]*5,[R(1)]*5,signs[0]),(qangles,qlengths,signs[1]),(qangles,qlengths,signs[2])]:
            if rev:
                angles=[angles[0]]+list(angles[:0:-1]); lengths=list(lengths[::-1])
            polys.append(list(angles));lens.append(list(lengths))
        offs=[0,5,10,17]; n=24
        angle=sum(polys,[]); length=sum(lens,[])
        tile=[t for t,p in enumerate(polys) for _ in p]
        nxt=[offs[t]+(i+1)%len(p) for t,p in enumerate(polys) for i in range(len(p))]
        def merge_state(parent,a,b):
            def root(x):
                while parent[x]!=x:x=parent[x]
                return x
            x,y=root(a),root(b)
            if x!=y:parent[y]=x
            roots={}
            for j in range(n): roots.setdefault(root(j),[]).append(j)
            return all(len(v)<=3 and sum(angle[j] for j in v)<=360 for v in roots.values())
        def recurse(rem,parent,pairs):
            nonlocal visited
            visited+=1
            if not rem:
                groups={}
                for i in range(n):
                    j=i
                    while parent[j]!=j:j=parent[j]
                    groups.setdefault(j,[]).append(i)
                if len(groups)==8 and all(len(v)==3 and sum(angle[j] for j in v)==360 for v in groups.values()):return pairs
                return None
            a=min(rem)
            for b in sorted(rem-{a}):
                if tile[a]<2 and tile[b]<2:continue
                if (tile[a]<2)!=(tile[b]<2):
                    q=b if tile[a]<2 else a
                    if (q-offs[tile[q]])%2:continue
                else:
                    if (a-offs[tile[a]])%2==0 or (b-offs[tile[b]])%2==0:continue
                if length[a]!=length[b]:continue
                par=parent[:]
                if not merge_state(par,a,nxt[b]):continue
                if not merge_state(par,nxt[a],b):continue
                ans=recurse(rem-{a,b},par,pairs+[(a,b)])
                if ans is not None:return ans
            return None
        for pp in [2,3,5]:
            par=list(range(n))
            if not merge_state(par,0,nxt[pp]) or not merge_state(par,nxt[0],pp):continue
            ans=recurse(set(range(n))-{0,pp},par,[(0,pp)])
            if ans is not None:return {'status':'flat oriented torus found','reflections':list(signs),'pairs':ans,'nodes':visited}
    return {'status':'no 2P+2Q carrier for this metric','nodes':visited}

results=[]
for angles in words:
    turns=[0]
    for a in angles[1:]: turns.append(turns[-1]+180-a)
    dirs=[z**(t//2) for t in turns]
    vectors=[vector(R,[QQbar(d).real(),QQbar(d).imag()]) for d in dirs]
    odd=[1,3,5]; even=[0,2,4,6]
    M=matrix(R,2,3,lambda i,j:vectors[odd[j]][i])
    b=-sum((vectors[i] for i in even),vector(R,[0,0]))
    types=[tuple(sorted((angles[i],angles[(i+1)%7]))) for i in odd]
    aa=[i for i,t in enumerate(types) if t==(124,124)]
    bb=[i for i,t in enumerate(types) if t==(128,128)]
    assert len(aa)==len(bb) and len(aa)<=1
    if aa:
        M=M.stack(matrix(R,1,3,lambda i,j: int(j==aa[0])-int(j==bb[0])))
        b=vector(R,list(b)+[0])
    if M.rank()!=M.augment(b).rank():
        results.append({"angles":list(angles),"positive":False,"reason":"inconsistent closure and AA=BB"}); continue
    sol=M.solve_right(b); ker=M.right_kernel().basis()
    witness=None; lo=None; hi=None
    if not ker:
        if all(s>0 for s in sol): witness=sol
    else:
        assert len(ker)==1
        d=ker[0]; lo=None; hi=None; possible=True
        for s,v in zip(sol,d):
            if v==0:
                if s<=0: possible=False
            elif v>0: lo=max(lo,-s/v) if lo is not None else -s/v
            else: hi=min(hi,-s/v) if hi is not None else -s/v
        if possible and (lo is None or hi is None or lo<hi):
            t=(lo+hi)/2 if lo is not None and hi is not None else (lo+1 if lo is not None else hi-1 if hi is not None else R(0))
            witness=sol+t*d
    entry={'angles':list(angles),'native_QQ_types':types,'positive':witness is not None,'particular_approx':[str(v.n(20)) for v in sol]}
    if witness is not None:
        lengths=[R(1)]*7
        for i,s in zip(odd,witness): lengths[i]=s
        assert sum((s*v for s,v in zip(lengths,vectors)),vector(R,[0,0]))==0
        assert all(s>0 for s in lengths)
        # Every positive-length convex-direction closed polygon is strictly convex.
        points=[vector(R,[0,0])]
        for s,v in zip(lengths,vectors):points.append(points[-1]+s*v)
        for i in range(7):
            edge=points[i+1]-points[i]
            for j in range(7):
                if j not in [i,(i+1)%7]:
                    delta=points[j]-points[i]
                    assert edge[0]*delta[1]-edge[1]*delta[0]>0
        entry['lengths_approx']=[str(s.n(30)) for s in lengths]
        entry['lengths_exact_definition']='unique/one-parameter exact closure solution as reconstructed by this script'
        entry['carrier']=carrier_search(angles,lengths)
    results.append(entry)
report=json.dumps({'scope':'ten dihedral words; forced alternating Q-Q/P-Q boundary; equal AA/BB seam lengths; exact AA closure and strict positivity','results':results},indent=2,default=str)
from pathlib import Path
Path('research/searches/regular-pentagon-heptagon-124-128-gate-sol-2026-10-19.json').write_text(report+'\n')
print(report)
