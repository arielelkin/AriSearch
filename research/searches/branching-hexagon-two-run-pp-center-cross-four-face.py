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
    parent=list(range(24));members=[{i} for i in range(24)]
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for (u,i),(v,j) in pairs:
        for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:
            a,b=root(6*a[0]+a[1]),root(6*b[0]+b[1])
            if a!=b:
                parent[b]=a;members[a]|=members[b]
                if len(members[a])>3:return None
    cs=[sorted((x//6,x%6) for x in members[r]) for r in range(24) if root(r)==r]
    if any(len(c)!=3 or tuple(sum(faces[u]['angle_rows'][i][j] for u,i in c) for j in range(4))!=(360,0,0,0) for c in cs):return None
    adj=defaultdict(list);graph=defaultdict(set);used=defaultdict(int)
    for (u,i),(v,j) in pairs:
        used[u,i]+=1;used[v,j]+=1;graph[u].add(v);graph[v].add(u)
        for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:adj[a].append(b);adj[b].append(a)
    assert len(used)==24 and set(used.values())=={1}
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
    if len(seen)!=4:return None
    assert len(cs)-12+4==0
    return cs

def run(output=None):
    ap=[(u,i) for u in(0,1) for i in range(6) if faces[u]['labels'][i]=='p']
    bp=[(u,i) for u in(2,3) for i in range(6) if faces[u]['labels'][i]=='p']
    aq=[[i for i in range(6) if faces[u]['labels'][i]=='q'] for u in(0,1)]
    matches=[perm for perm in itertools.permutations(ap) if all(endpointok(*b,*a) for b,a in zip(bp,perm))]
    count=0;witness=None
    for qa0,qa1,swap in itertools.product(aq[0],aq[1],(0,1)):
        abq=[((2,4),(swap,qa1 if swap else qa0)),((3,1),(1-swap,qa0 if swap else qa1))]
        if not all(endpointok(*x,*y) for x,y in abq):continue
        remainder=[]
        for u,selected in[(0,qa0),(1,qa1)]:
            rest=[i for i in aq[u] if i!=selected];remainder.append(((u,rest[0]),(u,rest[1])))
        qq=[((2,3),(3,0)),((2,5),(3,2))]+remainder+abq
        if not all(endpointok(*x,*y) for x,y in qq):continue
        for perm in matches:
            count+=1;pairs=list(zip(bp,perm))+qq;classes=evaluate(pairs)
            if classes is not None:
                witness={'faces':faces,'paired_edges':pairs,'vertex_classes':classes};break
        if witness:break
    out={'domain':'fixedA+,A-,B+,B-;allpAB;BmiddleqABoneperA;otherAqselfpair;BouterqcrossBB;genericcrossstarrows',
         'unfiltered_p_permutation_count':720,'endpoint_filtered_p_matchings':len(matches),'attempts':count,
         'status':'positive_witness' if witness else 'exhausted_only_stated_finite_domain','witness':witness}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(out['status'],'filteredp',len(matches),'attempts',count);return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();run(args.output)
