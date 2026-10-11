#!/usr/bin/env python3
"""Fresh V/V partner audit: independent native walks and separating axes.
No author code is imported. Formal edge cancellation yields the macro boundary.
"""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import json
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing

ROOT=Path(__file__).resolve().parents[2]
K=CyclotomicField(10);z=K.gen();phi=z+1/z
R=PolynomialRing(K,('x','k','y','f'));x,k,y,f=R.gens()

def walk(lengths,directions):
    p=[R(0)]
    for length,direction in zip(lengths,directions):p.append(p[-1]+length*z**direction)
    assert p[-1]==0
    return p[:-1]

def decode(row):
    return sum(variable*K(list(map(QQ,coeff))) for variable,coeff in zip((x,k,y,f),row))

def main():
    certificate=json.loads((ROOT/'research/certificates/pentagrid-v-v-general-double-y.json').read_text())
    data=certificate['formal_four_parameter_family']
    r=phi*(x+f)-y;e=f+phi*(x-y);l=phi*(x+k)-f;m=phi*(f-x)-k
    A=walk([x,r,y,e,f],[4,7,0,1,3]);A=[p-A[2] for p in A]
    B=walk([k,f,l,m,x],[5,8,1,2,4]);B=[p+A[0]+k for p in B]
    H=A[0]+B[0];motifs=[A,[H-p for p in A],B,[H-p for p in B]]
    assert motifs==[[decode(row) for row in polygon] for polygon in data['formal_motif_coefficients_x_k_y_f']]
    # Derive actual unmatched boundary without the producer's seam table.
    edges=Counter((p[i],p[(i+1)%5]) for p in motifs for i in range(5))
    canceled=0
    for a,b in list(edges):
        count=min(edges[a,b],edges[b,a]);edges[a,b]-=count;edges[b,a]-=count;canceled+=count
    assert canceled==5
    remaining=[edge for edge,count in edges.items() for _ in range(count)]
    assert len(remaining)==10
    successor=dict(remaining);assert len(successor)==10 and set(successor)==set(successor.values())
    chain=[R(0)]
    while successor[chain[-1]]!=0:
        nxt=successor[chain[-1]];assert nxt not in chain;chain.append(nxt)
    assert len(chain)==10
    def cj(p):return R({tuple(v):q.conjugate() for v,q in R(p).dict().items()})
    def cr(a,b):return (cj(a)*b-a*cj(b))/(z-z.conjugate())
    macro=[chain[i] for i in range(10) if cr(chain[i]-chain[i-1],chain[(i+1)%10]-chain[i])!=0]
    assert len(macro)==6 and macro[0]==0
    assert macro==list(map(decode,data['formal_macro_coefficients_x_k_y_f']))
    assert all(macro[(i+3)%6]==H-macro[i] for i in range(6))
    u,v=macro[2],macro[4]
    assert [u,v]==list(map(decode,data['formal_period_coefficients_x_k_y_f']))
    assert cr(u,v)==y*(e+l)+phi*y*(m+r)+(e+l)*(m+r)
    assert sum(cr(macro[i],macro[(i+1)%6]) for i in range(6))/2==cr(u,v)
    assert r-f==x/phi+(x+f/phi-y)
    # Independently evaluate and check every possible translated fixture overlap.
    substitutions={x:QQ(1),k:QQ(1),y:QQ(1)/2,f:QQ(2)}
    ev=lambda p:QQbar(R(p).subs(substitutions))
    polygons=[list(map(ev,p)) for p in motifs];pu,pv=ev(u),ev(v)
    cross=lambda a,b:AA((a.conjugate()*b).imag())
    determinant=cross(pu,pv);assert determinant>0
    def separated(P,Q):
        return any(all(cross(P[(i+1)%5]-P[i],q-P[i])<=0 for q in Q) for i in range(5))
    boxes=[]
    for P in polygons:
        for i in range(5):assert all(cross(P[(i+1)%5]-P[i],P[j]-P[i])>0 for j in range(5) if j not in (i,(i+1)%5))
        coordinates=[(cross(q,pv)/determinant,cross(pu,q)/determinant) for q in P]
        boxes.append([(min(q[d] for q in coordinates),max(q[d] for q in coordinates)) for d in (0,1)])
    cases=[]
    for i,j in product(range(4),repeat=2):
        domains=[range(int((boxes[i][d][0]-boxes[j][d][1]).ceil()),int((boxes[i][d][1]-boxes[j][d][0]).floor())+1) for d in (0,1)]
        for n,t in product(*domains):
            if i==j and n==t==0:continue
            Q=[q+n*pu+t*pv for q in polygons[j]]
            assert separated(polygons[i],Q) or separated(Q,polygons[i]),(i,j,n,t)
            cases.append([i,j,n,t])
    assert cases==certificate['asymmetric_fixture']['complete_lattice_clipping_comparisons']
    assert len(cases)==56
    print('PASS independent native V walks,5 canceled seams,10-edge boundary,6-gon macro,formal periods,and56 complete separating-axis comparisons')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
