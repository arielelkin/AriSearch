"""Exact conditional all-R zero-private (3,3,2) mask domain; no tiling assertion."""
from sage.all import QuadraticField, matrix
from itertools import product
K=QuadraticField(2,"r"); r=K.gen()
directions=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r))
def masks(word):
    result=set()
    for s in range(8):
        W=word[s:]+word[:s]
        if W[1] in (0,1) and W[2]==W[1] and W[4]==W[7]==1-W[1] and W[5]==W[6]==2:
            result.add(tuple(sorted((s,(s+3)%8))))
        if W[1] in (0,1) and W[3]==1-W[1] and W[5] in (0,1) and W[7]==1-W[5] and W[2]==W[6]==2:
            result.add(tuple(sorted((s,(s+4)%8))))
    return sorted(result)
domain=[]
for A,B in product(range(3),repeat=2):
    for a in (0,1): domain.append((3,(A,a,a,B,1-a,2,2,1-a)))
    for a,c in product((0,1),repeat=2): domain.append((4,(A,a,2,1-a,B,c,2,1-c)))
domain=[(m,W) for m,W in domain if sorted(W.count(i) for i in range(3))==[2,3,3]]
assert len(domain)==36
survivors=[]
for mask,W in domain:
    M=matrix(K,[[sum(directions[k][j] for k,L in enumerate(W) if L==i) for i in range(3)] for j in range(2)])
    if M.rank()==2:
        v=M.right_kernel().basis()[0]
        positive=all(x>0 for x in v) or all(x<0 for x in v)
        assert not positive or v[0]==v[1]==v[2]
        continue
    assert M.rank()==1
    row=next(row for row in M.rows() if row)
    nonzero=[i for i,x in enumerate(row) if x]
    if len(nonzero)==2:
        assert row[nonzero[0]]==-row[nonzero[1]]
        continue
    assert len(nonzero)==3 and mask==4
    assert masks(W)==[(0,4)]
    assert W[0]!=W[4]
    survivors.append((''.join('uvw'[i] for i in W),tuple(str(x) for x in row)))
expected={'uuwvwvwu','uvwuwuwv','vuwvwvwu','vvwuwuwv','wuwvuvwu','wvwuuuwv','wuwvvvwu','wvwuvuwv'}
assert {W for W,row in survivors}==expected
print('PASS: 36 rooted closure domains; 8 remaining distinct-metric words; unique QQ mask (0,4) in each')
for W,row in survivors:print(W,row)
