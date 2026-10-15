#!/usr/bin/env python3
"""Two fixed four-face positive-witness domains; no larger quotient search."""
from itertools import product
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json, argparse
A=(0,1,0,2,3,4)
REPS=((0,3,0,5,1,6),(0,3,0,2,1,5))

def matchings(items):
    if not items:
        yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in matchings(items[1:j]+items[j+1:]):
            yield ((a,items[j]),)+rest

def torus_atlas(B):
    W=(A,B);records={};counts=defaultdict(int)
    for tail in product((1,-1),repeat=3):
        signs=(1,)+tail;groups=defaultdict(list)
        for f in range(4):
            for k in range(6):
                side=k if signs[f]==1 else (-k-1)%6
                groups[W[f//2][side]].append(6*f+k)
        options=[list(matchings(tuple(groups[c]))) for c in sorted(groups)]
        for blocks in product(*options):
            pairs=tuple(p for block in blocks for p in block);counts['all_pairings']+=1
            adj=[set() for _ in range(4)]
            for a,b in pairs:adj[a//6].add(b//6);adj[b//6].add(a//6)
            reached={0}
            while True:
                nxt=reached|set().union(*(adj[f] for f in reached))
                if nxt==reached:break
                reached=nxt
            if len(reached)!=4:continue
            counts['connected']+=1;parent=list(range(24))
            def find(i):
                while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
                return i
            def unite(a,b):parent[find(a)]=find(b)
            for a,b in pairs:
                f,k=divmod(a,6);g,l=divmod(b,6)
                unite(6*f+k,6*g+(l+1)%6)
                unite(6*f+(k+1)%6,6*g+l)
            vertices=defaultdict(list)
            for c in range(24):vertices[find(c)].append(c)
            if len(vertices)!=8 or any(len(v)!=3 for v in vertices.values()):continue
            counts['trivalent_tori']+=1;triples=[]
            for v in vertices.values():
                corners=[]
                for c in v:
                    f,k=divmod(c,6)
                    corners.append(6*(f//2)+(signs[f]*k-1)%6)
                triples.append(tuple(sorted(corners)))
            sig=tuple(sorted(set(triples)))
            records.setdefault(sig,{'signs':signs,'edge_pairs':pairs,'vertex_triples':sorted(triples),'angle_support':sig})
    return {'B':B,'counts':dict(counts),'witnesses':[records[s] for s in sorted(records)]}

def row(star):return [F(star.count(i)) for i in range(12)]+[F(2)]

def basis(rows):
    n=len(rows);out={}
    for i,rr in enumerate(rows):
        r=list(rr);w=[F(j==i) for j in range(n)]
        for pivot,(b,c) in sorted(out.items()):
            q=r[pivot]
            if q:r=[x-q*y for x,y in zip(r,b)];w=[x-q*y for x,y in zip(w,c)]
        pivot=next((j for j,x in enumerate(r) if x),None)
        if pivot is not None:
            q=r[pivot];out[pivot]=([x/q for x in r],[x/q for x in w])
    return out

def express(r,bs,n):
    r=list(r);w=[F(0)]*n
    for pivot,(b,c) in sorted(bs.items()):
        q=r[pivot]
        if q:r=[x-q*y for x,y in zip(r,b)];w=[x+q*y for x,y in zip(w,c)]
    return None if any(r) else [str(x) for x in w]

def build():
    d=json.loads(Path('research/certificates/hexagon-five-noncommon-gate-2026-10-15.json').read_text())
    out=[]
    for B in REPS:
        s=next(r for r in d['hard_records'] if tuple(r['A'])==A and tuple(r['B'])==B)
        t=torus_atlas(B);checks=[]
        for support in s['supports']:
            rows=[[F(i<6) for i in range(12)]+[F(4)],[F(i>=6) for i in range(12)]+[F(4)]]+[row(st) for st in support]
            bs=basis(rows);found=None
            for j,wit in enumerate(t['witnesses']):
                co=[express(row(st),bs,len(rows)) for st in wit['angle_support']]
                if all(c is not None for c in co):found={'torus_index':j,'row_combinations':co};break
            checks.append({'source_support':support,'positive_torus_implication':found})
        assert all(c['positive_torus_implication'] is not None for c in checks)
        assert t['counts']['all_pairings']==(7560 if len(set(B)|set(A))==7 else 22680)
        t['support_checks']=checks;out.append(t)
    assert sum(len(c['support_checks']) for c in out)==10
    assert sum(len(r['positive_torus_implication']['row_combinations']) for c in out for r in c['support_checks'])==40
    return {'schema':'FIVE_NONCOMMON_TWO_FIXED_FOURFACE_ATLASES_V1','A':A,'classes':out,'scope':'Positive full-side flat tori from exact source angle row identities; a miss is no impossibility claim.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--summary',action='store_true');args=ap.parse_args();d=build()
    if args.output:Path(args.output).write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
    if not args.summary:
        print(json.dumps(d,sort_keys=True,indent=2))
        raise SystemExit(0)
    for c in d['classes']:
        print('B',c['B'],'counts',c['counts'],'angle supports',len(c['witnesses']),'covered',sum(s['positive_torus_implication'] is not None for s in c['support_checks']),'of',len(c['support_checks']))
        for s in c['support_checks']:
            if s['positive_torus_implication'] is None:print('MISS',s['source_support'])
