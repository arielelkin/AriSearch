#!/usr/bin/env python3
"""Independent 12-case closure, positive support and physical-symmetry audit.
No author producer import. The retained certificate is compared to native walks.
"""
from pathlib import Path
import json
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing

K=CyclotomicField(10);z=K.gen();phi=z+1/z
R=PolynomialRing(K,('L',));L=R.gen()
def cj(p):return R({j:a.conjugate() for j,a in R(p).dict().items()})
def cross(a,b):return (cj(a)*b-a*cj(b))/(z-z.conjugate())
def positive_coefficient(a):
    value=QQbar(a);assert value.imag()==0
    return AA(value.real())
def closed_walk(d,i,j,length):
    angles=[3 if v in (0,d) else 4 for v in range(8)]
    exponents=[0]
    for v in range(1,8):exponents.append(exponents[-1]+5-angles[v])
    assert exponents[-1]+5-angles[0]==10
    vertices=[R(0)]
    for side,exponent in enumerate(exponents):
        vertices.append(vertices[-1]+(length if side in (i,j) else 1)*z**exponent)
    assert vertices.pop()==0
    return vertices,exponents

def main():
    root=Path(__file__).resolve().parents[2]
    cert=json.loads((root/'research/certificates/private-octagon-equal-private-unit-closure.json').read_text())
    rows={(row['alpha_gap'],*row['private_sides']):row for row in cert['cases']}
    domain={(d,i,j) for d in (2,3,4) for i in (7,0) for j in (d-1,d)}
    assert len(cert['cases'])==12 and set(rows)==domain
    admitted=set();counts={'free':0,'fixed_positive_nonunit':0,'nonreal':0,'inconsistent':0,'unit':0,'zero':0}
    for d,i,j in sorted(domain):
        # Derive the directions from the corner turns, rather than the source equation.
        angles=[3 if v in (0,d) else 4 for v in range(8)];exponents=[0]
        for v in range(1,8):exponents.append(exponents[-1]+5-angles[v])
        base=sum(z**q for q in exponents)
        coefficient=z**exponents[i]+z**exponents[j]
        row=rows[d,i,j]
        assert base==-(z**d+z**9)
        if coefficient==0:
            assert row['closure']==('all L' if base==0 else 'inconsistent')
            valid=base==0
            counts['free' if valid else 'inconsistent']+=1
            length=L if valid else None
        else:
            value=1-base/coefficient
            assert K(list(map(QQ,row['L_cyclotomic_coefficients'])))==value
            real=value==value.conjugate();assert row['real']==real
            valid=bool(real and positive_coefficient(value)>0 and value!=1)
            if not real:counts['nonreal']+=1
            elif value==0:counts['zero']+=1
            elif value==1:counts['unit']+=1
            else:
                assert valid;counts['fixed_positive_nonunit']+=1
            length=R(value)
        assert row['positive_nonunit_admissible']==valid
        if not valid:continue
        admitted.add((d,i,j));vertices,exponents=closed_walk(d,i,j,length)
        if d in (2,3):
            assert length==R(phi if d==2 else 3-phi)
            permutation=lambda v:(d-v)%8
            linear=-z**(d-1);offset=vertices[d]
            symmetry=lambda p:linear*cj(p)+offset
            assert linear*linear.conjugate()==1 and linear*cj(offset)+offset==0
        else:
            permutation=lambda v:(v+4)%8
            offset=vertices[4];symmetry=lambda p:offset-p
        assert all(symmetry(vertices[v])==vertices[permutation(v)] for v in range(8))
        # The symmetry exchanges the actual private edges, not only their labels.
        image={permutation(i),permutation((i+1)%8)}
        assert image=={j,(j+1)%8}
        for a in range(8):
            edge=vertices[(a+1)%8]-vertices[a]
            for b in range(8):
                if b in (a,(a+1)%8):continue
                height=R(cross(edge,vertices[b]-vertices[a]))
                assert height!=0
                if length==L:
                    coefficients=height.list()
                    assert all(positive_coefficient(c)>=0 for c in coefficients)
                    assert any(positive_coefficient(c)>0 for c in coefficients)
                else:
                    assert height.degree()<=0 and positive_coefficient(height[0])>0
        # Same physical neighbor from a cross-slot label: H_i S^{-1}(Q)=H_i(Q).
        midpoint=(vertices[i]+vertices[(i+1)%8])/2
        halfturn=lambda p:2*midpoint-p
        assert {halfturn(symmetry(p)) for p in vertices}=={halfturn(p) for p in vertices}
    assert admitted=={(2,0,1),(3,0,2),(4,7,3),(4,0,4)}
    assert admitted==set(map(tuple,cert['admitted_rows']))
    assert counts=={'free':2,'fixed_positive_nonunit':2,'nonreal':4,'inconsistent':1,'unit':2,'zero':1}
    # The two gap-four descriptions are congruent for every L, including its unit boundary.
    A,_=closed_walk(4,7,3,L);B,_=closed_walk(4,0,4,L)
    assert all(-z**8*cj(A[v])==B[(-v)%8] for v in range(8))
    print('PASS all 12 native closure cases, 4 admitted rows, actual symmetries, strict positive supporting sides, physical-mate invariance, and full free-L congruence')
    print('Gap-4 L=1 closes but has no length private from regular unit P; L=0 is nongenuine and discarded')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
