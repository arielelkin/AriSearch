"""Independent 7680-case boundary reconstruction and integer polynomial determinant.
No Sage, producer import, numerical arithmetic, or elimination determinant.
"""
from itertools import combinations, permutations, product
from pathlib import Path
import json
ZERO=(0,0,0,0);ONE=(1,0,0,0);LAM=(0,1,0,0);MU=(0,0,1,0)
def add(a,b):return tuple(a[i]+b[i] for i in range(4))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
    raw=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):raw[i+j]+=x*y
    # λ^4=2λ^2+4, reducing from highest exponent downward.
    for k in range(6,3,-1):
        raw[k-2]+=2*raw[k];raw[k-4]+=4*raw[k];raw[k]=0
    return tuple(raw[:4])
perms=[(p,(-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))) for p in permutations(range(5))]
def det5(M):
    out=ZERO
    for p,sgn in perms:
        term=ONE
        for i in range(5):term=mul(term,M[i][p[i]])
        out=add(out,term if sgn==1 else neg(term))
    return out
cert=json.loads(Path('research/certificates/resumed_intrinsic_repeated_u.json').read_text())
assert cert['minimal_polynomial']=='t^4-2*t^2-4'
assert cert['positive_root_interval']==[1,2]
assert cert['after_side_word']==[1,3,4,4,3]
assert cert['vertex_before_side_word']==[3,1,3,4,4]
assert cert['case_count']==7680 and len(cert['records'])==7680
assert cert['singular_count']==cert['positive_count']==0
assert cert['singular_cases']==cert['positive_cases']==[]
from fractions import Fraction
choices=[(0,2),(1,),(0,2),(3,4),(3,4)]
supplied={}
for row in cert['records']:
    native=row['native_indices'];big=row['large_corners'];flips=row['reflections'];coeff=row['determinant_coefficients']
    assert len(native)==5 and all(type(j) is int and j in choices[i] for i,j in enumerate(native))
    assert type(row['central_large']) is bool
    assert len(big)==(1 if row['central_large'] else 2) and big==sorted(set(big))
    assert all(type(i) is int and 0<=i<5 for i in big)
    assert len(flips)==5 and all(type(i) is int and i in (0,1) for i in flips)
    assert len(coeff)==4 and all(type(c) is str for c in coeff)
    parsed=[Fraction(c) for c in coeff]
    assert all(c.denominator==1 for c in parsed)
    key=(tuple(native),row['central_large'],tuple(big),tuple(flips))
    assert key not in supplied;supplied[key]=tuple(int(c) for c in parsed)
expected={}
for native in product(*choices):
    for central_large in [False,True]:
        for big in combinations(range(5),1 if central_large else 2):
            for flips in product([0,1],repeat=5):
                C=[[ZERO for _ in range(5)] for _ in range(5)]
                for corner,j in enumerate(native):
                    incoming=(j-1)%5;outgoing=j
                    if flips[corner]:incoming,outgoing=outgoing,incoming
                    weight=LAM if corner in big else ONE
                    row=(corner-1)%5
                    C[row][incoming]=add(C[row][incoming],weight)
                    C[corner][outgoing]=add(C[corner][outgoing],weight)
                M=[[add(MU if i==j else ZERO,neg(C[i][j])) for j in range(5)] for i in range(5)]
                determinant=det5(M)
                assert determinant!=ZERO
                key=(native,central_large,big,flips)
                expected[key]=determinant
assert expected==supplied and len(expected)==7680
assert len({key[0] for key in expected})==16
assert sum(not key[1] for key in expected)==5120
assert sum(key[1] for key in expected)==2560
print('PASS: all7680 repeated-angle wheel coefficient vectors independently verified;16 native maps and5120/2560 central-size cases')
