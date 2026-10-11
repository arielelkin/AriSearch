#!/usr/bin/env python3
"""Exact retained-model and closure audit; does not reenumerate the domain."""
import contextlib,io,json,runpy
from itertools import combinations,permutations
from fractions import Fraction as F
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    source=runpy.run_path('research/searches/new-angle-three-pentagon-counterexample-verify.py')
E=source['E'];r3=source['r3'];a=source['a'];d=source['d']
X=(90,150,90,105,105);Y=(90,105,90,105,150)
unitX=((E(1),E(0)),(r3/2,E(F(1,2))),(E(-F(1,2)),r3/2),(-a,-d),(E(0),E(-1)))
unitY=source['unit']
record=json.loads(Path('research/certificates/new-angle-three-pentagon-mixed-word-angle-models.json').read_text())
assert record['attempts']==8*3*40320 and record['flat_models']==len(record['models'])==8

def determinant(mat):
    n=len(mat);answer=E(0)
    for perm in permutations(range(n)):
        sign=-1 if sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))%2 else 1
        term=E(sign)
        for i,j in enumerate(perm):term*=mat[i][j]
        answer+=term
    return answer

def normalize(part):
    ids={}
    return tuple(ids.setdefault(v,len(ids)) for v in part)
parts=set()
for model in record['models']:
    refs=model['reflected'];words=[X,X,Y,Y]
    fw=[tuple(w[-j%5] if r else w[j] for j in range(5)) for w,r in zip(words,refs)]
    vertex_parent=list(range(20));side_parent=list(range(10))
    def root(p,x):
        while p[x]!=x:p[x]=p[p[x]];x=p[x]
        return x
    def union(p,x,y):p[root(p,x)]=root(p,y)
    used=[]
    for (f,j),(g,k) in model['pairs']:
        used.extend(((f,j),(g,k)))
        union(vertex_parent,5*f+j,5*g+(k+1)%5)
        union(vertex_parent,5*f+(j+1)%5,5*g+k)
        nf=(0 if f<2 else 5)+((-j-1)%5 if refs[f] else j)
        ng=(0 if g<2 else 5)+((-k-1)%5 if refs[g] else k)
        union(side_parent,nf,ng)
    assert len(set(used))==len(used)==20
    cls={}
    for f in range(4):
        for j in range(5):cls.setdefault(root(vertex_parent,5*f+j),[]).append((f,j))
    assert len(cls)==6 and all(sum(fw[f][j] for f,j in vs)==360 for vs in cls.values())
    part=tuple(model['native_side_partition'])
    assert normalize(part)==normalize(tuple(root(side_parent,j) for j in range(10)))
    parts.add(part)
assert len(parts)==4
assert len({normalize(p) for p in parts})==3
assert record['raw_partition_labelings']==4 and record['distinct_equality_relations']==3
certificates=[]
for part in sorted(parts):
    n=len(set(part));M=[[E(0) for j in range(n)] for i in range(4)]
    for i in range(10):
        f,j=divmod(i,5);u,v=(unitX if f==0 else unitY)[j]
        M[2*f][part[i]]+=u;M[2*f+1][part[i]]+=v
    if n==3:
        witnesses=[]
        for rows in combinations(range(4),3):
            det=determinant([[M[i][j] for j in range(3)] for i in rows])
            if det!=0:witnesses.append({'rows':list(rows),'nonzero_minor':det.encode()})
        assert witnesses
        certificates.append({'partition':list(part),'rank':3,'conclusion':'all lengths zero',
                             'rank_witness':witnesses[0]})
    else:
        assert n==5 and part[3]==part[8]==4
        assert determinant([row[:4] for row in M])==0
        witnesses=[]
        for columns in combinations(range(5),4):
            det=determinant([[M[i][j] for j in columns] for i in range(4)])
            if det!=0:witnesses.append({'columns':list(columns),'nonzero_minor':det.encode()})
        assert witnesses
        # Rank4 gives a one-dimensional kernel. Its cofactor vector has
        # coordinate4 equal to det(columns0..3)=0, so every kernel hasx4=0.
        certificates.append({'partition':list(part),'rank':4,
                             'conclusion':'native side3 of both prototiles forced zero',
                             'zero_minor_columns':[0,1,2,3],'rank_witness':witnesses[0]})
print(json.dumps({'status':'PASS','retained_angle_models_checked':8,
                  'raw_partition_labelings_checked':4,'distinct_equality_relations_checked':3,'exact_rank_certificates':certificates,
                  'enumeration_completeness_dependency':'the declared generator domain/proof; this checker verifies retained models'},indent=2,sort_keys=True))
