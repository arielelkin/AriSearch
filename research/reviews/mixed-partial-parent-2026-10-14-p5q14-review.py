#!/usr/bin/env python3
"""Fresh canonical-ring generation and forced-Q attack, from atomic geometry.

Does not import any author module and does not use raw guest placements to
generate its ring domain. Those data are used only for a final comparison.
"""
import argparse
import json
import sys
from collections import Counter
from functools import cache
from pathlib import Path
from sage.all import AA, CyclotomicField, QQ, QQbar

if sys.flags.optimize: raise RuntimeError("Assertions must be enabled")
ROOT=Path(__file__).resolve().parents[1]
K=CyclotomicField(28);z=K.gen();imaginary=z**7
embedding=K.hom([QQbar.zeta(28)],QQbar)
def bar(a):return a.conjugate()
def cross(a,b):return (bar(a)*b-a*bar(b))/(2*imaginary)
@cache
def sign(a):
    assert a==bar(a)
    val=AA(embedding(a).real())
    return 1 if val>0 else -1 if val<0 else 0

def area(F):return sum(cross(a,F[(i+1)%len(F)]) for i,a in enumerate(F))/2
@cache
def ordered(F):return F if sign(area(F))>0 else tuple(reversed(F))
@cache
def separated(F,G):
    for H,O in ((ordered(F),G),(ordered(G),F)):
        for j,a in enumerate(H):
            edge=H[(j+1)%len(H)]-a
            if all(sign(cross(edge,p-a))<=0 for p in O):return True
    return False
@cache
def strict(p,a,b):
    dot=((p-a)*bar(p-b)+(p-b)*bar(p-a))/2
    return cross(b-a,p-a)==0 and sign(dot)<0
@cache
def hasT(F,G):
    return any(strict(p,a,G[(j+1)%len(G)]) for p in F for j,a in enumerate(G)) or any(strict(p,a,F[(j+1)%len(F)]) for p in G for j,a in enumerate(F))
def identity(F):return frozenset(F)
def move(F,hand,rotation,shift):return tuple(shift+rotation*(p if hand==1 else bar(p)) for p in F)
def mate(F):
    a,b=F[4],F[0];return tuple(a+(b-a)/bar(b-a)*bar(p-a) for p in F)
def encode(a):return [str(x) for x in a.list()]+["0"]*(12-len(a.list()))
def decode(a):return sum((QQ(x)*z**i for i,x in enumerate(a)),K(0))
s=(z-z**-1)/(2*imaginary);y=2*s+4*s*s;v=1+2*s*(1-y)
assert sign(y)>0 and sign(1-y)>0 and sign(v-1)>0
P=[K(0)]
for L,e in list(zip((1,1,1,v,y),(-5,1,7,13,19)))[:-1]:P.append(P[-1]+L*z**e)
P=tuple(P);assert P[-1]+y*z**19==0
word="vvuvvuu"*2
Q=[K(0)]
for j,tag in enumerate(word[:-1]):Q.append(Q[-1]+(v if tag=="v" else 1)*z**(2*j))
Q=tuple(Q);assert Q[-1]+z**26==0
# Every native right-length/hand attachment generated from scratch.
options=[]
for j,tag in enumerate(word):
    native=3 if tag=="v" else 1;a,b=P[native],P[(native+1)%5]
    qstart,qend=Q[j],Q[(j+1)%14];here=[]
    for hand in (-1,1):
        for target_start,target_end in ((qstart,qend),(qend,qstart)):
            rotation=(target_end-target_start)/((b-a) if hand==1 else bar(b-a))
            shift=target_start-rotation*(a if hand==1 else bar(a))
            F=move(P,hand,rotation,shift)
            if sign(cross(qend-qstart,sum(F)/5-qstart))>=0:continue
            assert rotation*bar(rotation)==1 and separated(Q,F)
            far=[]
            for endpoint in (qstart,qend):
                n=F.index(endpoint)
                neighbors=(F[(n-1)%5],F[(n+1)%5])
                far.append(next(p for p in neighbors if p not in (qstart,qend)))
            here.append((F,tuple(far)))
    assert len(here)==2;options.append(here)
cycles=[]
def visit(choice):
    j=len(choice)
    if j==14:
        if options[13][choice[13]][1][1]==options[0][choice[0]][1][0]:cycles.append(tuple(choice))
        return
    for k in range(2):
        if j and options[j-1][choice[-1]][1][1]!=options[j][k][1][0]:continue
        visit(choice+[k])
visit([]);assert len(cycles)==64
counts=Counter();survivors=[]
for choice in cycles:
    ring=[Q]+[options[j][k][0] for j,k in enumerate(choice)]
    faces=ring[:];keys=set(map(identity,faces))
    for F in ring[1:]:
        M=mate(F)
        if identity(M) not in keys:faces.append(M);keys.add(identity(M))
    assert len(faces)==21
    if any(not separated(faces[a],faces[b]) for a in range(21) for b in range(a)):
        counts["mandatory_overlap"]+=1;continue
    if any(hasT(faces[a],faces[b]) for a in range(21) for b in range(a)):
        counts["mandatory_T"]+=1;continue
    groups={}
    for F in faces:
        for c,p in enumerate(F):
            group=groups.setdefault(p,[0,0,0]);group[2 if len(F)==14 else 0 if c==0 else 1]+=1
    assert all(any(all(a<=b for a,b in zip(group,star)) for star in ((2,1,0),(0,2,1))) for group in groups.values())
    survivors.append(tuple(faces));counts["survivor"]+=1
assert dict(counts)=={"mandatory_overlap":28,"mandatory_T":32,"survivor":4}
# Compare freshly generated actual patches against frozen canonical positives.
raw=json.loads((ROOT/"certificates"/"contact-pentagon-5pi7-q14-exact.json").read_text())
compact=json.loads((ROOT/"certificates"/"p5q14-orientation-transition-2026-10-14-compact.json").read_text())
row=next(r for r in raw["rows"] if r["period"]=="vvuvvuu")
assert Q==tuple(map(decode,row["Q_vertices"])) and P==tuple(map(decode,raw["source"]["P_vertices"]))
frozen_sets=[]
for cycle in compact["central_cycles"]:
    faces=[Q]
    for j,k in enumerate(cycle):
        guest=[g for g in row["raw_native_guests"][j] if g["rejection"] is None][k]
        faces.append(move(P,guest["hand"],decode(guest["rotation"]),decode(guest["shift"])))
    keys=set(map(identity,faces))
    for F in faces[1:].copy():
        M=mate(F)
        if identity(M) not in keys:faces.append(M);keys.add(identity(M))
    frozen_sets.append(frozenset(keys))
assert set(frozen_sets)=={frozenset(map(identity,F)) for F in survivors}
# The three faces needed by the compact argument agree in all4 fresh states.
F=survivors[0][6];U=survivors[0][7];M=mate(F)
assert all(state[6]==F and state[7]==U and any(H==M for H in state) for state in survivors)
a,b=F[3],F[4];fside=sign(cross(b-a,sum(F)/5-a));cases=[]
index={(r["central_state"],r["Q_hand"],r["Q_native_side"]):r for r in compact["records"]}
for state in range(4):
    physical=set()
    for hand in (-1,1):
        base=Q if hand==1 else tuple(map(bar,Q))
        for j,tag in enumerate(word):
            if tag!="v":continue
            outside=[]
            for target_start,target_end in ((a,b),(b,a)):
                rotation=(target_end-target_start)/(base[(j+1)%14]-base[j])
                shift=target_start-rotation*base[j];G=move(Q,hand,rotation,shift)
                if sign(cross(b-a,sum(G)/14-a))*fside<0:outside.append((rotation,shift,G))
            assert len(outside)==1
            rotation,shift,G=outside[0];assert rotation*bar(rotation)==1 and separated(F,G)
            pointed=[]
            for label,H in (("slot6_guest",U),("slot5_mandatory_mate",M)):
                for corner,p in enumerate(G):
                    if strict(p,H[3],H[4]):
                        ratio=(p-H[3])/(H[4]-H[3]);assert ratio in (1/v,(v-1)/v)
                        pointed.append({"host":label,"Q_corner":corner,"parameter":encode(ratio)})
            assert pointed
            rec=index[state,hand,j]
            assert rotation==z**rec["rotation_exponent"] and shift==decode(rec["shift"])
            physical.add(identity(G));cases.append({"state":state,"hand":hand,"side":j,"T_witnesses":pointed})
    assert len(physical)==4
assert len(cases)==64
report={"schema":"mixed-partial-parent-2026-10-14-fresh-p5q14-review-v1",
        "canonical_native_cycles":64,"canonical_patch_counts":dict(counts),
        "generated_placements":"native P1/P3, both hands and endpoint maps; opposite side selected geometrically",
        "cases":cases,"summary":{"outside_Q_cases":64,"strict_T_cases":64,"survivors":0},
        "scope":"Fresh displayed-Q ring and64 forced-Q cases; all28 normalization checked by separately replayed author verifier, earlier35-word classification remains a reviewed dependency."}
expected=ROOT/"certificates"/"mixed-partial-parent-2026-10-14-p5q14-review.json"
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--output",type=Path)
args=parser.parse_args()
if args.output:args.output.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
else:assert json.loads(expected.read_text())==report
print("PASS fresh geometry generation:64 canonical cycles,28 overlap+32 T+4 survivors; all64 required Q placements have T at1/v or(v-1)/v.")
