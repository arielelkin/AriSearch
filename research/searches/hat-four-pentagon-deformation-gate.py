#!/usr/bin/env python3
"""Specific two-parameter deformation of the fixed hat's four-pentagon cut.

Normalize source Tile(a,b) to a=1. Preserve the source outline directions;
the only interior cut vertex is V=(u, y_of_outline_vertex7), so outline
vertex8 is a subdivision on one pentagon side. Tests the three pairwise
congruences among fixed faces P6,P48,P192, necessary for <=2 total classes.
No generic decoration enumeration or source forcing assumption.
"""
import importlib.util,itertools,json,sys
from pathlib import Path
from sage.all import QuadraticField,PolynomialRing,AA,QQbar

K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen()
R=PolynomialRing(K,['b','u'],order='lex');b,u=R.gens()
embedding=K.hom([QQbar(3).sqrt()])
spec=importlib.util.spec_from_file_location('hat',Path('research/searches/source-decoration-hat-patch.py'))
hat=importlib.util.module_from_spec(spec);spec.loader.exec_module(hat)
old=[(K(p[0].a)+K(p[0].b)*r,K(p[1].a)+K(p[1].b)*r) for p in hat.hat_outline]
outline=[(R(0),R(0))]
for i in range(13):
    d=tuple(old[(i+1)%13][j]-old[i][j] for j in (0,1))
    norm=sum(x*x for x in d)
    assert norm in (1,3,4)
    scale=b/r if norm==3 else 1
    outline.append(tuple(outline[-1][j]+scale*d[j] for j in (0,1)))
assert outline[-1]==outline[0];outline.pop()
V=(u,outline[7][1])
tiles={'P6':[outline[i] for i in (0,1,2,3,4)],
       'P9':[outline[0],outline[4],V,outline[11],outline[12]],
       'P48':[outline[i] for i in (4,5,6,7)]+[V],
       'P192':[V]+[outline[i] for i in (8,9,10,11)]}
def norm_delta(P,Q):return sum((P[j]-Q[j])**2 for j in (0,1))
def evaluate(p,values):return AA(sum(embedding(c)*values[0]**m[0]*values[1]**m[1] for m,c in R(p).dict().items()))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(a[j]-b[j] for j in (0,1))
def convex(P):
    return all(P[i]!=P[i-1] and cross(sub(P[i],P[i-1]),sub(P[(i+1)%5],P[i]))>0 for i in range(5)) and all(cross(sub(P[(i+1)%5],P[i]),sub(v,P[i]))>=0 for i in range(5) for v in P)
rows=[];points=[]
for left,right in itertools.combinations(('P6','P48','P192'),2):
    P,Q=tiles[left],tiles[right]
    for direction in (1,-1):
        for shift in range(5):
            equations=[norm_delta(P[i],P[j])-norm_delta(Q[(shift+direction*i)%5],Q[(shift+direction*j)%5]) for i,j in itertools.combinations(range(5),2)]
            ideal=R.ideal(equations);dimension=int(ideal.dimension())
            row={'pair':[left,right],'direction':direction,'shift':shift,'dimension':dimension,
                 'groebner_basis':[str(g) for g in ideal.groebner_basis()],'real_points':[]}
            assert dimension<=0,(left,right,direction,shift,dimension)
            if dimension==0:
                for sol in ideal.variety(QQbar):
                    values=[sol[b],sol[u]]
                    if any(x.imag()!=0 for x in values):continue
                    numerical={name:[tuple(evaluate(p,values) for p in v) for v in polygon] for name,polygon in tiles.items()}
                    source=[tuple(evaluate(p,values) for p in v) for v in outline]
                    admissible=values[0]>0 and AA(values[1])<source[8][0] and all(convex(P) for P in numerical.values())
                    rec={'b':str(AA(values[0])),'u':str(AA(values[1])),
                         'minpolys':[str(x.minpoly()) for x in values],
                         'all_four_strictly_convex':bool(admissible),
                         'original_hat_similarity_ratio':bool(values[0]==QQbar(3).sqrt())}
                    row['real_points'].append(rec)
                    if admissible:points.append(rec)
            rows.append(row)
    print(left,right,'checked',flush=True)
out={'scope':'Fixed cut O-X, X-V,Y-V,M-V on Tile(1,b), V_y=outline_vertex7_y; all four final pentagons strictly convex; all30 pair correspondences among P6,P48,P192; polygon membership/source assembly needs separate verification.',
     'field':'Q(r),r^2=3,r>0','tiles':{name:[[str(x),str(y)] for x,y in P] for name,P in tiles.items()},
     'rows':rows,'admissible_pair_collapse_points':points}
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
print('admissible pair collapse points',points,flush=True)
