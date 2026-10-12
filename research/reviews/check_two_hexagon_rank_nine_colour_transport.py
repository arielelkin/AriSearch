#!/usr/bin/env python3
"""Independent tiny colour census, canonical triangles, and endpoint side maps.
No import of the producer, global SFT, Sage, or a solver. Output is optional.
"""
import argparse, hashlib, itertools, json
from fractions import Fraction
from pathlib import Path

D=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
WORDS={'C':(0,0,0,1,1,1),'I':(0,0,1,0,1,1),'ALT':(0,1,0,1,0,1)}
P=tuple((r,s) for s in (1,-1) for r in range(6))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def placed(word,p): return tuple(word[(p[0]+p[1]*k)%6] for k in range(6))
def orbit(word): return sorted({placed(word,p) for p in P})
def side(p,k):
    # Native side i has corner endpoints {i,i+1}; derive rather than
    # assuming that a reflected side has the reflected corner index.
    ends={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
    answer=[i for i in range(6) if {i,(i+1)%6}==ends]
    assert len(answer)==1
    return answer[0]

INC=[]
for k in range(6):
    target={(0,0),D[k],D[(k+1)%6]}; matches=[]
    for x,y,o in itertools.product(range(-2,3),range(-2,3),(0,1)):
        z=(x,y); cells=(z,add(z,D[o]),add(z,D[o+1]))
        if set(cells)==target: matches.append(dict(zip(cells,(o,o+2,o+4))))
    assert len(matches)==1
    INC.append(matches[0])
DELTA=tuple(add(D[k],D[(k+1)%6]) for k in range(6))

def census(a,b):
    aw=orbit(WORDS[a]); states=[]
    for bw in orbit(WORDS[b]):
        constraints=[]
        for k,inc in enumerate(INC):
            colour=bw[inc[(0,0)]]
            constraints.append({(i,j) for i,u in enumerate(aw) for j,v in enumerate(aw)
                                if u[inc[D[k]]]==v[inc[D[(k+1)%6]]]==colour})
        def grow(path):
            if len(path)==6:
                if (path[-1],path[0]) in constraints[-1]:
                    states.append({'B':list(bw),'A_ring':list(path)})
                return
            for i in range(len(aw)):
                if not path or (path[-1],i) in constraints[len(path)-1]:grow(path+(i,))
        grow(())
    relations=[]
    for k,delta in enumerate(DELTA):
        overlaps=[(i,j) for i,x in enumerate(D) for j,y in enumerate(D) if x==add(delta,y)]
        assert len(overlaps)==2
        relations.append({(i,j) for i,u in enumerate(states) for j,v in enumerate(states)
                          if all(u['A_ring'][p]==v['A_ring'][q] for p,q in overlaps)})
    alive=set(range(len(states))); rounds=[]
    while alive:
        bad=[]
        for i in sorted(alive):
            for k in range(6):
                jdir=(k+1)%6
                cross=DELTA.index(sub(DELTA[jdir],DELTA[k]))
                left={j for u,j in relations[k] if u==i and j in alive}
                right={j for u,j in relations[jdir] if u==i and j in alive}
                if not any((j,l) in relations[cross] for j in left for l in right):
                    bad.append([i,k]);break
        if not bad:break
        rounds.append(bad);alive-={i for i,k in bad}
    return aw,states,relations,sorted(alive),rounds

def verify_torus(row,a,b,metric=None):
    n,s,m=row['hnf'];assert s==m==1
    labels=row['labels'];assert len(labels)==n
    def at(z):return labels[(z[0]-z[1])%n]
    parent=list(range(12))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    stars=[];seams=[]
    for x in range(n):
        z=(x,0);t,p=divmod(at(z),12); p=P[p]
        for o in (0,1):
            cells=(z,add(z,D[o]),add(z,D[o+1])); entries=[];colours=[]
            for cell,k in zip(cells,(o,o+2,o+4)):
                species,pi=divmod(at(cell),12);native=(P[pi][0]+P[pi][1]*k)%6
                entries.append(6*species+native);colours.append(WORDS[a if species==0 else b][native])
            assert sorted(v//6 for v in entries)==[0,0,1] and len(set(colours))==1
            stars.append(entries)
        for k in range(6):
            u=add(z,D[(k+1)%6]);ts,pi=divmod(at(u),12)
            i=6*t+side(p,k);j=6*ts+side(P[pi],(k+3)%6)
            parent[find(j)]=find(i);seams.append([i,j])
            if metric is not None:assert metric[i]==metric[j]
    classes={};closure=[]
    for i in range(12):
        root=find(i)
        if root not in classes:classes[root]=len(classes)
        closure.append(classes[root])
    assert stars==row['vertex_stars'] and seams==row['side_equalities']
    assert closure==row['required_side_closure']
    return len(stars),len(seams)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/two-hexagon-rank-nine-colour-transport.json')
    cert=json.loads(path.read_text());assert cert['native_bracelets']=={k:list(v) for k,v in WORDS.items()}
    balanced={w for w in itertools.product((0,1),repeat=6) if sum(w)==3}
    assert len(balanced)==20 and set().union(*(set(orbit(w)) for w in WORDS.values()))==balanced
    assert [len(orbit(w)) for w in WORDS.values()]==[6,12,2]
    assert len({min(orbit(w)) for w in balanced})==3
    # Exact 36-star closure at a representative nondegenerate parameter.
    p=Fraction(130);angles=[p,240-p,360-2*p,2*p-120]
    zero=[t for t in itertools.combinations_with_replacement(range(4),3) if sum(angles[i] for i in t)==360]
    assert zero==[(0,0,2),(1,1,3)]
    summary=[]; cc=None
    for row in cert['small_ring_censuses']:
        a,b=row['A_bracelet'],row['B_bracelet']; aw,states,relations,alive,rounds=census(a,b)
        assert aw==[tuple(w) for w in row['A_patterns']] and states==row['states']
        assert relations==[set(map(tuple,r)) for r in row['relations']]
        assert alive==row['survivors'] and rounds==row['triangle_deletion_rounds']
        summary.append([a,b,len(states),len(alive)])
        if (a,b)==('C','C'):cc=(states,relations,alive)
    assert summary==[['C','C',96,6],['C','I',48,0],['C','ALT',2,0],['ALT','C',0,0],['ALT','I',0,0],['ALT','ALT',2,2]]
    states,relations,alive=cc; assert alive==[15,26,37,58,69,80]
    maps=[]
    for rel in relations:
        nxt=[]
        for i in alive:
            js=[j for u,j in rel if u==i and j in alive];assert len(js)==1
            nxt.append(alive.index(js[0]))
        assert sorted(nxt)==list(range(6));maps.append(nxt)
    assert maps[:3]==[[5,1,3,2,4,0],[0,4,3,2,1,5],[5,4,2,3,1,0]] and maps[3:]==maps[:3]
    assert all(maps[i][maps[j][q]]==maps[j][maps[i][q]] for i,j,q in itertools.product(range(6),range(6),range(6)))
    for w in orbit(WORDS['C']):assert sum(placed(WORDS['C'],p)==w for p in P)==2
    # Every abstract equality table of two binary maps is tested by all
    # assignments of four values to up to four equivalence classes.
    allowed=set()
    for values in itertools.product(range(4),repeat=4):
        table=frozenset((i,j) for i,j in itertools.product(range(2),repeat=2) if values[i]==values[2+j])
        assert len(table)!=3;allowed.add(table)
    assert len(allowed)==12
    angle_tori=[]
    for row in cert['stripe_witnesses']:
        angle_tori.append([row['A_bracelet'],row['B_bracelet'],*verify_torus(row,row['A_bracelet'],row['B_bracelet'])])
    assert {(r[0],r[1]) for r in angle_tori}=={('C','C'),('I','C'),('I','I'),('I','ALT'),('ALT','ALT')}
    metric_tori=[]
    for row in cert['alternating_metric_witnesses']:
        q=row['B_length_class'];assert row['side_length_classes']==[0,1]*3+[q]*6
        metric_tori.append([q,*verify_torus(row,'ALT','ALT',row['side_length_classes'])])
    assert metric_tori==[[0,6,18],[1,6,18]]
    # All reflected/rotated A vertices with EO native sides: equality of
    # their shared ray forces equality of their other (B-boundary) rays.
    local_cases=0
    for pa,pb,k,l in itertools.product(P,P,range(6),range(6)):
        aa=[side(pa,(k-1)%6)%2,side(pa,k)%2]
        bb=[side(pb,(l-1)%6)%2,side(pb,l)%2]
        assert set(aa)==set(bb)=={0,1}
        if aa[1]==bb[0]:assert aa[0]==bb[1];local_cases+=1
    result={'status':'PASSED','balanced_words':20,'colour_bracelets':3,'small_censuses':summary,
            'CC_survivors':alive,'CC_successor_maps':maps,'binary_equality_table_types':len(allowed),
            'angle_tori':angle_tori,'alternating_metric_tori':metric_tori,'reflection_safe_local_metric_cases':local_cases,
            'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'scope':'Exact finite colour/native torus records and binary fibre tables; infinite fibre lifting and Euclidean development are separate dependencies'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
