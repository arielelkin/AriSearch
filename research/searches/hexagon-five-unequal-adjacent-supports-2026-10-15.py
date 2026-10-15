#!/usr/bin/env python3
"""UNREVIEWED author continuation: five source supports, narrow B1 positive atlas.
Reuses the prior reviewed generic four-face producer as an authoring routine;
this is NOT independent verification. Corona construction is the reviewer's
own anchored-sector algorithm. No larger quotient is searched.
"""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,argparse
HERE=Path(__file__).resolve().parent
A=(0,0,1,2,3,4)
REPS=((0,0,1,3,5,4),(2,2,1,3,0,5),(2,2,4,0,3,5))
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
native=module('unequal_adj_native',HERE/'hexagon-five-unequal-adjacent-recon-2026-10-15.py')
positive=module('reviewed_generic_positive_atlas',HERE/'hexagon-five-noncommon-fourface-2026-10-15.py')
positive.A=A
def reconstruct(W,S):
    def color(side):return W[side//6][side%6]
    opts={c:set() for c in range(12)}
    # Fix the host sector's directed arms. Enumerate both possible orders
    # of the other two occurrences and each guest sector's independent flip.
    for c in range(12):
        f,i=divmod(c,6);host=(6*f+i,6*f+(i+1)%6)
        for t in S:
            tt=list(t)
            if c not in tt:continue
            tt.remove(c)
            for d,e in set(permutations(tt)):
                for fd,fe in product((0,1),repeat=2):
                    g,j=divmod(d,6);h,k=divmod(e,6)
                    ds=(6*g+j,6*g+(j+1)%6);es=(6*h+k,6*h+(k+1)%6)
                    dl,dr=ds[fd],ds[1-fd];el,er=es[fe],es[1-fe]
                    if color(host[1])==color(dl) and color(dr)==color(el) and color(er)==color(host[0]):
                        opts[c].add(((er,e),(dl,d)))
    states=[set(),set()]
    for f in (0,1):
        for chosen in product(*(opts[6*f+i] for i in range(6))):
            signature=[]
            for i in range(6):
                j,dprev=chosen[(i-1)%6][1];k,dafter=chosen[i][0]
                if j!=k:break
                g,l=divmod(j,6)
                if {dprev,dafter}!={6*g+(l-1)%6,6*g+l}:break
                signature.append((j,dprev,dafter))
            else:states[f].add(tuple(signature))
    return opts,states

def guest_options(f,state,i,states):
    j,x,y=state[i];g,k=divmod(j,6)
    inverse={x:6*f+(i-1)%6,y:6*f+i}
    wanted=(6*f+i,inverse[6*g+(k-1)%6],inverse[6*g+k])
    return [s for s in states[g] if s[k]==wanted]

def freeze(states):return [{tuple(tuple(x) for x in s) for s in species} for species in states]

def corona(B,S):
    opts,states=reconstruct((A,B),S);initial=states
    while True:
        nxt=[{s for s in states[f] if all(guest_options(f,s,i,states) for i in range(6))} for f in (0,1)]
        if nxt==states:break
        states=nxt
    raw=[sorted(ss) for ss in states]
    choices=[]
    for f in (0,1):
        ff=[]
        for s in raw[f]:
            ff.append([[raw[s[i][0]//6].index(z) for z in guest_options(f,s,i,raw)] for i in range(6)])
        choices.append(ff)
    return {'corner_options':[sorted(opts[i]) for i in range(12)],'initial_states':[sorted(ss) for ss in initial],'fixed_states':raw,'neighbor_state_choices':choices}

def build():
    atlas=positive.torus_atlas(REPS[0]);classes=[]
    assert atlas['counts']['all_pairings']==22680
    for ci,B in enumerate(REPS):
        M=native.fixed(native.generate((A,B)));stars=sorted({t for t,ss in M});records=[]
        for bits in product((False,True),repeat=len(stars)):
            S={t for t,b in zip(stars,bits) if b}
            if {c for t in S for c in t}!=set(range(12)):continue
            L=native.fixed({state for state in M if state[0] in S})
            if {t for t,ss in L}!=S:continue
            src=sorted(S);rr=[[F(i<6) for i in range(12)]+[F(4)],[F(i>=6) for i in range(12)]+[F(4)]]+[positive.row(t) for t in src]
            witness=None
            if ci==0:
                bs=positive.basis(rr)
                for wi,w in enumerate(atlas['witnesses']):
                    co=[positive.express(positive.row(t),bs,len(rr)) for t in w['angle_support']]
                    if all(v is not None for v in co):witness={'index':wi,'weighted_rows':co};break
            records.append({'stars':src,'microstates':sorted(L),'vertex_species_counts':dict(Counter(sum(c//6 for c in t) for t in S)),'corner_occurrence_counts':[sum(t.count(i) for t in S) for i in range(12)],'corona':corona(B,S),'B1_positive_torus':witness})
        classes.append({'B':B,'supports':records})
    assert [len(c['supports']) for c in classes]==[3,1,1]
    return {'schema':'UNEQUAL_ADJACENT_FIVE_SOURCE_SUPPORT_RECON_V1','status':'UNREVIEWED_AUTHOR_RECONNAISSANCE','A':A,'classes':classes,'B1_fixed_22680_positive_atlas':atlas,'scope':'Only five exact source-support cases and a justified B1 2A2B positive domain. No larger quotient search; no aperiodicity/main-problem claim.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');p.add_argument('--summary',action='store_true');a=p.parse_args();d=build();encoded=json.dumps(d,sort_keys=True,indent=2)+'\n'
    if a.output:Path(a.output).write_text(encoded)
    if a.summary:
        print('B1 atlas',d['B1_fixed_22680_positive_atlas']['counts'],'patterns',len(d['B1_fixed_22680_positive_atlas']['witnesses']))
        for c in d['classes']:
            for s in c['supports']:
                co=s['corona'];print('B',c['B'],'stars',len(s['stars']),'states',list(map(len,co['fixed_states'])),'torus',s['B1_positive_torus'] is not None,'guest_counts',[[[len(x) for x in ss] for ss in f] for f in co['neighbor_state_choices']])
    else:print(encoded,end='')
