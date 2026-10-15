#!/usr/bin/env python3
"""Independent exact verifier: unequal-five adjacent-repeat theorem.
No author modules or solver imports. Rebuilds all 11160 raw words, maps,
all five exact actual supports, native full-side coronas, positive tori and
12 augmented Fraction row identities. Default reads retained evidence only.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
A = (0, 0, 1, 2, 3, 4)
REPS = ((0, 0, 1, 3, 5, 4), (2, 2, 1, 3, 0, 5), (2, 2, 4, 0, 3, 5))

def tup(x):
    return tuple(map(tup, x)) if isinstance(x, list) else x

def sides(c):
    f, i = divmod(c, 6)
    return (6*f+i, 6*f+(i+1)%6)

def ends(s):
    f, i = divmod(s, 6)
    return (6*f+(i-1)%6, 6*f+i)

def far(s, c):
    p, q = ends(s)
    assert c in (p, q)
    return q if c == p else p

def states(words):
    # A sorted triple has two cyclic readings, related by reversing ALL
    # arm choices; hence these eight independent choices cover every state.
    color = words[0] + words[1]
    out = set()
    for cs in combinations_with_replacement(range(12), 3):
        for flips in product((0, 1), repeat=3):
            arms = [sides(c)[::(-1 if b else 1)] for c,b in zip(cs, flips)]
            if any(color[arms[j][1]] != color[arms[(j+1)%3][0]] for j in range(3)):
                continue
            seams = []
            for j in range(3):
                k=(j+1)%3
                p,q=arms[j][1],arms[k][0]
                seams.append((tuple(sorted((p,q))), tuple(sorted((cs[j],cs[k]))),
                              tuple(sorted((far(p,cs[j]),far(q,cs[k]))))))
            out.add((cs,tuple(sorted(seams))))
    return out

def prune(atlas):
    atlas=set(atlas)
    while True:
        present={(slots,near) for _,ss in atlas for slots,near,remote in ss}
        remove={s for s in atlas if any((slots,remote) not in present for slots,near,remote in s[1])}
        if not remove:return atlas
        atlas-=remove

def category(atlas, sep):
    if {c for star,_ in atlas for c in star} != set(range(12)):return "no_cover"
    reach=[{i} for i in range(12)]
    for _,ss in atlas:
        for (x,y),_,_ in ss:
            merged=reach[x]|reach[y]
            for z in merged:reach[z]=merged
    return "both_joined" if 1 in reach[0] and 6+sep in reach[6] else "color_escape"

def check_map(source, target, m):
    cm={int(k):v for k,v in m["color_map"].items()}
    used=set(source[0])|set(source[1])
    assert set(cm)==used and len(set(cm.values()))==len(used)
    for f,n in enumerate(("A","B")):
        assert m[n+"_direction"] in (-1,1)
        got=tuple(cm[source[f][(m[n+"_shift"]+m[n+"_direction"]*i)%6]] for i in range(6))
        assert got==target[f]

def word_gate(d):
    records={tuple(r["B"]):r for r in d["hard_records"]}
    assert len(records)==len(d["hard_records"])==12
    observed=set(); summary=defaultdict(Counter); fixed_reps={}
    for sep in (1,2,3):
        for k in range(5):
            for common in combinations(range(5),k):
                for base in permutations(common+tuple(range(5,10-k))):
                    B=base[:sep]+(base[0],)+base[sep:]
                    observed.add((sep,B))
                    initial=states((A,B)); atlas=prune(initial)
                    kind=category(atlas,sep); summary[f"B{sep}_shared{k}"][kind]+=1
                    if kind=="both_joined":
                        r=records.pop(B)
                        assert r["shared_count"]==k and r["B_repeat_separation"]==sep
                        assert r["initial_state_count"]==len(initial)
                        assert r["fixed_state_count"]==len(atlas)
                        assert r["fixed_star_count"]==len({t for t,_ in atlas})
                        check_map((A,B),(A,tuple(r["representative"])),r["equivalence"])
    assert not records and len(observed)==11160
    assert dict(summary)==d["summary"]
    assert d["residual_raw_count"]==12 and d["residual_class_count"]==3 and d["unordered_class_count"]==2
    assert tuple(tuple(c["B"]) for c in d["classes"])==REPS
    all_members=set()
    for c in d["classes"]:
        B=tuple(c["B"]); atlas=prune(states((A,B))); fixed_reps[B]=atlas
        assert atlas==set(tup(c["fixed_states"])) and len({t for t,_ in atlas})==6
        members={tuple(w) for w in c["raw_words"]}
        assert len(members)==c["raw_word_count"]==4
        expected={tuple(r["B"]) for r in d["hard_records"] if tuple(r["representative"])==B}
        assert members==expected and not all_members&members
        all_members|=members
        check_map((B,A),(A,tuple(c["species_swap_representative"])),c["species_swap_equivalence"])
    assert set(tuple(c["species_swap_representative"]) for c in d["classes"])==set(REPS)
    print("PASS: complete 11160-word domain, 12 residual words, 3 ordered/2 unordered classes, all maps",flush=True)
    return fixed_reps

def coronas(B,S):
    colors=A+B; options=[set() for _ in range(12)]
    # Independently anchor each host sector, leaving guest order and arms free.
    for c in range(12):
        l,r=sides(c)
        for star in S:
            if c not in star:continue
            remaining=list(star);remaining.remove(c)
            for d,e in set(permutations(remaining)):
                for ds,es in product((sides(d),sides(d)[::-1]),(sides(e),sides(e)[::-1])):
                    if (colors[r],colors[ds[1]],colors[es[1]]) == (colors[ds[0]],colors[es[0]],colors[l]):
                        options[c].add(((es[1],e),(ds[0],d)))
    raw=[set(),set()]
    for f in (0,1):
        for assignment in product(*(options[6*f+i] for i in range(6))):
            record=[]
            for i in range(6):
                left=assignment[(i-1)%6][1];right=assignment[i][0]
                if left[0]!=right[0] or {left[1],right[1]}!=set(ends(left[0])):break
                record.append((left[0],left[1],right[1]))
            else:raw[f].add(tuple(record))
    def compatible(f,s,i,t):
        guest,x,y=s[i];g,j=divmod(guest,6)
        p,q=ends(guest);mapping={x:6*f+(i-1)%6,y:6*f+i}
        return t[j]==(6*f+i,mapping[p],mapping[q])
    current=[set(raw[0]),set(raw[1])]
    while True:
        nxt=[{s for s in current[f] if all(any(compatible(f,s,i,t) for t in current[s[i][0]//6]) for i in range(6))} for f in (0,1)]
        if nxt==current:break
        current=nxt
    ordered=[sorted(x) for x in current]
    choices=[[[[j for j,t in enumerate(ordered[s[i][0]//6]) if compatible(f,s,i,t)] for i in range(6)] for s in ordered[f]] for f in (0,1)]
    return dict(corner_options=[sorted(o) for o in options],initial_states=[sorted(x) for x in raw],fixed_states=ordered,neighbor_state_choices=choices)

def involutions(items):
    if not items:
        yield ();return
    first=items[0]
    for other in items[1:]:
        for rest in involutions(tuple(i for i in items[1:] if i!=other)):
            yield ((first,other),)+rest

def quotient(B,signs,pairs):
    assert sorted(x for p in pairs for x in p)==list(range(24))
    colors=[]
    for f in range(4):
        colors.extend((A,B)[f//2][i if signs[f]==1 else (-i-1)%6] for i in range(6))
    alpha={x:y for a,b in pairs for x,y in ((a,b),(b,a))}
    assert all(colors[x]==colors[y] for x,y in pairs)
    seen={0}
    while True:
        nxt=seen|{alpha[6*f+i]//6 for f in seen for i in range(6)}
        if nxt==seen:break
        seen=nxt
    if len(seen)!=4:return None
    # Cycles of boundary successor composed with edge reversal are precisely
    # the CIRCULAR vertex links; use these instead of endpoint union/find.
    successor={x:6*(alpha[x]//6)+(alpha[x]%6+1)%6 for x in range(24)}
    remaining=set(range(24));vertices=[]
    while remaining:
        x=min(remaining);cycle=[];y=x
        while y not in cycle:
            assert y in remaining
            cycle.append(y);y=successor[y]
        assert y==x
        remaining-=set(cycle);vertices.append(cycle)
    if len(vertices)!=8 or any(len(v)!=3 for v in vertices):return False
    stars=sorted(tuple(sorted(6*((c//6)//2)+(signs[c//6]*(c%6)-1)%6 for c in v)) for v in vertices)
    return stars

def positive(atlas):
    B=REPS[0];counts=Counter();supports=set()
    for tail in product((-1,1),repeat=3):
        signs=(1,)+tail;groups=defaultdict(list)
        for f in range(4):
            for i in range(6):groups[(A,B)[f//2][i if signs[f]==1 else (-i-1)%6]].append(6*f+i)
        for parts in product(*(tuple(involutions(tuple(g))) for g in groups.values())):
            pairs=sum(parts,());counts["all_pairings"]+=1
            result=quotient(B,signs,pairs)
            if result is None:continue
            counts["connected"]+=1
            if result is False:continue
            counts["trivalent_tori"]+=1;supports.add(tuple(sorted(set(result))))
    assert counts==atlas["counts"]==dict(all_pairings=22680,connected=22608,trivalent_tori=4)
    assert len(atlas["witnesses"])==2
    for w in atlas["witnesses"]:
        result=quotient(B,tuple(w["signs"]),tup(w["edge_pairs"]))
        assert result==list(tup(w["vertex_triples"]))
        assert tuple(sorted(set(result)))==tup(w["angle_support"])
    assert supports=={tup(w["angle_support"]) for w in atlas["witnesses"]}
    print("PASS: exact 22680-gluing domain, four trivalent tori, two retained positive witnesses and circular links",flush=True)

def star_row(star):return [star.count(i) for i in range(12)]+[2]

def support_gate(d,fixed_reps):
    total_rows=0
    assert tuple(tuple(c["B"]) for c in d["classes"])==REPS
    for ci,c in enumerate(d["classes"]):
        B=tuple(c["B"]);atlas=fixed_reps[B];stars=sorted({t for t,_ in atlas});accepted={}
        for n in range(7):
            for subset in combinations(stars,n):
                S=set(subset)
                if {i for t in S for i in t}!=set(range(12)):continue
                fixed=prune({s for s in atlas if s[0] in S})
                if {s[0] for s in fixed}==S:accepted[tuple(sorted(S))]=fixed
        assert len(accepted)==(3,1,1)[ci]==len(c["supports"])
        for rec in c["supports"]:
            S=tup(rec["stars"]);assert set(tup(rec["microstates"]))==accepted.pop(S)
            assert [sum(t.count(i) for t in S) for i in range(12)]==rec["corner_occurrence_counts"]
            assert Counter(sum(i//6 for i in t) for t in S)=={int(k):v for k,v in rec["vertex_species_counts"].items()}
            co=coronas(B,S)
            assert json.loads(json.dumps(co))==rec["corona"]
            if ci==0:
                implication=rec["B1_positive_torus"];assert implication is not None
                witness=d["B1_fixed_22680_positive_atlas"]["witnesses"][implication["index"]]
                rows=[[int(i<6) for i in range(12)]+[4],[int(i>=6) for i in range(12)]+[4]]+[star_row(s) for s in S]
                assert len(implication["weighted_rows"])==len(witness["angle_support"])==4
                for target,weights in zip(witness["angle_support"],implication["weighted_rows"]):
                    assert len(weights)==len(rows)
                    reconstructed=[sum(Fraction(w)*row[j] for w,row in zip(weights,rows)) for j in range(13)]
                    assert reconstructed==star_row(target);total_rows+=1
            else:
                assert rec["B1_positive_torus"] is None
                assert list(map(len,co["fixed_states"]))==([1,2] if ci==1 else [2,1])
                badslot=11 if ci==1 else 2
                expectedstar=(0,10,10) if ci==1 else (2,2,6)
                for f,ss in enumerate(co["fixed_states"]):
                    for si,s in enumerate(ss):
                        for i,choices in enumerate(co["neighbor_state_choices"][f][si]):
                            assert len(choices)==(2 if 6*f+i==badslot else 1)
                            if len(choices)>1:assert s[i][0]==badslot
                endpoint=10 if ci==1 else 2
                # Every actual uncertain edge uses the stated endpoint on
                # BOTH guests. Check the entire native seam atlas, not colors.
                for star,seams in tup(rec["microstates"]):
                    for slots,near,remote in seams:
                        if slots==(badslot,badslot):
                            assert near in ((endpoint,endpoint),(far(badslot,endpoint),)*2)
                            if near==(endpoint,endpoint):assert star==expectedstar
                assert expectedstar in S
                for star in S:
                    if endpoint in star:assert star==expectedstar
                # The other two sides incident to the bypass vertex are
                # native 4 on B2 or native 3 on A3; they are certain both ways.
                bypass=10 if ci==1 else 3
                for s in co["fixed_states"][bypass//6]:assert s[bypass%6][0]//6 != bypass//6
        assert not accepted
    assert total_rows==12
    print("PASS: all five exact supports, complete coronas, both two-edge bypasses, 12 augmented rational identities",flush=True)

if __name__=="__main__":
    gate=json.loads((ROOT/"research/certificates/hexagon-five-unequal-adjacent-recon-2026-10-15.json").read_text())
    certificate=json.loads((ROOT/"research/certificates/hexagon-five-unequal-adjacent-supports-2026-10-15.json").read_text())
    assert tuple(gate["A"])==tuple(certificate["A"])==A
    fixed_reps=word_gate(gate)
    positive(certificate["B1_fixed_22680_positive_atlas"])
    support_gate(certificate,fixed_reps)
    print("PASS: independent unequal-five adjacent-repeat finite proof inputs")
