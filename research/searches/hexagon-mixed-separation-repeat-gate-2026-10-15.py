#!/usr/bin/env python3
"""Exact narrow common-five-color mixed-repeat source gate and positive witnesses.
Integer/Fraction only. JSON stdout; --output explicitly retains evidence.
"""
from itertools import permutations, combinations, product
from pathlib import Path
import argparse, json
from fractions import Fraction as F
from collections import defaultdict
A=(0,1,0,2,3,4)

def arm(words,c):
 f,i=divmod(c,6)
 return frozenset((words[f][i],words[f][(i+1)%6]))

def slot(words,c,r):
 f,i=divmod(c,6)
 assert len(arm(words,c))==2 and r in arm(words,c)
 return 6*f+(i if words[f][i]==r else (i+1)%6)

def far(words,c,r):
 j=slot(words,c,r);f,i=divmod(j,6)
 return 6*f+(i-1)%6 if c==j else j

def atlas(words):
 return [t for t in combinations(range(12),3)
         if len({arm(words,c) for c in t})==3
         and len(set().union(*(arm(words,c) for c in t)))==3]

def demands(words,t):
 out=[]
 for c,d in combinations(t,2):
  common=arm(words,c)&arm(words,d)
  assert len(common)==1
  r=next(iter(common));cc,dd=far(words,c,r),far(words,d,r)
  out.append((c,d,r,cc,dd))
 return out

def choices(stars,cc,dd):
 return [t for t in stars if cc!=dd and cc in t and dd in t]

def components(words,stars):
 edges=set()
 for t in stars:
  for c,d,r,cc,dd in demands(words,t):
   edges.add(tuple(sorted((slot(words,c,r),slot(words,d,r)))))
 sets=[{c} for c in range(12)]
 for a,b in sorted(edges):
  union=sets[a]|sets[b]
  for c in union:sets[c]=union
 return sorted(edges),sorted({tuple(sorted(s)) for s in sets})

def matchings(items):
    if not items:
        yield ()
        return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        for rest in matchings(items[1:j]+items[j+1:]):
            yield ((a,b),)+rest

def torus_atlas():
    WORDS=(A,REP)
    records={};totals=defaultdict(int)
    for tail in product((1,-1),repeat=3):
        signs=(1,)+tail
        groups=defaultdict(list)
        for f in range(4):
            for k in range(6):
                side=k if signs[f]==1 else (-k-1)%6
                groups[WORDS[f//2][side]].append(6*f+k)
        choices=[list(matchings(tuple(groups[c]))) for c in range(5)]
        assert list(map(len,choices))==[15,3,15,3,3]
        for per_color in product(*choices):
            pairs=tuple(pair for block in per_color for pair in block)
            totals['all_pairings']+=1
            faces=[set() for _ in range(4)]
            for a,b in pairs:
                faces[a//6].add(b//6);faces[b//6].add(a//6)
            reached={0}
            while True:
                more=reached|set().union(*(faces[f] for f in reached))
                if more==reached:break
                reached=more
            if len(reached)<4:continue
            totals['connected_pairings']+=1
            parent=list(range(24))
            def find(i):
                while parent[i]!=i:
                    parent[i]=parent[parent[i]];i=parent[i]
                return i
            def unite(a,b):
                a,b=find(a),find(b)
                if a!=b:parent[b]=a
            for a,b in pairs:
                f,k=divmod(a,6);g,l=divmod(b,6)
                unite(6*f+k,6*g+(l+1)%6)
                unite(6*f+(k+1)%6,6*g+l)
            vertices=defaultdict(list)
            for c in range(24):vertices[find(c)].append(c)
            if len(vertices)!=8 or any(len(v)!=3 for v in vertices.values()):continue
            totals['trivalent_tori']+=1
            triples=[]
            for v in vertices.values():
                actual=[]
                for c in v:
                    f,k=divmod(c,6)
                    native_vertex=(signs[f]*k)%6
                    actual.append(6*(f//2)+(native_vertex-1)%6)
                triples.append(tuple(sorted(actual)))
            signature=tuple(sorted(set(triples)))
            records.setdefault(signature,{'signs':signs,'edge_pairs':pairs,
                'vertex_triples':sorted(triples),'angle_support':signature})
    assert totals['all_pairings']==48600
    return {'schema':'MIXED_SEPARATION_FOUR_FACE_ATLAS_V1',
        'A':WORDS[0],'B':WORDS[1],
        'domain':{'faces':['A','A','B','B'],'orientation_choices':8,
            'two_six_slot_matching_choices':[15,15],'three_four_slot_matching_choices':[3,3,3],'total':48600,
            'corner_convention':'native corner after side i; A0..5 B6..11'},
        'counts':dict(totals),'distinct_angle_supports':len(records),
        'witnesses':[records[s] for s in sorted(records)]}

def star_row(st):return [F(st.count(i)) for i in range(12)]+[F(2)]

def source_rows(stars):
    return [[F(i<6) for i in range(12)]+[F(4)],
            [F(i>=6) for i in range(12)]+[F(4)]]+[star_row(st) for st in stars]

def basis_with_weights(rows):
    n=len(rows);basis={}
    for j,source in enumerate(rows):
        row=list(source);weights=[F(i==j) for i in range(n)]
        for pivot,(b,w) in sorted(basis.items()):
            q=row[pivot]
            if q:
                row=[a-q*c for a,c in zip(row,b)]
                weights=[a-q*c for a,c in zip(weights,w)]
        pivot=next((i for i,x in enumerate(row) if x),None)
        if pivot is not None:
            q=row[pivot]
            basis[pivot]=([a/q for a in row],[a/q for a in weights])
    return basis

def express(row,basis,n):
    row=list(row);weights=[F(0)]*n
    for pivot,(b,w) in sorted(basis.items()):
        q=row[pivot]
        if q:
            row=[a-q*c for a,c in zip(row,b)]
            weights=[a+q*c for a,c in zip(weights,w)]
    return None if any(row) else [str(x) for x in weights]

REP=(2,0,3,2,4,1)

def prune(W):
 original=atlas(W);current=original;rounds=[]
 while True:
  survive=[t for t in current if all(choices(current,q[3],q[4]) for q in demands(W,t))]
  if survive==current:break
  rounds.append({'input':current,'output':survive});current=survive
 return original,rounds,current

def equivalence(B):
 for shift in range(6):
  for direction in (1,-1):
   mapping={};valid=True
   for i in range(6):
    old=A[(shift+direction*i)%6]
    if old in mapping and mapping[old]!=A[i]:valid=False;break
    mapping[old]=A[i]
   if not valid or len(set(mapping.values()))!=5:continue
   for s in range(6):
    for d in (1,-1):
     if tuple(mapping[B[(s+d*i)%6]] for i in range(6))==REP:
      return {'A_shift':shift,'A_direction':direction,'color_map':mapping,'B_shift':s,'B_direction':d}
 return None

def build():
 records=[];hard=[]
 for p in range(5):
  for q in permutations(sorted(set(range(5))-{p})):
   B=(p,q[0],q[1],p,q[2],q[3]);W=(A,B)
   original,rounds,S=prune(W);edges,comps=components(W,S)
   cover=sorted({c for t in S for c in t})
   joined=[any(a in c and b in c for c in comps) for a,b in ((0,2),(6,9))]
   eq=equivalence(B) if cover==list(range(12)) and all(joined) else None
   if cover==list(range(12)) and all(joined):assert eq is not None;hard.append(B)
   records.append({'B':B,'initial_atlas':original,'pruning_rounds':rounds,'fixed_atlas':S,'covered_corners':cover,'fixed_seams':edges,'fixed_components':comps,'repeated_joined':joined,'hard_class_equivalence':eq})
 assert len(records)==120 and len(hard)==8
 assert sum(r['covered_corners']!=list(range(12)) for r in records)==96
 W=(A,REP);_,_,S=prune(W);supports=[]
 for mask in range(1<<len(S)):
  selected=[t for i,t in enumerate(S) if mask>>i&1]
  if {c for t in selected for c in t}!=set(range(12)):continue
  if all(choices(selected,q[3],q[4]) for t in selected for q in demands(W,t)):
   supports.append({'mask':mask,'stars':selected})
 assert len(S)==12 and len(supports)==30
 torus=torus_atlas();covered=[];exceptional=[]
 partition=((0,2,11),(1,5,10),(3,6,7),(4,8,9))
 for support in supports:
  stars=support['stars'];source=source_rows(stars);basis=basis_with_weights(source)
  for i,w in enumerate(torus['witnesses']):
   combinations=[express(star_row(t),basis,len(source)) for t in w['angle_support']]
   if all(c is not None for c in combinations):
    covered.append({'source':support,'torus_index':i,'row_combinations':combinations});break
  else:
   if tuple(stars)==partition:kind='unique_indexed_frame_propagation'
   else:
    assert tuple(stars)==partition+((6,7,8),(9,10,11));kind='opposite_repeat_mono_B_two_face_torus'
   exceptional.append({'source':support,'escape':kind})
 assert len(covered)==28 and len(exceptional)==2
 return {'schema':'COMMON_FIVE_MIXED_REPEAT_SEPARATION_V1','A':A,'representative_B':REP,
   'domain':'A repeat separation2, B repeat separation3, same five formal colors; all120 raw B words, all12-corner stars and closed covers; fixed 2A2B torus witnesses',
   'word_records':records,'representative_fixed_atlas':S,'representative_supports':supports,
   'torus_atlas':torus,'covered_supports':covered,'exceptional_supports':exceptional,
   'summary':{'raw_B_words':120,'no_corner_cover':96,'six_color_escape':16,'hard_raw_words':8,'hard_classes':1,'representative_supports':30,'row_covered':28,'deterministic_escape':1,'mono_B_escape':1},
   'scope':'Exact finite necessary source classification and positive flat-torus certificates; geometry and frame propagation require the accompanying proof.'}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
 encoded=json.dumps(build(),sort_keys=True,indent=2)+'\n'
 if args.output:Path(args.output).write_text(encoded)
 print(encoded,end='')
