# Independent retained-certificate checker; fixed immediate neighborhoods only.
import json
from itertools import combinations, product
from functools import lru_cache
D=json.load(open('research/searches/aa-bb-strand-atlas-sol-2026-10-19.json'))
K=CyclotomicField(180); z=K.gen(); ii=z**45
cc=lambda x:K(x).conjugate()
re=lambda x:(x+cc(x))/2
im=lambda x:(x-cc(x))/(2*ii)
@lru_cache(None)
def sg(x):
    if not x:return 0
    n=80
    while True:
        C=ComplexIntervalField(n); w=C(0,2*RealIntervalField(n).pi()/180).exp()
        a=x.polynomial()(w).real()
        if a.lower()>0:return 1
        if a.upper()<0:return -1
        n*=2
xy=lambda p:K(p[0])+ii*K(p[1])
cross=lambda a,b:im(cc(a)*b)
def check(poly):
    assert all(sg(cross(poly[(j+1)%len(poly)]-a,v-a))>=0 for j,a in enumerate(poly) for v in poly)
def disjoint(p,q):
    # Independently project onto every edge normal; compare projection intervals.
    for h in (p,q):
        for j,a in enumerate(h):
            d=h[(j+1)%len(h)]-a
            pp=[cross(d,v) for v in p]; qq=[cross(d,v) for v in q]
            from functools import cmp_to_key
            key=cmp_to_key(lambda x,y:sg(x-y))
            if sg(max(pp,key=key)-min(qq,key=key))<=0 or sg(max(qq,key=key)-min(pp,key=key))<=0:return True
    return False
def audit(tiles):
    distinct=[]
    for t in tiles:
        if not any(set(t)==set(u) for u in distinct):distinct.append(t)
    assert all(disjoint(p,q) for p,q in combinations(distinct,2))
    return len(distinct)
for rec in D['results']:
    word=rec['word']; angles=[144]+[124 if a=='A' else 128 for a in word]
    Q=list(map(xy,rec['Q_vertices'])); check(Q)
    ds=[Q[(e+1)%7]-Q[e] for e in range(7)]
    assert ds[0]==1
    # Exact native turns and lengths, independent of certificate transform records.
    for e in range(1,7):
        ratio=ds[e]/ds[e-1]/z**((180-angles[e])//2)
        assert im(ratio)==0 and sg(re(ratio))>0
    assert all(ds[e]*cc(ds[e])==1 for e in [0,2,4,6])
    types={e:word[e-1]+word[e] for e in [1,3,5]}
    aa=next(e for e in types if types[e]=='AA'); bb=next(e for e in types if types[e]=='BB')
    assert ds[aa]*cc(ds[aa])==ds[bb]*cc(ds[bb])
    P=[]
    for e in [0,2,4,6]:
        # Walk an exterior regular pentagon clockwise from the root edge start.
        p=[Q[e]]
        for j in range(4):p.append(p[-1]+ds[e]*z**(-36*j))
        P.append(p)
    assert len(set(P[0]) & set(P[3]))==2
    audit([Q]+P)
    expected=[]; transformed={}
    for e,f,r in product([1,3,5],[1,3,5],[False,True]):
        j,k=(f,(f+1)%7) if r else ((f+1)%7,f)
        if angles[e]+angles[j]!=252 or angles[(e+1)%7]+angles[k]!=252:continue
        if ds[e]*cc(ds[e])!=ds[f]*cc(ds[f]):continue
        expected.append((e,f,r))
    assert len(expected)==5
    for s in rec['seams']:
        e,f,r=s['root_edge'],s['other_edge'],s['isometry']['reflection']
        assert (e,f,r) in expected; expected.remove((e,f,r))
        j,k=(f,(f+1)%7) if r else ((f+1)%7,f)
        cv=cc if r else lambda x:x
        c=ds[e]/(cv(Q[k])-cv(Q[j])); t=Q[e]-c*cv(Q[j])
        iso=s['isometry']; assert c==K(iso['complex_c']) and t==K(iso['complex_t']) and c*cc(c)==1
        mat=matrix(K,[[re(c),im(c) if r else -im(c)],[im(c),-re(c) if r else re(c)]])
        assert mat==matrix(K,[[K(x) for x in row] for row in iso['linear']])
        assert t==xy(iso['translation'])
        other=[[c*cv(v)+t for v in p] for p in [Q]+P]; transformed[s['id']]=other
        assert audit([Q]+P+other)==8
        assert sum(any(set(p)==set(q) for q in other[1:]) for p in P)==2
        assert s['compatible'] and not s['full_forced_P_neighborhood_overlap_pairs']
    assert not expected
    assert len(rec['strand_at_Q'])==4
    for row in rec['strand_at_Q']:
        assert audit([Q]+P+transformed[row['AA_seam']]+transformed[row['BB_seam']])==11
        assert row['compatible'] and not row['overlap_pairs']
    print(word, 'PASS: five seams, four two-seam combinations',flush=True)
print('PASS: finite exact certificate only')
