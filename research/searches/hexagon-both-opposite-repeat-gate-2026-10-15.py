#!/usr/bin/env python3
"""Exact narrow common-five-color both-opposite source gate and positive witnesses.
Integer/Fraction only. JSON stdout; --output explicitly retains evidence.
"""
from itertools import permutations, combinations, product
from pathlib import Path
import argparse, json
from fractions import Fraction as F
from collections import defaultdict
A=(0,1,2,0,3,4)

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
        assert list(map(len,choices))==[105,3,3,3,3]
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
    assert totals['all_pairings']==68040
    return {'schema':'OPPOSITE_REPEAT_FOUR_FACE_ATLAS_V1',
        'A':WORDS[0],'B':WORDS[1],
        'domain':{'faces':['A','A','B','B'],'orientation_choices':8,
            'eight_slot_matching_choices':105,'four_four_slot_matching_choices':[3,3,3,3],'total':68040,
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

def prune(W):
 original=atlas(W);current=original;rounds=[]
 while True:
  survive=[t for t in current if all(choices(current,q[3],q[4]) for q in demands(W,t))]
  if survive==current:break
  rounds.append({'input':current,'output':survive});current=survive
 return original,rounds,current

def equivalence(B,target):
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
     if tuple(mapping[B[(s+d*i)%6]] for i in range(6))==target:
      return {'A_shift':shift,'A_direction':direction,'color_map':mapping,'B_shift':s,'B_direction':d}
 return None

REPS=((0,1,2,0,3,4),(0,1,2,0,4,3),(0,1,3,0,2,4),(0,1,4,0,3,2))

def frame_escape(W,stars):
 counts=[sum(i in st for st in stars) for i in range(12)]
 if counts==[1]*12:return {'kind':'all_native_corners_unique'}
 unique=None
 for species in (0,1):
  if all(sum(c//6==species for c in st)==1 for st in stars) and all(counts[6*species+i]==1 for i in range(6)):
   unique=species;break
 assert unique is not None
 other=1-unique;maps=[]
 for side in range(6):
  color=W[other][side];ends=[]
  for local in ((side-1)%6,side):
   corner=6*other+local;poss=set()
   for st in stars:
    if corner in st:
     for c in st:
      if c//6==unique and color in arm(W,c):poss.add((c,slot(W,c,color)))
   assert len(poss)==1;ends.append(next(iter(poss)))
  assert ends[0][1]==ends[1][1] and ends[0][0]!=ends[1][0]
  maps.append({'other_side':side,'guest_side':ends[0][1],'guest_endpoint_corners':ends})
 return {'kind':'all_AAB_with_unique_singleton_species_corners','unique_species':unique,'conditional_other_to_unique_maps':maps,'other_state':'parity of alternating sides incident to unique species'}

def build():
 global REP
 records=[];hard=[]
 for p in range(5):
  for q in permutations(sorted(set(range(5))-{p})):
   B=(p,q[0],q[1],p,q[2],q[3]);W=(A,B)
   full=atlas(W);mixed=[st for st in full if len({c//6 for c in st})==2]
   S=mixed;rounds=[]
   while True:
    T=[st for st in S if all(choices(S,z[3],z[4]) for z in demands(W,st))]
    if T==S:break
    rounds.append({'input':S,'output':T});S=T
   edges,comps=components(W,S);cover=sorted({c for st in S for c in st})
   joined=[any(a in c and b in c for c in comps) for a,b in ((0,3),(6,9))]
   target=None;eq=None
   if cover==list(range(12)) and all(joined):
    for i,rep in enumerate(REPS):
     eq=equivalence(B,rep)
     if eq is not None:target=i;break
    assert target is not None;hard.append(B)
   records.append({'B':B,'full_atlas':full,'mixed_atlas':mixed,'pruning_rounds':rounds,'fixed_atlas':S,'covered_corners':cover,'fixed_seams':edges,'fixed_components':comps,'repeated_joined':joined,'hard_representative':target,'hard_class_equivalence':eq})
 assert len(records)==120 and len(hard)==16
 assert sum(r['covered_corners']!=list(range(12)) for r in records)==80
 classes=[]
 for REP in REPS:
  W=(A,REP);S=next(r['fixed_atlas'] for r in records if tuple(r['B'])==REP)
  supports=[]
  for mask in range(1<<len(S)):
   stars=[t for i,t in enumerate(S) if mask>>i&1]
   if {c for t in stars for c in t}!=set(range(12)):continue
   if all(choices(stars,z[3],z[4]) for t in stars for z in demands(W,t)):supports.append({'mask':mask,'stars':stars})
  if len(S)==4:
   assert len(supports)==1
   classes.append({'B':REP,'fixed_atlas':S,'supports':supports,'torus_atlas':None,'covered_supports':[],'exceptional_supports':[{'source':supports[0],'frame_escape':frame_escape(W,S)}]});continue
  torus=torus_atlas();covered=[];miss=[]
  for support in supports:
   stars=support['stars'];rows=source_rows(stars);basis=basis_with_weights(rows)
   for i,w in enumerate(torus['witnesses']):
    comb=[express(star_row(t),basis,len(rows)) for t in w['angle_support']]
    if all(c is not None for c in comb):covered.append({'source':support,'torus_index':i,'row_combinations':comb});break
   else:miss.append({'source':support,'frame_escape':frame_escape(W,stars)})
  classes.append({'B':REP,'fixed_atlas':S,'supports':supports,'torus_atlas':torus,'covered_supports':covered,'exceptional_supports':miss})
 assert [len(c['supports']) for c in classes]==[141,1,27,57]
 assert [len(c['covered_supports']) for c in classes]==[139,0,25,57]
 assert [len(c['exceptional_supports']) for c in classes]==[2,1,2,0]
 identities=sum(len(r['row_combinations']) for c in classes for r in c['covered_supports'])
 return {'schema':'COMMON_FIVE_BOTH_OPPOSITE_REPEAT_V1','A':A,'word_records':records,'hard_representatives':REPS,'classes':classes,
  'summary':{'raw_B_words':120,'mixed_no_cover':80,'mixed_six_color_escape':24,'hard_words':16,'hard_classes':4,'actual_supports':226,'row_covered_supports':221,'frame_escapes':5,'exact_row_identities':identities},
  'scope':'Complete necessary common-five both-opposite source gate after monohedral escapes; positive fixed-four-face witnesses and conditional indexed frame maps; no bounded-negative inference.'}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
 encoded=json.dumps(build(),sort_keys=True,indent=2)+'\n'
 if args.output:Path(args.output).write_text(encoded)
 print(encoded,end='')
