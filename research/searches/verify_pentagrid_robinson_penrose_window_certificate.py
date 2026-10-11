"""Small same-author certificate replay; imports no producer or polyhedron."""
from sage.all import QuadraticField, matrix
from itertools import product,combinations
from pathlib import Path
import json

F=QuadraticField(5,'rt5');phi=(1+F.gen())/2
C=[F(1),-phi/2,(phi-1)/2,(phi-1)/2,-phi/2]
S=[F(0),F(1),-phi,phi,F(-1)]
G=[(F(1),C[i],S[i]) for i in range(5)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(h):
    scale=next(abs(t) for t in h[1:] if t!=0)
    return tuple(t/scale for t in h)
facets=set()
for a,b in combinations(G,2):
    n=cross(a,b)
    for n in [n,tuple(-t for t in n)]:
        h0=-sum(min(F(0),dot(n,g)) for g in G)
        facets.add(norm((h0,)+n))
assert len(facets)==20
src=json.loads(Path('research/certificates/pentagrid-robinson-penrose-window.json').read_text())
reported=[tuple(F(t) for t in row) for row in src['window_facets']]
assert {norm(h) for h in reported}==facets
verts=[tuple(sum(t[j]*G[j][i] for j in range(5)) for i in range(3)) for t in product((0,1),repeat=5)]
assert all(h[0]+dot(h[1:],p)>=0 for h in reported for p in verts)
count=0
for group in ['fixtures','boundary_only']:
    for label,rec in src[group].items():
        for row in rec['results']:
            if group=='boundary_only':
                dirs=[0,4,6,7,8] if label=='U' else [0,3,6,7,9]
                k=0;levels=[k]
                for word,d in zip(row['side_words'],dirs):
                    for symbol in word:
                        k+=(-1)**d*{'u':1,'l':-2,'s':2}[symbol]
                        levels.append(k)
                assert k==0
                assert [min(levels),max(levels)]==row['layer_interval']
                assert max(levels)-min(levels)==row['layer_span']
            if row['layer_span']>3:
                assert row['layer_interval'][1]-row['layer_interval'][0]==row['layer_span']
                continue
            N=[]
            for p in row['lifted_vertices']:
                H=p['H_z_basis'];n=p['N_rho_basis']
                assert all(n[3*i%5]==(-1)**i*H[i] for i in range(5))
                N.append(n)
            assert min(sum(n) for n in N)==row['layer_interval'][0]
            assert max(sum(n) for n in N)==row['layer_interval'][1]
            cases=row['window_gate']['cases']
            assert [case['integer_intercept_sum'] for case in cases]==list(range(row['layer_interval'][1]-4,row['layer_interval'][0]))
            for case in cases:
                m=case['integer_intercept_sum'];allowed=set()
                for n in N:
                    k=sum(n);a=dot(n,C);b=dot(n,S)
                    for h0,hk,ha,hb in reported:allowed.add((h0+hk*(k-m)+ha*a+hb*b,-ha,-hb))
                cert=case['dual_obstruction']
                rows=[tuple(F(t) for t in r) for r in cert['selected_rows']]
                assert all(r in allowed for r in rows)
                weights=[F(t) for t in cert['positive_weights']]
                assert len(weights)==len(rows)<=3 and all(t>=0 for t in weights) and sum(weights)>0
                assert sum(w*r[1] for w,r in zip(weights,rows))==0
                assert sum(w*r[2] for w,r in zip(weights,rows))==0
                assert sum(w*r[0] for w,r in zip(weights,rows))==F(cert['constant_sum'])<=0
                count+=1
print('PASS:20 independently reconstructed zonotope facets;',count,'small exact strict-window rejection certificates; no polyhedron backend')
