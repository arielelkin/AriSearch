#!/usr/bin/env python3
"""Narrow complete common-five adjacent-repeat support/positive-witness gate.
Exact integers and Fraction only. Complete native microstates are reconstructed
by the retained narrow reconnaissance module, independently audited elsewhere.
Fixed four-face witnesses are positive certificates; no bounded miss is used.
"""
from itertools import product
from collections import defaultdict,Counter
from fractions import Fraction as F
from pathlib import Path
import importlib.util,argparse,json
HERE=Path(__file__).resolve().parent
def module(name,filename):
 spec=importlib.util.spec_from_file_location(name,HERE/filename)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
native=module('adjacent_native','hexagon-five-adjacent-microstate-recon-2026-10-15.py')
corona=module('adjacent_corona','hexagon-adjacent-corona-states-2026-10-15.py')
A=native.A
REPS=((0,0,1,3,2,4),(0,0,2,4,1,3),(2,2,1,3,0,4),(0,1,3,0,4,2))
def equivalence(B,target):
 for sh in range(6):
  for dr in (1,-1):
   mp={};valid=True
   for i in range(6):
    old=A[(sh+dr*i)%6]
    if old in mp and mp[old]!=A[i]:valid=False;break
    mp[old]=A[i]
   if not valid or len(set(mp.values()))!=5:continue
   for s in range(6):
    for t in (1,-1):
     if tuple(mp[B[(s+t*i)%6]] for i in range(6))==target:return {'A_shift':sh,'A_direction':dr,'color_map':mp,'B_shift':s,'B_direction':t}
 return None
def matchings(items):
    if not items:
        yield ()
        return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        for rest in matchings(items[1:j]+items[j+1:]):
            yield ((a,b),)+rest

def torus_atlas(WORDS):
    records={};totals=defaultdict(int)
    for tail in product((1,-1),repeat=3):
        signs=(1,)+tail
        groups=defaultdict(list)
        for f in range(4):
            for k in range(6):
                side=k if signs[f]==1 else (-k-1)%6
                groups[WORDS[f//2][side]].append(6*f+k)
        choices=[list(matchings(tuple(groups[c]))) for c in range(5)]
        assert sorted(map(len,choices)) in ([3,3,3,3,105],[3,3,3,15,15])
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
    assert totals['all_pairings'] in (48600,68040)
    return {'schema':'ADJACENT_FIVE_FOUR_FACE_ATLAS_V1',
        'A':WORDS[0],'B':WORDS[1],
        'domain':{'faces':['A','A','B','B'],'orientation_choices':8,
            'total':totals['all_pairings'],
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


def build():
 gate=native.build();hard=[r for r in gate['records'] if r['kind']=='both_joined'];maps=[]
 for r in hard:
  for i,B in enumerate(REPS):
   eq=equivalence(r['B'],B)
   if eq is not None:maps.append({'B':r['B'],'B_repeat_separation':r['B_repeat_separation'],'representative':i,'equivalence':eq});break
  else:raise AssertionError('Uncovered hard word')
 assert len(maps)==12
 out=[]
 for ci,B in enumerate(REPS):
  full=native.prune(native.microstates((A,B)));stars=sorted({m[0] for m in full});supports=[]
  for mask in range(1<<len(stars)):
   S={stars[i] for i in range(len(stars)) if mask>>i&1}
   if {c for st in S for c in st}!=set(range(12)):continue
   M=native.prune({m for m in full if m[0] in S})
   if {m[0] for m in M}==S:supports.append({'mask':mask,'stars':sorted(S),'fixed_microstates':sorted(M)})
  atlas=None if ci==1 else torus_atlas((A,B));covered=[];residual=[]
  for source in supports:
   S=source['stars'];rr=source_rows(S);basis=basis_with_weights(rr)
   if atlas is not None:
    for wi,w in enumerate(atlas['witnesses']):
     combos=[express(star_row(t),basis,len(rr)) for t in w['angle_support']]
     if all(c is not None for c in combos):covered.append({'source':source,'torus_index':wi,'row_combinations':combos});break
    else:wi=None
    if wi is not None:continue
   if ci==1:
    if len(S)>=12:
     combos=[]
     for i in range(12):
      goal=[F(j==i) for j in range(12)]+[F(2,3)]
      coeff=express(goal,basis,len(rr));assert coeff is not None;combos.append(coeff)
     residual.append({'source':source,'escape':'all_angles_120_then_all_lengths_equal','angle_row_combinations':combos})
    elif len(S)==7:
     pure=[st for st in S if len(set(st))==1];assert len(pure)==1
     residual.append({'source':source,'escape':'five_corner_alternation_forbids_sixth_pure_vertex','pure_star':pure[0]})
    else:
     assert len(S)==6
     counts=[sum(c//6 for c in st) for st in S]
     assert set(counts) in ({1},{2})
     residual.append({'source':source,'escape':'AB_alternation_and_connected_AB_graph','corona':corona.analyze(B,S)})
   elif ci==2:
    assert len(S)==6
    c=corona.analyze(B,S);bad=[]
    for f,ss in enumerate(c['neighbor_state_choices']):
     for k,state in enumerate(ss):
      for side,options in enumerate(state):
       if len(options)!=1:bad.append((f,side))
    assert set(bad) in ({(0,2)},{(1,5)})
    bypass=(2,2,6) if bad[0][0]==0 else (0,10,10)
    assert bypass in S
    residual.append({'source':source,'escape':'connected_certain_transition_graph','corona':c,'uncertain_species_side':sorted(set(bad)),'bypass_star':bypass})
   else:
    assert ci==3
    if (6,7,8) in S or (9,10,11) in S:
     residual.append({'source':source,'escape':'opposite_repeat_pure_B_two_face_torus'})
    else:
     c=corona.analyze(B,S)
     assert all(len(options)==1 for ss in c['neighbor_state_choices'] for state in ss for options in state)
     residual.append({'source':source,'escape':'all_corona_state_transitions_unique','corona':c})
  out.append({'B':B,'fixed_star_atlas':stars,'support_count':len(supports),'torus_atlas':atlas,'covered':covered,'residual':residual})
 assert [x['support_count'] for x in out]==[9,12,6,14]
 assert [len(x['covered']) for x in out]==[9,0,4,12]
 closure=[[F(x) for x in row] for row in ((3,-1,-2,-1,1),(1,1,0,-1,-1),(3,-1,-1,1,-2),(1,-1,1,-1,0))]
 basis=basis_with_weights(closure);assert len(basis)==4
 identities=[]
 for i in range(1,5):
  row=[F(j==i)-F(j==0) for j in range(5)]
  coeff=express(row,basis,len(closure));assert coeff is not None;identities.append(coeff)
 return {'schema':'COMMON_FIVE_ADJACENT_COMPLETE_PERIODIC_GATE_V1','A':A,'native_gate_summary':gate['summary'],'raw_word_count':360,'hard_word_equivalences':maps,'classes':out,
 'B2_equiangular_closure':{'rows':[[str(x) for x in row] for row in closure],'color_order':'r,x,y,z,t','all_lengths_equal_rows':identities},
 'summary':{'representative_supports':41,'positive_four_face_covered':25,'residual_supports':16,'large_equiangular':8,'parity_impossible':2,'intrinsic_state':5,'monohedral_B':1},
 'scope':'Complete necessary source cases plus positive torus and exact linear certificates; state-propagation connectivity is in the proof. Main target unresolved.'}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();encoded=json.dumps(build(),sort_keys=True,indent=2)+'\n'
 if a.output:Path(a.output).write_text(encoded)
 print(encoded,end='')
