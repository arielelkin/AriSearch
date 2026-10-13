"""Independent 640-case boundary reconstruction and integer polynomial determinant.
No Sage, producer import, numerical arithmetic, or elimination determinant.
"""
from itertools import combinations, permutations, product
from pathlib import Path
import json
from math import isqrt
# Independently check six arithmetic count cases and exact pruning signs.
for d in range(6):
    b=6-d;disc=d*d+4*b
    assert b>0 and isqrt(disc)**2!=disc
    p=lambda v:v*v-d*v-b
    assert p(0)<0
    if d in (4,5):assert p(4)<0  # μ>4, beyond all row sums<=2√μ.
    if d==0:assert p(2)<0       # μ>2; every corner-small row sum is2.
    if d==1:
        assert p(1)<0<p(3)    # 1<μ<3 and μ²=μ+5.
        # Then(μ−1)²−μ=6−2μ>0, yielding1+√μ<μ.
    if d==3:assert p(3)<0<p(4) # Remaining count is not discarded by μ>4.

ZERO=(0,0,0,0);ONE=(1,0,0,0);LAM=(0,1,0,0);MU=(0,0,1,0)
def add(a,b):return tuple(a[i]+b[i] for i in range(4))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
    raw=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):raw[i+j]+=x*y
    # λ^4=3λ^2+3, reducing from highest exponent downward.
    for k in range(6,3,-1):
        raw[k-2]+=3*raw[k];raw[k-4]+=3*raw[k];raw[k]=0
    return tuple(raw[:4])
perms=[(p,(-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))) for p in permutations(range(5))]
def det5(M):
    out=ZERO
    for p,sgn in perms:
        term=ONE
        for i in range(5):term=mul(term,M[i][p[i]])
        out=add(out,term if sgn==1 else neg(term))
    return out
cert_path=Path('research/certificates/resumed_intrinsic_wheel_d3.json')
cert=json.loads(cert_path.read_text())
assert cert['minimal_polynomial']=='t^4-3*t^2-3'
assert cert['area_multiplier']=='(3+sqrt(21))/2'
assert cert['case_count']==640 and cert['zero_determinant_count']==0
assert len(cert['records'])==640
supplied={}
for row in cert['records']:
    assert type(row['central_large']) is bool
    big=row['large_corners'];flips=row['reflections'];coeff=row['determinant_coefficients']
    assert len(big)==(2 if row['central_large'] else 3) and big==sorted(set(big))
    assert all(type(i) is int and 0<=i<5 for i in big)
    assert len(flips)==5 and all(type(i) is int and i in (0,1) for i in flips)
    assert len(coeff)==4 and all(type(i) is int for i in coeff)
    key=(row['central_large'],tuple(big),tuple(flips))
    assert key not in supplied; supplied[key]=tuple(coeff)
expected={}
for central_large in [False,True]:
    for big in combinations(range(5),2 if central_large else 3):
        for flips in product([0,1],repeat=5):
            C=[[ZERO for _ in range(5)] for _ in range(5)]
            for corner in range(5):
                prev=(corner-1)%5;weight=LAM if corner in big else ONE
                # Independently assemble one two-ray corner block at a time.
                entries=[(prev,corner),(corner,prev)] if flips[corner] else [(prev,prev),(corner,corner)]
                for row,col in entries:C[row][col]=add(C[row][col],weight)
            assert all(C[i][j]==C[j][i] for i in range(5) for j in range(5))
            M=[[add(MU if i==j else ZERO,neg(C[i][j])) for j in range(5)] for i in range(5)]
            determinant=det5(M)
            assert determinant!=ZERO
            expected[(central_large,big,flips)]=determinant
assert expected==supplied
assert len(expected)==640
assert sum(not key[0] for key in expected)==320
assert sum(key[0] for key in expected)==320
print('PASS: all640 certificate determinants independently reconstructed by integer polynomial Leibniz expansion;320/320 complete domains')
