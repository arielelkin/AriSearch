#!/usr/bin/env python3
"""Complete common-five adjacent proof-data audit; no author module imports."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,runpy
ROOT=Path(__file__).resolve().parents[2]
N=runpy.run_path(str(ROOT/'research/reviews/hexagon-five-adjacent-microstate-independent-2026-10-15.py'))
C=runpy.run_path(str(ROOT/'research/reviews/hexagon-adjacent-corona-independent-2026-10-15.py'))
D=json.loads((ROOT/'research/certificates/hexagon-common-five-adjacent-periodic-gate-2026-10-15.json').read_text())
G=json.loads((ROOT/'research/certificates/hexagon-five-adjacent-microstate-gate-2026-10-15.json').read_text())
A=(0,0,1,2,3,4)
assert json.loads(json.dumps(N['build']()))==G
assert tuple(D['A'])==A and D['raw_word_count']==360 and D['native_gate_summary']==G['summary']
REPS=((0,0,1,3,2,4),(0,0,2,4,1,3),(2,2,1,3,0,4),(0,1,3,0,4,2))
hard={tuple(r['B']) for r in G['records'] if r['kind']=='both_joined'}
assert len(hard)==12 and {tuple(r['B']) for r in D['hard_word_equivalences']}==hard
assert len(D['hard_word_equivalences'])==12
for r in D['hard_word_equivalences']:
    B=tuple(r['B']);assert r['B_repeat_separation']==next(z['B_repeat_separation'] for z in G['records'] if tuple(z['B'])==B)
    w=r['equivalence'];mp={int(k):v for k,v in w['color_map'].items()}
    assert set(mp)==set(range(5))==set(mp.values())
    for word,target,sh,dr in ((A,A,w['A_shift'],w['A_direction']),(B,REPS[r['representative']],w['B_shift'],w['B_direction'])):
        assert tuple(mp[word[(sh+dr*i)%6]] for i in range(6))==target
        for i in range(6):
            old=(sh+i)%6 if dr==1 else (sh-i-1)%6
            assert {mp[word[old]],mp[word[(old+1)%6]]}=={target[i],target[(i+1)%6]}

def canonical(x):return json.loads(json.dumps(x))
def frozentiles(x):return [{tuple(tuple(a) for a in s) for s in f} for f in x]
def corona(B,S,d):
    assert tuple(d['B'])==B and {tuple(t) for t in d['support']}==S
    opts,states=C['reconstruct']((A,B),S)
    assert canonical([sorted(opts[c]) for c in range(12)])==d['corner_port_options']
    assert states==frozentiles(d['initial_tile_states'])
    while True:
        nxt=[{s for s in states[f] if all(C['guest_options'](f,s,i,states) for i in range(6))} for f in (0,1)]
        if nxt==states:break
        states=nxt
    assert states==frozentiles(d['fixed_tile_states']) and all(states)
    raw=[[tuple(tuple(a) for a in s) for s in f] for f in d['fixed_tile_states']]
    bad=set()
    for f in (0,1):
        for k,s in enumerate(raw[f]):
            for i in range(6):
                options=C['guest_options'](f,s,i,raw);g=s[i][0]//6
                assert [raw[g].index(t) for t in options]==d['neighbor_state_choices'][f][k][i]
                if len(options)!=1:bad.add((f,i))
    return bad,states

def gluing(B,w):
    signs=w['signs'];pairs=w['edge_pairs'];words=(A,A,B,B)
    assert len(signs)==4 and signs[0]==1 and all(s in (-1,1) for s in signs)
    assert sorted(x for ab in pairs for x in ab)==list(range(24))
    matching={a:b for a,b in pairs}|{b:a for a,b in pairs}
    adj={f:set() for f in range(4)}
    for a,b in pairs:
        f,k=divmod(a,6);g,l=divmod(b,6)
        aa=k if signs[f]==1 else (-k-1)%6;bb=l if signs[g]==1 else (-l-1)%6
        assert words[f][aa]==words[g][bb]
        adj[f].add(g);adj[g].add(f)
    seen={0};todo=[0]
    for f in todo:
        for g in adj[f]:
            if g not in seen:seen.add(g);todo.append(g)
    assert len(seen)==4
    # Vertex links are cycles of next-boundary-dart after edge involution.
    unused=set(range(24));native=[]
    while unused:
        start=min(unused);x=start;link=[]
        while x not in link:
            assert x in unused
            unused.remove(x);link.append(x)
            p=matching[x];x=6*(p//6)+(p+1)%6
        assert x==start and len(link)==3
        native.append(tuple(sorted(6*(e//12)+(signs[e//6]*(e%6)-1)%6 for e in link)))
    assert len(native)==8
    assert sorted(native)==[tuple(t) for t in w['vertex_triples']]
    assert set(native)=={tuple(t) for t in w['angle_support']}

def rows(S):return [[F(i<6) for i in range(12)]+[F(4)],[F(i>=6) for i in range(12)]+[F(4)]]+[[F(t.count(i)) for i in range(12)]+[F(2)] for t in S]
def identity(coeff,rr,goal):
    assert len(coeff)==len(rr)
    assert [sum(F(c)*r[j] for c,r in zip(coeff,rr)) for j in range(len(goal))]==goal

tags=Counter();angle120=0;angle_torus=0;positive=0;total=0;witnesses=0
for ci,c in enumerate(D['classes']):
    B=REPS[ci];assert tuple(c['B'])==B
    M=N['fixed'](N['generate']((A,B)));stars=sorted({t for t,ss in M})
    assert stars==[tuple(t) for t in c['fixed_star_atlas']]
    expected={}
    for bits in product((False,True),repeat=len(stars)):
        S={t for t,b in zip(stars,bits) if b}
        if {x for t in S for x in t}!=set(range(12)):continue
        L=N['fixed']({s for s in M if s[0] in S})
        if {t for t,ss in L}==S:expected[tuple(sorted(S))]=(sum(1<<i for i,b in enumerate(bits) if b),L)
    assert len(expected)==c['support_count']==(9,12,6,14)[ci]
    records=[r['source'] for r in c['covered']+c['residual']]
    assert len(records)==len(expected)
    assert {tuple(tuple(t) for t in s['stars']) for s in records}==set(expected)
    for s in records:
        key=tuple(tuple(t) for t in s['stars']);mask,L=expected[key]
        assert s['mask']==mask and canonical(sorted(L))==s['fixed_microstates']
    total+=len(expected)
    atlas=c['torus_atlas']
    if atlas is not None:
        assert tuple(atlas['A'])==A and tuple(atlas['B'])==B
        for w in atlas['witnesses']:gluing(B,w);witnesses+=1
    for r in c['covered']:
        positive+=1;rr=rows(r['source']['stars']);w=atlas['witnesses'][r['torus_index']]
        assert len(r['row_combinations'])==len(w['angle_support'])
        for t,coeff in zip(w['angle_support'],r['row_combinations']):
            identity(coeff,rr,[F(t.count(i)) for i in range(12)]+[F(2)]);angle_torus+=1
    for r in c['residual']:
        tag=r['escape'];tags[tag]+=1;S={tuple(t) for t in r['source']['stars']};rr=rows(r['source']['stars'])
        if tag=='all_angles_120_then_all_lengths_equal':
            assert ci==1 and len(S)>=12 and len(r['angle_row_combinations'])==12
            for i,coeff in enumerate(r['angle_row_combinations']):
                identity(coeff,rr,[F(j==i) for j in range(12)]+[F(2,3)]);angle120+=1
        elif tag=='five_corner_alternation_forbids_sixth_pure_vertex':
            assert ci==1 and len(S)==7
            pure={t for t in S if min(t)//6==max(t)//6};assert pure=={tuple(r['pure_star'])}
            p,=pure;assert p in ((0,0,0),(6,6,6));majority=p[0]//6
            assert all(sum(x//6==majority for x in t)==2 for t in S-pure)
        elif tag=='AB_alternation_and_connected_AB_graph':
            assert ci==1 and len(S)==6
            majority=0 if all(sum(x<6 for x in t)==2 for t in S) else 1
            assert all(sum(x//6==majority for x in t)==2 for t in S)
            bad,states=corona(B,S,r['corona'])
            assert not bad
        elif tag=='connected_certain_transition_graph':
            assert ci==2
            bad,states=corona(B,S,r['corona']);assert bad=={tuple(x) for x in r['uncertain_species_side']}
            assert bad in ({(0,2)},{(1,5)})
            if bad=={(0,2)}:
                assert tuple(r['bypass_star'])==(2,2,6) and (2,2,6) in S
                assert all(s[2][0]==2 and s[3][0]//6==1 for s in states[0])
            else:
                assert tuple(r['bypass_star'])==(0,10,10) and (0,10,10) in S
                assert all(s[5][0]==11 and s[4][0]//6==0 for s in states[1])
        elif tag=='all_corona_state_transitions_unique':
            assert ci==3
            bad,states=corona(B,S,r['corona']);assert not bad
        elif tag=='opposite_repeat_pure_B_two_face_torus':
            assert ci==3 and ((6,7,8) in S or (9,10,11) in S)
        else:raise AssertionError(tag)
assert total==41 and positive==25 and angle120==96
assert tags==Counter({'all_angles_120_then_all_lengths_equal':8,'five_corner_alternation_forbids_sixth_pure_vertex':2,'AB_alternation_and_connected_AB_graph':2,'connected_certain_transition_graph':2,'all_corona_state_transitions_unique':1,'opposite_repeat_pure_B_two_face_torus':1})
# Independent exact equiangular closure coefficients and all four row witnesses.
directions=((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
closure=[[F(sum(directions[i][axis] for i,c in enumerate(w) if c==v)) for v in range(5)] for w in (A,REPS[1]) for axis in (0,1)]
z=D['B2_equiangular_closure'];assert closure==[[F(x) for x in r] for r in z['rows']]
assert len(z['all_lengths_equal_rows'])==4
for i,co in enumerate(z['all_lengths_equal_rows'],1):identity(co,closure,[F(j==i)-F(j==0) for j in range(5)])
print(f'PASS: 12 raw equivalences, all 41 source supports, 25 positive torus implications ({angle_torus} weighted rows; {witnesses} positive gluings), 96 angle120 identities, four closure identities, all 16 residual branches')
