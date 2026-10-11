#!/usr/bin/env python3
"""Exact use of Rao Table2 for the three surviving pentagrid angle words.

Angles m_i*pi/5 sit at vertex i; side i joins vertices i,i+1. All ten
rotation/reflection relabelings are included with their actual side maps.
The classification completeness is an external primary theorem, not replayed.
Positive metric feasibility is an exact ordered-field polyhedron computation.
"""
import json
from sage.all import AA, QQ, QuadraticField, Polyhedron

K=QuadraticField(5,'r',embedding=AA(5).sqrt())
r=K.gen()
phi=(1+r)/2
WORDS={'U':(1,3,4,4,3),'V':(2,2,4,3,4),'W':(3,3,3,3,3)}

def eq(row,target=10):
    return tuple(row),target

def L(*rows):
    return tuple(tuple(row) for row in rows)
FAMILIES={
1:([eq((1,1,1,0,0))],L()),
2:([eq((1,1,0,1,0))],L((0,0,1,0,-1))),
3:([eq((0,0,0,0,3)),eq((0,0,0,1,2)),eq((0,1,0,0,2))],L((0,0,1,-1,1),(1,-1,0,0,0))),
4:([eq((1,1,0,1,0)),eq((0,0,0,0,2),5)],L((0,0,0,1,-1),(0,1,-1,0,0))),
5:([eq((0,0,0,0,3)),eq((1,1,0,1,0))],L((0,0,0,1,-1),(0,1,-1,0,0))),
6:([eq((0,0,0,1,2)),eq((1,0,1,1,0))],L((0,0,1,-1,0),(0,0,0,1,-1),(1,-1,0,0,0))),
7:([eq((0,0,0,1,2)),eq((1,0,2,0,0))],L((1,0,-1,0,0),(0,0,1,-1,0),(0,0,0,1,-1))),
8:([eq((0,0,0,1,2)),eq((0,2,1,0,0))],L((1,-1,0,0,0),(0,1,-1,0,0),(0,0,1,-1,0))),
9:([eq((0,0,0,1,2)),eq((2,0,1,0,0))],L((1,-1,0,0,0),(0,1,-1,0,0),(0,0,1,-1,0))),
10:([eq((0,0,2,1,0)),eq((0,1,1,0,1)),eq((1,2,0,0,0))],L((1,0,1,-1,0),(0,0,0,1,-1))),
11:([eq((0,0,1,2,0)),eq((0,1,0,1,1)),eq((1,2,0,0,0))],L((1,-1,0,0,0),(0,1,-1,0,-2))),
12:([eq((0,0,1,2,0)),eq((0,1,0,1,1)),eq((1,2,0,0,0))],L((1,-1,1,0,0),(0,1,0,0,-2))),
13:([eq((0,1,0,2,0)),eq((1,1,0,1,0)),eq((0,0,0,0,2),5)],L((1,-2,0,0,0),(0,1,-1,0,0))),
14:([eq((0,0,1,2,0)),eq((0,1,0,1,1)),eq((1,2,0,0,0))],L((1,-1,0,0,0),(0,1,-2,0,0),(0,0,1,0,-1))),
15:([eq((0,0,1,2,0)),eq((0,2,0,0,1)),eq((2,0,0,1,0)),eq((0,0,0,0,2),5)],L((0,1,0,-1,0),(0,0,0,1,-1),(0,-2,1,0,0))),
}
C=(K(1),phi/2,(phi-1)/2,-(phi-1)/2,-phi/2,K(-1),-phi/2,-(phi-1)/2,(phi-1)/2,phi/2)
S=(K(0),K(1),phi,phi,K(1),K(0),K(-1),-phi,-phi,K(-1))

def closure(word):
    directions=[0]
    for m in word[1:]:
        directions.append((directions[-1]+5-m)%10)
    assert (directions[-1]+5-word[0])%10 == 0
    return tuple(C[d] for d in directions),tuple(S[d] for d in directions)

def encode(x):
    coeff=list(K(x))
    coeff.extend([QQ(0)]*(2-len(coeff)))
    return list(map(str,coeff))

def main():
    records=[]
    for name,word in WORDS.items():
        cx,sy=closure(word)
        for typ,(angle_eqs,length_eqs) in FAMILIES.items():
            for sign in (1,-1):
                for offset in range(5):
                    angle_map=tuple((offset+sign*i)%5 for i in range(5))
                    new=tuple(word[i] for i in angle_map)
                    if not all(sum(a*b for a,b in zip(row,new))==target
                               for row,target in angle_eqs):
                        continue
                    side_map=tuple((offset+i)%5 if sign==1 else (offset-i-1)%5
                                   for i in range(5))
                    transformed=[]
                    for row in length_eqs:
                        coefficients=[0]*5
                        for coefficient,side in zip(row,side_map):
                            coefficients[side]+=coefficient
                        transformed.append(coefficients)
                    equations=[[-1,1,1,1,1,1,0],[0,*cx,0],[0,*sy,0]]
                    equations.extend([[0,*row,0] for row in transformed])
                    inequalities=[]
                    for i in range(5):
                        row=[0]*7
                        row[i+1]=1
                        row[6]=-1
                        inequalities.append(row)
                    inequalities.append([0,0,0,0,0,0,1])
                    poly=Polyhedron(eqns=equations,ieqs=inequalities,base_ring=K,backend='field')
                    vertices=poly.vertices_list()
                    best=max(vertices,key=lambda v:v[5]) if vertices else None
                    positive=bool(best is not None and best[5]>0)
                    records.append({'word':name,'type':typ,'sign':sign,'offset':offset,
                                    'angle_word':new,'side_map':side_map,
                                    'length_equations':transformed,
                                    'positive_closed_metric':positive,
                                    'max_minimum_side':None if best is None else encode(best[5]),
                                    'maximizing_normalized_lengths':None if best is None else [encode(z) for z in best[:5]]})
    print(json.dumps({'primary_source':'Rao arXiv1708.00274v1 Table2 types1..15',
                     'domain':{'angle_words':WORDS,'type_count':15,'dihedral_maps_per_type':10,
                               'raw_angle_tests':450},'compatible_angle_cases':records,
                     'positive_case_count':sum(row['positive_closed_metric'] for row in records)},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
