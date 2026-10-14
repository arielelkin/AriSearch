#!/usr/bin/env python3
"""Critical one-Q-orbit check from raw author placements, without adversary code.

Every source Q-v edge and both endpoint translations are tried geometrically;
no handedness sign formula, C verdict, candidate lattice, or shift bound is used.
"""
from functools import cache
import json
from pathlib import Path
import sys

from sage.all import AA, CyclotomicField, QQ, QQbar

ROOT=Path(__file__).resolve().parents[2]
K=CyclotomicField(28);z=K.gen();ii=z**7
embedding=K.hom([QQbar.zeta(28)],QQbar)


def decode(coefficients):
    assert len(coefficients)==12
    return sum((QQ(c)*z**j for j,c in enumerate(coefficients)),K(0))


def cross(a,b):
    q=(a.conjugate()*b-a*b.conjugate())/(2*ii)
    assert q==q.conjugate()
    return q


@cache
def sign(q):
    assert q==q.conjugate()
    a=AA(embedding(q).real())
    return 1 if a>0 else -1 if a<0 else 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled.")
    data=json.loads((ROOT/"research/certificates/contact-pentagon-5pi7-q14-exact.json").read_text())
    P=list(map(decode,data["source"]["P_vertices"]))
    v=decode(data["source"]["v"])
    assert sign(v-1)>0
    rows=cycles=completed=bridges=failed_cycles=failed_completed=0
    for row in data["rows"]:
        rows+=1
        Q=list(map(decode,row["Q_vertices"]))
        qc=sum(Q)/14
        qedges=[Q[(j+1)%14]-Q[j] for j in range(14)]
        unit=[j for j,e in enumerate(qedges) if e*e.conjugate()==1]
        vedges=[j for j,e in enumerate(qedges) if e*e.conjugate()==v*v]
        assert len(unit)==6 and len(vedges)==8
        guests=[]
        for k,raw in enumerate(row["raw_native_guests"]):
            # Recreate the author's allowed-list order using native indices,
            # rather than trusting retained rejection/verdict strings.
            expected=1 if k in unit else 3
            selected=[g for g in raw if g["native_side"]==expected]
            assert len(selected)==2 and {g["hand"] for g in selected}=={-1,1}
            faces=[]
            for g in selected:
                rotation=decode(g["rotation"]);shift=decode(g["shift"])
                assert rotation*rotation.conjugate()==1
                source=P if g["hand"]==1 else [p.conjugate() for p in P]
                F=[shift+rotation*p for p in source]
                assert {F[expected],F[(expected+1)%5]}=={Q[k],Q[(k+1)%14]}
                assert sign(cross(qedges[k],sum(F)/5-Q[k]))<0
                faces.append(F)
            guests.append(faces)
        # Cache each individual raw u guest's complete translation-mate test.
        mates={}
        for k in unit:
            for choice,F in enumerate(guests[k]):
                a,b=F[3],F[4];edge=b-a;fc=sum(F)/5
                assert edge*edge.conjugate()==v*v
                admissible=[]
                for j in vedges:
                    for endpoint in (a,b):
                        shift=endpoint-Q[j]
                        if {Q[j]+shift,Q[(j+1)%14]+shift}!={a,b}:continue
                        # Translating preserves the physical Q polygon winding;
                        # the side test automatically handles either P hand.
                        if sign(cross(edge,fc-a))*sign(cross(edge,qc+shift-a))<0:
                            admissible.append((j,shift))
                mates[k,choice]=admissible
        completed_keys={tuple(r["cycle"]) for r in row["forced_dimer_completed_patches"]}
        completed+=len(completed_keys)
        for cycle in row["disjoint_native_cycles"]:
            cycles+=1
            assert len(cycle)==14
            # Recheck actual neighboring P edge endpoints at Q vertices.
            for k in range(14):
                endpoint=Q[(k+1)%14]
                ends=[]
                for slot in (k,(k+1)%14):
                    F=guests[slot][cycle[slot]];native=F.index(endpoint)
                    other=[F[(native-1)%5],F[(native+1)%5]]
                    ends.append(next(p for p in other if p not in (Q[slot],Q[(slot+1)%14])))
                assert ends[0]==ends[1]
            failed=[k for k in unit if not mates[k,cycle[k]]]
            bridges+=len(unit)
            if tuple(cycle) in completed_keys:
                assert failed, (row["period"],cycle)
                failed_completed+=1
            failed_cycles+=bool(failed)
    assert (rows,cycles,completed,failed_completed)==(35,896,364,364)
    assert bridges==5376
    print("PASS: all 35 raw Q words, 896 native rings (including 364 dimer-valid "
          "rings), 5376 mandatory u-to-v bridges; every dimer-valid ring has an impossible "
          "translated-Q mate after all eight native v edges and both endpoint "
          "translations. No adversary verdict or lattice basis imported.")
    print("Pre-dimer rings with a failed translation bridge:",failed_cycles,"of",cycles)


if __name__=="__main__":main()
