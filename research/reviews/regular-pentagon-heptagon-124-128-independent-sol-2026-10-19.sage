# Independent metric gate checker: no producer imports or carrier search.
from itertools import permutations, combinations_with_replacement
import json
from pathlib import Path
A=AA
assert [s for s in combinations_with_replacement([108,124,128,144],3) if sum(s)==360]==[(108,108,144),(108,124,128)]
words=sorted({min(w,w[::-1]) for w in set(permutations([124]*3+[128]*3))})
assert len(words)==10
out=[]
for w in words:
    angles=[144]+list(w)
    # Trig evaluated in exact algebraic field, independently of cyclotomic direction code.
    theta=0; dirs=[]
    for i in range(7):
        if i: theta+=180-angles[i]
        dirs.append(vector(A,[A(cos(pi*theta/180)),A(sin(pi*theta/180))]))
    odd=[1,3,5]
    m=matrix(A,[[dirs[j][i] for j in odd] for i in range(2)])
    rhs=-sum((dirs[j] for j in [0,2,4,6]),vector(A,[0,0]))
    types=[sorted([angles[j],angles[j+1]]) for j in odd]
    if [124,124] in types:
        row=[0]*3; row[types.index([124,124])]=1; row[types.index([128,128])]=-1
        m=m.stack(matrix(A,[row])); rhs=vector(A,list(rhs)+[0])
    if m.rank()!=m.augment(rhs).rank():
        out.append((''.join('A' if x==124 else 'B' for x in w),False)); continue
    u=m.solve_right(rhs); basis=m.right_kernel().basis()
    if basis:
        d=basis[0]; lower=[]; upper=[]
        for x,y in zip(u,d):
            if y>0: lower.append(-x/y)
            elif y<0: upper.append(-x/y)
            else: assert x>0
        lo=max(lower) if lower else None; hi=min(upper) if upper else None
        assert lo is None or hi is None or lo<hi
        t=(lo+hi)/2 if lo is not None and hi is not None else lo+1 if lo is not None else hi-1
        u+=t*d
    feasible=all(x>0 for x in u)
    name=''.join('A' if x==124 else 'B' for x in w)
    out.append((name,feasible))
    if not feasible: continue
    lengths=[A(1)]*7
    for j,x in zip(odd,u): lengths[j]=x
    vertices=[vector(A,[0,0])]
    for l,d in zip(lengths,dirs): vertices.append(vertices[-1]+l*d)
    assert vertices[-1]==vertices[0]
    for i in range(7):
        e=vertices[i+1]-vertices[i]
        for j in range(7):
            if j not in [i,(i+1)%7]: assert matrix([e,vertices[j]-vertices[i]]).det()>0
    if name=='AABBAB':
        assert u[0]==u[1]
        print('Independent isolated AABBAB witness:',[x.n(35) for x in u])
assert sum(ok for _,ok in out)==8
producer=json.loads(Path('research/searches/regular-pentagon-heptagon-124-128-gate-sol-2026-10-19.json').read_text())
assert [ok for _,ok in out]==[x['positive'] for x in producer['results']]
print(out)
