#!/usr/bin/env python3
"""Independent radical-coordinate check of the full positive b,c family."""
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar, matrix, vector

ROOT=Path(__file__).resolve().parents[2]
phi=(1+AA(5).sqrt())/2
z=QQbar.zeta(10)
assert z.real()==phi/2 and z.imag()>0
assert z**4-z**3+z**2-z+1==0
sine=AA(z.imag())

def point(q):
    q=QQbar(q)
    return vector(AA,(AA(q.real()),AA(q.imag())))

def decode(row):
    assert len(row)==4
    return point(sum(QQ(value)*z**i for i,value in enumerate(row)))

def real_decode(row):
    p=decode(row);assert p[1]==0
    return p[0]

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def area(p):
    return sum(cross(p[i],p[(i+1)%5]) for i in range(5))/2

def vertices(directions,lengths):
    result=[point(0)]
    for direction,length in zip(directions,lengths):
        result.append(result[-1]+length*direction)
    assert result[-1]==point(0)
    return result[:-1]

def main():
    cert=json.loads((ROOT/'research/certificates/pentagrid-golden-metric-area-compatible.json').read_text())
    data={
        'U':((0,4,6,7,8),(phi**2,phi**2,1,0,1),(phi,phi,0,1,0)),
        'V':((0,3,6,7,9),(1,2*phi,1,phi,phi),(0,phi**2,0,phi,phi)),
    }
    areas={};support_count=0
    for name,(powers,coeff_b,coeff_c) in data.items():
        directions=[point(z**power) for power in powers]
        assert all(b>=0 and c>=0 and b+c>0 for b,c in zip(coeff_b,coeff_c))
        vb=vertices(directions,coeff_b);vc=vertices(directions,coeff_c)
        saved=cert[name]
        assert [decode(row) for row in saved['vertex_b_coefficients']]==vb
        assert [decode(row) for row in saved['vertex_c_coefficients']]==vc
        rows=saved['supporting_side_linear_coefficients']
        indexed={(row['side'],row['vertex']):row for row in rows}
        expected={(i,j) for i in range(5) for j in range(5) if j not in (i,(i+1)%5)}
        assert len(rows)==15 and set(indexed)==expected
        for i,j in sorted(expected):
            b=cross(directions[i],vb[j]-vb[i])/sine
            c=cross(directions[i],vc[j]-vc[i])/sine
            assert b>=0 and c>=0 and b+c>0
            row=indexed[i,j]
            assert real_decode(row['b_coefficient'])==b
            assert real_decode(row['c_coefficient'])==c
            support_count+=1
        ab=area(vb)/sine;ac=area(vc)/sine
        abc=area([vb[j]+vc[j] for j in range(5)])/sine-ab-ac
        areas[name]=[ab,abc,ac]
        assert [real_decode(row) for row in saved['normalized_area_b_squared_bc_c_squared']]==areas[name]
        # Supports are symbolic positive coefficients, hence valid for ALL b,c>0.
        # Independently check both exact examples, including an extension beyond K.
        for b,c in ((AA(1),AA(1)),(AA(1),AA(2).sqrt())):
            p=[b*vb[j]+c*vc[j] for j in range(5)]
            assert area(p)>0
            for i in range(5):
                assert all(cross(p[(i+1)%5]-p[i],p[j]-p[i])>0
                           for j in range(5) if j not in (i,(i+1)%5))
    assert areas['U']==[phi**3,2*phi**2,phi**2/2]
    assert areas['V']==[phi*a for a in areas['U']]
    assert cert['area_V_over_area_U']=='phi'
    M=matrix(QQ,[[1,1],[1,2]])
    assert vector(AA,[1,phi])*M==phi**2*vector(AA,[1,phi])
    assert cert['inflation_area_count_matrices']=={
        str(k):[[int(value) for value in row] for row in M**k] for k in (1,2,3)}
    # The V monohedral gates L2=L4 or L3=L0 require b=phi*(b+c).
    assert 1-phi<0 and -phi<0
    print(json.dumps({'verdict':'valid positive metric and area family',
                      'symbolic_support_pairs':support_count,
                      'vertex_bases':4,'area_coefficient_identities':3,
                      'count_matrix_powers':3,'global_existence':'unresolved'},indent=2))

if __name__=='__main__':
    main()
