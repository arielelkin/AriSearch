#!/usr/bin/env python3
"""Certified-family angular cut; no polygon realization assumption.
Uses the reviewed all-native complementary-ternary escape theorem. Exact
point predicate is invariant on its complete native angle type because the
five-star core equations force all paired/equivalent/complement relations.
"""
from collections import Counter
from itertools import combinations

def matchings(indices):
    indices=tuple(indices)
    if not indices:yield ();return
    first=indices[0]
    for j in indices[1:]:
        rest=tuple(k for k in indices[1:] if k!=j)
        for pairs in matchings(rest):yield ((first,j),)+pairs
MATCHINGS=tuple(matchings(range(6)))
assert len(MATCHINGS)==15

def covered(angles,grid):
    for species in (0,1):
        aa=angles[6*species:6*species+6];bb=angles[6*(1-species):6*(1-species)+6]
        c=Counter(aa)
        if len(c)!=3 or set(c.values())!={2}:continue
        if any(a<=90*grid or a==120*grid or a>=180*grid for a in c):continue
        if Counter(bb)==Counter({360*grid-2*a:2 for a in c}):return True
    return False

def add_filter(model,angles,grid):
    assert grid>0 and len(angles)==12
    for species in (0,1):
        aa=angles[6*species:6*species+6];bb=angles[6*(1-species):6*(1-species)+6]
        eq={};gt=[];lt=[];mid=[];twice=[]
        for i,j in combinations(range(6),2):
            z=model.NewBoolVar('ternary_eq_%d_%d_%d'%(species,i,j))
            model.Add(aa[i]==aa[j]).OnlyEnforceIf(z)
            model.Add(aa[i]!=aa[j]).OnlyEnforceIf(z.Not());eq[i,j]=z
        for i in range(6):
            g=model.NewBoolVar('ternary_gt90_%d_%d'%(species,i))
            model.Add(aa[i]>90*grid).OnlyEnforceIf(g)
            model.Add(aa[i]<=90*grid).OnlyEnforceIf(g.Not());gt.append(g)
            h=model.NewBoolVar('ternary_lt180_%d_%d'%(species,i))
            model.Add(aa[i]<180*grid).OnlyEnforceIf(h)
            model.Add(aa[i]>=180*grid).OnlyEnforceIf(h.Not());lt.append(h)
            z=model.NewBoolVar('ternary_mid120_%d_%d'%(species,i))
            model.Add(aa[i]==120*grid).OnlyEnforceIf(z)
            model.Add(aa[i]!=120*grid).OnlyEnforceIf(z.Not());mid.append(z)
            comp=[]
            for j in range(6):
                b=model.NewBoolVar('ternary_complement_%d_%d_%d'%(species,i,j))
                model.Add(2*aa[i]+bb[j]==360*grid).OnlyEnforceIf(b)
                model.Add(2*aa[i]+bb[j]!=360*grid).OnlyEnforceIf(b.Not());comp.append(b)
            z=model.NewBoolVar('ternary_twice_%d_%d'%(species,i))
            model.Add(sum(comp)==2).OnlyEnforceIf(z)
            model.Add(sum(comp)!=2).OnlyEnforceIf(z.Not());twice.append(z)
        for pairs in MATCHINGS:
            reps=tuple(p[0] for p in pairs)
            literals=[eq[p].Not() for p in pairs]
            literals += [eq[tuple(sorted(p))] for p in combinations(reps,2)]
            literals += [gt[i].Not() for i in reps]+[lt[i].Not() for i in reps]+[mid[i] for i in reps]+[twice[i].Not() for i in reps]
            model.AddBoolOr(literals)
    return {'native_matchings_per_species':15,'species_choices':2,'angular_escape_clauses':30,
            'scope':'All actual metrics complementary ternary paired angles, distinct/non120; no abstract SFT empty claim'}
