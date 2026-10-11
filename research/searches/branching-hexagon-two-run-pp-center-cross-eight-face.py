"""Finite actual-star constrained cross-qq pp-center quotient search.
Exactly A+,A-,B+,B-; whole p allAB, BmiddleqAB, outerq crossBB,
Aremainingq selfpairs within same chirality. Failure excludes only this domain.
Read-only normally; explicit --output writes a witness/search record.
"""
import argparse,json,itertools
from pathlib import Path
from collections import defaultdict
labels=[['p','q']*3,['p']*3+['q']*3]
angles=[[(120,1,0,0),(120,-1,0,0)]*3,
        [(240,1,-1,0),(120,0,0,0),(120,0,0,0),(240,-1,0,-1),(0,0,1,0),(0,0,0,1)]]
def face(species,mirror):
    s=0 if species=='A' else 1
    return {'species':species,'mirror':mirror,
            'labels':[labels[s][(5-i)%6] if mirror else labels[s][i] for i in range(6)],
            'angle_rows':[angles[s][(-i)%6] if mirror else angles[s][i] for i in range(6)]}
faces=[face('A',False),face('A',True),face('B',False),face('B',True)]
def endpointok(u,i,v,j):
    for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:
        pair=tuple(x+y for x,y in zip(faces[a[0]]['angle_rows'][a[1]],faces[b[0]]['angle_rows'][b[1]]))
        if not any(tuple(x+y for x,y in zip(pair,c))==(360,0,0,0) for ar in angles for c in ar):return False
    return True

def evaluate(pairs):
    parent=list(range(48));members=[{i} for i in range(48)]
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for (u,i),(v,j) in pairs:
        for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:
            a,b=root(6*a[0]+a[1]),root(6*b[0]+b[1])
            if a!=b:
                parent[b]=a;members[a]|=members[b]
                if len(members[a])>3:return None
    cs=[sorted((x//6,x%6) for x in members[r]) for r in range(48) if root(r)==r]
    if any(len(c)!=3 or tuple(sum(faces[u]['angle_rows'][i][j] for u,i in c) for j in range(4))!=(360,0,0,0) for c in cs):return None
    adj=defaultdict(list);graph=defaultdict(set);used=defaultdict(int)
    for (u,i),(v,j) in pairs:
        used[u,i]+=1;used[v,j]+=1;graph[u].add(v);graph[v].add(u)
        for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:adj[a].append(b);adj[b].append(a)
    assert len(used)==48 and set(used.values())=={1}
    for c in cs:
        assert all(len(adj[tuple(v)])==2 for v in c)
        seen=set();todo=[tuple(c[0])]
        while todo:
            x=todo.pop()
            if x not in seen:seen.add(x);todo+=adj[x]
        assert seen==set(map(tuple,c))
    seen={0};todo=[0]
    while todo:
        for v in graph[todo.pop()]-seen:seen.add(v);todo.append(v)
    if len(seen)!=8:return None
    assert len(cs)-24+8==0
    return cs

def run(output=None):
    from fractions import Fraction
    from collections import Counter
    global faces
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-two-run-pp-center-cross-slot-balance.json'
    record=json.loads(source.read_text())['record'];assert record['status']=='sat'
    skeleton=set()
    for cycle,x in zip(record['oriented_stars'],record['star_frequencies']):
        if not Fraction(x):continue
        assert Fraction(x)==Fraction(1,2)
        for cyc in(cycle,[o^1 for o in reversed(cycle)]):
            for i,o in enumerate(cyc):
                oo=cyc[(i+1)%3];s,v=(o//2)//6,(o//2)%6;fl=o%2;t,j=(oo//2)//6,(oo//2)%6;fl2=oo%2
                ex=v if fl else(v-1)%6;ey=(j-1)%6 if fl2 else j
                a=(2*s+fl,5-ex if fl else ex);b=(2*t+fl2,5-ey if fl2 else ey)
                skeleton.add(tuple(sorted((a,b))))
    nonself=sorted(pair for pair in skeleton if pair[0]!=pair[1]);selfs=sorted(a for a,b in skeleton if a==b)
    degree=Counter(e for pair in nonself for e in pair);degree.update(selfs)
    assert len(nonself)==10 and len(selfs)==4 and len(degree)==24 and set(degree.values())=={1}
    base=faces;faces=[dict(f,base_face=u,copy=t) for u,f in enumerate(base) for t in(0,1)]
    witness=None;count=0
    for count,bits in enumerate(itertools.product((0,1),repeat=10),1):
        pairs=[((2*u+t,i),(2*v+(t^bit),j)) for ((u,i),(v,j)),bit in zip(nonself,bits) for t in(0,1)]+[((2*u,i),(2*u+1,i)) for u,i in selfs]
        classes=evaluate(pairs)
        if classes is not None:
            witness={'faces':faces,'paired_edges':pairs,'vertex_classes':classes,'lift_bits':bits};break
    out={'domain':'1024two-copy lifts of retained4star primal plusmirror support, crossqq centergeometry',
         'source_slot_balance':source.name,'skeleton':sorted(skeleton),'attempts':count,
         'status':'positive_witness' if witness else 'exhausted_only_stated_1024lift_domain','witness':witness}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(out['status'],'attempts',count);return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();run(args.output)
